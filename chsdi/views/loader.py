# -*- coding: utf-8 -*-

from pyramid.view import view_config
from pyramid.renderers import render_to_response


@view_config(route_name='ga_api', renderer='json')
def loadjs(request):
    mode = request.params.get('mode')
    topic = request.params.get('topic')
    response = render_to_response(
        'chsdi:templates/loader.js',
        {
            'mode': mode,
            'topic': topic if topic is not None else 'api'
        },
        request=request
    )
    response.content_type = 'application/javascript'
    return response
