# -*- coding: utf-8 -*-

import six
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config, Column

if six.PY3:
    unicode = str


dbs = ['are', 'bafu', 'bak', 'bod', 'dritte', 'edi', 'evd', 'kogis', 'stopo', 'uvek', 'uvek_solarkataster', 'vbs', 'zeitreihen', 'lubis', 'diemo']

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


def set_models_srid(models, srid):
    if models is None:
        return models
    ms = []
    for m in models:
        ms.append(m)
    return ms


def perimeter_models_from_bodid(bodId, srid=21781):
    perimeter_models = perimetermap.get(bodId)
    if perimeter_models is None:
        return models_from_bodid(bodId, srid=srid)
    return set_models_srid(perimeter_models, srid)


def oereb_models_from_bodid(bodId, scale=None, srid=21781):
    models = oerebmap.get(bodId)
    if scale is not None:
        models = [m for m in models if scale < max_scale(m) and scale >= min_scale(m)]
    return set_models_srid(models, srid)


# Returns None is the bodId is not registered and an empty list if the bodId is registered but
# the scale filtered all models out. orderScale orders by scale validity
def models_from_bodid(bodId, scale=None, resolution=None, orderScale=None, srid=21781):
    models = bodmap.get(bodId)
    if models:
        if orderScale is not None:
            mdls = []
            for m in models:
                if orderScale < max_scale(m) and orderScale >= min_scale(m):
                    mdls.insert(0, m)
                else:
                    mdls.append(m)
            models = mdls
        elif scale is not None:
            models = [m for m in models if scale < max_scale(m) and scale >= min_scale(m)]
        elif resolution is not None:
            models = [m for m in models if resolution < max_resolution(m) and resolution >= min_resolution(m)]
    return set_models_srid(models, srid)


def queryable_models_from_bodid(bodId, searchField, srid=21781):
    models = models_from_bodid(bodId, srid=srid)
    if models is not None:
        models = [m for m in models if isinstance(m.get_column_by_property_name(searchField), Column)]
        if len(models) > 0:
            return models


def get_models_attributes_keys(models, lang, attribute_only):
    all_attributes = []
    for model in models:
        attributes = []
        if hasattr(model, '__queryable_attributes__'):
            attributes = model.get_queryable_attributes_keys(lang)
        elif not attribute_only:
            attributes = model().get_attributes_keys()
        all_attributes = all_attributes + attributes
    return list(set(all_attributes))
