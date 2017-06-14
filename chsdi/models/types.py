# -*- coding: utf-8 -*-

import sqlalchemy.types as types


class DateTimeChsdi(types.TypeDecorator):

    impl = types.DateTime

    def process_bind_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        if value:
            m = '0%s' % value.month if value.month < 10 else '%s' % value.month
            d = '0%s' % value.day if value.day < 10 else '%s' % value.day
            return '%s.%s.%s' % (d, m, value.year)
        return '-'

    def copy(self):
        return DateTimeChsdi()
