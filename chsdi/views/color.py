# -*- coding: utf-8 -*-

import os.path

from PIL import Image
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config
from pyramid.response import Response

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class ColorService:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='color')
    def get_image_colored(self):
        r = self.request.matchdict['r']
        if r.isdigit() is False:
            raise HTTPBadRequest('The red channel must be an integer.')
        g = self.request.matchdict['g']
        if g.isdigit() is False:
            raise HTTPBadRequest('The green channel must be an integer.')
        b = self.request.matchdict['b']
        if b.isdigit() is False:
            raise HTTPBadRequest('The blue channel must be an integer.')
        r = int(r)
        g = int(g)
        b = int(b)
        imgName = self.request.matchdict['image']
        path = os.path.join(self.request.registry.settings['install_directory'], 'chsdi/static/images/maki/', imgName)
        if not os.path.isfile(path):
            raise HTTPBadRequest('The image to color doesn\'t exist')

        mask = Image.open(path)
        # This auto conversion gives really bad results
        if mask.mode == 'P':
            mask = mask.convert('RGBA')
        img = Image.composite(Image.new("RGB", mask.size, (r, g, b)), mask, mask)
        output = StringIO()
        img.save(output, format='PNG')
        response = Response(output.getvalue(), content_type='image/png')
        return response
