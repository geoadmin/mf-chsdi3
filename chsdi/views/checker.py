# -*- coding: utf-8 -*-

from boto.exception import JSONResponseError
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPInternalServerError
from chsdi.views.files import FileView


class Checker(FileView):

    def __init__(self, request):
        self.request = request
        self.dynamodb_table_name = 'geoadmin-file-'
        self.bucket_name = request.registry.settings['geoadmin_file_storage_bucket']
        self.key_name = '7iu88SxtTBGWlmSV540Iag'
        FileView.__init__(self, request)

    @view_config(route_name='checker')
    def home(self):
        return Response(body='OK', status_int=200)

    @view_config(route_name='backend_checker')
    def backend(self):
        try:
            self.dynamodb_fileshandler.table.count()
        except (KeyError, JSONResponseError):
            raise HTTPInternalServerError('Cannot access to DynamoDB backend {}'.format(self.dynamodb_fileshandler.table.table_name))

        try:
            resp = self.s3_fileshandler.bucket.get_key(self.key_name)
        except (KeyError, JSONResponseError):
            raise HTTPInternalServerError('Cannot access bucket {}'.format(self.bucket_name))

        if resp is None or resp.key != self.key_name:
            raise HTTPInternalServerError('Unable to find key {} in bucket {}'.format(self.key_name, self.bucket_name))

        return Response(body='OK', status_int=200)

    @view_config(route_name='checker_dev')
    def dev(self):
        return Response(body='OK', status_int=200)
