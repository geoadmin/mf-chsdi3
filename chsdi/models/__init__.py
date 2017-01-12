# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config, Column


dbs = ['are', 'bafu', 'bak', 'bod', 'dritte', 'edi', 'evd', 'kogis', 'mogis', 'stopo', 'uvek', 'uvek_solarkataster', 'vbs', 'zeitreihen', 'lubis']

engines = {}
bases = {}
bodmap = {}
oerebmap = {}
perimetermap = {}

for db in dbs:
    bases[db] = declarative_base()


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


def register_perimeter(name, klass):
    name = unicode(name)
    perimetermap.setdefault(name, []).append(klass)


def register_oereb(name, klass):
    name = unicode(name)
    oerebmap.setdefault(name, []).append(klass)


def min_resolution(m):
    return m.__minresolution__ if hasattr(m, '__minresolution__') else 0.0


def max_resolution(m):
    return m.__maxresolution__ if hasattr(m, '__maxresolution__') else float('inf')


def min_scale(m):
    return m.__minscale__ if hasattr(m, '__minscale__') else 0.0


def max_scale(m):
    return m.__maxscale__ if hasattr(m, '__maxscale__') else float('inf')


def perimeter_models_from_bodid(bodId):
    perimeter_models = perimetermap.get(bodId)
    if perimeter_models is None:
        return models_from_bodid(bodId)
    return perimeter_models


def oereb_models_from_bodid(bodId, scale=None):
    models = oerebmap.get(bodId)
    if scale is not None:
        models = [m for m in models if scale < max_scale(m) and scale >= min_scale(m)]
    return models


def models_from_bodid(bodId, scale=None, resolution=None):
    models = bodmap.get(bodId)
    if models:
        if scale is not None:
            models = [m for m in models if scale < max_scale(m) and scale >= min_scale(m)]
        if resolution is not None:
            models = [m for m in models if resolution < max_resolution(m) and resolution >= min_resolution(m)]
    return models


def queryable_models_from_bodid(bodId, searchField):
    models = models_from_bodid(bodId)
    if models is not None:
        models = [m for m in models if isinstance(m.get_column_by_property_name(searchField), Column)]
        if len(models) > 0:
            return models


def get_models_attributes_keys(models, lang, attributeOnly):
    allAttributes = []
    for model in models:
        attributes = []
        if hasattr(model, '__queryable_attributes__'):
            attributes = model.get_queryable_attributes_keys(lang)
        elif not attributeOnly:
            attributes = model().getAttributesKeys()
        allAttributes = allAttributes + attributes
    return list(set(allAttributes))
