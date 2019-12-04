# -*- coding: utf-8 -*-

import six
import uuid
import base64
import time
from boto.dynamodb2.exceptions import ItemNotFound

from boto.exception import S3ResponseError
from boto.s3.key import Key
from boto.utils import parse_ts
import pyramid.httpexceptions as exc
from pyramid.response import Response

from chsdi.lib.helpers import gzip_string
from chsdi.models.clientdata_dynamodb import get_dynamodb_table, get_bucket

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
                data={
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
            item = self.table.get_item(adminId=str(admin_id))
        except ItemNotFound:
            pass
        return item

    def update_item_timestamp(self, item, timestamp):
        try:
            item['timestamp'] = timestamp
            item.save()
        except Exception as e:
            raise exc.HTTPBadRequest('Error while updating the timestamp' % e)


class S3FilesHandler:

    def __init__(self, bucket_name):
        # We use instance roles
        self.bucket = get_bucket(bucket_name)
        self.bucket_name = bucket_name
        self.default_headers = {
            'Cache-Control': 'no-cache, must-revalidate'
        }

    def get_key(self, file_id):
        key = None
        try:
            key = self.bucket.get_key(file_id)
        except S3ResponseError as e:
            raise exc.HTTPInternalServerError('Cannot access file with id=%s: %s' % (file_id, e))
        except Exception as e:
            raise exc.HTTPInternalServerError('Cannot access file with id=%s: %s' % (file_id, e))
        return key

    def get_key_timestamp(self, file_id):
        key = self.get_key(file_id)
        if key:
            last_updated = parse_ts(key.last_modified)
            return last_updated.strftime('%Y-%m-%d %X')
        return time.strftime('%Y-%m-%d %X', time.localtime())

    def save_object(self, file_id, mime, content_encoding, data, replace=False):
        msg = 'configuring' if replace else 'updating'
        # Python2/3
        if data is None:
            error_msg = 'Error while saving %s S3 key (%s): file is empty' % (msg, file_id)
            log.error(error_msg)
            raise exc.HTTPInternalServerError(error_msg)

        try:
            k = Key(bucket=self.bucket)
            k.key = file_id
            k.set_metadata('Content-Type', mime)
            k.content_type = mime
            k.content_encoding = content_encoding
            k.set_metadata('Content-Encoding', content_encoding)
            logging.info(data)
            k.set_contents_from_string(data, headers=self.default_headers, replace=replace)
        except Exception as e:
            error_msg = 'Error while %s S3 key (%s) %s' % (msg, file_id, e)
            log.error(error_msg)
            raise exc.HTTPInternalServerError(error_msg)

    def delete_key(self, key):
        try:
            self.bucket.delete_key(key)
        except Exception as e:
            raise exc.HTTPInternalServerError('Error while deleting file %s. %e' % (key.key, e))


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

            key = self.s3_fileshandler.get_key(self.file_path)
            if key is None:
                raise exc.HTTPNotFound('File %s not found' % self.file_path)
            self.key = key

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
                data = self.key.get_contents_as_string()
                return Response(
                    data,
                    content_type=self.key.content_type,
                    content_encoding=self.key.content_encoding
                )
        except Exception as e:
            raise exc.HTTPNotFound('File %s not found %s' % (self.file_id, e))

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
        forked = status == 'copied'
        self.s3_fileshandler.save_object(self.file_path, mime, content_encoding, data, not forked)
        # Fetch last modified from S3 to add it to DynamoBD
        timestamp = self.s3_fileshandler.get_key_timestamp(self.file_path)

        if forked:
            # Save new entry to DynamoDB
            self.dynamodb_fileshandler.save_item(self.admin_id, self.file_id, timestamp)
        else:
            # Simply update the timestamp
            item = self.dynamodb_fileshandler.get_item(self.admin_id)
            self.dynamodb_fileshandler.update_item_timestamp(item, timestamp)

        return {
            'adminId': self.admin_id,
            'fileId': self.file_id,
            'status': status
        }

    def delete_file(self):
        if self.admin_id is None:
            raise exc.HTTPUnauthorized('You are not authorized to delete file %s' % self.file_id)
        self.s3_fileshandler.delete_key(self.key)
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
        del self.key
