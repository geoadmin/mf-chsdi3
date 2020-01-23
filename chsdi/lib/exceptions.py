# -*- coding: utf-8 -*-

import pyramid.httpexceptions as exc


class HTTPBandwidthLimited(exc.HTTPServerError):
    code = 509
    title = 'Bandwidth Limit Exceeded'


class QueryParseException(Exception):
    pass


class CoordinatesTransformationException(Exception):
    pass


class CoordinatesRoundingException(Exception):
    pass
