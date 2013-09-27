# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config

from geoalchemy import Geometry
from papyrus.geo_interface import GeoInterface

dbs = ['bod', 'bafu', 'uvek', 'search', 'stopo', 'evd', 'edi', 'are', 'dritte', 'kogis', 'zeitreihen']

engines = {}
bases = {}
bodmap = {}
esrimap = {}

for db in dbs:
    bases[db] = declarative_base(cls=GeoInterface)


def initialize_sql(settings):
    for db in dbs:
        engine = engine_from_config(
            settings,
            'sqlalchemy.%s.' % db,
            pool_recycle=20,
            pool_size=20,
            max_overflow=-1
        )
        engines[db] = engine
        bases[db].metadata.bind = engine


def register(name, klass):
    name = unicode(name)
    bodmap.setdefault(name, []).append(klass)
    if hasattr(klass, '__esriId__'):
        esrimap[klass.__esriId__] = name


def models_from_bodid(bodid):
    if bodid in bodmap:
        return bodmap[bodid]
    else:
        return None


def models_from_name(name):
    models = models_from_bodid(name)
    if models is not None:
        return models
    else:
        try:
            id = int(name)
            if id in esrimap:
                bodid = esrimap[id]
                return models_from_bodid(bodid)
        except:
            return None
