# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


def getLayers(query):
    for q in query:
        yield q[0]


class TestMapServiceView(TestsBase):

    def test_metadata_no_parameters(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_metadata_no_parameters_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer', status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_metadata_with_searchtext(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'searchText': 'wasser'}, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_metadata_with_callback(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')

    def test_metadata_chargeable_true(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'chargeable': 'true'}, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_metadata_chargeable_false(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'chargeable': 'false'}, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_no_parameters(self):
        self.testapp.get('/rest/services/ech/MapServer/identify', status=400)

    def test_identify_without_geometry(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter geometry')

    def test_identify_without_geometrytype(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter geometryType')

    def test_identify_without_imagedisplay(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter imageDisplay')

    def test_identify_without_mapextent(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('')

    def test_identify_without_tolerance(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter tolerance')

    def test_identify_polyline(self):
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}', 'geometryType': 'esriGeometryPolyline', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_polygon(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}', 'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_zero_tolerance_and_scale(self):
        params = {'geometry': '681999,251083,682146,251190', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '1920,452,96', 'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft',
                  'mapExtent': '679364.12,250588.34,684164.12,251718.34', 'tolerance': '0'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(len(resp.json['results']) == 1)

    def test_identify_valid(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_valid_topic_all(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_valid_with_callback(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all',
                  'callback': 'cb'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'text/javascript')
        resp.mustcontain('cb({')

    def test_identify_with_geojson(self):
        params = {'geometry': '600000,200000,631000,210000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1',
                  'layers': 'all:ch.bafu.bundesinventare-bln', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('properties' in resp.json['results'][0])
        self.failUnless('geometry' in resp.json['results'][0])

    def test_identify_with_geojson_returned_geometry(self):
        params = {'geometry': '600000,200000,631000,210000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1',
                  'layers': 'all:ch.swisstopo.lubis-luftbilder_farbe', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(resp.json['results'][0]['geometry']['type'] in ['Polygon', 'GeometryCollection'])

    def test_identify_gen50_geom(self):
        params = {'geometryType': 'esriGeometryPoint', 'returnGeometry': 'false', 'layers': 'all:ch.swisstopo-vd.geometa-gemeinde', 'geometry': '561289,185240', 'mapExtent': '561156.75,185155,561421.25,185325',
                  'imageDisplay': '529,340,96', 'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.failUnless(len(resp.json['results']) != 0)

    def test_identify_no_geom(self):
        params = {'geometry': '630000,245000,645000,265000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '545132,147068,550132,150568', 'tolerance': '1', 'layers': 'all',
                  'returnGeometry': 'false'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(('geometry' not in resp.json['results'][0]))
        self.failUnless(('geometryType' not in resp.json['results'][0]))

    def test_identify_faulty_params(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'geometry': '-Infinity,-Infinity,Infinity,Infinity', 'imageDisplay': '0,0,0', 'mapExtent': '0,0,0,0', 'tolerance': 0, 'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo.swissboundaries3d-land-flaeche.fill', 'returnGeometry': 'false', 'lang': 'fr'}

        self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)

    def test_identify_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson', 'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5', 'layers': 'all:ch.swisstopo.zeitreihen', 'timeInstant': '1936'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_wrong_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson', 'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997', 'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen', 'timeInstant': '19366'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_timeinstant_nottimeenabled_layer(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson', 'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997', 'tolerance': '5',
                  'layers': 'all:ch.bafu.bundesinventare-bln', 'timeInstant': '1936'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)

    def test_identify_oereb(self):
        params = {'geometry': '618953,170093', 'geometryType': 'esriGeometryPoint', 'imageDisplay': '1920,576,96', 'layers': 'all:ch.bav.kataster-belasteter-standorte-oev.oereb',
                  'mapExtent': '671164.31244,253770,690364.31244,259530', 'tolerance': '5', 'geometryFormat': 'interlis'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'text/xml')

    def test_identify_oereb_several_layers(self):
        params = {'geometry': '618953,170093', 'geometryType': 'esriGeometryPoint', 'imageDisplay': '1920,576,96', 'layers': 'all:ch.bav.kataster-belasteter-standorte-oev.oereb,ch.bazl.sicherheitszonenplan.oereb',
                  'mapExtent': '671164.31244,253770,690364.31244,259530', 'tolerance': '5', 'geometryFormat': 'interlis'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_query_time(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'abortionaccomplished > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_query_number(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'maxheightagl > 210'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_query_text(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_query_and_bbox(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'geometry': '502722,36344,745822,253444', 'imageDisplay': '0,0,0', 'mapExtent': '0,0,0,0', 'tolerance': '0',
                  'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'obstacletype = \'Antenna\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_query_escape_quote(self):
        params = {'geometryFormat': 'geojson', 'lang': 'en', 'layers': 'all:ch.bafu.hydrologie-wassertemperaturmessstationen', 'time': '2013', 'where': 'name ilike \'%Broye-Payerne, Caserne d\'aviation%\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_identify_query_offset(self):
        params = {'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', 'returnGeometry': 'false', 'timeInstant': '2015', 'where': 'gemname ilike \'%a%\''}
        resp1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        params.update({'offset': '2'})
        resp2 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp1.json['results'][2]['featureId'] == resp2.json['results'][0]['featureId'])
        self.failUnless(resp1.json['results'][5]['featureId'] == resp2.json['results'][3]['featureId'])
        params.update({'offset': '5'})
        resp3 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp2.json['results'][3]['featureId'] == resp3.json['results'][0]['featureId'])
        self.failUnless(resp1.json['results'][5]['featureId'] == resp3.json['results'][0]['featureId'])

    def test_identify_bbox_offset(self):
        params = {'layers': 'all:ch.bazl.luftfahrthindernis', 'timeInstant': '2015', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryEnvelope', 'geometry': '573788,93220,750288,192720',
                  'imageDisplay': '1920,778,96', 'mapExtent': '107788,-5279,1067788,383720', 'tolerance': '0'}
        resp1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        params.update({'offset': '2'})
        resp2 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp1.json['results'][2]['featureId'] == resp2.json['results'][0]['featureId'])
        self.failUnless(resp1.json['results'][5]['featureId'] == resp2.json['results'][3]['featureId'])
        params.update({'offset': '4'})
        resp3 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.failUnless(resp2.json['results'][2]['featureId'] == resp3.json['results'][0]['featureId'])
        self.failUnless(resp1.json['results'][4]['featureId'] == resp3.json['results'][0]['featureId'])

    def test_identify_query_wrong_offset(self):
        params = {'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', 'timeInstant': '2015', 'where': 'gemname ilike \'%aven%\'', 'offset': '12.1'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('provide an integer')

    def test_find_scan(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231641'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['results']) == 1)

    def test_find_exact_int(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231625', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['results']) == 1)

    def test_find_exact_float(self):
        params = {'layer': 'ch.bafu.bundesinventare-bln', 'searchField': 'bln_fl', 'searchText': '729.092', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['results']) == 1)

    def test_find_exact_text(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'strname1', 'searchText': 'Beaulieustrasse', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['results']) > 1)

    def test_find_exact_date(self):
        params = {'layer': 'ch.bazl.luftfahrthindernis', 'searchField': 'startofconstruction', 'searchText': '1950-01-01', 'returnGeometry': 'false', 'contains': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['results']) > 1)

    def test_find_geojson(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231641', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_find_withcb(self):
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchField': 'egid', 'searchText': '1231641', 'callback': 'cb'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'text/javascript')

    def test_find_nogeom(self):
        params = {'layer': 'ch.are.bauzonen', 'searchField': 'bfs_no', 'searchText': '4262', 'returnGeometry': 'false'}
        resp = self.testapp.get('/rest/services/all/MapServer/find', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')

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
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['results']) > 1)

    def test_feature_wrong_idlayer(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/toto/362', status=400)
        resp.mustcontain('No Vector Table was found for')

    def test_feature_wrong_idfeature(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/0', status=404)
        resp.mustcontain('No feature with id')

    def test_feature_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362', status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('attributes' in resp.json['feature'])
        self.failUnless('geometry' in resp.json['feature'])
        self.failUnless(resp.json['feature']['id'] == 362)

    def test_feature_valid_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.bundesinventare-bln/362', status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('attributes' in resp.json['feature'])
        self.failUnless('geometry' in resp.json['feature'])
        self.failUnless(resp.json['feature']['id'] == 362)

    def test_feature_geojson(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362', params={'geometryFormat': 'geojson'}, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('properties' in resp.json['feature'])
        self.failUnless('geometry' in resp.json['feature'])
        self.failUnless(resp.json['feature']['id'] == 362)

    def test_several_features(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362,363', status=200)
        self.failUnless(len(resp.json['features']) == 2)

    def test_several_features_geojson(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362,363', params={'geometryFormat': 'geojson'}, status=200)
        self.failUnless(len(resp.json['features']) == 2)

    def test_feature_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'text/javascript')
        resp.mustcontain('cb({')

    def test_htmlpopup_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup', status=200)
        self.failUnless(resp.content_type == 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_wrong_syntax(self):
        self.testapp.get('/rest/services/all/MapServer/ch.bafu.bundesinventare-bln/toto', status=400)

    def test_htmlpopup_cadastralwebmap(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/14/htmlPopup', params={'mapExtent': '485412.34375,109644.67,512974.44,135580.01999999999', 'imageDisplay': '600,400,96'}, status=200)
        self.failUnless(resp.content_type == 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_valid_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup', status=200)
        self.failUnless(resp.content_type == 'text/html')
        resp.mustcontain('<table')

    def test_htmlpopup_valid_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')

    def test_htmlpopup_missing_feature(self):
        self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/1/htmlPopup', status=404)

    def test_extendedhtmlpopup_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bakom.radio-fernsehsender/11/extendedHtmlPopup', status=200)
        self.failUnless(resp.content_type == 'text/html')

    def test_extendedhtmlpopup_valid_lubis(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.swisstopo.lubis-luftbilder_farbe/19981551013722/extendedHtmlPopup', status=200)
        self.failUnless(resp.content_type == 'text/html')

    def test_extendedhtmlpopup_valid_langs(self):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            resp = self.testapp.get('/rest/services/ech/MapServer/ch.babs.kulturgueter/6967/extendedHtmlPopup', params={'lang': lang}, status=200)
            self.failUnless(resp.content_type == 'text/html')

    def test_extendedhtmlpopup_valid_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bakom.radio-fernsehsender/12/extendedHtmlPopup', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')

    def test_extendedhtmlpopup_noinfo(self):
        self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/362/extendedHtmlPopup', status=404)

    def test_legend_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/legend', status=200)
        self.failUnless(resp.content_type == 'text/html')
        resp.mustcontain('<div class="legend-header">')

    def test_legend_valid_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/ch.bafu.bundesinventare-bln/legend', status=200)
        self.failUnless(resp.content_type == 'text/html')
        resp.mustcontain('<div class="legend-header">')

    def test_legend_wrong_layer_id(self):
        self.testapp.get('/rest/services/ech/MapServer/dummylayer/legend', status=404)

    def test_legend_valid_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/legend', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')

    def test_all_legends(self):
        from chsdi.models.bod import LayersConfig
        from sqlalchemy import distinct
        from sqlalchemy.orm import scoped_session, sessionmaker
        # Get list of layers to test the legend service
        DBSession = scoped_session(sessionmaker())
        # define the value to avoid pep troubles
        valnone = None
        valtrue = True
        # Get a list of all layers in prod, exclude sub-layers
        query = DBSession.query(distinct(LayersConfig.layerBodId)).filter(LayersConfig.staging == 'prod').filter(LayersConfig.parentLayerId == valnone).filter(LayersConfig.hasLegend == valtrue)

        try:
            for layer in getLayers(query):
                for lang in ('de', 'fr', 'it', 'rm', 'en'):
                    link = '/rest/services/all/MapServer/' + layer + '/legend?callback=cb&lang=' + lang
                    resp = self.testapp.get(link)
                    self.failUnless(resp.status_int == 200, link)
        finally:
            DBSession.close()

    def test_all_legends_images(self):
        import os
        from chsdi.models.bod import LayersConfig
        from sqlalchemy import distinct
        from sqlalchemy.orm import scoped_session, sessionmaker
        # Get list of layers from existing legend images
        legendsPath = os.getcwd() + '/chsdi/static/images/legends/'
        legendNames = os.listdir(legendsPath)
        parseLegendNames = lambda x: x[:-4] if 'big' not in x else x[:-8]
        legendImages = list(set(map(parseLegendNames, legendNames)))
        # Get list of layers that should have image in prod, exclude sublayers
        DBSession = scoped_session(sessionmaker())
        valnone = None
        valtrue = True
        query = DBSession.query(distinct(LayersConfig.layerBodId)).filter(LayersConfig.staging == 'prod').filter(LayersConfig.parentLayerId == valnone).filter(LayersConfig.hasLegend == valtrue)

        try:
            for layer in getLayers(query):
                for lang in ('de', 'fr', 'it', 'rm', 'en'):
                    self.failUnless((layer + '_' + lang) in legendImages, layer + lang)
        finally:
            DBSession.close()

    def test_all_htmlpopups(self):
        from chsdi.models import models_from_name
        from chsdi.models.bod import LayersConfig
        from sqlalchemy import distinct
        from sqlalchemy.orm import scoped_session, sessionmaker
        val = True
        DBSession = scoped_session(sessionmaker())
        valnone = None
        query = DBSession.query(distinct(LayersConfig.layerBodId)).filter(LayersConfig.staging == 'prod').filter(LayersConfig.queryable == val).filter(LayersConfig.parentLayerId == valnone)
        features = []
        try:
            for layer in getLayers(query):
                try:
                    FeatDBSession = scoped_session(sessionmaker())
                    models = models_from_name(layer)
                    self.failUnless(models is not None and len(models) > 0, layer)
                    model = models[0]
                    query = FeatDBSession.query(model.primary_key_column()).limit(1)
                    ID = [q[0] for q in query]
                    if ID:
                        features.append((layer, str(ID[0])))
                finally:
                    FeatDBSession.close()
        finally:
            DBSession.close()

        for f in features:
            for lang in ('de', 'fr', 'it', 'rm', 'en'):
                link = '/rest/services/all/MapServer/' + f[0] + '/' + f[1] + '/htmlPopup?callback=cb&lang=' + lang
                resp = self.testapp.get(link)
                self.failUnless(resp.status_int == 200, link)

    def test_layersconfig_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/layersConfig', status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('ch.swisstopo.pixelkarte-farbe' in resp.json)
        self.failUnless('attribution' in resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.failUnless('label' in resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.failUnless('background' in resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.failUnless('topics' in resp.json['ch.swisstopo.pixelkarte-farbe_wmts'])
        self.failUnless('topics' in resp.json['ch.swisstopo.pixelkarte-farbe'])

    def test_layersconfig_valid_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless('ch.swisstopo.pixelkarte-farbe' in resp.json)
        self.failUnless('attribution' in resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.failUnless('label' in resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.failUnless('background' in resp.json['ch.swisstopo.pixelkarte-farbe'])

    def test_layersconfig_geojson_layer(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.failUnless(resp.content_type == 'application/json')
        jsonData = resp.json
        if 'ch.bafu.hydroweb-messstationen_gefahren' in jsonData:
            layer = jsonData['ch.bafu.hydroweb-messstationen_gefahren']
            self.failUnless(layer['type'] == 'geojson')
            self.failUnless('geojsonUrl' in layer)
            self.failUnless('geojsonUrlDe' not in layer)
            self.failUnless('styleUrl' in layer)
            self.failUnless('updateDelay' in layer)

    def test_layersconfig_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/layersConfig', params={'callback': 'cb'}, status=200)
        self.failUnless(resp.content_type == 'application/javascript')

    def test_layersconfig_wrong_map(self):
        self.testapp.get('/rest/services/foo/MapServer/layersConfig', status=400)

    def test_layer_attributes(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln', status=200)
        self.failUnless(resp.content_type == 'application/json')

    def test_layer_attributes_lang_specific(self):
        lang = 'de'
        path = '/rest/services/all/MapServer/ch.bav.sachplan-infrastruktur-schiene_ausgangslage'
        params = {'lang': lang}
        resp = self.testapp.get(path, params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        fields = resp.json['fields']
        langSpecFields = []
        for field in fields:
            if field['name'].endswith('_%s' % lang):
                langSpecFields.append(field)
        self.failUnless(len(langSpecFields) > 0)
        langNotAvailable = 'rm'
        params = {'lang': langNotAvailable}
        resp = self.testapp.get(path, params=params, status=200)
        fields = resp.json['fields']
        langSpecFields = []
        # Check fallback lang
        for field in fields:
            if field['name'].endswith('_%s' % lang):
                langSpecFields.append(field)
        self.failUnless(len(langSpecFields) > 0)

    def test_layer_attributes_wrong_layer(self):
        self.testapp.get('/rest/services/ech/MapServer/dummy', status=400)

    def test_layer_attributes_multi_models(self):
        resp = self.testapp.get('/rest/services/api/MapServer/ch.bav.sachplan-infrastruktur-schiene_kraft', status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['fields']) == 3)

    def test_features_attributes_multi_models(self):
        resp = self.testapp.get('/rest/services/api/MapServer/ch.bav.sachplan-infrastruktur-schiene_kraft/attributes/plname_de', status=200)
        self.failUnless(resp.content_type == 'application/json')

zlayer = 'ch.swisstopo.zeitreihen'


class TestGebauedeGeometry(TestsBase):

    def test_feature_not_authorized(self):
        headers = {'X-SearchServer-Authorized': 'false'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/490830_0', headers=headers, status=200)
        self.assertTrue(resp.content_type == 'application/json')
        self.assertFalse('geometry' in resp.json['feature'])

    def test_feature_authorized(self):
        headers = {'X-SearchServer-Authorized': 'true'}
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/490830_0', headers=headers, status=200)
        self.assertTrue(resp.content_type == 'application/json')
        self.assertTrue('geometry' in resp.json['feature'])

    def test_find_not_authorized(self):
        headers = {'X-SearchServer-Authorized': 'false'}
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': 'berges', 'searchField': 'strname1'}
        resp = self.testapp.get('/rest/services/ech/MapServer/find', params=params, headers=headers, status=200)
        self.assertTrue(resp.content_type == 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertFalse('geometry' in resp.json['results'][0])

    def test_find_authorized(self):
        headers = {'X-SearchServer-Authorized': 'true'}
        params = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': 'berges', 'searchField': 'strname1'}
        resp = self.testapp.get('/rest/services/ech/MapServer/find', params=params, headers=headers, status=200)
        self.assertTrue(resp.content_type == 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertTrue('geometry' in resp.json['results'][0])

    def test_identify_not_authorized(self):
        headers = {'X-SearchServer-Authorized': 'false'}
        params = {'geometry': '653199.9999999999,137409.99999999997', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,623,96', 'layers': 'all:ch.bfs.gebaeude_wohnungs_register', 'mapExtent': '633200,132729.99999999997,671600,145189.99999999997',
                  'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=headers, status=200)
        self.assertTrue(resp.content_type == 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertFalse('geometry' in resp.json['results'][0])

    def test_identify_authorized(self):
        headers = {'X-SearchServer-Authorized': 'true'}
        params = {'geometry': '653199.9999999999,137409.99999999997', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,623,96', 'layers': 'all:ch.bfs.gebaeude_wohnungs_register', 'mapExtent': '633200,132729.99999999997,671600,145189.99999999997',
                  'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=headers, status=200)
        self.assertTrue(resp.content_type == 'application/json')
        self.assertTrue(len(resp.json['results']) >= 1)
        self.assertTrue('geometry' in resp.json['results'][0])


class TestReleasesService(TestsBase):

    def test_service(self):
        params = {'imageDisplay': '500,600,96', 'mapExtent': '611399.9999999999,158650,690299.9999999999,198150'}
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.failUnless(resp.content_type == 'application/json')
        self.failUnless(len(resp.json['results']) >= 122, len(resp.json['results']))

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
