# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestHistoricalMaps(TestsBase):

    def test_lufbilder(self):
        params = {'width': '4641', 'height': '7000', 'title': 'kartenwerk_lk100',
                  'bildnummer': 'bv80032193', 'layer': 'ch.swisstopo.zeitreihen',
                  'release_year': '1976'}
        resp = self.testapp.get('/historicalmaps/viewer.html', params=params, status=200)
        self.assertTrue(resp.content_type == 'text/html')

    def test_luftbilder_fail(self):
        self.testapp.get('/historicalmaps/viewer.html', status=400)
