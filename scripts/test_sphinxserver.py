import os
import sys
import socket
import six
from chsdi.lib.sphinxapi import sphinxapi

sys.tracebacklimit = 0


searchText ='@(title,detail,layer) "wand" | @(title,detail,layer) "^wand" | @(title,detail,layer) "wand$" | @(title,detail,layer) "^wand$" | @(title,detail,layer) "wand"~5 | @(title,detail,layer) "wand*" | @(title,detail,layer) "^wand*" | @(title,detail,layer) "wand*"~5 | @(title,detail,layer) "*wand*" | @(title,detail,layer) "^*wand*" | @(title,detail,layer) "*wand*"~5 & @topics (inspire | ech) & @staging prod | @staging integration | @staging test'
topicFilter='(inspire | ech)'
mapName='inspire'
index_name = 'layers_fr'
temp = []

sphinxhost = os.environ.get('SPHINXHOST', 'localhost')

sphinx = sphinxapi.SphinxClient()
sphinx.SetServer(sphinxhost, 9312)
sphinx.SetMatchMode(sphinxapi.SPH_MATCH_EXTENDED)
        

sphinx.SetConnectTimeout(10.0)

resp = sphinx._Connect()

if isinstance(resp, socket.socket):
        print("Connected to Sphinx server <{}>".format(sphinxhost))
else:
        print("Cannot connect to Sphinx server <{}>. Exit".format(sphinxhost))
        
try:
        temp = sphinx.Query(searchText, index=index_name)
except IOError:
        raise 
temp = temp['matches'] if temp is not None else temp

if temp is not None and len(temp) > 0:
    print("Querying Sphinx server successful")
    for l in temp:
        if six.PY2:
            print(l['attrs']['label'].encode("utf-8"))
        else:
            print(l['attrs']['label'])
else:
    print("Not the expected result while querying Sphinx Server")


    
