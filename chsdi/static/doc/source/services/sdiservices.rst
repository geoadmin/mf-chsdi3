.. raw:: html

  <head>
    <link href="../_static/custom.css" rel="stylesheet" type="text/css" />
    <script src="../examples/utils.js"></script>
  </head>


.. _rest_services:

API REST Services
=================

Most services are implementing or are heavily inspired by `ESRI GeoServices REST Specification <http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#//02r300000054000000>`_
or by the `Open Geospatial Consortium (OGC) <http://opengeospatial.org>`_.

All API REST endpoints supports only the following HTTP methods (unless specified):

+---------+------------------------------------------------------------------------------------------------+
| Method  | Description                                                                                    |
+=========+================================================================================================+
| GET     | Return the requested data.                                                                     |
+---------+------------------------------------------------------------------------------------------------+
| HEAD    | Return only HTTP headers of the GET request (no data in payload).                              |
+---------+------------------------------------------------------------------------------------------------+
| OPTIONS | Return only the HTTP headers for the communication options (e.g. CORS headers for preflight).  |
|         | No data in payload.                                                                            |
+---------+------------------------------------------------------------------------------------------------+

.. _metadata_description:

Layers Metadata
---------------

This service provides metadata for all the available layers in the GeoAdmin API.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer


Input Parameters
****************

RESTFul interface is available.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **searchText (optional)**         | The text to search for in the layer description.                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95), 4326 (WGS84)          |
|                                   | and 3857 (Web Pseudo-Mercator). Defaults to "21781".                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Response syntax
***************

Here is an example of response.

.. code-block:: javascript

    {
      "layers": [
        {
          "name": "Temperature monitoring stations",
          "fullName": "Water temperature monitoring stations",
          "idGeoCat": "4f10c35a-8fac-4000-ab6d-7a294284059a",
          "layerBodId": "ch.bafu.hydrologie-wassertemperaturmessstationen",
          "attributes": {
              "wmsUrlResource": "http://wms.geo.admin.ch/?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.3.0",
              "scaleLimit": "-",
              "inspireUpperAbstract": "Environnement, biology and geology | Space and population",
              "inspireName": "Environmental monitoring facilities | Human health and safety",
              "urlDetails": "http://www.bafu.admin.ch/hydrologie/01835/02122/index.html?lang=de",
              "abstract": "...",
              "inspireAbstract": "...",
              "dataOwner": "Federal Office for the Environment FOEN",
              "wmsContactAbbreviation": "swisstopo",
              "maps": "...",
              "wmsContactName": "Federal Office of Topography swisstopo",
              "dataStatus": "20130322",
              "inspireUpperName": "Environment biology and geology | Space and population",
              "urlApplication": "http://map.bafu.admin.ch"
          }
        }
      ],
      "tileInfo": {
        "origin": {
          "y": 350000,
          "x": 420000,
          "spatialReference": {
            "wkid": 21781
          }
        },
        "rows": 256,
        "format": "PNG,JPEG",
        "lods": [
            {
              "height": 1,
              "width": 1,
              "scale": 14285750.5715,
              "resolution": 4000,
              "level": 0
            }, ...
            {
                "height": 12500,
                "width": 18750,
                "scale": 357.1425,
                "resolution": 0.1,
                "level": 28
            }
        ],
        "spatialReference": {
          "wkid": 21781
        },
        "cols": 256,
        "dpi": 96,
        "compressionQuality": ""
      },
      "description": "Configuration for the map (topic) api",
      "fullExtent": {
        "xmin": 42000,
        "ymin": 30000,
        "ymax": 350000,
        "xmax": 900000,
        "spatialReference": {
            "wkid": 21781
        }
      },
      "units": "esriMeters",
      "initialExtent": {
        "xmin": 458000,
        "ymin": 76375,
        "ymax": 289125,
        "xmax": 862500,
        "spatialReference": {
          "wkid": 21781
        }
      },
      "spatialReference": {
        "wkid": 21781
      },
      "capabilities": "Map",
      "copyrightText": "Data api"
    }

Here is a description of the data one can find in the above response.

- **layers**: a list of object literals representing the layers

  - **name**: the name of the layer (short name less than 30 characters)
  - **fullName**: the layer's full name (not necessarily different from name)
  - **idGeoCat**: the associated metadata id in `GeoCat  <http://www.geocat.ch/geonetwork/srv/eng/geocat>`_
  - **layerBodId**: the technical name or BOD id
- **attributes**: the metadata attributes associated to a given layer

  - **wmsResource**: the WMS resource of the layer
  - **scaleLimit**: the scale at which the layer is valid
  - **inspireUpperAbstract**: the abstract of the `INSPIRE <https://www.geo.admin.ch/en/geo-information-switzerland/geodata-index-inspire.html>`_ category (first level)
  - **inprireName**: the name of the `INSPIRE <https://www.geo.admin.ch/en/geo-information-switzerland/geodata-index-inspire.html>`_ category
  - **urlDetails**: link to the official details page
  - **bundCollectionNumber**: the collection number
  - **dataOwner**: the data owner
  - **inprieAbstract**: the abstract of the `INSPIRE <https://www.geo.admin.ch/en/geo-information-switzerland/geodata-index-inspire.html>`_ category the layer belongs to
  - **absctract**: the layer absctract
  - **wmsContactAbbreviation**: the abbreviation contact for the WMS resource
  - **downloadUrl**: the link where the data can be downloaded
  - **maps**: the projects in which this layer is accessible
  - **wmsContactName**: the contact name for the WMS resource
  - **dataStatus**: the date of the latest data update
  - **bundCollectionName**: the collection name
  - **inspireUpperName**: the name of the `INSPIRE <https://www.geo.admin.ch/en/geo-information-switzerland/geodata-index-inspire.html>`_ category (first level)
  - **urlApplication**: the application where this layer is published
  - **tileInfo**: WMTS general information in json format. Note that this section is always identical and is not tied to a particular "map" like in ESRI specifications.


Examples
********

- List all the layers available in the GeoAdmin API: `https://api3.geo.admin.ch/rest/services/api/MapServer <../../../rest/services/api/MapServer>`_
- List all the layers available in the GeoAdmin API where the word "wasser" is found in their description: `https://api3.geo.admin.ch/rest/services/api/MapServer?searchText=wasser <../../../rest/services/api/MapServer?searchText=wasser>`_
- Find a layer by `geocat ID <http://www.geocat.ch/geonetwork/srv/eng/geocat>`_: `https://api3.geo.admin.ch/rest/services/api/MapServer?searchText=f198f6f6-8efa-4235-a55f-99767ea0206c  <../../../rest/services/api/MapServer?searchText=f198f6f6-8efa-4235-a55f-99767ea0206c>`_

.. _layer_attributes_description:

----------

Layer Attributes
----------------

This service is used to expose the attributes names that are specific to a layer. This service is especially useful when combined wit
h the find service.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}

Input Parameters
****************

RESTFul interface is available.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. (Defaults to de if browser language  |
|                                   | does not match any of the possible values)                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
*******

