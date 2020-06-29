# -*- coding: utf-8 -*-

import six
from distutils.util import strtobool
import cachetools.func

from pyramid.i18n import get_localizer, TranslationStringFactory
from chsdi.lib import helpers
from chsdi.models.bod import get_translations


import logging

# Interval (sec) between two request to translation table
DYNAMIC_TRANSLATION_TTL = 3600

log = logging.getLogger(__name__)


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
    # table in the BOD, if reuired.

    translations = get_translations(lang, session)

    if translations is not None and 'chsdi' in localizer.translations._domains.keys():
        localizer.translations._domains['chsdi']._catalog = translations
    else:
        log.error("Cannot add BOD translations to the 'localizer'. Inexisting domain or empty catalog.")
    return localizer


def add_localizer(event):
    request = event.request
    request._LOCALE_ = helpers.locale_negotiator(request)
    localizer = get_localizer(request)
    request.lang = 'rm' if localizer.locale_name == 'fi' else localizer.locale_name
    # Python2/3
    if not six.PY3:
        request.lang = request.lang.encode('ascii', 'ignore')
    # The load balancer forwards requests as http, therefore we need to check X-Forwarded-Proto
    request.scheme = request.headers.get('X-Forwarded-Proto', request.scheme)

    def auto_translate(string):
        return localizer.translate(tsf(string))
    request.localizer = localizer
    request.translate = auto_translate

    settings = request.registry.settings
    use_dynamic_translation = strtobool(settings.get('dynamic_translation', '1'))

    if use_dynamic_translation:
        request.localizer = update_localizer(request.lang, request.localizer, request.db)
