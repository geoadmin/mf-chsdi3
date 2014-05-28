#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
mapproxyfy.py Script to generate a MapProxy config file from a layer list.

"""

import os, sys, codecs
import cgi

import yaml
import json

from babel import support, Locale

try:
    import psycopg2
    import psycopg2.extras
    from psycopg2.extensions import register_type, UNICODE, connection
except ImportError:
    print 'You need psycopg2 to run this script. Try to install it with \'easy_install psycopg2\''
    sys.exit()

DEBUG = False



def get_conn():
    try:
        dsn = "dbname='bod' port=5432  host='pgcluster0t.bgdi.admin.ch'" 
        conn=psycopg2.connect(dsn)
        print 'Database connection established'
    except:
        print 'Critical Error: Unable to connect to the database. Have set your PGUSER and PGPASSWD ?\nExit'
        sys.exit()
    register_type(UNICODE)
    conn.set_client_encoding('UTF8')

    return conn



def get_layers(conn, sql="select * from re3.view_layers_js"):

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from re3.view_layers_js")

    return cur.fetchall()


try:
    with open(os.path.abspath('mapproxy/templates/mapproxy.tpl')) as f:
            y = yaml.load(f.read())

except EnvironmentError:
    print 'Critical error. Unable to open/read the mapproxy template file. Exit.'



# Translation
tr = support.Translations.load('chsdi/locale',locales=['de'], domain='chsdi')


conn = get_conn()

rows = get_layers(conn)



for row in rows:
    if row['layertype'] == 'wmts' and row['timestamps'] is not None:
        print row
        bod_layer_id = row['bod_layer_id']
        wmts_source_name = bod_layer_id
        wmts_cache_name = "%s_cache" % bod_layer_id
        layer_source_name = "%s_source" % bod_layer_id

        current_timestamp = row['timestamps'][0]
        
        dimensions = {'Time': {'default': current_timestamp, 'values': row['timestamps']}}
        title = cgi.escape(tr.ugettext(bod_layer_id))

        for matrix in ['mercator', 'etrs89', 'wgs84', 'lv95']:
            cache_name = "%s_cache_%s" % (bod_layer_id, matrix)
            layer_name = "%s.%s" % (bod_layer_id, matrix)

            grid_name = "lowres_%s" % matrix

            #layer config: one layer and one cache per each projection
            layer = {'name': layer_name, 'title': title, 'dimensions': dimensions, 'sources': [cache_name] }

            cache = {"sources": [wmts_cache_name], "format": "image/%s" %row['image_format'], "grids": [grid_name], "disable_storage": True, "meta_size": [4,4]}


            y['layers'].append(layer)
            y['caches'][cache_name] = cache

        # original source (one for all projection)
        wmts_url = "http://wmts3.geo.admin.ch/1.0.0/"+row['server_layername'] +"/default/"+current+"/21781/%(z)d/%(y)d/%(x)d.%(format)s"

        wmts_source = {"url": wmts_url, "type": "tile", "grid": "swisstopo-pixelkarte","http": {"headers": {"Referer": "http://mapproxy.geo.admin.ch"}}, \
                    "coverage": {   "bbox": [ 420000, 30000, 900000,350000 ], "bbox_srs": "EPSG:21781" } }

        wmts_cache = {"sources": [wmts_source_name], "format": "image/%s" %row['image_format'], "grids": ["swisstopo-pixelkarte"], "disable_storage": True}


        wmts_layer = {'name': bod_layer_id, 'title': title, 'dimensions': dimensions, 'sources': [wmts_cache_name] }


        if DEBUG:
            print layer

        y['layers'].append(wmts_layer)
        y['caches'][wmts_cache_name] = wmts_cache
        y['sources'][wmts_source_name] = wmts_source

if DEBUG:
    print json.dumps(y, sort_keys = False, indent = 4)

# outfile
with open('mapproxy/mapproxy.yaml', 'w') as o:
    o.write(yaml.safe_dump(y, encoding=None))

