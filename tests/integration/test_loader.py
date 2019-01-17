# -*- coding: utf-8 -*-

from tests.integration import TestsBase


class TestLoaderJs(TestsBase):
    default_version = '4.4.2'

    def test_loaderjs(self):
        resp = self.testapp.get('/loader.js', status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/{}/ga.js'.format(self.default_version))
        resp.mustcontain('resources/api/{}/ga.css'.format(self.default_version))
        resp.mustcontain('resources/api/{}/EPSG21781.js'.format(self.default_version))
        resp.mustcontain('resources/api/{}/EPSG2056.js'.format(self.default_version))
        resp.mustcontain('proj4.js')

    def test_loaderjs_lang(self):
        resp = self.testapp.get('/loader.js', params={'lang': 'fr'}, status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/{}/ga.js'.format(self.default_version))
        resp.mustcontain('resources/api/{}/ga.css'.format(self.default_version))
        resp.mustcontain('resources/api/{}/EPSG21781.js'.format(self.default_version))
        resp.mustcontain('resources/api/{}/EPSG2056.js'.format(self.default_version))
        resp.mustcontain('proj4.js')
        # We use french, as word in English or German maybe found in layers'attributes.
        self.assertTrue(resp.body.count('eau') >= 1)

    def test_loaderjs_debug(self):
        resp = self.testapp.get('/loader.js', params={'mode': 'debug'}, status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/{}/ga-debug.js'.format(self.default_version))
        resp.mustcontain('resources/api/{}/ga.css'.format(self.default_version))
        resp.mustcontain('resources/api/{}/EPSG21781.js'.format(self.default_version))
        resp.mustcontain('resources/api/{}/EPSG2056.js'.format(self.default_version))
        resp.mustcontain('proj4.js')

    def test_loaderjs_version(self):
        version = '3.18.2'
        resp = self.testapp.get('/loader.js', params={'version': version}, status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/{}/ga.js'.format(version))
        resp.mustcontain('resources/api/{}/ga.css'.format(version))
        resp.mustcontain('resources/api/{}/EPSG21781.js'.format(version))
        resp.mustcontain('resources/api/{}/EPSG2056.js'.format(version))
        resp.mustcontain('proj4.js')

    def test_loaderjs_bad_version(self):
        self.testapp.get('/loader.js', params={'version': '3.666'}, status=404)
