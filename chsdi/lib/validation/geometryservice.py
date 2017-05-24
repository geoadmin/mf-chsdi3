# -*- coding: utf-8 -*-


import esrijson
from pyramid.httpexceptions import HTTPBadRequest

from chsdi.lib.validation import BaseFeaturesValidation
from chsdi.lib.helpers import float_raise_nan


class GeometryServiceValidation(BaseFeaturesValidation):

    def __init__(self, request):
        super(GeometryServiceValidation, self).__init__(request)

        self.totalArea = False

        self._clipper = None
        self._geometry = None
        self._geometryType = None
        self._returnGeometry = None
        self._layers = None
        self._groupby = None
        self._chargeable = None

        clipper = request.params.get('clipper')
        geometryType = request.params.get('geometryType')
        geometry = request.params.get('geometry')

        self.esriGeometryTypes = (
            u'esriGeometryPolygon',
            u'esriGeometryEnvelope'
        )
        self.geometryTypes = (
            u'Polygon',
            u'MultiPolygon'
        )

        # No parameter -> we want the totalPerimeter
        if clipper is None and geometry is None and geometryType is None:
            self.totalArea = True

        if not self.totalArea:
            if not clipper:
                self.geometryType = geometryType
                self.geometry = geometry
            self.clipper = clipper
            self.groupby = request.params.get('groupby')
        self.layers = request.params.get('layers', u'all')

    @property
    def clipper(self):
        return self._clipper

    @property
    def geometry(self):
        return self._geometry

    @property
    def geometryType(self):
        return self._geometryType

    @property
    def layers(self):
        return self._layers

    @property
    def groupby(self):
        return self._groupby

    @property
    def chargeable(self):
        return self._chargeable

    @clipper.setter
    def clipper(self, value):
        # Either a geometry or a clipper must be defined
        if all((self._geometry, self._geometryType)):
            return
        if value is None:
            raise HTTPBadRequest('Please provide a clipper (Required if geometry is not defined)')
        temp = value.split(':')
        if len(temp) != 2:
            raise HTTPBadRequest(
                'Unexpected clipper syntax. It should use the following syntax (layerBodId:featureId)')
        else:
            self._clipper = temp

    @geometryType.setter
    def geometryType(self, value):
        if self._clipper:
            return
        if value is None:
            raise HTTPBadRequest('Please provide the parameter geometryType (Required if clipper is not defined)')
        if value not in self.esriGeometryTypes:
            raise HTTPBadRequest(
                'Please provide a valid geometry type. Available: (%s)' % ', '.join(self.esriGeometryTypes))
        self._geometryType = value

    @geometry.setter
    def geometry(self, value):
        if self._clipper:
            return
        if value is None:
            raise HTTPBadRequest('Please provide the parameter geometry (Required if clipper is not defined)')
        try:
            if self._geometryType == 'esriGeometryEnvelope':
                self._geometry = esrijson.to_shape([float_raise_nan(c) for c in value.split(',')])
            else:
                self._geometry = esrijson.to_shape(esrijson.loads(value))
        except:
            raise HTTPBadRequest('Please provide a valid geometry')

    @layers.setter
    def layers(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide a parameter layers')
        if value == u'all':
            self._layers = value
        else:
            try:
                layers = value.split(':')[1]
                self._layers = layers.split(',')
            except:
                HTTPBadRequest('There is an error in the parameter layers')

    @groupby.setter
    def groupby(self, value):
        if value is not None:
            self._groupby = value.split(',')

    @chargeable.setter
    def chargeable(self, value):
        if value is not None:
            if value.lower() == u'true':
                self._chargeable = True
            elif value.lower() == u'false':
                self._chargeable = False
