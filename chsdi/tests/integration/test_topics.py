# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestTopicsListingView(TestsBase):

    def test_topics(self):
        resp = self.testapp.get('/rest/services', status=200)
        self.assertTrue(resp.content_type == 'application/json')
        topics = resp.json['topics']
        i = 1
        for topic in topics:
            self.assertTrue('id' in topic)
            self.assertTrue('backgroundLayers' in topic)
            self.assertTrue('langs' in topic)
            self.assertTrue('selectedLayers' in topic)
            self.assertTrue('defaultBackground' in topic)
            self.assertTrue('activatedLayers' in topic)
            self.assertTrue('plConfig' in topic)
            self.assertTrue('groupId' in topic)
            if i != len(topics):
                self.assertGreaterEqual(topics[i]['groupId'], topics[i - 1]['groupId'])
            i += 1

    def test_topics_with_cb(self):
        resp = self.testapp.get('/rest/services', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')
        resp.mustcontain('cb_(')
