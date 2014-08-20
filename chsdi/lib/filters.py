# -*- coding: utf-8 -*-

from chsdi.models.bod import LayersConfig
from sqlalchemy.sql.expression import cast
from sqlalchemy import Text, or_, and_


def full_text_search(query, ormColumns, searchText):
    ''' Given a list of columns and a searchText, returns
    a filtered query '''
    def ilike_search(col):
        if col is not None:
            return cast(col, Text).ilike('%%%s%%' % searchText)
    return query.filter(or_(
        *map(ilike_search, ormColumns)
    ))


def filter_by_geodata_staging(query, ormColumn, staging):
    ''' Applies a filter on geodata based on application
    staging '''
    return {
        'test': query,
        'integration': query.filter(or_(
                                    ormColumn == 'integration',
                                    ormColumn == 'prod'
                                    )),
        'prod': query.filter(ormColumn == staging)
    }[staging]


def filter_by_map_name(query, model, mapName):
    ''' Applies a map/topic filter '''
    if mapName != 'all':
        clauses = []
        if mapName == 'api-notfree':
            mapName = 'api'
            chargeable = True
            clauses.append(model.maps.ilike('%%%s%%' % mapName))
            clauses.append(model.chargeable == chargeable)
            return query.filter(and_(*clauses))
        elif mapName == 'api-free':
            mapName = 'api'
            chargeable = False
            clauses.append(model.maps.ilike('%%%s%%' % mapName))
            clauses.append(model.chargeable == chargeable)
            return query.filter(and_(*clauses))
        elif mapName in ('api', 'swissmaponline'):
            clauses.append(model.maps.ilike('%%%s%%' % mapName))
        else:
            # add background layersConfig
            if model.__tablename__ == LayersConfig.__tablename__:
                isBgLayer = True
                clauses.append(model.background == isBgLayer)
            # we also want to always include all 'ech' layers (except for api's)
            clauses.append(model.maps.ilike('%%%s%%' % mapName))
            # whitelist hack
            clauses.append(model.maps.ilike('%%%s%%' % 'ech'))
        return query.filter(or_(*clauses))
    return query
