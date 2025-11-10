import unittest

from shapely import geometry

from chsdi.lib.esrijson.geometry import Geometry, to_shape
from chsdi.lib.esrijson.feature import Feature
from chsdi.lib.esrijson.codec import dumps, loads


class BaseTestClass(unittest.TestCase):

    def getPoint(self, hasZ=False):
        if hasZ:
            return geometry.Point([0, 1, 5])
        return geometry.Point([0, 1])

    def getMultiPoint(self, hasZ=False):
        if hasZ:
            return geometry.MultiPoint([[0, 1, 5], [1, 2, 5]])
        return geometry.MultiPoint([[0, 1], [1, 2]])

    def getLineString(self, hasZ=False):
        if hasZ:
            return geometry.LineString([(0, 0, 5), (1, 1, 5)])
        return geometry.LineString([(0, 0), (1, 1)])

    def getMultiLineString(self, hasZ=False):
        if hasZ:
            return geometry.MultiLineString(
                [((0, 0, 5), (1, 1, 5)), ((-1, 0, 6), (1, 0, 6))])
        return geometry.MultiLineString(
            [((0, 0), (1, 1)), ((-1, 0), (1, 0))])

    def getPolygon(self, hasZ=False):
        if hasZ:
            return geometry.Polygon(
                [(0, 0, 5), (1, 1, 5), (2, 1, 5), (0, 0, 5)])
        return geometry.Polygon([(0, 0), (1, 1), (2, 1), (0, 0)])

    def getMultiPolygon(self, hasZ=False):
        if hasZ:
            return geometry.MultiPolygon(
                [geometry.Polygon(
                    [(0, 0, 5), (1, 1, 5), (2, 1, 5), (0, 0, 5)]),
                 geometry.Polygon(
                    [(3, 3, 5), (4, 4, 5), (5, 3, 5), (3, 3, 5)])])
        return geometry.MultiPolygon(
            [geometry.Polygon([(0, 0), (1, 1), (2, 1), (0, 0)]),
             geometry.Polygon([(3, 3), (4, 4), (5, 3), (3, 3)])])

    def getGeometryCollection(self):
        return geometry.collection.GeometryCollection([
            self.getPoint(),
            self.getMultiPoint(),
            self.getLineString(),
            self.getMultiLineString(),
            self.getPolygon(),
            self.getMultiPolygon()
        ])

    def assertSpatialReference(self, geometry, wkid):
        if wkid:
            self.assertEqual(
                geometry['spatialReference']['wkid'],
                2056)
        else:
            self.assertNotIn('spatialReference', geometry)

    def assertPoint(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(geometry['x'], 0)
        self.assertEqual(geometry['y'], 1)
        if hasZ:
            self.assertEqual(geometry['z'], 5)
        self.assertSpatialReference(geometry, wkid)

    def assertMultiPoint(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['points']), 2)
        self.assertEqual(geometry['points'][0][0], 0)
        self.assertEqual(geometry['points'][0][1], 1)
        self.assertEqual(geometry['points'][1][0], 1)
        self.assertEqual(geometry['points'][1][1], 2)
        if hasZ:
            self.assertEqual(len(geometry['points']), 2)
            self.assertEqual(geometry['points'][0][2], 5)
            self.assertEqual(geometry['points'][1][2], 5)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['points'][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertLineString(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(geometry['paths'][0][0][0], 0)
        self.assertEqual(geometry['paths'][0][0][1], 0)
        self.assertEqual(geometry['paths'][0][1][0], 1)
        self.assertEqual(geometry['paths'][0][1][1], 1)
        if hasZ:
            self.assertEqual(geometry['paths'][0][0][2], 5)
            self.assertEqual(geometry['paths'][0][1][2], 5)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['paths'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertMultiLineString(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['paths']), 2)
        self.assertEqual(geometry['paths'][0][0][0], 0)
        self.assertEqual(geometry['paths'][0][0][1], 0)
        self.assertEqual(geometry['paths'][0][1][0], 1)
        self.assertEqual(geometry['paths'][0][1][1], 1)
        self.assertEqual(geometry['paths'][1][0][0], -1)
        self.assertEqual(geometry['paths'][1][0][1], 0)
        self.assertEqual(geometry['paths'][1][1][0], 1)
        self.assertEqual(geometry['paths'][1][1][1], 0)
        if hasZ:
            self.assertEqual(geometry['paths'][0][0][2], 5)
            self.assertEqual(geometry['paths'][0][1][2], 5)
            self.assertEqual(geometry['paths'][1][0][2], 6)
            self.assertEqual(geometry['paths'][1][1][2], 6)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['paths'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertPolygon(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['rings']), 1)
        self.assertEqual(len(geometry['rings'][0]), 4)
        self.assertEqual(geometry['rings'][0][0][0], 0)
        self.assertEqual(geometry['rings'][0][0][1], 0)
        self.assertEqual(geometry['rings'][0][1][0], 1)
        self.assertEqual(geometry['rings'][0][1][1], 1)
        self.assertEqual(geometry['rings'][0][2][0], 2)
        self.assertEqual(geometry['rings'][0][2][1], 1)
        self.assertEqual(geometry['rings'][0][3][0], 0)
        self.assertEqual(geometry['rings'][0][3][1], 0)
        if hasZ:
            self.assertEqual(geometry['rings'][0][0][2], 5)
            self.assertEqual(geometry['rings'][0][1][2], 5)
            self.assertEqual(geometry['rings'][0][2][2], 5)
            self.assertEqual(geometry['rings'][0][3][2], 5)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['rings'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertMultiPolygon(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['rings']), 2)
        self.assertEqual(len(geometry['rings'][0]), 4)
        self.assertEqual(geometry['rings'][0][0][0], 0)
        self.assertEqual(geometry['rings'][0][0][1], 0)
        self.assertEqual(geometry['rings'][0][1][0], 1)
        self.assertEqual(geometry['rings'][0][1][1], 1)
        self.assertEqual(geometry['rings'][0][2][0], 2)
        self.assertEqual(geometry['rings'][0][2][1], 1)
        self.assertEqual(geometry['rings'][0][3][0], 0)
        self.assertEqual(geometry['rings'][0][3][1], 0)
        self.assertEqual(geometry['rings'][1][0][0], 3)
        self.assertEqual(geometry['rings'][1][0][1], 3)
        self.assertEqual(geometry['rings'][1][1][0], 4)
        self.assertEqual(geometry['rings'][1][1][1], 4)
        self.assertEqual(geometry['rings'][1][2][0], 5)
        self.assertEqual(geometry['rings'][1][2][1], 3)
        self.assertEqual(geometry['rings'][1][3][0], 3)
        self.assertEqual(geometry['rings'][1][3][1], 3)
        if hasZ:
            self.assertEqual(geometry['rings'][0][0][2], 5)
            self.assertEqual(geometry['rings'][0][1][2], 5)
            self.assertEqual(geometry['rings'][0][2][2], 5)
            self.assertEqual(geometry['rings'][0][3][2], 5)
            self.assertEqual(geometry['rings'][1][0][2], 5)
            self.assertEqual(geometry['rings'][1][1][2], 5)
            self.assertEqual(geometry['rings'][1][2][2], 5)
            self.assertEqual(geometry['rings'][1][3][2], 5)
        else:
            self.assertEqual(len(geometry['rings'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertToShape(self, first_shp, esri_spec, esri_spec_copy):
        shp = to_shape(esri_spec)
        shp_copy = to_shape(esri_spec_copy)
        self.assertEqual(
            getattr(first_shp, '__geo_interface__'),
            getattr(shp, '__geo_interface__'))
        self.assertEqual(
            getattr(first_shp, '__geo_interface__'),
            getattr(shp_copy, '__geo_interface__'))


class TestCodec(BaseTestClass):

    def test_codecs(self):
        # we use sort keys for tests to compare strings
        geom = self.getPoint()
        geom_json = dumps(geom, sort_keys=True)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"x": 0.0, "y": 1.0}')
        self.assertPoint(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getPoint(hasZ=True)
        geom_json = dumps(geom, sort_keys=True)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"x": 0.0, "y": 1.0, "z": 5.0}')
        self.assertPoint(geom_esri, hasZ=True)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getMultiPoint()
        geom_json = dumps(geom, sort_keys=True)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"points": [[0.0, 1.0], [1.0, 2.0]]}')
        self.assertMultiPoint(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getLineString()
        geom_json = dumps(geom, sort_keys=True)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"paths": [[[0.0, 0.0], [1.0, 1.0]]]}')
        self.assertLineString(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getMultiLineString()
        geom_json = dumps(geom, sort_keys=True)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"paths": ' +
                                    '[[[0.0, 0.0], [1.0, 1.0]], ' +
                                    '[[-1.0, 0.0], [1.0, 0.0]]]}')
        self.assertMultiLineString(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getPolygon()
        geom_json = dumps(geom, sort_keys=True)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"rings": [[[0.0, 0.0], [1.0, 1.0], ' +
                                    '[2.0, 1.0], [0.0, 0.0]]]}')
        self.assertPolygon(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getMultiPolygon()
        geom_json = dumps(geom, sort_keys=True)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"rings": [[[0.0, 0.0], [1.0, 1.0], ' +
                                    '[2.0, 1.0], [0.0, 0.0]], ' +
                                    '[[3.0, 3.0], [4.0, 4.0], ' +
                                    '[5.0, 3.0], [3.0, 3.0]]]}')
        self.assertMultiPolygon(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        feat = Feature(attributes={'a': 'a'}, geometry=geom, wkid=2056)
        feat_json = dumps(feat, sort_keys=True)
        feat_esri = loads(feat_json)
        self.assertEqual(feat_json, '{"attributes": {"a": "a"}, ' +
                                    '"geometry": {"rings": [[[0.0, 0.0], ' +
                                    '[1.0, 1.0], [2.0, 1.0], [0.0, 0.0]], ' +
                                    '[[3.0, 3.0], [4.0, 4.0], [5.0, 3.0], ' +
                                    '[3.0, 3.0]]], ' +
                                    '"spatialReference": {"wkid": 2056}}}')
        self.assertMultiPolygon(feat_esri['geometry'], wkid=2056)
        self.assertIsInstance(feat_esri, Feature)

        feat = Feature(attributes={'x': 'a'}, geometry=geom, wkid=2056)
        feat_json = dumps(feat, sort_keys=True)
        feat_esri = loads(feat_json)
        self.assertIsInstance(feat_esri, Feature)


class TestFeature(BaseTestClass):

    def test_point(self):
        point = self.getPoint()
        esri_spec = Feature(geometry=point)
        self.assertPoint(esri_spec['geometry'])

        point = self.getPoint(hasZ=True)
        esri_spec = Feature(geometry=point)
        self.assertPoint(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=point, wkid=2056)
        self.assertPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertPoint(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(point, esri_spec, esri_spec_copy)

    def test_multipoint(self):
        multipoint = self.getMultiPoint()
        esri_spec = Feature(geometry=multipoint)
        self.assertMultiPoint(esri_spec['geometry'])

        multipoint = self.getMultiPoint(hasZ=True)
        esri_spec = Feature(geometry=multipoint)
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=multipoint, wkid=2056)
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multipoint, esri_spec, esri_spec_copy)

    def test_linestring(self):
        linestring = self.getLineString()
        esri_spec = Feature(geometry=linestring)
        self.assertLineString(esri_spec['geometry'])

        linestring = self.getLineString(hasZ=True)
        esri_spec = Feature(geometry=linestring)
        self.assertLineString(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=linestring, wkid=2056)
        self.assertLineString(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertLineString(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(linestring, esri_spec, esri_spec_copy)

    def test_multilinestring(self):
        multilinestring = self.getMultiLineString()
        esri_spec = Feature(geometry=multilinestring)
        self.assertMultiLineString(esri_spec['geometry'])

        multilinestring = self.getMultiLineString(hasZ=True)
        esri_spec = Feature(geometry=multilinestring)
        self.assertMultiLineString(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=multilinestring, wkid=2056)
        self.assertMultiLineString(
            esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertMultiLineString(
            esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multilinestring, esri_spec, esri_spec_copy)

    def test_polygon(self):
        # Coordinates are oriented clock-wise
        polygon = self.getPolygon()
        esri_spec = Feature(geometry=polygon)
        self.assertPolygon(esri_spec['geometry'])

        polygon = self.getPolygon(hasZ=True)
        esri_spec = Feature(geometry=polygon)
        self.assertPolygon(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=polygon, wkid=2056)
        self.assertPolygon(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertPolygon(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(polygon, esri_spec, esri_spec_copy)

    def test_multipolygon(self):
        multipolygon = self.getMultiPolygon()
        esri_spec = Feature(geometry=multipolygon)
        self.assertMultiPolygon(esri_spec['geometry'])

        multipolygon = self.getMultiPolygon(hasZ=True)
        esri_spec = Feature(geometry=multipolygon)
        self.assertMultiPolygon(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=multipolygon, wkid=2056)
        self.assertMultiPolygon(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertMultiPolygon(
            esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multipolygon, esri_spec, esri_spec_copy)

    def test_geometrycollection(self):
        geomcollection = geometry.GeometryCollection([self.getPoint(),
                                                      self.getPolygon()])
        esri_spec = Feature(geometry=geomcollection)
        self.assertPoint(esri_spec['geometry'])

    def test_bbox(self):
        bbox = geometry.box(1, 1, 2, 2)
        esri_spec = {'xmin': 1, 'ymin': 1, 'xmax': 2, 'ymax': 2}
        esri_spec_alt = [1, 1, 2, 2]
        self.assertToShape(bbox, esri_spec, esri_spec_alt)
        bbox = geometry.box(1, 1, 2, 2)
        esri_spec = {'xmin': 1, 'ymin': 1, 'xmax': 2, 'ymax': 2}
        esri_spec_alt = [2, 2, 1, 1]
        self.assertToShape(bbox, esri_spec, esri_spec_alt)
        bbox = geometry.box(1, 2, 3, 4)
        esri_spec = {'xmin': 1, 'ymin': 2, 'xmax': 3, 'ymax': 4}
        esri_spec_alt = [3, 2, 1, 4]
        self.assertToShape(bbox, esri_spec, esri_spec_alt)
        bbox = geometry.box(1, 2, 3, 4)
        esri_spec = {'xmin': 1, 'ymin': 2, 'xmax': 3, 'ymax': 4}
        esri_spec_alt = [1, 4, 3, 2]
        self.assertToShape(bbox, esri_spec, esri_spec_alt)

    def test_extra(self):
        polygon = self.getPolygon()
        esri_spec = Feature(geometry=polygon,
                            attributes={'name': 'a', 'number': 1},
                            id=2,
                            bbox=[1, 2, 4, 7])
        self.assertPolygon(esri_spec['geometry'])
        self.assertEqual(esri_spec['attributes']['name'], 'a')
        self.assertEqual(esri_spec['attributes']['number'], 1)
        self.assertEqual(esri_spec['id'], 2)
        self.assertEqual(esri_spec['bbox'][0], 1)
        self.assertEqual(esri_spec['bbox'][1], 2)
        self.assertEqual(esri_spec['bbox'][2], 4)
        self.assertEqual(esri_spec['bbox'][3], 7)
