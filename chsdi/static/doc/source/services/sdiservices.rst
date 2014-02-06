.. _metatdata_description:

Layers Metadata
---------------

This service provides metatdata for the available layers in the GeoAdmin API.

URL
^^^

https://api3.geo.admin.ch/rest/services/api/MapServer

Input Parameters
^^^^^^^^^^^^^^^^

RESTFul interface is available.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| searchText (optional)             | The text to search for in the layer description.                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| lang (optional)                   | The language metadata. Possible values: de (default), fr, it, rm, en                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
^^^^^^^^

- List all the layers available in the GeoAdmin API: `https://api3.geo.admin.ch/rest/services/api/MapServer <../../../rest/services/api/MapServer>`_
- List all the layers available in the GeoAdmin API where the word "wasser" is found in their description: `https://api3.geo.admin.ch/rest/services/api/MapServer?searchText=wasser <../../../rest/services/api/MapServer?searchText=wasser>`_

.. _legend_description:

Legend Resource
---------------

With a layer technical name, this service can be used to retrieve a legend.

URL
^^^

https://api3.geo.admin.ch/rest/services/api/MapServer/{layerID}/legend

Input Parameters
^^^^^^^^^^^^^^^^

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| lang (optional)                   | The language metadata. Possible values: de (default), fr, it, rm, en                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
^^^^^^^

- Get the legend for ch.bafu.bundesinventare-bln: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.bundesinventare-bln/legend <../../../rest/services/api/MapServer/ch.bafu.bundesinventare-bln/legend>`_

.. _identify_description:

Identify Features
-----------------

This service can be used to discover features at a specific location.

URL
^^^

https://api3.geo.admin.ch/rest/services/api/MapServer/identify

Input Parameters
^^^^^^^^^^^^^^^^

No more than 50 features can be retrieved per request.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| geometry (required)               | The geometry to identify on. The geometry is specified by the geometry type.              |
|                                   | This parameter is specified as a separated list of coordinates.                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| geometryType (required)           | The type of geometry to identify on. Possible values are:                                 |
|                                   | esriGeometryPoint or esriGeometryPolyline or esriGeometryPolygon or esriGeometryEnvelope  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| layers (optional)                 | The layers to perform the identify operation on. Per default query all the layers in the  |
|                                   | GeoAdmin API. Notation: all:"comma separated list of techincal layer names"               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| mapExtent (required)              | The extent of the map. (minX, minY, maxX, maxY)                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| imageDisplay (required)           | The screen image display parameters (width, height, and dpi) of the map.                  |
|                                   | GeoAdmin API dpi is 96.                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| tolerance (required)              | The tolerance in pixels around the specified geometry (used to create the buffer)         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| returnGeometry (optional)         | This parameter defines whether the geometry is returned or not. Default to "true".        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| geometryFormat (optional)         | Default to ESRI geometry format. Possible values are: "esrijson" or "geojson".            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| lang (optional)                   | The language metadata. Possible values: de (default), fr, it, rm, en                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
^^^^^^^^

- Identify all the features belonging to ch.bafu.bundesinventare-bln using a tolerance of 5 pixels around a point: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryPoint&geometry=653246,173129&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryPoint&geometry=653246,173129&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln>`_
- Identify all the features belonging to ch.bfs.arealstatistik-1985 using an enveloppe (or bounding box): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985 <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985>`_
- Same request than above but returned geometry format is GeoJSON: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&geometryFormat=geojson <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&geometryFormat=geojson>`_
- Same request than above but geometry is not returned: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&returnGeometry=false <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&returnGeometry=false>`_

.. _featureresource_description:

Feature Resource
----------------

With an ID and a layer technical name, this service can be used to retrieve a feature resource.

URL
^^^

https://api3.geo.admin.ch/rest/services/api/MapServer/{layerID}/{featureID}

Input Parameters
^^^^^^^^^^^^^^^^

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| lang (optional)                   | The language metadata. Possible values: de (default), fr, it, rm, en                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| geometryFormat (optional)         | Default to ESRI geometry format. Possible values are: "esrijson" or "geojson".            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| returnGeometry (optional)         | This parameter defines whether the geometry is returned or not. Default to "true".        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
^^^^^^^

- Get the feature with the ID 342 belonging to ch.bafu.bundesinventare-bln: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.bundesinventare-bln/362 <../../../rest/services/api/MapServer/ch.bafu.bundesinventare-bln/362>`_

