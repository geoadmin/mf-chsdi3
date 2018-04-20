# -*- coding: utf-8 -*-

from tests.integration import TestsBase


class TestAdminkml(TestsBase):

    def test_admin_kml(self):
        resp = self.testapp.get('/admin/kml', status=200)
        self.assertEqual(resp.content_type, 'text/html')
