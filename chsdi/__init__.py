# -*- coding: utf-8 -*-

import datetime
from pyramid.config import Configurator
from pyramid.renderers import JSONP
from pyramid.request import Request
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


class WsgiSchemeAdaptedRequest(Request):
    # TODO: remove this class, once apache is removed
    # (https://jira.swisstopo.ch/browse/BGDIINF_SB-2486).
    # Afterwards this can be solved similarly to our flask services using
    # e.g. gunicorn.
    def __init__(self, environ, **kwargs):
        if "HTTP_CLOUDFRONT_FORWARDED_PROTO" in environ:
            environ["wsgi.url_scheme"] = environ["HTTP_CLOUDFRONT_FORWARDED_PROTO"]
        elif "HTTP_X_FORWARDED_PROTO" in environ:
            environ["wsgi.url_scheme"] = environ["HTTP_X_FORWARDED_PROTO"]
        super().__init__(environ, **kwargs)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    app_version = settings.get('app_version')
    settings['app_version'] = app_version
    # TODO: request_factory can be removed, once apache is removed, see few
    # lines above.
    config = Configurator(settings=settings, request_factory=WsgiSchemeAdaptedRequest)
    config.include('pyramid_mako')
    config.include('akhet.static')

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
    config.add_route('luftbilder', '/luftbilder/viewer.html')
    config.add_route('historicalmaps', '/historicalmaps/viewer.html')
    config.add_route('checker', '/checker')
    config.add_route('checker_dev', '/checker_dev')
    config.add_route('translations', '/rest/services/translations')

    config.add_route('stationboard', '/stationboard/stops/{id}')
    config.add_route('faqlist', '/rest/services/{map}/faqlist')
    config.add_route('color', '/color/{r},{g},{b}/{image}')

    # Some new style routes used by the viewer see geoadmin/mf-geoadmin3 PR #4687 and geoadmin/web-mapviewer
    config.add_route('layersConfig-1', '/configs/{lang:\w\w}/layersConfig.json')
    config.add_route('translations-1', '/configs/{lang:\w\w}/translations.json')
    config.add_route('catalog-1', '/configs/{lang:\w\w}/catalog.{map:\w+}.json')
    # This route is only used by the new viewer geoadmin/web-mapviewer
    config.add_route('topics-1', '/configs/services.json')
    # The following route doesn't seems to be used anymore
    # config.add_route('topics-2', '/configs/{lang:\w\w}/services.json')

    # Static route
    config.add_static_route('chsdi', 'static')

    # Some views for specific routes
    config.add_view(route_name='dev', renderer='chsdi:templates/index.mako')
    config.add_view(route_name='testi18n', renderer='chsdi:templates/testi18n.mako')

    # static view definitions
    config.add_static_view('static', 'chsdi:static')
    config.add_static_view('images', 'chsdi:static/images')
    config.add_static_view('js', 'chsdi:static/js')
    config.add_static_view('examples', 'chsdi:static/doc/examples')
    config.add_static_view('vectorStyles', 'chsdi:static/vectorStyles')
    # keep this the last one
    config.add_static_view('/', 'chsdi:static/doc/build')

    # required to find code decorated by view_config
    config.scan(ignore=['chsdi.tests', 'chsdi.models.bod'])
    return config.make_wsgi_app()