Get the all the available attributes names of the municipal boundaries: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill <../../../rest/services/api/MapServer/ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`_

.. _legend_description:

----------

Legend Resource
---------------

With a layer ID (or technical name), this service can be used to retrieve a legend.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/legend

Input Parameters
****************

No css styling is provided per default so that you can use your own.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. (Defaults to de if browser language  |
|                                   | does not match any of the possible values)                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
*******

- Get the legend for ch.bafu.nabelstationen: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/legend <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/legend>`_
- Get the same legend using JSONP: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/legend?callback=callback <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/legend?callback=callback>`_

.. _identify_description:

----------

Identify Features
-----------------

This service can be used to discover features at a specific location. Here is a `complete list of layers <../../../api/faq/index.html#which-layers-have-a-tooltip>`_ for which this service is available.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer/identify

Input Parameters
****************

No more than 50 features can be retrieved per request.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **geometry (required)**           | The geometry to identify on. The geometry is specified by the geometry type.              |
|                                   | This parameter is specified as a separated list of coordinates. The simple syntax (comma  |
|                                   | separated list of coordinates) and the complex one can be used. (`ESRI syntax for         |
|                                   | geometries                                                                                |
|                                   | <http://resources.arcgis.com/en/help/arcgis-rest-api/index.html#//02r3000000n1000000>`_)  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **geometryType (required)**       | The type of geometry to identify on. Supported values are:                                |
|                                   | esriGeometryPoint or esriGeometryPolyline or esriGeometryPolygon or esriGeometryEnvelope. |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **layers (optional)**             | The layers to perform the identify operation on. Per default query all the layers in the  |
|                                   | GeoAdmin API. Notation: all:"comma separated list of technical layer names".              |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **mapExtent**                     | The extent of the map. (minx, miny, maxx, maxy). Optional if *tolerance=0*. Default to    |
|    **(required/optional)**        | The mapExtent and the imageDisplay parameters are used by the server to calculate the     |
|                                   | 0,0,0,0                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **imageDisplay**                  | The screen image display parameters (width, height, and dpi) of the map.                  |
|    **(required/optional)**        | The mapExtent and the imageDisplay parameters are used by the server to calculate the     |
|                                   | the distance on the map to search based on the tolerance in screen pixels.                |
|                                   | Optional if *tolerance=0*. Default to 0,0,0                                               |
|                                   |                                                                                           |
|                                   | The combination of *mapExtent* and *imageDisplay* is used to compute a *resultion* or     |
|                                   | *scale*. Some layer have *scale* dependant geometries                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **tolerance (required)**          | The tolerance in pixels around the specified geometry. This parameter is used to create   |
|                                   | a buffer around the geometry. Therefore, a tolerance of 0 deactivates the buffer          |
|                                   | creation.                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **returnGeometry (optional)**     | This parameter defines whether the geometry is returned or not. Default to "true".        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **geometryFormat (optional)**     | Returned geometry format.                                                                 |
|                                   | Default to ESRI geometry format. Supported values are: "esrijson" or "geojson".           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **offset (optional)**             | Offset for the first record (if more than 50 records)                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95), 4326 (WGS84)          |
|                                   | and 3857 (Web Pseudo-Mercator). Defaults to "21781".                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **layerDefs (optional)**          | Filter features with an expression.                                                       |
|                                   | Syntax: `{ "<layerId>" : "<layerDef1>" }` where `<layerId>` must correspond to the layer  |
|                                   | specified in `layers`.                                                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Tolerance, mapExtent and imageDisplay
*************************************

If *tolerance=0*, *imageDisplay* and *mapExtent* are generaly not needed, except to get models which are scale dependant, e.g.
displaying points at smaller scales and polygons ar larger one.
If using *tolerance>0*, both *imageDisplay* and *mapExtent* must be set to meaningfull values. As the *tolerance* is in pixels,
these value are used to convert it to map units, _i.e._ meters.

The following table summarize the various combinations:

+--------------------+------------------------------------------+-----------------------------------------+
|                    | imageDisplay=0,0,0  mapExtent=0,0,0,0    |  imageDisplay=1,1,1  mapExtent=1,1,1,1  |
+====================+==========================================+=========================================+
| **tolerance=0**    | No buffer & No scale                     |  No buffer & but scale                  |
+--------------------+------------------------------------------+-----------------------------------------+
| **tolerance>0**    | Forbidden                                |  Buffer & Scale                         |
+--------------------+------------------------------------------+-----------------------------------------+


Filters
*******

You may filter by attributes with **layerDefs** on `queryable layers <../api/faq/index.html#which-layers-are-queryable>`_.

To check which attributes are availables, their types and examples values for a given searchable layer, you may use the `attributes services <../../../services/sdiservices.html#layer-attributes>`_.

For instance, the layer **ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill** has the following two attributes:

    http://api3.geo.admin.ch/rest/services/api/MapServer/ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill

.. code-block:: javascript

    {
       "fields":[
          {
             "values":[
                "Epalinges",
                "Ependes (VD)",
                "Grub (AR)",
                "Leuk",
                "Uesslingen-Buch"
             ],
             "alias":"Name",
             "type":"VARCHAR",
             "name":"gemname"
          },
          {
             "values":[
                3031,
                4616,
                5584,
                5914,
                6110
             ],
             "alias":"BFS-Nummer",
             "type":"INTEGER",
             "name":"id"
          }
       ],
       "id":"ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill",
       "name":"Municipal boundaries"
    }


layerDefs syntax
****************

The syntax of the `layerDefs` parameter is a json with the layername as key and the filter expression as value:

::

  {"<layername>":"<filter_expression>"}

The filter expression can consist of a single expression of the form `<attribute> <operator> <value>` or several of these expressions combined with boolean operators `and` and `or`, e.g.

::

  state='open' and startofconstruction>='2018-10'

`<attribute>` must be one of the queryable attributes, the type of `<value>` must correspond the the type of the queryable attribute (see above) and `<operator>` can be one of

+-----------------+--------------------------------------+----------------------------------------------------------------+
|  Data type      |                Operators             |     Examples                                                   |
+=================+======================================+================================================================+
|  varchar        |  =, +=, like, ilike, not like        |  toto ='3455 Kloten', toto ilike '%SH%', toto is null          |
|                 |  not ilike, is null, is not null     |  toto ilike 'SH%'                                              |
+-----------------+--------------------------------------+----------------------------------------------------------------+
|  number         |  =, <, >, >=, <=, !=                 |  tutu >= 2.4 tutu<5                                            |
+-----------------+--------------------------------------+----------------------------------------------------------------+
|  boolean        |  is (true|false), is not (true|false)|  tata is not false                                             |
+-----------------+--------------------------------------+----------------------------------------------------------------+


Correct encoding
****************

It's important, that the parameters are correctly serialized and url-encoded, e.g.

