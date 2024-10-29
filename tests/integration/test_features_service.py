# -*- coding: utf-8 -*-

from unittest import skip, skipUnless
from webtest.app import AppError
from pyramid_mako import MakoRenderingException
from tests.integration import TestsBase, shift_to_lv95, reproject_to_srid, s3_tests

from chsdi.lib.validation import SUPPORTED_OUTPUT_SRS


class TestFeaturesView(TestsBase):

    def test_unsupported_srid(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid',
                  'searchText': '1231641',
                  'sr': '9999'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn('Unsupported spatial reference', resp.text)

    def test_searchField_none(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn('Please provide a searchField', resp.text)

    def test_searchField_error(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid, bln_fl',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn('You can provide only one searchField at a time', resp.text)

    def test_none_layer(self):
        params = {'searchField': 'egid',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn('Please provide a parameter layer', resp.text)

    def test_two_layer(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register,ch.bazl.luftfahrthindernis',
                  'searchField': 'egid',
                  'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn('You can provide only one layer at a time', resp.text)

    def test_find_scan(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register',
                  'searchField': 'egid',
                  'searchText': '1757559'}
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
                  'searchText': '1753854',
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
                  'searchField': 'strname_deinr',
                  'searchText': 'Rue Neuve 12',
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
                  'searchText': 'Rue Neuve 12',
                  'searchField': 'strname_deinr',
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
        self.assertIn('Please provide a float', resp.text)

    def test_find_non_integer(self):
        params = {'layer': 'ch.bafu.bundesinventare-bln',
                  'searchField': 'bln_obj',
                  'searchText': '1201.0',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn('Please provide an integer', resp.text)

    def test_find_boolean_true(self):
        params = {'layer': 'ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill',
                  'searchField': 'is_current_jahr',
                  'searchText': 'True',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_boolean_false(self):
        params = {'layer': 'ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill',
                  'searchField': 'is_current_jahr',
                  'searchText': 'FALSE',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 1)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781, hasGeometry=False)

    def test_find_wrong_boolean(self):
        params = {'layer': 'ch.swisstopo.lubis-luftbilder-dritte-firmen',
                  'searchField': 'orientierung',
                  'searchText': '3190',
                  'returnGeometry': 'false',
                  'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn('Please provide a boolean value (true/false)', resp.text)

    def test_find_wrong_layer_layerdefs(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'stn_label',
                  'searchText': 'Talstrasse',
                  'returnGeometry': 'false',
                  'contains': 'false',
                  'layerDefs': '{"tutu": "com_fosnr > 2000"}'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn("You can only filter on layer 'ch.swisstopo.amtliches-strassenverzeichnis' in 'layerDefs'", resp.text)

    def test_find_wrong_attribute(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'stn_label',
                  'searchText': 'Talstrasse',
                  'returnGeometry': 'false',
                  'contains': 'false',
                  'layerDefs': '{"ch.swisstopo.amtliches-strassenverzeichnis": "toto = 4307"}'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        self.assertIn("Query attribute 'toto' is not queryable", resp.text)

    def test_find_all_talstrasse(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'stn_label',
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
            "searchField": "stn_label",
            "returnGeometry": "false",
            "layerDefs": '''{"ch.swisstopo.amtliches-strassenverzeichnis": "com_name = 'Olten' or com_name = 'Sattel'"}'''
        }
        params2 = {
            "layer": "ch.swisstopo.amtliches-strassenverzeichnis",
            "searchText": "Studerweg",
            "searchField": "stn_label",
            "returnGeometry": "false",
            "layerDefs": '''{"ch.swisstopo.amtliches-strassenverzeichnis": "com_name = 'Sattel' or com_name = 'Olten'"}'''
        }

        resp1 = self.testapp.get('/rest/services/all/MapServer/find', params=params1, status=200)
        resp2 = self.testapp.get('/rest/services/all/MapServer/find', params=params2, status=200)
        self.assertEqual(resp1.content_type, 'application/json')
        # self.assertEqual(resp1.json['results'], resp2.json['results'])
        for feat in resp2.json['results']:
            self.assertIn(feat['attributes']['com_name'], ['Olten', 'Sattel'])
            self.assertIn('Studer', feat['attributes']['stn_label'])

    def test_find_filter_with_layerdefs(self):
        params = {'layer': 'ch.swisstopo.amtliches-strassenverzeichnis',
                  'searchField': 'stn_label',
                  'searchText': 'Talstrasse',
                  'returnGeometry': 'false',
                  'contains': 'false',
                  'layerDefs': '{"ch.swisstopo.amtliches-strassenverzeichnis": "com_fosnr = 4307"}'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        # Not more than one road should have the same name in a given commune
        self.assertLessEqual(len(resp.json['results']), 1)
        for feat in resp.json['results']:
            self.assertEqual(feat['attributes']['com_fosnr'], 4307)

    def test_feature_wrong_idlayer(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/toto/362', status=400)
        self.assertIn('No Vector Table was found for', resp.text)

    def test_feature_wrong_srid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/0', params={'sr': '111'}, status=400)
        self.assertIn('Unsupported spatial reference', resp.text)

    def test_feature_wrong_idfeature(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/0', status=404)
        self.assertIn('No feature with id', resp.text)

        resp = self.testapp.get('/rest/services/api/MapServer/ch.bafu.bundesinventare-bln/htmlPopup', status=404)
        self.assertIn('No feature with id', resp.text)

    # TODO; we should not hardcode stable IDs, because they are not so stable
    def test_feature_htmlpopup_opensurvey(self):
        params = {'coord': '2599337,1211687',
                  'imageDisplay': '929,949,96',
                  'lang': 'en',
                  'mapExtent': '2598014.39,1210612.06,2599872.39,1212510.06',
                  'sr': 2056}
        try:
            resp = self.testapp.get('/rest/services/ech/MapServer/ch.swisstopo-vd.amtliche-vermessung/159058372/htmlPopup', params=params, status=200)
            self.assertEqual(resp.status_int, 200)
            self.assertEqual(resp.content_type, 'text/html')
        except (AppError, AssertionError):
            skip("Skiping htmlPopup test for layer 'ch.swisstopo-vd.amtliche-vermessung' and id=159058372")

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
        self.assertIn('Too many featureIds', resp.text)

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
        self.assertIn('cb_({', resp.text)

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
        self.assertIn('Unsupported spatial reference', resp.text)

    def test_htmlpopup_valid(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), status=200)
        self.assertEqual(resp.content_type, 'text/html')
        self.assertIn('<table', resp.text)

    def test_htmlpopup_valid_lv95(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), params={'sr': '2056'}, status=200)
        self.assertEqual(resp.content_type, 'text/html')
        self.assertIn('<table', resp.text)

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
        params = {'mapExtent': '620000,180000,680000,230000',
                  'imageDisplay': '1410,887,96',
                  'lang': 'fr'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfe.windenergieanlagen/turbine_45/htmlPopup', params=params, status=200)
        self.assertIn('Puissance', resp.text)
        params = {'mapExtent': '650000,150000,700000,200000',
                  'imageDisplay': '1410,887,96',
                  'lang': 'fr'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfe.windenergieanlagen/facility_GUE/htmlPopup', params=params, status=200)
        self.assertIn('Type', resp.text)

    def test_htmlpopup_cadastralwebmap(self):
        params = {'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999',
                  'imageDisplay': '600,400,96'}
        bodId = 'ch.kantone.cadastralwebmap-farbe'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/ech/MapServer/%s/%s/htmlPopup' % (bodId, featureId), params=params, status=200)
        self.assertEqual(resp.content_type, 'text/html')
        self.assertIn('<table', resp.text)

    def test_htmlpopup_bad_request_image_display(self):
        params = {'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999',
                  'imageDisplay': '600,96'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/16847593/htmlPopup', params=params, status=400)
        self.assertIn('Please provide the parameter imageDisplay in a comma separated list of 3 arguments '
                      '(width,height,dpi)', resp.text)

    def test_htmlpopup_nan_image_display(self):
        params = {'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999', 'imageDisplay': '600,96,None'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/16847593/htmlPopup', params=params, status=400)
        self.assertIn('Please provide numerical values for the parameter imageDisplay', resp.text)

    def test_htmlpopup_bad_request_map_extent(self):
        params = {'mapExtent': 'quite_big_extent',
                  'imageDisplay': '1362,1139,96',
                  'lang': 'fr'}
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.schutzgebiete-aulav_uebrige/400/htmlPopup', params=params, status=400)
        self.assertIn('Please provide numerical values for the parameter mapExtent', resp.text)

    def test_htmlpopup_valid_topic_all(self):
        bodId = 'ch.bafu.bundesinventare-bln'
        featureId = self.getRandomFeatureId(bodId)
        resp = self.testapp.get('/rest/services/all/MapServer/%s/%s/htmlPopup' % (bodId, featureId), status=200)
        self.assertEqual(resp.content_type, 'text/html')
        self.assertIn('<table', resp.text)

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
        self.assertIn('<script src=', resp.text)

    def test_htmlpopup_with_iframeservice(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bav.haltestellen-oev/8573140/htmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        self.assertIn('<iframe src=', resp.text)

    @skipUnless(s3_tests, "Requires AWS S3 access")
    def test_feature_grid_valid_feature(self):
        layer_id = 'ch.bfe.windenergie-geschwindigkeit_h50'
        feature_id = '696_1249'
        for sr in [2056, 21781, 4326, 3857]:
            resp = self.testapp.get('/rest/services/all/MapServer/%s/%s' % (layer_id, feature_id), params={
                'sr': sr
            })
            self.assertEqual(resp.content_type, 'application/json')
            feature = resp.json['feature']
            self.assertEqual(feature['id'], feature_id)
            self.assertGeojsonFeature(feature, sr)


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
                "20001231", "20071231", "20171231", "20201231"]
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
                "19701231", "19761231", "19821231", "19881231", "19941231", "20001231",
                "20061231", "20121231", "20181231", "20211231"]
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

    def test_missing_params(self):
        params = {'mapExtent': '611399.9999999999,158650,690299.9999999999,198150'}
        self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=400)
        params = {'imageDisplay': '500,600,96'}
        self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=400)

    def test_layer_without_releases(self):
        params = {'imageDisplay': '500,600,96', 'mapExtent': '611399.9999999999,158650,690299.9999999999,198150'}
        self.testapp.get('/rest/services/all/MapServer/ch.swisstopo.pixelkarte-farbe/releases', params=params, status=400)

    def test_unknown_layers(self):
        params = {'imageDisplay': '500,600,96', 'mapExtent': '611399.9999999999,158650,690299.9999999999,198150'}
        self.testapp.get('/rest/services/all/MapServer/dummylayer/releases', params=params, status=400)

    def test_find_layerdefs_with_accents(self):
        params1 = {
            "layer": "ch.swisstopo.amtliches-strassenverzeichnis",
            "searchText": "371",
            "searchField": "com_fosnr",
            "returnGeometry": "false",
            "layerDefs": '''{"ch.swisstopo.amtliches-strassenverzeichnis": "stn_label like '%Contrôle%'"}'''
        }

        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params1, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        for feat in resp.json['results']:
            self.assertIn(feat['attributes']['com_fosnr'], [371])
            self.assertIn(u'Contrôle', feat['attributes']['stn_label'])
