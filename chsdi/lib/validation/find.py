# -*- coding: utf-8 -*-

import json
from pyramid.httpexceptions import HTTPBadRequest

from chsdi.lib.validation import MapNameValidation, SUPPORTED_OUTPUT_SRS


class FindServiceValidation(MapNameValidation):

    def __init__(self, request):
        super(FindServiceValidation, self).__init__()
        self._layer = None
        self._searchText = None
        self._searchField = None
        self._contains = None
        self._returnGeometry = None
        self._srid = 21781
        self._layerDefs = None
        self._where = None

        self.layer = request.params.get('layer')
        self.searchText = request.params.get('searchText')
        self.searchField = request.params.get('searchField')
        self.contains = request.params.get('contains')
        self.returnGeometry = request.params.get('returnGeometry')
        self.srid = request.params.get('sr')

        self.geometryFormat = request.params.get('geometryFormat', u'esrijson')
        self.mapName = request.matchdict.get('map')
        self.request = request
        self.lang = request.lang
        self.cbName = request.params.get('callback')
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.layerDefs = request.params.get('layerDefs')

    @property
    def layer(self):
        return self._layer

    @property
    def searchText(self):
        return self._searchText

    @property
    def searchField(self):
        return self._searchField

    @property
    def contains(self):
        return self._contains

    @property
    def returnGeometry(self):
        return self._returnGeometry

    @property
    def srid(self):
        return self._srid

    @layer.setter
    def layer(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide a parameter layer')
        if len(value.split(',')) > 1:
            raise HTTPBadRequest('You can provide only one layer at a time')
        self._layer = value

    @searchText.setter
    def searchText(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide a search text parameter')
        self._searchText = value

    @searchField.setter
    def searchField(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide a searchField')
        if len(value.split(',')) > 1:
            raise HTTPBadRequest('You can provide only one searchField at a time')
        self._searchField = value

    @contains.setter
    def contains(self, value):
        if value is None or value.lower() == u'true':
            self._contains = True
        else:
            self._contains = False

    @returnGeometry.setter
    def returnGeometry(self, value):
        if value is None:
            self._returnGeometry = True
        else:
            if value.lower() == u'true':
                self._returnGeometry = True
            elif value.lower() == u'false':
                self._returnGeometry = False
            else:
                self._returnGeometry = True

    @srid.setter
    def srid(self, value):
        if value in map(str, SUPPORTED_OUTPUT_SRS):
            self._srid = int(value)
        elif value is not None:
            raise HTTPBadRequest('Unsupported spatial reference %s' % value)

    @property
    def where(self):
        return self._where

    @property
    def layerDefs(self):
        return self._layerDefs

    @layerDefs.setter
    def layerDefs(self, value):
        if value is not None:
            try:
                defs = json.loads(value)
                if not (set(defs.keys()).issubset(set([self.layer]))):
                    raise HTTPBadRequest("You can only filter on layer '%s' in 'layerDefs'" % self.layer)
                where = "+and+".join(defs.values())
                self._layerDefs = defs
                self._where = where
            except ValueError:
                raise HTTPBadRequest("Cannot parse 'layerDefs' %s" % value)
