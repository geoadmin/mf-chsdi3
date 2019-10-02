# -*- coding: utf-8 -*-


from collections import OrderedDict
from pyramid.view import view_config

from chsdi.models import bodmap


class SourceService(object):

    def __init__(self, request):
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.cbName = request.params.get('callback')
        self.request = request
        self.lang = request.lang

    @view_config(route_name='sources', renderer='jsonp')
    def sources(self):
        layers = OrderedDict()
        for bodId in bodmap.keys():
            models = []
            for model in bodmap[bodId]:
                models.append({
                    'database': model.metadata.bind.engine.url.database,
                    'schema': model.__table_args__['schema'] if 'schema' in model.__table_args__ else 'public',
                    'table': model.__tablename__
                })
            layers[bodId] = models
        return layers
