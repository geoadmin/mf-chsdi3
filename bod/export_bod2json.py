#!/usr/bin/env python

import sys

try:
    import json,psycopg2,os
except ImportError:
    print "ERROR: Troubles exporting needed libraries"
    sys.exit(0)

from psycopg2.extras import RealDictCursor

dbconnectionstring = "dbname='bod_dev' port=5432 user='www-data' host='pg-sandbox.bgdi.ch'"

if __name__ == '__main__':
    bod_views = ['re3.topics',
                 're3.view_layers_js',
                 're3.view_catalog',
                 're3.view_bod_layer_info_de',
                 're3.view_bod_layer_info_fr',
                 're3.view_bod_layer_info_it',
                 're3.view_bod_layer_info_rm',
                 're3.view_bod_layer_info_en',
                 're3.view_bod_wmts_getcapabilities_de',
                 're3.view_bod_wmts_getcapabilities_fr',
                 're3.view_wms_service_metadata_de',
                 're3.view_wms_service_metadata_fr',
                 're3.view_bod_wmts_getcapabilities_themes_de',
                 're3.view_bod_wmts_getcapabilities_themes_fr',
                 're3.oereb_interlis_metadata']

    conn = psycopg2.connect(dbconnectionstring)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    for table in bod_views:
        print "export view %s ..." % table
        sql = "SELECT * FROM %s " % table
        # datetime has to be converted to text for the json encoding
        if table == 're3.oereb_interlis_metadata':
            sql = """
                    SELECT 
                    layer_id
                    , header
                    , footer
                    , bgdi_modified::text
                    , bgdi_created::text
                    , bgdi_modified_by
                    , bgdi_created_by
                    , bgdi_id
                    , data_created::text
                    , data_imported::text
                      FROM re3.oereb_interlis_metadata"""
        if table == 're3.topics':
            sql = """
                    SELECT
                    topic,
                    order_key,
                    lang,
                    selected_layers,
                    background_layers,
                    show_catalog,
                    staging
                    FROM re3.topics"""
        filename = "bod/%s.json" % table
        cur.execute(sql)
        f = open(filename, 'w')
        results = cur.fetchall()
        for r in results:
            for p in r:
                if type(r[p]) is list:
                    r[p] = ','.join(r[p])
        f.write(json.dumps(results,indent=2))
        f.close() 
