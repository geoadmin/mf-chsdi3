# -*- coding: utf-8 -*-

from webob.acceptparse import Accept
from pyramid.view import exception_view_config
from pyramid.httpexceptions import HTTPException


def format_exception_context(context):
    return {
        'detail': context.detail if context.detail else 'Unknown error',
        'status': 'error',
        'code': context.code if context.code else 500
    }


@exception_view_config(context=HTTPException, renderer='json')
def exception_view_json(context, request):
    headers = dict(request.headers)
    accept_header = headers.get('Accept')
    if accept_header is None:
        return context
    accept_parser = Accept(accept_header)
    if '*/*' in accept_header or 'application/json' in accept_parser:
        context.json_body = format_exception_context(context)
        context.content_type = 'application/json'
    return context
