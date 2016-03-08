# -*- coding: utf-8 -*-

import re
import geojson
from gatilegrid.grid import Grid

from pyramid.view import view_config
from pyramid.renderers import render, render_to_response
from pyramid.response import Response
import pyramid.httpexceptions as exc

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import InternalError, DataError
from sqlalchemy.sql.expression import cast, func
from sqlalchemy import Text, Integer, Boolean, Numeric, Date
from sqlalchemy import text
from geoalchemy2.types import Geometry

from chsdi.lib.validation.mapservice import MapServiceValidation
from chsdi.lib.helpers import format_query, extend_box2d
from chsdi.lib.filters import full_text_search
from chsdi.models import models_from_bodid, queryable_models_from_bodid, oereb_models_from_bodid
from chsdi.models.clientdata_dynamodb import get_bucket
from chsdi.models.bod import OerebMetadata, get_bod_model
from chsdi.models.vector import getToleranceMeters
from chsdi.models.grid import get_grid_spec, get_grid_layer_timestamp, get_grid_layer_template
from chsdi.views.layers import get_layer, get_layers_metadata_for_params

PROTECTED_GEOMETRY_LAYERS = ['ch.bfs.gebaeude_wohnungs_register']


# For several features
class FeatureParams(MapServiceValidation):

    def __init__(self, request):
        super(FeatureParams, self).__init__()
        # Map and topic represent the same resource
        self.mapName = request.matchdict.get('map')
        self.hasMap(request.db, self.mapName)
        self.cbName = request.params.get('callback')
        self.lang = request.lang
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.returnGeometry = request.params.get('returnGeometry')
        self.translate = request.translate
        self.request = request
        self.varnish_authorized = request.headers.get('X-SearchServer-Authorized', 'false').lower() == 'true'

# for releases requests


def _get_releases_params(request):
    params = FeatureParams(request)
    params.imageDisplay = request.params.get('imageDisplay')
    params.mapExtent = request.params.get('mapExtent')
    params.geometry = request.params.get('geometry')
    params.geometryType = request.params.get('geometryType')
    params.layer = request.matchdict.get('layerId')
    return params

# For identify services


def _get_features_params(request):
    params = FeatureParams(request)
    # where must come first order matters, see MapServiceValidation
    params.where = request.params.get('where')
    params.searchText = request.params.get('searchText')
    params.geometry = request.params.get('geometry')
    params.geometryType = request.params.get('geometryType')
    params.imageDisplay = request.params.get('imageDisplay')
    params.mapExtent = request.params.get('mapExtent')
    params.tolerance = request.params.get('tolerance')
    params.layers = request.params.get('layers', 'all')
    params.timeInstant = request.params.get('timeInstant')
    params.offset = request.params.get('offset')
    params.limit = request.params.get('limit')
    params.order = request.params.get('order')
    return params


# For feature, htmlPopup and extendedHtmlPopup services
def _get_feature_params(request):
    params = FeatureParams(request)
    params.layerId = request.matchdict.get('layerId')
    params.featureIds = request.matchdict.get('featureId')
    return params


def _get_find_params(request):
    params = FeatureParams(request)
    params.layer = request.params.get('layer')
    params.searchText = request.params.get('searchText')
    params.searchField = request.params.get('searchField')
    params.contains = request.params.get('contains')
    return params


def _get_attributes_params(request):
    params = FeatureParams(request)
    params.layerId = request.matchdict.get('layerId')
    params.attribute = request.matchdict.get('attribute')

    return params


@view_config(route_name='identify', request_param='geometryFormat=interlis')
def identify_oereb(request):
    return _identify_oereb(request)


@view_config(route_name='identify', renderer='geojson', request_param='geometryFormat=geojson')
def identify_geojson(request):
    return _identify(request)


@view_config(route_name='identify', renderer='esrijson')
def identify_esrijson(request):
    return _identify(request)


@view_config(route_name='feature', renderer='geojson',
             request_param='geometryFormat=geojson')
def view_get_feature_geojson(request):
    return _get_feature_service(request)


@view_config(route_name='feature', renderer='esrijson')
def view_get_feature_esrijson(request):
    return _get_feature_service(request)


# order matters, last route is the default one!
@view_config(route_name='find', renderer='geojson',
             request_param='geometryFormat=geojson')
def view_find_geojson(request):
    return _find(request)


@view_config(route_name='find', renderer='esrijson')
def view_find_esrijson(request):
    return _find(request)


