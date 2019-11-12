# -*- coding: utf-8 -*-

from tests.integration import TestsBase


def getLayers(query):
    for q in query:
        yield q[0]


class TestMapServiceView(TestsBase):

    def assertLods(self, lods):
        self.assertEqual(lods[0]['level'], 0)
        self.assertEqual(lods[0]['resolution'], 4000.0)
        self.assertEqual(lods[0]['width'], 1)
        self.assertEqual(lods[0]['height'], 1)
        self.assertEqual(lods[9]['level'], 9)
        self.assertEqual(lods[9]['resolution'], 1750.0)
        self.assertEqual(lods[9]['width'], 2)
        self.assertEqual(lods[9]['height'], 1)

    def assertSpatialReference(self, res, wkid):
        self.assertEqual(res['spatialReference']['wkid'], wkid)
        self.assertEqual(res['initialExtent']['spatialReference']['wkid'], wkid)
        self.assertEqual(res['fullExtent']['spatialReference']['wkid'], wkid)
        self.assertEqual(res['tileInfo']['spatialReference']['wkid'], wkid)

    def assertLayersConfigGroup(self, res, bod_id):
        self.assertIn(bod_id, res)
        self.assertIn('attribution', res[bod_id])
        self.assertIn('label', res[bod_id])
        self.assertIn('background', res[bod_id])
        self.assertIn('topics', res['%s_wmts' % bod_id])
        self.assertIn('topics', res[bod_id])
        self.assertNotIn('srid', res[bod_id])
        self.assertNotIn('srid', res['%s_wmts' % bod_id])
        self.assertNotIn('staging', res[bod_id])
        self.assertNotIn('staging', res[bod_id])
        self.assertNotIn('matrixSet', res[bod_id])
        self.assertNotIn('matrixSet', res['%s_wmts' % bod_id])

    def test_metadata_no_parameters(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_metadata_no_parameters_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer', status=200)
        result = resp.json
        lods = result['tileInfo']['lods']
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLods(lods)
        self.assertSpatialReference(result, 21781)

        resp = self.testapp.get('/rest/services/all/MapServer', params={'sr': '2056'}, status=200)
        result = resp.json
        lods = result['tileInfo']['lods']
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLods(lods)
        self.assertSpatialReference(result, 2056)

    def test_metadata_with_searchtext(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'searchText': 'wasser'}, status=200)
        result = resp.json
        lods = result['tileInfo']['lods']
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLods(lods)
        self.assertSpatialReference(result, 21781)

        resp = self.testapp.get('/rest/services/blw/MapServer', params={'searchText': 'wasser', 'sr': '2056'}, status=200)
        result = resp.json
        lods = result['tileInfo']['lods']
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLods(lods)
        self.assertSpatialReference(result, 2056)

    def test_metadata_with_callback(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_metadata_chargeable_true(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'chargeable': 'true'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_metadata_chargeable_false(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'chargeable': 'false'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_faqlist(self):
        resp = self.testapp.get('/rest/services/api/faqlist', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('ch.astra.ivs-nat', resp.json['searchableLayers'])
        self.assertIn('ch.are.agglomerationen_isolierte_staedte', resp.json['tooltipLayers'])
        self.assertIn('ch.swisstopo-karto.hangneigung', resp.json['chargeableLayers'])
        self.assertIn('ch.are.alpenkonvention', resp.json['notChargeableLayers'])
        self.assertGreater(len(resp.json['searchableLayers']), 20)
        self.assertGreater(len(resp.json['tooltipLayers']), 20)
        self.assertGreater(len(resp.json['chargeableLayers']), 20)
        self.assertGreater(len(resp.json['notChargeableLayers']), 20)
        self.assertGreater(len(resp.json['translations']), 20)

    def test_faqlist_topic_all(self):
        resp = self.testapp.get('/rest/services/all/faqlist', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('ch.astra.ivs-nat', resp.json['searchableLayers'])
        self.assertIn('ch.are.agglomerationen_isolierte_staedte', resp.json['tooltipLayers'])
        self.assertIn('ch.swisstopo-karto.hangneigung', resp.json['chargeableLayers'])
        self.assertIn('ch.are.alpenkonvention', resp.json['notChargeableLayers'])
        self.assertGreater(len(resp.json['searchableLayers']), 20)
        self.assertGreater(len(resp.json['tooltipLayers']), 20)
        self.assertGreater(len(resp.json['chargeableLayers']), 20)
        self.assertGreater(len(resp.json['notChargeableLayers']), 20)
        self.assertGreater(len(resp.json['translations']), 20)

    def test_legend_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/legend', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<div class="legend-header">')

    def test_legend_valid_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.bundesinventare-bln/legend', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<div class="legend-header">')

    def test_legend_wrong_layer_id(self):
        self.testapp.get('/rest/services/ech/MapServer/dummylayer/legend', status=404)

    def test_legend_valid_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/legend', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')

    def test_layersconfig_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/layersConfig', status=200)
        self.assertEqual(resp.content_type, 'application/json')

        resp = self.testapp.get('/rest/services/ech/MapServer/layersConfig', params={'sr': '2056'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_layersconfig_valid_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('ch.swisstopo.pixelkarte-farbe', resp.json)
        self.assertIn('attribution', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertIn('label', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertIn('background', resp.json['ch.swisstopo.pixelkarte-farbe'])
        # Test geojson config
        self.assertIn('ch.bafu.hydroweb-messstationen_gefahren', resp.json)
        self.assertIn('label', resp.json['ch.bafu.hydroweb-messstationen_gefahren'])
        self.assertIn('geojsonUrl', resp.json['ch.bafu.hydroweb-messstationen_gefahren'])
        self.assertIn('updateDelay', resp.json['ch.bafu.hydroweb-messstationen_gefahren'])
        self.assertIn('styleUrl', resp.json['ch.bafu.hydroweb-messstationen_gefahren'])
        self.assertNotIn('format', resp.json['ch.bafu.hydroweb-messstationen_gefahren'])
        self.assertNotIn('timeBehaviour', resp.json['ch.bafu.hydroweb-messstationen_gefahren'])

    def test_layersconfig_geojson_and_extent_layer(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        res = resp.json
        if 'ch.bafu.hydroweb-messstationen_gefahren' in res:
            layer = res['ch.bafu.hydroweb-messstationen_gefahren']
            self.assertEqual(layer['type'], 'geojson')
            self.assertIn('geojsonUrl', layer)
            self.assertNotIn('geojsonUrlDe', layer)
            self.assertIn('styleUrl', layer)
            self.assertIn('updateDelay', layer)
        if 'ch.swisstopo.swiss-map-vector1000.metadata' in res:
            layer = res['ch.swisstopo.swiss-map-vector1000.metadata']
            self.assertIn('extent', layer)
            extent = layer['extent']
            self.assertEqual(len(extent), 4)
            self.assertIsInstance(extent[0], float)
            self.assertIsInstance(extent[1], float)
            self.assertIsInstance(extent[2], float)
            self.assertIsInstance(extent[3], float)

        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', params={'sr': '2056'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        res = resp.json
        if 'ch.bafu.hydroweb-messstationen_gefahren' in res:
            layer = res['ch.bafu.hydroweb-messstationen_gefahren']
            self.assertEqual(layer['type'], 'geojson')
            self.assertIn('geojsonUrl', layer)
            self.assertNotIn('geojsonUrlDe', layer)
            self.assertIn('styleUrl', layer)
            self.assertIn('updateDelay', layer)
        if 'ch.swisstopo.swiss-map-vector1000.metadata' in res:
            layer = res['ch.swisstopo.swiss-map-vector1000.metadata']
            self.assertIn('extent', layer)
            extent = layer['extent']
            self.assertEqual(len(extent), 4)
            self.assertIsInstance(extent[0], float)
            self.assertIsInstance(extent[1], float)
            self.assertIsInstance(extent[2], float)
            self.assertIsInstance(extent[3], float)

    def test_layersconfig_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/layersConfig', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')

    def test_layersconfig_wrong_map(self):
        self.testapp.get('/rest/services/foo/MapServer/layersConfig', status=400)

    def test_layersconfig_queryable_attributes(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        jsonData = resp.json
        self.assertIn('ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp', jsonData)
        layer = jsonData['ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp']
        self.assertIn('queryableAttributes', layer)
        self.assertGreater(len(layer['queryableAttributes']), 0)
        # Should not have
        self.assertIn('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', jsonData)
        layer = jsonData['ch.swisstopo.vec200-transportation-oeffentliche-verkehr']
        self.assertNotIn('queryableAttributes', layer)

    def test_layer_attributes(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        resp = self.testapp.get('/rest/services/api/MapServer/ch.mobility.standorte', status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_layer_attributes_lang_specific(self):
        lang = 'de'
        path = '/rest/services/all/MapServer/ch.bav.sachplan-infrastruktur-schiene_ausgangslage'
        params = {'lang': lang}
        resp = self.testapp.get(path, params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        fields = resp.json['fields']
        langSpecFields = []
        for field in fields:
            if field['name'].endswith('_%s' % lang):
                langSpecFields.append(field)
        self.assertGreater(len(langSpecFields), 0)
        langNotAvailable = 'rm'
        params = {'lang': langNotAvailable}
        resp = self.testapp.get(path, params=params, status=200)
        fields = resp.json['fields']
        langSpecFields = []
        # Check fallback lang
        for field in fields:
            if field['name'].endswith('_%s' % lang):
                langSpecFields.append(field)
        self.assertGreater(len(langSpecFields), 0)

    def test_layer_attributes_wrong_layer(self):
        self.testapp.get('/rest/services/ech/MapServer/dummy', status=400)

    def test_layer_attributes_multi_models(self):
        resp = self.testapp.get('/rest/services/api/MapServer/ch.bav.sachplan-infrastruktur-schiene_kraft', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json['fields']), 3)

    def test_features_attributes_multi_models(self):
        resp = self.testapp.get('/rest/services/api/MapServer/ch.bav.sachplan-infrastruktur-schiene_kraft/attributes/plname_de', status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')

    def test_features_attributes_multi_models_integer_colType(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata/attributes/id', status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')

    def test_layer_attributes_none_models(self):
        self.testapp.get('/rest/services/ech/MapServer/wrongLayerId/attributes/id', status=400)

    def test_layer_attributes_none_modelToQuery(self):
        self.testapp.get('/rest/services/ech/MapServer/ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata/attributes/wrongAttribute', status=400)
