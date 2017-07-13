# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestTopicsListingView(TestsBase):

    def test_topics(self):
        resp = self.testapp.get('/rest/services', status=200)
        self.assertTrue(resp.content_type == 'application/json')
        topics = resp.json['topics']
        i = 1
        for topic in topics:
            self.assertIn('id', topic)
            self.assertIn('backgroundLayers', topic)
            self.assertIn('selectedLayers', topic)
            self.assertIn('defaultBackground', topic)
            self.assertIn('activatedLayers', topic)
            self.assertIn('plConfig', topic)
            self.assertIn('groupId', topic)
            if i != len(topics):
                self.assertGreaterEqual(topics[i]['groupId'], topics[i - 1]['groupId'])
            i += 1

    def test_topics_with_cb(self):
        resp = self.testapp.get('/rest/services', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')
