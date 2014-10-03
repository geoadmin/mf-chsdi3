# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import StaticPool
from sqlalchemy import engine_from_config


from chsdi.lib.helpers import remove_accents

dbs = ['sqlite', 'are', 'bafu', 'bak', 'bod', 'dritte', 'edi', 'evd', 'kogis', 'stopo', 'uvek', 'vbs', 'zeitreihen', 'lubis']

engines = {}
bases = {}
bodmap = {}
oerebmap = {}

for db in dbs:
    bases[db] = declarative_base()


def initialize_sql(settings):
    for db in dbs:
        if 'sqlite' not in db:
            engine = engine_from_config(
                settings,
                'sqlalchemy.%s.' % db,
                pool_recycle=20,
                pool_size=20,
                max_overflow=-1
            )
        else:
            '''
            In Memory sqlite database. For the connection parameters
            used, please see http://docs.sqlalchemy.org/en/rel_0_9/dialects/sqlite.html
            '''
            engine = engine_from_config(
                settings,
                'sqlalchemy.%s.' % db,
                connect_args={'check_same_thread': False},
                poolclass=StaticPool
            )
            engine.raw_connection().create_function('remove_accents', 1, remove_accents)
        engines[db] = engine
        bases[db].metadata.bind = engine


def register(name, klass):
    name = unicode(name)
    bodmap.setdefault(name, []).append(klass)


def register_oereb(name, klass):
    name = unicode(name)
    oerebmap.setdefault(name, []).append(klass)


def models_from_bodid(bodId):
    if bodId in bodmap:
        return bodmap[bodId]
    else:
        return None


def oereb_models_from_bodid(bodId):
    if bodId in oerebmap:
        return oerebmap[bodId]
    else:
        return None


def models_from_name(name):
    models = models_from_bodid(name)
    if models is not None:
        return models
    else:
        return None
