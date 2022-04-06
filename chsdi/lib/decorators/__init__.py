# -*- coding: utf-8 -*-

from functools import wraps

# import pyramid.httpexceptions as exc


def requires_authorization():
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *args, **kwargs):
            # deativated by boc due to unplanned changes in varnish
            # if hasattr(self, 'request'):
            #    request = self.request
            # else:
            #    request = self
            # if request.headers.get('X-SearchServer-Authorized', '').lower() != 'true':
            #    raise exc.HTTPForbidden(detail='This service requires an authorization')
            # else:
            #    return f(self, *args, **kwargs)
            return f(self, *args, **kwargs)

        return wrapped

    return wrapper