.. code-block:: python

    >>> import json
    >>> import urllib.parse
    >>> params = {
            "ch.swisstopo.amtliches-strassenverzeichnis": "zip_label = '8302 Kloten'"
        }
    >>> print(json.dumps(params))
    {"ch.swisstopo.amtliches-strassenverzeichnis": "zip_label = '8302 Kloten'"}
    >>> print(urllib.parse.quote(json.dumps(params)))
    %7B%22ch.swisstopo.amtliches-strassenverzeichnis%22%3A%20%22zip_label%20%3D%20%278302%20Kloten%27%22%7D
    >>> print('&layerDefs={}'.format(urllib.parse.quote(json.dumps(params))))
    &layerDefs=%7B%22ch.swisstopo.amtliches-strassenverzeichnis%22%3A%20%22zip_label%20%3D%20%278302%20Kloten%27%22%7D


Examples
********

- Identify all the features belonging to ch.bafu.nabelstationen using a tolerance of 5 pixels around a point: `https://api3.geo.admin.ch/rest/services/all/MapServer/identify?geometry=678250,213000&geometryFormat=geojson&geometryType=esriGeometryPoint&imageDisplay=1391,1070,96&lang=fr&layers=all:ch.bafu.nabelstationen&mapExtent=312250,-77500,1007750,457500&returnGeometry=true&tolerance=5 <../../../rest/services/all/MapServer/identify?geometry=678250,213000&geometryFormat=geojson&geometryType=esriGeometryPoint&imageDisplay=1391,1070,96&lang=fr&layers=all:ch.bafu.nabelstationen&mapExtent=312250,-77500,1007750,457500&returnGeometry=true&tolerance=5>`_
- Identify all the features belonging to ch.bfs.arealstatistik intersecting an envelope (or bounding box): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik>`_
- Identify all the features belonging to ch.bafu.bundesinventare-bln a polyline: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry={"paths":[[[675000,245000],[660000,260000],[620000,250000]]]}&geometryType=esriGeometryPolyline&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln <../../../rest/services/api/MapServer/identify?geometry={"paths":[[[675000,245000],[660000,260000],[620000,250000]]]}&geometryType=esriGeometryPolyline&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln>`_
- Identify all the features belonging to ch.bafu.bundesinventare-bln intersecting a polygon: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry={"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}&geometryType=esriGeometryPolygon&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln <../../../rest/services/api/MapServer/identify?geometry={"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}&geometryType=esriGeometryPolygon&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln>`_
- Same request for ch.bfs.arealstatistik as above but returned geometry format is GeoJSON: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik&geometryFormat=geojson <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik&geometryFormat=geojson>`_
- Same request for ch.bfs.arealstatistik as above but geometry is not returned: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik&returnGeometry=false <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik&returnGeometry=false>`_
- Filter features with **layerDefs**: `https://api3.geo.admin.ch/rest/services/all/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=2548945.5,1147956,2549402,1148103.5&geometryFormat=geojson&imageDisplay=1367,949,96&lang=en&layers=all:ch.swisstopo.amtliches-strassenverzeichnis&mapExtent=2318250,952750,3001750,1427250&returnGeometry=false&sr=2056&tolerance=5&layerDefs={"ch.swisstopo.amtliches-strassenverzeichnis":"stn_label+ilike+'%Corniche%'"} <../../../rest/services/all/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=2548945.5,1147956,2549402,1148103.5&geometryFormat=geojson&imageDisplay=1367,949,96&lang=en&layers=all:ch.swisstopo.amtliches-strassenverzeichnis&mapExtent=2318250,952750,3001750,1427250&returnGeometry=false&sr=2056&tolerance=5&layerDefs={"ch.swisstopo.amtliches-strassenverzeichnis":"stn_label+ilike+%27%Corniche%%27"}>`_



Examples of Reverse Geocoding
*****************************

The service identify can be used for Reverse Geocoding operations. Here is a `list of all the available layers <../../../api/faq/index.html#which-layers-are-available>`_.

- Perform an identify request to find the districts intersecting a given envelope geometry (no buffer): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill&returnGeometry=false  <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill&returnGeometry=false>`_
- Perform an identify request to find the municipal boundaries and ZIP (PLZ or NPA) intersecting with a point (no buffer): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryPoint&geometry=548945.5,147956&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo-vd.ortschaftenverzeichnis_plz&returnGeometry=false <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryPoint&geometry=548945.5,147956&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo-vd.ortschaftenverzeichnis_plz&returnGeometry=false>`_
- Reverse geocoding an `address` with a point (no buffer): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?mapExtent=0,0,100,100&imageDisplay=100,100,100&tolerance=1&geometryType=esriGeometryPoint&geometry=600968.625,197426.921875&layers=all:ch.bfs.gebaeude_wohnungs_register&returnGeometry=false <../../../rest/services/api/MapServer/identify?mapExtent=0,0,100,100&imageDisplay=100,100,100&tolerance=1&geometryType=esriGeometryPoint&geometry=600968.625,197426.921875&layers=all:ch.bfs.gebaeude_wohnungs_register&returnGeometry=false>`_


Simulate a search radius
************************

Equation:

::

  SearchRadius = Max(MapWidthInMeters / ScreenWidthInPx, MapHeightInMeters / ScreenHeightInPx) * toleranceInPx

For instance if one wants a radius of 5 meters:

::

  Max(100 / 100, 100 / 100) * 5 = 5


So you would set:

::

 mapExtent=0,0,100,100&imageDisplay=100,100,100&tolerance=5&geometryType=esriGeometryPoint&geometry=548945,147956 to perform an identify request with a search radius of 5 meters around a given point.

.. _find_description:

----------

Find
----

This service is used to search the attributes of features. Each result include a feature ID, a layer ID, a layer name, a geometry (optionally) and attributes in the form of name-value pair.
Here is a `complete list of layers <../../../api/faq/index.html#which-layers-have-a-tooltip>`_ for which this service is available.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer/find

Input Parameters
****************

