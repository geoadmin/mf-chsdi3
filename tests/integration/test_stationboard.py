# -*- coding: utf-8 -*-

from tests.integration import TestsBase
from webtest.app import AppError


class TestStationboard(TestsBase):

    def setUp(self):
        super(TestStationboard, self).setUp()
        self.opentransapi_is_up()

    def opentransapi_is_up(self):
        try:
            resp = self.testapp.get('/stationboard/stops/8501120', status=200)
            self.assertEqual(resp.status, 200)
        except (AppError, AssertionError):
            self.skipTest("OpenTrans API is down. Skipping iall  tests")

    def test_stationboard(self):
        resp = self.testapp.get('/stationboard/stops/8501120', status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_stationboard_wrong_station(self):
        resp = self.testapp.get('/stationboard/stops/153153', status=404)
        resp.mustcontain('No data available for the station 153153')

    def test_stationboardi_limit(self):
        params = {'destination': 'Luzern', 'limit': '1'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(len(resp.json), 1)
        self.assertEqual(resp.content_type, 'application/json')

    def test_stationboard_with_cb(self):
        params = {'destination': 'Luzern', 'callback': 'cb_'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')

    def test_stationboard_wrong_id(self):
        resp = self.testapp.get('/stationboard/stops/toto', status=400)
        resp.mustcontain('The id must be an integer')

    def test_stationboard_wrong_limit(self):
        params = {'limit': 'toto'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=400)
        resp.mustcontain('The limit parameter must be an integer')
