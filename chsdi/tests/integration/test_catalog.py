# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestCatalogService(TestsBase):

    def test_catalog_no_params(self):
        resp = self.testapp.get('/rest/services/blw/CatalogServer', status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('root' in resp.json['results'])
        self.failUnless('children' in resp.json['results']['root'])
        self.failUnless('selectedOpen' in resp.json['results']['root'])
        self.failUnless('category' in resp.json['results']['root'])

    def test_catalog_with_callback(self):
        resp = self.testapp.get('/rest/services/blw/CatalogServer', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')

    def test_catalog_existing_map_no_catalog(self):
        self.testapp.get('/rest/services/all/CatalogServer', status=404)

    def test_catalog_wrong_map(self):
        self.testapp.get('/rest/services/foo/CatalogServer', status=400)
