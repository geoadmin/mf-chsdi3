# -*- coding: utf-8 -*-
import os
from distutils.util import strtobool
import datetime
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import JSONP
from pyramid.request import Request
from sqlalchemy.orm import scoped_session, sessionmaker
from papyrus.renderers import GeoJSON

from chsdi.logging_setup import setup_logging
from chsdi.renderers import EsriJSON, CSVRenderer
from chsdi.models import initialize_sql


def db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        session.close()
    request.add_finished_callback(cleanup)

    return session


class WsgiSchemeAdaptedRequest(Request):
    def __init__(self, environ, **kwargs):
        if "HTTP_CLOUDFRONT_FORWARDED_PROTO" in environ:
            environ["wsgi.url_scheme"] = environ["HTTP_CLOUDFRONT_FORWARDED_PROTO"]
        elif "HTTP_X_FORWARDED_PROTO" in environ:
            environ["wsgi.url_scheme"] = environ["HTTP_X_FORWARDED_PROTO"]
        super().__init__(environ, **kwargs)


# This is a wrapper function around all views. If OPTIONS is given, an empty string will be returned
# As HTTP OPTIONS is not cached, this wrapper will safe some power
def options_view(view, info):
    def wrapper_view(context, request):
        if request.method == 'OPTIONS':
            return Response('')
        return view(context, request)
    return wrapper_view


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # Do not setup logging during unittest to avoid overwritting the unittest logging setup
    if not strtobool(os.getenv('TEST_APP', '0')):
        setup_logging()

    app_version = settings.get('app_version')
    settings['app_version'] = app_version
    # request_method is the type tuple: string->string without space->array->tuple
    request_method = tuple(settings.get('request_method').replace(' ', '').split(','))
    config = Configurator(settings=settings, request_factory=WsgiSchemeAdaptedRequest)
    config.include('pyramid_mako')
    config.include('akhet.static')
    # wrapper around all views
    config.add_view_deriver(options_view)

    # configure 'locale' dir as the translation dir for chsdi app
    config.add_translation_dirs('chsdi:locale/')

    # renderers
    config.add_mako_renderer('.html')
    config.add_mako_renderer('.js')

    json_renderer = JSONP(param_name='callback', indent=None, separators=(',', ':'))

    def datetime_adapter(obj, request):
        return obj.isoformat()
    json_renderer.add_adapter(datetime.datetime, datetime_adapter)
    config.add_renderer('jsonp', json_renderer)
    config.add_renderer('geojson', GeoJSON(jsonp_param_name='callback'))
    config.add_renderer('esrijson', EsriJSON(jsonp_param_name='callback'))
    config.add_renderer('csv', CSVRenderer)

    # sql section
    config.registry.dbmaker = scoped_session(sessionmaker())
    config.add_request_method(db, reify=True)
    initialize_sql(settings)

    # route definitions
    config.add_route('dev', '/dev', request_method=request_method)
    config.add_route('ga_api', '/loader.js', request_method=request_method)
    config.add_route('testi18n', '/testi18n', request_method=request_method)
    config.add_route('topics', '/rest/services', request_method=request_method)
    config.add_route('mapservice', '/rest/services/{map}/MapServer', request_method=request_method)
    config.add_route('layersConfig', '/rest/services/{map}/MapServer/layersConfig', request_method=request_method)
    config.add_route('catalog', '/rest/services/{map}/CatalogServer', request_method=request_method)
    config.add_route('identify', '/rest/services/{map}/MapServer/identify', request_method=request_method)
    config.add_route('find', '/rest/services/{map}/MapServer/find', request_method=request_method)
    config.add_route('attribute_values', '/rest/services/{map}/MapServer/{layerId}/attributes/{attribute}', request_method=request_method)
    config.add_route('legend', '/rest/services/{map}/MapServer/{layerId}/legend', request_method=request_method)
    config.add_route('releases', '/rest/services/{map}/MapServer/{layerId}/releases', request_method=request_method)
    config.add_route('cacheUpdate', '/rest/services/{map}/MapServer/{layerId}/cacheUpdate', request_method=request_method)
    config.add_route('featureAttributes', '/rest/services/{map}/MapServer/{layerId}', request_method=request_method)
    config.add_route('feature', '/rest/services/{map}/MapServer/{layerId}/{featureId}', request_method=request_method)
    config.add_route('htmlPopup', '/rest/services/{map}/MapServer/{layerId}/{featureId}/htmlPopup', request_method=request_method)
    config.add_route('iframeHtmlPopup', '/rest/services/{map}/MapServer/{layerId}/{featureId}/iframeHtmlPopup', request_method=request_method)
    config.add_route('extendedHtmlPopup', '/rest/services/{map}/MapServer/{layerId}/{featureId}/extendedHtmlPopup', request_method=request_method)
    config.add_route('luftbilder', '/luftbilder/viewer.html', request_method=request_method)
    config.add_route('historicalmaps', '/historicalmaps/viewer.html', request_method=request_method)
    config.add_route('checker', '/checker', request_method=request_method)
    config.add_route('checker_dev', '/checker_dev', request_method=request_method)
    config.add_route('translations', '/rest/services/translations', request_method=request_method)

    config.add_route('stationboard', '/stationboard/stops/{id}', request_method=request_method)
    config.add_route('faqlist', '/rest/services/{map}/faqlist', request_method=request_method)
    config.add_route('color', '/color/{r},{g},{b}/{image}', request_method=request_method)

    # Static route
    static_max_age = int(settings['static_max_age']) if settings['static_max_age'] else None
    config.add_static_route('chsdi', 'static', cache_max_age=static_max_age)

    # Some views for specific routes
    config.add_view(route_name='dev', renderer='chsdi:templates/index.mako')
    config.add_view(route_name='testi18n', renderer='chsdi:templates/testi18n.mako')

    # static view definitions
    config.add_static_view('static', 'chsdi:static', cache_max_age=static_max_age)
    config.add_static_view('images', 'chsdi:static/images', cache_max_age=static_max_age)
    config.add_static_view('js', 'chsdi:static/js', cache_max_age=static_max_age)
    config.add_static_view('examples', 'chsdi:static/doc/examples', cache_max_age=static_max_age)
    config.add_static_view('vectorStyles', 'chsdi:static/vectorStyles', cache_max_age=static_max_age)
    # keep this the last one
    config.add_static_view('/', 'chsdi:static/doc/build', cache_max_age=static_max_age)

    # required to find code decorated by view_config
    config.scan(ignore=['chsdi.tests', 'chsdi.models.bod'])
    return config.make_wsgi_app()
