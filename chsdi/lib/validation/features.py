# -*- coding: utf-8 -*-


from pyramid.httpexceptions import HTTPBadRequest
from shapely.geometry import asShape

from chsdi.lib.helpers import float_raise_nan
from chsdi.lib.validation import BaseFeaturesValidation
from chsdi.esrigeojsonencoder import loads


class HtmlPopupServiceValidation(BaseFeaturesValidation):

    def __init__(self, request):
        super(HtmlPopupServiceValidation, self).__init__(request)
        self._layerId = None
        self._featureIds = None
        self._imageDisplay = None
        self._mapExtent = None

        self.layerId = request.matchdict.get('layerId')
        self.featureIds = request.matchdict.get('featureId')
        self.imageDisplay = request.params.get('imageDisplay')
        self.mapExtent = request.params.get('mapExtent')

        self.returnGeometry = False

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
                    'Please provide the parameter imageDisplay in a comma separated list of 3 arguments '
                    '(width,height,dpi)')
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
        self._returnGeometry = None

        self.returnGeometry = request.params.get('returnGeometry')
        self.geometryFormat = request.params.get('geometryFormat', 'esrijson')

    @property
    def returnGeometry(self):
        return self._returnGeometry

    @returnGeometry.setter
    def returnGeometry(self, value):
        if value is None:
            self._returnGeometry = True
        else:
            if isinstance(value, unicode) and value.lower() == 'true':
                self._returnGeometry = True
            elif isinstance(value, unicode) and value.lower() == 'false':
                self._returnGeometry = False
            else:
                self._returnGeometry = True


class AttributesServiceValidation(BaseFeaturesValidation):

    def __init__(self, request):
        super(AttributesServiceValidation, self).__init__(request)

        self.layerId = request.matchdict.get('layerId')
        self.attribute = request.matchdict.get('attribute')


class IdentifyServiceValidation(BaseFeaturesValidation):

    def __init__(self, request, service=None):
        super(IdentifyServiceValidation, self).__init__(request)
        self._where = None
        self._geometry = None
        self._geometryType = None
        self._imageDisplay = None
        self._mapExtent = None
        self._returnGeometry = None
        self._tolerance = None
        self._timeInstant = None
        self._layers = None
        self._offset = None
        self._limit = None
        self._order = None

        self.esriGeometryTypes = (
            'esriGeometryPoint',
            'esriGeometryPolyline',
            'esriGeometryPolygon',
            'esriGeometryEnvelope'
        )
        self.where = request.params.get('where')
        self.geometry = request.params.get('geometry')
        self.geometryType = request.params.get('geometryType')
        self.imageDisplay = request.params.get('imageDisplay')
        self.mapExtent = request.params.get('mapExtent')
        self.returnGeometry = request.params.get('returnGeometry')
        if service != 'releases':
            self.tolerance = request.params.get('tolerance')
        self.layers = request.params.get('layers', 'all')
        self.timeInstant = request.params.get('timeInstant')
        self.offset = request.params.get('offset')
        self.limit = request.params.get('limit')
        self.order = request.params.get('order')

    @property
    def where(self):
        return self._where

    @property
    def geometryType(self):
        return self._geometryType

    @property
    def geometry(self):
        return self._geometry

    @property
    def imageDisplay(self):
        return self._imageDisplay

    @property
    def mapExtent(self):
        return self._mapExtent

    @property
    def returnGeometry(self):
        return self._returnGeometry

    @property
    def tolerance(self):
        return self._tolerance

    @property
    def timeInstant(self):
        return self._timeInstant

    @property
    def layers(self):
        return self._layers

    @property
    def offset(self):
        return self._offset

    @property
    def limit(self):
        return self._limit

    @property
    def order(self):
        return self._order

    @where.setter
    def where(self, value):
        # TODO regexp to test validity of sql clause
        if value is not None:
            self._where = value

    @geometryType.setter
    def geometryType(self, value):
        if value is None and self._where is not None:
            return
        elif value is None and self._where is None:
            raise HTTPBadRequest('Please provide the parameter geometryType  (Required)')
        if value not in self.esriGeometryTypes:
            raise HTTPBadRequest('Please provide a valid geometry type')
        self._geometryType = value

    @geometry.setter
    def geometry(self, value):
        if value is None and self._where is not None:
            return
        elif value is None and self._where is None:
            raise HTTPBadRequest('Please provide the parameter geometry  (Required)')
        else:
            try:
                self._geometry = loads(value)
            except ValueError:
                raise HTTPBadRequest('Please provide a valid geometry')

    @imageDisplay.setter
    def imageDisplay(self, value):
        if value is None and self._where is not None:
            return
        elif value is None and self._where is None:
            raise HTTPBadRequest('Please provide the parameter imageDisplay  (Required)')
        value = value.split(',')
        if len(value) != 3:
            raise HTTPBadRequest(
                'Please provide the parameter imageDisplay in a comma separated list of 3 arguments '
                '(width,height,dpi)')
        try:
            self._imageDisplay = map(float_raise_nan, value)
        except ValueError:
            raise HTTPBadRequest('Please provide numerical values for the parameter imageDisplay')

    @mapExtent.setter
    def mapExtent(self, value):
        if value is None and self._where is not None:
            return
        elif value is None and self._where is None:
            raise HTTPBadRequest('Please provide the parameter mapExtent  (Required)')
        else:
            try:
                feat = loads(value)
                self._mapExtent = asShape(feat)
            except ValueError:
                raise HTTPBadRequest('Please provide numerical values for the parameter mapExtent')

    @returnGeometry.setter
    def returnGeometry(self, value):
        if value is None:
            self._returnGeometry = True
        else:
            if isinstance(value, unicode) and value.lower() == 'true':
                self._returnGeometry = True
            elif isinstance(value, unicode) and value.lower() == 'false':
                self._returnGeometry = False
            else:
                self._returnGeometry = True

    @tolerance.setter
    def tolerance(self, value):
        if value is None and self._where is not None:
            return
        elif value is None and self._where is None:
            raise HTTPBadRequest('Please provide the parameter tolerance (Required)')
        try:
            self._tolerance = float_raise_nan(value)
        except ValueError:
            raise HTTPBadRequest('Please provide an integer value for the pixel tolerance')

    @timeInstant.setter
    def timeInstant(self, value):
        if value is not None:
            if len(value) != 4:
                raise HTTPBadRequest('Only years are supported as timeInstant parameter')
            if value.isdigit():
                self._timeInstant = int(value)
            else:
                raise HTTPBadRequest('Please provide an integer for the parameter timeInstant')
        else:
            self._timeInstant = value

    @layers.setter
    def layers(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide a parameter layers')
        if value == 'all':
            self._layers = value
        else:
            try:
                layers = value.split(':')[1]
                self._layers = layers.split(',')
            except:
                HTTPBadRequest('There is an error in the parameter layers')

    @offset.setter
    def offset(self, value):
        if value is not None:
            if not value.isdigit():
                raise HTTPBadRequest('Please provide an integer as an offset parameter')
            else:
                self._offset = int(value)

    @limit.setter
    def limit(self, value):
        if value is not None:
            if value.isdigit() and int(value) >= 0:
                self._limit = int(value)
            else:
                raise HTTPBadRequest('Please provide a positive integer for the parameter limit')

    @order.setter
    def order(self, value):
        if value is not None:
            if value != 'distance':
                raise HTTPBadRequest('Please provide a valid order parameter')
            if self.geometry is None:
                raise HTTPBadRequest('The order value can only be used together with a geometry.')
            self._order = value
