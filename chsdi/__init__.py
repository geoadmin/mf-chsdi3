# -*- coding: utf-8 -*-

from pyramid.config import Configurator
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.events import BeforeRender, NewRequest
from chsdi.subscribers import add_localizer, add_renderer_globals, add_cors_to_response
from chsdi.predicates import CorsPreflightPredicate
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


# CORS stuff from https://gist.github.com/mmerickel/1afaf64154b335b596e4
def add_cors_preflight_handler(config):
    config.add_route(
        'cors-options-preflight', '/{catch_all:.*}',
        cors_preflight=True,
    )
    config.add_view(
        cors_options_view,
        route_name='cors-options-preflight',
        permission=NO_PERMISSION_REQUIRED,
    )


def cors_options_view(context, request):
    response = request.response
    response.headers['Access-Control-Allow-Methods'] = (
        'OPTIONS,HEAD,GET,POST,PUT,DELETE')
    response.headers['Access-Control-Allow-Headers'] = (
        'Content-Type,Accept,Accept-Language,Authorization,X-Request-ID')
    return response


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

    # CORS, before all other routes as OPTIONS catch all
    config.add_directive(
        'add_cors_preflight_handler', add_cors_preflight_handler)
    config.add_route_predicate('cors_preflight', CorsPreflightPredicate)
    config.add_subscriber(add_cors_to_response, 'pyramid.events.NewResponse')

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
    config.add_route('dev', '/dev', request_method='GET,OPTIONS,HEAD')
    # JS API loader
    config.add_route('ga_api', '/loader.js', request_method='GET')

    config.add_route('testi18n', '/testi18n', request_method='GET')
    # List topics
    config.add_route('topics', '/rest/services')
    # Returns layers metdata
    config.add_route('mapservice',
                     '/rest/services/{map}/MapServer',
                     request_method='GET')
    # Returns the technical configuration of the layers in geoadmin
    config.add_route('layersConfig',
                     '/rest/services/{map}/MapServer/layersConfig',
                     request_method='GET')
    # Returns a tree like structure for catalogs
    config.add_route('catalog',
                     '/rest/services/{map}/CatalogServer',
                     request_method='GET')
    # Identify features in DB with a spatial and/or a attribute filter
    config.add_route('identify',
                     '/rest/services/{map}/MapServer/identify',
                     request_method='GET')
    # Find features in DB
    config.add_route('find',
                     '/rest/services/{map}/MapServer/find',
                     request_method='GET')
    # Returns attributes types and values
    config.add_route('attribute_values',
                     '/rest/services/{map}/MapServer/{layerId}/attributes/{attribute}',
                     request_method='GET')
    # Get the legend of a layer
    config.add_route('legend',
                     '/rest/services/{map}/MapServer/{layerId}/legend',
                     request_method='GET')
    # Zeitreihen only service
    config.add_route('releases',
                     '/rest/services/{map}/MapServer/{layerId}/releases',
                     request_method='GET')
    # Info about latestest WMTS tile update per layer
    config.add_route('cacheUpdate',
                     '/rest/services/{map}/MapServer/{layerId}/cacheUpdate',
                     request_method='GET')
    # Returns the type and a sample of a feature attributes
    config.add_route('featureAttributes',
                     '/rest/services/{map}/MapServer/{layerId}',
                     request_method='GET')
    # Returns of a feature object
    config.add_route('feature',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}',
                     request_method='GET')
    # Returns an html popup
    config.add_route('htmlPopup',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}/htmlPopup',
                     request_method='GET')
    # Returns an html popup in an iframe
    config.add_route('iframeHtmlPopup',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}/iframeHtmlPopup',
                     request_method='GET')
    # Returns an extended html popup
    config.add_route('extendedHtmlPopup',
                     '/rest/services/{map}/MapServer/{layerId}/{featureId}/extendedHtmlPopup',
                     request_method='GET')
    # Search using SphinxSearch
    config.add_route('search',
                     '/rest/services/{map}/SearchServer',
                     request_method='GET')
    # WMTS GetCapabilities document generation
    config.add_route('wmtscapabilities',
                     '/rest/services/{map}/1.0.0/WMTSCapabilities.xml',
                     request_method='GET')
    # Sends emails feedbacks
    config.add_route('feedback', '/feedback', request_method='POST')
    # Generates a qrcode
    config.add_route('qrcodegenerator',
                     '/qrcodegenerator',
                     request_method='GET')
    # Generates a sitemap for SEO
    config.add_route('sitemap', '/sitemap', request_method='GET')
    # Custom view for lufbilder individual images
    config.add_route('luftbilder',
                     '/luftbilder/viewer.html',
                     request_method='GET')
    # Custom view for zeitreigen, pk50 and pk25 individual map sheets
    config.add_route('historicalmaps',
                     '/historicalmaps/viewer.html',
                     request_method='GET')
    # Checks if the app is alive
    config.add_route('checker',
                     '/checker',
                     request_method='GET')
    # Download a KML created in geoadmin
    config.add_route('downloadkml',
                     '/downloadkml',
                     request_method='POST')
    # KML files handling, creation of the first entry
    config.add_route('files_collection',
                     '/files',
                     request_method=('GET', 'POST', 'DELETE'))
    # KML files handling, after the first one was created
    config.add_route('files',
                     '/files/{id}',
                     request_method=('GET', 'POST', 'DELETE'))

    # glstyles json files
    config.add_route('glstyles_collection', '/gl-styles', request_method=('GET', 'POST', 'DELETE'))
    config.add_route('glstyles', '/gl-styles/{id}', request_method=('GET', 'POST', 'DELETE'))

    # Admin KML page via simple auth
    config.add_route('adminkml',
                     '/admin/kml',
                     request_method='GET')
    # OpendataTrans API integration
    config.add_route('stationboard',
                     '/stationboard/stops/{id}',
                     request_method='GET')
    # Service for faqlist generation in API doc
    config.add_route('faqlist',
                     '/rest/services/{map}/faqlist',
                     request_method='GET')
    # Shop service cut
    config.add_route('cut',
                     '/rest/services/{map}/GeometryServer/cut',
                     request_method='GET')
    # Color service for kml icons
    config.add_route('color',
                     '/color/{r},{g},{b}/{image}',
                     request_method='GET')
    # Shortener
    config.add_route('shorten',
                     '/shorten.json',
                     request_method='GET')
    config.add_route('shorten_redirect',
                     '/shorten/{id}',
                     request_method='GET')

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
