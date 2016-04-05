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


class BaseFeaturesValidation(MapNameValidation):

    def __init__(self, request):
        super(BaseFeaturesValidation, self).__init__()

        self.mapName = request.matchdict.get('map')
        self.request = request
        self.lang = request.lang
        self.translate = request.translate
        self.cbName = request.params.get('callback')
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.varnish_authorized = request.headers.get('X-SearchServer-Authorized', 'false').lower() == 'true'
