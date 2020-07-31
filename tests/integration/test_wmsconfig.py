# -*- coding: utf-8 -*-

from tests.integration import TestsBase


class TestWmsConfigServiceView(TestsBase):

    def test_wmsconfig(self):
        attributes = ['timestamp', 'resolution_max', 'resolution_min', 's3_max_resolution', 'format', 'cache_ttl', 'wms_gutter']
        resp = self.testapp.get('/rest/services/wmsconfig', status=200)
        self.assertTrue(resp.content_type == 'application/json')
        restrictions = resp.json
        restr = restrictions['ch.swisstopo.pixelkarte-farbe']
        self.assertEqual(sorted(restr.keys()), sorted(attributes))

    def test_wmsconfig_with_cb(self):
        resp = self.testapp.get('/rest/services/translations', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')
