# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase
from chsdi.views.qrcode_generator import _shorten_url
from pyramid import testing


class TestQRCodeView(TestsBase):

    def test_qrcode(self):
        resp = self.testapp.get('/qrcodegenerator', params={'url': 'http://s.geo.admin.ch/e83c57af1'}, status=200)
        self.assertEqual(resp.content_type, 'image/png')

    def test_qrcode_badurl(self):
        self.testapp.get('/qrcodegenerator', params={'url': 'http://dummy.com'}, status=400)

    def test_shorten_url(self):
        url = 'https://map.geo.admin.ch/?topic=ech&lang=fr&bgLayer=ch.swisstopo.pixelkarte-farbe&' + \
              'layers=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bafu.wrz-wildruhezonen_portal,' + \
              'ch.swisstopo.swisstlm3d-wanderwege,ch.bag.zecken-fsme-impfung&layers_visibility=false,false,false,true,true' + \
              '&layers_timestamp=18641231,,,,&X=187271.64&Y=553103.37&zoom=6&catalogNodes=687,692&layers_opacity=1,1,1,1,0.75'
        request = testing.DummyRequest()
        request.host = 'api3.geo.admin.ch'
        request.scheme = 'http'
        request.registry.settings = {}
        request.registry.settings['apache_base_path'] = 'main'
        test_result = _shorten_url(request, url)
        self.assertEqual(test_result, 'http://s.geo.admin.ch/621417c5bc')