@view_config(route_name='attribute_values', renderer='geojson')
def view_attribute_values_geojson(request):
    return _attributes(request)


@view_config(route_name='htmlPopup', renderer='jsonp')
def htmlpopup(request):
    params = _get_feature_params(request)
    params.returnGeometry = False
    feature, vectorModel = next(_get_features(params))

    layerModel = get_bod_model(params.lang)
    layer = next(get_layers_metadata_for_params(
        params,
        request.db.query(layerModel),
        layerModel,
        layerIds=[params.layerId]
    ))
    feature.update({'attribution': layer.get('attributes')['dataOwner']})
    feature.update({'fullName': layer.get('fullName')})
    feature.update({'extended': False})

    response = _render_feature_template(vectorModel, feature, request)

    if params.cbName is None:
        return response
    return response.body


@view_config(route_name='extendedHtmlPopup', renderer='jsonp')
def extendedhtmlpopup(request):
    params = _get_feature_params(request)
    params.returnGeometry = True
    feature, vectorModel = next(_get_features(params))

    layerModel = get_bod_model(params.lang)
    layer = next(get_layers_metadata_for_params(
        params,
        request.db.query(layerModel),
        layerModel,
        layerIds=[params.layerId]
    ))
    feature.update({'attribution': layer.get('attributes')['dataOwner']})
    feature.update({'fullName': layer.get('fullName')})
    feature.update({'extended': True})

    response = _render_feature_template(vectorModel, feature, request, True)

    if params.cbName is None:
        return response
    return response.body


def _identify_oereb(request):
    def insertTimestamps(header, comments):
        pos = re.search(r'\?>', header).end()
        return ''.join((
            header[:pos],
            comments,
            header[pos:]
        ))

    params = _get_features_params(request)
    # At the moment only one layer at a time and no support of all
    if params.layers == 'all' or len(params.layers) > 1:
        raise exc.HTTPBadRequest('Please specify the id of the layer you want to query')
    layerBodId = params.layers[0]
    query = params.request.db.query(OerebMetadata)
    layerMetadata = get_layer(
        query,
        OerebMetadata,
        layerBodId
    )
    header = layerMetadata.header
    footer = layerMetadata.footer
    data_created = layerMetadata.data_created
    data_imported = layerMetadata.data_imported

    comments = render(
        'chsdi:templates/oereb_timestamps.mako',
        {
            'data_imported': data_imported,
            'data_created': data_created
        }
    )
    header = insertTimestamps(header, comments)

    # Only relation 1 to 1 is needed at the moment
    layerVectorModel = [{layerBodId: [oereb_models_from_bodid(layerBodId)[0]]}]
    features = []
    for feature in _get_features_for_filters(params, layerVectorModel):
        temp = feature.xmlData.split('##')
        for fragment in temp:
            if fragment not in features:
                features.append(fragment)
    results = ''.join((
        header,
        ''.join(features),
        footer
    ))
    response = Response(results)
    response.content_type = 'text/xml'
    return response


def _identify(request):
    params = _get_features_params(request)
    # Determine layer types
    layersGrid = []
    layersDB = []

    if params.layers == 'all':
        model = get_bod_model(params.lang)
        query = params.request.db.query(model)
        layerBodIds = []
        for layer in get_layers_metadata_for_params(params, query, model):
            layerBodId = layer['layerBodId']
            models = models_from_bodid(layerBodId)
            if models:
                layersDB.append({layerBodId: models})
            else:
                gridSpec = get_grid_spec(layerBodId)
                if gridSpec:
                    layersGrid.append({layerBodId: gridSpec})
    else:
        layerBodIds = params.layers
        for layerBodId in layerBodIds:
            gridSpec = get_grid_spec(layerBodId)
            if gridSpec:
                layersGrid.append({layerBodId: gridSpec})
            else:
                models = models_from_bodid(layerBodId)
                if models is None:
                    raise exc.HTTPBadRequest('No GeoTable was found for %s' % layerBodId)
                layersDB.append({layerBodId: models})

    featuresGrid = _identify_grid(params, layersGrid)
    featuresDB = _identify_db(params, layersDB)

    return {'results': featuresGrid + featuresDB}


