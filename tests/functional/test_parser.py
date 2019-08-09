# -*- coding: utf-8 -*-

import unittest
from chsdi.lib.parser import WhereParser


class TestWhereParser(unittest.TestCase):

    def test_with_numbers(self):
        sqls = ["toto = 1", "toto > 1", "toto < -5.6",  "toto >= 1.1", "toto<=3", "toto=4", "toto < 1.0e6", "toto > -1.5677e3"]
        expected = ["toto = 1", "toto > 1", "toto < -5.6",  "toto >= 1.1", "toto <= 3", "toto = 4", "toto < 1.0e6", "toto > -1.5677e3"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(expected[i],  w.sql)

    def test_with_strings(self):
        sqls = ["toto = 'raa'", "toto like 'ttu%'", "toto ilike '%urr%'", "toto not ilike 'Tata%'",
                "toto not ilike '%zaza%'", u"name ilike '%Aare-Bern, Schönau%'", u'andere_stoffe is null']
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(sqls[i],  w.sql)

    def test_with_is(self):
        sqls = ["toto is null", "toto is not null"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(sqls[i],  w.sql)

    def test_with_many_spaces(self):
        sqls = ["toto  =    2.3", "toto=1", "  toto  >=1.0"]
        expected = ["toto = 2.3", "toto = 1", "toto >= 1.0"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(expected[i],  w.sql)

    def test_with_is_boolean(self):
        sqls = ["toto is true", "toto is not true", "toto is false", "toto is not false",
                "toto != false", "toto <> false", "toto = false", "toto = true", "toto=true", "toto=false"]
        expected = ["toto is true", "toto is not true", "toto is false", "toto is not false",
                "toto != false", "toto <> false", "toto = false", "toto = true", "toto = true", "toto = false"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(expected[i],  w.sql)

    def test_with_and(self):
        sql = "toto is null and toto is not null"
        w = WhereParser(sql)
        self.assertEqual("and",  w.operators[0])

    def test_with_date(self):
        sql = u"startofconstruction > '2014-12-01'"
        w = WhereParser(sql)
        self.assertEqual(sql,  w.sql)

    def test_with_or(self):
        sql = "toto like 'tutu%' or toto is not null"
        w = WhereParser(sql)
        self.assertEqual("or",  w.operators[0])

    def test_with_many_operators(self):
        sql = "toto like 'tutu%' or toto is not null and tata > 0.2"
        w = WhereParser(sql)
        self.assertEqual(2,  len(w.operators))

    def test_failings(self):
        # 1/ ilike and number are forbidden
        # 2/ 'maybe' is not a keyword
        # 3/ no attribute
        # 4/ sql-injection
        sqls = ["toto ilike 2", "state ilike '%a%' maybe abortionaccomplished > '2014-12-01'",
                "1 = 1", "username='username' AND password='password' OR 1=1"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(None,  w.sql)