One layer, one search text and one attribute.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **layer (required)**              | A layer ID (only one layer at a time can be specified).                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **searchText (required)**         | The text to search for (one can use numerical values as well).                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **searchField (required)**        | The name of the field to search (only one search field can be searched at a time).        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **contains (optional)**           | If false, the operation searches for an exact match of the searchText string. An exact    |
|                                   | match is case sensitive. Otherwise, it searches for a value that contains the searchText  |
|                                   | string provided. This search is not case sensitive. The default is true.                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **geometryFormat (optional)**     | Returned geometry format.                                                                 |
|                                   | Default to ESRI geometry format. Supported values are: "esrijson" or "geojson".           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **returnGeometry (optional)**     | This parameter defines whether the geometry is returned or not. Default to "true".        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95), 4326 (WGS84)          |
|                                   | and 3857 (Web Pseudo-Mercator). Defaults to "21781".                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **layerDefs (optional)**          | Filter features with an expression (see                                                   |
|                                   | `identify <../../../services/sdiservices.html#identify-features>`_)                       |
|                                   | Syntax: `{ "<layerId>" : "<layerDef1>"}`                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
********
- Search for “Lavaux” in the field “bln_name” of the layer “ch.bafu.bundesinventare-bln” (infix match): `https://api3.geo.admin.ch/rest/services/api/MapServer/find?layer=ch.bafu.bundesinventare-bln&searchText=Lavaux&searchField=bln_name&returnGeometry=false  <../../../rest/services/api/MapServer/find?layer=ch.bafu.bundesinventare-bln&searchText=Lavaux&searchField=bln_name&returnGeometry=false>`_
- Search for “12316” in the field “egid” of the layer “ch.bfs.gebaeude_wohnungs_register” (infix match): `https://api3.geo.admin.ch/rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=123164&searchField=egid&returnGeometry=false  <../../../rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=123164&searchField=egid&returnGeometry=false>`_
- Search for “123164” in the field “egid” of the layer “ch.bfs.gebaeude_wohnungs_register” (exact match): `https://api3.geo.admin.ch/rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=1231641&searchField=egid&returnGeometry=false&contains=false <../../../rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=1231641&searchField=egid&returnGeometry=false&contains=false>`_
- Search for the Talstrasse in Commune 'Full-Reuenthal': `https://api3.geo.admin.ch/rest/services/api/MapServer/find?layer=ch.swisstopo.amtliches-strassenverzeichnis&searchText=Talstrasse&searchField=stn_label&returnGeometry=false&contains=false&layerDefs={"ch.swisstopo.amtliches-strassenverzeichnis": "com_fosnr = 4307"} <../../../rest/services/api/MapServer/find?layer=ch.swisstopo.amtliches-strassenverzeichnis&searchText=Talstrasse&searchField=stn_label&returnGeometry=false&contains=false&layerDefs=%7B"ch.swisstopo.amtliches-strassenverzeichnis"%3A%20"com_fosnr%20%3D%204307"%7D>`_

.. _featureresource_description:

----------

Feature Resource
----------------

With an ID (or several in a comma separated list) and a layer ID (technical name), this service can be used to retrieve a feature resource.
Here is a `complete list of layers <../../../api/faq/index.html#which-layers-have-a-tooltip>`_ for which this service is available.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/{featureId},{featureId}

Input Parameters
****************

RESTFul interface is available.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **geometryFormat (optional)**     | Returned geometry format.                                                                 |
|                                   | Default to ESRI geometry format. Supported values are: "esrijson" or "geojson".           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **returnGeometry (optional)**     | This parameter defines whether the geometry is returned or not. Default to "true".        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95), 4326 (WGS84)          |
|                                   | and 3857 (Web Pseudo-Mercator). Defaults to "21781".                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
*******

- Get the feature with the ID RIG belonging to ch.bafu.nabelstationen: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/RIG <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/RIG>`_
- Get several features with IDs RIG and LAU belonging to ch.bafu.bundesinventar-bln: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/RIG,LAU <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/RIG,LAU>`_
- A `GeoJSON` in `EPSG:4326`: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/RIG,LAU?sr=4326&geometryFormat=geojson <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/RIG,LAU?sr=4326&geometryFormat=geojson>`_

.. _htmlpopup_description:

----------

Htmlpopup Resource
------------------

With an ID and a layer ID (technical name), this service can be used to retrieve an html popup. An html popup is an html formatted representation of the textual information about the feature.
Here is a `complete list of layers <../../../api/faq/index.html#which-layers-have-a-tooltip>`_ for which this service is available.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/{featureId}/htmlPopup

Input Parameters
****************

No css styling is provided per default so that you can use your own.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95), 4326 (WGS84)          |
|                                   | and 3857 (Web Pseudo-Mercator). Defaults to "21781".                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **time (optional)**               | Time (YYYY) to filter out time enabled layers, e.g. LUBIS. Defaults to "none".            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **mapExtent (optional)**          | The extent of the map. (minx, miny, maxx, maxy).                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **imageDisplay (optional)**       | The screen image display parameters (width, height, and dpi) of the map.                  |
|                                   | The combination of *mapExtent* and *imageDisplay* are used to compute a *resolution* or   |
|                                   | *scale*. Some layer have *scale* dependant htmlpopup responses                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **coord (optional)**              | The coordinates of interest (x, y). Some layers with external datasource need to know the |
|                                   | cooridnates of the click on the map (p.e. ch.bafu.gefahren-aktuelle_erdbeben)             |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
*******

- Get the html popup with the feature ID RIG belonging to layer ch.bafu.nabelstationen: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/RIG/htmlPopup <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/RIG/htmlPopup>`_

.. _search_description:

----------

Search
------

The search service can be used to search for locations, layers or features.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/SearchServer

Description
***********

The search service is separated in 3 various categories or types:

* The **location search** which is composed of the following geocoded locations:

  * Cantons, Cities and communes
  * All names as printed on the national map (`SwissNames <https://www.swisstopo.admin.ch/en/geodata/landscape/names3d.html>`_)
  * The districts
  * The ZIP codes
  * The addresses
  * The cadastral parcels
* The **layer search** wich enables the search of layers belonging to the GeoAdmin API.
* The **feature search** which is used to search through features descriptions. Note: you can also specify a bounding box to filter the features. (`Searchable layers <../../../api/faq/index.html#which-layers-are-searchable>`_)

Input parameters
****************

Only RESTFul interface is available.

**Location Search**

+-------------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                          | Description                                                                               |
+=====================================+===========================================================================================+
| **searchText (required/optional)**  | Must be provided if the `bbox` is not. The text to search for. Maximum of 10 words.       |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **type (required)**                 | The type of performed search. Specify `locations` to perform a location search.           |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **bbox (required/optional)**        | Must be provided if the `searchText` is not. A comma separated list of 4 coordinates      |
|                                     | representing the bounding box on which features should be filtered (SRID: 21781 or 2056). |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **sortbbox (optional)**             | When `bbox` is specified and this parameter is "true", then the ranking of the results is |
|                                     | performed according to the distance between the locations and the center of the bounding  |
|                                     | box. Default to "true".                                                                   |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **returnGeometry (optional)**       | This parameter defines whether the geometry is returned or not. Default to "true".        |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **origins (optional)**              | A comma separated list of origins. Possible origins are:                                  |
|                                     | zipcode,gg25,district,kantone,gazetteer,address,parcel                                    |
|                                     | A description of the origins can be found hereunder. Per default all origins are used.    |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **limit (optional)**                | The maximum number of results to retrive per request (Max and default limit=50)           |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                   | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95), 4326 (WGS84)          |
|                                     | and 3857 (Web Pseudo-Mercator). Defaults to "21781".                                      |
|                                     | When a *returnGeometry* is set, its coordiantes will be returned in this *sr*.            |
|                                     | When setting a *bbox*, its coordinates have to be in the corresponding *sr*.              |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **geometryFormat (optional)**       | Set to *geojson* if you want the service to return a GeoJSON `FeatureCollection`.         |
|                                     | Geometries will be returned in the *sr* projection.                                       |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**             | The name of the callback function.                                                        |
+-------------------------------------+-------------------------------------------------------------------------------------------+