def _identify_grid(params, layerBodIds):
    features = []
    if len(layerBodIds) == 0:
        return features
    maxFeatures = 11
    mapExtent = params.mapExtent
    imageDisplay = params.imageDisplay
    tolerance = params.tolerance
    geometry = params.geometry
    # TODO support min/max scale and min/max resolution?
    toleranceMeters = getToleranceMeters(imageDisplay, mapExtent, tolerance)

    # TODO check the geometry type as we only support bbox and points
    # intersection for grid types
    extent = geometry.coordinates
    if len(extent) == 2:
        extent = extent + extent
        extent = extend_box2d(extent, toleranceMeters)
    elif len(extent) == 4:
        extent = extend_box2d(extent, toleranceMeters)
    else:
        return features

    # TODO change bucket and profile names
    bucket = get_bucket(profile_name='ltgal_aws_admin', bucket_name='waf-wmts-test')
    for layer in layerBodIds:
        [layerBodId, gridSpec] = next(layer.iteritems())
        timestamp = get_grid_layer_timestamp(layerBodId)
        grid = Grid(gridSpec.get('extent'),
                    gridSpec.get('resolutionX'),
                    gridSpec.get('resolutionY'))
        [colFrom, rowFrom, colTo, rowTo] = grid.getExtentAddress(extent)
        for col in xrange(colFrom, colTo + 1):
            for row in xrange(rowFrom, rowTo + 1):
                if len(features) >= maxFeatures:
                    return features

                featureS3KeyName = 'tooltip/%s/default/%s/%s/%s/data.json' % (layerBodId, timestamp, col, row)
                featureS3Key = bucket.get_key(featureS3KeyName)
                # Fail gracefully if the key doesn't exist
                if featureS3Key:
                    featureJson = featureS3Key.get_contents_as_string()
                    # Beacause of esriJSON design and papyrus no esrijson support for now
                    feature = geojson.loads(featureJson)
                    if not params.returnGeometry:
                        del feature['geometry']
                    feature['layerBodId'] = layerBodId
                    feature['layerName'] = params.translate(layerBodId)
                    features.append(feature)

    return features


def _identify_db(params, layerBodIds):
    features = []
    if len(layerBodIds) == 0:
        return features
    maxFeatures = 201
    feature_gen = _get_features_for_filters(
        params, layerBodIds, maxFeatures=maxFeatures, where=params.where)
    while len(features) <= maxFeatures:
        try:
            feature = next(feature_gen)
        except InternalError as e:
            raise exc.HTTPBadRequest('Your request generated the following database error: %s' % e)
        except StopIteration:
            break
        else:
            features.append(_process_feature(feature, params))
    return features


def _get_feature_service(request):
    params = _get_feature_params(request)
    features = []
    for feature, vectorModel in _get_features(params):
        features.append(feature)
    if len(features) == 1:
        return features[0]
    return features


def _get_features(params, extended=False):
    ''' Returns exactly one feature or raises
    an excpetion '''
    featureIds = params.featureIds.split(',')
    gridSpec = get_grid_spec(params.layerId)
    if not gridSpec:
        models = models_from_bodid(params.layerId)
        if models is None:
            raise exc.HTTPBadRequest('No Vector Table was found for %s' % params.layerId)

    for featureId in featureIds:
        if gridSpec:
            # By convention
            # TODO change bucket and profile names
            bucket = get_bucket(profile_name='ltgal_aws_admin', bucket_name='waf-wmts-test')
            col, row = featureId.split('_')
            grid = Grid(gridSpec.get('extent'),
                        gridSpec.get('resolutionX'),
                        gridSpec.get('resolutionY'))
            timestamp = get_grid_layer_timestamp(params.layerId)
            yield _get_feature_grid(col, row, timestamp, grid, bucket, params)
        else:
            yield _get_feature_db(featureId, params, models)


def _get_feature_db(featureId, params, models):
    # One layer can have several models
    for model in models:
        query = params.request.db.query(model)
        query = query.filter(model.id == featureId)
        try:
            feature = query.one()
        except (NoResultFound, DataError):
            feature = None
        except MultipleResultsFound:
            raise exc.HTTPInternalServerError('Multiple features found for the same id %s' % featureId)

        if feature is not None:
            vectorModel = model
            break

    if feature is None:
        raise exc.HTTPNotFound('No feature with id %s' % featureId)
    feature = _process_feature(feature, params)
    feature = {'feature': feature}
    return feature, vectorModel


def _get_feature_grid(col, row, timestamp, grid, bucket, params):
    feature = None
    col = str(col)
    row = str(row)
    timestamp = str(timestamp)
    layerBodId = params.layerId
    featureS3KeyName = 'tooltip/%s/default/%s/%s/%s/data.json' % (layerBodId, timestamp, col, row)
    featureS3Key = bucket.get_key(featureS3KeyName)
    # Fail gracefully if the key doesn't exist
    if featureS3Key:
        featureJson = featureS3Key.get_contents_as_string()
        # Beacause of esriJSON design and papyrus no esrijson support for now
        feature = geojson.loads(featureJson)
        if not params.returnGeometry:
            del feature['geometry']
        feature['layerBodId'] = layerBodId
        feature['layerName'] = params.translate(layerBodId)
    return feature, None


