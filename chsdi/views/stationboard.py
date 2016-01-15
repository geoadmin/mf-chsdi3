# -*- coding: utf-8 -*-


from sqlalchemy import and_
from sqlalchemy.exc import OperationalError
from pyramid.httpexceptions import HTTPInternalServerError, HTTPBadRequest
from pyramid.view import view_config, view_defaults
from chsdi.models.vector.uvek import OevDepartures
import datetime
from pytz import timezone


@view_defaults(renderer='jsonp', route_name='stationboard')
class TransportView(object):

    DEFAULT_LIMIT = 5

    MAX_LIMT = 20

    def __init__(self, request):
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
        current_date = datetime.datetime.now(timezone('Europe/Berlin'))
        filters = [OevDepartures.stop == self.id, OevDepartures.time > current_date]
        if self.destination != 'all':
            filters.append(OevDepartures.destination == self.destination)

        def serialize(t):
            return t.strftime('%H:%M')

        def serializeDate(t):
            return t.strftime('%d/%m/%Y %H:%M')

        query = self.request.db.query(OevDepartures).filter(and_(*filters)).order_by(
            OevDepartures.time
        ).limit(self.limit)

        try:
            # Not all the stations are in the table Haltestelle
            results = [{
                'id': q.stop,
                'time': serialize(q.time),
                'label': q.label,
                'via': q.via,
                'currentDate': serializeDate(current_date),
                'departureDate': serializeDate(q.time),
                'destinationName': q.haltestelle.name,
                'destinationId': q.haltestelle.id
            } for q in query if hasattr(q.haltestelle, 'id')]
        except OperationalError as e:  # pragma: no cover
            raise HTTPInternalServerError(e)

        if not results:
            return [{'destination': 'nodata'}]
        return results


@view_defaults(renderer='jsonp', route_name='stationboard_destination')
class DestinationView(object):

    def __init__(self, request):
        self.request = request
        if request.matched_route.name == 'stationboard_destination':
            id = request.matchdict['id']
            if id.isdigit() is False:
                raise HTTPBadRequest('The id must be an integer.')
            else:
                self.id = int(id)

    @view_config(request_method='GET')
    def get_destination(self):
        query = self.request.db.query(OevDepartures).filter(
            OevDepartures.stop == self.id
        ).distinct(OevDepartures.destination)

        try:
            # Not all the stations are in the table Haltestelle
            results = [{
                'id': q.haltestelle.id,
                'name': q.haltestelle.name
            } for q in query if hasattr(q.haltestelle, 'id')]
        except OperationalError as e:  # pragma: no cover
            raise HTTPInternalServerError(e)

        if not results:
            results = [{'destination': 'nodata'}]
        return results
