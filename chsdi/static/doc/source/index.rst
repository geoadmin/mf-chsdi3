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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.3.12/proj4.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/build/ol.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/css/ol.css">

    <div id="map" class="map"></div>
    <script>
      const TILEGRID_ORIGIN = [2420000, 1350000]; // in EPSG:2056
      // resolutions in meter/pixel
      const TILEGRID_RESOLUTIONS = [
        4000,
        3750,
        3500,
        3250,
        3000,
        2750,
        2500,
        2250,
        2000,
        1750,
        1500,
        1250,
        1000,
        750,
        650,
        500,
        250,
        100,
        50,
        20,
        10,
        5,
        2.5,
        2,
        1.5,
        1,
        0.5,
        0.25,
        0.1
      ];

      // adding Swiss projections to proj4 (proj string comming from https://epsg.io/)
      proj4.defs(
        "EPSG:2056",
        "+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333 +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs"
      );

      ol.proj.proj4.register(proj4);

      var projection = new ol.proj.Projection({
        code: "EPSG:2056",
          extent: [2420000, 1030000, 2900000, 1350000]
      });

      const backgroundLayer = new ol.layer.Tile({
        id: "background-layer",
        projection: projection,
        source: new ol.source.XYZ({
        tileGrid: new ol.tilegrid.WMTS({
          origin: [2420000, 1350000],
          resolutions: TILEGRID_RESOLUTIONS
        }),
        projection: projection,
          url: "https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/2056/{z}/{x}/{y}.jpeg"
          })
      });

      const view = new ol.View({
        projection: projection,
        center: [ 2659515.0, 1190001.3],
        zoom: 1.5
      });

      const map = new ol.Map({
        target: "map",
        controls: ol.control.defaults().extend([
          new ol.control.ScaleLine({
            units: "metric"
          })
        ]),
        layers: [backgroundLayer],
          view: view
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
