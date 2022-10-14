from distutils.util import strtobool
import cachetools.func
import time

from pyramid.events import NewRequest
from pyramid.events import BeforeRender
from pyramid.events import NewResponse
from pyramid.events import subscriber
from pyramid.i18n import get_localizer, TranslationStringFactory
from chsdi.lib import helpers
from chsdi.models.bod import get_translations
from chsdi.response_callbacks import add_default_cache_control
from chsdi.response_callbacks import add_cors_header
from chsdi.response_callbacks import add_cross_domain_policy


import logging

# Interval (sec) between two request to translation table
DYNAMIC_TRANSLATION_TTL = 3600

log = logging.getLogger(__name__)
route_logger = logging.getLogger('route')


@subscriber(BeforeRender)
def add_renderer_globals(event):
    request = event.get('request')
    if request:
        event['_'] = request.translate
        event['localizer'] = request.localizer
        event['h'] = helpers

tsf = TranslationStringFactory('chsdi')


@cachetools.func.ttl_cache(ttl = DYNAMIC_TRANSLATION_TTL)
def update_localizer(lang, localizer, session):
    # At this point the localizer is read. We update the translation catalog from the translation
    # table in the BOD, if required.

    translations = get_translations(lang, session)

    if translations is not None:
        if 'chsdi' in localizer.translations._domains.keys():
            localizer.translations._domains['chsdi']._catalog = translations
        else:
            log.error("Cannot update localizer. Inexisting domain.")
    else:
        log.error("Cannot update the 'localizer'. Empty catalog.")
    return localizer


@subscriber(NewRequest)
def add_localizer(event):
    request = event.request
    request._LOCALE_ = helpers.locale_negotiator(request)
    localizer = get_localizer(request)
    request.lang = 'rm' if localizer.locale_name == 'fi' else localizer.locale_name

    def auto_translate(string):
        return localizer.translate(tsf(string))
    request.localizer = localizer
    request.translate = auto_translate

    settings = request.registry.settings
    use_dynamic_translation = strtobool(settings.get('dynamic_translation', '1'))

    if use_dynamic_translation:
        request.localizer = update_localizer(request.lang, request.localizer, request.db)


def get_payload(obj):
    if not obj.content_length:
        return ''
    if obj.content_type in [
        'application/json',
        'application/javascript',
        'text/javascript',
        'text/css',
        'text/plain',
        'text/html'
    ]:
        return obj.text[:128]
    return '<not a text format>'


def get_request_for_logging(req):
    data = {
        "path": req.path,
        "method": req.method,
        "query_string": req.query_string,
        "headers": dict(req.headers),
        "payload": get_payload(req)
    }
    return data


@subscriber(NewRequest)
def log_request(event):
    setattr(event.request, 'started_at', time.time())
    if route_logger.isEnabledFor(logging.INFO):
        route_logger.debug(
            '%s %s',
            event.request.method,
            event.request.path_qs,
            extra={
                "request": get_request_for_logging(event.request)
            }
        )


@subscriber(NewRequest)
def setup_response_callbacks(event):
    event.request.add_response_callback(add_default_cache_control)
    event.request.add_response_callback(add_cors_header)
    event.request.add_response_callback(add_cross_domain_policy)


@subscriber(NewResponse)
def log_response(event):
    if route_logger.isEnabledFor(logging.INFO):
        started_at = getattr(event.request, 'started_at', None)
        route_logger.info(
            '%s %s %s',
            event.request.method,
            event.request.path_qs,
            event.response.status,
            extra={
                "duration": time.time() - started_at if started_at else '',
                "request": get_request_for_logging(event.request),
                "response": {
                    "status_code": event.response.status,
                    "headers": {h[0]: h[1] for h in event.response.headerlist},
                    "payload": get_payload(event.response)
                }
            }
        )
