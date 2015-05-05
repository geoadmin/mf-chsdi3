# -*- coding: utf-8 -*-

from pyramid.view import view_config

from chsdi.models.bod import Topics
from chsdi.lib.filters import filter_by_geodata_staging
from chsdi.lib.helpers import get_debug_headerlist


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
        'backgroundLayers': q.backgroundLayers,
        'selectedLayers': q.selectedLayers
    } for q in query]
    request.response.headerlist.extend(get_debug_headerlist(request.registry.settings))
    return {'topics': results}
