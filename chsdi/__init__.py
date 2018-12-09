# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from pyramid.events import BeforeRender, NewRequest
from chsdi.subscribers import add_localizer, add_renderer_globals
from pyramid.renderers import JSONP
from sqlalchemy.orm import scoped_session, sessionmaker
from papyrus.renderers import GeoJSON

from chsdi.renderers import EsriJSON, CSVRenderer
from chsdi.models import initialize_sql


def db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        session.close()
    request.add_finished_callback(cleanup)

    return session


def add_cors_route(config, pattern, service, headers=None, methods=[]):
    # The use of "GET" also implies that the view will respond to "HEAD".
    allowed_methods = ['OPTIONS', 'HEAD']

    def view(request):  # pragma: no cover
        response = request.response
        response.cache_control.no_cache = True
        response.cache_control.max_age = 0
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = ','.join(
            allowed_methods + methods)
        if headers is not None:
            for k, v in headers.iteritems():
                response.headers[k] = v
        return response

    name = service + '_options'
    config.add_route(name, pattern, request_method=allowed_methods)
    config.add_view(view, route_name=name)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    app_version = settings.get('app_version')
    settings['app_version'] = app_version
    config = Configurator(settings=settings)
    config.include('pyramid_mako')

    # configure 'locale' dir as the translation dir for chsdi app
    config.add_translation_dirs('chsdi:locale/')
    config.add_subscriber(add_localizer, NewRequest)
    config.add_subscriber(add_renderer_globals, BeforeRender)

    # renderers
    config.add_mako_renderer('.html')
    config.add_mako_renderer('.js')
    config.add_renderer('jsonp', JSONP(param_name='callback', indent=None, separators=(',', ':')))
    config.add_renderer('geojson', GeoJSON(jsonp_param_name='callback'))
    config.add_renderer('esrijson', EsriJSON(jsonp_param_name='callback'))
    config.add_renderer('csv', CSVRenderer)

    # sql section
    config.registry.dbmaker = scoped_session(sessionmaker())
    config.add_request_method(db, reify=True)
    initialize_sql(settings)

    # route definitions
    config.add_route('dev', '/dev')
    config.add_route('ga_api', '/loader.js')
    config.add_route('testi18n', '/testi18n')
    config.add_route('topics', '/rest/services')
    config.add_route('mapservice', '/rest/services/{map}/MapServer')
    config.add_route('layersConfig', '/rest/services/{map}/MapServer/layersConfig')
    config.add_route('catalog', '/rest/services/{map}/CatalogServer')
    config.add_route('identify', '/rest/services/{map}/MapServer/identify')
    config.add_route('find', '/rest/services/{map}/MapServer/find')
    config.add_route('attribute_values', '/rest/services/{map}/MapServer/{layerId}/attributes/{attribute}')
    config.add_route('legend', '/rest/services/{map}/MapServer/{layerId}/legend')
    config.add_route('releases', '/rest/services/{map}/MapServer/{layerId}/releases')
    config.add_route('cacheUpdate', '/rest/services/{map}/MapServer/{layerId}/cacheUpdate')
    config.add_route('featureAttributes', '/rest/services/{map}/MapServer/{layerId}')
    config.add_route('feature', '/rest/services/{map}/MapServer/{layerId}/{featureId}')
    config.add_route('htmlPopup', '/rest/services/{map}/MapServer/{layerId}/{featureId}/htmlPopup')
    config.add_route('iframeHtmlPopup', '/rest/services/{map}/MapServer/{layerId}/{featureId}/iframeHtmlPopup')
    config.add_route('extendedHtmlPopup', '/rest/services/{map}/MapServer/{layerId}/{featureId}/extendedHtmlPopup')
    config.add_route('search', '/rest/services/{map}/SearchServer')
    config.add_route('wmtscapabilities', '/rest/services/{map}/1.0.0/WMTSCapabilities.xml')
    config.add_route('feedback', '/feedback')
    config.add_route('qrcodegenerator', '/qrcodegenerator')
    config.add_route('sitemap', '/sitemap')
    config.add_route('luftbilder', '/luftbilder/viewer.html')
    config.add_route('historicalmaps', '/historicalmaps/viewer.html')
    config.add_route('checker', '/checker')
    config.add_route('checker_dev', '/checker_dev')
    config.add_route('downloadkml', '/downloadkml')

    # kml files
    config.add_route('files_collection', '/files', request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/files',
                   'files_collection',
                   headers={'Access-Control-Allow-Credentials': 'true'},
                   methods=['GET', 'POST', 'DELETE'])
    config.add_route('files', '/files/{id}', request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/files/{id}',
                   'files',
                   headers={'Access-Control-Allow-Credentials': 'true'},
                   methods=['GET', 'POST', 'DELETE'])

    # glstyles json files
    config.add_route('glstyles_collection', '/glstyles', request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/glstyles',
                   'glstyles_collection',
                   headers={'Access-Control-Allow-Credentials': 'true'},
                   methods=['GET', 'POST', 'DELETE'])
    config.add_route('glstyles', '/glstyles/{id}', request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/glstyles/{id}',
                   'glstyles',
                   headers={'Access-Control-Allow-Credentials': 'true'},
                   methods=['GET', 'POST', 'DELETE'])

    config.add_route('adminkml', '/admin/kml')
    config.add_route('stationboard', '/stationboard/stops/{id}')
    config.add_route('faqlist', '/rest/services/{map}/faqlist')
    config.add_route('cut', '/rest/services/{map}/GeometryServer/cut')
    config.add_route('color', '/color/{r},{g},{b}/{image}')

    # Some views for specific routes
    config.add_view(route_name='dev', renderer='chsdi:templates/index.mako')
    config.add_view(route_name='testi18n', renderer='chsdi:templates/testi18n.mako')

    # Shortener
    config.add_route('shorten', '/shorten.json')
    config.add_route('shorten_redirect', '/shorten/{id}')

    # static view definitions
    config.add_static_view('static', 'chsdi:static')
    config.add_static_view('images', 'chsdi:static/images')
    config.add_static_view('examples', 'chsdi:static/doc/examples')
    config.add_static_view('vectorStyles', 'chsdi:static/vectorStyles')
    # keep this the last one
    config.add_static_view('/', 'chsdi:static/doc/build')

    # required to find code decorated by view_config
    config.scan(ignore=['chsdi.tests', 'chsdi.models.bod'])
    return config.make_wsgi_app()
