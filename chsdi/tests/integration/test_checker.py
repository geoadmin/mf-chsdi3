# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestCheckerView(TestsBase):

    def test_checker(self):
        self.testapp.get('/checker', params={'url': 'http://s.geo.admin.ch/e83c57af1'}, status=200)

    def test_checker_dev(self):
        self.testapp.get('/checker_dev', params={'url': 'http://s.geo.admin.ch/e83c57af1'}, status=200)
