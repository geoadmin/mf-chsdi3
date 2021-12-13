:orphan:

.. raw:: html

  <head>
    <link href="../_static/custom.css" rel="stylesheet" type="text/css" />
  </head>


.. _oereb_feature_service:

OEREB/RDPPF: Feature Service
============================

This service can be used to discover features at a specific location.
The returned format is Interlis (XML).

.. warning::
  This service is only available for the following layers:

  Layers with model V2_0 (https://models.geo.admin.ch/V_D/OeREB/OeREBKRMtrsfr_V2_0.ili):
  - ch.astra.projektierungszonen-nationalstrassen_v2_0.oereb *(this layer has no data)*
  - ch.astra.baulinien-nationalstrassen_v2_0.oereb
  - ch.bav.projektierungszonen-eisenbahnanlagen_v2_0.oereb *(this layer has no data)*
  - ch.bav.baulinien-eisenbahnanlagen_v2_0.oereb *(this layer has no data)*
  - ch.bazl.projektierungszonen-flughafenanlagen_v2_0.oereb
  - ch.bazl.baulinien-flughafenanlagen_v2_0.oereb *(this layer has no data)*
  - ch.bazl.sicherheitszonenplan_v2_0.oereb
  - ch.vbs.kataster-belasteter-standorte-militaer_v2_0.oereb
  - ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb
  - ch.bav.kataster-belasteter-standorte-oev_v2_0.oereb
  - ch.bfe.projektierungszonen-starkstromanlagen_v2_0.oereb *(this layer has no data)*
  - ch.bfe.baulinien-starkstromanlagen_v2_0.oereb *(this layer has no data)*
 
  Layers with model V1_1 (https://models.geo.admin.ch/V_D/OeREB/replaced/OeREBKRMtrsfr_V1_1.ili):
  - ch.astra.projektierungszonen-nationalstrassen.oereb *(this layer has no data)*
  - ch.astra.baulinien-nationalstrassen.oereb
  - ch.bav.projektierungszonen-eisenbahnanlagen.oereb *(this layer has no data)*
  - ch.bav.baulinien-eisenbahnanlagen.oereb *(this layer has no data)*
  - ch.bazl.projektierungszonen-flughafenanlagen.oereb
  - ch.bazl.baulinien-flughafenanlagen.oereb *(this layer has no data)*
  - ch.bazl.sicherheitszonenplan.oereb
  - ch.vbs.kataster-belasteter-standorte-militaer.oereb
  - ch.bazl.kataster-belasteter-standorte-zivilflugplaetze.oereb
  - ch.bav.kataster-belasteter-standorte-oev.oereb
  
URL
***

http://api3.geo.admin.ch/rest/services/api/MapServer/identify

Input Parameters
****************

No more than 50 features can be retrieved per request.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **geometry (required)**           | The geometry to identify on. The geometry is specified by the geometry type.              |
|                                   | This parameter is specified as a separated list of coordinates.                           |
|                                   | The simple syntax (comma separated list of coordinates)                                   |
|                                   | and the complex one can be used.                                                          |
|                                   | (`ESRI syntax for geometries                                                              |
|                                   | <http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#//02r3000000n1000000>`_). |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **geometryType (required)**       | The type of geometry to identify on. Possible values are:                                 |
|                                   | esriGeometryPoint or esriGeometryPolyline or esriGeometryPolygon or esriGeometryEnvelope. |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **layers (required)**             | The layer to perform the identify operation on. Only one layer can be requested at a time |
|                                   | (notation: **all:{layerName}**).                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **mapExtent (required)**          | The extent of the map (minx, miny, maxx, maxy).                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **imageDisplay (required)**       | The screen image display parameters (width, height and dpi) of the map.                   |
|                                   | The mapExtent and the imageDisplay parameters are used by the server to calculate the     |
|                                   | distance on the map to search based on the tolerance in screen pixels.                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **tolerance (required)**          | The tolerance in pixels around the specified geometry. This parameter is used to create   |
|                                   | a buffer around the geometry. Therefore, a tolerance of 0 deactivates the buffer          |
|                                   | creation.                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **returnGeometry (optional)**     | This parameter defines whether the geometry is returned or not. Default to "true".        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **geometryFormat (optional)**     | Values: **interlis only for now!!**                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to “de”.                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
********

- Look for all the features of ch.bazl.projektierungszonen-flughafenanlagen_v2_0.oereb using a point: https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry=2682414.312,1257059.381&geometryType=esriGeometryPoint&layers=all:ch.bazl.projektierungszonen-flughafenanlagen_v2_0.oereb&mapExtent=2480000,1070000,2840000,1310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis&sr=2056
- Look for all the features of ch.bav.kataster-belasteter-standorte-oev_v2_0.oereb using a polygon: https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry={"rings"%20:%20[[%20[2675000,1245000],%20[2670000,1255000],%20[2680000,1260000],%20 [2690000,1255000],%20[2685000,1240000],%20[2675000,1245000]]]}&geometryType=esriGeometryPolygon&layers=all:ch.bav.kataster-belasteter-standorte-oev_v2_0.oereb&mapExtent=2480000,1070000,2840000,1310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis&sr=2056
- Look for all the features of ch.bazl.sicherheitszonenplan_v2_0.oereb using a bounding box (envelope): https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry=2575000,1109000,2610000,1127000&geometryType=esriGeometryEnvelope&layers=all:ch.bazl.sicherheitszonenplan_v2_0.oereb& mapExtent=2480000,1070000,2840000,1310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis&sr=2056
- Look for all the features of ch.astra.baulinien-nationalstrassen_v2_0.oereb using a bounding box (envelope): https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry=2599000,1200000,2604000,1203000&geometryType=esriGeometryEnvelope&layers=all: ch.astra.baulinien-nationalstrassen_v2_0.oereb& mapExtent=2480000,1070000,2840000,1310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis&sr=2056
