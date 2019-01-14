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
    # TODO: should add_route not also consider 'methods' from args?
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
    config.add_renderer('jsonp',
                        JSONP(param_name='callback',
                              indent=None,
                              separators=(',', ':')))
    config.add_renderer('geojson', GeoJSON(jsonp_param_name='callback'))
    config.add_renderer('esrijson', EsriJSON(jsonp_param_name='callback'))
    config.add_renderer('csv', CSVRenderer)

    # sql section
    config.registry.dbmaker = scoped_session(sessionmaker())
    config.add_request_method(db, reify=True)
    initialize_sql(settings)

    # route definitions
    # Dev page with bunch of demo links
    config.add_route('dev', '/dev', request_method='GET')
    # JS API loader
    config.add_route('ga_api', '/loader.js', request_method='GET')
    add_cors_route(config, '/loader.js', 'ga_api', methods=['GET'])

    config.add_route('testi18n', '/testi18n', request_method='GET')
    # List topics
    config.add_route('topics', '/rest/services')
    add_cors_route(config, '/rest/services', 'topics', methods=['GET'])
    # Returns layers metdata
    config.add_route('mapservice',
                     '/rest/services/{map}/MapServer',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer',
                   'mapservice',
                   methods=['GET'])
    # Returns the technical configuration of the layers in geoadmin
    config.add_route('layersConfig',
                     '/rest/services/{map}/MapServer/layersConfig',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/layersConfig',
                   'layersConfig',
                   methods=['GET'])
    # Returns a tree like structure for catalogs
    config.add_route('catalog',
                     '/rest/services/{map}/CatalogServer',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/CatalogServer',
                   'catalog',
                   methods=['GET'])
    # Identify features in DB with a spatial and/or a attribute filter
    config.add_route('identify',
                     '/rest/services/{map}/MapServer/identify',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/identify',
                   'identify',
                   methods=['GET'])
    # Find features in DB
    config.add_route('find',
                     '/rest/services/{map}/MapServer/find',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/find',
                   'find',
                   methods=['GET'])
    # Returns attributes types and values
    config.add_route('attribute_values',
                     '/rest/services/{map}/MapServer/{layerId}/attributes/{attribute}',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/attributes/{attribute}',
                   'attribute_values',
                   methods=['GET'])
    # Get the legend of a layer
    config.add_route('legend',
                     '/rest/services/{map}/MapServer/{layerId}/legend',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/legend',
                   'legend',
                   methods=['GET'])
    # Zeitreihen only service
    config.add_route('releases',
                     '/rest/services/{map}/MapServer/{layerId}/releases',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/releases',
                   'releases',
                   methods=['GET'])
    # Info about latestest WMTS tile update per layer
    config.add_route('cacheUpdate',
                     '/rest/services/{map}/MapServer/{layerId}/cacheUpdate',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/cacheUpdate',
                   'cacheUpdate',
                   methods=['GET'])
    # Returns the type and a sample of a feature attributes
    config.add_route('featureAttributes',
                     '/rest/services/{map}/MapServer/{layerId}',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}',
                   'featureAttributes',
                   methods=['GET'])
    # Returns of a feature object
    config.add_route('feature',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/{featureId}',
                   'feature',
                   methods=['GET'])
    # Returns an html popup
    config.add_route('htmlPopup',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}/htmlPopup',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/{featureId}/htmlPopup',
                   'htmlPopup',
                   methods=['GET'])
    # Returns an html popup in an iframe
    config.add_route('iframeHtmlPopup',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}/iframeHtmlPopup',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/{featureId}/iframeHtmlPopup',
                   'iframeHtmlPopup',
                   methods=['GET'])
    # Returns an extended html popup
    config.add_route('extendedHtmlPopup',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}/extendedHtmlPopup',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/MapServer/{layerId}/{featureId}/extendedHtmlPopup',
                   'extendedHtmlPopup',
                   methods=['GET'])
    # Search using SphinxSearch
    config.add_route('search',
                     '/rest/services/{map}/SearchServer',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/SearchServer',
                   'search',
                   methods=['GET'])
    # WMTS GetCapabilities document generation
    config.add_route('wmtscapabilities',
                     '/rest/services/{map}/1.0.0/WMTSCapabilities.xml',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/1.0.0/WMTSCapabilities.xml',
                   'wmtscapabilities',
                   methods=['GET'])
    # Sends emails feedbacks
    config.add_route('feedback', '/feedback', request_method='POST')
    add_cors_route(config, '/feedback', 'feedback', methods=['POST'])
    # Generates a qrcode
    config.add_route('qrcodegenerator',
                     '/qrcodegenerator',
                     request_method='GET')
    add_cors_route(config,
                   '/qrcodegenerator',
                   'qrcodegenerator',
                   methods=['GET'])
    # Generates a sitemap for SEO
    config.add_route('sitemap', '/sitemap', request_method='GET')
    add_cors_route(config,
                   '/sitemap',
                   'sitemap',
                   methods=['GET'])
    # Custom view for lufbilder individual images
    config.add_route('luftbilder',
                     '/luftbilder/viewer.html',
                     request_method='GET')
    add_cors_route(config,
                   '/luftbilder/viewer.html',
                   'luftbilder')
    # Custom view for zeitreigen, pk50 and pk25 individual map sheets
    config.add_route('historicalmaps',
                     '/historicalmaps/viewer.html',
                     request_method='GET')
    add_cors_route(config,
                   '/historicalmaps/viewer.html',
                   'historicalmaps',
                   methods=['GET'])
    # Checks if the app is alive
    config.add_route('checker',
                     '/checker',
                     request_method='GET')
    add_cors_route(config,
                   '/checker',
                   'checker',
                   methods=['GET'])
    # Download a KML created in geoadmin
    config.add_route('downloadkml',
                     '/downloadkml',
                     request_method='POST')
    add_cors_route(config,
                   '/downloadkml',
                   'downloadkml',
                   methods=['POST'])
    # KML files handling, creation of the first entry
    config.add_route('files_collection',
                     '/files',
                     request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/files',
                   'files_collection',
                   headers={
                       'Access-Control-Allow-Credentials': 'true'
                   },
                   methods=['GET', 'POST', 'DELETE'])
    # KML files handling, after the first one was created
    config.add_route('files',
                     '/files/{id}',
                     request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/files/{id}',
                   'files',
                   headers={
                       'Access-Control-Allow-Credentials': 'true'
                   },
                   methods=['GET', 'POST', 'DELETE'])

    # glstyles json files
    config.add_route('glstyles_collection', '/gl-styles', request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/gl-styles',
                   'glstyles_collection',
                   headers={'Access-Control-Allow-Credentials': 'true'},
                   methods=['GET', 'POST', 'DELETE'])
    config.add_route('glstyles', '/gl-styles/{id}', request_method=('GET', 'POST', 'DELETE'))
    add_cors_route(config,
                   '/gl-styles/{id}',
                   'glstyles',
                   headers={'Access-Control-Allow-Credentials': 'true'},
                   methods=['GET', 'POST', 'DELETE'])

    config.add_route('adminkml', '/admin/kml')
    config.add_route('stationboard', '/stationboard/stops/{id}')
    config.add_route('faqlist', '/rest/services/{map}/faqlist')
    config.add_route('cut', '/rest/services/{map}/GeometryServer/cut')
    config.add_route('color', '/color/{r},{g},{b}/{image}')
    # Admin KML page via simple auth
    config.add_route('adminkml',
                     '/admin/kml',
                     request_method='GET')
    add_cors_route(config,
                   '/admin/kml',
                   'adminkml',
                   methods=['GET'])
    # OpendataTrans API integration
    config.add_route('stationboard',
                     '/stationboard/stops/{id}',
                     request_method='GET')
    add_cors_route(config,
                   '/stationboard/stops/{id}',
                   'stationboard',
                   methods=['GET'])
    # Service for faqlist generation in API doc
    config.add_route('faqlist',
                     '/rest/services/{map}/faqlist',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/faqlist',
                   'faqlist',
                   methods=['GET'])
    # Shop service cut
    config.add_route('cut',
                     '/rest/services/{map}/GeometryServer/cut',
                     request_method='GET')
    add_cors_route(config,
                   '/rest/services/{map}/GeometryServer/cut',
                   'cut',
                   methods=['GET'])
    # Color service for kml icons
    config.add_route('color',
                     '/color/{r},{g},{b}/{image}',
                     request_method='GET')
    add_cors_route(config,
                   '/color/{r},{g},{b}/{image}',
                   'color',
                   methods=['GET'])
    # Shortener
    config.add_route('shorten',
                     '/shorten.json',
                     request_method='GET')
    add_cors_route(config,
                   '/shorten.json',
                   'shorten',
                   methods=['GET'])
    config.add_route('shorten_redirect',
                     '/shorten/{id}',
                     request_method='GET')
    add_cors_route(config,
                   '/shorten/{id}',
                   'shorten_redirect',
                   methods=['GET'])

    # Some views for specific routes
    config.add_view(route_name='dev',
                    renderer='chsdi:templates/index.mako',
                    request_method='GET')
    config.add_view(route_name='testi18n',
                    renderer='chsdi:templates/testi18n.mako',
                    request_method='GET')

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
