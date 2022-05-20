# -*- coding: utf-8 -*-
import os
import boto3

import pyramid.httpexceptions as exc


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


VECTOR_BUCKET_REGION = os.getenv('VECTOR_BUCKET_REGION', None)

if VECTOR_BUCKET_REGION:
    s3_connection = S3Connect(region=VECTOR_BUCKET_REGION)
else:
    s3_connection = S3Connect()


def get_file_from_bucket(bucket_name, file_name):
    conn = s3_connection.get()
    try:
        response = conn.get_object(Bucket=bucket_name,
                                   Key=file_name)
    except Exception as e:
        raise exc.HTTPInternalServerError("bucket (%s) or file (%s) not valids. \n%s" % (bucket_name, file_name, e))
    return response


def delete_file_in_bucket(bucket_name, file_name):
    return s3_connection.get().delete_object(Bucket=bucket_name,
                                             Key=file_name)


def upload_object_to_bucket(bucket_name, file_id, mime, content_encoding, data, cache_control):
    conn = s3_connection.get()
    return conn.put_object(
        Body=data,
        Key=file_id,
        ContentType=mime,
        ContentEncoding=content_encoding,
        CacheControl=cache_control,
        Bucket=bucket_name
    )
