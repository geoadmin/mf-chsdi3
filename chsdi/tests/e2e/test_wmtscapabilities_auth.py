# -*- coding: utf-8 -*-

import requests
from chsdi.tests.integration import TestsBase
from chsdi.tests.e2e import MapProxyTestsBase


class TestWmtsGetTileAuth(TestsBase):

    def setUp(self):
        super(TestWmtsGetTileAuth, self).setUp()
        self.mp = MapProxyTestsBase()
        self.mp.setUp()
        self.paths = ['/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/7/67/45.jpeg',
                      '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/2056/17/5/6.jpeg',
                      '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/4258/10/6/4.jpeg',
                      '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/4326/12/132/180.jpeg']

    def tearDown(self):
        self.mp.tearDown()
        super(TestWmtsGetTileAuth, self).tearDown()

    def check_status_code(self, url, referer, code):
        headers = None
        if referer:
            headers = {'Referer': referer, 'User-Agent': 'mf-geoadmin/python'}
            resp = requests.get(url, params={'_id': self.mp.hash()}, headers=headers)
        else:
            resp = requests.get(url, params={'_id': self.mp.hash()}, headers={'User-Agent': 'mf-geoadmin/python'})

        assert (resp.status_code == code), 'Called Url: ' + url + ' [referer: ' + str(referer) + '] with return code: ' + str(resp.status_code)

    def test_bad_referer_get_capabilties(self):
        # Get Cap is open for all
        self.check_status_code(self.mp.host_url + '/1.0.0/WMTSCapabilities.xml', self.mp.BAD_REFERER, 200)

    def test_bad_referer_get_tile(self):
        for path in self.paths:
            self.check_status_code(self.mp.mapproxy_url + path, self.mp.BAD_REFERER, 403)

    def test_no_referer_get_capabilties(self):
        # Get Cap is open for all
        self.check_status_code(self.mp.host_url + '/1.0.0/WMTSCapabilities.xml', None, 200)

    def test_no_referer_get_tile(self):
        for path in self.paths:
            self.check_status_code(self.mp.mapproxy_url + path, None, 403)

    def test_good_referer_get_capabilties(self):
        self.check_status_code(self.mp.host_url + '/1.0.0/WMTSCapabilities.xml', self.mp.GOOD_REFERER, 200)

    def test_good_referer_get_tile(self):
        for path in self.paths:
            self.check_status_code(self.mp.mapproxy_url + path, self.mp.GOOD_REFERER, 200)
