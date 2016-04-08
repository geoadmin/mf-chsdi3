# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPBadRequest

from chsdi.lib.validation import MapNameValidation


class FindServiceValidation(MapNameValidation):

    def __init__(self, request):
        super(FindServiceValidation, self).__init__()
        self._layer = None
        self._searchText = None
        self._searchField = None
        self._contains = None
        self._returnGeometry = None

        self.layer = request.params.get('layer')
        self.searchText = request.params.get('searchText')
        self.searchField = request.params.get('searchField')
        self.contains = request.params.get('contains')
        self.returnGeometry = request.params.get('returnGeometry')

        self.geometryFormat = request.params.get('geometryFormat', 'esrijson')
        self.mapName = request.matchdict.get('map')
        self.request = request
        self.lang = request.lang
        self.translate = request.translate
        self.cbName = request.params.get('callback')
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.varnish_authorized = request.headers.get('X-SearchServer-Authorized', 'false').lower() == 'true'

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
        if value is None or value.lower() == 'true':
            self._contains = True
        else:
            self._contains = False

    @returnGeometry.setter
    def returnGeometry(self, value):
        if value is None:
            self._returnGeometry = True
        else:
            if value.lower() == 'true':
                self._returnGeometry = True
            elif value.lower() == 'false':
                self._returnGeometry = False
            else:
                self._returnGeometry = True
