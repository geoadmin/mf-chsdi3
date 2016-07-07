# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestOGCproxyView(TestsBase):

    def setUp(self):
        super(TestOGCproxyView, self).setUp()
        self.headers = {'X-SearchServer-Authorized': 'true'}

    def test_proxy_forbidden(self):
        params = {'url': 'http://www.geo.admin.ch/'}
        self.testapp.get('/ogcproxy', params=params, status=403)

    def test_proxy_authorized(self):
        params = {'url': 'http://www.geo.admin.ch/'}
        resp = self.testapp.get('/ogcproxy', params=params, headers=self.headers, status=200)
        self.assertTrue(resp.content_type == 'text/html')
        resp.mustcontain('the federal geoportal')

    def test_proxy_no_url(self):
        self.testapp.get('/ogcproxy', headers=self.headers, status=400)

    def test_proxy_no_parsed_url(self):
        params = {'url': 'www.geo.admin.ch/'}
        self.testapp.get('/ogcproxy', params=params, headers=self.headers, status=400)

    def test_proxy_url_content(self):
        params = {'url': 'http://mf-chsdi3.dev.bgdi.ch/examples/bln-style.kmz'}
        self.testapp.get('/ogcproxy', params=params, headers=self.headers, status=200)

        params = {'url': 'http://mf-chsdi3.dev.bgdi.ch/examples/kml_example_utf16.kml'}
        self.testapp.get('/ogcproxy', params=params, headers=self.headers, status=200)
