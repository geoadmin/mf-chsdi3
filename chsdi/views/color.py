# -*- coding: utf-8 -*-

import os.path
import StringIO

from chsdi.lib.decorators import requires_authorization

from PIL import Image
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='color')
@requires_authorization()
def get_image_colored(request):
    r = request.matchdict['r']
    if r.isdigit() is False:
        raise HTTPBadRequest('The red channel must be an integer.')
    g = request.matchdict['g']
    if g.isdigit() is False:
        raise HTTPBadRequest('The green channel must be an integer.')
    b = request.matchdict['b']
    if b.isdigit() is False:
        raise HTTPBadRequest('The blue channel must be an integer.')
    r = int(r)
    g = int(g)
    b = int(b)
    imgName = request.matchdict['image']
    path = os.path.join(request.registry.settings['install_directory'], 'chsdi/static/images/maki/', imgName)
    if not os.path.isfile(path):
        raise HTTPBadRequest('The image to color doesn\'t exist')

    mask = Image.open(path)
    # This auto conversion gives really bad results
    if mask.mode == 'P':
        mask = mask.convert('RGBA')
    img = Image.composite(Image.new("RGB", mask.size, (r, g, b)), mask, mask)
    output = StringIO.StringIO()
    img.save(output, format='PNG')
    response = Response(output.getvalue(), content_type='image/png')
    return response
