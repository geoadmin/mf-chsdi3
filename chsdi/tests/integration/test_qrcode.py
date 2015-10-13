# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase
from chsdi.views.qrcode_generator import _shorten_url
from pyramid import testing


class TestQRCodeView(TestsBase):

    def test_qrcode(self):
        resp = self.testapp.get('/qrcodegenerator', params={'url': 'http://s.geo.admin.ch/e83c57af1'}, status=200)
        self.assertTrue(resp.content_type == 'image/png')

    def test_qrcode_badurl(self):
        self.testapp.get('/qrcodegenerator', params={'url': 'http://dummy.com'}, status=400)

    def test_shorten_url(self):
        url = 'http://s.geo.admin.ch/e83c57af1'
        request = testing.DummyRequest()
        request.host = 'api3.geo.admin.ch'
        request.scheme = 'http'
        request.registry.settings = {}
        request.registry.settings['apache_base_path'] = 'main'
        test_result = _shorten_url(request, url)
        self.assertEqual(test_result, 'http://s.geo.admin.ch/5faf70c820')
