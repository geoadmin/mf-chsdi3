# -*- coding: utf-8 -*-

import unittest
from chsdi.models.vector import get_fallback_lang_match


class TestAttributesTranslations(unittest.TestCase):

    def test_no_lang_specific_attribute(self):
        # No match, so no based on lang - return attr
        queryableAttrs = ['toto', 'tutu', 'tata']
        lang = 'de'
        availableLangs = 'de'
        attr = 'toto'
        self.assertEqual('toto', get_fallback_lang_match(queryableAttrs, lang, attr, availableLangs))

    def test_lang_specific_attribute(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        lang = 'fr'
        availableLangs = 'fr'
        attr = 'toto_fr'
        self.assertEqual('toto_fr', get_fallback_lang_match(queryableAttrs, lang, attr, availableLangs))

    def test_attribute_fallback_to_de(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        lang = 'en'
        availableLangs = 'de'
        attr = 'toto_de'
        self.assertEqual('toto_de', get_fallback_lang_match(queryableAttrs, lang, attr, availableLangs))

    def test_attribute_fallback_to_fr(self):
        queryableAttrs = ['toto', 'toto_fr', 'toto_de']
        lang = 'it'
        availableLangs = 'fr'
        attr = 'toto_fr'
        self.assertEqual('toto_fr', get_fallback_lang_match(queryableAttrs, lang, attr, availableLangs))
