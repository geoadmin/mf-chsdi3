# -*- coding: utf-8 -*-

from pyramid.view import exception_view_config
from pyramid.httpexceptions import HTTPException


def format_exception_context(context):
    return {
        'detail': context.detail if context.detail else 'Unknown error',
        'status': 'error',
        'code': context.code if context.code else 500
    }


@exception_view_config(context=HTTPException)
def exception_view_json(context, request):
    accepted_mime = list(request.accept)
    if '*/*' in accepted_mime or 'application/json' in accepted_mime:
        context.json_body = format_exception_context(context)
        context.content_type = 'application/json'
    else:
        context.content_typ = 'text/html'

    return context