**Layer Search**

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **searchText (required)**         | The text to search for. Maximum of 10 words allowed.                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **type (required)**               | The type of performed search. Specify `layers` to perform a layer search.                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language metadata. Supported values: de (default), fr, it, rm, en.                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **limit (optional)**              | The maximum number of results to retrive per request (Max and default limit=30)           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95), 4326 (WGS84)          |
|                                   | and 3857 (Web Pseudo-Mercator). Defaults to "21781". When setting *geometryFormat*        |
|                                   | to *geosjon*, the coordinates are returned in the corresponding *sr*.                     |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **geometryFormat (optional)**     | Set to *geojson* if you want the service to return a GeoJSON `FeatureCollection`.         |
|                                   | Geometries will be returned in the *sr* projection.                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

**Feature Search**

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **searchText (required)**         | The text to search for (in features detail field). Maximum of 10 words allowed.           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **type (required)**               | The type of performed search. Specify `featuresearch` to perform a feature search.        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **bbox (optional)**               | A comma separated list of 4 coordinates representing the bounding box according to which  |
|                                   | features should be ordered (SRID: 21781 or 2056).                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sortbbox (optional)**           | When `bbox` is specified and this parameter is "true", then the ranking of the results is |
|                                   | performed according to the distance between the locations and the center of the bounding  |
|                                   | box. Default to "true".                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **features (required)**           | A comma separated list of technical layer names.                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **limit (optional)**              | The maximum number of results to retrive per request (Max and default limit=20)           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03) and 2056 (LV95)                     |
|                                   | Defaults to "21781".                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **geometryFormat (optional)**     | Set to *geojson* if you want the service to return a GeoJSON `FeatureCollection`.         |
|                                   | Geometries will be returned in the *sr* projection.                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Response syntax
***************

The results are presented as a list of object literals. Here is an example of response for location search.

.. code-block:: javascript

  results: [
    {
      id: 206,
      weight: 12,
      attrs: {
        origin: "gg25",
        layerBodId: "ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill",
        featureId: "351",
        detail: "bern be",
        rank: 2,
        geom_st_box2d: "BOX(589008 196443.046875,604334.3125 204343.5)",
        num: 1,
        y: 598637.3125,
        x: 200393.28125,
        label: "<b>Bern (BE)</b>"
      }
    }
  ]

or a valid `GeoJSON` `FeatureCollection` if parameter `geometryFormat=geojson` is present

.. code-block:: javascript

    {
     "type": "FeatureCollection",
     "bbox": [
      601612,
      197186.8,
      601612,
      197186.8
     ],
     "features": [{
      "geometry": {
       "type": "Point",
       "coordinates": [
        197186.8125,
        601612.0625
       ]
      },
      "properties": {
       "origin": "gazetteer",
       "geom_quadindex": "021300220330313020221",
       "weight": 1,
       "zoomlevel": 10,
       "lon": 7.459799289703369,
       "detail": "wabern koeniz",
       "rank": 5,
       "lat": 46.925777435302734,
       "num": 1,
       "y": 601612.0625,
       "x": 197186.8125,
       "label": "<i>Populated Place</i> <b>Wabern</b> (BE) - Köniz",
       "id": 215754
      },
      "type": "Feature",
      "id": 215754,
      "bbox": [
       601612,
       197186.8,
       601612,
       197186.8
      ]
     }]
    }


Here is a description of the data one can find in the above response.

- **id**: This is an internal value and therefore shouldn't be used.
- **weight**:  The `weight` is dynamically computed according to the `searchText` that is provided. It informs the user about how close an entry is to the provided `searchText`.
- **attrs**: The attributes associated to a given entry.

  - **origin**: This attribute refers to the type of data an entry stands for.
  - **layerBodId**: The id of the associated layer (if any)
  - **featureId**: If available the object's Id can be combined with the `layerBodId` to collect more information about a feature.
  - **detail**: The search field
  - **rank**: A different `rank` is associated to each origin. Results are always ordered in ascending ranks.
  - **geom_st_box2d**: This attribute is in is in CH1903 / LV03 (EPSG:21781) reference system and represents the bounding box of the associated geometry.
  - **num**: This attribute is only valid for locations with **address** `origin`. It refers to the street number.
  - **x and y**: These attributes represent the coordinates of an entry. If an object's entry is a line or a polygon, those coordinates will always be on the underlying geometry.
  - **label**: The html label for an entry.

Here is a list of possible origins sorted in ascending ranking order:

- zipcode (ch.swisstopo-vd.ortschaftenverzeichnis_plz)
- gg25 (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)
- district (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)
- kantone (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)
- gazetteer (ch.swisstopo.swissnames3d, ch.bav.haltestellen-oev)
- address (ch.bfs.gebaeude_wohnungs_register with EGID or use prefix 'addresse', 'adresse', 'indirizzo', 'address' without EGID)
- parcel (use prefix "parcel", "parzelle", "parcelle" or "parcella" in your requests to filter out other origins)

Prefix filtering cannot be combined with parameter `origins`.

Examples
********

- Search for locations matching the word “wabern”: `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=wabern&type=locations <../../../rest/services/api/SearchServer?searchText=wabern&type=locations>`_
- Search for locations of type "parcel" and "district" (the origins): `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=bern&origins=parcel,district&type=locations <../../../rest/services/api/SearchServer?searchText=bern&origins=parcel,district&type=locations>`_
- Search for locations within a given map extent (the `bbox`): `https://api3.geo.admin.ch/rest/services/api/SearchServer?bbox=551306.5625,167918.328125,551754.125,168514.625&type=locations  <../../../rest/services/api/SearchServer?bbox=551306.5625,167918.328125,551754.125,168514.625&type=locations>`_
- Search for layers in French matching the word “géoïde” in their description: `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=géoïde&type=layers&lang=fr <../../../rest/services/api/SearchServer?searchText=géoïde&type=layers&lang=fr>`_
- Search for features matching word "433" in their description: `https://api3.geo.admin.ch/rest/services/api/SearchServer?features=ch.bafu.hydrologie-gewaesserzustandsmessstationen&type=featuresearch&searchText=433 <../../../rest/services/api/SearchServer?features=ch.bafu.hydrologie-gewaesserzustandsmessstationen&type=featuresearch&searchText=433>`_
- Get a GeoJSON for locations matching the word “wabern”: `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=wabern&type=locations&geometryFormat=geojson <../../../rest/services/api/SearchServer?searchText=wabern&type=locations&geometryFormat=geojson>`_
- Get a Webmercator GeoJSON: `https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=wabern&type=locations&geometryFormat=geojson&sr=3857 <../../../rest/services/api/SearchServer?searchText=wabern&type=locations&geometryFormat=geojson&sr=3857>`_
- Input `bbox` may also be in `LV95`: `https://api3.geo.admin.ch/rest/services/api/SearchServer?bbox=2551306.5625,1167918.328125,2551754.125,1168514.625&type=locations&sr=2056 <../../../rest/services/api/SearchServer?bbox=2551306.5625,1167918.328125,2551754.125,1168514.625&type=locations&sr=2056>`_

Example of feature search usage with other services
***************************************************

