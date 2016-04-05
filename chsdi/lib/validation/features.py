# -*- coding: utf-8 -*-


from pyramid.httpexceptions import HTTPBadRequest
from shapely.geometry import asShape

from chsdi.lib.helpers import float_raise_nan
from chsdi.lib.validation import MapNameValidation
from chsdi.esrigeojsonencoder import loads


class HtmlPopupServiceValidation(MapNameValidation):

    def __init__(self, request):
        super(HtmlPopupServiceValidation, self).__init__()
        self._layerId = None
        self._featureIds = None
        self._imageDisplay = None
        self._mapExtent = None

        self.layerId = request.matchdict.get('layerId')
        self.featureIds = request.matchdict.get('featureId')
        self.imageDisplay = request.params.get('imageDisplay')
        self.mapExtent = request.params.get('mapExtent')

        self.mapName = request.matchdict.get('map')
        self.returnGeometry = False
        self.request = request
        self.lang = request.lang
        self.translate = request.translate
        self.cbName = request.params.get('callback')
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.varnish_authorized = request.headers.get('X-SearchServer-Authorized', 'false').lower() == 'true'

    @property
    def layerId(self):
        return self._layerId

    @property
    def featureIds(self):
        return self._featureIds

    @property
    def imageDisplay(self):
        return self._imageDisplay

    @property
    def mapExtent(self):
        return self._mapExtent

    @layerId.setter
    def layerId(self, value):
        if value is not None:
            self._layerId = value
        else:
            raise HTTPBadRequest('Please provide a featureId')

    @featureIds.setter
    def featureIds(self, value):
        if value is not None:
            self._featureIds = value.split(',')
        else:
            raise HTTPBadRequest('Please provide a layerId')

    # Optional
    @imageDisplay.setter
    def imageDisplay(self, value):
        if value is not None:
            value = value.split(',')
            if len(value) != 3:
                raise HTTPBadRequest(
                    'Please provide the parameter imageDisplay in a comma separated list of 3 arguments (width,height,dpi)')
            try:
                self._imageDisplay = map(float_raise_nan, value)
            except ValueError:
                raise HTTPBadRequest('Please provide numerical values for the parameter imageDisplay')

    # Optional
    @mapExtent.setter
    def mapExtent(self, value):
        if value is not None:
            try:
                feat = loads(value)
                self._mapExtent = asShape(feat)
            except ValueError:
                raise HTTPBadRequest('Please provide numerical values for the parameter mapExtent')


class ExtendedHtmlPopupServiceValidation(HtmlPopupServiceValidation):

    def __init__(self, request):
        super(ExtendedHtmlPopupServiceValidation, self).__init__(request)

        self.returnGeometry = True


class GetFeatureServiceValidation(HtmlPopupServiceValidation):

    def __init__(self, request):
        super(GetFeatureServiceValidation, self).__init__(request)

        self.returnGeometry = request.params.get('returnGeometry', True)
        self.geometryFormat = request.params.get('geometryFormat', 'esrijson')
