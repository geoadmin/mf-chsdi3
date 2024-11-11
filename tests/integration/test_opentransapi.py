# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from unittest.mock import patch

from pytz import timezone
from tests.integration import TestsBase
from chsdi.lib.opentransapi import opentransapi


class Test_OpenTransApi(TestsBase):
    def _callOpenTrans(self):
        opentrans_api_key = self.testapp.app.registry.settings.get('opentrans_api_key')
        opentrans_url = self.testapp.app.registry.settings.get('opentrans_url')
        api = opentransapi.OpenTrans(opentrans_api_key, opentrans_url)
        return api

    def test_if_key_is_registered(self):
        opentrans_api_key = self.testapp.app.registry.settings.get('opentrans_api_key')
        self.assertNotEqual(opentrans_api_key, '')

    @patch.object(opentransapi.OpenTrans, 'get_departures')  # Mock the get_departures method
    def test_station_wabern(self, mock_get_departures):
        # Create a mock response for the get_departures method
        mock_get_departures.return_value = [
            {"departureDate": "11/11/2024 08:00", "station": "Wabern", "train": "IC123"},
            {"departureDate": "11/11/2024 08:30", "station": "Wabern", "train": "IC124"},
            {"departureDate": "11/11/2024 09:00", "station": "Wabern", "train": "IC125"},
            {"departureDate": "11/11/2024 09:30", "station": "Wabern", "train": "IC126"},
            {"departureDate": "11/11/2024 10:00", "station": "Wabern", "train": "IC127"}
        ]

        api = self._callOpenTrans()
        results = api.get_departures(8588562)
        len_results = len(results)
        self.assertEqual(len_results, 5)

    @patch.object(opentransapi.OpenTrans, 'get_departures')
    def test_station_not_exist(self, mock_get_departures):
        # Simulate a station not found scenario
        mock_get_departures.side_effect = opentransapi.OpenTransNoStationException("Station not found")

        api = self._callOpenTrans()
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures(153)

    @patch.object(opentransapi.OpenTrans, 'get_departures')
    def test_time_utc_zurich(self, mock_get_departures):
        # Simulate the response for a Zurich station on the next day
        time_zurich_tomorrow = datetime.now(timezone('Europe/Zurich')) + timedelta(days=1)
        time_zurich_tomorrow_12 = datetime.strptime('%s 12:00:00' % str(time_zurich_tomorrow.strftime('%d/%m/%Y')), '%d/%m/%Y %H:%M:%S')

        mock_get_departures.return_value = [
            {"departureDate": time_zurich_tomorrow_12.strftime('%d/%m/%Y %H:%M'), "station": "Zurich HB", "train": "SBB123"}
        ]

        api = self._callOpenTrans()
        results = api.get_departures(8503000, 1, time_zurich_tomorrow_12.strftime('%Y-%m-%dT%H:%M:%S'))  # Call Zurich HB next day 12:00

        time_next_dep_zurich = datetime.strptime(results[0]['departureDate'], '%d/%m/%Y %H:%M')
        time_diff = abs(time_zurich_tomorrow_12 - time_next_dep_zurich).seconds
        self.assertLess(time_diff, 900)  # assuming, that the next train in Zurich at 12am will depart within 15 min
