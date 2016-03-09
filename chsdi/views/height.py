# -*- coding: utf-8 -*-

from chsdi.lib.helpers import filter_alt
from chsdi.lib.validation.height import HeightValidation
from chsdi.lib.raster.georaster import get_raster
from chsdi.lib.decorators import requires_authorization

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest


class Height(HeightValidation):

    def __init__(self, request):
        super(Height, self).__init__()
        if 'easting' in request.params:
            self.lon = request.params.get('easting')
        else:
            self.lon = request.params.get('lon')
        if 'northing' in request.params:
            self.lat = request.params.get('northing')
        else:
            self.lat = request.params.get('lat')
        if 'layers' in request.params:
            self.layers = request.params.get('layers')
        elif 'elevation_model' in request.params:
            self.layers = request.params.get('elevation_model')
        else:
            self.layers = ['DTM25']
        self.request = request

    @requires_authorization()
    @view_config(route_name='height', renderer='jsonp', http_cache=0)
    def height(self):
        rasters = [get_raster(layer) for layer in self.layers]
        alt = filter_alt(rasters[0].getVal(self.lon, self.lat))
        if alt is None:
            raise HTTPBadRequest('Requested coordinate out of bounds')

        return {'height': str(alt)}
