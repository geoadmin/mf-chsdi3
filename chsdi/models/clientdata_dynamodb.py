# -*- coding: utf-8 -*-

import pyramid.httpexceptions as exc

from boto import connect_s3
from boto.dynamodb2 import connect_to_region
from boto.dynamodb2.table import Table

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
            except Exception as e:
                raise exc.HTTPBadRequest('DynamoDB: Error during connection init %s' % e)
        return self.conn


class S3Connection:

    def __init__(self, profile_name):
        self.conn = None
        self.profile_name = profile_name

    def get(self):
        if self.conn is None:
            try:
                self.conn = connect_s3(profile_name=self.profile_name)
            except Exception as e:
                raise exc.HTTPBadRequest('S3: Error during connection %s' % e)
        return self.conn


dynamodb_connection = DynamodbConnection()


def get_dynamodb_table(table_name='shorturl'):
    conn = dynamodb_connection.get()
    try:
        table = Table(table_name, connection=conn)
    except Exception as e:
        raise exc.HTTPBadRequest('Error during connection to the table %s' % e)
    return table


def get_bucket(profile_name='geoadmin_filestorage', bucket_name=None):
    s3_connection = S3Connection(profile_name)
    conn = s3_connection.get()
    try:
        bucket = conn.get_bucket(bucket_name)
    except Exception as e:
        raise exc.HTTPBadRequest('Error during connection %s' % e)
    return bucket
