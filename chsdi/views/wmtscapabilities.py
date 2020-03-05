# -*- coding: utf-8 -*-

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest
from gatilegrid import getTileGrid

from chsdi.models.bod import get_wmts_models
from chsdi.lib.helpers import sanitize_url
from chsdi.lib.validation import MapNameValidation
from chsdi.lib.filters import filter_by_geodata_staging, filter_by_map_name


def getDefaultTileMatrixSet(tileMatrixSet):
    tilematrixSet = {}

    tilegridClass = getTileGrid(int(tileMatrixSet))
    if tileMatrixSet not in ['2056', '21781']:
        useSwissExtent = False
    else:
        useSwissExtent = True
    gagrid = tilegridClass(useSwissExtent=useSwissExtent)
    minZoom = 0
    maxZoom = len(gagrid.RESOLUTIONS)
    for zoom in range(minZoom, maxZoom):
        tilematrixSet[zoom] = [
            gagrid.getResolution(zoom),
            gagrid.numberOfXTilesAtZoom(zoom),
            gagrid.numberOfYTilesAtZoom(zoom),
            gagrid.getScale(zoom)
        ]
    tilematrixSet['MAXY'] = gagrid.MAXY if tileMatrixSet == '4326' else gagrid.MINX
    tilematrixSet['MINX'] = gagrid.MINX if tileMatrixSet == '4326' else gagrid.MAXY
    return tilematrixSet


def getLayersZoomLevelSet(tileMatrixSet, layers):
    zoomLevelSet = set()
    for layer in layers:
        resolution = layer.resolution_max
        zoom = layer.getClosestZoom(tileMatrixSet, resolution)
        zoomLevelSet.add(zoom)
    return zoomLevelSet


class WMTSCapabilites(MapNameValidation):

    def __init__(self, request):
        super(WMTSCapabilites, self).__init__()
        self.mapName = request.matchdict.get('map')
        self.hasMap(request.db, self.mapName)
        self.lang = request.lang
        self.models = get_wmts_models(self.lang)
        self.request = request
        epsg = request.params.get('epsg', u'21781')
        available_epsg_codes = [u'21781', u'4326', u'2056', u'3857']
        if epsg not in available_epsg_codes:
            raise HTTPBadRequest('EPSG:%s not found. Must be one of %s' % (epsg, ", ".join(available_epsg_codes)))
        self.tileMatrixSet = epsg

    @view_config(route_name='wmtscapabilities', http_cache=0)
    def wmtscapabilities(self):
        from pyramid.renderers import render_to_response
        scheme = self.request.headers.get(
            'X-Forwarded-Proto',
            self.request.scheme)
        staging = self.request.registry.settings['geodata_staging']
        wmts_public_host = self.request.registry.settings['wmts_public_host']

        # Default ressource
        onlineressource = sanitize_url("%s://%s/" % (scheme, wmts_public_host))

        layers_query = self.request.db.query(self.models['GetCap'])
        layers_query = filter_by_geodata_staging(
            layers_query,
            self.models['GetCap'].staging,
            staging
        )
        if self.mapName != 'all':
            layers_query = filter_by_map_name(layers_query, self.models['GetCap'], self.mapName)
        layers = layers_query.all()
        zoom_levels = getLayersZoomLevelSet(self.tileMatrixSet, layers)
        if hasattr(self.models['GetCapThemes'], 'oberthema_id'):
            themes = self.request.db.query(self.models['GetCapThemes']).order_by(self.models['GetCapThemes'].oberthema_id).all()
        else:
            themes = self.request.db.query(self.models['GetCapThemes']).all()

        metadata = self.request.db.query(self.models['ServiceMetadata'])\
            .filter(self.models['ServiceMetadata']
                    .pk_map_name.like(u'%wmts-bgdi%')).first()

        wmts = {
            'layers': layers,
            'zoomlevels': zoom_levels,
            'themes': themes,
            'metadata': metadata,
            'scheme': scheme,
            'onlineressource': onlineressource,
            'tilematrixset': self.tileMatrixSet,
            'tilematrixsetDefs': getDefaultTileMatrixSet(self.tileMatrixSet)
        }
        response = render_to_response(
            'chsdi:templates/wmtscapabilities/wmtscapabilities.mako',
            wmts,
            request=self.request)
        response.content_type = 'text/xml'
        return response
