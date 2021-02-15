# -*- coding: utf-8 -*-


gridLayers = {}


grids = {
    '1': {
        'extent': [2485350.00, 1075250.00, 2833950.00, 1296050.00],
        'resolutionX': 100.0,
        'resolutionY': -100.0,
        'srid': '2056'
    },
    '2': {
        'extent': [485450.00, 75350.00, 833850.00, 295950.00],
        'resolutionX': 100.0,
        'resolutionY': -100.0,
        'srid': '21781'
    },
    '3': {
        'extent': [486450.00, 75450.00, 833550.00, 295550.00],
        'resolutionX': 100.0,
        'resolutionY': -100.0,
        'srid': '21781'
    },
    '4': {
        'extent': [2485410.040, 1075269.945, 2833710.041, 1295969.946],
        'resolutionX': 2.000000003445305,
        'resolutionY': -2.000000004531038,
        'srid': '2056'
    }

}


def register_bodid_gridid(layerBodId, gridId=None, timestamp=None, template=None, extended=False):
    gridLayers[layerBodId] = {
        'gridId': gridId,
        'timestamp': timestamp,
        'template': template,
        'extended': extended
    }


def get_grid_spec(layerBodId):
    layerSpec = gridLayers.get(layerBodId)
    if layerSpec:
        return grids.get(layerSpec.get('gridId'))


def get_grid_layer_properties(layerBodId):
    layerSpec = gridLayers.get(layerBodId)
    if layerSpec:
        return layerSpec


# Windatlas layers
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h50', gridId='1', extended=True,
                      timestamp='20181001', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h75', gridId='1', extended=True,
                      timestamp='20181001', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h100', gridId='1', extended=True,
                      timestamp='20181001', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h125', gridId='1', extended=True,
                      timestamp='20181001', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h150', gridId='1', extended=True,
                      timestamp='20181001', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor', gridId='2', extended=False,
                      timestamp='20150701', template='templates/htmlpopup/phosphor.mako')
register_bodid_gridid('ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff', gridId='3', extended=False,
                      timestamp='20150701', template='templates/htmlpopup/stickstoff.mako')

# ch.blw.erosion-quantitativ layer
register_bodid_gridid('ch.blw.erosion-quantitativ', gridId='4', extended=False,
                      timestamp='20190330', template='templates/htmlpopup/erosion_quantitativ.mako')

