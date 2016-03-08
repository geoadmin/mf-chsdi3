# -*- coding: utf-8 -*-


gridLayers = {}


grids = {
    '1': {
        'extent': [485349.96, 75250.055, 833849.959, 295950.054],
        'resolutionX': 100.0,
        'resolutionY': -100.0,
        'srid': '21781'
    }
}


def register_bodid_gridid(layerBodId, gridId=None, timestamp=None, template=None):
    gridLayers[layerBodId] = {
        'gridId': gridId,
        'timestamp': timestamp,
        'template': template
    }


def get_grid_spec(layerBodId):
    layerSpec = gridLayers.get(layerBodId)
    if layerSpec:
        return grids.get(layerSpec.get('gridId'))


def get_grid_layer_timestamp(layerBodId):
    layerSpec = gridLayers.get(layerBodId)
    if layerSpec:
        return layerSpec.get('timestamp')


def get_grid_layer_template(layerBodId):
    layerSpec = gridLayers.get(layerBodId)
    if layerSpec:
        return layerSpec.get('template')


# Windatlas layers
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h50', gridId='1',
                      timestamp='20160303', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h75', gridId='1',
                      timestamp='20160303', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h100', gridId='1',
                      timestamp='20160303', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h125', gridId='1',
                      timestamp='20160303', template='templates/htmlpopup/windatlas50.mako')
register_bodid_gridid('ch.bfe.windenergie-geschwindigkeit_h150', gridId='1',
                      timestamp='20160303', template='templates/htmlpopup/windatlas50.mako')
