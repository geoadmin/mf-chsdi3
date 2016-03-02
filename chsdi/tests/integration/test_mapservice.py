# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


def getLayers(query):
    for q in query:
        yield q[0]


class TestMapServiceView(TestsBase):

    def test_metadata_no_parameters(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_metadata_no_parameters_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer', status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_metadata_with_searchtext(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'searchText': 'wasser'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_metadata_with_callback(self):
        resp = self.testapp.get('/rest/services/blw/MapServer', params={'callback': 'cb'}, status=200)
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
        self.assertIn('ch.astra.ausnahmetransportrouten', resp.json['queryableLayers'])
        self.assertIn('ch.swisstopo-karto.hangneigung', resp.json['chargeableLayers'])
        self.assertIn('ch.are.alpenkonvention', resp.json['notChargeableLayers'])
        self.assertTrue(len(resp.json['searchableLayers']) > 20)
        self.assertTrue(len(resp.json['tooltipLayers']) > 20)
        self.assertTrue(len(resp.json['queryableLayers']) > 20)
        self.assertTrue(len(resp.json['chargeableLayers']) > 20)
        self.assertTrue(len(resp.json['notChargeableLayers']) > 20)
        self.assertTrue(len(resp.json['translations']) > 20)

    def test_faqlist_topic_all(self):
        resp = self.testapp.get('/rest/services/all/faqlist', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('ch.astra.ivs-nat', resp.json['searchableLayers'])
        self.assertIn('ch.are.agglomerationen_isolierte_staedte', resp.json['tooltipLayers'])
        self.assertIn('ch.astra.ausnahmetransportrouten', resp.json['queryableLayers'])
        self.assertIn('ch.swisstopo-karto.hangneigung', resp.json['chargeableLayers'])
        self.assertIn('ch.are.alpenkonvention', resp.json['notChargeableLayers'])
        self.assertTrue(len(resp.json['searchableLayers']) > 20)
        self.assertTrue(len(resp.json['tooltipLayers']) > 20)
        self.assertTrue(len(resp.json['queryableLayers']) > 20)
        self.assertTrue(len(resp.json['chargeableLayers']) > 20)
        self.assertTrue(len(resp.json['notChargeableLayers']) > 20)
        self.assertTrue(len(resp.json['translations']) > 20)

    def test_identify_no_parameters(self):
        self.testapp.get('/rest/services/ech/MapServer/identify', status=400)

    def test_identify_without_geometry(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter geometry')

    def test_identify_invalid_geometrytype(self):
        params = {'geometryType': 'Envelope', 'geometry': '548945.5,147956,549402,148103.5', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry type')

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
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_polygon(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}', 'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_nan_error(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}', 'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,600,96',
                  'mapExtent': 'NaN,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide numerical values for the parameter mapExtent')
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '600000,NaN,549402,148103.5', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry')
        params = {'geometry': '{"rings":[[[NaN,NaN],[NaN,NaN],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}', 'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,600,96',
                  'mapExtent': '600000,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide a valid geometry')
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}', 'geometryType': 'esriGeometryPolygon', 'imageDisplay': '500,NaN,96',
                  'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '0', 'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide numerical values for the parameter imageDisplay')
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}', 'geometryType': 'esriGeometryPolyline', 'imageDisplay': '500,600,96',
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
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_invalid_imageDisplay(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide the parameter imageDisplay in a comma separated list of 3 arguments (width,height,dpi)')

    def test_identify_valid_topic_all(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_valid_with_callback(self):
        params = {'geometry': '548945.5,147956,549402,148103.5', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1', 'layers': 'all',
                  'callback': 'cb'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'text/javascript')
        resp.mustcontain('cb({')

    def test_identify_with_geojson(self):
        params = {'geometry': '600000,200000,631000,210000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1',
                  'layers': 'all:ch.bafu.bundesinventare-bln', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_with_geojson_returned_geometry(self):
        params = {'geometry': '600000,200000,631000,210000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '548945.5,147956,549402,148103.5', 'tolerance': '1',
                  'layers': 'all:ch.swisstopo.lubis-luftbilder_farbe', 'geometryFormat': 'geojson'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn(resp.json['results'][0]['geometry']['type'], ['Polygon', 'GeometryCollection'])

    def test_identify_gen50_geom(self):
        params = {'geometryType': 'esriGeometryPoint', 'returnGeometry': 'false', 'layers': 'all:ch.swisstopo-vd.geometa-gemeinde', 'geometry': '561289,185240', 'mapExtent': '561156.75,185155,561421.25,185325',
                  'imageDisplay': '529,340,96', 'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertNotEqual(len(resp.json['results']), 0)

    def test_identify_no_geom(self):
        params = {'geometry': '630000,245000,645000,265000', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '500,600,96', 'mapExtent': '545132,147068,550132,150568', 'tolerance': '1', 'layers': 'all',
                  'returnGeometry': 'false'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertNotIn('geometry', resp.json['results'][0])
        self.assertNotIn('geometryType', resp.json['results'][0])

    def test_identify_faulty_params(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'geometry': '-Infinity,-Infinity,Infinity,Infinity', 'imageDisplay': '0,0,0', 'mapExtent': '0,0,0,0', 'tolerance': 0, 'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo.swissboundaries3d-land-flaeche.fill', 'returnGeometry': 'false', 'lang': 'fr'}

        self.testapp.get('/rest/services/ech/MapServer/identify', params=params, status=400)

    def test_identify_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson', 'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5', 'layers': 'all:ch.swisstopo.zeitreihen', 'timeInstant': '1936'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_invalid_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint', 'geometry': '630853.809670509,170647.93120352627', 'geometryFormat': 'geojson', 'imageDisplay': '1920,734,96', 'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5', 'layers': 'all:ch.swisstopo.zeitreihen', 'timeInstant': 'asdf'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)
        resp.mustcontain('Please provide an integer for the parameter timeInstant')

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
        self.assertEqual(resp.content_type, 'text/xml')

    def test_identify_oereb_several_layers(self):
        params = {'geometry': '618953,170093', 'geometryType': 'esriGeometryPoint', 'imageDisplay': '1920,576,96', 'layers': 'all:ch.bav.kataster-belasteter-standorte-oev.oereb,ch.bazl.sicherheitszonenplan.oereb',
                  'mapExtent': '671164.31244,253770,690364.31244,259530', 'tolerance': '5', 'geometryFormat': 'interlis'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_query_time(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'abortionaccomplished > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_null(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp', 'where': 'andere_stoffe is null'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_not_null(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp', 'where': 'andere_stoffe is not null'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_number(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'maxheightagl > 210'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_text(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_or(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\' and abortionaccomplished > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_and(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\' or abortionaccomplished > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_models_no_attr(self):
        params = {'geometry': '663500,224750,698500,281250', 'geometryFormat': 'geojson', 'geometryType': 'esriGeometryEnvelope', 'imageDisplay': '876,1075,96', 'lang': 'fr',
                  'layers': 'all:ch.swisstopo.hebungsraten', 'mapExtent': '441000,-78750,879000,458750', 'tolerance': '5', 'where': 'contour < 0.4'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_query_bad_operator(self):
        params = {'geometryFormat': 'geojson', 'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'state ilike \'%a%\' maybe abortionaccomplished > \'2014-12-01\''}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=400)

    def test_identify_query_and_bbox(self):
        params = {'geometryType': 'esriGeometryEnvelope', 'geometry': '502722,36344,745822,253444', 'imageDisplay': '0,0,0', 'mapExtent': '0,0,0,0', 'tolerance': '0',
                  'layers': 'all:ch.bazl.luftfahrthindernis', 'where': 'obstacletype = \'Antenna\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 0)

    def test_identify_query_escape_quote(self):
        params = {'geometryFormat': 'geojson', 'lang': 'en', 'layers': 'all:ch.bafu.hydrologie-wassertemperaturmessstationen',
                  'time': '2013', 'where': "name ilike \'%Broye-Payerne, Caserne d'aviation%\' or name ilike \'%Aare-Bern, Schönau%\'"}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 0)

    def test_identify_query_offset(self):
        params = {'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', 'returnGeometry': 'false', 'timeInstant': '2015',
                  'where': 'gemname ilike \'%a%\''}
        resp1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        params.update({'offset': '2'})
        resp2 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp1.json['results'][2]['featureId'], resp2.json['results'][0]['featureId'])
        self.assertEqual(resp1.json['results'][5]['featureId'], resp2.json['results'][3]['featureId'])
        params.update({'offset': '5'})
        resp3 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, status=200)
        self.assertEqual(resp2.json['results'][3]['featureId'], resp3.json['results'][0]['featureId'])
        self.assertEqual(resp1.json['results'][5]['featureId'], resp3.json['results'][0]['featureId'])

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
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/legend', params={'callback': 'cb'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_layersconfig_valid(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/layersConfig', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('ch.swisstopo.pixelkarte-farbe', resp.json)
        self.assertIn('attribution', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertIn('label', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertIn('background', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertIn('topics', resp.json['ch.swisstopo.pixelkarte-farbe_wmts'])
        self.assertIn('topics', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertNotIn('srid', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertNotIn('srid', resp.json['ch.swisstopo.pixelkarte-farbe_wmts'])
        self.assertNotIn('staging', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertNotIn('staging', resp.json['ch.swisstopo.pixelkarte-farbe_wmts'])
        self.assertNotIn('matrixSet', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertNotIn('matrixSet', resp.json['ch.swisstopo.pixelkarte-farbe_wmts'])

    def test_layersconfig_valid_topic_all(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('ch.swisstopo.pixelkarte-farbe', resp.json)
        self.assertIn('attribution', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertIn('label', resp.json['ch.swisstopo.pixelkarte-farbe'])
        self.assertIn('background', resp.json['ch.swisstopo.pixelkarte-farbe'])

    def test_layersconfig_geojson_layer(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.assertTrue(resp.content_type == 'application/json')
        jsonData = resp.json
        if 'ch.bafu.hydroweb-messstationen_gefahren' in jsonData:
            layer = jsonData['ch.bafu.hydroweb-messstationen_gefahren']
            self.assertTrue(layer['type'], 'geojson')
            self.assertIn('geojsonUrl', layer)
            self.assertNotIn('geojsonUrlDe', layer)
            self.assertIn('styleUrl', layer)
            self.assertIn('updateDelay', layer)

    def test_layersconfig_with_callback(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/layersConfig', params={'callback': 'cb'}, status=200)
        self.assertTrue(resp.content_type == 'application/javascript')

    def test_layersconfig_wrong_map(self):
        self.testapp.get('/rest/services/foo/MapServer/layersConfig', status=400)

    def test_layersconfig_queryable_attributes(self):
        resp = self.testapp.get('/rest/services/all/MapServer/layersConfig', status=200)
        self.assertTrue(resp.content_type == 'application/json')
        jsonData = resp.json
        self.assertIn('ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp', jsonData)
        layer = jsonData['ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp']
        self.assertIn('queryableAttributes', layer)
        self.assertTrue(len(layer['queryableAttributes']) > 0)
        # Should not have
        self.assertIn('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', jsonData)
        layer = jsonData['ch.swisstopo.vec200-transportation-oeffentliche-verkehr']
        self.assertNotIn('queryableAttributes', layer)

    def test_layer_attributes(self):
        resp = self.testapp.get('/rest/services/ech/MapServer/ch.bafu.bundesinventare-bln', status=200)
        self.assertTrue(resp.content_type == 'application/json')

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
        self.assertTrue(len(langSpecFields) > 0)
        langNotAvailable = 'rm'
        params = {'lang': langNotAvailable}
        resp = self.testapp.get(path, params=params, status=200)
        fields = resp.json['fields']
        langSpecFields = []
        # Check fallback lang
        for field in fields:
            if field['name'].endswith('_%s' % lang):
                langSpecFields.append(field)
        self.assertTrue(len(langSpecFields) > 0)

    def test_layer_attributes_wrong_layer(self):
        self.testapp.get('/rest/services/ech/MapServer/dummy', status=400)

    def test_layer_attributes_multi_models(self):
        resp = self.testapp.get('/rest/services/api/MapServer/ch.bav.sachplan-infrastruktur-schiene_kraft', status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(len(resp.json['fields']), 3)

    def test_features_attributes_multi_models(self):
        resp = self.testapp.get('/rest/services/api/MapServer/ch.bav.sachplan-infrastruktur-schiene_kraft/attributes/plname_de', status=200)
        self.assertEqual(resp.content_type, 'application/json')

zlayer = 'ch.swisstopo.zeitreihen'


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


class TestReleasesService(TestsBase):

    def test_service(self):
        params = {'imageDisplay': '500,600,96',
                  'mapExtent': '611399.9999999999,158650,690299.9999999999,198150',
                  'geometry': '650000.0,170000.0',
                  'geometryType': 'esriGeometryPoint'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/' + zlayer + '/releases', params=params, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(len(resp.json['results']) >= 26, len(resp.json['results']))

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
