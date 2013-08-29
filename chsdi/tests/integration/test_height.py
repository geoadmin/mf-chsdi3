# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestHeightView(TestsBase):

    def test_height_valid(self):
        resp = self.testapp.get('/rest/services/height', params={'easting': '600000', 'northing': '200000'}, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(resp.json['height'] == '560.2')

    def test_height_valid_with_lonlat(self):
        resp = self.testapp.get('/rest/services/height', params={'lon': '600000', 'lat': '200000'}, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(resp.json['height'] == '560.2')

    def test_height_with_dtm2(self):
        resp = self.testapp.get('/rest/services/height', params={'easting': '600000', 'northing': '200000', 'layers': 'DTM2'}, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(resp.json['height'] == '556.5')

    def test_height_with_comb(self):
        resp = self.testapp.get('/rest/services/height', params={'easting': '600000', 'northing': '200000', 'layers': 'COMB'}, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(resp.json['height'] == '556.5')

    def test_height_wrong_layer(self):
        resp = self.testapp.get('/rest/services/height', params={'easting': '600000', 'northing': '200000', 'layers': 'TOTO'}, status=400)
        resp.mustcontain("Please provide a valid name for the elevation")

    def test_height_wrong_lon_value(self):
        resp = self.testapp.get('/rest/services/height', params={'lon': 'toto', 'northing': '200000'}, status=400)
        resp.mustcontain("Please provide numerical values")

    def test_height_wrong_lat_value(self):
        resp = self.testapp.get('/rest/services/height', params={'lon': '600000', 'northing': 'toto'}, status=400)
        resp.mustcontain("Please provide numerical values")

    def test_height_with_callback_valid(self):
        resp = self.testapp.get('/rest/services/height', params={'easting': '600000', 'northing': '200000', 'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')
        resp.mustcontain('cb({')

    def test_height_miss_northing(self):
        resp = self.testapp.get('/rest/services/height', params={'easting': '600000'}, status=400)
        resp.mustcontain("Missing parameter 'norhting'/'lat'")

    def test_height_miss_easting(self):
        resp = self.testapp.get('/rest/services/height', params={'northing': '200000'}, status=400)
        resp.mustcontain("Missing parameter 'easting'/'lon'")
