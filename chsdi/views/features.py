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
from sqlalchemy import Text, Unicode, Integer, Boolean, Numeric, Date
from sqlalchemy import text
from geoalchemy2.types import Geometry

from chsdi.lib.validation.features import HtmlPopupServiceValidation, ExtendedHtmlPopupServiceValidation, GetFeatureServiceValidation, AttributesServiceValidation
from chsdi.lib.validation.find import FindServiceValidation
from chsdi.lib.validation.identify import IdentifyServiceValidation
from chsdi.lib.helpers import format_query, decompress_gzipped_string, center_from_box2d, make_geoadmin_url, shift_to, unnacent_where_text
from chsdi.lib.filters import full_text_search
from chsdi.models.s3_client import get_file_from_bucket
from chsdi.models import models_from_bodid, queryable_models_from_bodid, oereb_models_from_bodid
from chsdi.models.bod import OerebMetadata, get_bod_model
from chsdi.models.vector import get_scale, get_resolution, has_buffer
from chsdi.models.grid import get_grid_spec, get_grid_layer_properties
from chsdi.views.layers import get_layer, get_layers_metadata_for_params
from chsdi.lib.helpers import _transform_coordinates, transform_round_geometry


import logging
logger = logging.getLogger(__name__)

MAX_FEATURES = 201


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


def _get_feature_info_for_popup(request, params, isExtended=False, isIframe=False):
    feature, vector_model = next(_get_features(params))
    layerModel = get_bod_model(params.lang)
    # TODO Remove this ugly hack
    layer = next(get_layers_metadata_for_params(
        params,
        request.db.query(layerModel),
        layerModel,
        layerIds=[params.layerId if params.layerId != 'ch.bfs.gebaeude_wohnungs_register_preview' else 'ch.bfs.gebaeude_wohnungs_register']
    ))
    options = {}
    if 'feature' in feature:
        options.update(feature.pop('feature'))
    else:
        options.update(feature)

    # Regular html popup don't return a geometry
    if 'properties' in options:
        if hasattr(options, 'extra'):
            options['properties'].update(options['properties'].extra)
            options['bbox'] = options.extra['bbox']
        options['attributes'] = options.pop('properties')

    options.update({
        'featureId': options.get('featureId') or options.get('id'),  # For grid layer
        'attributes': options['attributes'],
        'scale': options.get('scale'),
        'attribution': layer.get('attributes')['dataOwner'],
        'fullName': layer.get('fullName'),
        'vector_model': vector_model,
        'isExtended': isExtended,
        'isIframe': isIframe,
        'time': params.time
    })
    return options


def _prepare_popup_response(params, request, isExtended=False, isIframe=False):
    options = _get_feature_info_for_popup(
        request, params, isExtended=isExtended, isIframe=isIframe)
    response = _render_feature_template(options, request)

    if params.cbName is None:
        return response

    return response.body.decode('utf8')


@view_config(route_name='htmlPopup', renderer='jsonp')
def htmlpopup(request):
    params = HtmlPopupServiceValidation(request)
    return _prepare_popup_response(params, request)


@view_config(route_name='extendedHtmlPopup', renderer='jsonp')
def extendedhtmlpopup(request):
    params = ExtendedHtmlPopupServiceValidation(request)
    return _prepare_popup_response(params, request, isExtended=True)


@view_config(route_name='iframeHtmlPopup', renderer='jsonp')
def iframeHtmlPopup(request):
    params = ExtendedHtmlPopupServiceValidation(request)
    return _prepare_popup_response(params, request, isIframe=True)


