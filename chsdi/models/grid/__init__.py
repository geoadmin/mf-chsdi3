# -*- coding: utf-8 -*-


gridLayers = {}


grids = {
    '1': {
        'extent': [485349.96, 75250.055, 833849.959, 295950.054],
        'resolutionX': 100.0,
        'resolutionY': -100.0,
        'srid': '21781'
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
                      timestamp='20160223', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h75', gridId='1', extended=True,
                      timestamp='20160223', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h100', gridId='1', extended=True,
                      timestamp='20160223', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h125', gridId='1', extended=True,
                      timestamp='20160223', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h150', gridId='1', extended=True,
                      timestamp='20160223', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor', gridId='2', extended=False,
                      timestamp='20150701', template='templates/htmlpopup/phosphor.mako')
register_bodid_gridid('ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff', gridId='3', extended=False,
                      timestamp='20150701', template='templates/htmlpopup/stickstoff.mako')
