# -*- coding: utf-8 -*-

import six
import uuid
import base64
import time

import pyramid.httpexceptions as exc
from pyramid.response import Response

from chsdi.lib.helpers import gzip_string
from chsdi.models.clientdata_dynamodb import get_dynamodb_table, get_file_from_bucket, delete_file_in_bucket, upload_object_to_bucket

import logging

log = logging.getLogger(__name__)


class DynamoDBFilesHandler:

    def __init__(self, table_name, bucket_name):
        # We use instance roles
        self.table = get_dynamodb_table(table_name=table_name)
        self.bucket_name = bucket_name

    def save_item(self, admin_id, file_id, timestamp):
        try:
            self.table.put_item(
                Item={
                    'adminId': admin_id,
                    'fileId': file_id,
                    'timestamp': timestamp,
                    'bucket': self.bucket_name
                }
            )
        except Exception as e:
            raise exc.HTTPBadRequest('Error during put item %s' % e)

    def get_item(self, admin_id):
        item = None
        try:
            item = self.table.get_item(Key={'adminId': str(admin_id)}).get('Item', None)
        except Exception:
            pass
        return item

    def update_item_timestamp(self, admin_id, timestamp):
        try:
            self.table.update_item(Key={
                'adminId': admin_id
            }, AttributeUpdates={
                'timestamp': {
                    'Value': timestamp,
                    'Action': 'PUT'
                }
            })
        except Exception as e:
            raise exc.HTTPBadRequest('Error while updating the timestamp' % e)


class S3FilesHandler:

    def __init__(self, bucket_name):
        # We use instance roles
        self.bucket_name = bucket_name
        self.default_headers = {
            'Cache-Control': 'no-cache, must-revalidate'
        }

    def get_item(self, file_id):  # TODO: errors
        try:
            item = get_file_from_bucket(self.bucket_name, file_id)
        except Exception as e:
            raise exc.HTTPInternalServerError('Cannot access file with id=%s: %s' % (file_id, e))
        return item

    def get_key_timestamp(self, file_id):
        try:
            last_updated = get_file_from_bucket(self.bucket_name, file_id)['LastModified']
            return last_updated.strftime('%Y-%m-%d %X')
        except Exception:
            return time.strftime('%Y-%m-%d %X', time.localtime())

    def save_object(self, file_id, mime, content_encoding, data, replace=False):
        msg = 'configuring' if not replace else 'updating'
        # Python2/3
        if data is None:
            error_msg = 'Error while saving %s S3 key (%s): file is empty' % (msg, file_id)
            log.error(error_msg)
            raise exc.HTTPInternalServerError(error_msg)

        try:
            response = upload_object_to_bucket(
                self.bucket_name, file_id, mime, content_encoding,
                data, self.default_headers['Cache-Control'])
            log.info(response)

        except Exception as e:
            error_msg = 'Error while %s S3 key (%s) %s' % (msg, file_id, e)
            log.error(error_msg)
            raise exc.HTTPInternalServerError(error_msg)

    def delete_key(self, file_id):
        try:
            delete_file_in_bucket(self.bucket_name, file_id)
        except Exception as e:
            raise exc.HTTPInternalServerError('Error while deleting file %s. %e' % (file_id, e))


class FilesHandler(object):

    # Properties to be overriden in the __init__ function of the child class
    dynamodb_table_name = ''
    bucket_key_name = ''
    bucket_name = ''
    bucket_folder = ''
    # Define with the dot
    bucket_file_extension = ''
    default_mime_type = ''
    default_route_name = ''

    def __init__(self, request):
        self.request = request
        # Set up AWS DynamoDB and S3 handlers
        self.dynamodb_fileshandler = DynamoDBFilesHandler(
            self.dynamodb_table_name, self.bucket_key_name)
        self.s3_fileshandler = S3FilesHandler(self.bucket_name)
        # This mean that we suppose a file has already been created
        if request.matched_route.name == self.default_route_name:
            req_id = request.matchdict['id']
            db_item = self.dynamodb_fileshandler.get_item(req_id)
            # Item is None if not found
            if db_item is None:
                self.admin_id = None
                self.file_id = req_id
            else:
                self.admin_id = req_id
                self.file_id = db_item.get('fileId')

            try:
                self.item = self.s3_fileshandler.get_item(self.file_path)
            except Exception:
                raise exc.HTTPNotFound('File %s not found' % self.file_path)

    @property
    def file_path(self):
        if self.bucket_folder:
            return '%s/%s%s' % (self.bucket_folder, self.file_id, self.bucket_file_extension)
        return self.file_id

    def create_file(self):
        self.file_id = self._get_uuid()
        self.admin_id = self._get_uuid()
        mime = self.request.content_type
        data = self.request.body
        # Python2/3
        if six.PY3:
            data = data.decode('utf8')

        content_encoding = None
        if mime == self.default_mime_type:
            content_encoding = 'gzip'
            data = gzip_string(data)

        # Save to S3
        self.s3_fileshandler.save_object(self.file_path, mime, content_encoding, data)
        # Fetch last modified from S3 to add it to DynamoBD
        timestamp = self.s3_fileshandler.get_key_timestamp(self.file_path)
        # Save to DynamoDB
        self.dynamodb_fileshandler.save_item(self.admin_id, self.file_id, timestamp)
        return {
            'adminId': self.admin_id,
            'fileId': self.file_id
        }

    def read_file(self):
        try:
            if self.admin_id:
                return {
                    'fileId': self.file_id
                }
            else:
                data = self.s3_fileshandler.get_item(self.file_path)['Body'].read()
                return Response(
                    data,
                    content_type=self.item['ContentType'],
                    content_encoding=self.item['ContentEncoding']
                )
        except Exception as e:
            raise exc.HTTPNotFound('File %s not found %s' % (self.file_path, e))

    def update_file(self):
        data = self.request.body
        mime = self.request.content_type
        content_encoding = None
        if mime == self.default_mime_type:
            content_encoding = 'gzip'
            data = gzip_string(data)
        if self.admin_id is not None:
            status = 'updated'
        else:
            # In case the file already exist, we create a fork
            status = 'copied'
            self._fork()
        updated = status == 'updated'
        self.s3_fileshandler.save_object(self.file_path, mime, content_encoding, data, updated)
        # Fetch last modified from S3 to add it to DynamoBD
        timestamp = self.s3_fileshandler.get_key_timestamp(self.file_path)

        if updated:
            # Simply update the timestamp
            self.dynamodb_fileshandler.update_item_timestamp(self.admin_id, timestamp)
        else:
            # Save new entry to DynamoDB
            self.dynamodb_fileshandler.save_item(self.admin_id, self.file_id, timestamp)

        return {
            'adminId': self.admin_id,
            'fileId': self.file_id,
            'status': status
        }

    def delete_file(self):
        if self.admin_id is None:
            raise exc.HTTPUnauthorized('You are not authorized to delete file %s' % self.file_id)
        self.s3_fileshandler.delete_key(self.file_id)
        return {
            'success': True
        }

    def _get_uuid(self):
        # Python2/3
        # TODO
        uuid_ = base64.urlsafe_b64encode(uuid.uuid4().bytes)
        if six.PY2:
            return uuid_.replace('=', '')

        logging.info(uuid_.decode('utf8').replace('=', ''))
        return uuid_.decode('utf8').replace('=', '')

    def _fork(self):
        self.file_id = self._get_uuid()
        self.admin_id = self._get_uuid()
        del self.item