def _render_feature_template(vectorModel, feature, request, extended=False):
    if vectorModel:
        hasExtendedInfo = True if hasattr(vectorModel, '__extended_info__') else False
        if extended and not hasExtendedInfo:
            raise exc.HTTPNotFound('No extended info has been found for %s' % vectorModel.__bodId__)
        template = vectorModel.__template__
    else:
        hasExtendedInfo = False
        template = get_grid_layer_template(feature['layerBodId'])
    return render_to_response(
        'chsdi:%s' % template,
        {
            'feature': feature,
            'hasExtendedInfo': hasExtendedInfo
        },
        request=request)


def _get_features_for_filters(params, layerBodIds, maxFeatures=None, where=None):
    ''' Returns a generator function that yields
    a feature. '''
    for layer in layerBodIds:
        layerBodId, models = next(layer.iteritems())
        if where is not None:
            vectorLayer = []
            for model in models:
                txt = format_query(model, where)
                if txt is not None:
                    vectorLayer.append((model, txt))
            if len(vectorLayer) == 0:
                raise exc.HTTPBadRequest('The where clause is not valid for %s.' % layerBodId)
        else:
            vectorLayer = [(model, None) for model in models]

        for model, where_txt in vectorLayer:
            query = params.request.db.query(model)
            # Filter by sql query
            # Only one filter = one layer
            if where_txt is not None:
                query = query.filter(text(
                    where_txt
                ))
            # Filter by bbox
            if params.geometry is not None:
                geomFilter = model.geom_filter(
                    params.geometry,
                    params.geometryType,
                    params.imageDisplay,
                    params.mapExtent,
                    params.tolerance
                )
                # Can be None because of max and min scale
                if geomFilter is not None:
                    # TODO Remove code specific clauses
                    ordering = model.bgdi_order if hasattr(model, 'bgdi_order') else None
                    if params.order == 'distance':
                        ordering = model.order_by_distance(
                            params.geometry,
                            params.geometryType,
                            params.imageDisplay,
                            params.mapExtent,
                            params.tolerance
                        )
                    query = query.order_by(ordering) if ordering is not None else query
                    query = query.filter(geomFilter)

            # Filter by time instant
            if params.timeInstant is not None and hasattr(model, '__timeInstant__'):
                timeInstantColumn = model.time_instant_column()
                query = query.filter(timeInstantColumn == params.timeInstant)

            # Add limit
            limits = [x for x in [maxFeatures, params.limit] if x is not None]
            flimit = min(limits) if len(limits) > 0 else None
            query = query.limit(flimit) if flimit is not None else query

            # Add offset
            if params.offset is not None:
                query = query.offset(params.offset)

            # We need either where or geomFilter (geomFilter especially for zeitreihen layer)
            # This probably needs refactoring...
            if where is not None or geomFilter is not None:
                # TODO remove layer specific code
                if model.__bodId__ == 'ch.swisstopo.zeitreihen':
                    counter = 0
                    bgdi_order = 0
                    for feature in query:
                        counter += 1
                        if counter > 1:
                            if bgdi_order < feature.bgdi_order:
                                continue
                        bgdi_order = feature.bgdi_order
                        yield feature
                else:
                    for feature in query:
                        yield feature


def _attributes(request):
    ''' This service exposes preview values based on a layer Id
    and an attribute name (mapped in the model) '''
    MAX_ATTR_VALUES = 50
    attributesValues = []
    params = _get_attributes_params(request)

    models = models_from_bodid(params.layerId)

    if models is None:
        raise exc.HTTPBadRequest('No Vector Table was found for %s' % params.layerId)

    # Check that the attribute provided is found at least in one model
    modelToQuery = None
    for model in models:
        attributes = model().getAttributesKeys()
        if params.attribute in attributes:
            modelToQuery = model
            break
    if modelToQuery is None:
        raise exc.HTTPBadRequest('No attribute %s was found for %s' % (params.attribute, params.layerId))

    col = modelToQuery.get_column_by_property_name(params.attribute)
    colType = str(col.type)
    if colType in ['DATE', 'INTEGER', 'NUMERIC']:
        query = request.db.query(func.max(col).label('max'), func.min(col).label('min'))
        res = query.one()
        return {'values': [res.min, res.max]}
    else:
        query = request.db.query(col).distinct().order_by(col)
        query = query.limit(MAX_ATTR_VALUES)
        for attr in query:
            if len(attr):
                attributesValues.append(attr[0])
        return {'values': sorted(attributesValues)}


