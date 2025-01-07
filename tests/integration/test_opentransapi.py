# -*- coding: utf-8 -*-
from datetime import datetime
from unittest.mock import Mock
from unittest.mock import patch

from pytz import timezone
from pyramid.httpexceptions import HTTPBadRequest
import requests_mock

from chsdi.lib.opentransapi import opentransapi
from chsdi.lib.opentransapi.opentransapi import format_time
from chsdi.views.stationboard import TransportView
from tests.integration import TestsBase
from tests.integration.helpers import generate_mock_response
from tests.integration.helpers import generate_mock_empty_response


class TestOpenTransApi(TestsBase):
    def setUp(self):
        self.mock_api_key = "dummy_api_key"
        self.mock_url = "https://dummy-url.com"

    @requests_mock.Mocker()
    def test_stationboard(self, mock_requests):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_departures = [
            {
                "id": "ch:1:sloid:30813::1",
                "label": "Hogwarts Express",
                "currentDate": now,
                "departureDate": "2024-11-19T08:52:00Z",
                "estimatedDate": "2024-11-19T08:52:00Z",
                "destinationName": "Hogwarts",
                "destinationId": "ch:1:sloid:91178::3",
            }
        ]
        mock_response = generate_mock_response(mock_departures, now)

        mock_requests.post(
            self.mock_url,
            text=mock_response,
            status_code=200
        )

        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        results = api.get_departures(8501120, number_results=1)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "ch:1:sloid:30813::1")
        self.assertEqual(results[0]["label"], "Hogwarts Express")
        self.assertEqual(results[0]["currentDate"], format_time(now))
        self.assertEqual(results[0]["departureDate"], format_time("2024-11-19T08:52:00Z"))
        self.assertEqual(results[0]["estimatedDate"], format_time("2024-11-19T08:52:00Z"))
        self.assertEqual(results[0]["destinationName"], "Hogwarts")
        self.assertEqual(results[0]["destinationId"], "ch:1:sloid:91178::3")

    def test_format_time(self):
        # assert, that several timestamp formats are correctly handled and transformed into the
        # correct local time
        self.assertEqual(format_time("2024-11-19T08:52:00Z"), "19/11/2024 09:52")
        self.assertEqual(format_time("2024-11-19T09:52:00.123456789"), "19/11/2024 09:52")
        self.assertEqual(format_time("2024-11-19T08:52:00.123456789Z"), "19/11/2024 09:52")
        self.assertEqual(format_time("2024-11-19T08:52:00+01:00"), "19/11/2024 08:52")

    @requests_mock.Mocker()
    def test_stationboard_nonexisting_station(self, mock_requests):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        # mock an empty response to simulate a "station not found" event.
        mock_response = generate_mock_empty_response(now)
        mock_requests.post(
            self.mock_url,
            text=mock_response,
            status_code=200
        )

        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures(999999)

    @requests_mock.Mocker()
    def test_stationboard_invalid_id(self, mock_requests):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        mock_response = generate_mock_response([], now)
        mock_requests.post(self.mock_url, text=mock_response, status_code=200)

        api = opentransapi.OpenTrans(self.mock_api_key, self.mock_url)
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures("invalid_id")

    @patch('chsdi.views.stationboard.get_current_registry')
    def test_invalid_limit_param(self, mock_get_current_registry):

        mock_request = Mock()
        mock_request.matched_route.name = 'stationboard'
        mock_request.params = {}
        mock_request.matchdict = {'id': '8501120'}

        mock_registry = Mock()
        mock_registry.settings = {
            'opentrans_api_key': 'dummy_api_key',
            'opentrans_url': 'https://dummy-url.com',
        }
        mock_get_current_registry.return_value = mock_registry

        mock_request.params['limit'] = 'lalala'

        # Expect an HTTPBadRequest exception
        with self.assertRaises(HTTPBadRequest):
            TransportView(mock_request)
