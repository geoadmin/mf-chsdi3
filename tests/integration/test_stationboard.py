from datetime import datetime
from pytz import timezone

from tests.integration import TestsBase
import requests_mock
from tests.integration.helpers import generate_mock_response
from tests.integration.helpers import generate_mock_empty_response


class TestStationboard(TestsBase):

    def setUp(self):
        super(TestStationboard, self).setUp()
        self.mock_url = self.testapp.app.registry.settings.get('opentrans_url')

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

        resp = self.testapp.get('/stationboard/stops/8501120', status=200)

        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn("Hogwarts Express", resp.text)

    @requests_mock.Mocker()
    def test_stationboard_wrong_station(self, mock_requests):
        now = datetime.now(timezone('Europe/Zurich')).isoformat(timespec="microseconds")
        # mock an empty response to simulate a "station not found" event.
        mock_response = generate_mock_empty_response(now)
        mock_requests.post(
            self.mock_url,
            text=mock_response,
            status_code=200
        )

        resp = self.testapp.get('/stationboard/stops/153153', status=404)
        resp.mustcontain('No data available for the station 153153')

    @requests_mock.Mocker()
    def test_stationboardi_limit(self, mock_requests):
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

        params = {'limit': '1'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(len(resp.json), 1)
        self.assertEqual(resp.content_type, 'application/json')

    @requests_mock.Mocker()
    def test_stationboard_with_cb(self, mock_requests):

        opentrans_url = self.testapp.app.registry.settings.get('opentrans_url')

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
            opentrans_url,
            text=mock_response,
            status_code=200
        )

        params = {'callback': 'cb_'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        self.assertIn('cb_(', resp.text)  # Ensure the callback prefix is in the response

    def test_stationboard_wrong_id(self):
        resp = self.testapp.get('/stationboard/stops/toto', status=400)
        resp.mustcontain('The id must be an integer')

    def test_stationboard_wrong_limit(self):
        params = {'limit': 'toto'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=400)
        resp.mustcontain('The limit parameter must be an integer')