def _identify_oereb(request):
    def insertTimestamps(header, comments):
        pos = re.search(r'\?>', header).end()
        return ''.join((
            header[:pos],
            comments,
            header[pos:]
        ))

    params = IdentifyServiceValidation(request)
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

    comments = render('chsdi:templates/oereb_timestamps.mako', {
        'data_imported': data_imported,
        'data_created': data_created
    })
    header = insertTimestamps(header, comments)

    isScaleDependent = has_buffer(params.imageDisplay, params.mapExtent, params.tolerance)
    scale = get_scale(params.imageDisplay, params.mapExtent) if isScaleDependent else None
    # Only relation 1 to 1 is needed at the moment
    layerVectorModel = [{layerBodId: [oereb_models_from_bodid(layerBodId, scale=scale, srid=params.srid)[0]]}]
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
    params = IdentifyServiceValidation(request)
    response = {'results': []}
    scale = None
    # Determine layer types
    # Grid layers are serverless
    layersDB = []
    layersGrid = []
    # By definition, if both mapExtent and imageDisplay are null, scale is not relevant
    if params.imageDisplay is not None and all(i > 0 for i in params.imageDisplay) \
            and params.mapExtent is not None and all(j > 0 for j in params.mapExtent.bounds):
        isScaleDependent = has_buffer(params.imageDisplay, params.mapExtent, params.tolerance)
        scale = get_scale(params.imageDisplay, params.mapExtent) if isScaleDependent else None
    if params.layers == 'all':
        model = get_bod_model(params.lang)
        query = params.request.db.query(model)
        for layer in get_layers_metadata_for_params(params, query, model):
            layerBodId = layer['layerBodId']
            models = models_from_bodid(layerBodId, scale=scale, srid=params.srid)
            if models:
                layersDB.append({layerBodId: models})
            else:
                gridSpec = get_grid_spec(layerBodId)
                if gridSpec and params.geometryType == 'esriGeometryPoint':
                    layersGrid.append({layerBodId: gridSpec})
    else:
        for layerBodId in params.layers:
            gridSpec = get_grid_spec(layerBodId)
            if gridSpec:
                if params.geometryType not in ('esriGeometryPoint', 'esriGeometryEnvelope'):
                    raise exc.HTTPBadRequest(
                        'Only esriGeometryPoint or esriGeometryEnvelope'
                        'are supported for geometryType parameter for grid like data')
                layersGrid.append({layerBodId: gridSpec})
            else:
                models = models_from_bodid(layerBodId, scale=scale, srid=params.srid)
                # The layer has a model but not at the right scale
                if models is not None and len(models) == 0:
                    return response
                # There is no model for this layer
                elif models is None:
                    raise exc.HTTPBadRequest('No GeoTable was found for %s' % layerBodId)
                layersDB.append({layerBodId: models})
    featuresGrid = _identify_grid(params, layersGrid)
    featuresDB = _identify_db(params, layersDB)
    response['results'] = featuresGrid + featuresDB
    return response


def _identify_grid(params, layerBodIds):
    features = []
    if len(layerBodIds) == 0:
        return features
    geometry = params.geometry
    # TODO support min/max scale and min/max resolution?

    # For select by rectangle
    if params.geometryType == 'esriGeometryEnvelope':
        coords = list(geometry.exterior.coords)
        minx = miny = float('inf')
        maxx = maxy = float('-inf')
        for x, y in coords:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
        bbox = [minx, miny, maxx, maxy]
        pointCoordinates = center_from_box2d(bbox)
    else:
        pointCoordinates = list(list(geometry.coords)[0])
    # if coordinates is in WebMercator, we reproject the coordinate to LV95
    if params.srid == 3857 or params.srid == 4326:
        pointCoordinates = _transform_coordinates(pointCoordinates, params.srid, 2056)
    bucketName = params.request.registry.settings['vector_bucket']
    for layer in layerBodIds:
        [layerBodId, gridSpec] = next(iter(layer.items()))
        params.layerId = layerBodId
        layerProperties = get_grid_layer_properties(layerBodId)
        timestamp = layerProperties.get('timestamp')
        grid = Grid(gridSpec.get('extent'),
                    gridSpec.get('resolutionX'),
                    gridSpec.get('resolutionY'))
        if (params.srid == 2056 or params.srid == 3857 or params.srid == 4326) and gridSpec.get('srid') == '21781':
            pointCoordinates = shift_to(pointCoordinates, 21781)
        elif params.srid == 21781 and gridSpec.get('srid') == '2056':
            pointCoordinates = shift_to(pointCoordinates, 2056)
        [col, row] = grid.cellAddressFromPointCoordinate(pointCoordinates)
        if col is not None and row is not None:
            feature, none = _get_feature_grid(col, row, timestamp, gridSpec, bucketName, params, process=False)
            if feature is not None:
                features.append(feature)

    return features


