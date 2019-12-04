# -*- coding: utf-8 -*-

import unittest
from pyramid import testing
from pyramid.threadlocal import get_current_registry
from chsdi.lib.helpers import (
    make_agnostic, make_api_url, check_url, sanitize_url, _transform_point,
    check_even, format_search_text, remove_accents, escape_sphinx_syntax,
    quoting, float_raise_nan, resource_exists, parseHydroXML, locale_negotiator,
    versioned, parse_box2d, center_from_box2d, format_scale,
    parse_date_string, parse_date_datenstand, int_with_apostrophe, get_loaderjs_url,
    get_proj_from_srid, get_precision_for_proj, _round_bbox_coordinates, _round_shape_coordinates,
    round_geometry_coordinates, _transform_coordinates, _transform_shape, transform_round_geometry
)
from shapely.geometry import Point, Polygon
from shapely.geometry import mapping
from numpy.testing import assert_almost_equal

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class Test_Helpers(unittest.TestCase):

    def test_versioned(self):
        registry = get_current_registry()

        registry.settings = {}

        registry.settings['app_version'] = None
        registry.settings['entry_path'] = '/ltxxx'
        path = 'https://api3.geo.admin.ch/ltxxx'
        versioned_path = versioned(path)
        self.assertEqual(path, versioned_path)

        registry.settings['app_version'] = '1234'
        registry.settings['entry_path'] = '/ltxxx'
        path = 'https://api3.geo.admin.ch/ltxxx/?dummy=toto'
        versioned_path = versioned(path)
        self.assertEqual(versioned_path, '//api3.geo.admin.ch/ltxxx/1234/?dummy=toto')

    def test_make_agnostic(self):
        url = 'http://foo.com'
        agnostic_link = make_agnostic(url)
        self.assertTrue(not agnostic_link.startswith('http://'))
        self.assertTrue(agnostic_link.startswith('//'))

        url_2 = 'https://foo.com'
        agnostic_link_2 = make_agnostic(url_2)
        self.assertTrue(not agnostic_link_2.startswith('https://'))
        self.assertTrue(agnostic_link_2.startswith('//'))

        url_3 = '//foo.com'
        agnostic_link_3 = make_agnostic(url_3)
        self.assertEqual(url_3, agnostic_link_3)

    def test_resource_exists(self):
        test_path = 'https://api3.geo.admin.ch'
        test_result = resource_exists(test_path)
        self.assertTrue(test_result)

        test_path2 = 'http://junodummyducolozouzlouwioiii.ch'
        test_result2 = resource_exists(test_path2)
        self.assertFalse(test_result2)

    def test_make_api_url(self):
        request = testing.DummyRequest()
        request.host = 'api3.geo.admin.ch'
        request.scheme = 'http'
        request.registry.settings = {}
        request.registry.settings['apache_base_path'] = 'main'
        api_url = make_api_url(request, agnostic=True)
        self.assertTrue(not api_url.startswith('http://'))
        self.assertTrue(api_url.startswith('//'))
        self.assertEqual(api_url, '//api3.geo.admin.ch')

        request.scheme = 'https'
        api_url = make_api_url(request)
        self.assertEqual(api_url, 'https://api3.geo.admin.ch')

        request.host = 'localhost:9000'
        request.scheme = 'http'
        api_url = make_api_url(request)
        self.assertEqual(api_url, api_url)

    def test_check_url(self):
        from pyramid.httpexceptions import HTTPBadRequest
        url = None
        config = {'shortener.allowed_hosts': 'admin.ch,swisstopo.ch,bgdi.ch'}
        with self.assertRaises(HTTPBadRequest):
            check_url(url, config)

        url = 'dummy'
        with self.assertRaises(HTTPBadRequest):
            check_url(url, config)

        url = 'http://dummy.ch'
        with self.assertRaises(HTTPBadRequest):
            check_url(url, config)

        url = 'http://admin.ch'
        self.assertEqual(url, check_url(url, config))

    def test_sanitize_url(self):
        base_url_string = 'http://somehost.com/some/path/here'
        relative_url_string = 'http://somehost.com/some/other/path'
        result1 = sanitize_url(base_url_string)
        self.assertEqual(result1, base_url_string)

        result2 = sanitize_url(relative_url_string)
        self.assertEqual(result2, relative_url_string)

        self.assertNotEqual(result1, urljoin(base_url_string, relative_url_string))

        self.assertEqual(result2, urljoin(base_url_string, relative_url_string))

    def test_local_negotiator(self):
        request = testing.DummyRequest()
        request.host = 'api3.geo.admin.ch'
        request.scheme = 'http'
        request.registry.settings = {}
        request.registry.settings['apache_base_path'] = 'main'
        request.registry.settings['available_languages'] = 'fr de it rm en'

        request.params['lang'] = 'de'
        test_result = locale_negotiator(request)
        self.assertTrue(test_result, 'de')

        request.params['lang'] = 'rm'
        test_result2 = locale_negotiator(request)
        self.assertTrue(test_result2, 'fi')

        request.params['lang'] = None
        request.accept_language = False
        test_result3 = locale_negotiator(request)
        self.assertTrue(test_result3, 'en')

    def test_sanitize_url_throws_ValueError(self):
        # ValueError
        url2 = None
        res2 = sanitize_url(url2)
        self.assertEqual(url2, res2)

    def test_parseHydroXML(self):
        import xml.etree.ElementTree as ET

        tree = ET.parse('tests/functional/filename.xml')
        root = tree.getroot()
        test_result = parseHydroXML('idname', root)
        self.assertEqual({'date_time': '01 September 8Uhr', 'wasserstand': '-', 'wassertemperatur': '-', 'abfluss': '141100'}, test_result)

        tree2 = ET.parse('tests/functional/filename2.xml')
        root2 = tree2.getroot()
        test_result2 = parseHydroXML('idname', root2)
        self.assertEqual({'date_time': '04 Oktober 11 Uhr', 'wasserstand': '59900', 'wassertemperatur': '-', 'abfluss': '-'}, test_result2)

        tree3 = ET.parse('tests/functional/filename3.xml')
        root3 = tree3.getroot()
        test_result3 = parseHydroXML('idname', root3)
        self.assertEqual({'date_time': '16 Mai 18 Uhr', 'wasserstand': '-', 'wassertemperatur': '59900', 'abfluss': '-'}, test_result3)

    def test_check_even(self):
        testnumber = 10
        result = check_even(testnumber)
        self.assertTrue(result)

        testnumber = 5
        result = check_even(testnumber)
        self.assertFalse(result)

    def test_format_search_text(self):
        testinput_str = 'Hallo!'
        result = format_search_text(testinput_str)
        self.assertEqual(result, 'Hallo\\!')

        testinput_str2 = u'über'
        result2 = format_search_text(testinput_str2)
        self.assertEqual(result2, 'ueber')

    def test_remove_accents(self):
        testinput_str = None
        result = remove_accents(testinput_str)
        self.assertEqual(result, None)

    def test_escape_sphinx_syntax(self):
        testinput_str = None
        result = escape_sphinx_syntax(testinput_str)
        self.assertEqual(result, None)

    def test_quoting(self):
        testtext = 'Hallo'
        result = quoting(testtext)
        self.assertEqual(result, 'Hallo')

    def test_float_raise_nan(self):
        testval = 5
        result = float_raise_nan(testval)
        self.assertEqual(result, 5.0)
        with self.assertRaises(ValueError):
            float_raise_nan(float('nan'))

    def test_parse_box2d(self):
        strBox2d = 'BOX(1.1 2.2,3.3 4.4)'
        box2d = parse_box2d(strBox2d)
        self.assertEqual(box2d[0], 1.1)
        self.assertEqual(box2d[1], 2.2)
        self.assertEqual(box2d[2], 3.3)
        self.assertEqual(box2d[3], 4.4)

    def test_center_from_box2d(self):
        box2d = [1.1, 2.2, 3.3, 6.6]
        center = center_from_box2d(box2d)
        self.assertEqual(center[0], 2.2)
        self.assertEqual(center[1], 4.4)

    def test_center_from_box2d_wrong(self):
        box2d = [10.1, 2.2, 3.3, 6.6]
        with self.assertRaises(ValueError):
            center_from_box2d(box2d)
        box2d = [1.1, 2.2, 3.3]
        with self.assertRaises(ValueError):
            center_from_box2d(box2d)

    def test_format_scale(self):
        scale = 50000
        result = format_scale(scale)
        self.assertEqual(result, "1:50'000")

    def test_parse_date_string(self):
        d = '2014-01-09'
        result = parse_date_string(d)
        self.assertEqual(result, '09.01.2014')
        result = parse_date_string(d, format_output='%Y')
        self.assertEqual(result, '2014')
        rand = '!6ndawkdbuhd'
        result = parse_date_string(rand, format_input='%Y%m', format_output='%m.%Y')
        self.assertEqual(result, '-')

    def test_parse_date_datenstand(self):
        digits4 = '2015'
        result = parse_date_datenstand(digits4)
        self.assertEqual(result, digits4)
        digits6 = '201512'
        result = parse_date_datenstand(digits6)
        self.assertEqual(result, '12.2015')
        digits8 = '20151201'
        result = parse_date_datenstand(digits8)
        self.assertEqual(result, '01.12.2015')
        digits9 = '2014-2015'
        result = parse_date_datenstand(digits9)
        self.assertEqual(result, '2014-2015')
        digits13 = '201412-201501'
        result = parse_date_datenstand(digits13)
        self.assertEqual(result, '12.2014-01.2015')
        digits17 = '20141202-20150112'
        result = parse_date_datenstand(digits17)
        self.assertEqual(result, '02.12.2014-12.01.2015')
        nodata = '-'
        result = parse_date_datenstand(nodata)
        self.assertEqual(result, nodata)
        rand = '!6nhd'
        result = parse_date_datenstand(rand)
        self.assertEqual(result, '-')
        fulldate = '20160208 13:50'
        result = parse_date_datenstand(fulldate)
        self.assertEqual(result, '08.02.2016 13:50')
        fulldate2 = '20160208-13:50'
        result = parse_date_datenstand(fulldate2)
        self.assertEqual(result, '08.02.2016-13:50')

    def test_int_with_apostrophe(self):
        x1 = 'toto'
        result1 = int_with_apostrophe(x1)
        self.assertEqual(result1, '-')
        x2 = -5
        result2 = int_with_apostrophe(x2)
        self.assertEqual(result2, str(x2))

    def test_get_loaderjs_url(self):
        api_url = '//example.com'
        config = testing.setUp()
        config.add_route('ga_api', '/loader.js')
        request = testing.DummyRequest()
        url = get_loaderjs_url(request)
        self.assertEqual(url, '%s/loader.js?version=3.6.0' % api_url)
        url = get_loaderjs_url(request, version='3.18.2')
        self.assertEqual(url, '%s/loader.js?version=3.18.2' % api_url)
        testing.tearDown()

    def test_get_proj_from_srid(self):
        srid = 21781
        proj = get_proj_from_srid(srid)
        self.assertFalse(proj.is_latlong())
        self.assertEqual(proj.srs, '+units=m +init=epsg:21781 ')

    def test__transform_point(self):
        srid_from = 4326
        srid_to = 21781
        coords = _transform_point([7.37840, 45.91616], srid_from, srid_to)
        self.assertEqual(int(coords[0]), 595324)
        self.assertEqual(int(coords[1]), 84952)

    def get_precision_for_proj(self):
        # rounding all coordinates for to about 0.1 meter
        # Lat/Long proj -> precision of 7 decimals
        # Metric proj   -> precision of 1 decimal (obviously)
        self.assertEqual(get_precision_for_proj(2056), 1)
        self.assertEqual(get_precision_for_proj(3857), 1)
        self.assertEqual(get_precision_for_proj(21781), 1)
        self.assertEqual(get_precision_for_proj(4326), 7)

    def test__round_bbox_coordinates(self):
        bbox = [1.1111, 2.2222, 3.33333333, 4.44444444]
        self.assertEqual(_round_bbox_coordinates(bbox, precision=1), [1.1, 2.2, 3.3, 4.4])

    def test__round_shape_coordinates(self):
        point = Point(1.3456, 3.43434)
        point_rounded = _round_shape_coordinates(point, precision=1)
        polygon = Polygon([(0.231, 0.345), (1.4564, 1.1965), (1.38509, 0.97979)])
        polygon_rounded = _round_shape_coordinates(polygon, precision=2)

        self.assertEqual(mapping(point_rounded), {'type': 'Point', 'coordinates': (1.3, 3.4)})
        self.assertNotEqual(mapping(point), {'type': 'Point', 'coordinates': (1.3, 3.4)})
        self.assertEqual(mapping(polygon_rounded), {'coordinates': (((0.23, 0.34), (1.46, 1.2), (1.39, 0.98), (0.23, 0.34)),), 'type': 'Polygon'})
        self.assertNotEqual(mapping(polygon)['coordinates'][0], (0.231, 0.345))

    def test_round_geometry_coordinates(self):
        point = Point(1.3456, 3.43434)
        point_rounded = round_geometry_coordinates(point, precision=1)
        self.assertEqual(mapping(point_rounded), {'type': 'Point', 'coordinates': (1.3, 3.4)})

        bbox = [1.1111, 2.2222, 3.33333333, 4.44444444]
        self.assertEqual(round_geometry_coordinates(bbox, precision=1), [1.1, 2.2, 3.3, 4.4])

    def test__transform_coordinates(self):
        bbox = [2600000, 1200000, 2650000, 1250000]
        bbox_wgs84 = _transform_coordinates(bbox, 2056, 4326, rounding=False)
        bbox_wgs84_rounded = _transform_coordinates(bbox, 2056, 4326, rounding=True)

        self.assertEqual(bbox_wgs84_rounded, [7.438632, 46.951083, 8.100963, 47.398925])
        assert_almost_equal(bbox_wgs84, [7.438632420871815, 46.95108277187108, 8.100963474961302, 47.39892497922299], decimal=10)

    def test_transform_shape(self):
        point = Point(2600000, 120000)
        point_wgs84 = _transform_shape(point, 2056, 4326, rounding=False)
        point_wgs84_rounded = _transform_shape(point, 2056, 4326)

        self.assertEqual(mapping(point_wgs84_rounded), {'type': 'Point', 'coordinates': (7.438767, 37.274227)})
        assert_almost_equal(point_wgs84.coords[0],  (7.438767146513139, 37.27422679580366))

    def test_transform_round_geometry(self):

        bbox = [2600000, 1200000, 2650000, 1250000]
        bbox_wgs84 = transform_round_geometry(bbox, 2056, 4326, rounding=False)
        bbox_wgs84_rounded = transform_round_geometry(bbox, 2056, 4326, rounding=True)

        self.assertEqual(bbox_wgs84_rounded, [7.438632, 46.951083, 8.100963, 47.398925])
        assert_almost_equal(bbox_wgs84, [7.438632420871815, 46.95108277187108, 8.100963474961302, 47.39892497922299], decimal=10)

        point = Point(2600000, 120000)
        point_wgs84 = transform_round_geometry(point, 2056, 4326, rounding=False)
        point_wgs84_rounded = transform_round_geometry(point, 2056, 4326)

        self.assertEqual(mapping(point_wgs84_rounded), {'type': 'Point', 'coordinates': (7.438767, 37.274227)})
        assert_almost_equal(point_wgs84.coords[0], (7.438767146513139, 37.27422679580366), decimal=10)
