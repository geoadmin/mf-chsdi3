# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestStationboard(TestsBase):

    def test_stationboard(self):
        params = {'destination': 'Luzern'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_stationboard_nodata(self):
        params = {'destination': 'myDestination'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json), 1)
        resp.mustcontain('[{"destination":"nodata"}]')

    def test_stationboardi_limit(self):
        params = {'destination': 'Luzern', 'limit': '1'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(len(resp.json), 1)
        self.assertEqual(resp.content_type, 'application/json')

    def test_stationboard_with_cb(self):
        params = {'destination': 'Luzern', 'callback': 'cb'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_stationboard_wrong_id(self):
        resp = self.testapp.get('/stationboard/stops/toto', status=400)
        resp.mustcontain('The id must be an integer')

    def test_stationboard_wrong_id_stationboard_destination(self):
        resp = self.testapp.get('/stationboard/stops/toto/destinations', status=400)
        resp.mustcontain('The id must be an integer')

    def test_stationboard_wrong_limit(self):
        params = {'limit': 'toto'}
        resp = self.testapp.get('/stationboard/stops/8501120', params=params, status=400)
        resp.mustcontain('The limit parameter must be an integer')

    def test_available_destinations(self):
        resp = self.testapp.get('/stationboard/stops/8500109/destinations', status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_available_destinations_with_cb(self):
        params = {'callback': 'cb'}
        resp = self.testapp.get('/stationboard/stops/8500109/destinations', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_stationboard_destination_nodata(self):
        resp = self.testapp.get('/stationboard/stops/123/destinations', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json), 1)
        resp.mustcontain('[{"destination":"nodata"}]')
