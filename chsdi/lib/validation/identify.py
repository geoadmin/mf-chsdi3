# -*- coding: utf-8 -*-

import json
import esrijson
import six
from shapely.geometry.linestring import LineString
from shapely.geometry.polygon import Polygon
from pyramid.httpexceptions import HTTPBadRequest

from chsdi.lib.helpers import float_raise_nan
from chsdi.lib.validation import BaseFeaturesValidation

if six.PY3:
    unicode = str


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
        self._layerDefs = None

        self.esriGeometryTypes = (
            u'esriGeometryPoint',
            u'esriGeometryPolyline',
            u'esriGeometryPolygon',
            u'esriGeometryEnvelope'
        )
        if request.params.get('where') is not None and request.params.get('layerDefs'):
            raise HTTPBadRequest("Parameters 'layerDefs' and 'where' are mutually exclusive")
        self.where = request.params.get('where')
        self.geometryType = request.params.get('geometryType')
        self.geometry = request.params.get('geometry')
        self.imageDisplay = request.params.get('imageDisplay')
        self.mapExtent = request.params.get('mapExtent')
        self.returnGeometry = request.params.get('returnGeometry')
        if service != 'releases':
            self.tolerance = request.params.get('tolerance')
        if service == 'releases':
            self.layerId = request.matchdict.get('layerId')
        self.layers = request.params.get('layers', 'all')
        self.timeInstant = request.params.get('timeInstant')
        self.offset = request.params.get('offset')
        self.limit = request.params.get('limit')
        self.order = request.params.get('order')
        self.layerDefs = request.params.get('layerDefs')

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

    @property
    def layerDefs(self):
        return self._layerDefs

    @layerDefs.setter
    def layerDefs(self, value):
        if value is not None:
            try:
                defs = json.loads(value)
                if self.layers != 'all':
                    if not (set(defs.keys()).issubset(set(self.layers))):
                        raise HTTPBadRequest("You can only filter on layer '%s' in 'layerDefs'" % self.layers)
                where = "+and+".join(defs.values())
                self._layerDefs = defs
                self.where = where
            except ValueError:
                raise HTTPBadRequest("Cannot parse 'layerDefs' %s" % value)

    @where.setter
    def where(self, value):
        # TODO regexp to test validity of sql clause
        if value is not None:
            self._where = value

    @geometryType.setter
    def geometryType(self, value):
        if value is None and (self._where is not None or self._layerDefs is not None):
            return
        elif value is None and self._where is None and self._layerDefs is None:
            raise HTTPBadRequest('Please provide the parameter geometryType  (Required)')
        if value not in self.esriGeometryTypes:
            raise HTTPBadRequest('Please provide a valid geometry type')
        self._geometryType = value

    @geometry.setter
    def geometry(self, value):
        if value is None and (self._where is not None or self._layerDefs is not None):
            return
        elif value is None and self._where is None and self._layerDefs is None:
            raise HTTPBadRequest('Please provide the parameter geometry  (Required)')
        else:
            try:
                if self._geometryType == 'esriGeometryEnvelope':
                    self._geometry = esrijson.to_shape([float_raise_nan(c) for c in value.split(',')])
                elif self._geometryType == 'esriGeometryPoint' \
                        and 'x' not in value and 'y' not in value:
                    # Simple simplified point geometry
                    value = [float_raise_nan(c) for c in value.split(',')]
                    self._geometry = esrijson.to_shape({'x': value[0], 'y': value[1]})
                else:
                    self._geometry = esrijson.to_shape(esrijson.loads(value))

            except Exception:
                raise HTTPBadRequest('Please provide a valid geometry')
        if (self._geometryType == u'esriGeometryPolyline' and not isinstance(self._geometry, LineString)) \
                or (self._geometryType == u'esriGeometryPolygon' and not isinstance(self._geometry, Polygon)):
            raise HTTPBadRequest(u"Missmatch between 'geometryType': {} and provided 'geometry' parsed as '{}'".format(self._geometryType, self._geometry.__class__.__name__))

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
            self._imageDisplay = list(map(float_raise_nan, value))
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
                self._mapExtent = esrijson.to_shape([float_raise_nan(c) for c in value.split(',')])
            except Exception:
                raise HTTPBadRequest('Please provide numerical values for the parameter mapExtent')

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
        def validateTimeinstant(instant):
            if len(instant) not in (0, 4):
                raise HTTPBadRequest(
                    'Only years are supported as timeInstant parameter: provided value %s' % instant)
            if instant.isdigit():
                instant = int(instant)
            elif len(instant) == 0:
                instant = None
            else:
                raise HTTPBadRequest(
                    'Please provide an integer for the parameter timeInstant: provided value %s' % instant)
            return instant

        if value is not None:
            instants = []
            timeInstants = value.split(',')
            nbTimeInstants = len(timeInstants)
            nbLayers = len(self.layers)
            if nbTimeInstants == nbLayers:
                for instant in timeInstants:
                    instants.append(validateTimeinstant(instant))
            elif nbTimeInstants == 1:
                instant = validateTimeinstant(timeInstants[0])
                instants = [instant for i in range(0, len(self.layers) + 1)]
            else:
                raise HTTPBadRequest(
                    'Number of timInstants (%s) and layers (%s) mismatch' % (nbTimeInstants, nbLayers))
            self._timeInstant = instants
        else:
            self._timeInstant = value

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
            except Exception:
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
            if value != u'distance':
                raise HTTPBadRequest('Please provide a valid order parameter')
            if self.geometry is None:
                raise HTTPBadRequest('The order value can only be used together with a geometry.')
            self._order = value
