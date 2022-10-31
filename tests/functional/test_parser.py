# -*- coding: utf-8 -*-

import unittest
from chsdi.lib.parser import WhereParser
from chsdi.lib.helpers import ilen


class TestWhereParser(unittest.TestCase):

    def test_with_numbers(self):
        sqls = [u"toto = 1", u"toto > 1", u"toto < -5.6",  u"toto >= 1.1", u"toto<=3", u"toto=4", u"toto < 1.0e6", u"toto > -1.5677e3"]
        expected = [u"toto = 1", u"toto > 1", u"toto < -5.6",  u"toto >= 1.1", u"toto <= 3", u"toto = 4", u"toto < 1.0e6", u"toto > -1.5677e3"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(expected[i],  w.sql)

    def test_with_strings(self):
        sqls = [u"toto = 'raa'", u"toto like 'ttu%'", u"toto ilike '%urr%'", u"toto not ilike 'Tata%'",
                u"toto not ilike '%zaza%'", u"name ilike '%Aare-Bern, Schönau%'", u'andere_stoffe is null']
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(sqls[i],  w.sql)

    def test_with_is(self):
        sqls = [u"toto is null", u"toto is not null"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(sqls[i],  w.sql)

    def test_with_many_spaces(self):
        sqls = [u"toto  =    2.3", u"toto=1", u"  toto  >=1.0"]
        expected = [u"toto = 2.3", u"toto = 1", u"toto >= 1.0"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(expected[i],  w.sql)

    def test_with_is_boolean(self):
        sqls = [u"toto is true", u"toto is not true", u"toto is false", u"toto is not false",
                u"toto != false", u"toto = false", u"toto = true", u"toto=true", u"toto=false"]
        expected = [u"toto is true", u"toto is not true", u"toto is false", u"toto is not false",
                u"toto != false", u"toto = false", u"toto = true", u"toto = true", u"toto = false"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(expected[i],  w.sql)

    def test_with_and(self):
        sql = u"toto is null and toto is not null"
        w = WhereParser(sql)
        self.assertEqual("and",  list(w.operators)[0])

    def test_with_date(self):
        sql = u"startofconstruction > '2014-12-01'"
        w = WhereParser(sql)
        self.assertEqual(sql,  w.sql)

    def test_with_or(self):
        sql = u"toto like 'tutu%' or toto is not null"
        w = WhereParser(sql)
        self.assertEqual("or",  list(w.operators)[0])

    def test_with_many_operators(self):
        sql = u"toto like 'tutu%' or toto is not null and tata > 0.2"
        w = WhereParser(sql)
        self.assertEqual(2,  ilen(w.operators))

    def test_failings(self):
        # 1/ ilike and number are forbidden
        # 2/ 'maybe' is not a keyword
        # 3/ no attribute
        # 4/ sql-injection
        sqls = [u"toto ilike 2", u"state ilike '%a%' maybe abortionaccomplished > '2014-12-01'",
                u"1 = 1", u"username='username' AND password='password' OR 1=1"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(None,  w.sql)