def _identify_db(params, layerBodIds):
    maxFeatures = MAX_FEATURES
    features = []
    if len(layerBodIds) == 0:
        return features
    feature_gen = _get_features_for_filters(
        params, layerBodIds, maxFeatures=maxFeatures, where=params.where)
    while len(features) <= maxFeatures:
        try:
            feature = next(feature_gen)
        except InternalError as e:
            # Note: in order not to expose too much details about internal
            # db structure, we only return the title of the error and not details
            # about table names and the like
            # Python2/3
            logger.error("Database error while reading features: {}".format(e))
            raise exc.HTTPBadRequest('Your request generated a database errorwhile reading features')
        except StopIteration:
            break
        else:
            features.append(_process_feature(feature, params))
    return features


def _get_feature_service(request):
    params = GetFeatureServiceValidation(request)
    features = []
    for feature, vector_model in _get_features(params):
        if hasattr(params, 'featureIds') and len(params.featureIds) > 1:
            features.append(feature['feature'])
        else:
            features.append(feature)
    if len(features) == 1:
        return features[0]
    return features


def _get_features(params, extended=False, process=True):
    ''' Returns exactly one feature or raises
    an excpetion '''
    featureIds = params.featureIds
    scale = None
    if hasattr(params, 'imageDisplay') and hasattr(params, 'mapExtent'):
        if all((params.imageDisplay, params.mapExtent)):
            scale = get_scale(params.imageDisplay, params.mapExtent)

    models = models_from_bodid(params.layerId, orderScale=scale, srid=params.srid)
    gridSpec = get_grid_spec(params.layerId)
    if models is None and gridSpec is None:
        raise exc.HTTPBadRequest(
            'No Vector Table was found for %s' % params.layerId)
    for featureId in featureIds:
        if gridSpec:
            bucketName = params.request.registry.settings['vector_bucket']
            # By convention
            if featureId.find('_') == -1:
                raise exc.HTTPBadRequest('Unexpected id formatting')
            col, row = featureId.split('_')
            layerProperties = get_grid_layer_properties(params.layerId)
            timestamp = layerProperties.get('timestamp')
            yield _get_feature_grid(col, row, timestamp, gridSpec, bucketName, params, process=process)
        else:
            yield _get_feature_db(featureId, params, models, process=process)


def _get_feature_by_id(featureId, params, model):
    query = params.request.db.query(model) \
                             .filter(model.id == featureId)
    try:
        return query.one()
    except (NoResultFound, DataError, InternalError):
        return None
    except MultipleResultsFound:
        raise exc.HTTPInternalServerError(
            'Multiple features found for the same id %s' % featureId)


def _get_feature_db(featureId, params, models, process=True):
    feature = None
    # One layer can have several models
    for model in models:
        # return a sqlalchemy.util._collections.result
        feature = _get_feature_by_id(featureId, params, model)
        if feature is not None:
            vector_model = model
            break
    if feature is None:
        raise exc.HTTPNotFound('No feature with id %s' % featureId)
    if process:
        feature = _process_feature(feature, params)
        feature = {'feature': feature}
    return feature, vector_model


