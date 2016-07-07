# -*- coding: utf-8 -*-

"""
This script can be used to scan the models in chsdi and return a list of dependent tables.

The output format is a csv with | delimiter and it contains the following attributes:
* layer name
* data source

Usage:

  .venv/bin/python scripts/scan_models.py > results.csv
"""

import re
from pyramid.paster import get_app


def getPGTables(layerId, engine, dbname, schema, tablename):
    sqlTemplate = 'EXPLAIN VERBOSE SELECT * FROM %s.%s'
    try:
        t = []
        sqlQuery = sqlTemplate %(schema, tablename) 
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
        for model in models:
            dbname = re.match(
                '^.*\/{1}([a-z]*)',
                model.metadata.__str__()).group(1)
            engine = engines.get(dbname)
            schema = model.__table_args__['schema'] if 'schema' in model.__table_args__ else 'public'
            tablename = model.__tablename__
            columnNames = [k.name for k in model.__table__.columns]
            tmp.append(getPGTables(layerId, engine, dbname, schema, tablename))
            tmpColumns += columnNames
        result = [item for sublist in tmp for item in sublist]
        result = sorted(list(set(result)))
        resultColumns = sorted(list(set(tmpColumns)))
        yield layerId, result, resultColumns


def main():
    # Load app to register the models
    app = get_app('production.ini')
    from chsdi.models import bodmap, oerebmap, perimetermap, engines
    print 'layerId|data|columns'
    dbsmap = [bodmap, oerebmap, perimetermap]
    for dbmap in dbsmap:
        for layerId, ref, refColumns in getTableReferences(dbmap, engines):
            print '%s|%s|%s' %(layerId, ','.join(ref), ','.join(refColumns))


if __name__ == '__main__':
    main()
