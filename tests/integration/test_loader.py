# -*- coding: utf-8 -*-

from tests.integration import TestsBase


class TestLoaderJs(TestsBase):

    def test_loaderjs(self):
        resp = self.testapp.get('/loader.js', status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/3.6.0/ga.js')
        resp.mustcontain('resources/api/3.6.0/ga.css')
        resp.mustcontain('resources/api/3.6.0/EPSG21781.js')
        resp.mustcontain('resources/api/3.6.0/EPSG2056.js')
        resp.mustcontain('proj4.js')
        resp.mustcontain('proj4.js')

    def test_loaderjs_lang(self):
        resp = self.testapp.get('/loader.js', params={'lang': 'en'}, status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/3.6.0/ga.js')
        resp.mustcontain('resources/api/3.6.0/ga.css')
        resp.mustcontain('resources/api/3.6.0/EPSG21781.js')
        resp.mustcontain('resources/api/3.6.0/EPSG2056.js')
        resp.mustcontain('proj4.js')

    def test_loaderjs_debug(self):
        resp = self.testapp.get('/loader.js', params={'mode': 'debug'}, status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/3.6.0/ga-debug.js')
        resp.mustcontain('resources/api/3.6.0/ga.css')
        resp.mustcontain('resources/api/3.6.0/EPSG21781.js')
        resp.mustcontain('resources/api/3.6.0/EPSG2056.js')
        resp.mustcontain('proj4.js')

    def test_loaderjs_version(self):
        resp = self.testapp.get('/loader.js', params={'version': '3.18.2'}, status=200)
        self.assertTrue(resp.content_type, 'application/javascript')
        resp.mustcontain('resources/api/3.18.2/ga.js')
        resp.mustcontain('resources/api/3.18.2/ga.css')
        resp.mustcontain('resources/api/3.18.2/EPSG21781.js')
        resp.mustcontain('resources/api/3.18.2/EPSG2056.js')
        resp.mustcontain('proj4.js')

    def test_loaderjs_bad_version(self):
        self.testapp.get('/loader.js', params={'version': '3.666'}, status=404)
