# -*- coding: utf-8 -*-

"""
This script can be used to scan the models in chsdi and return a list of dependent tables.

The output format is a csv with | delimiter and it contains the following attributes:
* layer name
* data source (db.schema.table)
* list of attributes referenced in the model
* list of queryable attributes

Usage:

  .venv/bin/python scripts/models_scan.py > results.csv

  .venv/bin/python scripts/models_scan.py fixme (to display all duplicated pkeys)
"""

import re
import sys
from pyramid.paster import get_app


def getPGTables(layerId, engine, dbname, schema, tablename):
    sqlTemplate = 'EXPLAIN VERBOSE SELECT * FROM %s.%s'
    try:
        t = []
        sqlQuery = sqlTemplate % (schema, tablename)
        records = engine.execute(sqlQuery)
        for i in records:
            table = re.search('[Bitmap Heap|Index|Seq] Scan.* on ([^ ]+)', i[0])
            table = table.group(1) if table else None
            if table and 'Bitmap Index Scan' not in i[0]:
                t.append('%s.%s.%s' % (dbname, schema, tablename))
        t = list(set(t))
        return sorted(t)
    except:
        pass


def getTableReferences(dbmap, engines):
    for layerId, models in dbmap.iteritems():
        tmp = []
        tmpColumns = []
        tmpQueryableAttributes = []
        for model in models:
            try:
                queryable_attributes = model.__queryable_attributes__
            except AttributeError:
                queryable_attributes = []
            matches = re.match(
                '^.*\/{1}([a-z]*_solarkataster)|^.*\/{1}([a-z]*)',
                model.metadata.__str__())
            dbname = matches.group(1) if matches.group(1) else matches.group(2)
            engine = engines.get(dbname)
            schema = model.__table_args__['schema'] if 'schema' in model.__table_args__ else 'public'
            tablename = model.__tablename__
            columnNames = [k.name for k in model.__table__.columns]
            queryableAttributes = [k for k in queryable_attributes]
            tmp.append(getPGTables(layerId, engine, dbname, schema, tablename))
            tmpColumns += columnNames
            tmpQueryableAttributes += queryableAttributes
        if len(models) > 1:
            print layerId
        result = [item for sublist in tmp for item in sublist]
        result = sorted(list(set(result)))
        resultColumns = sorted(list(set(tmpColumns)))
        resultQueryableAttributes = sorted(list(set(tmpQueryableAttributes)))
        yield layerId, result, resultColumns, resultQueryableAttributes, len(models), dbname


def main():
    bodIdsWithMultipleModels = []
    dbsWithMultipleModels = []
    # Load app to register the models
    app = get_app('production.ini')
    from sqlalchemy.orm import scoped_session, sessionmaker
    from chsdi.models import bodmap, oerebmap, perimetermap, engines
    print 'layerId|data|columns|queryableAttributes'
    dbsmap = [bodmap, oerebmap, perimetermap]
    for dbmap in dbsmap:
        for layerId, ref, refColumns, refQueryableAttributes, nbTables, dbname in getTableReferences(dbmap, engines):
            print '%s|%s|%s|%s' % (layerId, ','.join(ref), ','.join(refColumns), ','.join(refQueryableAttributes))
            if nbTables > 1:
                bodIdsWithMultipleModels.append(layerId)
                dbsWithMultipleModels.append(dbname)

    if len(sys.argv) == 1:
        sys.exit(0)

    fixme = []
    # Test if we don't have the same IDs
    for b in range(0, len(bodIdsWithMultipleModels)):
        bodId = bodIdsWithMultipleModels[b]
        dbname = dbsWithMultipleModels[b]
        if dbname == 'uvek_solarkataster':
            continue
        models = bodmap.get(bodId)
        nbModels = len(models)
        engine = engines.get(dbname)
        session = scoped_session(sessionmaker(bind=engine))
        for i in range(0, nbModels):
            for j in range(i, nbModels):
                if i != j:
                    iColType = models[i].primary_key_column().type
                    jColType = models[j].primary_key_column().type
                    if type(iColType) == type(jColType):
                        subQuery = session.query(models[i].primary_key_column())
                        subQuery = subQuery.filter(
                            models[i].primary_key_column() == models[j].primary_key_column())
                        exists = session.query(subQuery.exists()).scalar()
                        if exists:
                            fixme.append(
                                [dbname, bodId, models[i], models[j], models[i].__tablename__, models[j].__tablename__])
    for m in fixme:
        print m

if __name__ == '__main__':
    main()
