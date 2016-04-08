# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config, Column


dbs = ['are', 'bafu', 'bak', 'bod', 'dritte', 'edi', 'evd', 'kogis', 'stopo', 'uvek', 'vbs', 'zeitreihen', 'lubis']

engines = {}
bases = {}
bodmap = {}
oerebmap = {}

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


def register_oereb(name, klass):
    name = unicode(name)
    oerebmap.setdefault(name, []).append(klass)


def oereb_models_from_bodid(bodId):
    return oerebmap.get(bodId)


def models_from_bodid(bodId, scale=None):
    models = bodmap.get(bodId)
    if scale and models:
        filteredModels = []
        for m in models:
            hasMinScale = hasattr(m, '__minscale__')
            hasMaxScale = hasattr(m, '__maxscale__')
            if hasMinScale and hasMaxScale:
                if m.__minscale__ < scale and m.__maxscale__ > scale:
                    filteredModels.append(m)
            elif hasMinScale:
                if m.__minscale__ < scale:
                    filteredModels.append(m)
            elif hasMaxScale:
                if m.__maxscale__ > scale:
                    filteredModels.append(m)
        if len(filteredModels) > 0:
            return filteredModels
    else:
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
