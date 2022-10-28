# -*- coding: utf-8 -*-

from tests.integration import TestsBase
from chsdi.lib.opentransapi import opentransapi
from datetime import datetime, timedelta
from pytz import timezone


class Test_OpenTransApi(TestsBase):

    def _callOpenTrans(self):
        opentrans_api_key = self.testapp.app.registry.settings.get('opentrans_api_key')
        api = opentransapi.OpenTrans(opentrans_api_key)
        return api

    def test_if_key_is_registered(self):
        opentrans_api_key = self.testapp.app.registry.settings.get('opentrans_api_key')
        self.assertNotEqual(opentrans_api_key, '')

    def test_station_wabern(self):
        api = self._callOpenTrans()
        # valid station id should be requested from opentransport api p.e.
        # https://api.opentransportdata.swiss/ckan-api/datastore_search?resource_id=b1a45b18-2a36-4582-a94d-71f2825e95e8&q=wabern
        results = api.get_departures(8588562)
        len_results = len(results)
        self.assertEqual(len_results, 5)

    def test_station_not_exist(self):
        api = self._callOpenTrans()
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures(153)

    def test_time_utc_zurich(self):
        api = self._callOpenTrans()
        time_zurich_tomorrow = datetime.now(timezone('Europe/Zurich')) + timedelta(days=1)
        time_zurich_tomorrow_12 = datetime.strptime('%s 12:00:00' % str(time_zurich_tomorrow.strftime('%d/%m/%Y')), '%d/%m/%Y %H:%M:%S')
        results = api.get_departures(8503000, 1, time_zurich_tomorrow_12.strftime('%Y-%m-%dT%H:%M:%S'))  # API call Zurich HB next day 12:00
        time_next_dep_zurich = datetime.strptime(results[0]['departureDate'], '%d/%m/%Y %H:%M')
        time_diff = abs(time_zurich_tomorrow_12 - time_next_dep_zurich).seconds
        self.assertLess(time_diff, 900)  # assuming, that the next train in Zurich at 12am will depart within 15 min
