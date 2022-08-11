import logging
from webob.cachecontrol import CacheControl

logger = logging.getLogger(__name__)


def add_default_cache_control(request, response):
    # NOTE: response.cache_control is a webob.cachecontrol.CacheControl object and we need
    # to serialize it with str() to check if it has been already set.
    if not str(response.cache_control):
        dft_cache_control = request.registry.settings['default_cache_control']
        response.cache_control = CacheControl.parse(dft_cache_control, type='response')
