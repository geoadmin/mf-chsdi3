# -*- coding: utf-8 -*-

import requests

from chsdi.tests.integration import TestsBase


class TestLinks(TestsBase):

    def test_external_links(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.68 Safari/537.36'
        }
        for i in range(1, 27):
            response = self.testapp.get('/rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/%d/htmlPopup' % i, status=200)

            soup = response.html
            for a in soup.findAll('a'):
                link = a.get('href')
                r = requests.get(link, timeout=10, headers=headers)
                self.assertEqual(r.status_code, 200, link)
