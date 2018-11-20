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
        self.bucket_key_name = 'geoadmin_file_storage_bucket66'
        self.bucket_name = request.registry.settings['geoadmin_file_storage_bucket']
        FileView.__init__(self, request)

    @view_config(route_name='checker')
    def home(self):
        try:
            self.dynamodb_fileshandler.table.count()
        except (KeyError, JSONResponseError):
            raise HTTPInternalServerError('Cannot access to DynamoDB backend {}'.format(self.dynamodb_fileshandler.table.table_name))

        return Response(body='OK', status_int=200)

    @view_config(route_name='checker_dev')
    def dev(self):
        return Response(body='OK', status_int=200)
