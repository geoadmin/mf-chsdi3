# -*- coding: utf-8 -*-

import os
import decimal
import six
import datetime
from itertools import chain


from pyramid.view import view_config
from pyramid.renderers import render_to_response
import pyramid.httpexceptions as exc

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from chsdi.lib.validation import BaseLayersValidation
from chsdi.models import models_from_bodid, get_models_attributes_keys
from chsdi.models.bod import LayersConfig, get_bod_model, computeHeader, CacheUpdate
from chsdi.lib.filters import full_text_search, filter_by_geodata_staging, filter_by_map_name

SAMPLE_SIZE = 100
MAX_ATTRIBUTES_VALUES = 5


@view_config(route_name='mapservice', renderer='jsonp')
def metadata(request):
    params = BaseLayersValidation(request)
    model = get_bod_model(params.lang)
    query = params.request.db.query(model)
    query = _filter_on_chargeable_attr(params, query, model)
    if params.searchText is not None:
        query = full_text_search(
            query,
            [
                model.fullTextSearch,
                model.layerBodId,
                model.idGeoCat
            ],
            params.searchText
        )
    results = computeHeader(params.mapName, params.srid)
    for layer in get_layers_metadata_for_params(params, query, model):
        results['layers'].append(layer)
    return results


@view_config(route_name='layersConfig', renderer='jsonp')
def layers_config(request):
    params = BaseLayersValidation(request)
    query = params.request.db.query(LayersConfig)
    layers = {}
    # Python 2/3
    for layer in get_layers_config_for_params(params, query, LayersConfig):
        # layers = dict(list(layers.items()) + list(layer.items()))
        layers = dict(chain(layers.items(), layer.items()))

    return layers


@view_config(route_name='legend', renderer='jsonp')
def legend(request):
    params = BaseLayersValidation(request)
    layerId = request.matchdict.get('layerId')
    model = get_bod_model(params.lang)
    query = params.request.db.query(model)
    layerMetadata = next(get_layers_metadata_for_params(
        params,
        query,
        model,
        layerIds=[layerId]
    ))
    # FIXME datenstand if not defined
    # should be available in view_bod_layer_info
    if 'attributes' in layerMetadata:
        if 'dataStatus' in layerMetadata['attributes']:
            status = layerMetadata['attributes']['dataStatus']
            if status == u'bgdi_created':
                layerMetadata['attributes']['dataStatus'] = params.translate('None') + params.translate('Datenstand')
    legend = {
        'layer': layerMetadata,
        'hasLegend': _has_legend(layerId, params.lang)
    }
    response = render_to_response(
        'chsdi:templates/legend.mako',
        {'legend': legend},
        request=request
    )
    if params.cbName is None:
        return response
    if six.PY3:
        return response.body.decode('utf8')
    return response.body


def _find_type(model, colProp):
    if hasattr(model, '__table__') and hasattr(model, colProp):
        return model.get_column_by_property_name(colProp).type


# Could be moved in features.py as it accesses vector models
@view_config(route_name='featureAttributes', renderer='jsonp')
def feature_attributes(request):
    ''' This service is used to expose the
    attributes of vector layers. '''
    params = BaseLayersValidation(request)
    layerId = request.matchdict.get('layerId')
    models = models_from_bodid(layerId, srid=params.srid)
    # Models for the same layer have the same attributes
    if models is None:
        raise exc.HTTPBadRequest('No Vector Table was found for %s' % layerId)

    # Take into account all models and remove duplicated keys
    attributes = get_models_attributes_keys(models, params.lang, False)
    trackAttributesNames = []
    fields = []

    def insert_value_at(field, attrName, value):
        if field['name'] == attrName:
            if len(field['values']) < MAX_ATTRIBUTES_VALUES and \
               value not in field['values']:
                field['values'].append(value)
                field['values'].sort()
        return field

    for model in models:
        query = params.request.db.query(model)
        query = query.limit(SAMPLE_SIZE)

        for rowIndex, row in enumerate(query):
            # attrName as defined in the model
            for attrIndex, attrName in enumerate(attributes):
                featureAttrs = row.get_attributes(exclude_pkey=False)
                if attrName not in trackAttributesNames and \
                   attrName in featureAttrs:
                    fieldType = _find_type(model(), attrName)
                    fields.append({'name': attrName, 'type': str(fieldType),
                                   'alias': params.translate("%s.%s" % (layerId, attrName)),
                                   'values': []
                                   })
                    trackAttributesNames.append(attrName)
                if attrName in featureAttrs:
                    for fieldsIndex, field in enumerate(fields):
                        value = featureAttrs[attrName]
                        if isinstance(value, (decimal.Decimal, datetime.date, datetime.datetime)):
                            value = str(value)
                        fields[fieldsIndex] = insert_value_at(field, attrName, value)

    return {'id': layerId, 'name': params.translate(layerId), 'fields': fields}


