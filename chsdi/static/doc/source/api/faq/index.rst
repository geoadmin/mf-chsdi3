.. raw:: html

  <head>
    <link href="../../_static/custom.css" rel="stylesheet" type="text/css" />
  </head>

API FAQ
=======

.. contents::

General Information
-------------------

What is the GeoAdmin API ?
**************************

The GeoAdmin API allows the integration in web pages of geospatial information provided by the Swiss Confederation and Cantons.

The GeoAdmin API provides also :ref:`rest_services`

Who can use the GeoAdmin API ?
******************************

The GeoAdmin API terms of use are accessible here: `Terms of Use <https://www.geo.admin.ch/terms-of-use>`_

What is the license of the GeoAdmin JS API ?
********************************************

The GeoAdmin JavaScript API has a BSD license.

How many calls am I allowed to make ?
*************************************

20 requests per minute on a 24/7 average on any of the REST services are considered "fair use". If you need more - pls contact us via info@geo.admin.ch. Please keep in mind our terms
https://www.geo.admin.ch/terms-of-use


Are the GeoAdmin services running ?
***********************************

The status of all GeoAdmin services and applications is available here: http://status.geo.admin.ch

What are the technical restrictions of the GeoAdmin API ?
*********************************************************

The GeoAdmin API has been tested in the two last versions of the following browsers:  Firefox, Internet Explorer, Chrome, Safari.

The GeoAdmin API does support mobile devices.

How to use the GeoAdmin API in a CMS ?
********************************************

The link is here: `Geoadmin API in CMS <../integrate_cms.html>`_

Is there a forum or a mailing list ?
************************************

Yes, under http://groups.google.com/group/geoadmin-api
Feel free to use it and ask all the questions you want.

.. _available_layers:

Which layers are available ?
****************************

From 1.3.2021 all layers can be freely used.

The following list contains all the free accessible layers:

.. raw:: html

   <body>
      <div id="notChargeableLayers" style="margin-left:10px;margin-bottom:24px"></div>
   </body>


.. raw:: html

    <script type="text/javascript">
        function init() {
            const sections = [
                {
                    identifier: 'notChargeableLayers',
                    filter: (layer) => !layer.chargeable,
                },
                {
                    identifier: 'tooltipLayers',
                    filter: (layer) => !!layer.tooltip
                },
                {
                    identifier: 'searchableLayers',
                    filter: (layer) => !!layer.searchable
                },
                {
                    identifier: 'queryableLayers',
                    filter: (layer) => layer.queryableAttributes?.length > 0
                }
            ];

            $.getJSON( "../../rest/services/all/MapServer/layersConfig", function( layersConfig ) {
                const allLayers = Object.keys(layersConfig).map((layerId) => {
                    return {
                        id: layerId,
                        ...layersConfig[layerId],
                    }
                });
                // sorting all layers alphabetically by ID
                allLayers.sort((layer1, layer2) => layer1.id.localeCompare(layer2.id));
                sections.forEach((section) => {
                    const layers = allLayers.filter(section.filter);
                    let layerTable = `<br /><table style="border: none;">`;
                    layerTable += layers.map((layer, counter) => {
                        let layerRow = `<tr>`;
                        layerRow += `<td>${counter}</td>`;
                        layerRow += `<td><a target="_blank" href="https://map.geo.admin.ch/?layers=${layer.id}">${layer.id}</a>&nbsp;${layer.label}</td>`;
                        layerRow += `<td style="text-transform: capitalize">${layer.type}</td>`;
                        layerRow += `</tr>`;
                        return layerRow;
                    })
                    layerTable += `</table>`;
                    const sectionElement = document.getElementById(section.identifier);
                    if (sectionElement) {
                        sectionElement.innerHTML = layerTable;
                    }
                })
            });
        }
    </script>

    <body onload="init();">
    </body>

.. _querybale_layers:

Which layers have a tooltip?
****************************

Not all the layers have a tooltip. The complete list of layer using the `htmlPopup <../../services/sdiservices.html#htmlpopup-resource>`_ service is
the following. Note: some vector layer (GeoJSON) have a client-only tooltip and are not using this service:

.. raw:: html

  <body>
    <div id="tooltipLayers" style="margin-left:10px;margin-bottom:24px;"></div>
  </body>

.. _searchable_layers:

Which layers are searchable?
****************************

A layer is searchable when its features can be searched. Below, you can find the complete list of all searchable layers:

.. raw:: html

  <body>
    <div id="searchableLayers" style="margin-left:10px;margin-bottom:24px;"></div>
  </body>


.. _queryable_layers:

Which layers are queryable?
***************************

A queryable layer is a layer you may filter out features on some attributes:

.. raw:: html

  <body>
    <div id="queryableLayers" style="margin-left:10px;margin-bottom:24px;"></div>
  </body>


How can I have access to the tiles ?
************************************

The tiles used in the GeoAdmin API are generated by `TileCache <http://www.tilecache.org>`_ and are stored according to
a RESTful OGC `Web Map Tile Service <http://www.opengeospatial.org/standards/wmts>`_ Implementation Standard schema.

The parameters for the tiles are the following:

 * **Resolution** (meters): 4000,3750,3500,3250,3000,2750,2500,2250,2000,1750,1500,1250,1000,750,650,500,250,100,50,20,10,5,2.5,2,1.5,1,0.5,0.25,0.1

 * **Maximum extent bounding box**: 420000,30000,900000,350000

 * **Coordinate system**: EPSG:21781

For practical information on how to use the tiles, see our description of the `WMTS <../../services/sdiservices.html#wmts>`_ service.

Where is the source code ?
**************************

The source code of the GeoAdmin API project can be found here: https://github.com/geoadmin/ol3

I have difficulty to use map.geo.admin.ch, where can I get more help ?
**********************************************************************

The help pages of http://map.geo.admin.ch is accessible here: http://help.geo.admin.ch/

Can I use http://localhost to test my developments ?
****************************************************

Yes, localhost can be used to test the developments. In all cases, you have to follow the `Terms of Use <https://www.geo.admin.ch/terms-of-use>`_.

Where can I get information about OEREB/RDPPF Feature Service ?
***************************************************************
These information can be found on the `OEREB/RDPPF: Feature Service <../../services/oerebservices.html>`_ page.
