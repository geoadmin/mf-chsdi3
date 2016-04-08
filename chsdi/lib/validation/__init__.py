# -*- coding: utf-8 -*-

from pyramid.httpexceptions import HTTPBadRequest

from chsdi.models.bod import Topics


class MapNameValidation(object):

    def hasMap(self, db, mapName):
        availableMaps = [q[0] for q in db.query(Topics.id)]
        # FIXME add this info in DB
        availableMaps.append('all')

        if mapName not in availableMaps:
            raise HTTPBadRequest('The map you provided does not exist')


class BaseValidation(MapNameValidation):

    def __init__(self, request):
        super(BaseValidation, self).__init__()

        self.mapName = request.matchdict.get('map')
        self.hasMap(request.db, self.mapName)
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.cbName = request.params.get('callback')
        self.request = request
        self.lang = request.lang
        self.translate = request.translate


class BaseLayersValidation(BaseValidation):

    def __init__(self, request):
        super(BaseLayersValidation, self).__init__(request)
        self._chargeable = None

        # Not to be published in doc
        self.chargeable = request.params.get('chargeable')
        self.searchText = request.params.get('searchText')

    @property
    def chargeable(self):
        return self._chargeable

    @chargeable.setter
    def chargeable(self, value):
        if value is not None:
            if value.lower() == 'true':
                self._chargeable = True
            elif value.lower() == 'false':
                self._chargeable = False


class BaseFeaturesValidation(BaseLayersValidation):

    def __init__(self, request):
        super(BaseFeaturesValidation, self).__init__(request)

        self.varnish_authorized = request.headers.get(
            'X-SearchServer-Authorized', 'false').lower() == 'true'
