# -*- coding: utf-8 -*-

import uuid
import base64
import time

from boto.dynamodb2.exceptions import ItemNotFound

from boto.exception import S3ResponseError
from boto.s3.key import Key
from boto.utils import parse_ts

import pyramid.httpexceptions as exc
from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from chsdi.models.clientdata_dynamodb import get_dynamodb_table, get_bucket
from chsdi.lib.decorators import requires_authorization, validate_kml_input
from chsdi.lib.helpers import gzip_string


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
        try:
            k = Key(bucket=self.bucket)
            k.key = file_id
            k.set_metadata('Content-Type', mime)
            k.content_type = mime
            k.content_encoding = content_encoding
            k.set_metadata('Content-Encoding', content_encoding)
            k.set_contents_from_string(data, headers=self.default_headers, replace=replace)
        except Exception as e:
            raise exc.HTTPInternalServerError('Error while %s S3 key (%s) %s' % (msg, file_id, e))

    def delete_key(self, key):
        try:
            self.bucket.delete_key(key)
        except Exception as e:
            raise exc.HTTPInternalServerError('Error while deleting file %s. %e' % (key.key, e))


@view_defaults(renderer='jsonp', route_name='files')
class FileView(object):

    def __init__(self, request):
        self.bucket_key_name = 'geoadmin_file_storage_bucket'
        self.bucket_name = request.registry.settings['geoadmin_file_storage_bucket']
        self.request = request

        # Set up AWS DynamoDB and S3 handlers
        self.dynamodb_fileshandler = DynamoDBFilesHandler(
            'geoadmin-file-storage', self.bucket_key_name)
        self.s3_fileshanlder = S3FilesHandler(self.bucket_name)

        # This mean that we suppose a file has already been created
        if request.matched_route.name == 'files':
            req_id = request.matchdict['id']
            db_item = self.dynamodb_fileshandler.get_item(req_id)
            # Item is None if not found
            if db_item is None:
                self.admin_id = None
                self.file_id = req_id
            else:
                self.admin_id = req_id
                self.file_id = db_item.get('fileId')

            key = self.s3_fileshanlder.get_key(self.file_id)
            if key is None:
                raise exc.HTTPNotFound('File %s not found' % self.file_id)
            self.key = key

    @view_config(route_name='files_collection', request_method='POST')
    @requires_authorization()
    @validate_kml_input()
    def create_file(self):
        self.file_id = self._get_uuid()
        self.admin_id = self._get_uuid()
        mime = self.request.content_type
        data = self.request.body
        content_encoding = None
        if mime == 'application/vnd.google-earth.kml+xml':
            content_encoding = 'gzip'
            data = gzip_string(data)
        # Save to S3
        self.s3_fileshanlder.save_object(self.file_id, mime, content_encoding, data)
        # Fetch last modified from S3 to add it to DynamoBD
        timestamp = self.s3_fileshanlder.get_key_timestamp(self.file_id)
        # Save to DynamoDB
        self.dynamodb_fileshandler.save_item(self.admin_id, self.file_id, timestamp)
        return {
            'adminId': self.admin_id,
            'fileId': self.file_id
        }

    @view_config(request_method='GET')
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

    @view_config(request_method='POST')
    @requires_authorization()
    @validate_kml_input()
    def update_file(self):
        data = self.request.body
        mime = self.request.content_type
        content_encoding = None
        if mime == 'application/vnd.google-earth.kml+xml':
            content_encoding = 'gzip'
            data = gzip_string(data)
        if self.admin_id is not None:
            status = 'updated'
        else:
            # In case the file already exist, we create a fork
            status = 'copied'
            self._fork()
        forked = status == 'copied'
        self.s3_fileshanlder.save_object(self.file_id, mime, content_encoding, data, not forked)
        # Fetch last modified from S3 to add it to DynamoBD
        timestamp = self.s3_fileshanlder.get_key_timestamp(self.file_id)

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

    @view_config(request_method='DELETE')
    @requires_authorization()
    def delete_file(self):
        if self.admin_id is None:
            raise exc.HTTPUnauthorized('You are not authorized to delete file %s' % self.file_id)
        self.s3_fileshanlder.delete_key(self.key)
        return {
            'success': True
        }

    def _get_uuid(self):
        return base64.urlsafe_b64encode(uuid.uuid4().bytes).replace('=', '')

    def _fork(self):
        self.file_id = self._get_uuid()
        self.admin_id = self._get_uuid()
        del self.key
