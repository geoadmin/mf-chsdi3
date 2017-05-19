# -*- coding: utf-8 -*-

import os
import requests
import time
from chsdi.tests.integration import TestsBase

from chsdi.tests.integration.test_file_storage import VALID_KML, NOT_WELL_FORMED_KML


class TestVarnish(TestsBase):

    ''' Testing the Varnish 'security' configuration. As some settings are IP address dependant,
        we use an external HTTP Proxy to make the queries.
    '''

    def hash(self, bits=96):
        assert bits % 8 == 0
        return os.urandom(bits / 8).encode('hex')

    def timestamp(self):
        return int(round(time.time() * 1000.0))

    def setUp(self):
        super(TestVarnish, self).setUp()
        self.registry = self.testapp.app.registry

        try:
            os.environ["http_proxy"] = self.registry.settings['http_proxy']
            self.api_url = 'http:%s' % self.registry.settings['api_url']
            self.alti_url = 'http:%s' % self.registry.settings['alti_url']
            self.mapproxy_url = 'http://' + self.registry.settings['mapproxyhost'] + '/'
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


class TestLocation(TestVarnish):

    def test_locations_no_referer(self):

        payload = {'type': 'locations', 'searchText': 'fontenay 10 lausanne', '_id': self.hash()}
        r = requests.get(self.api_url + '/rest/services/api/SearchServer', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        returned_attrs = r.json()['results'][0]['attrs'].keys()

        self.assertNotIn('geom_st_box2d', r.json()['results'][0]['attrs'])
        self.assertEqual(self.has_geometric_attributes(returned_attrs), False)

    def test_locations_good_referer(self):

        payload = {'type': 'locations', 'searchText': 'fontenay 10 lausanne', '_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}

        r = requests.get(self.api_url + '/rest/services/api/SearchServer', params=payload, headers=headers)

        returned_attrs = r.json()['results'][0]['attrs'].keys()

        self.assertIn('geom_st_box2d', r.json()['results'][0]['attrs'])
        self.assertEqual(self.has_geometric_attributes(returned_attrs), True)

    def test_location_cached_no_referer(self):

        payload = {'type': 'locations', 'searchText': 'fontenay 10 lausanne'}
        r = requests.get(self.api_url + '/%d/rest/services/api/SearchServer' % self.timestamp(), params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        returned_attrs = r.json()['results'][0]['attrs'].keys()

        self.assertNotIn('geom_st_box2d', r.json()['results'][0]['attrs'])
        self.assertEqual(self.has_geometric_attributes(returned_attrs), False)

    def test_location_cached_good_referer(self):

        payload = {'type': 'locations', 'searchText': 'fontenay 10 lausanne'}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}

        r = requests.get(self.api_url + '/%d/rest/services/api/SearchServer' % self.timestamp(), params=payload, headers=headers)

        returned_attrs = r.json()['results'][0]['attrs'].keys()

        self.assertIn('geom_st_box2d', r.json()['results'][0]['attrs'])
        self.assertEqual(self.has_geometric_attributes(returned_attrs), True)


class TestGebaeude(TestVarnish):

    ''' Results with layer 'ch.bfs.gebaeude_wohnungs_register' should never return a geometry
        for invalid referers

        See https://github.com/geoadmin/mf-chsdi3/issues/886
    '''

    def test_gebaude_no_referer(self):

        payload = {'_id': self.hash()}
        r = requests.get(self.api_url + '/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/490830_0', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertNotIn('geometry', r.json()['feature'].keys())

    def test_find_gebaude_no_referer(self):

        payload = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': 'berges', 'searchField': 'strname1', '_id': self.hash()}
        r = requests.get(self.api_url + '/rest/services/ech/MapServer/find', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertNotIn('geometry', r.json()['results'][0].keys())

    def test_gebaude_good_referer(self):

        payload = {'type': 'location', 'searchText': 'dorf', '_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}

        r = requests.get(self.api_url + '/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/490830_0', params=payload, headers=headers)

        self.assertIn('geometry', r.json()['feature'].keys())

    def test_find_gebaude_good_referer(self):

        payload = {'layer': 'ch.bfs.gebaeude_wohnungs_register', 'searchText': 'berges', 'searchField': 'strname1', '_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}
        r = requests.get(self.api_url + '/rest/services/ech/MapServer/find', params=payload, headers=headers)

        self.assertIn('geometry', r.json()['results'][0].keys())


class TestMapproxyGetTile(TestVarnish):

    ''' See https://github.com/geoadmin/mf-chsdi3/issues/873
    '''

    def test_mapproxy_no_referer(self):

        payload = {'_id': self.hash()}

        resp = requests.get(self.mapproxy_url + '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/13/4265/2883.jpeg', params=payload, headers={'User-Agent': 'mf-geoadmin/python'})

        self.assertEqual(resp.status_code, 403)

    def test_mapproxy_bad_referer(self):

        payload = {'_id': self.hash()}
        headers = {'referer': 'http://gooffy-referer.ch', 'User-Agent': 'mf-geoadmin/python'}

        resp = requests.get(self.mapproxy_url + '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/13/4265/2883.jpeg', params=payload, headers=headers)

        self.assertEqual(resp.status_code, 403)

    def test_mapproxy_good_referer(self):

        payload = {'_id': self.hash()}
        headers = {'referer': 'http://unittest.geo.admin.ch', 'User-Agent': 'mf-geoadmin/python'}

        resp = requests.get(self.mapproxy_url + '/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/13/4265/2883.jpeg', params=payload, headers=headers)

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
