# -*- coding: utf-8 -*-

import unittest
import datetime
from chsdi.models.types import DateTimeChsdi


class Test_DateTimeChsdi(unittest.TestCase):
    _multiprocess_can_split_ = True

    def test_datetimechsdi(self):
        dt = DateTimeChsdi()
        value = None
        dialect = None
        result = dt.process_bind_param(value, dialect)
        self.assertEqual(result, None)
        value1 = '30-12-2011'
        result1 = dt.process_bind_param(value1, dialect)
        self.assertEqual(result1, value1)
        value2 = datetime.datetime(2017, 8, 22, 7, 5, 5)
        result2 = dt.process_bind_param(value2, dialect)
        self.assertEqual(str(result2), '2017-08-22 07:05:05')

    def test_datetimechsdi_process_value(self):
        dt = DateTimeChsdi()
        value = datetime.datetime(2013, 9, 30, 7, 6, 5)
        dialect = None
        result = dt.process_result_value(value, dialect)
        self.assertEqual(result, '30.09.2013')

    def test_copy(self):
        dt = DateTimeChsdi()
        result = dt.copy()
        self.assertEqual(str(result), str(dt))
