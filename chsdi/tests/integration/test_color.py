# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestColorView(TestsBase):

    def setUp(self):
        super(TestColorView, self).setUp()

    def test_color_valid(self):
        resp = self.testapp.get('/color/23,24,25/marker-24@2x.png', None, status=200)
        self.assertEqual(resp.content_type, 'image/png')

    def test_color_bad_r_channel(self):
        resp = self.testapp.get('/color/as,24,25/marker-24@2x.png', None, status=400)
        resp.mustcontain('The red channel must be an integer')

    def test_color_bad_g_channel(self):
        resp = self.testapp.get('/color/25,gfdfg,25/marker-24@2x.png', None, status=400)
        resp.mustcontain('The green channel must be an integer')

    def test_color_bad_b_channel(self):
        resp = self.testapp.get('/color/25,24,dffsd/marker-24@2x.png', None, status=400)
        resp.mustcontain('The blue channel must be an integer')

    def test_color_bad_image_name(self):
        resp = self.testapp.get('/color/25,24,25/dfgdfg', None, status=400)
        resp.mustcontain('The image to color doesn\'t exist')

    def test_color_options(self):
        resp = self.testapp.options('/color/25,24,25/dfgdfg', status=200)
        self.assertEqual(resp.headers.get('Cache-Control'), 'max-age=0, no-cache')
        self.assertEqual(resp.headers.get('Access-Control-Allow-Origin'), '*')
        self.assertEqual(resp.headers.get('Access-Control-Allow-Methods'), 'OPTIONS,HEAD,GET')
