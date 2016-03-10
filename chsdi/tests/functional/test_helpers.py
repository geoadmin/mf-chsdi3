# -*- coding: utf-8 -*-

import unittest
from pyramid import testing
from pyramid.threadlocal import get_current_registry
from chsdi.lib.helpers import (
    make_agnostic, make_api_url, check_url, transformCoordinate, sanitize_url,
    check_even, format_search_text, remove_accents, escape_sphinx_syntax,
    quoting, float_raise_nan, resource_exists, parseHydroXML, locale_negotiator,
    versioned, parse_box2d, center_from_box2d, format_scale, format_price,
    parse_date_string, parse_date_datenstand
)
from urlparse import urljoin


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

        test_path2 = 'http://dummy.com'
        test_result2 = resource_exists(test_path2)
        self.assertTrue(test_result2)

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
        try:
            check_url(url, config)
        except Exception as e:
            self.assertTrue(isinstance(e, HTTPBadRequest))

        url = 'dummy'
        try:
            check_url(url, config)
        except Exception as e:
            self.assertTrue(isinstance(e, HTTPBadRequest))

        url = 'http://dummy.com'

        try:
            check_url(url, config)
        except Exception as e:
            self.assertTrue(isinstance(e, HTTPBadRequest))

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
        request.accept_language = False  # I cannot check line 95
        test_result3 = locale_negotiator(request)
        self.assertTrue(test_result3, 'en')

    def test_sanitize_url_throws_ValueError(self):
        # ValueError
        url2 = None
        result2 = sanitize_url(url2)
        self.assertRaises(ValueError, result2)

    def test_parseHydroXML(self):
        import xml.etree.ElementTree as ET

        tree = ET.parse('chsdi/tests/functional/filename.xml')
        root = tree.getroot()
        test_result = parseHydroXML('idname', root)
        self.assertEqual({'date_time': '01 September 8Uhr', 'wasserstand': '-', 'wassertemperatur': '-', 'abfluss': '141100'}, test_result)

        tree2 = ET.parse('chsdi/tests/functional/filename2.xml')
        root2 = tree2.getroot()
        test_result2 = parseHydroXML('idname', root2)
        self.assertEqual({'date_time': '04 Oktober 11 Uhr', 'wasserstand': '59900', 'wassertemperatur': '-', 'abfluss': '-'}, test_result2)

        tree3 = ET.parse('chsdi/tests/functional/filename3.xml')
        root3 = tree3.getroot()
        test_result3 = parseHydroXML('idname', root3)
        self.assertEqual({'date_time': '16 Mai 18 Uhr', 'wasserstand': '-', 'wassertemperatur': '59900', 'abfluss': '-'}, test_result3)

    def test_transformCoordinate(self):
        from osgeo.ogr import Geometry
        wkt = 'POINT (7.37840 45.91616)'
        srid_from = 4326
        srid_to = 21781
        wkt_21781 = transformCoordinate(wkt, srid_from, srid_to)
        self.assertTrue(isinstance(wkt_21781, Geometry))
        self.assertEqual(int(wkt_21781.GetX()), 595324)
        self.assertEqual(int(wkt_21781.GetY()), 84952)

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
        self.assertRaises('ValueError')

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
        try:
            center_from_box2d(box2d)
        except ValueError as e:
            self.assertRaises(e)

    def test_format_scale(self):
        scale = 50000
        result = format_scale(scale)
        self.assertEqual(result, "1:50'000")

    def test_format_price(self):
        price = 1400
        result = format_price(price)
        self.assertEqual(result, "CHF 14.00")

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
