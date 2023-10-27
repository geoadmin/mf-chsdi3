import logging
from webob.cachecontrol import CacheControl

logger = logging.getLogger(__name__)


def add_default_cache_control(request, response):
    # NOTE: response.cache_control is a webob.cachecontrol.CacheControl object and we need
    # to serialize it with str() to check if it has been already set.
    if not str(response.cache_control):
        dft_cache_control = request.registry.settings['default_cache_control']
        response.cache_control = CacheControl.parse(dft_cache_control, type='response')

    # overwrite with these 5xx cache settings
    # no cache on these 5xx errors, they are supposed to be temporary
    if response.status_code in (502, 503, 504, 507):
        response.cache_control = CacheControl.parse('no-cache', type='response')
    # short cache duration for other 5xx errors
    elif response.status_code >= 500:
        response.cache_control = CacheControl.parse('public, max-age=10', type='response')


def add_cors_header(request, response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS"
    response.headers['Access-Control-Allow-Headers'] = "*"


def add_cross_domain_policy(request, response):
    # Check if the request is a cross domain policy request
    if request.path in ['/crossdomain.xml', '/clientaccesspolicy.xml']:
        response.headers['Content-Type'] = 'text/x-cross-domain-policy'
