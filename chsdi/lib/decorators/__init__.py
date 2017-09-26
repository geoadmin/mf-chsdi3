# -*- coding: utf-8 -*-

from functools import wraps
import xml.parsers.expat

import pyramid.httpexceptions as exc

import urllib
import re


EXPECTED_CONTENT_TYPE = 'application/vnd.google-earth.kml+xml'


def requires_authorization():
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *args, **kwargs):
            if hasattr(self, 'request'):
                request = self.request
            else:
                request = self
            if request.headers.get('X-SearchServer-Authorized', '').lower() != 'true':
                raise exc.HTTPForbidden(detail='This service requires an authorization')
            else:
                return f(self, *args, **kwargs)
        return wrapped
    return wrapper


def validate_kml_input():
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if hasattr(self, 'request'):
                request = self.request
            else:
                request = self

            MAX_FILE_SIZE = 1024 * 1024 * 2

            # IE 9/10 doesn't send custom headers
            # webO default Content-Type to 'application/x-www-form-urlencoded' when not explictly set
            if request.content_type in (None, '', 'application/x-www-form-urlencoded'):
                request.content_type = EXPECTED_CONTENT_TYPE

            if request.content_type != EXPECTED_CONTENT_TYPE:
                raise exc.HTTPUnsupportedMediaType('Only KML file are accepted')
            # IE9 sends data urlencoded
            data = urllib.unquote_plus(request.body)
            if len(data) > MAX_FILE_SIZE:
                raise exc.HTTPRequestEntityTooLarge('File size exceed %s bytes' % MAX_FILE_SIZE)

            # Prevent erroneous kml
            data = re.sub('(\s+on\w*=(\"[^\"]+\"|\'[^\']+\'))', ' ', data, flags = re.I | re.M)
            data = re.sub('(<|&lt;)script\s*\S*[^(>|&gt;)]*?(>|&gt;)(.|\s)*?(<|&lt;)\/script(>|&gt;)', ' ', data, flags = re.I | re.M)
            try:
                p = xml.parsers.expat.ParserCreate()
                p.Parse(data)
            except Exception:
                raise exc.HTTPUnsupportedMediaType('Only valid KML file are accepted')

            request.body = data

            return func(self, *args, **kwargs)
        return wrapper
    return decorator
