.. raw:: html

  <head>
    <link href="../_static/custom.css" rel="stylesheet" type="text/css" />
  </head>

API Examples
============

JS API examples
---------------
.. raw:: html

  <ul id="cat1"></ul>

OpenLayers 3 examples
---------------------

.. raw:: html

  <ul id="cat2"></ul>

`map.geo.admin.ch <https://map.geo.admin.ch>`_ Iframe examples
------------------------

Communication between Iframe-embeded map and parent window

.. raw:: html

  <ul id="cat3"></ul>
 
.. raw:: html

  <script type="text/javascript">
    var conf = [{
      label: 'Map with overlay layer',
      codepen: 'qbeqPQ',
      cat: 1 
    }, {
      label: 'Map with KML file overlay',
      codepen: 'eJqBVV',
      cat: 1
    }, {
      label: 'Geocoder',
      codepen: 'JGgzQG',
      cat: 1
    }, {
      label: 'Rectangle selection',
      codepen: 'NxQmvo',
      cat: 1
    }, {
      label: 'Searchbox',
      codepen: 'xZvNEY',
      cat: 1
    }, {
      label: 'Catalog',
      codepen: 'grYLdY',
      cat: 1
    }, {
      label: 'Localisation',
      codepen: 'GZKrem',
      cat: 1
    }, {
      label: 'GeoJSON integration',
      codepen: 'ZWzXgv',
      cat: 1
    }, {
      label: 'WMTS reprojected on-the-fly from a WMS in swiss projection (EPSG:21781)',
      codepen: 'xVKLdV',
      cat: 2
    }, {
      label: 'WMTS reprojected on-the-fly in Pseudo-Mercator projection (EPSG:3857)',
      codepen: 'pyzwwL',
      cat: 2
    }, {
      label: 'WMTS reprojected on-the-fly in LV95 (EPSG:2056)',
      codepen: 'GZKEam',
      cat: 2
    }, {
      label: 'All available layers as WMTS',
      codepen: 'MyYYXR',
      cat: 2 
    }, {
      label: 'More OpenLayers 3 Examples on the official website.', 
      link: 'http://openlayers.org/en/v3.6.0/examples/',
      cat: 2 
    }, {
      label: 'Feature selection of KML and GeoJSON layers',
      codepen: 'yOBzqM',
      cat: 3
    }];
    var tpl = '<li><a href="{link}" target="_blank">{label}</a></li>';
    var cat1 = '', cat2 = '', cat3 = '';
    conf.forEach(function(item) {
      if (item.codepen) {
        item.link = '//codepen.io/geoadmin/pen/' + item.codepen + '?editors=0010';
      }
      var link = tpl.replace('{link}', item.link).replace('{label}', item.label);
      switch(item.cat) {
        default:
        case 1:
          cat1 += link;
          break;
        case 2 :
          cat2 += link;
          break;
        case 3:
          cat3 += link;
          break;
      };
    });
    document.getElementById('cat1').innerHTML = cat1;
    document.getElementById('cat2').innerHTML = cat2;
    document.getElementById('cat3').innerHTML = cat3;
  </script>