- First: search for addresses using the feature search service: `https://api3.geo.admin.ch/rest/services/api/SearchServer?features=ch.bfs.gebaeude_wohnungs_register&type=featuresearch&searchText=isabelle <../../../rest/services/api/SearchServer?features=ch.bfs.gebaeude_wohnungs_register&type=featuresearch&searchText=isabelle>`_
- Then: use "feature_id" found in "attrs" to get detailed information about a feature: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bfs.gebaeude_wohnungs_register/880711_0?returnGeometry=false <../../../rest/services/api/MapServer/ch.bfs.gebaeude_wohnungs_register/880711_0?returnGeometry=false>`_


.. _height_description:

----------

Height
------

This service allows to obtain elevation information for a point.

Outside of Switzerland a 10m grid elevation model is used. It is a combined digital elevation model consisting of elevation models from mapping agencies of France, Italy, Austria, Bavaria and Baden-Württemberg and derived with a resolution of 10m.
The extend covers XMin: 2443000 YMin: 1024000 XMax: 2895000 YMax: 1340000

See `Height models <https://www.swisstopo.admin.ch/en/geodata/height/alti3d.html>`_ for more details about data used by this service.


URL
***

::

  GET https://api3.geo.admin.ch/rest/services/height

Input Parameters
****************

RESTFul interface is available.

+--------------------------------+-----------------------------------------------------------------------------------------+
| Parameters                     | Description                                                                             |
+================================+=========================================================================================+
| **easting (required)**         | The easting coordinate in LV03 (EPSG:21781) or LV95 (EPSG:2056)                         |
+--------------------------------+-----------------------------------------------------------------------------------------+
| **northing (required)**        | The northing coordinate in LV03 (EPSG:21781) or LV95 (EPSG:2056)                        |
+--------------------------------+-----------------------------------------------------------------------------------------+
| **sr(optional)**               | The reference system to use (EPSG code). Valid values are 2056 (for LV95) and 21781     |
|                                | (for )LV03). If not given, trying to guess which one to use.                            |
+--------------------------------+-----------------------------------------------------------------------------------------+
| **callback (optional)**        | The name of the callback function.                                                      |
+--------------------------------+-----------------------------------------------------------------------------------------+

Examples
********

- `https://api3.geo.admin.ch/rest/services/height?easting=2600000&northing=1200000 <../../../rest/services/height?easting=2600000&northing=1200000>`_

.. _profile_description:

----------

Profile
-------

This service allows to obtain elevation information for a polyline in CSV format. See `Height models <https://www.swisstopo.admin.ch/en/geodata/height/alti3d.html>`_ for more details about data used by this service.


URL
***

::

  GET|POST https://api3.geo.admin.ch/rest/services/profile.json (for json format)
  GET|POST https://api3.geo.admin.ch/rest/services/profile.csv  (for a csv)

Input Parameters
****************

RESTFul interface is available.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **geom (required)**               | A GeoJSON representation of a polyline (type = LineString). The LineString should not     |
|                                   | have more than `PROFILE_MAX_AMOUNT_POINTS`, generally 5'000 coordinates.                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The reference system to use (EPSG code). Valid value are 2056 (for LV95) and 21781 (for   |
|                                   | LV03). Strongly advised to set one, but if not given, trying to guess which one to use.   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **nb_points (optional)**          | The number of points used for the polyline segmentation. Default "200".                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **offset (optional)**             | The offset value (INTEGER) in order to use the `exponential moving algorithm              |
|                                   | <http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average>`_ . For a given  |
|                                   | value the offset value specify the number of values before and after used to calculate    |
|                                   | the average.                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **distinct_points (optional)**    | If True, it will ensure the coordinates given to the service are part of the response.    |
|                                   | Possible values are True or False, default to False.                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | Only available for **profile.json**. The name of the callback function.                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+


Example
*******

- A profile in JSON: `https://api3.geo.admin.ch/rest/services/profile.json?geom={"type"%3A"LineString"%2C"coordinates"%3A[[2550050%2C1206550]%2C[2556950%2C1204150]%2C[2561050%2C1207950]]}&sr=2056 <../../../rest/services/profile.json?geom={"type"%3A"LineString"%2C"coordinates"%3A[[2550050%2C1206550]%2C[2556950%2C1204150]%2C[2561050%2C1207950]]}>`_
- A profile in CSV: `https://api3.geo.admin.ch/rest/services/profile.csv?geom={"type"%3A"LineString"%2C"coordinates"%3A[[2550050%2C1206550]%2C[2556950%2C1204150]%2C[2561050%2C1207950]]}&sr=2056 <../../../rest/services/profile.csv?geom={"type"%3A"LineString"%2C"coordinates"%3A[[2550050%2C1206550]%2C[2556950%2C1204150]%2C[2561050%2C1207950]]}>`_

----------

.. _wmts_description:

WMTS
----

A RESTFul implementation of the `WMTS <http://www.opengeospatial.org/standards/wmts>`_ `OGC <http://www.opengeospatial.org/>`_ standard.
For detailed information, see `WMTS OGC standard <http://www.opengeospatial.org/standards/wmts>`_

.. note::
    Only the RESTFul request encoding to `GetTile` is implemented, not the `GetLegend` and `GetFeatureInfo`. No KVP and SOAP request encoding is supported.



GetCapabilities
***************

The GetCapabilites document provides informations about the service, along with layer description, both in german and french.

