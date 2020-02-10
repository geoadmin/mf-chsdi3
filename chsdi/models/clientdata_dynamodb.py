# -*- coding: utf-8 -*-

import boto3

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
    # This is a singleton. This is nice.
    def __init__(self, region='eu-west-1'):
        self.conn = None
        self.region = region

    def get(self):
        if self.conn is None:
            try:
                self.conn = boto3.resource('dynamodb', region_name=self.region)
            except Exception as e:  # pragma: no cover
                raise exc.HTTPBadRequest(
                    'DynamoDB: Error during connection init %s' % e)
        return self.conn


class S3Connect:
    def __init__(self, region='eu-west-1'):
        self.conn = None
        self.region = region

    def get(self):
        if self.conn is None:
            try:
                # Cannot use bucket names with dots
                # see: https://github.com/boto/boto/issues/2836
                self.conn = boto3.client('s3', region_name=self.region)
            except Exception as e:  # pragma: no cover
                raise exc.HTTPInternalServerError(
                    'S3: Error during connection init %s' % e)
        return self.conn


dynamodb_connection = DynamodbConnection()
s3_connection = S3Connect()


def get_dynamodb_table(table_name='shorturl'):
    conn = dynamodb_connection.get()
    try:
        table = conn.Table(table_name)
    except Exception as e:  # pragma: no cover
        raise exc.HTTPInternalServerError(
            'DynamoDB: Error during connection to the table %s\n%s' % (
                table_name, e))
    return table


def get_bucket(bucket_name):
    conn = s3_connection.get()
    try:
        bucket = conn.Bucket(bucket_name)

    except Exception as e:  # pragma: no cover
        raise exc.HTTPInternalServerError(
            'S3 Error during connection to the bucket %s\n%s' % (
                bucket_name, e))
    return bucket


def get_file_from_bucket(bucket_name, file_name):
    conn = s3_connection.get()
    response = conn.get_object(Bucket=bucket_name,
                               Key=file_name)
    return response


def delete_file_in_bucket(bucket_name, file_name):
    return s3_connection.get().delete_object(Bucket=bucket_name,
                                  Key=file_name)


def upload_object_to_bucket(bucket_name, file_id, mime, content_encoding, data, cache_control, replace=False):
    if not replace:
        try:
            get_file_from_bucket(bucket_name, file_id)
            return None
        except Exception:
            pass
    return s3_connection.get().put_object(
        Body=data,
        Key=file_id,
        ContentType=mime,
        ContentEncoding=content_encoding,
        CacheControl=cache_control,
        Bucket=bucket_name
    )
