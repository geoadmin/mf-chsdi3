# -*- coding: utf-8 -*-

from numpy.testing import assert_almost_equal
from tests.integration import TestsBase

EPSGS = [21781, 4326, 2056, 3857]


class TestWmtsCapabilitiesView(TestsBase):

    def test_valid_wmtscapabilities(self):
        resp = self.testapp.get('/rest/services/all/1.0.0/WMTSCapabilities.xml', status=200)
        self.assertEqual(resp.content_type, 'text/xml')
        resp.mustcontain('TileMatrixSet')

    def test_wrong_map_wmtscapabilities(self):
        resp = self.testapp.get('/rest/services/toto/1.0.0/WMTSCapabilities.xml', status=400)
        resp.mustcontain('The map you provided does not exist')

    def test_wrong_epsg_wmtscapabilities(self):
        resp = self.testapp.get('/rest/services/bafu/1.0.0/WMTSCapabilities.xml?epsg=9999', status=400)
        resp.mustcontain("EPSG:9999 not found. Must be one of 21781, 4326, 2056, 3857")

    def test_contains_correct_tilelink(self):
        resp = self.testapp.get('/rest/services/api/1.0.0/WMTSCapabilities.xml', status=200)
        # native s3 tiles (always on wmts), row/col order
        wmts_public_host = self.testapp.app.registry.settings['wmts_public_host']
        resp.mustcontain('<ResourceURL format="image/jpeg" resourceType="tile" '
                         'template="http://%s/1.0.0/ch.swisstopo.swissimage/default/{Time}/21781/{TileMatrix}/{TileRow}/{TileCol}.jpeg"/>' % wmts_public_host)
        # mapproxy, host dependant, col/row order
        resp.mustcontain('/1.0.0/ch.kantone.cadastralwebmap-farbe/default/{Time}/21781/{TileMatrix}/{TileRow}/{TileCol}.png"/>')

    def test_validate_wmtscapabilities(self):
        import os
        import six
        from six import StringIO, BytesIO
        from lxml import etree
        file_name = 'wmts.xsd'
        current_dir = os.getcwd()
        schema_dir = os.path.join(os.path.dirname(__file__), 'wmts/1.0.1/')

        if six.PY3:
            InputIO = BytesIO
        else:
            InputIO = StringIO

        def isValidSchema(resp, f_wmts):
            f_wmts = etree.parse(InputIO(resp.body))
            self.assertTrue(xml_schema.validate(f_wmts) is True)

        with open(schema_dir + file_name) as file_xml_schema:
            os.chdir(schema_dir)
            if six.PY3:
                data = file_xml_schema.read().encode('utf8')
            else:
                data = file_xml_schema.read()
            raw_schema = InputIO(data)

            xml_schema_doc = etree.parse(raw_schema)
            xml_schema = etree.XMLSchema(xml_schema_doc)
            for lang in ['de', 'fr', 'it', 'en']:
                for epsg in [4326, 2056, 3857, 21781]:
                    resp = self.testapp.get(
                        '/rest/services/api/1.0.0/WMTSCapabilities.xml',
                        params={'lang': lang, 'epsg': epsg},
                        status=200)
                    isValidSchema(resp, etree.parse(InputIO(resp.body)))
        os.chdir(current_dir)

    def test_gettile_wmtscapabilities(self):
        resp = self.testapp.get('/rest/services/inspire/1.0.0/WMTSCapabilities.xml', status=200)
        self.assertEqual(resp.content_type, 'text/xml')

    def test_tilematrixsets_are_defined(self):
        import xml.etree.ElementTree as etree
        for epsg in EPSGS:
            resp = self.testapp.get('/rest/services/inspire/1.0.0/WMTSCapabilities.xml?epsg=%s' % str(epsg), status=200)
            used_matrices = []
            defined_matrices = []

            root = etree.fromstring(resp.body)

            # Get all used TileMatrixSet
            layers = root.findall('.//{http://www.opengis.net/wmts/1.0}Layer')
            for layer in layers:
                tilematrixsets = layer.findall('.//{http://www.opengis.net/wmts/1.0}TileMatrixSetLink/*')
                for tilematrixset in tilematrixsets:
                    s = tilematrixset.text
                    if s not in used_matrices:
                        used_matrices.append(s)
            # Get all TileMatrixSets which are defined
            tile_matrixes = root.findall('.//{http://www.opengis.net/wmts/1.0}TileMatrixSet/{http://www.opengis.net/wmts/1.0}TileMatrix')
            for tile_matrix in tile_matrixes:
                top_left_corner = tile_matrix.find('.//{http://www.opengis.net/wmts/1.0}TopLeftCorner')
                left, right = top_left_corner.text.split(' ')
                if epsg == 4326:
                    self.assertEqual(float(left), 90)
                    self.assertEqual(float(right), -180)
                elif epsg == 21781:
                    self.assertEqual(float(left), 420000)
                    self.assertEqual(float(right), 350000)
                elif epsg == 2056:
                    self.assertEqual(float(left), 2420000)
                    self.assertEqual(float(right), 1350000)
                else:
                    assert_almost_equal(float(left), -20037508.3428, decimal=2)
                    assert_almost_equal(float(right), 20037508.3428, decimal=2)

            tilematrixsets_ids = root.findall(
                './/{http://www.opengis.net/wmts/1.0}TileMatrixSet/{http://www.opengis.net/ows/1.1}Identifier')

            for tilematrixset_id in tilematrixsets_ids:
                t = tilematrixset_id.text
                if t not in defined_matrices:
                    defined_matrices.append(t)

            self.assertTrue(set(used_matrices).issubset(defined_matrices))

    def test_maximum_extent_for_non_swiss(self):
        import xml.etree.ElementTree as etree

        resp = self.testapp.get('/rest/services/api/1.0.0/WMTSCapabilities.xml', params={'epsg': 3857}, status=200)

        root = etree.fromstring(resp.body)
        tilematrices = root.findall('.//{http://www.opengis.net/wmts/1.0}TileMatrix')
        for tilematrix in tilematrices:
            id = tilematrix.find('./{http://www.opengis.net/ows/1.1}Identifier')
            if id.text == '0':
                topleft = tilematrix.find('./{http://www.opengis.net/wmts/1.0}TopLeftCorner')
                coords = topleft.text.split(' ')
                assert_almost_equal(float(coords[0]), -20037508.3428, decimal=4)
                assert_almost_equal(float(coords[1]), 20037508.3428, decimal=4)

    def test_axis_order(self):
        try:
            from urllib.parse import urlparse
        except ImportError:
            from urlparse import urlparse
        import xml.etree.ElementTree as etree

        for epsg in EPSGS:
            resp = self.testapp.get('/rest/services/api/1.0.0/WMTSCapabilities.xml', params={'epsg': epsg}, status=200)

            root = etree.fromstring(resp.body)
            layers = root.findall('.//{http://www.opengis.net/wmts/1.0}Layer')
            for layer in layers:
                resourceurls = layer.findall('.//{http://www.opengis.net/wmts/1.0}ResourceURL')
                for resourceurl in resourceurls:
                    tpl = resourceurl.attrib['template']
                    tpl_parsed = urlparse(tpl)
                    pth = tpl_parsed.path
                    col_idx = pth.find('{TileCol}')
                    row_idx = pth.find('{TileRow}')
                    is_normal_order = col_idx < row_idx if col_idx > 0 else None
                    if epsg == 21781:
                        self.assertFalse(is_normal_order)
                    else:
                        self.assertTrue(is_normal_order)

    def test_layers_refs_are_defined(self):
        import xml.etree.ElementTree as etree
        resp = self.testapp.get('/rest/services/inspire/1.0.0/WMTSCapabilities.xml', status=200)
        root = etree.fromstring(resp.body)

        layers_refs = []
        defined_layers = []

        # Get all Layers Refs
        themes = root.findall(('.//{http://www.opengis.net/wmts/1.0}Themes'))
        for theme in themes:
            refs = theme.findall('.//{http://www.opengis.net/wmts/1.1}LayerRef')
            for ref in refs:
                lr = ref.text
                if lr not in layers_refs:
                    layers_refs.append(lr)

        # Get all Layers
        layers = root.findall('.//{http://www.opengis.net/wmts/1.0}Layer')
        for layer in layers:
            bodid = layer.find('./{http://www.opengis.net/ows/1.1}Identifier').text
            if bodid not in defined_layers:
                defined_layers.append(bodid)

        self.assertTrue(set(layers_refs).issubset(defined_layers))
