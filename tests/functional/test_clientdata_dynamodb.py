# -*- coding: utf-8 -*-

import unittest
import pyramid.httpexceptions as exc
from chsdi.models.clientdata_dynamodb import DynamodbConnection, S3Connect, get_dynamodb_table, get_bucket


class Test_DynamodbConnection(unittest.TestCase):
    _multiprocess_can_split_ = True

    def test_dynamodbConnection_toto(self):
        d = DynamodbConnection(region='toto')
        result = d.get()
        self.assertEqual(result, None)

    def test_dynamodbConnection(self):
        d = DynamodbConnection(region='eu-west-1')
        result = d.get()
        self.assertEqual(str(result), 'DynamoDBConnection:dynamodb.eu-west-1.amazonaws.com')


class Test_S3Connect(unittest.TestCase):
    _multiprocess_can_split_ = True

    def test_s3connection(self):
        s = S3Connect()
        result = s.get()
        self.assertNotEqual(result, None)
        self.assertEqual(str(result), 'S3Connection:s3-eu-west-1.amazonaws.com')

    def test_get_dynamodb_table(self):
        result = get_dynamodb_table('shortenurl')
        self.assertNotEqual(result, exc.HTTPBadRequest)

    def test_get_bucket_badrequest(self):
        with self.assertRaises(exc.HTTPInternalServerError):
            get_bucket('wrongbucket')
