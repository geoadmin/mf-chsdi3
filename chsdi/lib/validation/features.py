# -*- coding: utf-8 -*-


import re
import esrijson
import six
from pyramid.httpexceptions import HTTPBadRequest

from chsdi.lib.helpers import float_raise_nan
from chsdi.lib.validation import BaseFeaturesValidation


if six.PY3:
    unicode = str


class HtmlPopupServiceValidation(BaseFeaturesValidation):

    def __init__(self, request):
        super(HtmlPopupServiceValidation, self).__init__(request)
        self._layerId = None
        self._featureIds = None
        self._imageDisplay = None
        self._mapExtent = None
        self._time = None

        self.layerId = request.matchdict.get('layerId')
        self.featureIds = request.matchdict.get('featureId')
        self.imageDisplay = request.params.get('imageDisplay')
        self.mapExtent = request.params.get('mapExtent')
        self.time = request.params.get('time')

        self.returnGeometry = False
        self.geometryFormat = u'geojson'

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

    @property
    def time(self):
        return self._time

    @layerId.setter
    def layerId(self, value):
        if value is not None:
            self._layerId = value
        else:
            raise HTTPBadRequest('Please provide a layerId')  # pragma: no cover

    @featureIds.setter
    def featureIds(self, value):
        if value is not None:
            self._featureIds = value.split(',')
            if len(self._featureIds) > int(self.request.registry.settings['max_featureids_request']):
                raise HTTPBadRequest('Too many featureIds')
        else:
            raise HTTPBadRequest('Please provide featureIds')  # pragma: no cover

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
                self._imageDisplay = list(map(float_raise_nan, value))
            except ValueError:
                raise HTTPBadRequest('Please provide numerical values for the parameter imageDisplay')

    # Optional
    @mapExtent.setter
    def mapExtent(self, value):
        if value is not None:
            try:
                self._mapExtent = esrijson.to_shape([float_raise_nan(c) for c in value.split(',')])
            except ValueError:
                raise HTTPBadRequest('Please provide numerical values for the parameter mapExtent')

    # Optional
    @time.setter
    def time(self, value):
        if value is not None:
            try:
                self._time = int(value) if re.search(r'[12]{1}[0-9]{3}', value) else None
            except ValueError:
                raise HTTPBadRequest('Please provide a valid year for the parameter <time>')


class ExtendedHtmlPopupServiceValidation(HtmlPopupServiceValidation):

    def __init__(self, request):
        super(ExtendedHtmlPopupServiceValidation, self).__init__(request)

        self.returnGeometry = True


class GetFeatureServiceValidation(HtmlPopupServiceValidation):

    def __init__(self, request):
        super(GetFeatureServiceValidation, self).__init__(request)
        self._returnGeometry = None

        self.returnGeometry = request.params.get('returnGeometry')
        self.geometryFormat = request.params.get('geometryFormat', u'esrijson')

    @property
    def returnGeometry(self):
        return self._returnGeometry

    @returnGeometry.setter
    def returnGeometry(self, value):
        if value is None:
            self._returnGeometry = True
        else:
            if isinstance(value, unicode) and value.lower() == u'true':
                self._returnGeometry = True
            elif isinstance(value, unicode) and value.lower() == u'false':
                self._returnGeometry = False
            else:
                self._returnGeometry = True


class AttributesServiceValidation(BaseFeaturesValidation):

    def __init__(self, request):
        super(AttributesServiceValidation, self).__init__(request)

        self.layerId = request.matchdict.get('layerId')
        self.attribute = request.matchdict.get('attribute')
