# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase
import dateutil.parser


class TestCacheUpdateView(TestsBase):

    def test_cachupdate_good(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/cacheUpdate', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('cache_update', resp.json)
        self.assertIn('cache_type', resp.json)
        date = resp.json['cache_update']
        self.assertEqual(19, len(date))
        # the below throws an exception is the date is not in correct RFC3339 format
        dateutil.parser.parse(date)

    def test_invalid_layer(self):
        self.testapp.get('/rest/services/ech/MapServer/does_not_exists/cacheUpdate', status=404)