def _get_feature_grid(col, row, timestamp, gridSpec, bucket_name, params, process=True):
    feature = None
    col = str(col)
    row = str(row)
    timestamp = str(timestamp)
    layerBodId = params.layerId
    featureS3KeyName = 'tooltip/%s/default/%s/%s/%s/data.json' % (layerBodId, timestamp, col, row)
    featureJson = decompress_gzipped_string(get_file_from_bucket(bucket_name, featureS3KeyName)['Body'])
    # Because of esriJSON design and papyrus no esrijson support for now
    feature = geojson.loads(featureJson)
    if not params.returnGeometry:
        del feature['geometry']
    feature['layerBodId'] = layerBodId
    feature['layerName'] = params.translate(layerBodId)
    # For some reason we define the id twice...
    feature['featureId'] = feature['id']
    feature['properties']['label'] = feature['id']

    logger.debug('Get feature grid: params.srid=%s, gridSpec.get(srid)=%s feature.geometry=%s', params.srid, gridSpec.get('srid'), hasattr(feature, 'geometry'))

    # to mimic DB output, we add a bbox value, defined by the geom of the GeoJSON (it's always a mono shape polygon
    # representing the tile surface)
    # for some reason, we can't use the grid here to extract the extent of the tile when coming from the feature
    # metadata endpoint (it raises an exception)
    bbox_bottom_left = None
    bbox_top_right = None
    if hasattr(feature, 'geometry') and hasattr(feature.geometry, 'coordinates'):
        for coord in feature.geometry.coordinates[0]:
            if not bbox_bottom_left or bbox_bottom_left[0] > coord[0] or bbox_bottom_left[1] > coord[1]:
                bbox_bottom_left = coord
            if not bbox_top_right or bbox_top_right[0] < coord[0] or bbox_top_right[1] < coord[1]:
                bbox_top_right = coord
        if bbox_top_right and bbox_bottom_left:
            feature['bbox'] = [bbox_bottom_left[0], bbox_bottom_left[1], bbox_top_right[0], bbox_top_right[1]]

            if (params.srid == 2056 or params.srid == 3857 or params.srid == 4326) and gridSpec.get('srid') == '21781':
                feature['bbox'] = shift_to(feature['bbox'], 2056)
                coords = feature['geometry']['coordinates']
                coords = [[shift_to(c, 2056) for c in coords[0]]]
                feature['geometry']['coordinates'] = coords
            if params.srid == 21781 and gridSpec.get('srid') == '2056':
                feature['bbox'] = shift_to(feature['bbox'], 21781)
                coords = feature['geometry']['coordinates']
                coords = [[shift_to(c, 21781) for c in coords[0]]]
                feature['geometry']['coordinates'] = coords

            # if targeted SRID is WebMercator, we reproject the feature geometry and bbox here
            if params.srid == 3857 or params.srid == 4326:
                coords = feature['geometry']['coordinates']
                coords = [[_transform_coordinates(c, 2056, params.srid) for c in coords[0]]]
                feature['geometry']['coordinates'] = coords
                feature['bbox'] = transform_round_geometry(feature['bbox'], 2056, params.srid)

    # in order to mimic DB output, if process flag is true we wrap the feature into a "feature" attribute
    if process:
        # the DB also calls here the process method from Vector class, but what we have here is not an instance of this
        # class. So we just wrap the feature without processing it to a GeoJSON or EsriJSON.
        feature = {'feature': feature}
    return feature, None


def _has_extended_info(isExtended, hasExtendedInfo, bodId):
    if isExtended and not hasExtendedInfo:
        raise exc.HTTPNotFound('No extended info has been found for %s' % bodId)


def _render_feature_template(options, request):
    # Determine if we should render the extended tooltip or the iframe
    isExtended = options.get('isExtended')
    vector_model = options.get('vector_model')
    if vector_model:
        template = vector_model.__template__
        options['hasExtendedInfo'] = hasattr(vector_model, '__extended_info__')
    else:
        # For grid like models
        layerProperties = get_grid_layer_properties(options['layerBodId'])
        template = layerProperties.get('template')
        options['hasExtendedInfo'] = layerProperties.get('extended')
        options['isGridLayer'] = True

    # We can't test earlier, some features may or may not have extended info for
    # the same layer.
    _has_extended_info(isExtended, options['hasExtendedInfo'], options['layerBodId'])

    options['baseUrl'] = make_geoadmin_url(request)
    return render_to_response(
        'chsdi:%s' % template, {
            'c': options
        }, request=request)


