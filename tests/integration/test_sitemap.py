# -*- coding: utf-8 -*-


import subprocess
import tempfile
import os
import time
from tests.integration import TestsBase
from chsdi.lib.helpers import to_utf8


def _validate_scheme(scheme, body):
    def validate(schema_url, f, attempts):
        try:
            retcode = subprocess.call(["xmllint", "--noout", "--nocatalogs", "--schema", schema_url, f.name])
        except OSError:
            if attempts > 3:
                retcode = 5342
            else:
                attempts += 1
                time.sleep(2)
                return validate(schema_url, f, attempts)
        return retcode

    schema_url = os.path.join(os.path.dirname(__file__), "sitemaps/" + scheme)
    os.environ['XML_CATALOG_FILES'] = os.path.join(os.path.dirname(__file__), "xml/catalog")
    f = tempfile.NamedTemporaryFile(mode='w+t', prefix='sitemap-index')
    f.write(body)
    f.seek(0)
    retcode = validate(schema_url, f, 1)
    f.close()
    return retcode


class TestSitemapView(TestsBase):

    def __init__(self, other):
        super(TestsBase, self).__init__(other)
        self.sitemaps_with_urls = ['base', 'topics', 'layers']
        self.sitemaps_notin_index = ['index', 'addresses']

    def test_no_parameter_failure(self):
        resp = self.testapp.get('/sitemap', status=400)
        resp.mustcontain('Please provide the parameter content')

    def test_wrong_parameter_failure(self):
        resp = self.testapp.get('/sitemap?dummy=base', status=400)
        resp.mustcontain('Please provide the parameter content')

    def test_wrong_parameter_values_failure(self):
        resp = self.testapp.get('/sitemap?content=wrongthing', status=404)
        resp.mustcontain('Please provide a valid content parameter')

    def test_malformed_parameter_values_failure(self):
        resp = self.testapp.get('/sitemap?content=base_index_address', status=400)
        resp.mustcontain('Malformed content parameter')

    def test_index_file(self):
        resp = self.testapp.get('/sitemap?content=index', status=200)
        resp.content_type == 'application/xml'
        body = to_utf8(resp.body)
        # contains all links
        for urlbase in self.sitemaps_with_urls:
            resp.mustcontain('/sitemap?content=base')
        # does not contain
        for urlbase in self.sitemaps_notin_index:
            self.assertNotIn('/sitemap?content=' + urlbase, body)

        # contains correct domain
        self.assertIn(self.testapp.app.registry.settings.get('host'), body)
        # validate scheme
        self.assertEqual(0, _validate_scheme('siteindex.xsd', body))

    def test_base_file(self):
        resp = self.testapp.get('/sitemap?content=base', status=200)
        resp.content_type == 'application/xml'
        body = to_utf8(resp.body)
        # contains all languages
        for lang in ['de', 'fr', 'it', 'rm', 'en']:
            resp.mustcontain('lang=' + lang)
        # contains correct domain
        self.assertTrue(self.testapp.app.registry.settings.get('geoadminhost') in body)
        # validate scheme
        self.assertEqual(0, _validate_scheme('sitemap.xsd', body))

    def test_topics_file(self):
        resp = self.testapp.get('/sitemap?content=topics', status=200)
        resp.content_type == 'application/xml'
        body = to_utf8(resp.body)
        # contains all languages
        for lang in ['de', 'fr', 'it', 'rm', 'en']:
            resp.mustcontain('lang=' + lang)
        # test for some topics
        for topic in ['blw', 'ech', 'swisstopo', 'luftbilder', 'inspire']:
            resp.mustcontain('topic=' + topic)
        # contains correct domain
        self.assertTrue(self.testapp.app.registry.settings.get('geoadminhost') in body)
        # validate scheme
        self.assertEqual(0, _validate_scheme('sitemap.xsd', body))

    def test_layers_file(self):
        resp = self.testapp.get('/sitemap?content=layers', status=200)
        resp.content_type == 'application/xml'
        body = to_utf8(resp.body)
        # contains all languages
        for lang in ['de', 'fr', 'it', 'rm', 'en']:
            self.assertTrue('lang=' + lang in body)
        # test for some topics
        for topic in ['blw', 'ech', 'swisstopo', 'luftbilder', 'inspire']:
            self.assertTrue('topic=' + topic in body)
        # test for some layers
        for layer in ['ch.blw.bodeneignung-kulturtyp', 'ch.bafu.laerm-strassenlaerm_tag', 'ch.swisstopo-vd.spannungsarme-gebiete']:
            self.assertTrue('layers=' + layer in body)
        # contains correct domain
        self.assertTrue(self.testapp.app.registry.settings.get('geoadminhost') in body)
        # validate scheme
        self.assertEqual(0, _validate_scheme('sitemap.xsd', body))

    def test_bad_multi_files(self):
        # multipart (after _) must be integer
        self.testapp.get('/sitemap?content=addresses_other', status=400)
        # mutiipart can't be empty
        self.testapp.get('/sitemap?content=addresses_', status=400)
        # multipart muast be >= 0
        self.testapp.get('/sitemap?content=addresses_-1', status=400)

    def test_addresses_index_file(self):
        resp = self.testapp.get('/sitemap?content=addresses', status=200)
        resp.content_type == 'application/xml'
        body = to_utf8(resp.body)
        # shouldn't contain too big (this might theoretically fail if address db grew)
        self.assertNotIn('/sitemap?content=addresses_500', body)
        # check for first link
        resp.mustcontain('/sitemap?content=addresses_0')
        # check for last link (this might change depending on size of db
        resp.mustcontain('/sitemap?content=addresses_387')
        # contains correct domain
        self.assertIn(self.testapp.app.registry.settings.get('host'), body)
        # validate scheme
        self.assertEqual(0, _validate_scheme('siteindex.xsd', body))

    def test_addresses_file(self):
        resp = self.testapp.get('/sitemap?content=addresses_387', status=200)
        resp = self.testapp.get('/sitemap?content=addresses_0', status=200)
        resp.content_type == 'application/xml'
        body = to_utf8(resp.body)
        # some checks on content
        resp.mustcontain('ch.bfs.gebaeude_wohnungs_register=')
        resp.mustcontain('X=')
        resp.mustcontain('Y=')
        resp.mustcontain('zoom=')
        # contains correct domain
        self.assertTrue(self.testapp.app.registry.settings.get('geoadminhost') in body)
        # validate scheme
        self.assertEqual(0, _validate_scheme('sitemap.xsd', body))
