# -*- coding: utf-8 -*-

from chsdi.lib.helpers import parse_box2d, center_from_box2d
from chsdi.views.features import _get_feature_params, _get_features
from pyramid.view import view_config

from pyramid.renderers import render_to_response
import pyramid.httpexceptions as exc


@view_config(route_name='historicalmaps')
def luftbilder(request):
    release_year = request.params.get('release_year')
    if release_year is None:
        exc.HTTPBadRequest('Please provide a parameter realease_year')

    # In order to use the validator and the associated service
    request.matchdict['map'] = 'api'
    layerId = request.params.get('layer')
    request.matchdict['layerId'] = layerId
    bildnummer = request.params.get('bildnummer')
    featureId = bildnummer + '_' + release_year
    request.matchdict['featureId'] = featureId

    # Call service directly
    params = _get_feature_params(request)
    feature, vectorModel = next(_get_features(params))
    featureBbox = parse_box2d(feature['feature'].properties['box2d'])
    center = center_from_box2d(featureBbox)

    # View specific variables
    width = request.params.get('width')
    height = request.params.get('height')
    rotation = request.params.get('rotation')
    title = request.params.get('title')
    baseUrl = request.registry.settings.get('geoadminhost')
    tileUrlBasePath = 'http://historicalmaps.geo.admin.ch/tiles'

    return render_to_response(
        'chsdi:templates/historicalmaps/viewer.mako',
        {
            'baseUrl': baseUrl,
            'title': title,
            'width': width,
            'height': height,
            'rotation': rotation,
            'bildnummer': bildnummer,
            'release_year': release_year,
            'center': center,
            'tileUrlBasePath': tileUrlBasePath,
            'params': params
        },
        request=request
    )
