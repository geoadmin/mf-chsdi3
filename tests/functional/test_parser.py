# -*- coding: utf-8 -*-

import unittest
from chsdi.lib.parser import WhereParser


class TestWhereParser(unittest.TestCase):

    def test_with_numbers(self):
        sqls = ["toto = 1", "toto > 1", "toto >= 1.1"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(sqls[i],  w.sql)

    def test_with_strings(self):
        sqls = ["toto = 'raa'", "toto like 'ttu%'", "toto not ilike '%zaza%'"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(sqls[i],  w.sql)

    def test_with_is(self):
        sqls = ["toto is null", "toto is not null"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(sqls[i],  w.sql)

    def test_with_and(self):
        sql = "toto is null and toto is not null"
        w = WhereParser(sql)
        self.assertEqual("and",  w.operators[0])

    def test_with_or(self):
        sql = "toto like 'tutu%' or toto is not null"
        w = WhereParser(sql)
        self.assertEqual("or",  w.operators[0])

    def test_with_many_operators(self):
        sql = "toto like 'tutu%' or toto is not null and tata > 0.2"
        w = WhereParser(sql)
        self.assertEqual(2,  len(w.operators))

    def test_failings(self):
        # 1/ ilike and number are forbidden, 2/ maybe is not a keyword
        sqls = ["toto ilike 2", "state ilike '%a%' maybe abortionaccomplished > '2014-12-01'"]
        for i, sql in enumerate(sqls):
            w = WhereParser(sql)
            self.assertEqual(None,  w.sql)