def _find(request):
    MaxFeatures = 50
    params = _get_find_params(request)
    if params.searchText is None:
        raise exc.HTTPBadRequest('Please provide a searchText')

    models = queryable_models_from_bodid(params.layer, params.searchField)
    features = []
    if models is None:
        raise exc.HTTPBadRequest(
            'No Vector Table was found for %s for searchField %s' % (params.layer, params.searchField))

    for model in models:
        searchColumn = model.get_column_by_property_name(params.searchField)
        query = request.db.query(model)
        if params.contains:
            query = full_text_search(
                query,
                [searchColumn],
                params.searchText
            )
        else:
            if isinstance(searchColumn.type, Date):
                query = query.filter(
                    cast(searchColumn, Date) == params.searchText
                )
            else:
                searchText = _format_search_text(searchColumn.type, params.searchText)
                query = query.filter(
                    searchColumn == searchText
                )
        query = query.limit(MaxFeatures)
        for feature in query:
            f = _process_feature(feature, params)
            features.append(f)

    return {'results': features}


def _format_search_text(columnType, searchText):
    if isinstance(columnType, Text):
        return searchText
    elif isinstance(columnType, Boolean):
        if searchText.lower() == 'true':
            return True
        elif searchText.lower() == 'false':
            return False
        else:
            raise exc.HTTPBadRequest('Please provide a boolean value (true/false)')
    elif isinstance(columnType, Integer):
        if searchText.isdigit():
            return int(searchText)
        else:
            raise exc.HTTPBadRequest('Please provide an integer')
    elif isinstance(columnType, Numeric):
        if re.match('^\d+?\.\d+?$', searchText) is not None:
            return float(searchText)
        else:
            raise exc.HTTPBadRequest('Please provide a float')
    elif isinstance(columnType, Geometry):
        raise exc.HTTPBadRequest('Find operations cannot be performed on geometry columns')


def has_long_geometry(feature):
    return bool(len(getattr(feature, feature.geometry_column_to_return().name).data) > 1000000)


def _process_feature(feature, params):
    # TODO find a way to use translate directly in the model
    if params.returnGeometry and not has_long_geometry(feature):
        f = feature.__geo_interface__
        # Filter out this layer individually, disregarding of the global returnGeometry
        # setting
        if not params.varnish_authorized:
            if hasattr(params, 'layers') and feature.__bodId__ in PROTECTED_GEOMETRY_LAYERS:
                f = feature.__interface__
            if hasattr(params, 'layer') and params.layer in PROTECTED_GEOMETRY_LAYERS:
                f = feature.__interface__
            if hasattr(params, 'layerId') and params.layerId in PROTECTED_GEOMETRY_LAYERS:
                f = feature.__interface__
    else:
        f = feature.__interface__
    if hasattr(f, 'extra'):
        layerBodId = f.extra['layerBodId']
        f.extra['layerName'] = params.translate(layerBodId)
    else:
        layerBodId = f.get('layerBodId')
        f['layerName'] = params.translate(layerBodId)
    return f


@view_config(route_name='releases', renderer='geojson')
def releases(request):
    params = _get_releases_params(request)
    # For this sevice, we have to use different models based
    # on specially sorted views. We add the _meta part to the given
    # layer name
    # Note that only zeitreihen is currently supported for this service
    layerMetaId = params.layer + '_meta'
    models = models_from_bodid(layerMetaId)
    if models is None:
        raise exc.HTTPBadRequest('No Vector Table was found for %s' % params.layer)

    # Default timestamp
    timestamps = []
    minYear = 9999
    for f in _get_features_for_filters(params, [{layerMetaId: models}]):
        if hasattr(f, 'release_year') and f.release_year is not None:
            for x in f.release_year:
                if int(x) < minYear:
                    timestamps.append(str(x))
                    minYear = int(x)

    if len(timestamps) > 0:
        # remove duplicates
        timestamps = list(set(timestamps))
        # add day to have full timestamp
        timestamps = sorted([int(ts + '1231') for ts in timestamps])
        # transform back to string
        timestamps = [str(ts) for ts in timestamps]

    return {'results': timestamps}
