# -*- coding: utf-8 -*-
import boto3

import botocore.exceptions as boto_exc
import pyramid.httpexceptions as exc

from chsdi.lib.helpers import anonymize_string


class S3Connect:
    def __init__(self):
        self.conn = None

    def get(self):
        if self.conn is None:
            try:
                # Cannot use bucket names with dots
                # see: https://github.com/boto/boto/issues/2836
                self.conn = boto3.client('s3')
            except Exception as e:  # pragma: no cover
                raise exc.HTTPInternalServerError(
                    'S3: Error during connection init %s' % e)
        return self.conn

s3_connection = S3Connect()


def get_file_from_bucket(bucket_name, file_name):
    conn = s3_connection.get()
    try:
        response = conn.get_object(Bucket=bucket_name,
                                   Key=file_name)
    except boto_exc.NoCredentialsError as c:
        raise exc.HTTPInternalServerError("Credential error for  bucket (%s)\n%s" % (anonymize_string(bucket_name), c))
    except Exception as e:
        raise exc.HTTPInternalServerError("Bucket (%s) or file (%s) not valids. \n%s" % (anonymize_string(bucket_name), file_name, e))
        return e
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
