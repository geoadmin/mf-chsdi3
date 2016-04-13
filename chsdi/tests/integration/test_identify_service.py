# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestIdentifyService(TestsBase):

    def test_identify_no_parameters(self):
        self.testapp.get('/rest/services/ech/MapServer/identify', status=400)

    def test_identify_without_geometry(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter geometry')

    def test_identify_invalid_geometrytype(self):
        params = {'geometryType': 'Envelope', 'geometry': '548945.5,147956,549402,148103.5', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry type')

    def test_identify_without_geometrytype(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter geometryType')

    def test_identify_without_imagedisplay(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter imageDisplay')

    def test_identify_without_mapextent(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('')

    def test_identify_without_tolerance(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter tolerance')

    def test_identify_polyline(self):
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('attributes', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_polygon(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('attributes', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_nan_error(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,600,96',
                  'mapExtent': 'NaN,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide numerical values for the parameter mapExtent')
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '600000,NaN,549402,148103.5', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry')
        params = {'geometry': '{"rings":[[[NaN,NaN],[NaN,NaN],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,600,96',
                  'mapExtent': '600000,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry')
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,NaN,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide numerical values for the parameter imageDisplay')
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': 'NaN', 'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide an integer value for the pixel tolerance')

    def test_identify_zero_tolerance_and_scale(self):
        params = {'geometry': '681999,251083,682146,251190', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '1920,452,96', 'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft',
                  'mapExtent': '679364.12,250588.34,684164.12,251718.34', 'tolerance': '0'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(len(resp.json['results']), 1)

    def test_identify_valid(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('results', resp.json)
        self.assertIn('attributes', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_valid_on_grid(self):
        params = {'geometry': '555000,171125', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,793,96', 'layers': 'all:ch.bfe.windenergie-geschwindigkeit_h50',
                  'mapExtent': '346831.18,86207.571,826831.18,284457.57', 'returnGeometry': 'true', 'tolerance': '10'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('results', resp.json)
        self.assertEqual(len(resp.json['results']), 1)

    def test_identify_valid_envelope_on_grid(self):
        params = {'geometry': '555000,171125,556000,172125', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '1920,793,96', 'layers': 'all:ch.bfe.windenergie-geschwindigkeit_h50',
                  'mapExtent': '346831.18,86207.57,826831.18,284457.57', 'returnGeometry': 'true', 'tolerance': '10'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('results', resp.json)
        self.assertEqual(len(resp.json['results']), 1)

    def test_identify_invalid_geom_type_on_grid(self):
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline', 'imageDisplay': '500,600,96', 'layers': 'all:ch.bfe.windenergie-geschwindigkeit_h100',
                  'mapExtent': '346831.18,86207.57,826831.18,284457.57', 'returnGeometry': 'true', 'tolerance': '10'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_invalid_imageDisplay(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter imageDisplay in a comma separated list of 3 arguments (width,height,dpi)')

    def test_identify_valid_topic_all(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('attributes', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_valid_with_callback(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all',
                  'callback': 'cb'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'text/javascript')
        resp.mustcontain('cb({')

    def test_identify_with_geojson(self):
        params = {'geometry': '600000,200000,631000,210000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1',
                  'layers': 'all:ch.bafu.bundesinventare-bln', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_with_geojson_returned_geometry(self):
        params = {'geometry': '600000,200000,631000,210000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1',
                  'layers': 'all:ch.swisstopo.lubis-luftbilder_farbe', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn(resp.json['results'][0]['geometry']['type'], ['Polygon', 'GeometryCollection'])

    def test_identify_gen50_geom(self):
        params = {'geometryType': 'esriGeometryPoint', 'returnGeometry': 'false', 'layers': 'all:ch.swisstopo-vd.geometa-gemeinde',
                  'geometry': '561289,185240', 'mapExtent': '561156.75,185155,561421.25,185325',
                  'imageDisplay': '529,340,96', 'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertNotEqual(len(resp.json['results']), 0)
        self.assertIn('attributes', resp.json['results'][0])
        self.assertNotIn('geometry', resp.json['results'][0])

    def test_identify_no_geom(self):
        params = {'geometry': '630000,245000,645000,265000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96',
                  'mapExtent': '545132,147068,550132,150568', 'tolerance': '1', 'layers': 'all',
                  'returnGeometry': 'false'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertNotIn('geometry', resp.json['results'][0])
        self.assertNotIn('geometryType', resp.json['results'][0])

    def test_identify_faulty_params(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'geometry': '-Infinity,-Infinity,Infinity,Infinity', 'imageDisplay': '0,0,0',
                  'mapExtent': '0,0,0,0', 'tolerance': 0,
                  'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo.swissboundaries3d-land-flaeche.fill',
                  'returnGeometry': 'false', 'lang': 'fr'}
        self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)

    def test_identify_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5', 'layers': 'all:ch.swisstopo.zeitreihen', 'timeInstant': '1936'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_invalid_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5', 'layers': 'all:ch.swisstopo.zeitreihen', 'timeInstant': 'asdf'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide an integer for the parameter timeInstant')

    def test_identify_wrong_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997', 'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen', 'timeInstant': '19366'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_timeinstant_nottimeenabled_layer(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997', 'tolerance': '5',
                  'layers': 'all:ch.bafu.bundesinventare-bln', 'timeInstant': '1936'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)

    def test_identify_oereb(self):
        params = {'geometry': '618953,170093', 'geometryType': 'esriGeometryPoint', 'imageDisplay': '1920,576,96',
                  'layers': 'all:ch.bav.kataster-belasteter-standorte-oev.oereb',
                  'mapExtent': '671164.31244,253770,690364.31244,259530', 'tolerance': '5', 'geometryFormat': 'interlis'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'text/xml')

    def test_identify_oereb_several_layers(self):
        params = {'geometry': '618953,170093', 'geometryType': 'esriGeometryPoint', 'imageDisplay': '1920,576,96',
                  'layers': 'all:ch.bav.kataster-belasteter-standorte-oev.oereb,ch.bazl.sicherheitszonenplan.oereb',
                  'mapExtent': '671164.31244,253770,690364.31244,259530', 'tolerance': '5', 'geometryFormat': 'interlis'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_query_time(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'abortionaccomplished > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_null(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp', 'where': 'andere_stoffe is null'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_not_null(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp', 'where': 'andere_stoffe is not null'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_number(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'maxheightagl > 210'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_text(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_or(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\' and startofconstruction > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_and(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\' or startofconstruction > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_models_no_attr(self):
        params = {'geometry': '663500,224750,698500,281250', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '876,1075,96', 'lang': 'fr',
                  'layers': 'all:ch.swisstopo.hebungsraten', 'mapExtent': '441000,-78750,879000,458750', 'tolerance': '5', 'where': 'contour < 0.4'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_bad_operator(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\' maybe abortionaccomplished > \'2014-12-01\''}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_query_and_bbox(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'geometry': '502722,36344,745822,253444', 'imageDisplay': '0,0,0', 'mapExtent': '0,0,0,0', 'tolerance': '0',
                  'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'obstacletype = \'Antenna\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 0)
        self.assertIn('attributes', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_escape_quote(self):
        params = {'geometryFormat': 'geojson', 'lang': 'en', 'layers': 'all:ch.bafu.hydrologie-wassertemperaturmessstationen',
                  'time': '2013', 'where': "name ilike \'%Broye-Payerne, Caserne d'aviation%\' or name ilike \'%Aare-Bern, Schönau%\'"}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 0)
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_query_offset(self):
        params = {'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', 'returnGeometry': 'false', 'timeInstant': '2015',
                  'where': 'gemname ilike \'%a%\''}
        resp1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        params.update({'offset': '2'})
        self.assertNotIn('geometry', resp1.json['results'][0])
        resp2 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp1.json['results'][2]['featureId'], resp2.json['results'][0]['featureId'])
        self.assertEqual(resp1.json['results'][5]['featureId'], resp2.json['results'][3]['featureId'])
        self.assertNotIn('geometry', resp2.json['results'][0])
        params.update({'offset': '5'})
        resp3 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp2.json['results'][3]['featureId'], resp3.json['results'][0]['featureId'])
        self.assertEqual(resp1.json['results'][5]['featureId'], resp3.json['results'][0]['featureId'])
        self.assertNotIn('geometry', resp3.json['results'][0])

    def test_identify_bbox_offset(self):
        params = {'layers': 'all:ch.bazl.luftfahrthindernis', 'timeInstant': '2015', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryEnvelope',
                  'geometry': '573788,93220,750288,192720',
                  'imageDisplay': '1920,778,96', 'mapExtent': '107788,-5279,1067788,383720', 'tolerance': '0'}
        resp1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        params.update({'offset': '2'})
        resp2 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp1.json['results'][2]['featureId'], resp2.json['results'][0]['featureId'])
        self.assertEqual(resp1.json['results'][5]['featureId'], resp2.json['results'][3]['featureId'])
        params.update({'offset': '4'})
        resp3 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp2.json['results'][2]['featureId'], resp3.json['results'][0]['featureId'])
        self.assertEqual(resp1.json['results'][4]['featureId'], resp3.json['results'][0]['featureId'])

    def test_identify_query_wrong_offset(self):
        params = {'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', 'timeInstant': '2015', 'where': 'gemname ilike \'%aven%\'', 'offset': '12.1'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('provide an integer')

    def test_identify_result_limit(self):
        # Assure not more than 201 results are returned
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '10', 'layers': 'all:ch.bfs.gebaeude_wohnungs_register'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(201, len(resp.json['results']))

    def test_identify_limit_parameter(self):
        # No limit parameters
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '10', 'layers': 'all:ch.bfs.gebaeude_wohnungs_register'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLess(10, len(resp.json['results']))

        # Limit parameter
        params.update({'limit': '5'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(5, len(resp.json['results']))
        params.update({'limit': '1'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(1, len(resp.json['results']))
        params.update({'limit': '0'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(0, len(resp.json['results']))

        # Invalid limit parameters
        params.update({'limit': '-1'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('provide a positive integer')
        params.update({'limit': 'a'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_order_by_distance(self):
        params = {'layers': 'all:ch.bfs.gebaeude_wohnungs_register',
                  'geometry': '643952.5,164121.24999999997',
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,765,96',
                  'mapExtent': '641960.1008933608,163518.83578498938,646760.1008933608,165431.33578498938',
                  'tolerance': '50'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLess(1, len(resp.json['results']))
        firstBefore = resp.json['results'][0]['attributes']['deinr']

        params.update({'order': 'distance'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLess(1, len(resp.json['results']))
        firstAfter = resp.json['results'][0]['attributes']['deinr']

        self.assertNotEqual(firstBefore, firstAfter)

        # Wrong order parameter should not have impact
        params.update({'order': 'x'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('valid order parameter')

        # order does only work with geometry
        params.update({'order': 'distance'})
        params.pop('geometry', None)
        params.update({'where': 'abortionaccomplished > \'2014-12-01\''})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('together with a geometry')
