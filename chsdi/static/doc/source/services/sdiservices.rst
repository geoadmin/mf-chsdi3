.. _wmts_description:

WMTS
----

A RESTFul implementation of the `WMTS <http://www.opengeospatial.org/standards/wmts>`_ `OGC <http://www.opengeospatial.org/>`_ standard.
For detailed information, see See `WMTS OGC standard <http://www.opengeospatial.org/standards/wmts>`_

URL
^^^

- http://wmts.geo.admin.ch or  https://wmts.geo.admin.ch
- http://wmts0.geo.admin.ch or https://wmts0.geo.admin.ch
- http://wmts1.geo.admin.ch or https://wmts1.geo.admin.ch
- http://wmts2.geo.admin.ch or https://wmts2.geo.admin.ch
- http://wmts3.geo.admin.ch or https://wmts3.geo.admin.ch
- http://wmts4.geo.admin.ch or https://wmts4.geo.admin.ch

GetCapabilities
^^^^^^^^^^^^^^^

The GetCapabilites document provides informations on the service, along with layer description, both in german and french.

http://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml or https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml

http://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml?lang=fr or https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml?lang=fr

Parameters
^^^^^^^^^^

Only the RESTFul interface ist implemented. No KVP and SOAP.

A request is in the form:

    ``<protocol>://<ServerName>/<ProtocoleVersion>/<LayerName>/<Stylename>/<Time>/<TileMatrixSet>/<TileSetId>/<TileRow>/<TileCol>.<FormatExtension>``

with the following parameters:

===================    =============================   ==========================================================================
Parameter              Example                         Explanation
===================    =============================   ==========================================================================
Protocol               http ou https                   
ServerName             wmts[0-4].geo.admin.ch
Version                1.0.0                           WMTS protocol version
Layername              ch.bfs.arealstatistik-1997      See the WMTS `GetCapabilities <//wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_ document.
StyleName              default                         mostly constant
Time                   2010, 2010-01                   Date of tile generation in (ISO-8601). Some dataset will be updated quite often.
TileMatrixSet          21781 (constant)                EPSG code for LV03/CH1903
TileSetId              22                              Zoom level (see below)
TileRow                236
TileCol                284
FormatExtension        png                             Mostly png, except for some raster layer (pixelkarte and swissimage)
===================    =============================   ==========================================================================


The *<TileMatrixSet>* **21781** is as follow defined::

  MinX              420000
  MaxX              900000
  MinY               30000
  MaxY              350000
  TileWidth            256

With the *<tileOrigin>* in the top left corner of the bounding box.

===============  ========= ========= ============ ======== ======== =============== ================
Resolution [m]   Zoomlevel Map zoom  Tile width m Tiles X  Tiles Y    Tiles          Scale at 96 dpi
===============  ========= ========= ============ ======== ======== =============== ================
      4000            0                  1024000        1        1               1
      3750            1                   960000        1        1               1
      3500            2                   896000        1        1               1
      3250            3                   832000        1        1               1
      3000            4                   768000        1        1               1
      2750            5                   704000        1        1               1
      2500            6                   640000        1        1               1
      2250            7                   576000        1        1               1
      2000            8                   512000        1        1               1
      1750            9                   448000        2        1               2
      1500           10                   384000        2        1               2
      1250           11                   320000        2        1               2
      1000           12                   256000        2        2               4
       750           13                   192000        3        2               6
       650           14        0          166400        3        2               6    1 : 2'456'694
       500           15        1          128000        4        3              12    1 : 1'889'765
       250           16        2           64000        8        5              40    1 : 944'882
       100           17        3           25600       19       13             247    1 : 377'953
        50           18        4           12800       38       25             950    1 : 188'976
        20           19        5            5120       94       63           5'922    1 : 75'591
        10           20        6            2560      188      125          23'500    1 : 37'795
         5           21        7            1280      375      250          93'750    1 : 18'898
       2.5           22        8             640      750      500         375'000    1 : 9'449
         2           23        9             512      938      625         586'250    1 : 7'559
       1.5           24                      384     1250      834       1'042'500             
         1           25       10             256     1875     1250       2'343'750    1 : 3'780
       0.5           26       11             128     3750     2500       9'375'000    1 : 1'890
       0.25          27       12              64     7500     5000      37'500'000    1 : 945
       0.1           28       13            25.6    18750    12500     234'375'000    1 : 378
===============  ========= ========= ============ ======== ======== =============== ================



**Notes**

 #. The zoom level 24 (resolution 1.5m) has been generated, but is not currently used in the API.
 #. The zoom levels 27 and 28 (resolution 0.25m and 0.1m) are only available for a few layers, e.g. swissimage or cadastral web map. For the others 
    layers it is only a client zoom (tiles are stretched).

Result
^^^^^^

A tile.

http://wmts1.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/20110401/21781/20/58/70.jpeg or https://wmts1.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/20110401/21781/20/58/70.jpeg 
