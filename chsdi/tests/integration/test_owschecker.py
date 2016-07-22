# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase
from nose.plugins.capture import Capture
from chsdi.views import owschecker as ows
from chsdi.views.owschecker import to_bunch


class TestOwsChecker(TestsBase):

    def setUp(self):
        super(TestOwsChecker, self).setUp()
        self.capture = Capture()
        self.capture.begin()

    def tearDown(self):
        super(TestOwsChecker, self).tearDown()
        del self.capture

    def _callFUT(self):
        base_url = 'http://wms.geo.admin.ch'
        dictionary = {'service': 'WMS', 'base_url': base_url}
        bunch = ows.Bunch(dictionary)
        return bunch

    def test_bunch(self):
        bunch = self._callFUT()
        self.assertEqual({'base_url': 'http://wms.geo.admin.ch', 'service': 'WMS'}, bunch)

    def test_to_bunch(self):
        dictionary_1 = {'base_url': 'http://wms.geo.admin.ch', 'service': 'WMS'}
        bunch_1 = to_bunch(dictionary_1)
        self.assertEqual(bunch_1, {'base_url': 'http://wms.geo.admin.ch', 'service': 'WMS'})

        dictionary_2 = {'base_url': 'http://wms.geo.admin.ch', 'service': {'service1': 'WMS', 'service2': 'WMTS'}}
        bunch_2 = to_bunch(dictionary_2)
        self.assertEqual(bunch_2, {'base_url': 'http://wms.geo.admin.ch', 'service': {'service2': 'WMTS', 'service1': 'WMS'}})

    def test_bykvp_no_args(self):
        self.testapp.get('/owschecker/bykvp', status=400)

    def test_form(self):
        resp = self.testapp.get('/owschecker/form', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain("Hint: Don't use tailing")

    def test_bykvp_minimal_wms_request(self):
        base_url = 'http://wms.geo.admin.ch'
        resp = self.testapp.get('/owschecker/bykvp', params={'service': 'WMS', 'base_url': base_url}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        resp.mustcontain("Checked Service: WMS")

    def test_bykvp_minimal_wmts_request(self):
        base_url = 'http://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml'
        resp = self.testapp.get('/owschecker/bykvp', params={'service': 'WMTS', 'base_url': base_url}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        resp.mustcontain("Checked Service: WMTS")

    def test_bykvp_minimal_wfs_request(self):
        base_url = 'http://wfs.geo.admin.ch'
        resp = self.testapp.get('/owschecker/bykvp', params={'service': 'WFS', 'base_url': base_url}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        resp.mustcontain("Checked Service: WFS")

    def test_bykvp_wms_request_restful(self):
        base_url = 'http://wms.geo.admin.ch'
        resp = self.testapp.get('/owschecker/bykvp', params={'service': 'WMS', 'base_url': base_url, 'restful': True}, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_form_params(self):
        base_url = 'http://wms.geo.admin.ch'
        resp = self.testapp.get('/owschecker/form', params={'service': 'WMS', 'base_url': base_url}, status=200)
        self.assertEqual(resp.content_type, 'text/html')
