# -*- coding: utf-8 -*-

from past.utils import old_div
import os


from pyramid.paster import get_app


class TodProxyTestsBase(object):

    def setUp(self):
        app = get_app('development.ini')
        registry = app.registry
        try:
            os.environ["http_proxy"] = registry.settings['http_proxy']
            apache_entry_path = registry.settings['apache_entry_path']
            self.wmts_public_host = "http://" + registry.settings['wmts_public_host'] + '/'
            self.host_url = "http://" + registry.settings['host'] + apache_entry_path
        except KeyError as e:
            raise e
        self.BAD_REFERER = 'http://foo.ch'
        self.GOOD_REFERER = 'http://unittest.geo.admin.ch'
        self.EPSGS = [21781, 4326, 2056, 3857]

    def tearDown(self):
        if "http_proxy" in os.environ:
            del os.environ["http_proxy"]

    def hash(self, bits=96):
        assert bits % 8 == 0
        try:
            hexstr = os.urandom(old_div(bits, 8)).hex()
        except AttributeError:
            hexstr = os.urandom(old_div(bits, 8)).encode('hex')
        return hexstr
