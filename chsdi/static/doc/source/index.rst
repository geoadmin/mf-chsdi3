.. GeoAdmin API documentation master file, created by
   sphinx-quickstart on Wed Jul 21 07:44:14 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. raw:: html

  <head>
    <link href="_static/custom.css" rel="stylesheet" type="text/css" />
    <link rel="apple-touch-icon" sizes="76x76" href="_static/touch-icon-bund-76x76.png"/>
    <link rel="apple-touch-icon" sizes="120x120" href="_static/touch-icon-bund-120x120.png"/>
    <link rel="apple-touch-icon" sizes="152x152" href="_static/touch-icon-bund-152x152.png"/>
  </head>


.. raw:: html

  <div id="logo">
    <img src="_static/bg_header_logo.png" alt="bg_header_logo">
  </div>

--------------------

Welcome to GeoAdmin API's documentation!
========================================

.. meta::
   :google-site-verification: b6J0Gs_QtsxWzW6PY5Uie1UkQC5SYA40k1kP6fcgFJ4

The GeoAdmin API allows the integration in web pages of geospatial information provided by the Swiss Confederation.

These pages are dedicated to developer interested in using the API.

Use the GeoAdmin API Forum to ask questions: http://groups.google.com/group/geoadmin-api

.. raw:: html

  <style>
    #map {
      width: 100%;
      height: 400px;
      border: 1px;
      border-style: solid;
      border-color: #efefef;
    }
  </style>
  <body>
    <script src="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/build/ol.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/css/ol.css">

    <div id="map" class="map"></div>
    <script>
      var projection = ol.proj.get("EPSG:3857");
      var projectionExtent = projection.getExtent();
      
      let size = (projectionExtent[2] - projectionExtent[0]) / 256;
      
      const topleft = [projectionExtent[0], projectionExtent[3]];
      
      const layer = new ol.layer.Tile({
        opacity: 0.95,
        source: new ol.source.WMTS({
          url:
            "http://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{TileMatrix}/{TileCol}/{TileRow}.jpeg",
          crossOrigin: "anonymous",
          attributions: "(c) swisstopo",
          matrixSet: "3857",
          format: "image/jpeg",
          resourceType: "tile",
          requestEncoding: "REST",
          projection: projection,
          tileGrid: new ol.tilegrid.WMTS({
            origin: topleft,
            resolutions: [...Array(21).keys()].map((key) => size / Math.pow(2, key)),
            matrixIds: [...Array(21).keys()]
          })
        }),
        extent: projectionExtent,
        style: "default",
        wrapX: true,
        visible: true
      });
      
      var map = new ol.Map({
        target: "map",
        layers: [layer],
        view: new ol.View({
          center: ol.proj.fromLonLat([7.44835, 46.94811]),
          zoom: 7
        })
      });

    </script>
  </body>

`Do you want to see some more examples? <api/examples.html>`_

.. warning::
   
    The GeoAdmin API and all GeoAdmin services can be used in both HTTP and HTTPS contexts. The access and use of the data or the services is free of charge, subject to the provisions on fair use, see www.geo.admin.ch/terms-of-use. For a list of all available layers and their accessibility please refer to the `FAQ <api/faq/index.html#which-layers-are-available>`_.
    
To receive technical updates, we recommend to actively use the forum or mailing list at http://groups.google.com/group/geoadmin-api and RSS Feed https://groups.google.com/group/geoadmin-api/feed/rss_v2_0_msgs.xml.

  **Note on web scraping**: Automatic parsing of the geoservices via bots with  `high query intensities <https://www.geo.admin.ch/terms-of-use>`_ is to be refrained from. For obtaining the datasets outside the context of the web services (use in offline systems, databases, etc.), the  `download service  <https://data.geo.admin.ch/api/stac/v0.9/static/api.html>`_ or  `file based download <https://data.geo.admin.ch>`_  has to be used.


API
===

.. toctree::
   :maxdepth: 1

   api/examples
   api/doc
   services/sdiservices
   api/faq/index
   api/status

Release notes
=============

.. toctree::
   :maxdepth: 1

   releasenotes/index

Terms of use
============

.. toctree::
   :maxdepth: 1
   :hidden:

   api/terms_of_use

.. note::
    The GeoAdmin API terms of use are accessible here: `www.geo.admin.ch/terms-of-use <www.geo.admin.ch/terms-of-use>`_

.. About Geoadmin API section

.. toctree::
   :maxdepth: 1
   :hidden:

   About Geoadmin API <https://www.geo.admin.ch/>
