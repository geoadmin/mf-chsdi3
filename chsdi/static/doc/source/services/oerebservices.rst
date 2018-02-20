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

  - ch.astra.projektierungszonen-nationalstrassen.oereb *(this layer has no data)*
  - ch.bav.baulinien-eisenbahnanlagen.oereb *(this layer has no data)*
  - ch.bav.kataster-belasteter-standorte-oev.oereb
  - ch.bav.projektierungszonen-eisenbahnanlagen.oereb *(this layer has no data)*
  - ch.bazl.baulinien-flughafenanlagen.oereb *(this layer has no data)*
  - ch.bazl.kataster-belasteter-standorte-zivilflugplaetze.oereb
  - ch.bazl.projektierungszonen-flughafenanlagen.oereb
  - ch.bazl.sicherheitszonenplan.oereb

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

- Look for all the features of ch.bazl.projektierungszonen-flughafenanlagen.oereb using a point: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry=682414.31244,257059.38135&geometryType=esriGeometryPoint&layers=all:ch.bazl.projektierungszonen-flughafenanlagen.oereb&mapExtent=480000,70000,840000,310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis <../../../rest/services/api/MapServer/identify?geometry=682414.31244,257059.38135&geometryType=esriGeometryPoint&layers=all:ch.bazl.projektierungszonen-flughafenanlagen.oereb&mapExtent=480000,70000,840000,310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis>`_
- Look for all the features of ch.bazl.projektierungszonen-flughafenanlagen.oereb using a point in LV95: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry=2682414.31244,1257059.38135&geometryType=esriGeometryPoint&layers=all:ch.bazl.projektierungszonen-flughafenanlagen.oereb&mapExtent=2480000,170000,2840000,1310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis&sr=2056 <../../../rest/services/api/MapServer/identify?geometry=2682414.31244,1257059.38135&geometryType=esriGeometryPoint&layers=all:ch.bazl.projektierungszonen-flughafenanlagen.oereb&mapExtent=2480000,170000,2840000,1310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis&sr=2056>`_
- Look for all the features of ch.bav.kataster-belasteter-standorte-oev.oereb using a polygon:: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry={"rings"%20:%20[[%20[675000,245000],%20[670000,255000],%20[680000,260000],%20[690000,255000],%20[685000,240000],%20[675000,245000]]]}&geometryType=esriGeometryPolygon&layers=all:ch.bav.kataster-belasteter-standorte-oev.oereb&mapExtent=480000,70000,840000,310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis <../../../rest/services/api/MapServer/identify?geometry={"rings"%20:%20[[%20[675000,245000],%20[670000,255000],%20[680000,260000],%20[690000,255000],%20[685000,240000],%20[675000,245000]]]}&geometryType=esriGeometryPolygon&layers=all:ch.bav.kataster-belasteter-standorte-oev.oereb&mapExtent=480000,70000,840000,310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis>`_
- Look for all the features of ch.bazl.sicherheitszonenplan.oereb using a bounding box (envelope): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry=680000,254000,690000,260000&geometryType=esriGeometryEnvelope&layers=all:ch.bazl.sicherheitszonenplan.oereb&mapExtent=480000,70000,840000,310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis <../../../rest/services/api/MapServer/identify?geometry=680000,254000,690000,260000&geometryType=esriGeometryEnvelope&layers=all:ch.bazl.sicherheitszonenplan.oereb&mapExtent=480000,70000,840000,310000&imageDisplay=3600,2400,96&tolerance=0&geometryFormat=interlis>`_