.. _htmlpopup_description:

Htmlpopup Resource
------------------

With an ID and a layer technical name, this service can be used to retrieve an html popup. An html popup is an html formatted representation of the textual information about the feature.

URL
^^^

https://api3.geo.admin.ch/rest/services/api/MapServer/{layerID}/{featureID}/htmlPopup

Input Parameters
^^^^^^^^^^^^^^^^

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| lang (optional)                   | The language metadata. Possible values: de (default), fr, it, rm, en                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
^^^^^^^

- Get the html popup with the ID 342 belonging to ch.bafu.bundesinventare-bln: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup <../../../rest/services/api/MapServer/ch.bafu.bundesinventare-bln/362/htmlPopup>`_

.. _search_description:

Search
------

The search service can be used to search for locations, layers or features.

URL
^^^

https://api3.geo.admin.ch/rest/services/api/SearchServer

Description
^^^^^^^^^^^

The search service is separated in 3 different categories or types:

* The **location search** which is composed of the following geocoded locations:

  * Cantons, Cities and communes
  * All names as printed on the national map (`SwissNames <http://www.swisstopo.admin.ch/internet/swisstopo/en/home/products/landscape/toponymy.html>`_)
  * The districts
  * The ZIP codes
  * The addresses (!! the swiss cantons only allow websites of the federal governement to use the addresses search service !!)
  * The cadastral parcels
  * And optionally features belonging to a specified layer. The search is here performed within the attribute information of a layer using a search text.
* The **layer search** wich enables the search of layers belonging to the API.
* The **feature search** which is used to search through features descriptions. Note that you can also specify a bounding box to filter the features.
* The **feature identify** which is designed to efficiently discover the features of a layer based on an geographic extent.

Input parameters
^^^^^^^^^^^^^^^^

Only RESTFul interface is available.

**Location Search**

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| searchText (required)             | The text to search for.                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| type (required)                   | The type of performed search. Specify “locations” to perform a location search.           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| features (optional)               | A comma separated list of technical layer names.                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| bbox (optional)                   | A comma separated list of 4 coordinates representing the bounding box on which features   |
|                                   | should be filtered. (SRID: 21781)                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| returnGeometry (optional)         | This parameter defines whether the geometry is returned or not. You have to set this      |
|                                   | parameter to "false" if your website is not a federal one. Default to "true".             |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

**Layer Search**

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| searchText (required)             | The text to search for.                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| type (required)                   | The type of performed search.  Specify “layers” to perform a layer search.                |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| lang (optional)                   | The language metadata. Possible values: de (default), fr, it, rm, en                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

**Feature Search**

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| searchText (required)             | The text to search for. (in features detail field)                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| type (required)                   | The type of performed search. Specify “featuresearch” to perform a feature search.        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| bbox (optional)                   | A comma separated list of 4 coordinates representing the bounding box on which features   |
|                                   | should be filtered. (SRID: 21781)                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| features (required)               | A comma separated list of technical layer names.                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

**Feature Identify**

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| type (required)                   | The type of performed search. Specify “featureidentify” to perform a feature search.      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| bbox (optional)                   | A comma separated list of 4 coordinates representing the bounding box on which features   |
|                                   | should be filtered. (SRID: 21781)                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| features (optional)               | A comma separated list of technical layer names.                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
^^^^^^^^