def _get_features_for_filters(params, layerBodIds, maxFeatures=None, where=None):
    ''' Returns a generator function that yields
    a feature. '''
    for layer in layerBodIds:
        layerBodId, models = next(iter(layer.items()))

        # Determine the limit
        limits = [x for x in [maxFeatures, params.limit] if x is not None]
        flimit = min(limits) if len(limits) > 0 else None

        if where is not None:
            vectorLayer = []
            filter_attributes = []
            for model in models:
                filter_attributes += list(model().get_orm_columns_names())
                txt = format_query(model, where, params.lang)
                if txt is not None:
                    vectorLayer.append((model, txt))
            if len(vectorLayer) == 0:
                raise exc.HTTPBadRequest('The layerDefs clause is not valid for %s.' % layerBodId)
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
                    params.imageDisplay,
                    params.mapExtent,
                    params.tolerance,
                    params.srid
                )
                query = query.filter(geomFilter)

            # Filter by time instant
            if params.timeInstant is not None and hasattr(model, '__timeInstant__'):
                timeInstantColumn = model.time_instant_column()
                timeInstantIndex = layerBodIds.index(layer)
                timeInstant = params.timeInstant[timeInstantIndex]
                if timeInstant:
                    query = query.filter(
                        timeInstantColumn == timeInstant)

            if hasattr(model, 'bgdi_order'):
                # bgdi_order used only in zeitreihen at the moment
                query = query.order_by(model.bgdi_order)
            elif params.order == 'distance':
                ordering = model.order_by_distance(
                    params.geometry,
                    params.geometryType,
                    params.imageDisplay,
                    params.mapExtent,
                    params.tolerance,
                    flimit,
                    params.srid
                )
                query = query.order_by(ordering)

            # Add limit
            query = query.limit(flimit) if flimit is not None else query

            # Add offset
            if params.offset is not None:
                query = query.offset(params.offset)

            # We need either where or geomFilter (geomFilter especially for zeitreihen layer)
            if where is not None or geomFilter is not None:
                # bgdi_order used only in zeitreihen at the moment
                if hasattr(model, 'bgdi_order'):
                    # standard identify show first bgdi_order only
                    bgdi_order = None
                    for feature in query:
                        if bgdi_order is None:
                            bgdi_order = feature.bgdi_order
                        if bgdi_order < feature.bgdi_order:
                            continue
                        yield feature
                else:
                    for feature in query:
                        yield feature


def _attributes(request):
    ''' This service exposes preview values based on a layer Id
    and an attribute name (mapped in the model) '''
    MAX_ATTR_VALUES = 50
    attributes_values = []
    params = AttributesServiceValidation(request)

    models = models_from_bodid(params.layerId, srid=params.srid)

    if models is None:
        raise exc.HTTPBadRequest('No Vector Table was found for %s' % params.layerId)

    # Check that the attribute provided is found at least in one model
    model_to_query = None
    for model in models:
        attributes = model().get_attributes_keys()
        if params.attribute in attributes:
            model_to_query = model
            break
    if model_to_query is None:
        raise exc.HTTPBadRequest('No attribute %s was found for %s' % (params.attribute, params.layerId))

    col = model_to_query.get_column_by_property_name(params.attribute)
    col_type = str(col.type)
    if col_type in ('DATE', 'INTEGER', 'NUMERIC'):
        query = request.db.query(func.max(col).label('max'), func.min(col).label('min'))
        res = query.one()
        return {'values': [res.min, res.max]}
    # Return a sample of values otherwise
    query = request.db.query(col).distinct().order_by(col)
    query = query.limit(MAX_ATTR_VALUES)
    for attr in query:
        if len(attr):
            attributes_values.append(attr[0])
    return {'values': sorted(attributes_values)}


