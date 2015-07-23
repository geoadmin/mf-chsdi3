# -*- coding: utf-8 -*-

from pyramid.view import view_config

from chsdi.models.bod import Topics
from chsdi.lib.filters import filter_by_geodata_staging


@view_config(route_name='topics', renderer='jsonp')
def topics(request):
    model = Topics
    geodataStaging = request.registry.settings['geodata_staging']
    showCatalog = True
    query = request.db.query(model).filter(model.showCatalog == showCatalog).order_by(model.orderKey)
    query = filter_by_geodata_staging(query, model.staging, geodataStaging)
    results = [{
        'id': q.id,
        'langs': q.availableLangs,
        'showCatalog': q.showCatalog,
        'backgroundLayers': q.backgroundLayers if type(q.backgroundLayers) is list else q.backgroundLayers.split(','),
        'selectedLayers': q.selectedLayers if type(q.selectedLayers) is list else q.selectedLayers.split(',')
    } for q in query]
    return {'topics': results}
