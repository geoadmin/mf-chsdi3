# -*- coding: utf-8 -*-

import pyramid.httpexceptions as exc

from boto.dynamodb2.table import Table
from boto.dynamodb2 import connect_to_region
from boto.s3.connection import S3Connection, OrdinaryCallingFormat

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
                self.conn = connect_to_region(self.region)
            except Exception as e:  # pragma: no cover
                raise exc.HTTPBadRequest('DynamoDB: Error during connection init %s' % e)
        return self.conn


class S3Connect:

    def __init__(self, profile_name):
        self.conn = None
        self.profile_name = profile_name

    def get(self):
        # Work around because of https://github.com/boto/boto/issues/2836
        S3Connection.DefaultHost = 's3-eu-west-1.amazonaws.com'
        if self.conn is None:
            try:
                self.conn = S3Connection(
                    profile_name=self.profile_name, calling_format=OrdinaryCallingFormat())
            except Exception as e:  # pragma: no cover
                raise exc.HTTPInternalServerError('Error during connection to the table %s' % e)
        return self.conn


dynamodb_connection = DynamodbConnection()


def get_dynamodb_table(table_name='shorturl'):
    conn = dynamodb_connection.get()
    try:
        table = Table(table_name, connection=conn)
    except Exception as e:  # pragma: no cover
        raise exc.HTTPInternalServerError('Error during connection to the table %s' % e)
    return table


def get_bucket(profile_name='geoadmin_filestorage', bucket_name=None):
    s3_connection = S3Connect(profile_name)
    conn = s3_connection.get()
    try:
        bucket = conn.get_bucket(bucket_name)
    except Exception as e:  # pragma: no cover
        raise exc.HTTPInternalServerError('Error during connection to the bucket %s' % e)
    return bucket
