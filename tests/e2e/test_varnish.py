# -*- coding: utf-8 -*-

from past.utils import old_div

import os
import requests
import time
from tests.integration import TestsBase

from tests.integration.test_file_storage import VALID_KML, NOT_WELL_FORMED_KML


class TestVarnish(TestsBase):

    ''' Testing the Varnish 'security' configuration. As some settings are IP address dependant,
        we use an external HTTP Proxy to make the queries.
    '''

    def hash(self, bits=96):
        assert bits % 8 == 0
        try:
            hexstr = os.urandom(old_div(bits ,8)).hex()
        except AttributeError:
            hexstr = os.urandom(old_div(bits ,8)).encode('hex')
        return hexstr

    def timestamp(self):
        return int(round(time.time() * 1000.0))

    def setUp(self):
        super(TestVarnish, self).setUp()
        self.registry = self.testapp.app.registry

        try:
            os.environ["http_proxy"] = self.registry.settings['http_proxy']
            self.api_url = 'http:%s' % self.registry.settings['api_url']
            self.alti_url = 'http:%s' % self.registry.settings['alti_url']
            self.wmts_public_host = 'http://' + self.registry.settings['wmts_public_host'] + '/'
        except KeyError as e:
            raise e

    def tearDown(self):
        if "http_proxy" in os.environ:
            del os.environ["http_proxy"]
        super(TestVarnish, self).tearDown()

    def has_geometric_attributes(self, attrs):
        geometric_attrs = ['x', 'y', 'lon', 'lat', 'geom_st_box2d']
        return len(set(geometric_attrs).intersection(attrs)) > 0


class TestHeight(TestVarnish):

    def test_height_no_referer(self):

        payload = {'easting': 600000.0, 'northing': 200000.0, '_id': self.hash()}
        resp = requests.get(self.alti_url + '/rest/services/height', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertEqual(resp.status_code, 403)

    def test_height_good_referer(self):

        payload = {'easting': 600000.0, 'northing': 200000.0, '_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        resp = requests.get(self.alti_url + '/rest/services/height', params=payload, headers=headers)

        self.assertEqual(resp.status_code, 200)


class TestProfile(TestVarnish):

    def test_profile_json_no_referer(self):

        payload = {'geom': '{"type":"LineString","coordinates":[[550050,206550],[556950,204150],[561050,207950]]}', '_id': self.hash()}
        resp = requests.get(self.alti_url + '/rest/services/profile.json', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertEqual(resp.status_code, 403)

    def test_profile_json_good_referer(self):

        payload = {'geom': '{"type":"LineString","coordinates":[[550050,206550],[556950,204150],[561050,207950]]}', '_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        resp = requests.get(self.alti_url + '/rest/services/profile.json', params=payload, headers=headers)

        self.assertEqual(resp.status_code, 200)

    def test_profile_csv_no_referer(self):

        payload = {'geom': '{"type":"LineString","coordinates":[[550050,206550],[556950,204150],[561050,207950]]}', '_id': self.hash()}
        resp = requests.get(self.alti_url + '/rest/services/profile.csv', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertEqual(resp.status_code, 403)

    def test_profile_csv_good_referer(self):

        payload = {'geom': '{"type":"LineString","coordinates":[[550050,206550],[556950,204150],[561050,207950]]}', '_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        resp = requests.get(self.alti_url + '/rest/services/profile.csv', params=payload, headers=headers)

        self.assertEqual(resp.status_code, 200)


class TestMapproxyGetTile(TestVarnish):

    ''' See https://github.com/geoadmin/mf-chsdi3/issues/873
    '''

    def test_mapproxy_no_referer(self):

        payload = {'_id': self.hash()}

        resp = requests.get(self.wmts_public_host + '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/13/4265/2883.jpeg', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertEqual(resp.status_code, 403)

    def test_mapproxy_bad_referer(self):

        payload = {'_id': self.hash()}
        headers = {'referer': 'http://gooffy-referer.ch', 'User-Agent': 'mf-geoadmin/python'}

        resp = requests.get(self.wmts_public_host + '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/13/4265/2883.jpeg', params=payload, headers=headers)

        self.assertEqual(resp.status_code, 403)

    def test_mapproxy_good_referer(self):

        payload = {'_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}

        resp = requests.get(self.wmts_public_host + '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/13/4265/2883.jpeg', params=payload, headers=headers)

        self.assertEqual(resp.status_code, 200)


class TestFilestorage(TestVarnish):

    def test_post_filestorage_no_referer(self):

        resp = requests.post(self.api_url + '/files', VALID_KML, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertEqual(resp.status_code, 403)

    def test_post_filestorage_good_referer(self):

        headers = {'Content-Type': 'application/vnd.google-earth.kml+xml', 'Referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        resp = requests.post(self.api_url + '/files', VALID_KML, headers=headers)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('adminId', resp.json())
        self.assertIn('fileId', resp.json())

    def test_post_filestorage_wrong_referer(self):

        headers = {'Content-Type': 'application/vnd.google-earth.kml+xml', 'Referer': 'http://foo.bar', 'User-Agent': 'mf-geaodmin/python'}
        resp = requests.post(self.api_url + '/files', VALID_KML, headers=headers)

        self.assertEqual(resp.status_code, 403)

    def test_post_filestorage_wrong_content_type(self):

        headers = {'Content-Type': 'application/xml', 'Referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        resp = requests.post(self.api_url + '/files', VALID_KML, headers=headers)

        self.assertEqual(resp.status_code, 415)

    def test_post_filestorage_not_well_formed(self):

        headers = {'Content-Type': 'application/vnd.google-earth.kml+xml', 'Referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        resp = requests.post(self.api_url + '/files', NOT_WELL_FORMED_KML, headers=headers)

        self.assertEqual(resp.status_code, 415)

    def test_post_filestorage_too_big(self):

        headers = {'Content-Type': 'application/vnd.google-earth.kml+xml', 'Referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_dir, '../integration', 'big.kml')) as f:
            data = f.read()

        resp = requests.post(self.api_url + '/files', data, headers=headers)

        self.assertEqual(resp.status_code, 413)
