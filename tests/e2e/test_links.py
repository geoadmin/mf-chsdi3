# -*- coding: utf-8 -*-

import six
from webtest import TestApp
from pyramid.paster import get_app
from unittest import skip
from tests.integration import TestsBase
import requests
from requests.exceptions import ConnectionError, Timeout, RetryError


try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


MAX_RETRIES = 3
TIMEOUT = 10


if six.PY3:
    long = int


class LinksChecker(TestsBase):

    def __enter__(self):
        def num(s):
            if s.isdigit():
                return long(s)
            else:
                return s

        self.testapp = TestApp(get_app('development.ini'))

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del self.testapp
        return False

    def ilinks(self):
        bod_id = 'ch.kantone.cadastralwebmap-farbe'
        ids = [self.getRandomFeatureId(bod_id) for i in range(30)]
        for i in ids:
            response = self.testapp.get('/rest/services/ech/MapServer/%s/%d/htmlPopup' % (bod_id, i), status=200)
            soup = response.html
            for a in soup.findAll('a'):
                link = a.get('href')
                yield link

    def checkLink(self, link):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.68 Safari/537.36'
        }
        s = requests.Session()
        a = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        scheme, netloc, path, params, query, fragment = urlparse(link)
        scheme = scheme if scheme in ['http', 'https'] else 'http'
        s.mount('%s://' % scheme, a)

        try:
            r = s.get(link, timeout=TIMEOUT, headers=headers)
            self.assertEqual(r.status_code, 200, link)
        except (ConnectionError, Timeout, RetryError) as e:
            skip("Skipping link <{}> because of Connection/TimeoutError: {}".format(link, e))


def test_all_links():
    with LinksChecker() as lc:
        for link in lc.ilinks():
            yield lc.checkLink, link