`https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml <https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_

`https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml?lang=fr <https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml?lang=fr>`_

GetTile
*******

::

    GET <Scheme>://<ServerName>/<ProtocoleVersion>/<LayerName>/<Stylename>/<Time>/<TileMatrixSet>/<TileSetId>/<TileRow>/<TileCol>.<FormatExtension>

with the following parameters:

===================    =============================   ==========================================================================
Parameter              Example                         Explanation
===================    =============================   ==========================================================================
Scheme                 https                           The scheme type
ServerName             wmts[0-9].geo.admin.ch
Version                1.0.0                           WMTS protocol version
Layername              ch.bfs.arealstatistik-1997      See the WMTS `GetCapabilities <//wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_ document.
StyleName              default                         Only **default** is supported.
Time                   2010, 2010-01                   Date of tile generation in (ISO-8601) or logical value like **current**. A list of available values is provided in the `GetCapabilities <//wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_ document under the <Dimension> tag. We recommend to use the value under the <Default> tag. Note that these values might change frequently - **check for updates regularly**.
TileMatrixSet          2056  (constant)                EPSG code for LV03/CH1903
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

===============  ========= ========= ============ ======== ======== =============== =======================================
Resolution [m]   Zoomlevel Map zoom  Tile width m Tiles X  Tiles Y    Tiles         Approx. scale at 96 dpi per zoom level
===============  ========= ========= ============ ======== ======== =============== =======================================
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
===============  ========= ========= ============ ======== ======== =============== =======================================



**Notes**

#. The projection for the tiles is **LV95** (EPSG:2056). Other projection are supported, see further down.
#. The tiles are generated on-the-fly and stored in a cache (hundreds of requests per second)
#. The zoom level 24 (resolution 1.5m) has been generated, but is not currently used in the API.
#. The zoom levels 27 and 28 (resolution 0.25m and 0.1m) are only available for a few layers,
   e.g. swissimage or cadastral web map. For the others layers it is only a client zoom (tiles are stretched).
#. You **have** to use the `<ResourceURL>` to construct the `GetTile` request.
#. **Axis order**: for historical reasons, EPSG:21781 WMTS tiles use the
   non-standard **row/col** order, while all other projections use the usual **col/row** order.
   However, most desktop GIS allow you to either use the advertized order or to override it.
#. The tiles of a given layer might be updated **withtout** resulting in a new <Time> dimension in the GetCapabilities dimension. In case your application is caching tiles locally, you need to invalidate your local cache for this layer. To check the latest change of any layer, use the `Cache Update`_ service.

Result
******

A tile.

http://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/21781/20/58/70.jpeg

or https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/21781/20/58/70.jpeg



Supported projections
---------------------

Four projections are supported. The same tiles are offered in four other *tilematrixsets/projection*.

* LV95/CH1903+ (EPSG:2056)
    https://wmts.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml
* LV03/CH1903 (EPSG:21781)
    https://wmts.geo.admin.ch/EPSG/21781/1.0.0/WMTSCapabilities.xml
* Plate-Carrée WGS1984 (EPSG:4326, in **lat/lon order**)
    https://wmts.geo.admin.ch/EPSG/4326/1.0.0/WMTSCapabilities.xml
* WGS84/Pseudo-Mercator (EPSG:3857, as used in OSM, Bing, Google Map)
    https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml


Note:

* Partly due to a limitation of the WTMS 1.0.0 recommendations, each *projection* has its own *GetCapabilities* document.
* The same `timestamps` are available in all projection. New `timestamp` are added to the former ones.
* The layer *ch.kantone.cadastralwebmap-farbe* uses a WMS service as its source.
* Note that all layers are available at all scales. You have to check for which **tileMatrixSets** a particuliar layer is defined. Your WMTS client may either stretch the
  tiles from the last available level or display nothing.

Example
*******
* At tile: `https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/9/266/180.jpeg <https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/9/266/180.jpeg>`_

.. raw:: html

       <img src="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/9/266/180.jpeg" />

* An OpenLayers3 application using the `pseudo-Mercator projection <http://codepen.io/geoadmin/pen/pyzwwL?editors=0010>`_
* An OpenLayers3 example showing the `Cadastralwebmap as WMTS <http://codepen.io/geoadmin/pen/xVKLdV?editors=0010>`_
* Switzerland is now adopting the new `LV95 frame <http://codepen.io/geoadmin/pen/GZKEam?editors=0010>`_.
* All `available layers as WMTS <http://codepen.io/geoadmin/pen/MyYYXR?editors=0010>`_.

.. _XYZ_description:

XYZ
----

XYZ tile layers are layers comprised of multiple tiles. The XYZ tile service provides tiles based on a URL template with values substituted in for Zoom Level and X and Y counts of the tile. Unlike WMTS that follow the OGC standard, the XYZ tile service is often used in Web Mapping Context and is therefore a de facto standard. The XYZ tile service is provided with a fixed projection ( EPSG:3857).

.. note::
    We encourage  users to use WMTS layer  service which provides predefined tiles (like an XYZ service) with an option to use a RESTful templated URL or a KVP request and with a variety of projections and grids. Moreover, using WMTS GetCapabilities provides an up to date Metadata Service for the available layers.

GetTile
*******

::

    GET <Scheme>://<ServerName>/<ProtocoleVersion>/<LayerName>/<Stylename>/<Time>/<TileMatrixSet>/{z}/{x}/{y}.<FormatExtension>

with the following parameters:

===================    =============================   ==========================================================================
Parameter              Example                         Explanation
===================    =============================   ==========================================================================
Scheme                 https                           The scheme type
ServerName             wmts[0-9].geo.admin.ch
Version                1.0.0                           WMTS protocol version
Layername              ch.bfs.arealstatistik-1997      See the WMTS `GetCapabilities <//wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_ document.
StyleName              default                         Only **default** is supported.
Time                   2010, 2010-01                   Date of tile generation in (ISO-8601) or logical value like **current**. A list of available values is provided in the `GetCapabilities <//wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_ document under the <Dimension> tag. We recommend to use the value under the <Default> tag. Note that these values might change frequently - **check for updates regularly**.
TileMatrixSet          3857  (constant)                EPSG code for Webmercator
{z}                    {z}
{x}                    {x}
{y}                    {y}
FormatExtension        png                             Mostly png, except for some raster layer (pixelkarte and swissimage)
===================    =============================   ==========================================================================


**Notes**

#. The tiles of a given layer might be updated **without** resulting in a new <Time> dimension. In case your application is caching tiles locally, you need to invalidate your local cache for this layer. To check the latest change of any layer, use the `Cache Update`_ service.

Result
******

Access to ch.swisstopo.swissimage.

https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.swissimage/default/current/3857/{z}/{x}/{y}.jpeg


Supported projections
*********************

Unlike WMTS that follow the OGC standard, the XYZ tile service are often used in Web Mapping Context and therefore one projection is supported.

* WGS84/Pseudo-Mercator (EPSG:3857, as used in OSM, Bing, Google Map)
    https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.swissimage/default/current/**3857**/{z}/{x}/{y}.jpeg


Example
*******
* An OpenLayers example showing the `Swissimage as XYZ <https://codepen.io/geoadmin/pen/xxYEwjQ>`_


.. _cacheupdate_description:

----------

Cache Update
------------

As noted in the :ref:`wmts_description` service, the Tiles of a given <Time> dimension might be updated for technical reasons. If you are caching Tiles locally, this might result in your cache being outdated. Use the Cache Update service to query the Date of the last update for a given layer. If your cache is older than the returned Date, you have to clear your local cache.

URL
***

::

  GET https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/cacheUpdate


Example
*******

- The the latest Cache Update for SwissImage Product: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.swisstopo.swissimage-product/cacheUpdate <../../../rest/services/api/MapServer/ch.swisstopo.swissimage-product/cacheUpdate>`_


.. _terrain_service_description:

---------------

Terrain Service
---------------

A RESTFul implementation of "`Cesium <http://cesiumjs.org/>`_" `Quantized Mesh <https://github.com/AnalyticalGraphicsInc/quantized-mesh>`_ terrain service.
Terrain tiles are served according to the `Tile Map Service (TMS) <http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification>`_ layout and global-geodetic profile.

URL
***

https://3d.geo.admin.ch

Metadata Service
****************

The `layer.json` file determines which terrain tiles are available.

- https://3d.geo.admin.ch/ch.swisstopo.terrain.3d/v1/layer.json (alway most recent terrain tiles)
- https://3d.geo.admin.ch/ch.swisstopo.terrain.3d/v1/20201203/layer.json (terrain tiles of the date 20201203)

Parameters
**********

A request is in the form:

::

    GET https://<ServerName>/ch.swisstopo.terrain.3d/<Version>/<Time>/<Zoom>/<X>/<Y>.<FormatExtension>

with the following parameters:

