# -*- coding: utf-8 -*-

import unittest
import logging
import pyramid.httpexceptions as exc
from chsdi.models.clientdata_dynamodb import DynamodbConnection, S3Connect, get_dynamodb_table, get_file_from_bucket


class Test_DynamodbConnection(unittest.TestCase):

    def test_dynamodbConnection_toto(self):
        d = DynamodbConnection(region='toto')
        result = d.get()
        logging.debug(result)
        self.assertEqual(result, None)

    def test_dynamodbConnection(self):
        d = DynamodbConnection(region='eu-west-1')
        result = d.get()
        logging.debug(result)

        self.assertEqual(str(result), 'DynamoDBConnection:dynamodb.eu-west-1.amazonaws.com')


class Test_S3Connect(unittest.TestCase):

    def test_s3connection(self):
        s = S3Connect()
        result = s.get()
        logging.debug(result)

        self.assertNotEqual(result, None)
        self.assertEqual(str(result), 'S3Connection:s3-eu-west-1.amazonaws.com')

    def test_get_dynamodb_table(self):
        result = get_dynamodb_table('shortenurl')
        logging.debug(result)

        self.assertNotEqual(result, exc.HTTPBadRequest)

    def test_get_bucket_badrequest(self):
        with self.assertRaises(exc.HTTPInternalServerError):
            get_file_from_bucket('wrongbucket', "nonexistent_file.jpg")
