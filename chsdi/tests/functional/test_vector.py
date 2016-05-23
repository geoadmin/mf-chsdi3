# -*- coding: utf-8 -*-

import unittest

from chsdi.models.vector import getFallbackLangMatch, esriRest2Shapely


class Test_AttributesTranslations(unittest.TestCase):

    def test_no_lang_specific_attribute(self):
        # No match, so no based on lang - return attr
        queryableAttrs = ['toto', 'tutu', 'tata']
        lang = 'de'
        availableLangs = 'de'
        attr = 'toto'
        self.assertEqual('toto', getFallbackLangMatch(queryableAttrs, lang, attr, availableLangs))

    def test_lang_specific_attribute(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        lang = 'fr'
        availableLangs = 'fr'
        attr = 'toto_fr'
        self.assertEqual('toto_fr', getFallbackLangMatch(queryableAttrs, lang, attr, availableLangs))

    def test_attribute_fallback_to_de(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        lang = 'en'
        availableLangs = 'de'
        attr = 'toto_de'
        self.assertEqual('toto_de', getFallbackLangMatch(queryableAttrs, lang, attr, availableLangs))

    def test_attribute_fallback_to_fr(self):
        queryableAttrs = ['toto', 'toto_fr', 'toto_de']
        lang = 'it'
        availableLangs = 'fr'
        attr = 'toto_fr'
        self.assertEqual('toto_fr', getFallbackLangMatch(queryableAttrs, lang, attr, availableLangs))

    def test_point_geometry(self):
        geometry = {'type': 'Point', 'coordinates': (0.0, 0.0)}
        shape = esriRest2Shapely(geometry)
        self.assertEqual('Point', shape.geom_type)
        self.assertEqual([(0.0, 0.0)], list(shape.coords))

    def test_false_geometry(self):
        # it returns the initial geometry
        geometry = {'type': 'onepoint', 'coordinates': (0.0, 0.0)}
        shape = esriRest2Shapely(geometry)
        self.assertEqual(shape, geometry)

    def test_none_geometry(self):
        geometry = None
        shape = esriRest2Shapely(geometry)
        self.assertEqual(None, shape)
