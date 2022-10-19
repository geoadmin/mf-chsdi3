from logging_utilities.context import set_logging_context

from chsdi.lib import helpers


def logging_context_tween(handler, registry):

    def logging_context_tween(request):
        set_logging_context({
            "request": {
                "method": request.method,
                "path": request.path,
                "queryString": request.query_string,
                "headers": dict(request.headers),
                "payload": helpers.get_payload(request)
            }
        })
        return handler(request)

    return logging_context_tween
