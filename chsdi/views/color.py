# -*- coding: utf-8 -*-

import Image
import StringIO

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='color')
def get_image_colored(request):
    r = request.matchdict['r']
    if r.isdigit() is False:
        raise HTTPBadRequest('The red channel must be an integer.')
    g = request.matchdict['g']
    if g.isdigit() is False:
        raise HTTPBadRequest('The green channel must be an integer.')
    b = request.matchdict['b']
    if g.isdigit() is False:
        raise HTTPBadRequest('The blue channel must be an integer.')
    r = int(r)
    g = int(g)
    b = int(b)
    imgName = request.matchdict['image']
    if imgName is None:
        raise HTTPBadRequest('The image to color must be defined')

    mask = Image.open('chsdi/static/images/maki/' + imgName)

    # This auto conversion gives really bad results
    if mask.mode == 'P':
        mask = mask.convert('RGBA')

    img = Image.composite(Image.new("RGB", mask.size, (r, g, b)), mask, mask)
    output = StringIO.StringIO()
    img.save(output, format='PNG')
    response = Response(output.getvalue(), content_type='image/png')
    return response
