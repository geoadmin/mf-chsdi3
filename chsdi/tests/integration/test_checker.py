# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestCheckerView(TestsBase):

    def test_checker(self):
        self.testapp.get('/checker', params={'url': 'http://s.geo.admin.ch/e83c57af1'}, status=200)

    def test_checker_options(self):
        resp = self.testapp.options('/checker', status=200)
        self.assertEqual(resp.headers.get('Cache-Control'), 'max-age=0, no-cache')
        self.assertEqual(resp.headers.get('Access-Control-Allow-Origin'), '*')
        self.assertEqual(resp.headers.get('Access-Control-Allow-Methods'), 'OPTIONS,HEAD,GET')

    def test_checker_head(self):
        self.testapp.head('/checker', status=200)
