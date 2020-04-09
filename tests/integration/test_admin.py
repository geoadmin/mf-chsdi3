# -*- coding: utf-8 -*-

from unittest import skipUnless
from tests.integration import TestsBase, dynamodb_tests, s3_tests


class TestAdminkml(TestsBase):

    @skipUnless(dynamodb_tests and s3_tests, "No connection to AWS DynamoDB and/or AWS S3")
    def test_admin_kml(self):
        resp = self.testapp.get('/admin/kml', status=200)
        self.assertEqual(resp.content_type, 'text/html')
