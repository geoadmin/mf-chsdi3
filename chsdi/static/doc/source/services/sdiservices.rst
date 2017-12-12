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

.. _metadata_description:

Layers Metadata
---------------

This service provides metadata for all the available layers in the GeoAdmin API.

URL
***

::

  https://api3.geo.admin.ch/rest/services/api/MapServer


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
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
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
              "wmsUrlResource": "http://wms.geo.admin.ch/?REQUEST=GetCapabilities&SERVICE=WMS&VERSION=1.0.0",
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

  https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}

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

  https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/legend

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

  https://api3.geo.admin.ch/rest/services/api/MapServer/identify

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
| **mapExtent (required)**          | The extent of the map. (minx, miny, maxx, maxy).                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **imageDisplay (required)**       | The screen image display parameters (width, height, and dpi) of the map.                  |
|                                   | The mapExtent and the imageDisplay parameters are used by the server to calculate the     |
|                                   | the distance on the map to search based on the tolerance in screen pixels.                |
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
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
********

- Identify all the features belonging to ch.bafu.nabelstationen using a tolerance of 5 pixels around a point: `https://api3.geo.admin.ch/rest/services/all/MapServer/identify?geometry=678250,213000&geometryFormat=geojson&geometryType=esriGeometryPoint&imageDisplay=1391,1070,96&lang=fr&layers=all:ch.bafu.nabelstationen&mapExtent=312250,-77500,1007750,457500&returnGeometry=true&tolerance=5 <../../../rest/services/all/MapServer/identify?geometry=678250,213000&geometryFormat=geojson&geometryType=esriGeometryPoint&imageDisplay=1391,1070,96&lang=fr&layers=all:ch.bafu.nabelstationen&mapExtent=312250,-77500,1007750,457500&returnGeometry=true&tolerance=5>`_
- Identify all the features belonging to ch.bfs.arealstatistik-1985 intersecting an enveloppe (or bounding box): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985 <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985>`_
- Identify all the features belonging to ch.bafu.bundesinventare-bln a polyline: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry={"paths":[[[675000,245000],[660000,260000],[620000,250000]]]}&geometryType=esriGeometryPolyline&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln <../../../rest/services/api/MapServer/identify?geometry={"paths":[[[675000,245000],[660000,260000],[620000,250000]]]}&geometryType=esriGeometryPolyline&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln>`_
- Identify all the features belonging to ch.bafu.bundesinventare-bln intersecting a polygon: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometry={"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}&geometryType=esriGeometryPolygon&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln <../../../rest/services/api/MapServer/identify?geometry={"rings":[[[675000,245000],[670000,255000],[680000,260000],[690000,255000],[685000,240000],[675000,245000]]]}&geometryType=esriGeometryPolygon&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln>`_
- Same request than above but returned geometry format is GeoJSON: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&geometryFormat=geojson <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&geometryFormat=geojson>`_
- Same request than above but geometry is not returned: `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&returnGeometry=false <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bfs.arealstatistik-1985&returnGeometry=false>`_

Examples of Reverse Geocoding
*****************************

The service identify can be used for Reverse Geocoding operations. Here is a `list of all the available layers <../../../api/faq/index.html#which-layers-are-available>`_.

- Perform an identify request to find the districts intersecting a given enveloppe geometry (no buffer): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill&returnGeometry=false  <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=548945.5,147956,549402,148103.5&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill&returnGeometry=false>`_
- Perform an identify request to find the municipal boundaries and ZIP (PLZ or NPA) intersecting with a point (no buffer): `https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryPoint&geometry=548945.5,147956&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo-vd.ortschaftenverzeichnis_plz&returnGeometry=false <../../../rest/services/api/MapServer/identify?geometryType=esriGeometryPoint&geometry=548945.5,147956&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill,ch.swisstopo-vd.ortschaftenverzeichnis_plz&returnGeometry=false>`_


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

  https://api3.geo.admin.ch/rest/services/api/MapServer/find

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
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Examples
********

- Search for “Lavaux” in the field “bln_name” of the layer “ch.bafu.bundesinventare-bln” (infix match): `https://api3.geo.admin.ch/rest/services/api/MapServer/find?layer=ch.bafu.bundesinventare-bln&searchText=Lavaux&searchField=bln_name&returnGeometry=false  <../../../rest/services/api/MapServer/find?layer=ch.bafu.bundesinventare-bln&searchText=Lavaux&searchField=bln_name&returnGeometry=false>`_
- Search for “12316” in the field “egid” of the layer “ch.bfs.gebaeude_wohnungs_register” (infix match): `https://api3.geo.admin.ch/rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=123164&searchField=egid&returnGeometry=false  <../../../rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=123164&searchField=egid&returnGeometry=false>`_
- Search for “123164” in the field “egid” of the layer “ch.bfs.gebaeude_wohnungs_register” (exact match): `https://api3.geo.admin.ch/rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=1231641&searchField=egid&returnGeometry=false&contains=false <../../../rest/services/api/MapServer/find?layer=ch.bfs.gebaeude_wohnungs_register&searchText=1231641&searchField=egid&returnGeometry=false&contains=false>`_

.. _featureresource_description:

----------

Feature Resource
----------------

With an ID (or several in a comma separated list) and a layer ID (technical name), this service can be used to retrieve a feature resource.
Here is a `complete list of layers <../../../api/faq/index.html#which-layers-have-a-tooltip>`_ for which this service is available.

URL
***

::

  https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/{featureId},{featureId}

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
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **callback (optional)**           | The name of the callback function.                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+

Example
*******

- Get the feature with the ID RIG belonging to ch.bafu.nabelstationen: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/RIG <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/RIG>`_
- Get several features with IDs RIG and LAU belonging to ch.bafu.bundesinventar-bln: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bafu.nabelstationen/RIG,LAU <../../../rest/services/api/MapServer/ch.bafu.nabelstationen/RIG,LAU>`_

.. _htmlpopup_description:

----------

Htmlpopup Resource
------------------

With an ID and a layer ID (technical name), this service can be used to retrieve an html popup. An html popup is an html formatted representation of the textual information about the feature.
Here is a `complete list of layers <../../../api/faq/index.html#which-layers-have-a-tooltip>`_ for which this service is available.

URL
***

::

  https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/{featureId}/htmlPopup

Input Parameters
****************

No css styling is provided per default so that you can use your own.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **lang (optional)**               | The language. Supported values: de, fr, it , rm, en. Defaults to "de".                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
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

  https://api3.geo.admin.ch/rest/services/api/SearchServer

Description
***********

The search service is separated in 3 various categories or types:

* The **location search** which is composed of the following geocoded locations:

  * Cantons, Cities and communes
  * All names as printed on the national map (`SwissNames <https://shop.swisstopo.admin.ch/de/products/landscape/names3D>`_)
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
|                                     | representing the bounding box on which features should be filtered (SRID: 21781).         |
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
| **sr (optional)**                   | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
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
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
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
|                                   | features should be ordered (SRID: 21781).                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sortbbox (optional)**           | When `bbox` is specified and this parameter is "true", then the ranking of the results is |
|                                   | performed according to the distance between the locations and the center of the bounding  |
|                                   | box. Default to "true".                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **features (required)**           | A comma separated list of technical layer names.                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **limit (optional)**              | The maximum number of results to retrive per request (Max and default limit=20)           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The spatial reference. Supported values: 21781 (LV03), 2056 (LV95). Defaults to "21781".  |
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

Example of feature search usage with other services
***************************************************

- First: search for addresses using the feature search service: `https://api3.geo.admin.ch/rest/services/api/SearchServer?features=ch.bfs.gebaeude_wohnungs_register&type=featuresearch&searchText=isabelle <../../../rest/services/api/SearchServer?features=ch.bfs.gebaeude_wohnungs_register&type=featuresearch&searchText=isabelle>`_
- Then: use "feature_id" found in "attrs" to get detailed information about a feature: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bfs.gebaeude_wohnungs_register/880711_0?returnGeometry=false <../../../rest/services/api/MapServer/ch.bfs.gebaeude_wohnungs_register/880711_0?returnGeometry=false>`_


.. _height_description:

----------

Height
------

This service allows to obtain elevation information for a point. **Note: this service is not freely accessible (fee required).** `Please Contact us <mailto:geodata@swisstopo.ch>`_
See `Height models <https://shop.swisstopo.admin.ch/de/products/height_models/alti3D>`_ for more details about data used by this service.

URL
***

::

  https://api3.geo.admin.ch/rest/services/height

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
| **elevation_model (optional)** | The elevation model. Three elevation models are available DTM25, DTM2 (swissALTI3D)     |
|                                | and COMB (a combination of DTM25 and DTM2). Default to "DTM25".                         |
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

This service allows to obtain elevation information for a polyline in CSV format. **Note: this service is not freely accessible (fee required).** `Please Contact us <mailto:geodata@swisstopo.ch>`_
See `Height models <https://shop.swisstopo.admin.ch/de/products/height_models/alti3D>`_ for more details about data used by this service.

URL
***

::

  https://api3.geo.admin.ch/rest/services/profile.json (for json format)
  https://api3.geo.admin.ch/rest/services/profile.csv  (for a csv)

Input Parameters
****************

RESTFul interface is available.

+-----------------------------------+-------------------------------------------------------------------------------------------+
| Parameters                        | Description                                                                               |
+===================================+===========================================================================================+
| **geom (required)**               | A GeoJSON representation of a polyline (type = LineString).                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **sr (optional)**                 | The reference system to use (EPSG code). Valid value are 2056 (for LV95) and 21781 (for   |
|                                   | LV03). Strongly advised to set one, but if not given, trying to guess which one to use.   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **elevation_models (optional)**   | A comma separated list of elevation models. Three elevation models are available DTM25,   |
|                                   | DTM2 (swissALTI3D) and COMB (a combination of DTM25 and DTM2).  Default to "DTM25".       |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **nb_points (optional)**          | The number of points used for the polyline segmentation. Default "200".                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| **offset (optional)**             | The offset value (INTEGER) in order to use the `exponential moving algorithm              |
|                                   | <http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average>`_ . For a given  |
|                                   | value the offset value specify the number of values before and after used to calculate    |
|                                   | the average.                                                                              |
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
In order to have access to the WMTS, you require a `swisstopo web access - WMTS documentation <https://www.swisstopo.ch/webaccess>`_,
despite the fact that most layers are free to use. See :ref:`available_layers` for a list of all available layers.


URL
***

- http://wmts.geo.admin.ch or https://wmts.geo.admin.ch
- http://wmts1.geo.admin.ch or https://wmts1.geo.admin.ch
- http://wmts2.geo.admin.ch or https://wmts2.geo.admin.ch
- http://wmts3.geo.admin.ch or https://wmts3.geo.admin.ch
- http://wmts4.geo.admin.ch or https://wmts4.geo.admin.ch
- http://wmts5.geo.admin.ch or https://wmts5.geo.admin.ch
- http://wmts6.geo.admin.ch or https://wmts6.geo.admin.ch
- http://wmts7.geo.admin.ch or https://wmts7.geo.admin.ch
- http://wmts8.geo.admin.ch or https://wmts8.geo.admin.ch
- http://wmts9.geo.admin.ch or https://wmts9.geo.admin.ch


GetCapabilities
***************

The GetCapabilites document provides informations about the service, along with layer description, both in german and french.

`https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml <https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_

`https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml?lang=fr <https://wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml?lang=fr>`_

Parameters
**********

Only the RESTFul interface is implemented. No KVP and SOAP.

::

    <Scheme>://<ServerName>/<ProtocoleVersion>/<LayerName>/<Stylename>/<Time>/<TileMatrixSet>/<TileSetId>/<TileRow>/<TileCol>.<FormatExtension>

with the following parameters:

===================    =============================   ==========================================================================
Parameter              Example                         Explanation
===================    =============================   ==========================================================================
Scheme                 http or https                   The scheme type
ServerName             wmts[5-9].geo.admin.ch
Version                1.0.0                           WMTS protocol version
Layername              ch.bfs.arealstatistik-1997      See the WMTS `GetCapabilities <//wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_ document.
StyleName              default                         Only **default** is supported.
Time                   2010, 2010-01                   Date of tile generation in (ISO-8601) or logical value like **current**. A list of available values is provided in the `GetCapabilities <//wmts.geo.admin.ch/1.0.0/WMTSCapabilities.xml>`_ document under the <Dimension> tag. We recommend to use the value under the <Default> tag. Note that these values might change frequently - **check for updates regularly**.
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

#. The projection for the tiles is **LV03** (EPSG:21781). Other projection are supported, see further down.
#. The tiles are pregenerated and stored in a way it supports a heavy load (many hundreds requests per second)
#. The zoom level 24 (resolution 1.5m) has been generated, but is not currently used in the API.
#. The zoom levels 27 and 28 (resolution 0.25m and 0.1m) are only available for a few layers,
   e.g. swissimage or cadastral web map. For the others layers it is only a client zoom (tiles are stretched).
#. You **have** to use the `<ResourceURL>` to construct the `GetTile` request.
#. **Axis order**: EPSG:21781 native WMTS tiles (*pregenerated* and stored in S3) use the
   non-standard **row/col** order, while the Mapproxy reprojected ones (all other projections)
   use the usual **col/row** order. The exception being *ch.kantone.cadastralwebmap-farbe* which always use
   the **col/row** order.
   However, most desktop GIS allow you to either use the advertized order or to override it.
#. The tiles of a given layer might be updated **withtout** resulting in a new <Time> dimension in the GetCapabilities dimension. In case your application is caching tiles locally, you need to invalidate your local cache for this layer. To check the latest change of any layer, use the `Cache Update`_ service.

Result
******

A tile.

http://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/20110401/21781/20/58/70.jpeg

or https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/20110401/21781/20/58/70.jpeg



Other projections
-----------------

Beside, the **LV03** projection, the same tiles are offered in four other *tilematrixsets/projection*.
These projections are:

* Plate-Carrée WGS1984 (EPSG:4326)
    `https://wmts.geo.admin.ch/EPSG/4326/1.0.0/WMTSCapabilities.xml <https://wmts.geo.admin.ch/EPSG/4326/1.0.0/WMTSCapabilities.xml>`_
* LV95/CH1903+ (EPSG:2056)
    `https://wmts.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml <https://wmts.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml>`_
* WGS84/Pseudo-Mercator (EPSG:3857, as used in OSM, Bing, Google Map)
    `https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml <https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml>`_


Note:

* Partly due to a limitation of the WTMS 1.0.0 recommendations, each *projection* has its own *GetCapabilities* document.
* You have to use the hosts `wmts{20-24}.geo.admin.ch`. This is done to avoid parsing every requests to determine which are
  using native tiles and which are using reporjected tiles.
* The same access restrictions apply as above.
* The same `timestamps` are available in all projection. New `timestamp` are added to the former ones.
* Reprojected tiles are generated *on-the-fly* with `MapProxy <http://mapproxy.org>`_. If you plan to heavily use this service, please
  inform us in advance.
* *MapProxy* uses the `Proj.4 <http://trac.osgeo.org/proj/>`_ library internaly to transform between datum, except for the reframe from
  **LV03/MN03** tiles which is *NTv2* grid based (`CHENyx06 <https://www.swisstopo.admin.ch/en/knowledge-facts/surveying-geodesy/reference-frames/local.html>`_)
* Source for these reprojected tiles are the *native* **LV03/MN03** ones. The only exception is *ch.kantone.cadastralwebmap-farbe* that uses a WMS service as its source.
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

.. _cacheupdate_description:

----------

Cache Update
------------

As noted in the :ref:`wmts_description` service, the Tiles of a given <Time> dimension might be updated for technical reasons. If you are caching Tiles locally, this might result in your cache being outdated. Use the Cache Update service to query the Date of the last update for a given layer. If your cache is older than the returned Date, you have to clear your local cache.

URL
***

::

  https://api3.geo.admin.ch/rest/services/api/MapServer/{layerBodId}/cacheUpdate


Example
*******

- The the latest Cache Update for SwissImage Product: `https://api3.geo.admin.ch/rest/services/api/MapServer/ch.swisstopo.swissimage-product/cacheUpdate <../../../rest/services/api/MapServer/ch.swisstopo.swissimage-product/cacheUpdate>`_


.. _terrain_service_description:

---------------

Terrain Service
---------------

A RESTFul implementation of "`Cesium <http://cesiumjs.org/>`_" `Quantized Mesh <https://github.com/AnalyticalGraphicsInc/quantized-mesh>`_ terrain service.
Terrain tiles are served according to the `Tile Map Service (TMS) <http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification>`_ layout and global-geodetic profile.
In order to access the terrain tiles, you require a `swisstopo web access - WMTS documentation <https://www.swisstopo.ch/webaccess>`_.

URL
***

- https://terrain0.geo.admin.ch
- https://terrain1.geo.admin.ch
- https://terrain2.geo.admin.ch
- https://terrain3.geo.admin.ch
- https://terrain4.geo.admin.ch

Metadata Service
****************

The `layer.json` file determines which terrain tiles are available.

- https://3d.geo.admin.ch/1.0.0/ch.swisstopo.terrain.3d/default/20160115/4326/layer.json

Parameters
**********

A request is in the form:

::

    https://<ServerName>/<ProtocoleVersion>/ch.swisstopo.terrain.3d/<Stylename>/<Time>/<TileMatrixSetId>/<Zoom>/<X>/<Y>.<FormatExtension>

with the following parameters:

===================    ==================================   ==========================================================================
Parameter              Example                              Explanation
===================    ==================================   ==========================================================================
ServerName             terrain[0-5].geo.admin.ch
Version                1.0.0                                The terrain service protocol version
Layername              ch.swisstopo.terrain.3d (constant)   The name of the terrain layer. (only one terrain layer is available)
StyleName              default                              mostly constant
Time                   2015311201                           Date of tile generation in (ISO-8601).
TileMatrixSet          4326 (constant)                      EPSG code for WGS84
TileSetId              12                                   Zoom level (see below)
X                      4309                                 The longitue index
Y                      3111                                 The latitude index
FormatExtension        terrain                              The file extension (a gzipped binary terrain file)
===================    ==================================   ==========================================================================


The *<TileMatrixSet>* **4326** is defined as follow::

  MinX              5.013926957923385
  MaxX              11.477436312994008
  MinY              45.35600133779394
  MaxY              48.27502358353741
  TileWidth         256

With the *<tileOrigin>* in the bottom left corner of the bounding box.

=============================== ========= ========================================
Resoultion [m/pixel at equator] Zoomlevel Availability
=============================== ========= ========================================
78271.80469                     0         [-180, -90, 90, 180]
39135.90234                     1         [-180, -90, 90, 180]
19567.95117                     2         [-180, -90, 90, 180]
9783.975586                     3         [-180, -90, 90, 180]
4891.987793                     4         [-180, -90, 90, 180]
2445.993896                     5         [-180, -90, 90, 180]
1222.996948                     6         [-180, -90, 90, 180]
611.4984741                     7         [-180, -90, 90, 180]
305.749237                      8         Ranges as defined in the layer.json file
152.8746185                     9         Ranges as defined in the layer.json file
76.43730927                     10        Ranges as defined in the layer.json file
38.21865463                     11        Ranges as defined in the layer.json file
19.10932732                     12        Ranges as defined in the layer.json file
9.554663658                     13        Ranges as defined in the layer.json file
4.777331829                     14        Ranges as defined in the layer.json file
2.388665915                     15        Ranges as defined in the layer.json file
1.194332957                     16        Ranges as defined in the layer.json file
0.597166479                     17        Ranges as defined in the layer.json file
=============================== ========= ========================================

Example
*******

* A `Terrain tile <https://terrain2.geo.admin.ch/1.0.0/ch.swisstopo.terrain.3d/default/20160115/4326/12/4309/3111.terrain>`_


.. _tiles3d_description:

----------

3D Tiles
----------
A RESTFul implementation of "`Cesium <http://cesiumjs.org/>`_" `3D Tiles specification <https://github.com/AnalyticalGraphicsInc/3d-tiles>`_.
In order to access the 3D tiles, you require a `swisstopo web access - WMTS documentation <https://www.swisstopo.ch/webaccess>`_.

URL
***

- https://vectortiles.geo.admin.ch

Metadata Service
****************

The `tileset.json` file describes the available set of tiles. In order to use this service, you must currently use a fork of CesiumJS, `the 3d-tiles branch <https://github.com/AnalyticalGraphicsInc/cesium/tree/3d-tiles>`_. Stay informed and have a look at the current `RoadMap for 3D Tiles <https://github.com/AnalyticalGraphicsInc/cesium/issues/3241>`_.

Currently, 2 technical layers (ch.swisstopo.swisstlm3d.3d, ch.swisstopo.swissnames3d.3d) are available and they contains all available 3D objects. Additional layers will be available in the future. Partial 3D buildings model coverage can be vizsualised `here <https://s.geo.admin.ch/70fb32e692>`_.

- https://vectortiles.geo.admin.ch/ch.swisstopo.swisstlm3d.3d/20170425/tileset.json
- https://vectortiles.geo.admin.ch/ch.swisstopo.swissnames3d.3d/20170814/tileset.json

Example
*******

* A `3D tile <https://vectortiles.geo.admin.ch/ch.swisstopo.swisstlm3d.3d/20170425/8/41/41.b3dm?v=1.0>`_

.. _sparql_description:

--------------

SPARQL Service
--------------

This service enables the connection of geodata from different sources as Linked Data. It uses the open query language `SPARQL <https://www.w3.org/TR/sparql11-overview/>`_.

URL
***

::

  https://sparql.geo.admin.ch/sparql
  https://ld.geo.admin.ch/sparql/ (YASGUI)

Available datasets
******************

- `swissBOUNDARIES3D <https://ld.geo.admin.ch/data/swissBOUNDARIES3D>`_

Examples
********

- `Get the top five most populated municipalities in 2016 <https://tinyurl.com/hxzfqel>`_
- `Get the 2016 version of the administrative units at coordinate (lon,lat) 7.43, 46.95 <https://tinyurl.com/jjtk9a5>`_
- `Get all the districts by canton number and year <https://tinyurl.com/jghhphw>`_
- `Get all the versions of a resource by URI <https://tinyurl.com/hvw2zhq>`_
- `Get the corresponding resource in Wikidata and GeoNames (Municipality) <https://tinyurl.com/jqkkwrv>`_
- `Get the Wikipedia abstract (Municipality) <https://tinyurl.com/z42lts9>`_
