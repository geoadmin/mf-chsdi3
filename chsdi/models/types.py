# -*- coding: utf-8 -*-

import json
import sqlalchemy.types as types
from geoalchemy2.types import Geometry
from sqlalchemy.sql import func


from chsdi.lib.validation import SUPPORTED_OUTPUT_SRS


class JsonChsdi(types.TypeDecorator):

    impl = types.Unicode

    def process_bind_param(self, value, dialect):
        if value:
            return json.dumps(value)
        return None

    def process_result_value(self, value, dialect):
        if value:
            return json.loads(value)
        return {}

    def copy(self):
        return JsonChsdi()


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


"""
Custom class that extends the base geometry class of geoalchemy2.
This class is used to reproject geometries on the fly so that the reference to
the main model is kept.
"""


class GeometryChsdi(Geometry):
    cache_ok = True

    def __init__(self, geometry_type='GEOMETRY', srid=-1, dimension=2,
                 spatial_index=True, management=False, srid_out=21781):
        super(GeometryChsdi, self).__init__(geometry_type=geometry_type,
              srid=srid, dimension=dimension, spatial_index=spatial_index,
              management=management)
        self._srid_out = int(srid)

    @property
    def srid_out(self):
        return self._srid_out

    @srid_out.setter
    def srid_out(self, value):
        try:
            value = int(value)
        except (TypeError, ValueError):
            pass
        if value in SUPPORTED_OUTPUT_SRS:
            self._srid_out = value

    def column_expression(self, col):
        if self.srid != self.srid_out:
            col = func.ST_Transform(col, self._srid_out)
        return getattr(func, self.as_binary)(col, type_=self)
