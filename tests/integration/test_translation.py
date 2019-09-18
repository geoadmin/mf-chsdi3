# -*- coding: utf-8 -*-

from tests.integration import TestsBase


class TestTraductionServiceView(TestsBase):

    def test_traductions(self):
        params = {'lang': 'en'}
        resp = self.testapp.get('/rest/services/translations', params=params, status=200)
        self.assertTrue(resp.content_type == 'application/json')
        msgids = resp.json
        self.assertEqual(msgids['ch.swisstopo.pixelkarte-farbe'], 'National Maps (color)')

    def test_translations_with_cb(self):
        resp = self.testapp.get('/rest/services/translations', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')
