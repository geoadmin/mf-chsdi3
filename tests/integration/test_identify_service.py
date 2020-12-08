# -*- coding: utf-8 -*-

from unittest import skip, skipUnless
from tests.integration import TestsBase, shift_to_lv95, reproject_to_srid, s3_tests
import math
from shapely.geometry import shape, Point, box


accept_headers = {'Accept': 'application/json, text/plain, */*'}


class TestIdentifyService(TestsBase):

    def test_identify_trivial(self):
        params = {'lang': 'fr',
                  'layers': 'all:ch.bafu.nabelstationen',
                  'imageDisplay': '1391,1070,96',
                  'mapExtent': '312250,-77500,1007750,457500',
                  'geometry': '678250,213000',
                  'geometryFormat': 'geojson',
                  'returnGeometry': 'true',
                  'geometryType': 'esriGeometryPoint',
                  'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')

    def test_trivial_from_doc(self):
        params = {'lang': 'fr',
                  'sr': '2056',
                  'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo-vd.ortschaftenverzeichnis_plz',
                  'imageDisplay': '0,0,0',
                  'mapExtent': '0,0,0,0',
                  'geometry': '2585438.308,1220677.966',
                  'geometryFormat': 'geojson',
                  'returnGeometry': 'false',
                  'geometryType': 'esriGeometryPoint',
                  'tolerance': '0'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(len(resp.json['results']), 2)

    def test_identify_no_parameters(self):
        self.testapp.get('/rest/services/ech/MapServer/identify', headers=accept_headers, status=400)

    def test_identify_without_geometry(self):
        params = {'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide the parameter geometry')

    def test_identify_invalid_geometrytype(self):
        params = {'geometryType': 'Envelope',
                  'geometry': '548945.5,147956,549402,148103.5',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide a valid geometry type')

    def test_identify_without_geometrytype(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertEqual(resp.json['status'], 'error')
        self.assertTrue(resp.json['detail'].startswith('Please provide the parameter geometryType'))

    def test_identify_without_imagedisplay(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'geometryType': 'esriGeometryEnvelope',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertEqual(resp.json['status'], 'error')
        self.assertTrue(resp.json['detail'].startswith('Please provide the parameter imageDisplay'))

    def test_identify_without_mapextent(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'tolerance': '1',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertEqual(resp.json['status'], 'error')

    def test_identify_without_tolerance(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertEqual(resp.json['status'], 'error')
        self.assertTrue(resp.json['detail'].startswith('Please provide the parameter tolerance'))

    # TODO This example is valid, but makes no sens at all.
    # You cannot get a resolution or a scale from such imageDisplay
    def test_identify_null_imageDisplay(self):
        params = {'lang': 'fr',
                  'layers': 'all:ch.bafu.nabelstationen',
                  'imageDisplay': '0,100,100',
                  'mapExtent': '312250,-77500,1007750,457500',
                  'geometry': '678250,213000',
                  'geometryFormat': 'geojson',
                  'returnGeometry': 'true',
                  'geometryType': 'esriGeometryPoint',
                  'tolerance': '5'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertTrue(resp.json['detail'].startswith('All values for parameter "imageDisplay" must be strictly positive'))

    def test_identify_optional_imageDisplay_when_tolerance_is_zero(self):
        params = {'lang': 'fr',
                  'layers': 'all:ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill',
                  'geometry': '548945.5,147956,549402,148103.5',
                  'returnGeometry': 'false',
                  'geometryType': 'esriGeometryEnvelope',
                  'tolerance': '0'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn('Lavaux', resp)

    def test_identify_polyline(self):
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '0',
                  'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEsrijsonFeature(resp.json['results'][0], 21781)

    def test_identify_polygon(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '0',
                  'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEsrijsonFeature(resp.json['results'][0], 21781)

    def test_identify_geometry_polyline_missmatch(self):
        # Geometry is a PolyLine ("paths") and not a Polygon ("rings")!
        params = {'geometry': '{"paths": [[[2554060, 1198340],[2554060, 1198530],[2554240, 1198530],[2554240, 1198340],[2554060, 1198340]]]}',
                  'geometryType': 'esriGeometryPolygon',
                  'imageDisplay': '1920,852,96',
                  'mapExtent': '420000,350000,900000,30000',
                  'tolerance': '0',
                  'layers': 'all:ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain("Missmatch between 'geometryType': esriGeometryPolygon and provided 'geometry' parsed as 'LineString'")

    def test_identify_geometry_polygon_missmatch(self):
        # Geometry is a Polygon ("rings") and not a Polyline ("paths")!
        params = {'geometry': '{"rings": [[[2554060, 1198340],[2554060, 1198530],[2554240, 1198530],[2554240, 1198340],[2554060, 1198340]]]}',
                  'geometryType': 'esriGeometryPolyline',
                  'imageDisplay': '1920,852,96',
                  'mapExtent': '420000,350000,900000,30000',
                  'tolerance': '0',
                  'layers': 'all:ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain("Missmatch between 'geometryType': esriGeometryPolyline and provided 'geometry' parsed as 'Polygon'")

    # If tolerance is 0, imageMap and mapxExtent may be optinal
    def test_tolerance_zero_optional_params(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon',
                  'tolerance': '0',
                  'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(len(resp.json['results']), 3)

    def test_identify_nan_error(self):
        params = {'geometry': '{"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon',
                  'imageDisplay': '500,600,96',
                  'mapExtent': 'NaN,147956,549402,148103.5',
                  'tolerance': '5',
                  'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide numerical values for the parameter mapExtent')
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '600000,NaN,549402,148103.5',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide a valid geometry')
        params = {'geometry': '{"rings":[[[NaN,NaN],[NaN,NaN],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolygon',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '600000,147956,549402,148103.5',
                  'tolerance': '0',
                  'layers': 'all:ch.bafu.bundesinventare-bln'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide a valid geometry')
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': 'NaN',
                  'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide an integer value for the pixel tolerance')

    # TODO
    def test_identify_zero_tolerance_and_scale(self):
        params = {'geometry': '681999,251083,682146,251190',
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '1920,452,96',
                  'layers': 'all:ch.bazl.sachplan-infrastruktur-luftfahrt_kraft',
                  'mapExtent': '679364.12,250588.34,684164.12,251718.34',
                  'tolerance': '0'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(len(resp.json['results']), 1)
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_valid(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all:ch.swisstopo.fixpunkte-agnes'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_geom_within_bbox(self):
        # All stations west of Bern
        envelop = [450000, 50000, 600000, 450000]
        params = {'geometry': ','.join(map(str, envelop)),
                  'sr': 21781,
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '0',
                  'geometryFormat': 'geojson',
                  'returnGeometry': True,
                  'layers': 'all:ch.swisstopo.fixpunkte-agnes'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        features = resp.json['results']
        self.assertEqual(len(features), 11)
        bbox = box(*envelop)
        for f in features:
            pnt = shape(f['geometry'])
            self.assertTrue(bbox.contains(pnt))

    @skip("How is this working? Really")
    def test_identify_geom_within_point(self):
        # Distance from the old observatory in Bern
        # tolerance=9  --> [(u'HUTT', 36780.71389369724), (u'NEUC', 38203.81803602861), (u'ZIM2', 8467.901107122028), (u'ZIMM', 8471.975418401587)]
        center = [2600000, 1200000]
        params = {'geometry': ','.join(map(str, center)),
                  'sr': 2056,
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '400,300,100',                   # In theory, 1 pixel = 1'000 meters
                  'mapExtent': '2450000,1050000,2850000,2350000',  # 400'000 x 300'000 meters
                  'tolerance': '9',           # Zimmerwald is about 8.57 km from the old observatory in Bern
                  'geometryFormat': 'geojson',
                  'returnGeometry': True,
                  'layers': 'all:ch.swisstopo.fixpunkte-agnes'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        features = resp.json['results']
        self.assertEqual(len(features), 4)
        origin = Point(*center)
        s = []
        for f in features:
            pnt = shape(f['geometry'])
            distance = origin.distance(pnt)
            s.append((f['featureId'],  distance))
            # self.assertTrue(distance < 9000)
        self.assertEqual('', s)

    def test_identify_geom_within_point_dummy_params(self):
        # Distance from the old observatory in Bern
        # tolerance=9'000 px  --> 9'000 meeters  (u'ZIM2', 8467.901107122028), (u'ZIMM', 8471.975418401587)
        center = [2600000, 1200000]
        params = {'geometry': ','.join(map(str, center)),
                  'sr': 2056,
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '100,100,100',         # In theory, 1 pixel = 1 meters
                  'mapExtent': '0,0,100,100',            # 100 x 100 meters
                  'tolerance': 9000,                     # Zimmerwald is about 8.57 km from the old observatory in Bern
                  'geometryFormat': 'geojson',
                  'returnGeometry': True,
                  'layers': 'all:ch.swisstopo.fixpunkte-agnes'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        features = resp.json['results']
        origin = Point(*center)
        for f in features:
            pnt = shape(f['geometry'])
            distance = origin.distance(pnt)
            self.assertLessEqual(distance, params['tolerance'])

    def test_identify_geom_addresses_within_circle(self):
        # Distance from the old observatory in Bern
        # tolerance=200px --> 200 meters
        center = [2600000, 1200000]
        params = {'geometry': ','.join(map(str, center)),
                  'sr': 2056,
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '100,100,100',         # In theory, 1 pixel = 1 meters
                  'mapExtent': '0,0,100,100',            # 100 x 100 meters
                  'tolerance': 200,                      # Should be a center with radius 200 meters
                  'geometryFormat': 'geojson',
                  'returnGeometry': True,
                  'layers': 'all:ch.bfs.gebaeude_wohnungs_register'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        features = resp.json['results']
        origin = Point(*center)
        for f in features:
            pnt = shape(f['geometry'])
            distance = origin.distance(pnt)
            self.assertLessEqual(distance, params['tolerance'])

    def test_identify_valid_esri_point(self):
        params = {'geometry': '{"x":717725.72800819238,"y":96257.179952642487,"spatialReference":{"wkid":21781}}',
                  'geometryType': 'esriGeometryPoint',
                  'returnGeometry': True,
                  'imageDisplay': '100,100,100',
                  'mapExtent': '0,0,100,100',
                  'tolerance': '100',
                  'layers': 'all:ch.bfs.gebaeude_wohnungs_register'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    @skipUnless(s3_tests, "Requires AWS S3 access")
    def test_identify_valid_on_grid(self):
        params = {'geometry': '555000,171125',
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,793,96',
                  'layers': 'all:ch.bfe.windenergie-geschwindigkeit_h50',
                  'mapExtent': '346831.18,86207.571,826831.18,284457.57',
                  'returnGeometry': 'true',
                  'tolerance': '10'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertIn('results', resp.json)
        self.assertEqual(len(resp.json['results']), 1)
        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_2.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_2.json['results'][0], 2056)
        self.assertEqual(resp.json['results'][0]['id'], resp_2.json['results'][0]['id'])

    @skipUnless(s3_tests, "Requires AWS S3 access")
    def test_identify_valid_envelope_on_grid(self):
        params = {'geometry': '555000,171125,556000,172125',
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '1920,793,96',
                  'layers': 'all:ch.bfe.windenergie-geschwindigkeit_h50',
                  'mapExtent': '346831.18,86207.57,826831.18,284457.57',
                  'returnGeometry': 'true',
                  'tolerance': '10'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertIn('results', resp.json)
        self.assertEqual(len(resp.json['results']), 1)

    def test_identify_invalid_geom_type_on_grid(self):
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline',
                  'imageDisplay': '500,600,96',
                  'layers': 'all:ch.bfe.windenergie-geschwindigkeit_h100',
                  'mapExtent': '346831.18,86207.57,826831.18,284457.57',
                  'returnGeometry': 'true',
                  'tolerance': '10'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertEqual(resp.json['status'], 'error')

    def test_invalid_imageDisplay(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertEqual(resp.json['status'], 'error')
        self.assertTrue(resp.json['detail'].startswith('Please provide the parameter imageDisplay in a comma separated list of 3 arguments (width,height,dpi)'))

        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers={'Accept': 'text/html'}, status=400)
        self.assertEqual(resp.content_type, 'text/html')

        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers={'Accept': '*/*'}, status=400)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_valid_topic(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all:ch.swisstopo.fixpunkte-agnes'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_identify_valid_with_callback(self):
        params = {'geometry': '548945.5,147956,549402,148103.5',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all:ch.swisstopo.fixpunkte-agnes',
                  'callback': 'cb_'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'text/javascript')

    def test_identify_with_geojson(self):
        params = {'geometry': '600000,200000,631000,210000',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all:ch.bafu.bundesinventare-bln',
                  'geometryFormat': 'geojson'}
        resp_1 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_1.json['results'][0], 21781)

        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_2.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_2.json['results'][0], 2056)

        self.assertEqual(resp_1.json['results'][0]['id'], resp_2.json['results'][0]['id'])

    def test_identify_with_geojson_returned_geometry(self):
        params = {'geometry': '600000,200000,6020000,2020000',  # 600000,200000,631000,210000',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '1',
                  'layers': 'all:ch.swisstopo.lubis-luftbilder_farbe',
                  'geometryFormat': 'geojson'}
        resp_1 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_1.json['results'][0], 21781)
        self.assertIn(resp_1.json['results'][0]['geometry']['type'], ['Polygon', 'GeometryCollection'])

        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_2.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_2.json['results'][0], 2056)
        self.assertEqual(len(resp_2.json['results']), len(resp_1.json['results']))
        self.assertEqual(resp_1.json['results'][0]['id'], resp_2.json['results'][0]['id'])

    def test_identify_with_geojson_returned_geometry_various_sr(self):
        params = {'geometry': '600000,200000,601000,201000',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '600000,200000,601000,201000',
                  'tolerance': '1',
                  'layers': 'all:ch.bav.haltestellen-oev',
                  'geometryFormat': 'geojson',
                  'sr': '21781'}

        # LV03
        resp_1 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_1.json['results'][0], 21781)
        self.assertIn(resp_1.json['results'][0]['geometry']['type'], ['MultiPoint', 'GeometryCollection'])
        resp1_ids = [d['id'] for d in resp_1.json['results']]

        # LV95
        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_2.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_2.json['results'][0], 2056)
        self.assertEqual(len(resp_2.json['results']), len(resp_1.json['results']))
        self.assertEqual(resp_1.json['results'][0]['id'], resp_2.json['results'][0]['id'])
        resp2_ids = [d['id'] for d in resp_2.json['results']]
        self.assertEqual(resp1_ids, resp2_ids)

        # Web Mercator
        # TODO requess is OK, geometries are not reprojected
        params['sr'] = '3857'
        params['geometry'] = reproject_to_srid(params['geometry'], 2056, 3857)
        params['mapExtent'] = reproject_to_srid(params['mapExtent'], 2056, 3857)
        resp_3 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_3.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_3.json['results'][0], 3857)
        self.assertEqual(len(resp_3.json['results']), len(resp_2.json['results']))
        self.assertEqual(resp_3.json['results'][0]['id'], resp_2.json['results'][0]['id'])
        resp3_ids = [d['id'] for d in resp_3.json['results']]
        self.assertEqual(resp1_ids, resp3_ids)

    def test_identify_gen50_geom(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'returnGeometry': 'false',
                  'layers': 'all:ch.swisstopo-vd.geometa-gemeinde',
                  'geometry': '561289,185240',
                  'mapExtent': '561156.75,185155,561421.25,185325',
                  'imageDisplay': '529,340,96',
                  'tolerance': '5'}
        resp_1 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertNotEqual(len(resp_1.json['results']), 0)
        self.assertEsrijsonFeature(resp_1.json['results'][0], 21781, hasGeometry=False)

        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertNotEqual(len(resp_2.json['results']), 0)
        self.assertEsrijsonFeature(resp_2.json['results'][0], 2056, hasGeometry=False)

        self.assertEqual(resp_1.json['results'][0]['id'], resp_2.json['results'][0]['id'])

    def test_identify_no_geom(self):
        params = {'geometry': '630000,245000,645000,265000',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '545132,147068,550132,150568',
                  'tolerance': '1',
                  'layers': 'all',
                  'returnGeometry': 'false'}
        resp = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertNotIn('geometry', resp.json['results'][0])
        self.assertNotIn('geometryType', resp.json['results'][0])

    def test_identify_faulty_params(self):
        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': '-Infinity,-Infinity,Infinity,Infinity',
                  'imageDisplay': '0,0,0',
                  'mapExtent': '0,0,0,0',
                  'tolerance': 0,
                  'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo.swissboundaries3d-land-flaeche.fill',
                  'returnGeometry': 'false',
                  'lang': 'fr'}
        self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=400)

    def test_identify_timeinstant(self):
        params = {'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.809670509,170647.93120352627',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen',
                  'timeInstant': '1936'}
        resp_1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.content_type, 'application/geo+json')
        # TODO: Results looks OK, 'years'=1936 is present
        self.assertEqual(len(resp_1.json['results']), 7)
        self.assertGeojsonFeature(resp_1.json['results'][0], 21781)

        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertNotEqual(len(resp_2.json['results']), 0)
        self.assertGeojsonFeature(resp_2.json['results'][0], 2056)

        self.assertEqual(resp_1.json['results'][0]['id'], resp_2.json['results'][0]['id'])

    def test_identify_timeinstant_zeitreihen(self):
        params = {'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryPoint',
                  'geometry': '614277,188148',
                  'imageDisplay': '1920,573,96',
                  'mapExtent': '570727,172398,666727,201048',
                  'tolerance': '10',
                  'timeInstant': '2000',
                  'returnGeometry': 'true',
                  'layers': 'all:ch.swisstopo.zeitreihen'}
        resp_1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.content_type, 'application/geo+json')
        self.assertEqual(resp_1.json['results'][0]['properties']['produkt'], 'lk25')
        self.assertEqual(len(resp_1.json['results']), 1)
        self.assertGeojsonFeature(resp_1.json['results'][0], 21781)

        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertNotEqual(len(resp_2.json['results']), 0)
        self.assertGeojsonFeature(resp_2.json['results'][0], 2056)

        self.assertEqual(resp_1.json['results'][0]['id'], resp_2.json['results'][0]['id'])

    def test_identify_one_timeinstant_several_layers(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.8,170647.9',
                  'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen,ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.bazl.luftfahrthindernis',
                  'timeInstant': '2000'}
        resp_1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp_1.json['results'][0], 21781)

        params['sr'] = '2056'
        params['geometry'] = shift_to_lv95(params['geometry'])
        params['mapExtent'] = shift_to_lv95(params['mapExtent'])
        resp_2 = self.testapp.get('/rest/services/ech/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertNotEqual(len(resp_2.json['results']), 0)
        self.assertGeojsonFeature(resp_2.json['results'][0], 2056)

        self.assertEqual(resp_1.json['results'][0]['id'], resp_2.json['results'][0]['id'])

    def test_identify_nbtimeinstants_nblayers_mismatch(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.8,170647.9',
                  'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen,ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.bazl.luftfahrthindernis',
                  'timeInstant': '2000,2002'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.json['code'], 400)
        self.assertEqual(resp.json['status'], 'error')
        resp.mustcontain('Number of timInstants')

    def test_identify_several_timeinstants(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.8,170647.9',
                  'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen,ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.bazl.luftfahrthindernis',
                  'timeInstant': '1936,,2014'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertIn('properties', resp.json['results'][0])
        self.assertIn('geometry', resp.json['results'][0])

    def test_identify_several_timeinstants_onebad(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.8,170647.9',
                  'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen,ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.bazl.luftfahrthindernis',
                  'timeInstant': '1936,,toto'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide an integer for the parameter timeInstant')

    def test_invalid_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.809670509,170647.93120352627',
                  'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5', 'layers': 'all:ch.swisstopo.zeitreihen',
                  'timeInstant': 'asdf'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('Please provide an integer for the parameter timeInstant')

    def test_identify_wrong_timeinstant(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.809670509,170647.93120352627',
                  'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5',
                  'layers': 'all:ch.swisstopo.zeitreihen',
                  'timeInstant': '19366'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)

    def test_identify_timeinstant_nottimeenabled_layer(self):
        params = {'geometryType': 'esriGeometryPoint',
                  'geometry': '630853.809670509,170647.93120352627',
                  'geometryFormat': 'geojson',
                  'imageDisplay': '1920,734,96',
                  'mapExtent': '134253,-21102,1382253,455997',
                  'tolerance': '5',
                  'layers': 'all:ch.bafu.bundesinventare-bln',
                  'timeInstant': '1936'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)

    def test_identify_oereb(self):
        params = {'geometry': '618953,170093',
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,576,96',
                  'layers': 'all:ch.bav.kataster-belasteter-standorte-oev.oereb',
                  'mapExtent': '671164.31244,253770,690364.31244,259530',
                  'tolerance': '5',
                  'geometryFormat': 'interlis'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'text/xml')

    def test_identify_oereb_several_layers(self):
        params = {'geometry': '618953,170093',
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,576,96',
                  'layers': 'all:ch.bav.kataster-belasteter-standorte-oev.oereb,ch.bazl.sicherheitszonenplan.oereb',
                  'mapExtent': '671164.31244,253770,690364.31244,259530',
                  'tolerance': '5',
                  'geometryFormat': 'interlis'}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)

    def test_identify_query_time(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'where': 'startofconstruction > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_null(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp',
                  'where': 'andere_stoffe is null'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_not_null(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp',
                  'where': 'andere_stoffe is not null'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_number(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'where': 'maxheightagl > 210'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_text(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'where': 'state ilike \'%a%\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_or(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'where': 'state ilike \'%a%\' and startofconstruction > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_and(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'where': 'state ilike \'%a%\' or startofconstruction > \'2014-12-01\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    @skip("Attribute 'contour' is not queryable. So make it queryable or remove test")
    def test_identify_query_models_no_attr(self):
        params = {'geometry': '663500,224750,698500,281250',
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryEnvelope',
                  'imageDisplay': '876,1075,96',
                  'lang': 'fr',
                  'layers': 'all:ch.swisstopo.hebungsraten',
                  'mapExtent': '441000,-78750,879000,458750',
                  'tolerance': '5',
                  'where': 'contour < 0.4'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_bad_operator(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'where': 'state ilike \'%a%\' maybe abortionaccomplished > \'2014-12-01\''}
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)

    @skip("Attribute 'obstacletype' is not queryable. So make it queryable or remove test")
    def test_identify_query_and_bbox(self):
        params = {'geometryType': 'esriGeometryEnvelope',
                  'geometry': '502722,36344,745822,253444',
                  'imageDisplay': '0,0,0',
                  'mapExtent': '0,0,0,0',
                  'tolerance': '0',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'where': 'obstacletype = \'Antenna\''}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertGreater(len(resp.json['results']), 0)
        self.assertEsrijsonFeature(resp.json['results'][0], 21781)

    @skip("Skiping until the string is correctly escaped")
    def test_identify_query_escape_quote(self):
        params = {'geometryFormat': 'geojson',
                  'lang': 'en',
                  'layers': 'all:ch.bafu.hydrologie-wassertemperaturmessstationen',
                  'time': '2013',
                  'where': "name ilike \'%Broye-Payerne, Caserne d'aviation%\' or name ilike \'%Aare-Bern, Schönau%\'"}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGreater(len(resp.json['results']), 0)
        self.assertGeojsonFeature(resp.json['results'][0], 21781)

    def test_identify_query_offset(self):
        params = {'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill',
                  'returnGeometry': 'false',
                  'timeInstant': '2015',
                  'where': 'gemname ilike \'%a%\''}
        resp_1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        params.update({'offset': '2'})
        self.assertNotIn('geometry', resp_1.json['results'][0])
        resp_2 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.json['results'][2]['featureId'], resp_2.json['results'][0]['featureId'])
        self.assertEqual(resp_1.json['results'][5]['featureId'], resp_2.json['results'][3]['featureId'])
        self.assertNotIn('geometry', resp_2.json['results'][0])
        params.update({'offset': '5'})
        resp_3 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_2.json['results'][3]['featureId'], resp_3.json['results'][0]['featureId'])
        self.assertEqual(resp_1.json['results'][5]['featureId'], resp_3.json['results'][0]['featureId'])
        self.assertNotIn('geometry', resp_3.json['results'][0])

    def test_identify_bbox_offset(self):
        params = {'layers': 'all:ch.bazl.luftfahrthindernis',
                  'timeInstant': '2015',
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryEnvelope',
                  'geometry': '573788,93220,750288,192720',
                  'imageDisplay': '1920,778,96',
                  'mapExtent': '107788,-5279,1067788,383720',
                  'tolerance': '0'}
        resp_1 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        params.update({'offset': '2'})
        resp_2 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_1.json['results'][2]['featureId'], resp_2.json['results'][0]['featureId'])
        self.assertEqual(resp_1.json['results'][5]['featureId'], resp_2.json['results'][3]['featureId'])
        params.update({'offset': '4'})
        resp_3 = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp_2.json['results'][2]['featureId'], resp_3.json['results'][0]['featureId'])
        self.assertEqual(resp_1.json['results'][4]['featureId'], resp_3.json['results'][0]['featureId'])

    def test_identify_query_wrong_offset(self):
        params = {'layers': 'all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill',
                  'timeInstant': '2015',
                  'where': 'gemname ilike \'%aven%\'',
                  'offset': '12.1'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('provide an integer')

    def test_identify_result_limit(self):
        # Assure not more than 201 results are returned
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '10',
                  'layers': 'all:ch.bfs.gebaeude_wohnungs_register'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(201, len(resp.json['results']))

    def test_identify_limit_parameter(self):
        # No limit parameters
        params = {'geometry': '{"paths":[[[595000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}',
                  'geometryType': 'esriGeometryPolyline',
                  'imageDisplay': '500,600,96',
                  'mapExtent': '548945.5,147956,549402,148103.5',
                  'tolerance': '10',
                  'layers': 'all:ch.bfs.gebaeude_wohnungs_register'}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertLess(10, len(resp.json['results']))

        # Limit parameter
        params.update({'limit': '5'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(5, len(resp.json['results']))
        params.update({'limit': '1'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(1, len(resp.json['results']))
        params.update({'limit': '0'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(0, len(resp.json['results']))

        # Invalid limit parameters
        params.update({'limit': '-1'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('provide a positive integer')
        params.update({'limit': 'a'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)

    def test_identify_quer_spatial_filters_scale_dep(self):
        params = {'layers': 'all:ch.bav.haltestellen-oev',
                  'geometry': '643952.5,164121.24999999997',
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1641,867,96',
                  'mapExtent': '533750,136249.99999999994,550250,174249.99999999997',
                  'tolerance': '5',
                  'where': 'name ilike \'%dietikon%\''
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(len(resp.json['results']), 0)
        params['geometryType'] = 'esriGeometryEnvelope'
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)

    def test_identify_order_by_distance(self):
        x_a = 2643952.5
        y_a = 1164121.24999999997

        params = {'layers': 'all:ch.bfs.gebaeude_wohnungs_register',
                  'geometry': str(x_a) + ',' + str(y_a),
                  'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryPoint',
                  'imageDisplay': '1920,765,96',
                  'mapExtent': '2641960.1008933608,1163518.83578498938,2646760.1008933608,1165431.33578498938',
                  'tolerance': '50',
                  'sr': 2056
                  }
        params.update({'order': 'distance'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertLess(1, len(resp.json['results']))
        res = resp.json['results']

        # Test ordering
        d = 0
        for r in res:
            x_b = r['geometry']['coordinates'][0]
            y_b = r['geometry']['coordinates'][1]
            dist = math.sqrt(math.pow(x_b - x_a, 2) + math.pow(y_b - y_a, 2))
            self.assertLess(d, dist)
            d = dist

        # Wrong order parameter should not have impact
        params.update({'order': 'x'})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('valid order parameter')

        # order does only work with geometry
        params.update({'order': 'distance'})
        params.pop('geometry', None)
        params.update({'where': 'abortionaccomplished > \'2014-12-01\''})
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        resp.mustcontain('together with a geometry')

    def test_identify_outside_extent(self):
        params = dict(geometryType='esriGeometryPoint',
                      geometry='516750,307656.25',
                      geometryFormat='geojson',
                      imageDisplay='671,600,96',
                      mapExtent='492250,35000,827750,335000',
                      tolerance=10,
                      layers='all:ch.bfe.windenergie-geschwindigkeit_h125',
                      lang='de'
                      )
        resp = self.testapp.get('/rest/services/api/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(len(resp.json['results']), 0)
#
#    TODO: activate after update of data (ltpal)
#   def test_identify_treasurehunt_good_scale(self):
#
#       params = dict(geometryType='esriGeometryPoint',
#                     geometry='2791830,1142580',
#                     geometryFormat='geojson',
#                     imageDisplay='1920,730,96',
#                     layers='all:ch.swisstopo.treasurehunt',
#                     mapExtent='2791830,1142580,2791830,1142580',
#                     returnGeometry='true',
#                     sr='2056',
#                     tolerance='10',
#                     lang='fr')
#       resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
#       self.assertEqual(resp.content_type, 'application/json')
#       self.assertEqual(len(resp.json['results']), 1)

    def test_identify_treasurehunt_not_in_scale_range(self):
        params = dict(geometryType='esriGeometryPoint',
                      geometry='611334,271015',
                      geometryFormat='geojson',
                      imageDisplay='1920,730,96',
                      layers='all:ch.swisstopo.treasurehunt',
                      mapExtent='601163,260868,621504,281135',
                      returnGeometry='true',
                      tolerance='10',
                      lang='fr')
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertEqual(len(resp.json['results']), 0)

    def test_identify_no_geotable(self):
        params = dict(geometryType='esriGeometryPoint',
                      geometry='612824.615589634,177050.95813678834',
                      geometryFormat='geojson',
                      imageDisplay='1920,730,96',
                      layers='all:ch.bakom.anschlussart-glasfaser',
                      mapExtent='659174.774934163,256650.066299024,663974.774934163,259240.066299024',
                      returnGeometry='true',
                      tolerance='10',
                      lang='fr')
        self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)

    def test_identify_layerDefs_and_where(self):
        params = {'geometryFormat': 'geojson',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'layerDefs': '{"ch.bazl.luftfahrthindernis": "startofconstruction > \'2014-12-01\'"}',
                  'where': "startofconstruction > \'2014-12-01\'"}
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn("Parameters 'layerDefs' and 'where' are mutually exclusive", resp.json['detail'])

    def test_identify_layerDefs_non_existing_layer(self):
        params = {'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryEnvelope',
                  'geometry': '2548945.5,1147956,2549402,1148103.5',
                  'imageDisplay': '1367,949,96',
                  'mapExtent': '2318250,952750,3001750,1427250',
                  'sr': '2056',
                  'tolerance': '5',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'layerDefs': '{"ch.another.layer": "startofconstruction > \'2014-12-01\'"}'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertIn("You can only filter on layer", resp.json['detail'])

    def test_identify_layerDefs_non_existing_attribute(self):
        params = {'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryEnvelope',
                  'geometry': '2548945.5,1147956,2549402,1148103.5',
                  'imageDisplay': '1367,949,96',
                  'mapExtent': '2318250,952750,3001750,1427250',
                  'sr': '2056',
                  'tolerance': '5',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'layerDefs': '{"ch.bazl.luftfahrthindernis": "dummy_attribute > \'2014-12-01\'"}'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=400)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue(u"Query attribute 'dummy_attribute' is not queryable" in resp.json['detail'])

    def test_identify_layerDefs(self):

        params = {'geometryFormat': 'geojson',
                  'geometryType': 'esriGeometryEnvelope',
                  'geometry': '2548945.5,1147956,2549402,1148103.5',
                  'imageDisplay': '1367,949,96',
                  'mapExtent': '2318250,952750,3001750,1427250',
                  'sr': '2056',
                  'tolerance': '5',
                  'layers': 'all:ch.bazl.luftfahrthindernis',
                  'layerDefs': '{"ch.bazl.luftfahrthindernis": "startofconstruction > \'2014-12-01\'"}'
                  }
        resp = self.testapp.get('/rest/services/all/MapServer/identify', params=params, headers=accept_headers, status=200)
        self.assertEqual(resp.content_type, 'application/geo+json')
        self.assertGeojsonFeature(resp.json['results'][0], 2056)
