# -*- coding: utf-8 -*-

import boto.s3
from boto.s3.connection import OrdinaryCallingFormat
from boto.s3.connection import S3Connection
import boto.dynamodb2
from boto.dynamodb2.table import Table
import pyramid.httpexceptions as exc


'''
CREATE a table
--------------

import time
from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, GlobalKeysOnlyIndex

table = Table.create(shorturl, schema=[
    HashKey('url_short'),
], throughput={
    'read': 18,
    'write': 18,
},
global_indexes=[
    GlobalKeysOnlyIndex('UrlIndex', parts=[
        HashKey('url')
    ], throughput={
        'read': 18,
        'write': 18
    }),
])
time.sleep(30)

DROP a table
------------

from boto.dynamodb import connect_to_region

conn = connect_to_region(region_name='eu-west-1')
table=conn.get_table('shorturl')
table.delete()

'''


class DynamodbConnection:

    def __init__(self, region='eu-west-1'):
        self.conn = None
        self.region = region

    def get(self):
        if self.conn is None:
            try:
                self.conn = boto.dynamodb2.connect_to_region(self.region)
            except Exception as e:  # pragma: no cover
                raise exc.HTTPBadRequest(
                    'DynamoDB: Error during connection init %s' % e)
        return self.conn


class S3Connect:

    def __init__(self, region='eu-west-1'):
        self.conn = None
        self.region = region

    def get(self, profile_name=None):
        if self.conn is None:
            try:
                if profile_name:
                    S3Connection.DefaultHost = 's3-eu-west-1.amazonaws.com'
                    self.profile_name = profile_name
                    self.conn = S3Connection(
                        profile_name=self.profile_name,
                        calling_format=OrdinaryCallingFormat())
                else:
                    # Cannot use bucket names with dots
                    # see: https://github.com/boto/boto/issues/2836
                    self.conn = boto.s3.connect_to_region(
                        self.region,
                        calling_format=OrdinaryCallingFormat())
            except Exception as e:  # pragma: no cover
                raise exc.HTTPInternalServerError(
                    'S3: Error during connection init %s' % e)
        return self.conn


dynamodb_connection = DynamodbConnection()


def get_dynamodb_table(table_name='shorturl'):
    conn = dynamodb_connection.get()
    try:
        table = Table(table_name, connection=conn)
    except Exception as e:  # pragma: no cover
        raise exc.HTTPInternalServerError(
            'DynamoDB: Error during connection to the table %s\n%s' % (
                table_name, e))
    return table


def get_bucket(profile_name=None, bucket_name=None):
    s3_connection = S3Connect()
    conn = s3_connection.get(profile_name=profile_name)
    try:
        bucket = conn.get_bucket(bucket_name)
    except Exception as e:  # pragma: no cover
        raise exc.HTTPInternalServerError(
            'S3 Error during connection to the bucket %s\n%s' % (
                bucket_name, e))
    return bucket
