# -*- coding: utf-8 -*-

import sqlalchemy.types as types


class DateTimeChsdi(types.TypeDecorator):

    impl = types.DateTime

    def process_bind_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        return value.strftime('%d.%m.%Y')

    def copy(self):
        return DateTimeChsdi()
