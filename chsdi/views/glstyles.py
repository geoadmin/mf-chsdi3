# -*- coding: utf-8 -*-

from pyramid.view import view_config, view_defaults

from chsdi.lib.files_handler import FilesHandler
from chsdi.lib.decorators import requires_authorization, validate_glstyle_input


@view_defaults(renderer='jsonp', route_name='glstyles')
class GLStylesView(FilesHandler):

    def __init__(self, request):
        self.dynamodb_table_name = 'vectortiles-styles-storage'
        self.bucket_key_name = 'geoadmin_file_storage_bucket'
        self.bucket_name = request.registry.settings['geoadmin_file_storage_bucket']
        self.default_mime_type = 'application/json'
        self.bucket_folder = 'gl-styles'
        self.default_route_name = 'glstyles'
        FilesHandler.__init__(self, request)

    @view_config(route_name='glstyles_collection', request_method='POST')
    @requires_authorization()
    @validate_glstyle_input()
    def create_file_view(self):
        return self.create_file()

    @view_config(request_method='GET')
    def read_file_view(self):
        return self.read_file()

    @view_config(request_method='POST')
    @requires_authorization()
    @validate_glstyle_input()
    def update_file_view(self):
        return self.update_file()

    @view_config(request_method='DELETE')
    @requires_authorization()
    def delete_file_view(self):
        return self.delete_file()
