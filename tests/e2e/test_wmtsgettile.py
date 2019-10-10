# -*- coding: utf-8 -*-

import requests
import random

from tests.e2e import TodProxyTestsBase

# Official URLS we support
WMTS_URLS = [
    'wmts.geo.admin.ch',
    'wmts1.geo.admin.ch',
    'wmts2.geo.admin.ch',
    'wmts3.geo.admin.ch',
    'wmts4.geo.admin.ch',
    'wmts5.geo.admin.ch',
    'wmts6.geo.admin.ch',
    'wmts7.geo.admin.ch',
    'wmts8.geo.admin.ch',
    'wmts9.geo.admin.ch'
]


def rotateUrl(url):
    return url.replace(WMTS_URLS[0], WMTS_URLS[random.randint(0, len(WMTS_URLS) - 1)]).replace(WMTS_URLS[0], WMTS_URLS[random.randint(0, len(WMTS_URLS) - 1)])

HEADER_RESULTS = [{
    'Results': [200, 304],
    'Header': {'User-Agent': 'WMTS Unit Tester v0.0.1', 'Referer': 'http://unittest.geo.admin.ch'}
}, {
    'Results': [403],
    'Header': {'User-Agent': 'WMTS Unit Tester v0.0.1', 'Referer': None}
}, {
    'Results': [403],
    'Header': {'User-Agent': 'WMTS Unit Tester v0.0.1', 'Referer': 'http://foonogood.ch'}
}
]


def get_header():
    return HEADER_RESULTS[random.randint(0, len(HEADER_RESULTS) - 1)]


class TileChecker(TodProxyTestsBase):

    def __init__(self):
        super(TileChecker, self).setUp()

    def __enter__(self):
        self.session = requests.Session()
        self.session.mount("http://", requests.adapters.HTTPAdapter(max_retries=5))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.tearDown()
        return False

    def check_status_code(self, path):
        url = rotateUrl(path)
        h = get_header()
        self.session.headers.update(h['Header'])
        resp = self.session.get(url, timeout=(5, 30))
        checkcode = resp.status_code in h['Results']
        if 'ch.astra.ivs-nat-verlaeufe' in path or 'ch.swisstopo.vec25-eisenbahnnetz' in path:
            checkcode = (checkcode or resp.status_code == 500)
        assert checkcode, url

    def itiles(self, epsg=21781):
        from urlparse import urlparse, urlunparse
        import xml.etree.ElementTree as etree

        tiles = {3857: [(16, 34243, 23004)],
                 21781: [(17, 5, 6)],
                 2056: [(17, 5, 6)],
                 4326: [(15, 34136, 7882)]
                 }

        if epsg in tiles.keys():
            capabilities_name = "WMTSCapabilities.EPSG.%d.xml" % epsg if epsg != 21781 else "WMTSCapabilities.xml"
            resp = requests.get(self.host_url + '/1.0.0/%s' % capabilities_name, params={'_id': self.hash()},
                                headers=HEADER_RESULTS[0]['Header'])

            root = etree.fromstring(resp.content)
            layers = root.findall('.//{http://www.opengis.net/wmts/1.0}Layer')
            for layer in layers:
                resourceurls = layer.findall('.//{http://www.opengis.net/wmts/1.0}ResourceURL')
                for resourceurl in resourceurls:
                    tpl = resourceurl.attrib['template']
                    tpl_parsed = urlparse(tpl)
                    pth = tpl_parsed.path

                    dim = layer.find('.//{http://www.opengis.net/wmts/1.0}Dimension')
                    times = dim.findall('./{http://www.opengis.net/wmts/1.0}Value')
                    tilematrixset = layer.find('.//{http://www.opengis.net/wmts/1.0}TileMatrixSet')
                    maxzoom = [int(s) for s in tilematrixset.text.split('_')][1]

                    tiles_proj = tiles[epsg]
                    if maxzoom > tiles_proj[0][0]:
                        for tile in tiles_proj:
                            zoom, col, row = tile
                            for time in times:
                                t = time.text
                                try:
                                    pth2 = pth.replace('{TileCol}', str(col)).replace('{TileRow}', str(row)).replace('{TileMatrix}', str(zoom)).replace('{Time}', str(t))
                                except Exception:
                                    print('Cannot replace in template {}'.format(pth))
                                yield urlunparse((tpl_parsed.scheme, tpl_parsed.netloc, pth2, '', '', ''))


def test_epsg21781():
    with TileChecker() as tc:
        for tile in tc.itiles():
            yield tc.check_status_code, tile


def test_epsg3857():
    with TileChecker() as tc:
        for tile in tc.itiles(epsg=3857):
            yield tc.check_status_code, tile


def test_epsg2056():
    with TileChecker() as tc:
        for tile in tc.itiles(epsg=2056):
            yield tc.check_status_code, tile


def test_epsg4326():
    with TileChecker() as tc:
        for tile in tc.itiles(epsg=4326):
            yield tc.check_status_code, tile