@view_config(route_name='faqlist', renderer='jsonp')
def faqlist(request):
    params = BaseLayersValidation(request)
    params.geodataStaging = 'prod'
    translations = {}

    # That there is a tooltip
    tooltipLayers = []
    # That you can search in layer search
    searchableLayers = []
    # That you need to pay for
    chargeableLayers = []
    # Free layers
    notChargeableLayers = []
    # queryable layer (filtering with where and layerDefs)
    queryableLayers = []

    query = params.request.db.query(LayersConfig)
    for layer in get_layers_config_for_params(params, query, LayersConfig):
        # Python2/3
        k = list(layer.keys()).pop()
        lyr = list(layer.values()).pop()
        if 'parentLayerId' not in lyr and not k.endswith('_3d'):
            if k not in translations:
                translations[k] = request.translate(k)
            if 'tooltip' in lyr and lyr['tooltip']:
                tooltipLayers.append(k)
            if 'queryableAttributes' in lyr and lyr['queryableAttributes']:
                queryableLayers.append(k)
            if 'searchable' in lyr and lyr['searchable']:
                searchableLayers.append(k)
            if 'chargeable' in lyr and lyr['chargeable']:
                chargeableLayers.append(k)
            if 'chargeable' in lyr and not lyr['chargeable']:
                notChargeableLayers.append(k)

    return {
        'translations': translations,
        'tooltipLayers': sorted(tooltipLayers),
        'searchableLayers': sorted(searchableLayers),
        'chargeableLayers': sorted(chargeableLayers),
        'notChargeableLayers': sorted(notChargeableLayers),
        'queryableLayers': sorted(queryableLayers)
    }


def _has_legend(layerId, lang):
    legendsDir = os.path.join(os.path.dirname(__file__), '../static/images/legends')
    image = "%s_%s.png" % (layerId, lang)
    imageFullPath = os.path.abspath(os.path.join(legendsDir, image))
    return os.path.exists(imageFullPath)


def _filter_on_chargeable_attr(params, query, model):
    ''' Filter on chargeable parameter '''
    if params.chargeable is not None:
        return query.filter(model.chargeable == params.chargeable)
    return query


def get_layer(query, model, layerId):
    ''' Returns exactly one layer or raises
    an exception. This function can be used with
    both a layer config model or a layer metadata
    model. '''
    query = query.filter(model.layerBodId == layerId)

    try:
        layer = query.one()
    except NoResultFound:
        raise exc.HTTPNotFound('No layer with id %s' % layerId)
    except MultipleResultsFound:  # pragma: no cover
        raise exc.HTTPInternalServerError('Multiple layers found for the same id %s' % layerId)

    return layer


def get_layers_metadata_for_params(params, query, model, layerIds=None):
    ''' Returns a generator function that yields
    layer metadata dictionaries. '''
    query = filter_by_map_name(
        query,
        model,
        params.mapName
    )
    query = filter_by_geodata_staging(
        query,
        model.staging,
        params.geodataStaging
    )
    if layerIds is not None:
        for layerId in layerIds:
            layer = get_layer(query, model, layerId)
            yield layer.layerMetadata()

    for q in query:
        yield q.layerMetadata()


def get_layers_config_for_params(params, query, model):
    ''' Returns a generator function that yields
    layer config dictionaries. '''
    model = LayersConfig
    query = filter_by_map_name(
        query,
        model,
        params.mapName
    )
    query = filter_by_geodata_staging(
        query,
        model.staging,
        params.geodataStaging
    )

    for q in query:
        yield q.layerConfig(params)


@view_config(route_name='cacheUpdate', renderer='geojson')
def cacheUpdate(request):
    params = BaseLayersValidation(request)
    layerId = request.matchdict.get('layerId')
    model = CacheUpdate
    query = params.request.db.query(model)

    query = query.filter(model.id == layerId)

    try:
        layer = query.one()
    except NoResultFound:
        raise exc.HTTPNotFound('No layer with id %s' % layerId)
    except MultipleResultsFound:  # pragma: no cover
        raise exc.HTTPInternalServerError('Multiple layers found for the same id %s' % layerId)

    return {
        'cache_type': layer.cache_type,
        'cache_update': layer.cache_modified
    }
