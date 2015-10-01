# -*- coding: utf-8 -*-

import unittest

from pyramid import testing

from chsdi.lib.zadara_helpers import find_files, hbytes


class Test_ZadaraHelpers(unittest.TestCase):

    def test_hbytes(self):
        testnumber = 5
        result = hbytes(testnumber)
        self.assertEqual(result, '5.0 bytes')

    def test_hbytes_KB(self):
        testnumber = 1024.0 + 5
        result = hbytes(testnumber)
        self.assertEqual(result, '1.0 KB')

    def test_hbytes_MB(self):
        testnumber = 1024.0 ** 2 + 5
        result = hbytes(testnumber)
        self.assertEqual(result, '1.0 MB')

    def test_hbytes_GB(self):
        testnumber = 1024.0 ** 3 + 5
        result = hbytes(testnumber)
        self.assertEqual(result, '1.0 GB')

    def test_hbytes_TB(self):
        testnumber = 1024.0 ** 4 + 5
        result = hbytes(testnumber)
        self.assertEqual(result, '1.0 TB')

    def test_find_files(self):
        import os
        request = testing.DummyRequest()
        request.host = 'api3.geo.admin.ch'
        request.scheme = 'http'
        request.registry.settings = {}
        request.registry.settings['apache_base_path'] = 'main'
        request.registry.settings['zadara_dir'] = '/var/local/cartoweb/downloads/'
        layerBodId = 'ch.swisstopo.geologie-gisgeol'
        fileName = os.listdir(request.registry.settings['zadara_dir'] + layerBodId)[0]
        for f in find_files(request, layerBodId, fileName):
            self.assertTrue('name' in f)
            self.assertTrue('size' in f)
            self.assertTrue('url' in f)
            self.assertEqual(f['url'], ''.join(
                ('//', request.host, '/downloads/', layerBodId, '/', fileName)
            ))
            self.assertTrue(isinstance(f['size'], int))
            self.assertEqual(f['name'], fileName)
