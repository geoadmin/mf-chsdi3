# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase
from chsdi.lib.opentransapi import opentransapi


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
        results = api.get_departures(8507078)
        len_results = len(results)
        self.assertEqual(len_results, 5)

    def test_station_not_exist(self):
        api = self._callOpenTrans()
        with self.assertRaises(opentransapi.OpenTransNoStationException):
            api.get_departures(153)