===================    ==================================   ==========================================================================
Parameter              Example                              Explanation
===================    ==================================   ==========================================================================
ServerName             3d.geo.admin.ch
Version                v1                                   v1 means terrain tiles generated with cesium tiles
Layername              ch.swisstopo.terrain.3d (constant)   The name of the terrain layer. (only one terrain layer is available)
Time                   20201203                             Date of tile generation in (ISO-8601).
Zoom                   12                                   Zoom level (see below)
X                      4309                                 The longitue index
Y                      3111                                 The latitude index
FormatExtension        terrain                              The file extension (a gzipped binary terrain file)
===================    ==================================   ==========================================================================


Example
*******

* A `Terrain tile <https://3d.geo.admin.ch/ch.swisstopo.terrain.3d/v1/20201203/7/136/98.terrain?v=3924.0.0>`_

.. _tiles3d_description:

----------

3D Tiles
----------
A RESTFul implementation of "`Cesium <http://cesiumjs.org/>`_" `3D Tiles specification <https://github.com/CesiumGS/3d-tiles>`_.


URL
***

- https://3d.geo.admin.ch


Metadata Service
****************

The `tileset.json` file describes the available set of tiles. In order to use this service you can use `CesiumJS <https://github.com/CesiumGS/cesium>`_.

Currently, 3 technical layers (ch.swisstopo.swisstlm3d.3d, ch.swisstopo.swissnames3d.3d, ch.swisstopo.vegetation.3d) are available and they contains all available 3D objects.

Most recent 3D tiles:

- https://3d.geo.admin.ch/ch.swisstopo.swissbuildings3d.3d/v1/tileset.json
- https://3d.geo.admin.ch/ch.swisstopo.vegetation.3d/v1/tileset.json

3D tiles of a specific date:

- https://3d.geo.admin.ch/ch.swisstopo.swissbuildings3d.3d/v1/20240501/tileset.json
- https://3d.geo.admin.ch/ch.swisstopo.vegetation.3d/v1/20240412/tileset.json
- https://3d.geo.admin.ch/3d-tiles/ch.swisstopo.swissnames3d.3d/20180716/tileset.json

Example
*******

* A `3D tile <https://3d.geo.admin.ch/ch.swisstopo.swissbuildings3d.3d/v1/20240501/7/54/21.b3dm>`_


.. _vectortiles_description:

-------------------

Mapbox Vector Tiles
-------------------
A RESTFul implementation of `Mapbox Vector Tiles <https://www.mapbox.com/vector-tiles>`_.
See  `description <https://www.geo.admin.ch/en/geo-services/geo-services/portrayal-services-web-mapping/vector_tiles_service.html>`_

The service provides both *tiles* and *styles* that the customer can use.

GetStyle
********

A current (latest version) style request is in the following form:

::

    GET <Scheme>://<ServerName>/styles/<layername>/style.json

example of current maplibre styles of light base map and imagery base map:

- https://vectortiles.geo.admin.ch/styles/ch.swisstopo.basemap.vt/style.json
- https://vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json
- https://vectortiles.geo.admin.ch/styles/ch.swisstopo.imagerybasemap.vt/style.json
- https://vectortiles.geo.admin.ch/styles/ch.swisstopo.basemap-winter.vt/style.json

.. _vectortiles GetTile:

GetTile
*******

A tile request is in the following form:

::

    GET <Scheme>://<ServerName>/tiles/<LayerName>/<version>/<zoomlevel>/<x>/<y>.pbf

example of one pbf tile:

- https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.base.vt/v1.0.0/7/67/44.pbf
- https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.relief.vt/v1.0.0/7/67/44.pbf


GetTileSets
***********

MBTiles for storing  tiled map data in SQLite databases for immediate or offline usage and for efficient transfer. A MBtileSet request is in the following form:

::

    GET <Scheme>://<ServerName>/tiles/<LayerName>/<version>/<LayerName>.mbtiles

example of the .mbtiles file:

- https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.base.vt/v1.0.0/ch.swisstopo.base.vt.mbtiles
- https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.relief.vt/v1.0.0/ch.swisstopo.relief.vt.mbtiles



Available datasets and styles as mapbox vector tiles
****************************************************

The list of current datasets and styles is available visiting the `official service description <https://www.geo.admin.ch/en/vector-tiles-service-available-services-and-data>`_


Metadata Service
****************

Each tileset has a corresponding metatdata `json` file that describes the available set of tiles.
The URL of the metadata `json` file is :

::

   GET <Scheme>://<ServerName>/tiles/<LayerName>/<version>.json

example of tileset:

- https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.base.vt/v1.0.0/tiles.json
- https://vectortiles.geo.admin.ch/tiles/ch.swisstopo.relief.vt/v1.0.0/tiles.json


.. _sparql_description:

--------------

SPARQL Service
--------------

This service enables the connection of geodata from different sources as Linked Data. `See description <https://www.geo.admin.ch/linkeddata>`_.

URL
***

::

  GET https://geo.ld.admin.ch/query/ (SPARQL Endpoint)
  GET https://geo.ld.admin.ch/sparql/ (YASGUI)

Available datasets
******************

- `Data Catalog <https://geo.ld.admin.ch/.well-known/void>`_


.. _inspireAtomFeed:

----------------------------------------

Atom Feed / Open Search Download Service
----------------------------------------

This service enables the download of datasets conforming to the `INSPIRE Data Specifications <https://inspire.ec.europa.eu/data-specifications/2892>`_. It is implemented as an Atom Feed / Open Search service according to the `Technical Guidance for the implementation of INSPIRE Download Services  <https://inspire.ec.europa.eu/sites/default/files/documents/network-services/technical_guidance_download_services_v3.1.pdf>`_.

URL
***

::

  GET https://atom.geo.admin.ch/inspire/service.xml - Service Feed
  GET https://atom.geo.admin.ch/inspire/search/opensearchdescription.xml - Open Search Description Document
  GET https://atom.geo.admin.ch/inspire/search?q={} - Search Interface

Available datasets
******************

- `Administrative units <https://www.geocat.ch/geonetwork/srv/eng/catalog.search#/metadata/fc2c80e5-fc87-415a-ac05-b2520957d155>`_
- `Geographical Names <https://www.geocat.ch/geonetwork/srv/eng/catalog.search#/metadata/e81d4df0-52c8-4258-a38b-96f6761c976b>`_

Examples
********

- `Get a Dataset Feed (Describe Spatial Data Set Operation) <https://atom.geo.admin.ch/inspire/search?spatial_dataset_identifier_code=e81d4df0-52c8-4258-a38b-96f6761c976b&spatial_dataset_identifier_namespace=http://www.swisstopo.ch/>`_ (code and namespace to be found in the Open Search Description Document)
- `Get a dataset (Get Spatial Data Set Operation) <https://atom.geo.admin.ch/inspire/search?spatial_dataset_identifier_code=e81d4df0-52c8-4258-a38b-96f6761c976b&spatial_dataset_identifier_namespace=http://www.swisstopo.ch/&crs=http://www.opengis.net/def/crs/EPSG/0/3857>`_ (code, namespace and crs to be found in the Open Search Description Document)
- `Search for all available downloads <https://atom.geo.admin.ch/inspire/search?q=inspire>`_


