from pyramid.view import view_config
from pyramid.httpexceptions import HTTPMovedPermanently


class Root(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='root', renderer='string')
    def root_view(self):
        """
        The destination view (the root '/'). Just in case.
        """
        # Raise the Moved Permanently exception (HTTP 301)
        raise HTTPMovedPermanently(location='https://docs.geo.admin.ch')
