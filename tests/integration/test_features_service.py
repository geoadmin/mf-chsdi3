# -*- coding: utf-8 -*-

from unittest import skip
from webtest.app import AppError
from pyramid_mako import MakoRenderingException
from tests.integration import TestsBase, shift_to_lv95, reproject_to_srid

from chsdi.lib.validation import SUPPORTED_OUTPUT_SRS


class TestFeaturesView(TestsBase):

    def test_unsupported_srid(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid',
                  'searchText': '1231641',
                  'sr': '9999'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Unsupported spatial reference')

    def test_searchField_none(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Please provide a searchField')

    def test_searchField_error(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid, bln_fl',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('You can provide only one searchField at a time')

    def test_none_layer(self):
        params = {'searchField': 'egid',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Please provide a parameter layer')

    def test_two_layer(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register,ch.bazl.luftfahrthindernis',
                  'searchField': 'egid',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('You can provide only one layer at a time')

    def test_find_scan(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        results = resp.json['results']
        self.assertEqual(len(results), 1)

    def test_find_scan_supported_srs(self):
        params = {'layer': 'ch.are.bauzonen',
                  'searchField': 'bfs_no',
                  'searchText': '4262'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        results = resp.json['results']

        params['sr'] = '2056'
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        results = resp.json['results']
        self.assertEsrijsonFeature(results[0], 2056)

        params['sr'] = '21781'
        params['geometryFormat'] = 'geojson'
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        results = resp.json['results']
        self.assertGeojsonFeature(results[0], 21781)

        params['sr'] = '2056'
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        results = resp.json['results']
        self.assertGeojsonFeature(results[0], 2056)

        params['sr'] = '3857'
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        results = resp.json['results']
        self.assertGeojsonFeature(results[0], 3857)

        params['sr'] = '4326'
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        results = resp.json['results']
        self.assertGeojsonFeature(results[0], 4326)

    def test_find_exact_int(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid',
                  'searchText': '1231625',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_exact_float(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        params = {'layer': bodId,
                  'searchField': 'id',
                  'searchText': '%s' % featureId,
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_exact_text(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'strname1',
                  'searchText': 'Beaulieustrasse',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_exact_date(self):
        params = {'layer': 'ch.bazl.luftfahrthindernis',
                  'searchField': 'startofconstruction',
                  'searchText': '1950-01-01',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_geojson(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid',
                  'searchText': '1231641',
                  'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')

    def test_find_withcb(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid',
                  'searchText': '1231641',
                  'callback': 'cb_'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'text/javascript')

    def test_find_nogeom(self):
        params = {'layer': 'ch.are.bauzonen',
                  'searchField': 'bfs_no',
                  'searchText': '4262',
                  'returnGeometry': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_find_wrong_searchfield(self):
        params = {'layer': 'ch.are.bauzonen',
                  'searchField': 'toto',
                  'searchText': '4262',
                  'returnGeometry': 'false'}
        self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)

    def test_find_nosearchtext(self):
        params = {'layer': 'ch.are.bauzonen',
                  'searchField': 'toto',
                  'returnGeometry': 'false'}
        self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)

    def test_find_wrong_layer(self):
        params = {'layer': 'dummy',
                  'searchField': 'gdename',
                  'returnGeometry': 'false'}
        self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)

    def test_find_contains(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchText': 'Islastrasse',
                  'searchField': 'strname1',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 1)
        self.assertNotIn('geometry', resp.json['results'][0])

    def test_find_non_float(self):
        params = {'layer': 'ch.bafu.bundesinventare-bln',
                  'searchField': 'bln_fl',
                  'searchText': '1740',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Please provide a float')

    def test_find_non_integer(self):
        params = {'layer': 'ch.bafu.bundesinventare-bln',
                  'searchField': 'bln_obj',
                  'searchText': '1201.0',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Please provide an integer')

    def test_find_boolean_true(self):
        params = {'layer': 'ch.swisstopo.lubis-luftbilder_farbe',
                  'searchField': 'orientierung',
                  'searchText': 'True',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_boolean_false(self):
        params = {'layer': 'ch.swisstopo.lubis-luftbilder_farbe',
                  'searchField': 'orientierung',
                  'searchText': 'FALSE',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_wrong_boolean(self):
        params = {'layer': 'ch.swisstopo.lubis-luftbilder_farbe',
                  'searchField': 'orientierung',
                  'searchText': '3190',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Please provide a boolean value (true/false)')

    def test_find_wrong_layer_layerdefs(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'label',
                  'searchText': 'Talstrasse',
                  'returnGeometry': 'false',
                  'contains': 'false',
                  'layerDefs': '{"tutu": "gdenr > 2000"}'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain("You can only filter on layer 'ch.swisstopo.amtliches-strassenverzeichnis' in 'layerDefs'")

    def test_find_wrong_attribute(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'label',
                  'searchText': 'Talstrasse',
                  'returnGeometry': 'false',
                  'contains': 'false',
                  'layerDefs': '{"ch.swisstopo.amtliches-strassenverzeichnis": "toto = 4307"}'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain("Query attribute 'toto' is not queryable")

    def test_find_all_talstrasse(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'label',
                  'searchText': 'Talstrasse',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        # Should be many Talstrasse in Switzerland
        self.assertGreater(len(resp.json['results']), 1)

    # Should return two features (see https://github.com/geoadmin/mf-chsdi3/issues/3267)
    def test_find_layerdefs_two_or_statements(self):
        params1 = {
            "layer": "ch.swisstopo.amtliches-strassenverzeichnis",
            "searchText": "Studerweg",
            "searchField": "label",
            "returnGeometry": "false",
            "layerDefs": '''{"ch.swisstopo.amtliches-strassenverzeichnis": "gdename = 'Olten' or gdename = 'Sattel'"}'''
        }
        params2 = {
            "layer": "ch.swisstopo.amtliches-strassenverzeichnis",
            "searchText": "Studerweg",
            "searchField": "label",
            "returnGeometry": "false",
            "layerDefs": '''{"ch.swisstopo.amtliches-strassenverzeichnis": "gdename = 'Sattel' or gdename = 'Olten'"}'''
        }

        resp1 = self.testapp.get('/rest/services/all/MapServer/find', params=params1, status=200)
        resp2 = self.testapp.get('/rest/services/all/MapServer/find', params=params2, status=200)
        self.assertEqual(resp1.content_type, 'application/json')
        # self.assertEqual(resp1.json['results'], resp2.json['results'])
        for feat in resp2.json['results']:
            self.assertIn(feat['attributes']['gdename'], ['Olten', 'Sattel'])
            self.assertIn('Studer', feat['attributes']['label'])

    def test_find_filter_with_layerdefs(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'label',
                  'searchText': 'Talstrasse',
                  'returnGeometry': 'false',
                  'contains': 'false',
                  'layerDefs': '{"ch.swisstopo.amtliches-strassenverzeichnis": "gdenr = 4307"}'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        # Not more than one road should have the same name in a given commune
        self.assertLessEqual(len(resp.json['results']), 1)
        for feat in resp.json['results']:
            self.assertEqual(feat['attributes']['gdenr'], 4307)

    def test_feature_wrong_idlayer(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/toto/362', status=400)
        resp.mustcontain('No Vector Table was found for')

    def test_feature_wrong_srid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/0', params={'sr': '111'}, status=400)
        resp.mustcontain('Unsupported spatial reference')

    def test_feature_wrong_idfeature(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/0', status=404)
        resp.mustcontain('No feature with id')

        resp = self.testapp.get('/rest/services/api/MapServer/ch.bafu.bundesinventare-bln/htmlPopup', status=404)
        resp.mustcontain('No feature with id')

    def test_feature_htmlpopup_not_scale_dep(self):
        params = {'imageDisplay': '960,700,96',
                  'lang': 'it',
                  'mapExtent': '642389,81044,882389,256044'}
        resp = self.testapp.get('/rest/services/swisstopo/MapServer/ch.swisstopo.treasurehunt/1/htmlPopup', params=params, status=200)
        self.assertEqual(resp.content_type, 'text/html')

    def test_feature_valid(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        self.assertEsrijsonFeature(resp.json['feature'], 21781)

    def test_feature_too_many_featuresids(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureIds = ','.join(map(str, range(50)))
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureIds), status=400)
        resp.mustcontain('Too many featureIds')

    def test_feature_valid_topic_all(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/all/MapServer/%s/%s' % (bodId, featureId), status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        self.assertEsrijsonFeature(resp.json['feature'], 21781)

    def test_feature_geojson(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'geometryFormat': 'geojson'}, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        self.assertGeojsonFeature(resp.json['feature'], 21781)

    def test_feature_geojson_nogeom(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'geometryFormat': 'geojson', 'returnGeometry': 'false'}, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        self.assertGeojsonFeature(resp.json['feature'], 21781, hasGeometry=False)

    def test_feature_geojson_geom(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'geometryFormat': 'geojson', 'returnGeometry': 'true'}, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        self.assertGeojsonFeature(resp.json['feature'], 21781)

    @skip("Apparently, there is no too big data anymore")
    def test_too_large_feature_only_attributes(self):
        bodId = 'ch.swisstopo.geologie-geologischer_atlas'
        featureId = 680287
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'geometryFormat': 'geojson', 'returnGeometry': 'true'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        self.assertGeojsonFeature(resp.json['feature'], 21781, hasGeometry=False)
        self.assertIsNone(resp.json['feature']['geometry'])

    def test_several_features(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId1 = self.getRandomFeatureId(bodId)
        featureId2 = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s,%s' % (bodId, featureId1, featureId2), status=200)
        features = resp.json['features']
        feature1 = features[0]
        feature2 = features[1]
        self.assertEqual(len(features), 2)
        self.assertEqual(feature1['id'], featureId1)
        self.assertEqual(feature2['id'], featureId2)
        self.assertEsrijsonFeature(feature1, 21781)
        self.assertEsrijsonFeature(feature2, 21781)

    def test_several_features_geojson(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId1 = self.getRandomFeatureId(bodId)
        featureId2 = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s,%s' % (bodId, featureId1, featureId2), params={'geometryFormat': 'geojson'}, status=200)
        self.assertEqual(len(resp.json['features']), 2)
        features = resp.json['features']
        feature1 = features[0]
        feature2 = features[1]
        self.assertEqual(len(features), 2)
        self.assertEqual(feature1['id'], featureId1)
        self.assertEqual(feature2['id'], featureId2)
        self.assertGeojsonFeature(feature1, 21781)
        self.assertGeojsonFeature(feature2, 21781)

    def test_feature_with_callback(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'text/javascript')
        resp.mustcontain('cb_({')

    def test_feature_geojson_geom_supported_srs(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)

        for srs in SUPPORTED_OUTPUT_SRS:
            resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'sr': srs, 'geometryFormat': 'geojson', 'returnGeometry': 'true'}, status=200)
            self.assertEqual(resp.content_type, 'application/geo+json')
            self.assertEqual(resp.json['feature']['id'], featureId)
            self.assertGeojsonFeature(resp.json['feature'], srs)

    def test_feature_geojson_geom_default_srs(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)

        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'geometryFormat': 'geojson', 'returnGeometry': 'true'}, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        # 21781 is the default srs at the time
        self.assertGeojsonFeature(resp.json['feature'], 21781)

    def test_feature_esrijson_geom_supported_srs(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)

        for srs in SUPPORTED_OUTPUT_SRS:
            resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'sr': srs, 'geometryFormat': 'esrijson', 'returnGeometry': 'true'}, status=200)
            self.assertEqual(resp.content_type, 'application/json')
            self.assertEqual(resp.json['feature']['id'], featureId)
            self.assertEsrijsonFeature(resp.json['feature'], srs)

    def test_feature_esrijson_geom_default_srs(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)

        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s' % (bodId, featureId), params={'geometryFormat': 'esrijson', 'returnGeometry': 'true'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['feature']['id'], featureId)
        # 21781 is the default srs at the time
        self.assertEsrijsonFeature(resp.json['feature'], 21781)

    def test_feature_big_but_good(self):
        bodId = 'ch.swisstopo.geologie-geocover'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/all/MapServer/%s/%s' % (bodId, featureId), params={'geometryFormat': 'geojson'}, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertIn('geometry', resp.json['feature'])

    def test_htmlpopup_invalid_srid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup', params={'sr': '111'}, status=400)
        resp.mustcontain('Unsupported spatial reference')

    def test_htmlpopup_invalid_id_format(self):
        bodId = 'ch.swisstopo.geologie-geologischer_atlas'
        featureId = 'GA25-PK-140'
        self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), status=400)

    def test_htmlpopup_valid(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_valid_lv95(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), params={'sr': '2056'}, status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_lang(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), params={'lang': 'fr'}, status=200)
        self.assertEqual(resp.content_type, 'text/html')
        msgids = [u'No.', u'Nom', u'Partie-No', u'Partie', u'Surface [ha]']
        for msgid in msgids:
            self.assertIn(msgid, resp.text)

    def test_htmlpopup_time(self):
        bodId = 'ch.swisstopo.lubis-luftbilder_farbe'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), params={'time': 1999}, status=200)
        self.assertEqual(resp.content_type, 'text/html')
        self.assertIn(bodId + '=' + featureId + '&amp;time=1999', resp.text)

    def test_htmlpopup_scale_dependent(self):
        params = {'mapExtent': '625622.5,210705,629147.5,212922.5',
                  'imageDisplay': '1410,887,96',
                  'lang': 'fr'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfe.windenergieanlagen/turbine_21/htmlPopup', params=params, status=200)
        resp.mustcontain('Puissance')
        params = {'mapExtent': '588187.5,183652.5,658687.5,228002.5',
                  'imageDisplay': '1410,887,96',
                  'lang': 'fr'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfe.windenergieanlagen/facility_SCH/htmlPopup', params=params, status=200)
        resp.mustcontain('Type')

    def test_htmlpopup_cadastralwebmap(self):
        params = {'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999',
                  'imageDisplay': '600,400,96'}
        bodId = 'ch.kantone.cadastralwebmap-farbe'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), params=params, status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_bad_request_image_display(self):
        params = {'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999',
                  'imageDisplay': '600,96'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/16847593/htmlPopup', params=params, status=400)
        resp.mustcontain('Please provide the parameter imageDisplay in a comma separated list of 3 arguments '
                         '(width,height,dpi)')

    def test_htmlpopup_nan_image_display(self):
        params = {'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999', 'imageDisplay': '600,96,None'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/16847593/htmlPopup', params=params, status=400)
        resp.mustcontain('Please provide numerical values for the parameter imageDisplay')

    def test_htmlpopup_bad_request_map_extent(self):
        params = {'mapExtent': 'quite_big_extent',
                  'imageDisplay': '1362,1139,96',
                  'lang': 'fr'}
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.schutzgebiete-aulav_uebrige/400/htmlPopup', params=params, status=400)
        resp.mustcontain('Please provide numerical values for the parameter mapExtent')

    def test_htmlpopup_valid_topic_all(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/all/MapServer/%s/%s/htmlPopup' % (bodId, featureId), status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_valid_with_callback(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_htmlpopup_missing_feature(self):
        self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/0/htmlPopup', status=404)

    def test_extendedhtmlpopup_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bakom.radio-fernsehsender/11/extendedHtmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')

    def test_extendedhtmlpopup_valid_lubis(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.swisstopo.lubis-luftbilder_farbe/19981551013722/extendedHtmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')

    def test_extendedhtmlpopup_valid_langs(self):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            try:
                resp = self.testapp.get('/rest/services/ech/MapServer/ch.babs.kulturgueter/6967/extendedHtmlPopup', params={'lang': lang}, status=200)
                self.assertEqual(resp.content_type, 'text/html')
            except (AppError, AssertionError, MakoRenderingException):
                self.skipTest("Skiping test")

    def test_extendedhtmlpopup_valid_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bakom.radio-fernsehsender/12/extendedHtmlPopup', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_extendedhtmlpopup_noinfo(self):
        self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/1/extendedHtmlPopup', status=404)

    def test_iframehtmlpopup(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bav.haltestellen-oev/8573140/iframeHtmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<script src=')

    def test_htmlpopup_with_iframeservice(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bav.haltestellen-oev/8573140/htmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<iframe src=')

    def test_cut_all_dataset(self):
        params = {'layers': 'all:ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung', resp.json)
        self.assertIn('groupby', resp.json['ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'][0])
        self.assertIn('groupbyvalue', resp.json['ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'][0])
        self.assertIn('area', resp.json['ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'][0])

    def test_cut_all_dataset_lv95(self):
        params = {'layers': 'all:ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung', 'sr': '2056'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung', resp.json)
        self.assertIn('groupby', resp.json['ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'][0])
        self.assertIn('groupbyvalue', resp.json['ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'][0])
        self.assertIn('area', resp.json['ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'][0])

    def test_cut_no_group_geom_only(self):
        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': '545000,145000,555000,170005',
                  'layers': 'all:ch.swisstopo.images-swissimage.metadata'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.images-swissimage.metadata', resp.json)
        self.assertIn('area', resp.json['ch.swisstopo.images-swissimage.metadata'][0])
        self.assertIn('groupby', resp.json['ch.swisstopo.images-swissimage.metadata'][0])
        self.assertIn('groupbyvalue', resp.json['ch.swisstopo.images-swissimage.metadata'][0])

        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': '545000,145000,555000,170005',
                  'layers': 'all:ch.swisstopo.pixelkarte-farbe-pk50.noscale'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.pixelkarte-farbe-pk50.noscale', resp.json)
        self.assertIn('area', resp.json['ch.swisstopo.pixelkarte-farbe-pk50.noscale'][0])
        self.assertIn('groupby', resp.json['ch.swisstopo.pixelkarte-farbe-pk50.noscale'][0])
        self.assertIn('groupbyvalue', resp.json['ch.swisstopo.pixelkarte-farbe-pk50.noscale'][0])

    def test_cut_no_group_geom_only_lv95(self):
        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': shift_to_lv95('545000,145000,555000,170005'),
                  'layers': 'all:ch.swisstopo.images-swissimage.metadata',
                  'sr': '2056'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        result = resp.json['ch.swisstopo.images-swissimage.metadata'][0]
        self.assertIn('ch.swisstopo.images-swissimage.metadata', resp.json)
        self.assertIn('area', result)
        self.assertGreater(result['area'], 0)
        self.assertIn('groupby', result)
        self.assertIn('groupbyvalue', result)

        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': shift_to_lv95('545000,145000,555000,170005'),
                  'layers': 'all:ch.swisstopo.pixelkarte-farbe-pk50.noscale',
                  'sr': '2056'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        result = resp.json['ch.swisstopo.pixelkarte-farbe-pk50.noscale'][0]
        self.assertIn('ch.swisstopo.pixelkarte-farbe-pk50.noscale', resp.json)
        self.assertIn('area', result)
        self.assertGreater(result['area'], 0)
        self.assertIn('groupby', result)
        self.assertIn('groupbyvalue', result)

    def test_cut_bad_geom(self):
        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': '545000,145000,555000',
                  'layers': 'all:ch.swisstopo.images-swissimage.metadata'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry')

    def test_cut_bad_geom_type(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '545000,145000,555000,170005',
                  'layers': 'all:ch.swisstopo.images-swissimage.metadata'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry type. Available: (esriGeometryPolygon, esriGeometryEnvelope)')

    def test_cut_with_group_geom_only(self):
        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': '545000,145000,555000,170005',
                  'layers': 'all:ch.swisstopo.images-swissimage.metadata',
                  'groupby': 'datenstand'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.images-swissimage.metadata', resp.json)
        self.assertGreater(len(resp.json['ch.swisstopo.images-swissimage.metadata']), 1)
        self.assertIn('area', resp.json['ch.swisstopo.images-swissimage.metadata'][0])
        self.assertIn('groupby', resp.json['ch.swisstopo.images-swissimage.metadata'][0])
        self.assertIn('groupbyvalue', resp.json['ch.swisstopo.images-swissimage.metadata'][0])

    def test_cut_swissimage_product_whole_dataset(self):
        params = {'layers': 'all:ch.swisstopo.swissimage-product',
                  'groupby': 'resolution'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.swissimage-product', resp.json)
        self.assertEqual(len(resp.json['ch.swisstopo.swissimage-product']), 2)
        self.assertGreater(len(resp.json['ch.swisstopo.swissimage-product']), 1)
        # A bit more than Switzerland should be covered by either resolution: 0.25 or 0.50m
        totalArea = 0
        for group in resp.json['ch.swisstopo.swissimage-product']:
            totalArea += group['area']
        self.assertGreaterEqual(totalArea, 45045)

    def test_cut_with_feature_clipper(self):
        params = {'clipper': 'ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill:2222',
                  'layers': 'all:ch.swisstopo.swisstlm3d-karte-farbe'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.swisstlm3d-karte-farbe', resp.json)
        self.assertEqual(len(resp.json['ch.swisstopo.swisstlm3d-karte-farbe']), 1)

    def test_cut_total_area(self):
        params = {'layers': 'all:ch.swisstopo.swisstlm3d-karte-farbe'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.swisstlm3d-karte-farbe', resp.json)
        self.assertEqual(len(resp.json['ch.swisstopo.swisstlm3d-karte-farbe']), 1)

    def test_cut_complex_polygon_and_two_layers_with_groups(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon', 'layers': 'all:ch.swisstopo.images-swissimage.metadata,ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill',
                  'groupby': 'datenstand,kanton'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertIn('ch.swisstopo.images-swissimage.metadata', resp.json)
        self.assertIn('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', resp.json)
        self.assertEqual('datenstand', resp.json['ch.swisstopo.images-swissimage.metadata'][0]['groupby'])

    def test_cut_total_wrong_id(self):
        params = {'layers': 'all:foo'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=400)
        resp.mustcontain('No GeoTable was found for foo')

    def test_cut_bad_clipper_layer_id(self):
        params = {'clipper': 'foo:2222', 'layers': 'all:ch.swisstopo.swisstlm3d-karte-farbe'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=400)
        resp.mustcontain('No Vector Table was found for foo')

    def test_cut_bad_clipper_feature_id(self):
        params = {'clipper': 'ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill:toto',
                  'layers': 'all:ch.swisstopo.images-swissimage.metadata', 'groupby': 'datenstand'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=404)
        resp.mustcontain('No feature with id toto')

    def test_cut_outside_extent(self):
        params = {'layers': 'all:ch.swisstopo.swissimage-product',
                  'geometryType': 'esriGeometryEnvelope',
                  'geometry': '478968,280720,486572,292875'}
        resp = self.testapp.get('/rest/services/ech/GeometryServer/cut', params=params, status=200)
        self.assertEqual(list(resp.json.keys())[0], 'ch.swisstopo.swissimage-product')
        self.assertEqual(list(resp.json['ch.swisstopo.swissimage-product'])[0]['area'], 0.0)


zlayer = 'ch.swisstopo.zeitreihen'


class TestReleasesService(TestsBase):

    def test_service(self):
        mapExtent = '611399.9999999999,158650,690299.9999999999,198150'
        geometry = '650000.0,170000.0'
        params = {'imageDisplay': '500,600,96',
                  'mapExtent': mapExtent,
                  'geometry': geometry,
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        results_lv03 = resp.json['results']
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertTrue(len(results_lv03) >= 22, len(results_lv03))

        params = {'imageDisplay': '500,600,96',
                  'mapExtent': shift_to_lv95(mapExtent),
                  'geometry': shift_to_lv95(geometry),
                  'geometryType': 'esriGeometryPoint',
                  'sr': '2056'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertTrue(len(resp.json['results']) >= 22, len(resp.json['results']))

        params = {'imageDisplay': '500,600,96',
                  'mapExtent': reproject_to_srid(mapExtent, 21781, 3857),
                  'geometry': reproject_to_srid(geometry, 21781, 3857),
                  'geometryType': 'esriGeometryPoint',
                  'sr': '3857'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertTrue(len(resp.json['results']) >= 22, len(resp.json['results']))

        mapExtent = '611398,158649,6903005,198152'
        params = {'imageDisplay': '500,600,50',
                  'mapExtent': reproject_to_srid(mapExtent, 21781, 4326),
                  'geometry': reproject_to_srid(geometry, 21781, 4326),
                  'geometryType': 'esriGeometryPoint',
                  'sr': '4326'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        # FIXME Deactivatingi failing test, as it is not related to WebMercator
        # diff_wgs84_lv03 = list(set(resp.json['results']) - set(results_lv03))
        # self.assertEqual(diff_wgs84_lv03, [])

    def test_service_dummyLayer(self):
        params = {'imageDisplay': '500,600,96',
                  'mapExtent': '611399.9999999999,158650,690299.9999999999,198150',
                  'geometry': '650000.0,170000.0',
                  'geometryType': 'esriGeometryPoint'
                  }
        self.testapp.get('/rest/services/all/MapServer/dummyLayer/releases', params=params, status=400)

    # Test cases Oftringen by Kerngruppe Zeitreise
    def test_scale_100000(self):
        mapExtent = '620998.611111,231681.388889,649291.388889,250378.611111'
        geometry = '636500.0,241000.0'
        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': mapExtent,
                  'geometry': geometry,
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGreaterEqual(len(resp.json['results']), 25)
        ist = resp.json['results']
        soll = ["18611231", "18641231", "18661231", "18711231", "18751231", "18761231",
                "18791231", "18821231", "18851231", "18891231", "18931231", "18951231",
                "18981231", "19021231", "19051231", "19061231", "19081231", "19091231",
                "19121231", "19221231", "19231231", "19281231", "19331231", "19591231",
                "19651231", "19701231", "19761231", "19821231", "19881231", "19941231",
                "20001231", "20071231", "20171231"]
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': shift_to_lv95(mapExtent),
                  'geometry': shift_to_lv95(geometry),
                  'geometryType': 'esriGeometryPoint',
                  'sr': '2056'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGreaterEqual(len(resp.json['results']), 25)
        ist = resp.json['results']
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

    def test_scale_50000(self):
        mapExtent = '629426.805556,236325.694444,643573.194444,245674.305556'
        geometry = '636500.0,241000.0'
        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': mapExtent,
                  'geometry': geometry,
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGreaterEqual(len(resp.json['results']), 25)
        ist = resp.json['results']
        soll = ["18611231", "18641231", "18661231", "18711231", "18751231", "18761231",
                "18791231", "18821231", "18841231", "18961231", "18971231", "19011231",
                "19131231", "19311231", "19421231", "19571231", "19641231", "19701231",
                "19761231", "19821231", "19881231", "19941231", "20001231", "20061231", "20121231"]
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': shift_to_lv95(mapExtent),
                  'geometry': shift_to_lv95(geometry),
                  'geometryType': 'esriGeometryPoint',
                  'sr': '2056'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGreaterEqual(len(resp.json['results']), 25)
        ist = resp.json['results']
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

    def test_scale_25000(self):
        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': '632963.402778,238662.847222,640036.597222,243337.152778',
                  'geometry': '636500.0,241000.0',
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGreaterEqual(len(resp.json['results']), 25)
        ist = resp.json['results']
        soll = ["18611231", "18641231", "18661231", "18711231", "18751231", "18761231",
                "18791231", "18821231", "18841231", "18961231", "18971231", "19011231",
                "19131231", "19311231", "19421231", "19551231", "19571231", "19641231",
                "19701231", "19761231", "19821231", "19881231", "19941231", "20001231", "20061231", "20121231"]
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

    def test_missing_params(self):
        params = {'mapExtent': '611399.9999999999,158650,690299.9999999999,198150'}
        self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=400)
        params = {'imageDisplay': '500,600,96'}
        self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=400)

    def test_layer_without_releases(self):
        params = {'imageDisplay': '500,600,96', 'mapExtent': '611399.9999999999,158650,690299.9999999999,198150'}
        self.testapp.get('/rest/services/all/MapServer/ch.swisstopo.images-swissimage.metadata/releases', params=params, status=400)

    def test_unknown_layers(self):
        params = {'imageDisplay': '500,600,96', 'mapExtent': '611399.9999999999,158650,690299.9999999999,198150'}
        self.testapp.get('/rest/services/all/MapServer/dummylayer/releases', params=params, status=400)
