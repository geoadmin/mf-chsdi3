# -*- coding: utf-8 -*-

import json
from pyramid.exceptions import HTTPNotFound
from pyramid.view import view_config
from pyramid.renderers import render_to_response
from pyramid.request import Request


available_versions = ['3.6.0', '3.18.2', '4.3.2', '4.4.2']


@view_config(route_name='ga_api', renderer='json')
def loadjs(request):
    mode = request.params.get('mode')
    ignore_polyfill = request.params.get('ignore_polyfill')
    # Determined automatically in subscriber
    lang = request.lang

    loader_js_bucket_localhost = request.registry.settings.get("loader_js_bucket_localhost", None)
    if loader_js_bucket_localhost:
        host_url = request.registry.settings["loader_js_bucket_localhost"]
    else:
        host_url = request.host_url

    # If version not provided fallback to the first entry
    version_str = request.params.get('version', available_versions[0])
    # If provided make sure the version exists
    if version_str not in available_versions:
        raise HTTPNotFound(
            'Version %s you request is not available, available versions are %s.' % (version_str, ', '.join(available_versions)))

    path = '/rest/services/api/MapServer/layersConfig?lang=%s' % lang
    subRequest = Request.blank(path)
    resp = request.invoke_subrequest(subRequest)
    data = json.loads(resp.body)

    s3_resources_path = 'resources/api/%s' % version_str
    mode_str = '-debug' if mode is not None else ''

    def get_resource_url(filename, extension, mode_str=''):
        return '%s/%s/%s%s.%s' % (
            host_url, s3_resources_path, filename, mode_str, extension)

    ga_css = get_resource_url('ga', 'css')
    ga_js = get_resource_url('ga', 'js', mode_str)
    epsg_21781_js = get_resource_url('EPSG21781', 'js')
    epsg_2056_js = get_resource_url('EPSG2056', 'js')

    disable_polyfill = request.registry.settings.get('disable_polyfill')
    polyfill_url = request.registry.settings.get('polyfill_url')

    response = render_to_response(
        'chsdi:templates/loader.js',
        {
            'lang': lang,
            'ga_css': ga_css,
            'ga_js': ga_js,
            'epsg_21781_js': epsg_21781_js,
            'epsg_2056_js': epsg_2056_js,
            'api_url': request.path_url.replace('/loader.js', ''),
            'ignore_polyfill': ignore_polyfill,
            'data': json.dumps(data, separators=(',', ':')),
            'disable_polyfill': disable_polyfill,
            'polyfill_url': polyfill_url
        },
        request=request
    )
    response.content_type = 'application/javascript'
    return response
