.. raw:: html

  <head>
    <link href="../_static/custom.css" rel="stylesheet" type="text/css" />
  </head>

JS API Doc
==========

The GeoAdmin JS API extends `OpenLayers <https://openlayers.org/>`_ with Swiss specific configurations and layers.

.. warning::
    The GeoAdmin JS API is now very **mature** and not updated anymore. It's default version is based on Openlayers 3.6.0 (released on 7 Jun 2015), and the subsequent ones on Openlayers 3.18.2 (1 Sep 2016) and 4.4.2 (released on  6 Oct 2017).
    We urge you to use your favorite webmapping framework for new development, like `OpenLayers <https://openlayers.org/>`_ , `Leaflets <https://leafletjs.com/>`_ , Google Maps, Yandex Map, Bing Map or anything implementing the `OGC WMTS <https://www.ogc.org/standards/wmts>`_

The API is available in multiple versions:

Versions using LV95:

- 4.4.2


Versions using LV03:

- 4.3.2
- 3.18.2
- 3.6.0 (default)


The version number refers to the same version in OpenLayers.

You can access a specific version using the version parameter in the url of the loader:

- `https://api3.geo.admin.ch/loader.js?version=4.4.2 <https://api3.geo.admin.ch/loader.js?version=4.4.2>`_ 
- `https://api3.geo.admin.ch/loader.js?version=4.3.2 <https://api3.geo.admin.ch/loader.js?version=4.3.2>`_ 
- `https://api3.geo.admin.ch/loader.js?version=3.18.2 <https://api3.geo.admin.ch/loader.js?version=3.18.2>`_ 
- `https://api3.geo.admin.ch/loader.js (default: 3.6.0) <https://api3.geo.admin.ch/loader.js>`_ 

More examples of use are available on the `API Examples <https://api3.geo.admin.ch/api/examples.html>`_ page.


Other useful links:

- `GeoAdmin API documentation <http://geoadmin.github.io/ol3/apidoc/>`_
- `OpenLayers API documentation <https://openlayers.org/en/latest/doc/>`_

