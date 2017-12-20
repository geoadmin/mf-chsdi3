# -*- coding: utf-8 -*-


from pyramid.httpexceptions import HTTPInternalServerError, HTTPBadRequest, HTTPServiceUnavailable, HTTPTooManyRequests, HTTPNotFound
from requests.exceptions import RequestException
from pyramid.view import view_config, view_defaults
from chsdi.lib.opentransapi import opentransapi
from pyramid.threadlocal import get_current_registry


@view_defaults(renderer='jsonp', route_name='stationboard')
class TransportView(object):

    DEFAULT_LIMIT = 5

    MAX_LIMT = 20

    def __init__(self, request):
        self.opentrans_api_key = get_current_registry().settings['opentrans_api_key']  # Get API key from config .ini
        if self.opentrans_api_key == '':
            raise HTTPInternalServerError('The opentrans_api_key has no value, is registeret in .ini')
        self.ot_api = opentransapi.OpenTrans(self.opentrans_api_key)
        self.request = request
        if request.matched_route.name == 'stationboard':
            id = request.matchdict['id']
            if id.isdigit() is False:
                raise HTTPBadRequest('The id must be an integer.')
            else:
                self.id = int(id)

            self.destination = request.params.get('destination', 'all')

            limit = request.params.get('limit')
            if limit:
                if limit.isdigit():
                    self.limit = min(int(limit), self.MAX_LIMT)
                else:
                    raise HTTPBadRequest('The limit parameter must be an integer.')
            else:
                self.limit = self.DEFAULT_LIMIT

    @view_config(request_method='GET')
    def get_departures(self):
        try:
            results = self.ot_api.get_departures(self.id, self.limit)
        except opentransapi.OpenTransRateLimitException as e:
            raise HTTPTooManyRequests(str(e))  # limit API exceeded
        except opentransapi.OpenTransNoStationException as e:
            raise HTTPNotFound(str(e))  # no station for this request
        except (RequestException, opentransapi.OpenTransException) as e:
            raise HTTPServiceUnavailable(str(e))
        return results