- Search for locations matching the word “wabern”: `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=wabern&type=locations <../../../rest/services/api/SearchServer?searchText=wabern&type=locations>`_
- Search for locations and features matching the word “vd 446” (only features are filtered within the bbox are returned): `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=vd%20446&features=ch.astra.ivs-reg_loc&type=locations&bbox=551306.5625,167918.328125,551754.125,168514.625 <../../../rest/services/api/SearchServer?searchText=vd%20446&features=ch.astra.ivs-reg_loc&type=locations&bbox=551306.5625,167918.328125,551754.125,168514.625>`_
- Search for layers in French matching the word “géoïde” in their description: `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=géoïde&type=layers&lang=fr <../../../rest/services/api/SearchServer?searchText=géoïde&type=layers&lang=fr>`_ 
- Search for features matching word "433" in their description: `https://api3.geo.admin.ch/rest/services/api/SearchServer?features=ch.bafu.hydrologie-gewaesserzustandsmessstationen&type=featuresearch&searchText=433 <../../../rest/services/api/SearchServer?features=ch.bafu.hydrologie-gewaesserzustandsmessstationen&type=featuresearch&searchText=433>`_
- Search only for features belonging to the layer “ch.astra.ivs-reg_loc” (only using a bbox, no search text): `https://api3.geo.admin.ch/rest/services/api/SearchServer?features=ch.astra.ivs-reg_loc&type=featureidentify&bbox=551306.5625,167918.328125,551754.125,168514.625 <../../../rest/services/api/SearchServer?features=ch.astra.ivs-reg_loc&type=featureidentify&bbox=551306.5625,167918.328125,551754.125,168514.625>`_

.. _height_description:

Height
------

This service allows to obtain elevation information for a point. **Note: this service is not freely accessible (fee required)**.

URL
^^^
https://api3.geo.admin.ch/rest/services/height

Input Parameters
^^^^^^^^^^^^^^^^

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| easting (required)                | The Y position in CH1903 coordinate system (SRID: 21781)                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| northing (required)               | The X position in CH1903 coordinate system (SRIF: 21781)                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| elevation_model (optional)        | The elevation model. Three elevation models are available DTM25, DTM2 (swissALTI3D)       |
|                                   | and COMB (a combination of DTM25 and DTM2). Default to "DTM25"                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
^^^^^^^^

- `https://api3.geo.admin.ch/rest/services/height?easting=600000&northing=200000 <../../../rest/services/height?easting=600000&northing=200000>`_

.. _profile_description:

Profile
-------

This service allows to obtain elevation information for a polyline in CSV format. **Note: this service is not freely accessible (fee required)**.

URL
^^^
https://api3.geo.admin.ch/rest/services/profile.json (for json format)
https://api3.geo.admin.ch/rest/services/profile.csv  (for a csv)

Input Parameters
^^^^^^^^^^^^^^^^

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| geom (required)                   | A GeoJSON representation of a polyline (type = LineString)                                |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| elevation_models (optional)       | A comma separated list of elevation models. Three elevation models are available DTM25,   |
|                                   | DTM2 (swissALTI3D) and COMB (a combination of DTM25 and DTM2).  Default to "DTM25"        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| nb_points (optional)              | The number of points used for the polyline segmentation. Default "200"                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| offset (optional)                 | The offset value (INTEGER) in order to use the `exponential moving algorithm              |
|                                   | <http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average>`_ . For a given  |
|                                   | value the offset value specify the number of values before and after used to calculate    | 
|                                   | the average.                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| callback (optional)               | Only available for **profile.json**. The name of the callback function.                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
^^^^^^^

- A profile in JSON: `https://api3.geo.admin.ch/rest/services/profile.json?geom={"type"%3A"LineString"%2C"coordinates"%3A[[550050%2C206550]%2C[556950%2C204150]%2C[561050%2C207950]]} <../../../rest/services/profile.json?geom={"type"%3A"LineString"%2C"coordinates"%3A[[550050%2C206550]%2C[556950%2C204150]%2C[561050%2C207950]]}>`_
- A profile in CSV: `https://api3.geo.admin.ch/rest/services/profile.csv?geom={"type"%3A"LineString"%2C"coordinates"%3A[[550050%2C206550]%2C[556950%2C204150]%2C[561050%2C207950]]} <../../../rest/services/profile.csv?geom={"type"%3A"LineString"%2C"coordinates"%3A[[550050%2C206550]%2C[556950%2C204150]%2C[561050%2C207950]]}>`_

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

http://api3.geo.admin.ch/rest/services/api/1.0.0/WMTSCapabilities.xml

http://api3.geo.admin.ch/rest/services/api/1.0.0/WMTSCapabilities.xml?lang=fr

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
#. The zoom levels 27 and 28 (resolution 0.25m and 0.1m) are only available for a few layers, e.g. swissimage or cadastral web map. For the others layers it is only a client zoom (tiles are stretched).

Result
^^^^^^

A tile.

http://wmts1.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/20110401/21781/20/58/70.jpeg or https://wmts1.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/20110401/21781/20/58/70.jpeg 
