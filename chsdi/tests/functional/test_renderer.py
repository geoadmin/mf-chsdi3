# -*- coding: utf-8 -*-

import unittest
import esrijson
from geojson import Point
from pyramid import testing


class Test_EsriGeoJSON(unittest.TestCase):

    def _callFUT(self, **kwargs):
        from chsdi.renderers import EsriJSON
        fake_info = {}
        return EsriJSON(**kwargs)(fake_info)

    def test_json(self):
        renderer = self._callFUT()
        result = renderer({'a': 1}, {})
        self.assertEqual(result, '{"a": 1}')

    def test_esrijson(self):
        f = esrijson.Feature(geometry=Point([600000, 200000]), attributes={'name': 'toto'})
        renderer = self._callFUT()
        request = testing.DummyRequest()
        result = renderer(f, {'request': request})
        self.assertEqual(result, '{"geometry": {"y": 200000, "x": 600000}, "attributes": {"name": "toto"}}')

        self.assertEqual(request.response.content_type, 'application/json')

    def test_jsonp(self):
        renderer = self._callFUT(jsonp_param_name="callback")
        f = esrijson.Feature(geometry=Point([600000, 200000]), attributes={'name': 'toto'})
        request = testing.DummyRequest()
        request.params['callback'] = 'jsonp_cb'
        result = renderer(f, {'request': request})
        self.assertEqual(result, 'jsonp_cb({"geometry": {"y": 200000, "x": 600000}, "attributes": {"name": "toto"}});')
        self.assertEqual(request.response.content_type, 'text/javascript')
