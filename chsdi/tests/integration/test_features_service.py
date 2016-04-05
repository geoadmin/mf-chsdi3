# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


def getLayers(query):
    for q in query:
        yield q[0]


class TestFeaturesView(TestsBase):

    def test_searchField_none(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Please provide a searchField')

    def test_searchField_error(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid, bln_fl', 'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('You can provide only one searchField at a time')

    def test_none_layer(self):
        params = {'searchField': 'egid', 'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('Please provide a parameter layer')

    def test_two_layer(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register,ch.bazl.luftfahrthindernis', 'searchField': 'egid', 'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)
        resp.mustcontain('You can provide only one layer at a time')

    def test_find_scan(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json['results']), 1)

    def test_find_exact_int(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231625', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json['results']), 1)

    def test_find_exact_float(self):
        params = {'layer': 'ch.bafu.bundesinventare-bln', 'searchField': 'bln_fl', 'searchText': '729.092', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json['results']), 1)

    def test_find_exact_text(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'strname1', 'searchText': 'Beaulieustrasse', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) > 1)

    def test_find_exact_date(self):
        params = {'layer': 'ch.bazl.luftfahrthindernis', 'searchField': 'startofconstruction', 'searchText': '1950-01-01', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) > 1)

    def test_find_geojson(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231641', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_find_withcb(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231641', 'callback': 'cb'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'text/javascript')

    def test_find_nogeom(self):
        params = {'layer': 'ch.are.bauzonen', 'searchField': 'bfs_no', 'searchText': '4262', 'returnGeometry': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_find_wrong_searchfield(self):
        params = {'layer': 'ch.are.bauzonen', 'searchField': 'toto', 'searchText': '4262', 'returnGeometry': 'false'}
        self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)

    def test_find_nosearchtext(self):
        params = {'layer': 'ch.are.bauzonen', 'searchField': 'toto', 'returnGeometry': 'false'}
        self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)

    def test_find_wrong_layer(self):
        params = {'layer': 'dummy', 'searchField': 'gdename', 'returnGeometry': 'false'}
        self.testapp.get('/rest/services/all/MapServer/find', params=params, status=400)

    def test_find_contains(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': 'Islastrasse', 'searchField': 'strname1', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) > 1)

    def test_feature_wrong_idlayer(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/toto/362', status=400)
        resp.mustcontain('No Vector Table was found for')

    def test_feature_wrong_idfeature(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/0', status=404)
        resp.mustcontain('No feature with id')

        resp = self.testapp.get('/rest/services/api/MapServer/ch.bafu.bundesinventare-bln/htmlPopup', status=404)
        resp.mustcontain('No feature with id')

    def test_feature_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('attributes', resp.json['feature'])
        self.assertIn('geometry', resp.json['feature'])
        self.assertEqual(resp.json['feature']['id'], 362)

    def test_feature_valid_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.bundesinventare-bln/362', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('attributes', resp.json['feature'])
        self.assertIn('geometry', resp.json['feature'])
        self.assertEqual(resp.json['feature']['id'], 362)

    def test_feature_geojson(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362', params={'geometryFormat': 'geojson'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['feature'])
        self.assertIn('geometry', resp.json['feature'])
        self.assertEqual(resp.json['feature']['id'], 362)

    def test_several_features(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362,363', status=200)
        self.assertEqual(len(resp.json['features']), 2)

    def test_several_features_geojson(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362,363', params={'geometryFormat': 'geojson'}, status=200)
        self.assertEqual(len(resp.json['features']), 2)

    def test_feature_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362', params={'callback': 'cb'}, status=200)
        self.assertEqual(resp.content_type, 'text/javascript')
        resp.mustcontain('cb({')

    def test_feature_big_but_good(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.swisstopo.geologie-geocover/1080284', params={'geometryFormat': 'geojson'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('geometry', resp.json['feature'])

    def test_htmlpopup_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_cadastralwebmap(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/14/htmlPopup', params={'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999', 'imageDisplay': '600,400,96'}, status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_valid_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_valid_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup', params={'callback': 'cb'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_htmlpopup_missing_feature(self):
        self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/1/htmlPopup', status=404)

    def test_htmlpopup_scale_dependent(self):
        params = {'mapExtent': '559349.7,127280.7,695549.7,241180.7', 'imageDisplay': '1362,1139,96', 'lang': 'fr'}
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.schutzgebiete-aulav_uebrige/400/htmlPopup', params=params, status=200)
        resp.mustcontain('Les atterrissages en campagne')
        params = {'mapExtent': '654998,188636.6,657722,190914.6', 'imageDisplay': '1362,1139,96', 'lang': 'fr'}
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.schutzgebiete-aulav_uebrige/400/htmlPopup', params=params, status=200)
        resp.mustcontain('Haut-marais')

    def test_extendedhtmlpopup_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bakom.radio-fernsehsender/11/extendedHtmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')

    def test_extendedhtmlpopup_valid_lubis(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.swisstopo.lubis-luftbilder_farbe/19981551013722/extendedHtmlPopup', status=200)
        self.assertEqual(resp.content_type, 'text/html')

    def test_extendedhtmlpopup_valid_langs(self):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            resp = self.testapp.get('/rest/services/ech/MapServer/ch.babs.kulturgueter/6967/extendedHtmlPopup', params={'lang': lang}, status=200)
            self.assertEqual(resp.content_type, 'text/html')

    def test_extendedhtmlpopup_valid_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bakom.radio-fernsehsender/12/extendedHtmlPopup', params={'callback': 'cb'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_extendedhtmlpopup_noinfo(self):
        self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362/extendedHtmlPopup', status=404)


class TestGebauedeGeometry(TestsBase):

    def test_feature_not_authorized(self):
        headers = {'X-SearchServer-Authorized': 'false'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/490830_0', headers=headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertNotIn('geometry', resp.json['feature'])

    def test_feature_authorized(self):
        headers = {'X-SearchServer-Authorized': 'true'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/490830_0', headers=headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('geometry', resp.json['feature'])

    def test_find_not_authorized(self):
        headers = {'X-SearchServer-Authorized': 'false'}
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': 'berges', 'searchField': 'strname1'}
        resp = self.testapp.get('/rest/services/ech/MapServer/find', params=params, headers=headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertNotIn('geometry', resp.json['results'][0])

    def test_find_authorized(self):
        headers = {'X-SearchServer-Authorized': 'true'}
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': 'berges', 'searchField': 'strname1'}
        resp = self.testapp.get('/rest/services/ech/MapServer/find', params=params, headers=headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_not_authorized(self):
        headers = {'X-SearchServer-Authorized': 'false'}
        params = {'geometry': '653199.9999999999,137409.99999999997', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,623,96', 'layers': 'all:ch.bfs.gebaeude_wohnungs_register', 'mapExtent': '633200,132729.99999999997,671600,145189.99999999997',
                  'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertNotIn('geometry', resp.json['results'][0])

    def test_identify_authorized(self):
        headers = {'X-SearchServer-Authorized': 'true'}
        params = {'geometry': '653199.9999999999,137409.99999999997', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,623,96', 'layers': 'all:ch.bfs.gebaeude_wohnungs_register', 'mapExtent': '633200,132729.99999999997,671600,145189.99999999997',
                  'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertIn('geometry', resp.json['results'][0])

zlayer = 'ch.swisstopo.zeitreihen'


class TestReleasesService(TestsBase):

    def test_service(self):
        params = {'imageDisplay': '500,600,96',
                  'mapExtent': '611399.9999999999,158650,690299.9999999999,198150',
                  'geometry': '650000.0,170000.0',
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 22, len(resp.json['results']))

    # Test cases Oftringen by Kerngruppe Zeitreise
    def test_scale_100000(self):
        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': '620998.611111,231681.388889,649291.388889,250378.611111',
                  'geometry': '636500.0,241000.0',
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 25, len(resp.json['results']))
        ist = resp.json['results']
        soll = ["18611231", "18641231", "18661231", "18711231", "18751231", "18761231", "18791231", "18821231", "18851231", "18891231", "18931231", "18951231", "18981231", "19021231", "19051231", "19061231", "19081231", "19091231", "19121231", "19221231", "19231231", "19281231", "19331231", "19591231", "19651231", "19701231", "19761231", "19821231", "19881231", "19941231", "20001231", "20071231"]
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

    def test_scale_50000(self):
        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': '629426.805556,236325.694444,643573.194444,245674.305556',
                  'geometry': '636500.0,241000.0',
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 25, len(resp.json['results']))
        ist = resp.json['results']
        soll = ["18611231", "18641231", "18661231", "18711231", "18751231", "18761231", "18791231", "18821231", "18841231", "18961231", "18971231", "19011231", "19131231", "19311231", "19421231", "19571231", "19641231", "19701231", "19761231", "19821231", "19881231", "19941231", "20001231", "20061231", "20121231"]
        for idx, i in enumerate(ist):
            self.assertEqual(i, soll[idx], str(idx))

    def test_scale_25000(self):
        params = {'imageDisplay': '2851,1884,256.0',
                  'mapExtent': '632963.402778,238662.847222,640036.597222,243337.152778',
                  'geometry': '636500.0,241000.0',
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 25, len(resp.json['results']))
        ist = resp.json['results']
        soll = ["18611231", "18641231", "18661231", "18711231", "18751231", "18761231", "18791231", "18821231", "18841231", "18961231", "18971231", "19011231", "19131231", "19311231", "19421231", "19551231", "19571231", "19641231", "19701231", "19761231", "19821231", "19881231", "19941231", "20001231", "20061231", "20121231"]
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
