from unittest.mock import patch
from tests.integration import TestsBase


class TestStationboard(TestsBase):

    @patch('requests.get')
    def test_stationboard(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "departures": [
                {"departureDate": "2024-11-11T08:00:00", "station": "Zurich", "train": "IC123"},
                {"departureDate": "2024-11-11T08:30:00", "station": "Zurich", "train": "IC124"}
            ]
        }

        resp = self.testapp.get('/stationboard/stops/8501120', status=200)
        self.assertEqual(resp.content_type, 'application/json')

    @patch('requests.get')
    def test_stationboard_wrong_station(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"error": "No data available for the station 153153"}

        resp = self.testapp.get('/stationboard/stops/153153', status=404)
        resp.mustcontain('No data available for the station 153153')

    @patch('requests.get')
    def test_stationboard_limit(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "departures": [
                {"departureDate": "2024-11-11T08:00:00", "station": "Zurich", "train": "IC123"}
            ]
        }

        params = {'limit': '1'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(len(resp.json), 1)
        self.assertEqual(resp.content_type, 'application/json')

    @patch('requests.get')
    def test_stationboard_with_cb(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "departures": [
                {"departureDate": "2024-11-11T08:00:00", "station": "Zurich", "train": "IC123"}
            ]
        }

        params = {'callback': 'cb_'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')

    @patch('requests.get')
    def test_stationboard_wrong_id(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"error": "The id must be an integer"}

        resp = self.testapp.get('/stationboard/stops/toto', status=400)
        resp.mustcontain('The id must be an integer')

    @patch('requests.get')
    def test_stationboard_wrong_limit(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"error": "The limit parameter must be an integer"}

        params = {'limit': 'toto'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=400)
        resp.mustcontain('The limit parameter must be an integer')