def _find(request):
    MaxFeatures = MAX_FEATURES
    params = FindServiceValidation(request)
    if params.searchText is None:
        raise exc.HTTPBadRequest('Please provide a searchText')

    models = queryable_models_from_bodid(params.layer, params.searchField, srid=params.srid)
    features = []
    if models is None:
        raise exc.HTTPBadRequest(
            'No Vector Table was found for %s for searchField %s' % (params.layer, params.searchField))
    vectorLayers = []
    for model in models:
        where_txt = None
        if params.where is not None:
            where_txt = format_query(model, params.where, params.lang)
        vectorLayers.append((model, where_txt))

    layers = list(list(zip(*vectorLayers))[1])
    if params.where is not None and not any(layers):
        raise exc.HTTPBadRequest(
            'Filtering on a not existing field on layer {}'.format(params.layer)
        )

    for model, where_text in vectorLayers:
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
        if where_text is not None:
            where_txt = unnacent_where_text(where_text, model)
            query = query.filter(text(
                "({})".format(where_txt))  # operator precedance
            )
        query = query.limit(MaxFeatures)
        for feature in query:
            f = _process_feature(feature, params)
            features.append(f)

    return {'results': features}


def _format_search_text(columnType, searchText):
    if isinstance(columnType, (Text, Unicode)):
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
        if re.match(r'^\d+?\.\d+?$', searchText) is not None:
            return float(searchText)
        else:
            raise exc.HTTPBadRequest('Please provide a float')
    elif isinstance(columnType, Geometry):
        raise exc.HTTPBadRequest('Find operations cannot be performed on geometry columns')
    return searchText


def _process_feature(feature, params):
    if params.geometryFormat == 'geojson':
        return feature.to_geojson(params.translate,
                           params.returnGeometry,
                           srid=params.srid)
    return feature.to_esrijson(params.translate,
                               params.returnGeometry,
                               srid=params.srid)


def _get_features_releases(model, params):
    maxFeatures = 1000
    query = params.request.db.query(model)
    if hasattr(model, 'bgdi_order'):
        query = query.distinct(model.bgdi_order)
    if params.geometry is not None:
        geomFilter = model.geom_filter(
            params.geometry,
            params.imageDisplay,
            params.mapExtent,
            params.tolerance,
            params.srid
        )
        query = query.filter(geomFilter)
    if params.timeInstant is not None and hasattr(model, '__timeInstant__'):
        timeInstantColumn = model.time_instant_column()
        query = query.filter(timeInstantColumn == params.timeInstant)
    if hasattr(model, 'bgdi_order'):
        query = query.order_by(model.bgdi_order)
    query = query.limit(maxFeatures)
    for feature in query:
        yield feature


@view_config(route_name='releases', renderer='geojson')
def releases(request):
    params = IdentifyServiceValidation(request, service='releases')
    # For this sevice, we have to use different models based
    # on specially sorted views. We add the _meta part to the given
    # layer name
    # Note that only zeitreihen is currently supported for this service
    # Use scale rather than resolutions for zeitreihen like the other layers
    resolution = get_resolution(params.imageDisplay, params.mapExtent)
    models = models_from_bodid(params.layerId, resolution=resolution, srid=params.srid)
    if models is None:
        raise exc.HTTPBadRequest('No Vector Table was found for %s' % params.layerId)

    minYear = float('inf')
    # Default timestamp
    timestamps = []
    # group timestamps by bgdi_order
    for f in _get_features_releases(models[0], params):
        if hasattr(f, 'array_release_years') and f.array_release_years is not None and \
                hasattr(f, 'bgdi_order') and f.bgdi_order is not None:
            # Here we use some kind of filtering technique
            # to avoid returning too many results (used in service-print only)
            for y in f.array_release_years:
                if y < minYear:
                    timestamps.append(y)
                    minYear = y

    timestamps = list(set(timestamps))
    # add day to have full timestamp
    timestamps = sorted([int(str(ts) + '1231') for ts in timestamps])
    # transform back to string
    timestamps = [str(ts) for ts in timestamps]
    return {'results': timestamps}
