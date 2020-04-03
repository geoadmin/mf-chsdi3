# -*- coding: utf-8 -*-

from unittest import skipUnless
from tests.integration import TestsBase, dynamodb_tests


class TestAdminkml(TestsBase):

    @skipUnless(dynamodb_tests, "No connection do AWS DynamoDB")
    def test_admin_kml(self):
        resp = self.testapp.get('/admin/kml', status=200)
        self.assertEqual(resp.content_type, 'text/html')
