# -*- coding: utf-8 -*-

from pyramid.view import exception_view_config
from pyramid.httpexceptions import HTTPException
from pyramid.response import Response


class ViewExceptionJSON(HTTPException):

    def __init__(self, message, pyramid_exc):
        self.message = message
        self.pyramid_exc = pyramid_exc


@exception_view_config(ViewExceptionJSON, renderer='json')
def exception_view_json(exc):
    print(dir(exc))
    response = Response(body=exc.message)
    response.status_int = exc.pyramid_exc.code
    return Response
