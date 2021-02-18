.. raw:: html

  <head>
  <link href="../_static/custom.css" rel="stylesheet" type="text/css" />
  <link rel="alternate" type="application/rss+xml" title="GeoAdmin RSS Feed" href="rss2.xml"/>
  </head>

.. _releasenotes:

Release Notes
=============

.. raw:: html

    <p id="rss-feed"><a class="reference external" href="rss2.xml"> <i class="fa fa-rss"> RSS Feeds </i></a></p>

.. _releasenotes_20210224:

Release 20210224 - Wednesday, February 24th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- All services are now freely accessible, no registration required, no referer checks in place. we updated our terms of use: https://www.geo.admin.ch/terms-of-use, taking effect on 1.3.2021. We still do recommend that you sign-up for our mailing list / forum http://groups.google.com/group/geoadmin-api to get notified regarding announcements.
- Mapbox Vector Tiles services: test phase is over- please update to the `production  URL schema to GetTile and GetStyle <https://api3.geo.admin.ch/services/sdiservices.html#mapbox-vector-tiles>`__.
- Announcement: the layers ch.swisstopo.digitales-hoehenmodell_25.metadata, ch.swisstopo.images-spot-5.metadata, ch.swisstopo.images-swissimage.metadata, ch.swisstopo.luftfahrtkarten-icao.metadata, ch.swisstopo.pixelkarte-pk500.metadata, ch.swisstopo.pixelkarte-pk1000.metadata, ch.swisstopo.segelflugkarte.metadata, ch.swisstopo.swissalti3d.metadata, ch.swisstopo.swissbuildings3d_1.metadata, ch.swisstopo.swissbuildings3d_2.metadata, ch.swisstopo.swiss-map-raster10.metadata, ch.swisstopo.swiss-map-vector10.metadata, ch.swisstopo.swiss-map-vector1000.metadata, ch.swisstopo.swiss-map-vector500.metadata and ch.swisstopo.swisstlm3d.metadata are obsolete and have been removed from FSDI services on Feb. 24th 2021
- Announcement: the layers ch.bafu.grundwasserschutzareale, ch.bafu.grundwasserschutzzonen and ch.bafu.gewaesserschutzbereiche will be completely removed from the FSDI services in March 2021
- Announcement: the layers ch.blw.emapis-beizugsgebiet, ch.blw.emapis-bewaesserung, ch.blw.emapis-elektrizitaetsversorgung, ch.blw.emapis-entwaesserung, ch.blw.emapis-hochbau, ch.blw.emapis-milchleitung, ch.blw.emapis-oekologie, ch.blw.emapis-projektschwerpunkt, ch.blw.emapis-seilbahnen, ch.blw.emapis-wasserversorgung, ch.blw.emapis-wegebau and ch.blw.emapis-zusammenfassung will be completely removed from the FSDI services in March 2021
- Announcement: the layers ch.bfe.bikesharing, ch.mobility.standorte and ch.bfe.energiestaedte-energieregionen will be completely removed from the FSDI services in May 2021
- Announcement: the layer ch.bafu.bundesinventare-flachmoore_regional will be completely removed from the FSDI services in June 2021
- Announcement: the layers ch.bafu.showme-gemeinden_hochwasser, ch.bafu.showme-gemeinden_lawinen, ch.bafu.showme-gemeinden_rutschungen, ch.bafu.showme-gemeinden_sturzprozesse, ch.bafu.showme-kantone_hochwasser, ch.bafu.showme-kantone_lawinen, ch.bafu.showme-kantone_rutschungen and ch.bafu.showme-kantone_sturzprozesse will be completely removed from the FSDI services in June 2021
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_201028...r_201209>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_201028...r_201209>`__

Geodata
*******

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Tank relocation routes <//map.geo.admin.ch/?layers=ch.vbs.panzerverschiebungsrouten>`__ (ch.vbs.panzerverschiebungsrouten)                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Future mean runoff (m³/s) and regime <//map.geo.admin.ch/?layers=ch.bafu.mittlere-abfluesse_zukunft>`__ (ch.bafu.mittlere-abfluesse_zukunft)                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1000>`__ (ch.bakom.uplink1000)                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre FTTB/FTTH <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2G - GSM / EDGE <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-2g>`__ (ch.bakom.mobilnetz-2g)                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `5G - NR <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-3g>`__ (ch.bakom.mobilnetz-3g)                                                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3G - UMTS / HSPA <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-4g>`__ (ch.bakom.mobilnetz-4g)                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `4G - LTE / LTE-A <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-5g>`__ (ch.bakom.mobilnetz-5g)                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 3 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink3>`__ (ch.bakom.downlink3)                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 30 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink30>`__ (ch.bakom.downlink30)                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 300 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink300>`__ (ch.bakom.downlink300)                                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 500 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink500>`__ (ch.bakom.downlink500)                                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1000>`__ (ch.bakom.downlink1000)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Interregional wildlife corridor <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierkorridor_national>`__ (ch.bafu.fauna-wildtierkorridor_national)                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| update | `Division swissALTI3D Raster <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d.metadata>`__ (ch.swisstopo.swissalti3d.metadata)                                                    | 
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division National Map 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.swiss-map-vector25.metadata>`__ (ch.swisstopo.swiss-map-vector25.metadata)                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-relief-monodirektional>`__ (ch.swisstopo.swissalti3d-relief-monodirektional)              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-relief_multidirektional>`__ (ch.swisstopo.swissalti3d-relief_multidirektional)           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Soil bulk density <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gesteinsdichte>`__ (ch.swisstopo.geologie-gesteinsdichte)                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperature model - data <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturmodell_eingangsdaten>`__ (ch.swisstopo.geologie-geomol-temperaturmodell_eingangsdaten)   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures Top Upper Malm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperatur_top_omalm>`__ (ch.swisstopo.geologie-geomol-temperatur_top_omalm)                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures Top OMM <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperatur_top_omm>`__ (ch.swisstopo.geologie-geomol-temperatur_top_omm)                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures Top Muschelkalk <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk>`__ (ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk)       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures 500 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_500>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_500)               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures 1000 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_1000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_1000)            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures 1500 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_1500>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_1500)            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures 2000 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_2000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_2000)            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures 3000 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_3000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_3000)            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperatures 4000 m depth - data <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_4000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_4000)     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevation 60 °C isotherm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-isotherme_60>`__ (ch.swisstopo.geologie-geomol-isotherme_60)                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevation 100 °C isotherm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-isotherme_100>`__ (ch.swisstopo.geologie-geomol-isotherme_100)                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevation 150 °C isotherm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-isotherme_150>`__ (ch.swisstopo.geologie-geomol-isotherme_150)                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=bafu.wrz-wildruhezonen_portal>`__ (bafu.wrz-wildruhezonen_portal)                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vermessungsstrecken - Querprofilmarke <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected areas MIL <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-luftfahrt>`__ (ch.bafu.schutzgebiete-luftfahrt)                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dry grasslands (DGS) <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden)                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Fens <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-flachmoore>`__ (ch.bafu.bundesinventare-flachmoore)                                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Biogeographical regions ARE <//map.geo.admin.ch/?layers=ch.bafu.biogeographische_regionen>`__ (ch.bafu.biogeographische_regionen)                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Anlagen Gütertransport Schiene <//map.geo.admin.ch/?layers=ch.bav.anlagen-schienengueterverkehr>`__ (ch.bav.anlagen-schienengueterverkehr)                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Status of Cantonal Geotope Inventories <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geotope_kantone_stand>`__ (ch.swisstopo.geologie-geotope_kantone_stand)                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20201209:

Release 20201209 - Wednesday, December 9th 2020
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: the swisstopo layer ch.swisstopo.vec200-landcover-wald has been removed from FSDI services as previously announced on July 1st 2020
- Announcement: the layers ch.bafu.grundwasserschutzareale, ch.bafu.grundwasserschutzzonen and ch.bafu.gewaesserschutzbereiche will be completely removed from the FSDI services in March 2021
- Announcement: the layers ch.blw.emapis-beizugsgebiet, ch.blw.emapis-bewaesserung, ch.blw.emapis-elektrizitaetsversorgung, ch.blw.emapis-entwaesserung, ch.blw.emapis-hochbau, ch.blw.emapis-milchleitung, ch.blw.emapis-oekologie, ch.blw.emapis-projektschwerpunkt, ch.blw.emapis-seilbahnen, ch.blw.emapis-wasserversorgung, ch.blw.emapis-wegebau and ch.blw.emapis-zusammenfassung will be completely removed from the FSDI services in March 2021
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_201028...r_201209>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_201028...r_201209>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `PCP Inventory 2021 <//map.geo.admin.ch/?layers=ch.babs.kulturgueter-anhoerung>`__ (ch.babs.kulturgueter-anhoerung)                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Basemap light hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.leichte-basiskarte_reliefschattierung>`__ (ch.swisstopo.leichte-basiskarte_reliefschattierung)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Production regions NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-produktionsregionen>`__ (ch.bafu.landesforstinventar-produktionsregionen)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Economic regions NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-wirtscahftsregionen>`__ (ch.bafu.landesforstinventar-wirtscahftsregionen)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Protection forest regions NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-schutzwaldregionen>`__ (ch.bafu.landesforstinventar-schutzwaldregionen)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Soil bulk density <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gesteinsdichte>`__ (ch.swisstopo.geologie-gesteinsdichte)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Status of Cantonal Geotope Inventories <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geotope_kantone_stand>`__ (ch.swisstopo.geologie-geotope_kantone_stand)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Glacier Extent <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gletscherausdehnung>`__ (ch.swisstopo.geologie-gletscherausdehnung)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Glacier Thickness <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gletschermaechtigkeit>`__ (ch.swisstopo.geologie-gletschermaechtigkeit)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Housing Inventory <//map.geo.admin.ch/?layers=ch.are.wohnungsinventar-zweitwohnungsanteil>`__ (ch.are.wohnungsinventar-zweitwohnungsanteil)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Winter national map LK10, LK25, LK50, LK100 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-winter>`__ (ch.swisstopo.pixelkarte-farbe-winter)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division snowshoe/ski tour maps 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.skitourenkarte-50.metadata>`__ (ch.swisstopo.skitourenkarte-50.metadata)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe trekking <//map.geo.admin.ch/?layers=ch.swisstopo.schneeschuhwandern>`__ (ch.swisstopo.schneeschuhwandern)                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Deep geothermal projects <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tiefengeothermie_projekte>`__ (ch.swisstopo.geologie-tiefengeothermie_projekte)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport stops <//map.geo.admin.ch/?layers=ch.bav.haltestellen-oev>`__ (ch.bav.haltestellen-oev)                                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spectral micro-zoning <//map.geo.admin.ch/?layers=ch.bafu.gefahren-spektral>`__ (ch.bafu.gefahren-spektral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic zones SIA 261 <//map.geo.admin.ch/?layers=ch.bafu.gefahren-gefaehrdungszonen>`__ (ch.bafu.gefahren-gefaehrdungszonen)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division Dufour Map Raster <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-dufour.metadata>`__ (ch.swisstopo.hiks-dufour.metadata)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division special geological maps Vector <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata>`__ (ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata)                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `General Geological Map of Switzerland 1:200,000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-generalkarte-ggk200>`__ (ch.swisstopo.geologie-generalkarte-ggk200)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division General Geol. Map 200 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-generalkarte-ggk200.metadata>`__ (ch.swisstopo.geologie-generalkarte-ggk200.metadata)                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Soil bulk density <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gesteinsdichte>`__ (ch.swisstopo.geologie-gesteinsdichte)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division National Map 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.swiss-map-vector25.metadata>`__ (ch.swisstopo.swiss-map-vector25.metadata)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division swissSURFACE3D Raster <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-raster.metadata>`__ (ch.swisstopo.swisssurface3d-raster.metadata)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division special geological maps Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-spezialkarten_schweiz.metadata>`__ (ch.swisstopo.geologie-spezialkarten_schweiz.metadata)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_vector.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas_vector.metadata)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division swissSURFACE3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d.metadata>`__ (ch.swisstopo.swisssurface3d.metadata)                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Filling stations BEBECO <//map.geo.admin.ch/?layers=ch.vbs.bundestankstellen-bebeco>`__ (ch.vbs.bundestankstellen-bebeco)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+










.. _releasenotes_20201028:

Release 20201028 - Wednesday, October 28th 2020
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_200916...r_201028>`__
- Due to maintenance work, the layer ch.swisstopo.geologie-tiefengeothermie-projekte will be temporarily unavailable in CHSDI until the release of December 9th 2020. In the meantime, the layer is still accessible for `download <https://data.geo.admin.ch/ch.swisstopo.geologie-tiefengeothermie_projekte/>`__.
- Announcement:
    - The BFS layer ch.bfs.gebaeude_wohnungs_register (Register of Buildings and Dwellings) will extend its data model on all FSDI services (map, api3 and download on data.geo.admin.ch) by this release according to https://www.bfs.admin.ch/bfs/en/home/statistics/catalogues-databases/publications.assetdetail.7008785.html (model description available in German only).
        - now productive data model: https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bfs.gebaeude_wohnungs_register/9051164_0 


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_200916...r_201028>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division swissSURFACE3D Raster <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-raster.metadata>`__ (ch.swisstopo.swisssurface3d-raster.metadata)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissSURFACE3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional)         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissSURFACE3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional)      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Seilbahnen mit Bundeskonzession <//map.geo.admin.ch/?layers=ch.bav.seilbahnen-bundeskonzession>`__ (ch.bav.seilbahnen-bundeskonzession)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate normals sunshine duration 1961-1990 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-sonnenscheindauer_1961_1990>`__ (ch.meteoschweiz.klimanormwerte-sonnenscheindauer_1961_1990)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate normals sunshine duration 1981-2010 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-sonnenscheindauer_aktuelle_periode>`__ (ch.meteoschweiz.klimanormwerte-sonnenscheindauer_aktuelle_periode)|
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate normals temperature 1961-1990 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-temperatur_1961_1990>`__ (ch.meteoschweiz.klimanormwerte-temperatur_1961_1990)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate normals temperature 1981-2010 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-temperatur_aktuelle_periode>`__ (ch.meteoschweiz.klimanormwerte-temperatur_aktuelle_periode)                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate normals precipitation 1961-1990 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-niederschlag_1961_1990>`__ (ch.meteoschweiz.klimanormwerte-niederschlag_1961_1990)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate normals precipitation 1981-2010 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-niederschlag_aktuelle_periode>`__ (ch.meteoschweiz.klimanormwerte-niederschlag_aktuelle_periode)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Arsenals <//map.geo.admin.ch/?layers=ch.vbs.retablierungsstellen>`__ (ch.vbs.retablierungsstellen)                                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Konsultationsbereiche Rohrleitungen <//map.geo.admin.ch/?layers=ch.bfe.rohrleitungen-konsultationsbereiche>`__ (ch.bfe.rohrleitungen-konsultationsbereiche)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Biogas plants <//map.geo.admin.ch/?layers=ch.bfe.biogasanlagen>`__ (ch.bfe.biogasanlagen)                                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of forest damage – projectile <//map.geo.admin.ch/?layers=ch.vbs.waldschadenkarte>`__ (ch.vbs.waldschadenkarte)                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 1st night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde)                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lmax <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lr <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light / large airecrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge)|
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. ligt aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. last night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde)             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. milit. aerodr. (tot.) <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt)             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 2nd night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected Areas VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-adminboundaries-protectedarea>`__ (ch.swisstopo.vec200-adminboundaries-protectedarea)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forested areas <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover-wald>`__ (ch.swisstopo.vec200-landcover-wald)                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects  VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transportation VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Federal filling stations BEBECO <//map.geo.admin.ch/?layers=ch.vbs.bundestankstellen-bebeco>`__ (ch.vbs.bundestankstellen-bebeco)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 25 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte25_papier.metadata>`__ (ch.swisstopo.landeskarte25_papier.metadata)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte50_papier.metadata>`__ (ch.swisstopo.landeskarte50_papier.metadata)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 100 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte100_papier.metadata>`__ (ch.swisstopo.landeskarte100_papier.metadata)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division hiking map 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.wanderkarte50_papier.metadata>`__ (ch.swisstopo.wanderkarte50_papier.metadata)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Reserved zones aiports <//map.geo.admin.ch/?layers=ch.bazl.projektierungszonen-flughafenanlagen>`__ (ch.bazl.projektierungszonen-flughafenanlagen)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3D Objects from TLM <//s.geo.admin.ch/81bdb0f497>`__ (ch.swisstopo.swisstlm3d.3d)                                                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Register of Buildings and Dwellings <//map.geo.admin.ch/?layers=ch.bfs.gebaeude_wohnungs_register>`__ (ch.bfs.gebaeude_wohnungs_register)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20200916:

Release 20200916 - Wednesday, September 16th 2020
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Added oereb layer ch.vbs.kataster-belasteter-standorte-militaer.oereb
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_200701...r_200916>`__
- Announcement:
    - The swisstopo layer ch.swisstopo.vec200-landcover-wald will be completely removed from the FSDI services in december 2020.
    - The model change of the BFS layer ch.bfs.gebaeude_wohnungs_register (Register of Buildings and Dwellings) has been postponed to the FSDI release of October 28th 2020. For Identify users the data structure will change as given in the following example, which can actively be tested:
        - previous, now productive data model: https://api3.geo.admin.ch/rest/services/api/MapServer/ch.bfs.gebaeude_wohnungs_register/9051164_0
        - new data model: https://mf-chsdi3.int.bgdi.ch/feature_bfs_sedex/rest/services/all/MapServer/ch.bfs.gebaeude_wohnungs_register/9051164_0


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_200701...r_200916>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `112 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_zentral>`__ (ch.bakom.notruf-112_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `117 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_zentral>`__ (ch.bakom.notruf-117_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `118 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_zentral>`__ (ch.bakom.notruf-118_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `143 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_zentral>`__ (ch.bakom.notruf-143_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `144 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_zentral>`__ (ch.bakom.notruf-144_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `147 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_zentral>`__ (ch.bakom.notruf-147_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `TBE: Side of tick bite reported <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Documentation of landscape change <//map.geo.admin.ch/?layers=ch.bfs.landschaftswandel>`__ (ch.bfs.landschaftswandel)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Fleischwaren (GGA) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Käse (GUB) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Konditoreiwaren (GGA) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-konditoreiwaren>`__ (ch.blw.ursprungsbezeichnungen-konditoreiwaren)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Pflanziche Produkte (GUB) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-pflanzen>`__ (ch.blw.ursprungsbezeichnungen-pflanzen)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Spirituosen (GUB) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-spirituosen>`__ (ch.blw.ursprungsbezeichnungen-spirituosen)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissALTI3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-relief-monodirektional>`__ (ch.swisstopo.swissalti3d-relief-monodirektional)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rock laboratories <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-felslabore>`__ (ch.swisstopo.geologie-felslabore)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Belastete Standorte Militär <//map.geo.admin.ch/?layers=ch.vbs.kataster-belasteter-standorte-militaer>`__ (ch.vbs.kataster-belasteter-standorte-militaer)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway noise protection walls <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_laermschutzwaende>`__ (ch.bav.laermbelastung-eisenbahn_laermschutzwaende)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport stops <//map.geo.admin.ch/?layers=ch.bav.haltestellen-oev>`__ (ch.bav.haltestellen-oev)                                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Waste incineration plants <//map.geo.admin.ch/?layers=ch.bfe.kehrichtverbrennungsanlagen>`__ (ch.bfe.kehrichtverbrennungsanlagen)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=2019&time=2019>`__ (ch.swisstopo.swissimage-product)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=2019&time=2019>`__ (ch.swisstopo.swissimage-product.metadata)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Register of Buildings and Dwellings <//map.geo.admin.ch/?layers=ch.bfs.gebaeude_wohnungs_register>`__ (ch.bfs.gebaeude_wohnungs_register)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 1st night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde)                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lmax <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lr <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light / large airecrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge)|
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. ligt aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. last night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde)             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. milit. aerodr. (tot.) <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt)             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 2nd night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind: federal government interests <//map.geo.admin.ch/?layers=ch.are.windenergie-bundesinteressen>`__ (ch.are.windenergie-bundesinteressen)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division hiking map 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.wanderkarte50_papier.metadata>`__ (ch.swisstopo.wanderkarte50_papier.metadata)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIS starting point <//map.geo.admin.ch/?layers=ch.bav.sachplan-infrastruktur-schiene_ausgangslage>`__ (ch.bav.sachplan-infrastruktur-schiene_ausgangslage)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIS consultation <//map.geo.admin.ch/?layers=ch.bav.sachplan-infrastruktur-schiene_anhorung>`__ (ch.bav.sachplan-infrastruktur-schiene_anhorung)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Treasurehunt <//map.geo.admin.ch/?layers=ch.swisstopo.treasurehunt>`__ (ch.swisstopo.treasurehunt)                                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bike sharing and bike hire <//map.geo.admin.ch/?layers=ch.bfe.bikesharing>`__ (ch.bfe.bikesharing)                                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dam <//map.geo.admin.ch/?layers=ch.bfe.stauanlagen-bundesaufsicht>`__ (ch.bfe.stauanlagen-bundesaufsicht)                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20200701:

Release 20200701 - Wednesday, July 1st 2020
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_200520...r_200701>`__
- Announcement:
    - The BFS layer ch.bfs.gebaeude_wohnungs_register (Register of Buildings and Dwellings) will extend its data model on all FSDI services (map, api3 and download on data.geo.admin.ch) by the release of September 16th 2020 according to https://www.bfs.admin.ch/bfs/en/home/statistics/catalogues-databases/publications.assetdetail.7008785.html (model description available in German only).
    - The swisstopo layer ch.swisstopo.vec200-landcover-wald will be completely removed from the FSDI services in december 2020.

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_200520...r_200701>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Apr. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-apr>`__ (ch.bafu.niederschlagserosivitaet-apr)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Mai. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-mai>`__ (ch.bafu.niederschlagserosivitaet-mai)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Jun. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-jun>`__ (ch.bafu.niederschlagserosivitaet-jun)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Jul. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-jul>`__ (ch.bafu.niederschlagserosivitaet-jul)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Aug. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-aug>`__ (ch.bafu.niederschlagserosivitaet-aug)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Sep. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-sep>`__ (ch.bafu.niederschlagserosivitaet-sep)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Oct. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-okt>`__ (ch.bafu.niederschlagserosivitaet-okt)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Nov. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-nov>`__ (ch.bafu.niederschlagserosivitaet-nov)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rainfall erosivity Dec. <//map.geo.admin.ch/?layers=ch.bafu.niederschlagserosivitaet-dez>`__ (ch.bafu.niederschlagserosivitaet-dez)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Forest swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wald>`__ (ch.swisstopo.swisstlm3d-wald)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images privates <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-firmen>`__ (ch.swisstopo.lubis-luftbilder-dritte-firmen)                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alps with guard dogs <//map.geo.admin.ch/?layers=ch.bafu.alpenweiden_herdenschutzhunde>`__ (ch.bafu.alpenweiden_herdenschutzhunde)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Basiskarte GIN <//map.geo.admin.ch/?layers=ch.bafu.gefahren-basiskarte>`__ (ch.bafu.gefahren-basiskarte)                                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_festnetz>`__ (ch.bakom.notruf-117_festnetz)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_mobilnetz>`__ (ch.bakom.notruf-117_mobilnetz)                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_festnetz>`__ (ch.bakom.notruf-143_festnetz)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_mobilnetz>`__ (ch.bakom.notruf-143_mobilnetz)                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_festnetz>`__ (ch.bakom.notruf-144_festnetz)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_mobilnetz>`__ (ch.bakom.notruf-144_mobilnetz)                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_festnetz>`__ (ch.bakom.notruf-147_festnetz)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_mobilnetz>`__ (ch.bakom.notruf-147_mobilnetz)                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 30 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink30>`__ (ch.bakom.downlink30)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 3 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink3>`__ (ch.bakom.downlink3)                                                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest ecoregions <//map.geo.admin.ch/?layers=ch.bafu.wald-standortsregionen>`__ (ch.bafu.wald-standortsregionen)                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1000>`__ (ch.bakom.uplink1000)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre FTTB/FTTH <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 300 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink300>`__ (ch.bakom.downlink300)                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 500 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink500>`__ (ch.bakom.downlink500)                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1000>`__ (ch.bakom.downlink1000)                                                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Areas of silver fir <//map.geo.admin.ch/?layers=ch.bafu.wald-tannenareale>`__ (ch.bafu.wald-tannenareale)                                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tracer tests <//map.geo.admin.ch/?layers=ch.bafu.hydrogeologie-markierversuche>`__ (ch.bafu.hydrogeologie-markierversuche)                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic zones SIA 261 <//map.geo.admin.ch/?layers=ch.bafu.gefahren-gefaehrdungszonen>`__ (ch.bafu.gefahren-gefaehrdungszonen)                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3G - UMTS / HSPA <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-3g>`__ (ch.bakom.mobilnetz-3g)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3D geological models <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologische_3dmodelle>`__ (ch.swisstopo.geologie-geologische_3dmodelle)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `4G - LTE / LTE-A <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-4g>`__ (ch.bakom.mobilnetz-4g)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2G - GSM / EDGE <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-2g>`__ (ch.bakom.mobilnetz-2g)                                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Advice on renewable energy <//map.geo.admin.ch/?layers=ch.bfe.erneuerbarheizen>`__ (ch.bfe.erneuerbarheizen)                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `5G - NR <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-5g>`__ (ch.bakom.mobilnetz-5g)                                                                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3D terrain and corresponding backgroundmaps <//s.geo.admin.ch/8a12282172>`__ (ch.swisstopo.swisstlm3d-karte-grau.3d and ch.swisstopo.swisstlm3d-karte-farbe.3d)                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mapping of Floodplains of National Importance <//map.geo.admin.ch/?layers=ch.bafu.auen-vegetationskarten>`__ (ch.bafu.auen-vegetationskarten)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geosites <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geosites>`__ (ch.swisstopo.geologie-geosites)                                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geo-trails <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geowege>`__ (ch.swisstopo.geologie-geowege)                                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20200520:

Release 20200520 - Wednesday, Mai 20th 2020
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_200318...r_200520>`__
- Announcement:
    - The ARE layer `ch.are.agglomerationen_isolierte_staedte` (Agglomerations - Definition 2000) will be removed from the BGDI services on 01.07.2020. The layer will be replaced by `ch.are.agglomerationsverkehr` (on prod starting 20.05.2020).
    - The swisstopo layer `ch.swisstopo-vd.geometa-los` will be completely removed from the FSDI services during Q2/2020.
    - The geology layer `ch.swisstopo.geologie-generalkarte-ggk200_papier.metadata` will be removed from CHSDI services on May 20th 2020.

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r200318...r_200520>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accessibility by road <//map.geo.admin.ch/?layers=ch.are.erreichbarkeit-miv>`__ (ch.are.erreichbarkeit-miv)                                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway noise, perm. immissions D <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag)         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway noise, perm. immissions N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht)     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `GeoEvents on request <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geoevents_anfrage>`__ (ch.swisstopo.geologie-geoevents_anfrage)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Cities and conurbations BeSA <//map.geo.admin.ch/?layers=ch.are.agglomerationsverkehr>`__ (ch.are.agglomerationsverkehr)                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geosites <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geosites>`__ (ch.swisstopo.geologie-geosites)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accessibility by PT <//map.geo.admin.ch/?layers=ch.are.erreichbarkeit-oev>`__ (ch.are.erreichbarkeit-oev)                                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Travel time to agglos by road <//map.geo.admin.ch/?layers=ch.are.reisezeit-agglomerationen-miv>`__ (ch.are.reisezeit-agglomerationen-miv)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Upcoming GeoEvents <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geoevents_demnaechst>`__ (ch.swisstopo.geologie-geoevents_demnaechst)                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Published shooting range bulletins and hazard zones <//map.geo.admin.ch/?layers=ch.vbs.schiessanzeigen>`__ (ch.vbs.schiessanzeigen)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Travel time to agglos by PT <//map.geo.admin.ch/?layers=ch.are.reisezeit-agglomerationen-oev>`__ (ch.are.reisezeit-agglomerationen-oev)                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway noise, act. immissions N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht)        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway noise, act. immissions D <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag)            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Amtliches Gebäudeadressverzeichnis <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis>`__ (ch.swisstopo.amtliches-gebaeudeadressverzeichnis)                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Travel time to centres by PT <//map.geo.admin.ch/?layers=ch.are.reisezeit-oev>`__ (ch.are.reisezeit-oev)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Travel time to centres by road <//map.geo.admin.ch/?layers=ch.are.reisezeit-miv>`__ (ch.are.reisezeit-miv)                                                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geo-trails <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geowege>`__ (ch.swisstopo.geologie-geowege)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy-Regions <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-energieregionen>`__ (ch.bfe.energiestaedte-energieregionen)                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Passenger traffic (public transport) <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-bahn>`__ (ch.are.belastung-personenverkehr-bahn)                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Passenger traffic <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-strasse>`__ (ch.are.belastung-personenverkehr-strasse)                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) N emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) D emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag)      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map swissTLM (color) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-farbe>`__ (ch.swisstopo.swisstlm3d-karte-farbe)                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map swissTLM (grey) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-grau>`__ (ch.swisstopo.swisstlm3d-karte-grau)                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20200318:

Release 20200318 - Wednesday, March 18th 2020
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_191218...r_200318>`__
- Announcement:
    - The ARE layer `ch.are.agglomerationen_isolierte_staedte` (Agglomerations - Definition 2000) will be removed from the BGDI services on 01.07.2020. The layer will be replaced by `ch.are.agglomerationsverkehr` (on prod starting 20.05.2020).
    - The swisstopo layer `ch.swisstopo-vd.geometa-los` will be completely removed from the FSDI services during Q2/2020.
    - The geology layer `ch.swisstopo.geologie-generalkarte-ggk200_papier.metadata` will be removed from CHSDI services on May 20th 2020.

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r191218...r_200318>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `3D geological models <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologische_3dmodelle>`__ (ch.swisstopo.geologie-geologische_3dmodelle)                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sunshine cumulative daily total <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-sonnenscheindauer-kumuliert-10min>`__ (ch.meteoschweiz.messwerte-sonnenscheindauer-kumuliert-10min)                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2km2 sub catchment areas <//map.geo.admin.ch/?layers=ch.bafu.wasser-teileinzugsgebiete_2>`__ (ch.bafu.wasser-teileinzugsgebiete_2)                                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `40km2 sub catchment areas <//map.geo.admin.ch/?layers=ch.bafu.wasser-teileinzugsgebiete_40>`__ (ch.bafu.wasser-teileinzugsgebiete_40)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mean runoff (m³/s) and regime <//map.geo.admin.ch/?layers=ch.bafu.mittlere-abfluesse>`__ (ch.bafu.mittlere-abfluesse)                                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrological gauging stations <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hydromessstationen>`__ (ch.bafu.hydrologie-hydromessstationen)                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Area outlets <//map.geo.admin.ch/?layers=ch.bafu.wasser-gebietsauslaesse>`__ (ch.bafu.wasser-gebietsauslaesse)                                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Type of flow regime <//map.geo.admin.ch/?layers=ch.bafu.wasser-vorfluter>`__ (ch.bafu.wasser-vorfluter)                                                                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:500'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk500.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk500.noscale)                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 1st night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde)                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 2nd night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde)                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lmax <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel)     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lr <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter)                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. last night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light / large aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge)    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. milit. aerodr. (tot.) <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=1986&time=1986>`__ (ch.swisstopo.swissimage-product)                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=1986&time=1986>`__ (ch.swisstopo.swissimage-product.metadata)                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3D Objects from TLM <https://s.geo.admin.ch/81bdb0f497>`__ (ch.swisstopo.swisstlm3d.3d)                                                                                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents in the annual comparison <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_jahresvergleich>`__ (ch.astra.schwerverunfallte-kanton_jahresvergleich)                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20191218:

Release 20191218 - Wednesday, December 18th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_191204...r_191218>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_191204...r191218>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `5G - NR <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-5g>`__ (ch.bakom.mobilnetz-5g)                                                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division swissSURFACE3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d.metadata>`__ (ch.swisstopo.swisssurface3d.metadata)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre FTTB/FTTH <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1000>`__ (ch.bakom.downlink1000)                                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 500 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink500>`__ (ch.bakom.downlink500)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 300 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink300>`__ (ch.bakom.downlink300)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 30 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink30>`__ (ch.bakom.downlink30)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 3 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink3>`__ (ch.bakom.downlink3)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1000>`__ (ch.bakom.uplink1000)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `4G - LTE / LTE-A <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-4g>`__ (ch.bakom.mobilnetz-4g)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3G - UMTS / HSPA <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-3g>`__ (ch.bakom.mobilnetz-3g)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2G - GSM / EDGE <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-2g>`__ (ch.bakom.mobilnetz-2g)                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Zones) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alp. Floodplains outside Fed. Inv. <//map.geo.admin.ch/?layers=ch.bafu.auen-ausserhalb_bundesinventar_alpin>`__ (ch.bafu.auen-ausserhalb_bundesinventar_alpin)                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Filling stations BEBECO <//map.geo.admin.ch/?layers=ch.vbs.bundestankstellen-bebeco>`__ (ch.vbs.bundestankstellen-bebeco)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=2017&time=2017>`__ (ch.swisstopo.swissimage-product.metadata)   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=2017&time=2017>`__ (ch.swisstopo.swissimage-product)                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20191204:

Release 20191204 - Wednesday, December 4th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_191113...r_191204>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_191113...r191204>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Thermal networks <//map.geo.admin.ch/?layers=ch.bfe.thermische-netze>`__ (ch.bfe.thermische-netze)                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Traffic counting locations - principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung-uebergeordnet)                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal )                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:100'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk100.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk100.noscale)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20191113:

Release 20191113 - Wednesday, November 13th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_191023...r_191113>`__
- Announcement:
    - The ASTRA layer `ch.astra.ausnahmetransportrouten` (Routes for exceptional loads) will be removed from the BGDI services in December 2019.
    - The two geology layers `ch.swisstopo.geologie-geotechnik-ziegeleien_1965` and `ch.swisstopo.geologie-geotechnik-ziegeleien_1995` are as per now removed from the BGDI services.

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_191023...r191113>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Impulsberatung erneuerbar heizen <//map.geo.admin.ch/?layers=ch.bfe.erneuerbarheizen>`__ (ch.bfe.erneuerbarheizen)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ziegeleirohstoffe: Abbau <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-ziegel_abbau>`__ (ch.swisstopo.geologie-rohstoffe-ziegel_abbau)                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `COMO projects <//map.geo.admin.ch/?layers=ch.bfe.komo-projekte>`__ (ch.bfe.komo-projekte)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ziegeleirohstoffe: Verarbeitung <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung>`__ (ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung)                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Snowshoe trekking <//map.geo.admin.ch/?layers=ch.swisstopo.schneeschuhwandern>`__ (ch.swisstopo.schneeschuhwandern)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Jan. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_jan>`__ (ch.bafu.erosion-gruenland_bodenabtrag_jan)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Feb. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_feb>`__ (ch.bafu.erosion-gruenland_bodenabtrag_feb)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Mrz. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_mrz>`__ (ch.bafu.erosion-gruenland_bodenabtrag_mrz)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Apr. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_apr>`__ (ch.bafu.erosion-gruenland_bodenabtrag_apr)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Mai <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_mai>`__ (ch.bafu.erosion-gruenland_bodenabtrag_mai)                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Jun. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_jun>`__ (ch.bafu.erosion-gruenland_bodenabtrag_jun)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Jul. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_jul>`__ (ch.bafu.erosion-gruenland_bodenabtrag_jul)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Aug. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_aug>`__ (ch.bafu.erosion-gruenland_bodenabtrag_aug)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Sep. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_sep>`__ (ch.bafu.erosion-gruenland_bodenabtrag_sep)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Okt. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_okt>`__ (ch.bafu.erosion-gruenland_bodenabtrag_okt)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Nov. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_nov>`__ (ch.bafu.erosion-gruenland_bodenabtrag_nov)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erosion risk permanent grassland Dez. <//map.geo.admin.ch/?layers=ch.bafu.erosion-gruenland_bodenabtrag_dez>`__ (ch.bafu.erosion-gruenland_bodenabtrag_dez)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Fresh snow, 2 days <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-neuschnee-2d>`__ (ch.meteoschweiz.messwerte-neuschnee-2d)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Fresh snow, 3 days <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-neuschnee-3d>`__ (ch.meteoschweiz.messwerte-neuschnee-3d)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation, 24h total <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-niederschlag-24h>`__ (ch.meteoschweiz.messwerte-niederschlag-24h)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation, 48h total <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-niederschlag-48h>`__ (ch.meteoschweiz.messwerte-niederschlag-48h)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation, 72h total <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-niederschlag-72h>`__ (ch.meteoschweiz.messwerte-niederschlag-72h)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wind gust 1 s, max. 6 h <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-6h>`__ (ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-6h)                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Pressure change, 3 h <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-luftdruck-differenz-3h>`__ (ch.meteoschweiz.messwerte-luftdruck-differenz-3h)                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20191023:

Release 20191023 - Wednesday, October 23th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190924...r_191023>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190924...r191023>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dam <//map.geo.admin.ch/?layers=ch.bfe.stauanlagen-bundesaufsicht>`__ (ch.bfe.stauanlagen-bundesaufsicht)                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected Areas VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-adminboundaries-protectedarea>`__ (ch.swisstopo.vec200-adminboundaries-protectedarea)                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forested areas <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover-wald>`__ (ch.swisstopo.vec200-landcover-wald)                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects  VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transportation VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr)         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Axis of national routes <//map.geo.admin.ch/?layers=ch.astra.nationalstrassenachsen>`__ (ch.astra.nationalstrassenachsen)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Winter national map LK10, LK25, LK50, LK100 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-winter>`__ (ch.swisstopo.pixelkarte-farbe-winter)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190924:

Release 20190924 - Tuesday, September 24th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190910...r_190924>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q4 2019.
    - The BLW layer `ch.blw.erosion-mit_bergzonen` will be completely removed from the FSDI services during Q4 2019.
    - The `Charging points for electric cars` layer with live data about more than 2500 chargins points is now queryable via our api.


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190910...r190924>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Alp. Floodplains outside Fed. Inv. <//map.geo.admin.ch/?layers=ch.bafu.auen-ausserhalb_bundesinventar_alpin>`__ (ch.bafu.auen-ausserhalb_bundesinventar_alpin)                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging points for electric cars <//map.geo.admin.ch/?layers=ch.bfe.ladestellen-elektromobilitaet>`__ (ch.bfe.ladestellen-elektromobilitaet)                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hospital landing sites <//map.geo.admin.ch/?layers=ch.bazl.spitallandeplaetze>`__ (ch.bazl.spitallandeplaetze)                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Groundwater level/spring discharge <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_grundwasserzustand>`__ (ch.bafu.hydroweb-messstationen_grundwasserzustand)                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190910:

Release 20190910 - Tuesday, September 10th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190807...r_190910>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q4 2019.
    - The BLW layer `ch.blw.erosion-mit_bergzonen` will be completely removed from the FSDI services during Q4 2019.


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190807...r190910>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Recent earthquakes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-aktuelle_erdbeben>`__ (ch.bafu.gefahren-aktuelle_erdbeben)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy cities <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte>`__ (ch.bfe.energiestaedte)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy advice services <//map.geo.admin.ch/?layers=ch.bfe.energieberatungsstellen>`__ (ch.bfe.energieberatungsstellen)                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of forest damage – projectile <//map.geo.admin.ch/?layers=ch.vbs.waldschadenkarte>`__ (ch.vbs.waldschadenkarte)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190807:

Release 20190807 - Wednesday, August 7th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190626...r_190807>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190626...r190807>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wasserverfügbarkeit im Boden <//map.geo.admin.ch/?layers=ch.bafu.wald-wasserverfuegbarkeit_boden>`__ (ch.bafu.wald-wasserverfuegbarkeit_boden)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wasserverfügbarkeit für Pflanzen <//map.geo.admin.ch/?layers=ch.bafu.wald-wasserverfuegbarkeit_pflanzen>`__ (ch.bafu.wald-wasserverfuegbarkeit_pflanzen)                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Flow-path map <//map.geo.admin.ch/?layers=ch.blw.erosion-fliesswegkarte>`__ (ch.blw.erosion-fliesswegkarte)                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Erosion risk crop quantitative <//map.geo.admin.ch/?layers=ch.blw.erosion-quantitativ>`__ (ch.blw.erosion-quantitativ)                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Erosion risk crop qualitative <//map.geo.admin.ch/?layers=ch.blw.erosion>`__ (ch.blw.erosion)                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PGI meat products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Biogas plants <//map.geo.admin.ch/?layers=ch.bfe.biogasanlagen>`__ (ch.bfe.biogasanlagen)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy advice services <//map.geo.admin.ch/?layers=ch.bfe.energieberatungsstellen>`__ (ch.bfe.energieberatungsstellen)                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PDO cheese <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tresurehunt <//map.geo.admin.ch/?layers=ch.swisstopo.treasurehunt>`__ (ch.swisstopo.treasurehunt)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190626:

Release 20190626 - Wednesday, June 26th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190605...r_190626>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190605...r190626>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Heat and cooling sources <//map.geo.admin.ch/?layers=ch.bfe.fernwaerme-angebot>`__ (ch.bfe.fernwaerme-angebot)                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Heat/cooling demand: industry <//map.geo.admin.ch/?layers=ch.bfe.fernwaerme-nachfrage_industrie>`__ (ch.bfe.fernwaerme-nachfrage_industrie)                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Heat/cooling demand: resid./comm. <//map.geo.admin.ch/?layers=ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude>`__ (ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude)     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alps with guard dogs <//map.geo.admin.ch/?layers=ch.bafu.alpweiden-herdenschutzhunde>`__ (ch.bafu.alpweiden-herdenschutzhunde)                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre FTTB/FTTH <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2G - GSM / EDGE <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-2g>`__ (ch.bakom.mobilnetz-2g)                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3G - UMTS / HSPA <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-3g>`__ (ch.bakom.mobilnetz-3g)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `4G - LTE / LTE-A <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-4g>`__ (ch.bakom.mobilnetz-4g)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 3 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink3>`__ (ch.bakom.downlink3)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 30 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink30>`__ (ch.bakom.downlink30)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 300 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink300>`__ (ch.bakom.downlink300)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 500 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink500>`__ (ch.bakom.downlink500)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1000>`__ (ch.bakom.downlink1000)                                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1000>`__ (ch.bakom.uplink1000)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_festnetz>`__ (ch.bakom.notruf-117_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_mobilnetz>`__ (ch.bakom.notruf-117_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_festnetz>`__ (ch.bakom.notruf-143_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_mobilnetz>`__ (ch.bakom.notruf-143_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_festnetz>`__ (ch.bakom.notruf-144_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_mobilnetz>`__ (ch.bakom.notruf-144_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_festnetz>`__ (ch.bakom.notruf-147_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_mobilnetz>`__ (ch.bakom.notruf-147_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Waste incineration plants <//map.geo.admin.ch/?layers=ch.bfe.kehrichtverbrennungsanlagen>`__ (ch.bfe.kehrichtverbrennungsanlagen)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Field block map <//map.geo.admin.ch/?layers=ch.blw.feldblockkarte>`__ (ch.blw.feldblockkarte)                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Patrouille des Glaciers (A race) <//map.geo.admin.ch/?layers=ch.vbs.patrouilledesglaciers-a_rennen>`__ (ch.vbs.patrouilledesglaciers-a_rennen)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Patrouille des Glaciers (Z race) <//map.geo.admin.ch/?layers=ch.vbs.patrouilledesglaciers-z_rennen>`__ (ch.vbs.patrouilledesglaciers-z_rennen)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung&topic=sachplan>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190605:

Release 20190605 - Wednesday, June 5th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Features geometries reprojection to `LV03` (EPSG:21781), `WGS1984` (EPSG:4326) and `Spherical mercator` (EPSG:3857)
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190513...r_190605>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190513...r190605>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20190513:

Release 20190513 - Monday, May 13th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190429...r_190513>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190429...r_190513>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway location and areas MAO <//map.geo.admin.ch/?layers=ch.bav.lage-stoerfallverordnung_eisenbahnanlagen>`__ (ch.bav.lage-stoerfallverordnung_eisenbahnanlagen)                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SWISSIMAGE HIST 1946 <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product_1946>`__ (ch.swisstopo.swissimage-product_1946)                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) N emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) D emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag)      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest Reserves <//map.geo.admin.ch/?layers=ch.bafu.waldreservate>`__ (ch.bafu.waldreservate)                                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Forest Preserves <//map.geo.admin.ch/?layers=ch.pronatura.waldreservate>`__ (ch.pronatura.waldreservate)                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Enterprises <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G1, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g1>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g1)                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G2, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g2>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g2)                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Buildings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude)                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Population (residents) <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner>`__ (ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner)                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dwellings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen)                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissTLM-Map light (color) <https://s.geo.admin.ch/81bdb0f497>`__ (ch.swisstopo.swisstlm3d-karte-farbe.3d)                                                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissTLM-Map light (grey) <https://s.geo.admin.ch/81bdb2620c>`__ (ch.swisstopo.swisstlm3d-karte-grau.3d)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `3D Objects from TLM <https://s.geo.admin.ch/81bdb0f497>`__ (ch.swisstopo.swisstlm3d.3d)                                                                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy cities <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte>`__ (ch.bfe.energiestaedte)                                                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy-Regions <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-energieregionen>`__ (ch.bfe.energiestaedte-energieregionen)                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 25 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte25_papier.metadata>`__ (ch.swisstopo.landeskarte25_papier.metadata)                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190429:

Release 20190429 - Monday, April 29th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190410...r_190429>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.
    - The following BAFU layers are today removed from the BGDI services
        - ch.bafu.holzvorrat
        - ch.bafu.holznutzung
        - ch.bafu.holzzuwachs
        - ch.bafu.landesforstinventar-baumarten
        - ch.bafu.landesforstinventar-totholz
        - ch.bafu.landesforstinventar-waldanteil


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190410...r_190429>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Areas of silver fir <//map.geo.admin.ch/?layers=ch.bafu.wald-tannenareale>`__ (ch.bafu.wald-tannenareale)                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Forest ecoregions <//map.geo.admin.ch/?layers=ch.bafu.wald-standortsregionen>`__ (ch.bafu.wald-standortsregionen)                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Altitudinal zones 2085 less dry <//map.geo.admin.ch/?layers=ch.bafu.wald-vegetationshoehenstufen_2085_weniger_trocken>`__ (ch.bafu.wald-vegetationshoehenstufen_2085_weniger_trocken)     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `<Altitudinal zones 2085 dry <//map.geo.admin.ch/?layers=ch.bafu.wald-vegetationshoehenstufen_2085_trocken>`__ (ch.bafu.wald-vegetationshoehenstufen_2085_trocken)                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Altitudinal zones 1995 <//map.geo.admin.ch/?layers=ch.bafu.wald-vegetationshoehenstufen_1995>`__ (ch.bafu.wald-vegetationshoehenstufen_1995)                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hydrological network VECTOR25 <//map.geo.admin.ch/?layers=ch.swisstopo.vec25-gewaessernetz_referenz>`__ (ch.swisstopo.vec25-gewaessernetz_referenz)                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_hochwasser>`__ (ch.bafu.showme-gemeinden_hochwasser)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_lawinen>`__ (ch.bafu.showme-gemeinden_lawinen)                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_rutschungen>`__ (ch.bafu.showme-gemeinden_rutschungen)                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: fall processes <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_sturzprozesse>`__ (ch.bafu.showme-gemeinden_sturzprozesse)                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_hochwasser>`__ (ch.bafu.showme-kantone_hochwasser)                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_lawinen>`__ (ch.bafu.showme-kantone_lawinen)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_rutschungen>`__ (ch.bafu.showme-kantone_rutschungen)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: fall processes <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_sturzprozesse>`__ (ch.bafu.showme-kantone_sturzprozesse)                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Statistics on hydropower plants (WASTA) <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20190410:

Release 20190410 - Wednesday, April 10th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190327...r_190410>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.
    - The following BAFU layers will be removed from the BGDI services on 29.04.2019
        - ch.bafu.holzvorrat
        - ch.bafu.holznutzung
        - ch.bafu.holzzuwachs
        - ch.bafu.landesforstinventar-baumarten
        - ch.bafu.landesforstinventar-totholz
        - ch.bafu.landesforstinventar-waldanteil


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190327...r_190410>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Waste incineration plants <//map.geo.admin.ch/?layers=ch.bfe.kehrichtverbrennungsanlagen>`__ (ch.bfe.kehrichtverbrennungsanlagen)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division swissSURFACE3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d.metadata>`__ (ch.swisstopo.swisssurface3d.metadata)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents in the annual comparison <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_jahresvergleich>`__ (ch.astra.schwerverunfallte-kanton_jahresvergleich)                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tracer tests <//map.geo.admin.ch/?layers=ch.bafu.hydrogeologie-markierversuche>`__ (ch.bafu.hydrogeologie-markierversuche)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190327:

Release 20190327 - Wednesday, March 27th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190313...r_190327>`__
- Announcement:
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.
    - The following BAFU layers will be removed from the BGDI services on 29.04.2019
        - ch.bafu.holzvorrat
        - ch.bafu.holznutzung
        - ch.bafu.holzzuwachs
        - ch.bafu.landesforstinventar-baumarten
        - ch.bafu.landesforstinventar-totholz
        - ch.bafu.landesforstinventar-waldanteil


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190313...r_190327>`__


Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperature model - data <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturmodell_eingangsdaten>`__ (ch.swisstopo.geologie-geomol-temperaturmodell_eingangsdaten)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures Top Upper Malm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperatur_top_omalm>`__ (ch.swisstopo.geologie-geomol-temperatur_top_omalm)                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures Top OMM <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperatur_top_omm>`__ (ch.swisstopo.geologie-geomol-temperatur_top_omm)                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures Top Muschelkalk <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk>`__ (ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk)                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures 1000 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_1000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_1000)                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures 500 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_500>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_500)                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures 1500 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_1500>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_1500)                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures 2000 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_2000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_2000)                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures 3000 m depth <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_3000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_3000)                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Temperatures 4000 m depth - data <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-temperaturverteilung_4000>`__ (ch.swisstopo.geologie-geomol-temperaturverteilung_4000)                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Elevation 100 °C isotherm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-isotherme_100>`__ (ch.swisstopo.geologie-geomol-isotherme_100)                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Elevation 60 °C isotherm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-isotherme_60>`__ (ch.swisstopo.geologie-geomol-isotherme_60)                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Elevation 150 °C isotherm <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol-isotherme_150>`__ (ch.swisstopo.geologie-geomol-isotherme_150)                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (fixed) N emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht)     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (fixed) D emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag)         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) N emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) D emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag)      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - TMA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-nahkontrollbezirke>`__ (ch.bazl.luftraeume-nahkontrollbezirke)                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - FIZ <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationszonen>`__ (ch.bazl.luftraeume-fluginformationszonen)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - CTR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollzonen>`__ (ch.bazl.luftraeume-kontrollzonen)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - CTR <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronatutical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISS MIL PILOTS CHART <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20190313:

Release 20190313 - Wednesday, March 13th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190227...r_190313>`__
- Announcement:
    - The layer `ch.bfe.energiestaedte-2000watt-aufdemweg` is now completely removed from the BGDI.
    - The BAG layer `ch.bag.zecken-lyme` will be completely removed from the BGDI services during Q2 2019.

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190227...r_190313>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PCP Inventory <//map.geo.admin.ch/?layers=ch.babs.kulturgueter>`__ (ch.babs.kulturgueter)                                                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20190227:

Release 20190227 - Wednesday, February 27th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190220...r_190227>`__
- Announcement:
    - The layer `ch.sgpk.maechtigkeit-lockergesteine` is now fully decommissioned. Please use `ch.swisstopo.geologie-lockergestein_maechtigkeitsmodell` instead.
    - The layer `ch.bfe.energiestaedte-2000watt-aufdemweg` is now removed from the map.geo.admin.ch catalogs. The layer will be completely removed from the BGDI on 13.03.2019.
    - The BAG decided to update the layers `ch.bag.zecken-fsme-faelle`, `ch.bag.zecken-fsme-impfung` instead of decommissioning them as previously announced. Those two layers are updated today and will continue to work as before in teh BGDI.
    - The BAG layer `ch.bag.zecken-lyme` is still tagged for decommission. It is today removed from the map.geo.admin.ch catalogs and will be completely removed from the BGDI services during Q2 2019.


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190220...r_190227>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Biogas plants <//map.geo.admin.ch/?layers=ch.bfe.biogasanlagen>`__ (ch.bfe.biogasanlagen)                                                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Zeckenstichmodell <//map.geo.admin.ch/?layers=ch.bag.zeckenstichmodell>`__ (ch.bag.zeckenstichmodell)                                                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Floodplains outside the federal inventary <//map.geo.admin.ch/?layers=ch.bafu.auen-ausserhalb_bundesinventar>`__ (ch.bafu.auen-ausserhalb_bundesinventar)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability of the PLR Cadastre <//map.geo.admin.ch/?layers=ch.swisstopo-vd.stand-oerebkataster>`__ (ch.swisstopo-vd.stand-oerebkataster)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: cluster <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: recommendation of vaccination <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-impfung>`__ (ch.bag.zecken-fsme-impfung)                                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Official street index <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-strassenverzeichnis>`__ (ch.swisstopo.amtliches-strassenverzeichnis)                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20190220:

Release 20190220 - Wednesday, February 20th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190206...r_190220>`__
- Announcement:
    - Swisssearch the order of the search results has been changed. The resultset can contain now up to 10 exact search results on top, followed by the other results. `Additional Information <https://github.com/geoadmin/mf-chsdi3/pull/3073>`__.

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190206...r_190220>`__

.. _releasenotes_20190206:

Release 20190206 - Wednesday, February 6th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_190123...r_190206>`__
- Announcement:
    - The layer `ch.sgpk.maechtigkeit-lockergesteine` is from today on replaced with `ch.swisstopo.geologie-lockergestein_maechtigkeitsmodell` in the catalogs. The layer `ch.sgpk.maechtigkeit-lockergesteine` will be completely removed from the BGDI in Q2 2019 (middle 2019).
    - The layer `ch.bfe.energiestaedte-2000watt-aufdemweg` will be removed from the map.geo.admin.ch catalogs on 27.02. The layer will be completely removed from the BGDI on 13.03.2019.
    - The 3 BAG layers `ch.bag.zecken-fsme-faelle`, `ch.bag.zecken-fsme-impfung` and `ch.bag.zecken-lyme` will be removed from the map.geo.admin.ch catalogs on 27.02 and completely removed from all the BGDI services on 27.03. Those layers will be collectively replaced on 27.02 by the new layer `ch.bag.zeckenstichmodell` and by the layer `ch.bag.borelliose-verbreitung` on 10.04
- New layer (API only) : ch.bazl.hindernisbegrenzungsflaechen-perimeter

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_190123...r_190206>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Thickness of unconsolidated deposits <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-lockergestein_maechtigkeitsmodell>`__ (ch.swisstopo.geologie-lockergestein_maechtigkeitsmodell)        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Bedrock elevation model <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-felsoberflaeche_hoehenmodell>`__ (ch.swisstopo.geologie-felsoberflaeche_hoehenmodell)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind speed 50 meters above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h50>`__ (ch.bfe.windenergie-geschwindigkeit_h50)                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind speed 75 meters above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h75>`__ (ch.bfe.windenergie-geschwindigkeit_h75)                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind speed 100 meters above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h100>`__ (ch.bfe.windenergie-geschwindigkeit_h100)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind speed 125 meters above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h1250>`__ (ch.bfe.windenergie-geschwindigkeit_h125)                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind speed 150 meters above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h150>`__ (ch.bfe.windenergie-geschwindigkeit_h150)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations local <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal>`__ (ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Background map hydrol. data <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hintergrundkarte>`__ (ch.bafu.hydrologie-hintergrundkarte)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Biosphere reserves <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-biosphaerenreservate>`__ (ch.bafu.schutzgebiete-biosphaerenreservate)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Built-up areas VIL <//map.geo.admin.ch/?layers=ch.bazl.bebaute-gebiete_luftfahrtrecht>`__ (ch.bazl.bebaute-gebiete_luftfahrtrecht)                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20190123:

Release 20181219 - Wednesday, January 23th 2019
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_181205...r_190123>`__
- Announcement:
   - 9 NGA layers are today completely removed from the API without substitution:
      - ch.bakom.verfuegbarkeit-tv
      - ch.bakom.verfuegbarkeit-hdtv
      - ch.bakom.uplink2
      - ch.bakom.uplink50
      - ch.bakom.uplink20
      - ch.bakom.downlink1
      - ch.bakom.downlink2
      - ch.bakom.downlink20
      - ch.bakom.downlink50
   - From February 6th 2019 on the layer `ch.sgpk.maechtigkeit-lockergesteine` will be replaced with `ch.swisstopo.geologie-lockergestein_maechtigkeitsmodell` in the catalogs. The layer `ch.sgpk.maechtigkeit-lockergesteine` will be completely removed from the BGDI in Q2 2019 (middle 2019).

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_181205...r_190123>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Konsultationsbereiche Rohrleitungen <//map.geo.admin.ch/?layers=ch.bfe.rohrleitungen-konsultationsbereiche>`__ (ch.bfe.rohrleitungen-konsultationsbereiche)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update |  `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Journey through time <//map.geo.admin.ch/?layers=ch.swisstopo.zeitreihen>`__ (ch.swisstopo.zeitreihen)                                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=2017&time=2017>`__ (ch.swisstopo.swissimage-product.metadata)   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=2017&time=2017>`__ (ch.swisstopo.swissimage-product)                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Historical monuments' rocks <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke>`__ (ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke)   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _releasenotes_20181219:

Release 20181219 - Wednesday, December 19th 2018
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_181205...r_181219>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_181205...r_181219>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Woody biomass for energy <//map.geo.admin.ch/?layers=ch.bfe.biomasse-verholzt>`__ (ch.bfe.biomasse-verholzt)                                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Non-woody biomass for energy <//map.geo.admin.ch/?layers=ch.bfe.biomasse-nicht-verholzt>`__ (ch.bfe.biomasse-nicht-verholzt)                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Zones) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 3 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink3>`__ (ch.bakom.downlink3)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `4G - LTE / LTE-A <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-4g>`__ (ch.bakom.mobilnetz-4g)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 300 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink300>`__ (ch.bakom.downlink300)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1000>`__ (ch.bakom.uplink1000)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snow avalanches (SilvaProtect-CH) <//map.geo.admin.ch/?layers=ch.bafu.silvaprotect-lawinen>`__ (ch.bafu.silvaprotect-lawinen)                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tankstellen BEBECO <//map.geo.admin.ch/?layers=ch.vbs.bundestankstellen-bebeco>`__ (ch.vbs.bundestankstellen-bebeco)                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _releasenotes_20181205:

Release 20181205 - Wednesday, December 5th 2018
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_181120...r_181205>`__
- Announcement:
   - 9 NGA layers will be removed completely from the API by January 23rd 2019 without substitution:
      - ch.bakom.verfuegbarkeit-tv
      - ch.bakom.verfuegbarkeit-hdtv
      - ch.bakom.uplink2
      - ch.bakom.uplink50
      - ch.bakom.uplink20
      - ch.bakom.downlink1
      - ch.bakom.downlink2
      - ch.bakom.downlink20
      - ch.bakom.downlink50
   - Complete removal of ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung from the FSDI (including WMS and API). If possible, use `ch.bfe.sachplan-geologie-tiefenlager` instead.
   - Removal of ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung from the catalogs. If possible, use `ch.bfe.sachplan-geologie-tiefenlager` instead. From March 2019 on the layer will be removed completely.
   - Removal of a geology layer. From February 6th 2019 on the layer listed below will be replaced with `ch.swisstopo.geologie-lockergestein_maechtigkeitsmodell`. The layer `ch.sgpk.maechtigkeit-lockergesteine` will disappear completely by Q2 2019 (middle 2019).
      - ch.sgpk.maechtigkeit-lockergesteine



`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_181120...r_181205>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `117 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_mobilnetz>`__ (ch.bakom.notruf-117_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `117 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_festnetz>`__ (ch.bakom.notruf-117_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `143 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_mobilnetz>`__ (ch.bakom.notruf-143_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `144 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_festnetz>`__ (ch.bakom.notruf-144_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `147 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_festnetz>`__ (ch.bakom.notruf-147_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `143 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_festnetz>`__ (ch.bakom.notruf-143_festnetz)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `147 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_mobilnetz>`__ (ch.bakom.notruf-147_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `144 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_mobilnetz>`__ (ch.bakom.notruf-144_mobilnetz)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Built-up areas VIL <//map.geo.admin.ch/?layers=ch.bazl.bebaute-gebiete_luftfahrtrecht>`__ (ch.bazl.bebaute-gebiete_luftfahrtrecht)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Water & migrant bird reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-vogelreservate>`__ (ch.bafu.bundesinventare-vogelreservate)                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Deep Geol. Repositories <//map.geo.admin.ch/?layers=ch.bfe.sachplan-geologie-tiefenlager>`__ (ch.bfe.sachplan-geologie-tiefenlager)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amtliches Strassenverzeichnis <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-strassenverzeichnis>`__ (ch.swisstopo.amtliches-strassenverzeichnis)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport stops <//map.geo.admin.ch/?layers=ch.bav.haltestellen-oev>`__ (ch.bav.haltestellen-oev)                                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _releasenotes_20181120:

Release 20181120 - Tuesday, November 20th 2018
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- migrate sphinx search from version 2.1.6 to version 2.2.11, due to this migration the order of the results within the same rank can slightly change
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_181031...r_181120>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_181031...r_181120>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Interregional wildlife corridor <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierkorridor_national>`__ (ch.bafu.fauna-wildtierkorridor_national)                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Arsenals <//map.geo.admin.ch/?layers=ch.vbs.retablierungsstellen>`__ (ch.vbs.retablierungsstellen)                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of forest damage – projectile <//map.geo.admin.ch/?layers=ch.vbs.waldschadenkarte>`__ (ch.vbs.waldschadenkarte)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500 m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Landeskarte Winter LK25, LK50 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-winter>`__ (ch.swisstopo.pixelkarte-farbe-winter)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIS consultation <//map.geo.admin.ch/?layers=ch.bav.sachplan-infrastruktur-schiene_anhorung>`__ (ch.bav.sachplan-infrastruktur-schiene_anhorung)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `AGNES <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-agnes>`__ (ch.swisstopo.fixpunkte-agnes)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Safety zone plan <//map.geo.admin.ch/?layers=ch.bazl.sicherheitszonenplan>`__ (ch.bazl.sicherheitszonenplan)                                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=bafu.wrz-wildruhezonen_portal>`__ (bafu.wrz-wildruhezonen_portal)                                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20181031:

Release 20181031 - Wednesday, October 31st 2018
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_181017...r_181031>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_181017...r_181031>`__


Geodata
*******

+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geothermal potential studies <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geothermische_potenzialstudien_regional>`__ (ch.swisstopo.geologie-geothermische_potenzialstudien_regional)   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20181017:

Release 20181017 - Wednesday, October 17th 2018
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180926...r_181017>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180926...r_181017>`__


Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Energy advice services <//map.geo.admin.ch/?layers=ch.bfe.energieberatungsstellen>`__ (ch.bfe.energieberatungsstellen)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected Areas VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-adminboundaries-protectedarea>`__ (ch.swisstopo.vec200-adminboundaries-protectedarea)                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forested areas <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover-wald>`__ (ch.swisstopo.vec200-landcover-wald)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects  VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transportation VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500 m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Deep geothermal projects <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tiefengeothermie_projekte>`__ (ch.swisstopo.geologie-tiefengeothermie_projekte)                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180926:

Release 20180926 - Wednesday, September 26th 2018
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180829...r_180926>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180829...r_180926>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nighttime railway noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_nacht>`__ (ch.bafu.laerm-bahnlaerm_nacht)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Daytime road traffic noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-strassenlaerm_tag>`__ (ch.bafu.laerm-strassenlaerm_tag)                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nighttime road traffic noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-strassenlaerm_nacht>`__ (ch.bafu.laerm-strassenlaerm_nacht)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Daytime railway noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_tag>`__ (ch.bafu.laerm-bahnlaerm_tag)                                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180829:

Release 20180829 - Wednesday, Augutst 29th 2018
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180718...r_180829>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180718...r_180829>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Landeskarte Winter LK25, LK50 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-winter>`__ (ch.swisstopo.pixelkarte-farbe-winter)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport stops <//map.geo.admin.ch/?layers=ch.bav.haltestellen-oev>`__ (ch.bav.haltestellen-oev)                                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_vector.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas_vector.metadata)   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division National Map 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.swiss-map-vector25.metadata>`__ (ch.swisstopo.swiss-map-vector25.metadata)                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180718:
   *******

Release 20180718 - Wednesday, July 18th 2018
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Added oereb layer ch.astra.baulinien-nationalstrassen.oereb
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180704...r_180718>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180704...r_180718>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SIN consultation <//map.geo.admin.ch/?layers=ch.astra.sachplan-infrastruktur-strasse_anhoerung>`__ (ch.astra.sachplan-infrastruktur-strasse_anhoerung)                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SP Road infrastructure <//map.geo.admin.ch/?layers=ch.astra.sachplan-infrastruktur-strasse_kraft>`__ (ch.astra.sachplan-infrastruktur-strasse_kraft)                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Building lines for motorways <//map.geo.admin.ch/?layers=ch.astra.baulinien-nationalstrassen>`__ (ch.astra.baulinien-nationalstrassen)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vegetation alpine floodplains <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-auen_vegetation_alpin>`__ (ch.bafu.bundesinventare-auen_vegetation_alpin)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Treasurehunt <//map.geo.admin.ch/?layers=ch.swisstopo.treasurehunt>`__ (ch.swisstopo.treasurehunt)                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180704:
   *******

Release 20180704 - Wednesday, July 4th 2018
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180627...r_180704>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180627...r_180704>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Download ≥ 500 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink500>`__ (ch.bakom.downlink500)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `2G - GSM / EDGE <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-2g>`__ (ch.bakom.mobilnetz-2g)                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `3G - UMTS / HSPA <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-3g>`__ (ch.bakom.mobilnetz-3g)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Download ≥ 30 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink30>`__ (ch.bakom.downlink30)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `4G - LTE / LTE-A <//map.geo.admin.ch/?layers=ch.bakom.mobilnetz-4g>`__ (ch.bakom.mobilnetz-4g)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Download ≥ 3 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink3>`__ (ch.bakom.downlink3)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Download ≥ 300 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink300>`__ (ch.bakom.downlink300)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Upload ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1000>`__ (ch.bakom.uplink1000)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Download ≥ 1000 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1000>`__ (ch.bakom.downlink1000)                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre FTTB/FTTH <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dam <//map.geo.admin.ch/?layers=ch.bfe.stauanlagen-bundesaufsicht>`__ (ch.bfe.stauanlagen-bundesaufsicht)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180627:
   *******

Release 20180627 - Wednesday, June 27th 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180530...r_180627>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180530...r_180627>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hydrocotyle ranunculoides <//map.geo.admin.ch/?layers=ch.bafu.neophyten-grosser_wassernabel>`__ (ch.bafu.neophyten-grosser_wassernabel)                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Prunus serotina <//map.geo.admin.ch/?layers=ch.bafu.neophyten-herbst_traubenkirsche>`__ (ch.bafu.neophyten-herbst_traubenkirsche)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sicyos angulatus <//map.geo.admin.ch/?layers=ch.bafu.neophyten-haargurke>`__ (ch.bafu.neophyten-haargurke)                                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reynoutria japonica <//map.geo.admin.ch/?layers=ch.bafu.neophyten-japanischer_staudenknoeterich>`__ (ch.bafu.neophyten-japanischer_staudenknoeterich)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Lonicera henryi <//map.geo.admin.ch/?layers=ch.bafu.neophyten-henrys_geissblatt>`__ (ch.bafu.neophyten-henrys_geissblatt)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Echinocystis lobata <//map.geo.admin.ch/?layers=ch.bafu.neophyten-igelgurke>`__ (ch.bafu.neophyten-igelgurke)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Cabomba caroliniana <//map.geo.admin.ch/?layers=ch.bafu.neophyten-karolina_haarnixe>`__ (ch.bafu.neophyten-karolina_haarnixe)                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sedum spurium <//map.geo.admin.ch/?layers=ch.bafu.neophyten-kaukasus_fettkraut>`__ (ch.bafu.neophyten-kaukasus_fettkraut)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Elodea canadensis <//map.geo.admin.ch/?layers=ch.bafu.neophyten-kanadische_wasserpest>`__ (ch.bafu.neophyten-kanadische_wasserpest)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Phytolacca americana <//map.geo.admin.ch/?layers=ch.bafu.neophyten-amerikanische_kermesbeere>`__ (ch.bafu.neophyten-amerikanische_kermesbeere)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solidago canadensis <//map.geo.admin.ch/?layers=ch.bafu.neophyten-kanadische_goldrute>`__ (ch.bafu.neophyten-kanadische_goldrute)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ambrosia artemisiifolia <//map.geo.admin.ch/?layers=ch.bafu.neophyten-aufrechtes_traubenkraut>`__ (ch.bafu.neophyten-aufrechtes_traubenkraut)                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Impatiens balfourii <//map.geo.admin.ch/?layers=ch.bafu.neophyten-balfours_springkraut>`__ (ch.bafu.neophyten-balfours_springkraut)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rubus armeniacus <//map.geo.admin.ch/?layers=ch.bafu.neophyten-armenische_brombeere>`__ (ch.bafu.neophyten-armenische_brombeere)                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Amorpha fruticosa <//map.geo.admin.ch/?layers=ch.bafu.neophyten-bastardindigo>`__ (ch.bafu.neophyten-bastardindigo)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `N.N. <//map.geo.admin.ch/?layers=ch.bafu.neophyten-amerikanischer_stinktierkohl>`__ (ch.bafu.neophyten-amerikanischer_stinktierkohl)                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reynoutria bohemica <//map.geo.admin.ch/?layers=ch.bafu.neophyten-bastard_staudenknoeterich>`__ (ch.bafu.neophyten-bastard_staudenknoeterich)                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Bassia scoparia <//map.geo.admin.ch/?layers=ch.bafu.neophyten-besen_radmelde>`__ (ch.bafu.neophyten-besen_radmelde)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paulownia tomentosa <//map.geo.admin.ch/?layers=ch.bafu.neophyten-blauglockenbaum>`__ (ch.bafu.neophyten-blauglockenbaum)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Myriophyllum aquaticum <//map.geo.admin.ch/?layers=ch.bafu.neophyten-brasilianisches_tausendblatt>`__ (ch.bafu.neophyten-brasilianisches_tausendblatt)                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Abutilon theophrasti <//map.geo.admin.ch/?layers=ch.bafu.neophyten-chinesische_samtpappel>`__ (ch.bafu.neophyten-chinesische_samtpappel)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Impatiens glandulifera <//map.geo.admin.ch/?layers=ch.bafu.neophyten-druesiges_springkraut>`__ (ch.bafu.neophyten-druesiges_springkraut)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solanum carolinense <//map.geo.admin.ch/?layers=ch.bafu.neophyten-carolina_nachtschatten>`__ (ch.bafu.neophyten-carolina_nachtschatten)                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Phytolacca esculenta <//map.geo.admin.ch/?layers=ch.bafu.neophyten-essbare_kermesbeere>`__ (ch.bafu.neophyten-essbare_kermesbeere)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Erigeron annuus <//map.geo.admin.ch/?layers=ch.bafu.neophyten-einjaehriges_berufkraut>`__ (ch.bafu.neophyten-einjaehriges_berufkraut)                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rhus typhina <//map.geo.admin.ch/?layers=ch.bafu.neophyten-essigbaum>`__ (ch.bafu.neophyten-essigbaum)                                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Senecio rupestris <//map.geo.admin.ch/?layers=ch.bafu.neophyten-felsen_greiskraut>`__ (ch.bafu.neophyten-felsen_greiskraut)                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Cyperus esculentus <//map.geo.admin.ch/?layers=ch.bafu.neophyten-essbares_zypergras>`__ (ch.bafu.neophyten-essbares_zypergras)                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Trachycarpus fortunei <//map.geo.admin.ch/?layers=ch.bafu.neophyten-fortunes_hanfpalme>`__ (ch.bafu.neophyten-fortunes_hanfpalme)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Glyceria striata <//map.geo.admin.ch/?layers=ch.bafu.neophyten-gestreiftes_suessgras>`__ (ch.bafu.neophyten-gestreiftes_suessgras)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `N.N. <//map.geo.admin.ch/?layers=ch.bafu.neophyten-grossbluetiges_heusenkraut>`__ (ch.bafu.neophyten-grossbluetiges_heusenkraut)                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Parthenocissus inserta <//map.geo.admin.ch/?layers=ch.bafu.neophyten-gewoehnliche_jungfernrebe>`__ (ch.bafu.neophyten-gewoehnliche_jungfernrebe)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Bunias orientalis <//map.geo.admin.ch/?layers=ch.bafu.neophyten-glattes_zackenschoetchen>`__ (ch.bafu.neophyten-glattes_zackenschoetchen)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ailanthus altissima <//map.geo.admin.ch/?layers=ch.bafu.neophyten-goetterbaum>`__ (ch.bafu.neophyten-goetterbaum)                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map3.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__  (ch.bfe.solarenergie-eignung-fassaden)                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180530:
   *******

Release 20180530 - Wednesday, Mai 30th 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180508...r_180530>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180508...r_180530>`__

Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements pressure station QFE <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-luftdruck-qfe-10min>`__ (ch.meteoschweiz.messwerte-luftdruck-qfe-10min)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements fresh snow <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-neuschnee-1d>`__ (ch.meteoschweiz.messwerte-neuschnee-1d)                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aviation stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-flugwetter>`__ (ch.meteoschweiz.messnetz-flugwetter)                                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements pressure reduced QFF <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-luftdruck-qff-10min>`__ (ch.meteoschweiz.messwerte-luftdruck-qff-10min)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerological stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-atmosphaere>`__ (ch.meteoschweiz.messnetz-atmosphaere)                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements humidity <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-luftfeuchtigkeit-10min>`__ (ch.meteoschweiz.messwerte-luftfeuchtigkeit-10min)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements pressure reduced QNH <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-luftdruck-qnh-10min>`__ (ch.meteoschweiz.messwerte-luftdruck-qnh-10min)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements temperature 2 m, max. 24 h <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-lufttemperatur-24h-max-1h>`__ (ch.meteoschweiz.messwerte-lufttemperatur-24h-max-1h)             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements global radiation, 1 d <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-globalstrahlung-1d>`__ (ch.meteoschweiz.messwerte-globalstrahlung-1d)                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements precipitation, 10 min <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-niederschlag-10min>`__ (ch.meteoschweiz.messwerte-niederschlag-10min)                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements temperature 2 m, min. 24 h <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-lufttemperatur-24h-min-1h>`__ (ch.meteoschweiz.messwerte-lufttemperatur-24h-min-1h)             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements dew point <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-taupunkt-10min>`__ (ch.meteoschweiz.messwerte-taupunkt-10min)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements precipitation, 1 day <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-niederschlag-1d>`__ (ch.meteoschweiz.messwerte-niederschlag-1d)                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements precipitation, 1 h <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-niederschlag-1h>`__ (ch.meteoschweiz.messwerte-niederschlag-1h)                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements temperature 2 m <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-lufttemperatur-10min>`__ (ch.meteoschweiz.messwerte-lufttemperatur-10min)                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements wind gusts <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-10min>`__ (ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-10min)                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Manual precipitation stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-manuell>`__ (ch.meteoschweiz.messnetz-manuell)                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Pollen stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-pollen>`__ (ch.meteoschweiz.messnetz-pollen)                                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate monitoring stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-klima>`__ (ch.meteoschweiz.messnetz-klima)                                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements wind speed <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-windgeschwindigkeit-kmh-10min>`__ (ch.meteoschweiz.messwerte-windgeschwindigkeit-kmh-10min)                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Automatic weather stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-automatisch>`__ (ch.meteoschweiz.messnetz-automatisch)                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geopotential height 850 hPa-surface <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-luftdruck-850hpa-flaeche-10min>`__ (ch.meteoschweiz.messwerte-luftdruck-850hpa-flaeche-10min)       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements sunshine duration, 10 min <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-sonnenscheindauer-10min>`__ (ch.meteoschweiz.messwerte-sonnenscheindauer-10min)                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements relative sunshine, 1 d <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-sonnenscheindauer-relativ-1d>`__ (ch.meteoschweiz.messwerte-sonnenscheindauer-relativ-1d)           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements global radiation, 10 min <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-globalstrahlung-10min>`__ (ch.meteoschweiz.messwerte-globalstrahlung-10min)                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Visual observations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-beobachtungen>`__ (ch.meteoschweiz.messnetz-beobachtungen)                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Weather cams <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-webcams>`__ (ch.meteoschweiz.messnetz-webcams)                                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements snow depth <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-gesamtschnee-1d>`__ (ch.meteoschweiz.messwerte-gesamtschnee-1d)                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Phenological observations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-phaenologie>`__ (ch.meteoschweiz.messnetz-phaenologie)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `MeteoSwiss partner stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-partner>`__ (ch.meteoschweiz.messnetz-partner)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geopotential height 700 hPa-surface <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-luftdruck-700hpa-flaeche-10min>`__ (ch.meteoschweiz.messwerte-luftdruck-700hpa-flaeche-10min)       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Measurements foehn index <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-foehn-10min>`__ (ch.meteoschweiz.messwerte-foehn-10min)                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Zementrohstoffe: Abbau und Verarbeitung <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung>`__ (ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung) |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Gips: Abbau und Verarbeitung <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung>`__ (ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung)                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Salz: Abbau und Verarbeitung <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung>`__ (ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung)                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SWISS MIL PILOTS CHART <//map.geo.admin.ch/?layers=ch.vbs.swissmilpilotschart>`__ (ch.vbs.swissmilpilotschart)                                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Radon map <//map.geo.admin.ch/?layers=ch.bag.radonkarte>`__ (ch.bag.radonkarte)                                                                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Territorial divisions <//map.geo.admin.ch/?layers=ch.vbs.territorialregionen>`__ (ch.vbs.territorialregionen)                                                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:10'000 (color) <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte-farbe-10>`__ (ch.swisstopo.landeskarte-farbe-10)                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:10'000 (grey) <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte-grau-10>`__ (ch.swisstopo.landeskarte-grau-10)                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PDO plant products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-pflanzen>`__ (ch.blw.ursprungsbezeichnungen-pflanzen)                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pollutant releases (SwissPRTR) <//map.geo.admin.ch/?layers=ch.bafu.swissprtr>`__ (ch.bafu.swissprtr)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180502:
   *******

Release 20180502 - Wednesday, Mai 2nd 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180418...r_180502>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180418...r_180502>`__

Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Amtliches Strassenverzeichnis <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-strassenverzeichnis>`__ (ch.swisstopo.amtliches-strassenverzeichnis)                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Enterprises <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Buildings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Dwellings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen)                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Administrative borders G1, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g1>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g1) |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Administrative borders G2, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g2>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g2) |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Population (residents) <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner>`__ (ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner)          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division National Map 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.swiss-map-vector25.metadata>`__ (ch.swisstopo.swiss-map-vector25.metadata)                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Red list bryophytes <//map.geo.admin.ch/?layers=ch.bafu.moose>`__ (ch.bafu.moose)                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20180418:
   *******

Release 20180418 - Wednesday, April 18th 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180328...r_180418>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180328...r_180418>`__

Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Water & migrant bird reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-vogelreservate>`__ (ch.bafu.bundesinventare-vogelreservate)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Regional fens <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-flachmoore_regional>`__ (ch.bafu.bundesinventare-flachmoore_regional)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_rutschungen>`__ (ch.bafu.showme-kantone_rutschungen)                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_hochwasser>`__ (ch.bafu.showme-kantone_hochwasser)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons : avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_lawinen>`__ (ch.bafu.showme-kantone_lawinen)                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: fall processes <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_sturzprozesse>`__ (ch.bafu.showme-gemeinden_sturzprozesse)                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_hochwasser>`__ (ch.bafu.showme-gemeinden_hochwasser)                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: fall processes <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_sturzprozesse>`__ (ch.bafu.showme-kantone_sturzprozesse)                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_rutschungen>`__ (ch.bafu.showme-gemeinden_rutschungen)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_lawinen>`__ (ch.bafu.showme-gemeinden_lawinen)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map swissTLM (color) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-farbe>`__ (ch.swisstopo.swisstlm3d-karte-farbe)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map swissTLM (grey) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-grau>`__ (ch.swisstopo.swisstlm3d-karte-grau)                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:25'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk25.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk25.noscale)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:50'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk50.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk50.noscale)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:100'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk100.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk100.noscale)                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Color Map <//map.geo.admin.ch/?bgLayer=ch.swisstopo.pixelkarte-farbe>`__ (ch.swisstopo.pixelkarte-farbe)                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Grey Map <//map.geo.admin.ch/?bgLayer=ch.swisstopo.pixelkarte-grau>`__ (ch.swisstopo.pixelkarte-grau)                                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20180328:
   *******

Release 20180328 - Wednesday, March 28th 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180312...r_180328>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180312...r_180328>`__

Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sports facilities CSFNI <//map.geo.admin.ch/?layers=ch.baspo.nationales-sportanlagenkonzept>`__ (ch.baspo.nationales-sportanlagenkonzept)                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata>`__ (ch.swisstopo.swissimage-product.metadata)                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=1999&time=1999>`__ (ch.swisstopo.swissimage-product)                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sperr- und Gefahrenzonenkarte <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Gebrochene Gesteine: Abbau <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau>`__ (ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau)  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Naturwerksteine: Abbau <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau>`__ (ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau)              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - TMA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-nahkontrollbezirke>`__ (ch.bazl.luftraeume-nahkontrollbezirke)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - FIZ <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationszonen>`__ (ch.bazl.luftraeume-fluginformationszonen)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Industrial minerals <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-industrieminerale>`__ (ch.swisstopo.geologie-rohstoffe-industrieminerale)                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Fossil fuels <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas>`__ (ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas)                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mineralizations <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-vererzungen>`__ (ch.swisstopo.geologie-rohstoffe-vererzungen)                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20180312:
   *******

Release 20180312 - Monday, March 12th 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180228...r_180312>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- More accurate geometries for the tooltip of the layer Geocover - Vector datasets
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180228...r_180312>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20180228:
   *******

Release 20180228 - Wednesday, February 28th 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- New symbology for the layers ch.bafu.naqua-grundwasser_nitrat and ch.bafu.naqua-grundwasser_voc
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180207...r_180228>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Coordinates with the same number of decimal places in footer and pop-up
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180207...r_180228>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Floodplains AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_auen>`__ (ch.bafu.schutzgebiete-aulav_auen)                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Game reserves AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_jagdbanngebiete>`__ (ch.bafu.schutzgebiete-aulav_jagdbanngebiete)     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mirelandscapes AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_moorlandschaften>`__ (ch.bafu.schutzgebiete-aulav_moorlandschaften)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Other protected areas AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_uebrige>`__ (ch.bafu.schutzgebiete-aulav_uebrige)             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dam <//map.geo.admin.ch/?layers=ch.bfe.stauanlagen-bundesaufsicht>`__ (ch.bfe.stauanlagen-bundesaufsicht)                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `LV95 Transformation accuracy <//map.geo.admin.ch/?layers=ch.swisstopo.transformationsgenauigkeit>`__ (ch.swisstopo.transformationsgenauigkeit)    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20180207:
   *******

Release 20180207 - Wednesday, February 7th 2018
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_180124...r_180207>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Update libraries
-  Add new external WMTS
-  Bug fixes
-  `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_180124...r_180207>`__

Geodata
*******
+--------+---------------------------------------------------------------------------------------------+
| Update | `PCP Inventory <//map.geo.admin.ch/?layers=ch.babs.kulturgueter>`__ (ch.babs.kulturgueter)  |
+--------+---------------------------------------------------------------------------------------------+


.. _releasenotes_20180124:
   *******

Release 20180124 - Wednesday, January 24th 2018
------------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_171220...r_180124>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_171220...r_180124>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Zones) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hillside and steep slopes situation <//map.geo.admin.ch/?layers=ch.blw.hang_steillagen>`__ (ch.blw.hang_steillagen)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Viticulture in steep areas <//map.geo.admin.ch/?layers=ch.blw.steil_terrassenlagen_rebbau>`__ (ch.blw.steil_terrassenlagen_rebbau)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PGI meat products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division SWISSIMAGE 10 cm Raster <//map.geo.admin.ch/?layers=ch.swisstopo.images-swissimage-dop10.metadata>`__ (ch.swisstopo.images-swissimage-dop10.metadata)                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20171220:
   *******

Release 20171220 - Wednesday, December 20th 2017
------------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_171206...r_171220>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_171206...r_171220>`__


Geodata
*******
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Anlagen Gütertransport Schiene <//map.geo.admin.ch/?layers=ch.bav.anlagen-schienengueterverkehr>`__ (ch.bav.anlagen-schienengueterverkehr)   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SP Asylum <//map.geo.admin.ch/?layers=ch.sem.sachplan-asyl_kraft>`__ (ch.sem.sachplan-asyl_kraft)                                            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)       |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                              |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                               |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                               |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                               |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                    |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway network <//map.geo.admin.ch/?layers=ch.bav.schienennetz>`__ (ch.bav.schienennetz)                                                    |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bike sharing and bicycle hire <//map.geo.admin.ch/?layers=ch.bfe.bikesharing>`__ (ch.bfe.bikesharing)                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20171206:
   *******

Release 20171206 - Wednesday, December 6th 2017
------------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_171122...r_171206>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_171122...r_171206>`__


Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Floodplains appendix 2 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-auen_anhang2>`__ (ch.bafu.bundesinventare-auen_anhang2)                                                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amphibians stationary objects <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien>`__ (ch.bafu.bundesinventare-amphibien)                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amphibians appendix 4 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien_anhang4>`__ (ch.bafu.bundesinventare-amphibien_anhang4)                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amphibians shifting sites <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien_wanderobjekte>`__ (ch.bafu.bundesinventare-amphibien_wanderobjekte)                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Floodplains <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-auen>`__ (ch.bafu.bundesinventare-auen)                                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Fens <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-flachmoore>`__ (ch.bafu.bundesinventare-flachmoore)                                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Raised bogs <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-hochmoore>`__ (ch.bafu.bundesinventare-hochmoore)                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mire landscapes <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-moorlandschaften>`__ (ch.bafu.bundesinventare-moorlandschaften)                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dry grasslands (DGS) <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden)                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dry grasslands appendix 2 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2)  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport stops <//map.geo.admin.ch/?layers=ch.bav.haltestellen-oev>`__ (ch.bav.haltestellen-oev)                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20171122:
   *******

Release 20171122 - Wednesday, November 22th 2017
-------------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_171025...r_171121>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_171025...r_171121>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Groundwater bodies <//map.geo.admin.ch/?layers=ch.bafu.grundwasserkoerper>`__ (ch.bafu.grundwasserkoerper)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SP DGR consultation stage 2 <//map.geo.admin.ch/?layers=ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung>`__ (ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung)                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division geological atlas 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_vector.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas_vector.metadata)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_papier.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas_papier.metadata)   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division snowshoe/ski tour maps 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.skitourenkarte-50.metadata>`__ (ch.swisstopo.skitourenkarte-50.metadata)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+





.. _releasenotes_20171025:
   *******

Release 20171025 - Wednesday, October 25th 2017
-------------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_171011...r_171025>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_171011...r_171025>`__

Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wells > 500 m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations local <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal>`__ (ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal)    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet)  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrological gauging stations <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hydromessstationen>`__ (ch.bafu.hydrologie-hydromessstationen)                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Temperature monitoring stations <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-wassertemperaturmessstationen>`__ (ch.bafu.hydrologie-wassertemperaturmessstationen)                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+





.. _releasenotes_20171011:
   *******

Release 20171011 - Wednesday, October 11th 2017
-------------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Removed layer Hydrological network (ch.swisstopo.vec25-gewaessernetz)
-  Removed layer Road network (ch.swisstopo.vec25-strassennetz)
-  Removed layer Railway network (ch.swisstopo.vec25-eisenbahnnetz)
-  Removed layer Other traffic (ch.swisstopo.vec25-uebrigerverkehr)
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170920...r_171011>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  We can now import GPX files in geoadmin
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170920...r_171011>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ludwigia peploides <//map.geo.admin.ch/?layers=ch.bafu.neophyten-portulak_heusenkraut>`__ (ch.bafu.neophyten-portulak_heusenkraut)                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Elodea nuttallii <//map.geo.admin.ch/?layers=ch.bafu.neophyten-nuttalls_wasserpest>`__ (ch.bafu.neophyten-nuttalls_wasserpest)                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Robinia pseudoacacia  <//map.geo.admin.ch/?layers=ch.bafu.neophyten-robinie>`__ (ch.bafu.neophyten-robinie)                                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Viburnum rhytidophyllum <//map.geo.admin.ch/?layers=ch.bafu.neophyten-runzelblaettriger_schneeball>`__ (ch.bafu.neophyten-runzelblaettriger_schneeball)                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sedum stoloniferum <//map.geo.admin.ch/?layers=ch.bafu.neophyten-auslaeuferbildendes_fettkraut>`__ (ch.bafu.neophyten-auslaeuferbildendes_fettkraut)                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Prunus laurocerasus <//map.geo.admin.ch/?layers=ch.bafu.neophyten-kirschlorbeer>`__ (ch.bafu.neophyten-kirschlorbeer)                                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Toxicodendron radicans <//map.geo.admin.ch/?layers=ch.bafu.neophyten-kletternder_giftsumach>`__ (ch.bafu.neophyten-kletternder_giftsumach)                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Pueraria lobata <//map.geo.admin.ch/?layers=ch.bafu.neophyten-kopoubohne>`__ (ch.bafu.neophyten-kopoubohne)                                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mahonie <//map.geo.admin.ch/?layers=ch.bafu.neophyten-mahonie>`__ (ch.bafu.neophyten-mahonie)                                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Crassule de Helms <//map.geo.admin.ch/?layers=ch.bafu.neophyten-nadelkraut>`__ (ch.bafu.neophyten-nadelkraut)                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hydography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170920:
   *******

Release 20170920 - Wednesday, September 20th 2017
-------------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
-  Removed layer 2015 railway noise emissions plan, night (ch.bav.laerm-emissionsplan_eisenbahn_nacht)
-  Removed layer 2015 railway noise emissions plan, day (ch.bav.laerm-emissionsplan_eisenbahn_tag)
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170830...r_170920>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170830...r_170920>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170830:
   *******

Release 20170830 - Wednesday, August 30th 2017
----------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170816...r_170830>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170816...r_170830>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Eisenbahnlärm, festgel. Emission N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht)    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Eisenbahnlärm, festgel. Emission T <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag)        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Eisenbahnlärm, tats. Emission N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht)   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Eisenbahnlärm, tats. Emission T <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag)       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Water & migrant bird reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-vogelreservate>`__ (ch.bafu.bundesinventare-vogelreservate)                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of forest damage – projectile <//map.geo.admin.ch/?layers=ch.vbs.waldschadenkarte>`__ (ch.vbs.waldschadenkarte)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170816:
   *******

Release 20170816 - Wednesday, August 16th 2017
----------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170726...r_170816>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170726...r_170816>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ammonia Concentration <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-ammoniakkonzentration>`__ (ch.bafu.luftreinhaltung-ammoniakkonzentration)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Nitrogen Deposition <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-stickstoffdeposition>`__ (ch.bafu.luftreinhaltung-stickstoffdeposition)                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `CLN Exceedance <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-stickstoff_kritischer_eintrag>`__ (ch.bafu.luftreinhaltung-stickstoff_kritischer_eintrag)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20170726:
   *******

Release 20170726 - Wednesday, July 26th 2017
---------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170719...r_170726>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170719...r_170726>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ARA - cleaning type <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp>`__ (ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected Areas VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-adminboundaries-protectedarea>`__ (ch.swisstopo.vec200-adminboundaries-protectedarea)                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forested areas <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover-wald>`__ (ch.swisstopo.vec200-landcover-wald)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects  VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transportation VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 .. _releasenotes_20170719:
    *******

Release 20170719 - Wednesday, July 19th 2017
---------------------------------------------

API & applications
******************


`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Removed OWSChecker
-  Removed address geometry protection
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170705...r_170719>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170705...r_170719>`__


Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `AGNES <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-agnes>`__ (ch.swisstopo.fixpunkte-agnes)                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170705:
   *******

Release 20170705 - Wednesday, July 05th 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170627...r_170705>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170627...r_170705>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Anthrop. seismic noise CH <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bodenunruhe>`__ (ch.swisstopo.geologie-bodenunruhe)             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170627:
   *******

Release 20170627 - Tuesday, June 27th 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170613...r_170627>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170613...r_170627>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Groundwater level/spring discharge <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_grundwasserzustand>`__ (ch.bafu.hydroweb-messstationen_grundwasserzustand)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SAIP in consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Release 20170613 - Tuesday, June 13th 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170531...r_170613>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170531...r_170613>`__

Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Alps with guard dogs <//map.geo.admin.ch/?layers=ch.bafu.alpweiden-herdenschutzhunde>`__ (ch.bafu.alpweiden-herdenschutzhunde)                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Notifications for maps and geodata <//map.geo.admin.ch/?layers=ch.swisstopo.meldungen-karten_geodaten>`__ (ch.swisstopo.meldungen-karten_geodaten)                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Diatoms <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen)                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Fish <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_fische>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_fische)                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Macrophytes <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten)                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Macrozoobenthos <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos)    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ammonium <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_ammonium>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_ammonium)                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dissolved Organic Carbon (DOC) <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_doc>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_doc)                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nitrate <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_nitrat>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_nitrat)                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nitrite <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_nitrit>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_nitrit)                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Phosphate <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_phosphat>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_phosphat)                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Total Phosphorus <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt)       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ILNM <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-bln>`__ (ch.bafu.bundesinventare-bln)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:10'000 (color) <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte-farbe-10>`__ (ch.swisstopo.landeskarte-farbe-10)                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:10'000 (grey) <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte-grau-10>`__ (ch.swisstopo.landeskarte-grau-10)                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung&topic=sachplan>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Sectoral Plan Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft&topic=sachplan>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170531:
   *******

Release 20170531 - Wednesday, May 31st 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170426...r_170531>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Add WMTS import
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170426...r_170531>`__

Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------+
| Update | `Pollutant releases (SwissPRTR) <//map.geo.admin.ch/?layers=ch.bafu.swissprtr>`__ (ch.bafu.swissprtr)  |
+--------+--------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170426:
   *******

Release 20170426 - Wednesday, April 26th 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170412...r_170426>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
-  Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170412...r_170426>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reynoutria sachalinensis <//map.geo.admin.ch/?layers=ch.bafu.neophyten-sachalin_staudenknoeterich>`__ (ch.bafu.neophyten-sachalin_staudenknoeterich)    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Buddleja davidii <//map.geo.admin.ch/?layers=ch.bafu.neophyten-schmetterlingsstrauch>`__ (ch.bafu.neophyten-schmetterlingsstrauch)                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Cornus sericea <//map.geo.admin.ch/?layers=ch.bafu.neophyten-seidiger_hornstrauch>`__ (ch.bafu.neophyten-seidiger_hornstrauch)                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solidago gigantea <//map.geo.admin.ch/?layers=ch.bafu.neophyten-spaetbluehende_goldrute>`__ (ch.bafu.neophyten-spaetbluehende_goldrute)                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Senecio inaequidens <//map.geo.admin.ch/?layers=ch.bafu.neophyten-suedafrikanisches_greiskraut>`__ (ch.bafu.neophyten-suedafrikanisches_greiskraut)     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Asclepias syriaca <//map.geo.admin.ch/?layers=ch.bafu.neophyten-syrische_seidenpflanze>`__ (ch.bafu.neophyten-syrische_seidenpflanze)                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Helianthus tuberosus <//map.geo.admin.ch/?layers=ch.bafu.neophyten-topinambur>`__ (ch.bafu.neophyten-topinambur)                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Artemisia verlotiorum <//map.geo.admin.ch/?layers=ch.bafu.neophyten-verlotscher_beifuss>`__ (ch.bafu.neophyten-verlotscher_beifuss)                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Polygonum polystachyum <//map.geo.admin.ch/?layers=ch.bafu.neophyten-vielaehriger_knoeterich>`__ (ch.bafu.neophyten-vielaehriger_knoeterich)            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Lupinus polyphyllus <//map.geo.admin.ch/?layers=ch.bafu.neophyten-vielblaettrige_lupine>`__ (ch.bafu.neophyten-vielblaettrige_lupine)                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest Reserves <//map.geo.admin.ch/?layers=ch.bafu.waldreservate>`__ (ch.bafu.waldreservate)                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `UNESCO World cultural heritage <//map.geo.admin.ch/?layers=ch.bak.schutzgebiete-unesco_weltkulturerbe>`__ (ch.bak.schutzgebiete-unesco_weltkulturerbe)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Forest Preserves <//map.geo.admin.ch/?layers=ch.pronatura.waldreservate>`__ (ch.pronatura.waldreservate)                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170412:
   *******

Release 20170412 - Wednesday, April 12th 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170329...r_170412>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- New, consolidated import tool
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170329...r_170412>`__

Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_hochwasser>`__ (ch.bafu.showme-gemeinden_hochwasser)                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_hochwasser>`__ (ch.bafu.showme-gemeinden_hochwasser)                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_lawinen>`__ (ch.bafu.showme-gemeinden_lawinen)                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_rutschungen>`__ (ch.bafu.showme-gemeinden_rutschungen)          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: fall processes <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_sturzprozesse>`__ (ch.bafu.showme-gemeinden_sturzprozesse)  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_hochwasser>`__ (ch.bafu.showme-kantone_hochwasser)                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons : avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_lawinen>`__ (ch.bafu.showme-kantone_lawinen)                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_rutschungen>`__ (ch.bafu.showme-kantone_rutschungen)               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: fall processes <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_sturzprozesse>`__ (ch.bafu.showme-kantone_sturzprozesse)       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20170329:
   *******

Release 20170329 - Wednesday, March 29nd 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170322...r_170329>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170322...r_170329>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Airspaces: Control areas - CTA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollbezirke>`__ (ch.bazl.luftraeume-kontrollbezirke)                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Airspaces: Control zones - CTR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollzonen>`__ (ch.bazl.luftraeume-kontrollzonen)                                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Airspaces: Flight information region - FIR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationsgebiet>`__ (ch.bazl.luftraeume-fluginformationsgebiet)                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Airspaces: Flight information zones - FIZ <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationszonen>`__ (ch.bazl.luftraeume-fluginformationszonen)                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Airspaces: Terminal control areas - TMA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-nahkontrollbezirke>`__ (ch.bazl.luftraeume-nahkontrollbezirke)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Housing Inventory <//map.geo.admin.ch/?layers=ch.are.wohnungsinventar-zweitwohnungsanteil>`__ (ch.are.wohnungsinventar-zweitwohnungsanteil)                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected areas MIL <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-luftfahrt>`__ (ch.bafu.schutzgebiete-luftfahrt)                                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart Switzerland 1:300'000 <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO Switzerland 1:500'000 <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _releasenotes_20170322:
   *******

Release 20170322 - Wednesday, March 22nd 2017
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170313...r_170322>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170313...r_170322>`__

Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Microwave links <//map.geo.admin.ch/?layers=ch.bakom.richtfunkverbindungen>`__ (ch.bakom.richtfunkverbindungen)                                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: cluster <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: recommendation of vaccination <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-impfung>`__ (ch.bag.zecken-fsme-impfung)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Release 20170313 - Monday, March 13th 2017
------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170301...r_170313>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170201...r_170313>`__

Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 1st night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde)                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 2nd night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde)                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lmax <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel)     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lr <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter)                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. last night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light / large aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge)    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. milit. aerodr. (tot.) <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents in the annual comparison <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_jahresvergleich>`__ (ch.astra.schwerverunfallte-kanton_jahresvergleich)                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20170301:
   *******

Release 20170301 - Wednesday, March 1st 2017
------------------------------------------------

Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Deep geothermal projects <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tiefengeothermie_projekte>`__ (ch.swisstopo.geologie-tiefengeothermie_projekte)                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Filling stations BEBECO <//map.geo.admin.ch/?layers=ch.vbs.bundestankstellen-bebeco>`__ (ch.vbs.bundestankstellen-bebeco)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20170222:
   *******

Release 20170222 - Wednesday, February 22nd 2017
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170201...r_170222>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170201...r_170222>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PCP Inventory <//map.geo.admin.ch/?layers=ch.babs.kulturgueter&topic=kgs>`__ (ch.babs.kulturgueter)                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20170201:
   *******

Release 20170201 - Wednesday, February 1st 2017
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_170125...r_170201>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_170125...r_170201>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20170125:
   *******

Release 20170125 - Wednesday, January 25th 2017
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- `3D Tiles initial doc </services/sdiservices.html#d-tiles>`__
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_161214...r_170125>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Addition of a partial `3D buildings model <//map.geo.admin.ch?topic=ech&lang=fr&bgLayer=ch.swisstopo.pixelkarte-farbe&layers=ch.swisstopo.swissbuildings3d_2.metadata&layers_opacity=0.75&lon=7.78711&lat=46.92932&elevation=1535&heading=0.001&pitch=-40.032&layers_visibility=false>`__.
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_161214...r_170125>`__


Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mobility Carsharing <//map.geo.admin.ch/?layers=ch.mobility.standorte>`__ (ch.mobility.standorte)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet)  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations local <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal>`__ (ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal)    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Zones) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `LV95 Transformation accuracy <//map.geo.admin.ch/?layers=ch.swisstopo.transformationsgenauigkeit>`__ (ch.swisstopo.transformationsgenauigkeit)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20161214:
   *******

Release 20161214 - Wednesday, December 14th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Add ignore_polyfill parameter to the loader.js, see `doc <http://api3.geo.admin.ch/api/quickstart.html#include-the-geoadmin-javascript-api>`__.
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_161130...r_161214>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- Ability to order `digital products from map.geo.admin.ch <https://map.geo.admin.ch?topic=ech&lang=fr&bgLayer=ch.swisstopo.pixelkarte-farbe&layers=ch.swisstopo.pixelkarte-pk25.metadata&X=192510.47&Y=682227.64&zoom=2>`__
- New topic `emapis <https://map.geo.admin.ch?topic=emapis>`__
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_161130...r_161214>`__

Geodata
*******
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Karst water resources <//map.geo.admin.ch/?layers=ch.bafu.karst-ausdehnung_grundwasservorkommen>`__ (ch.bafu.karst-ausdehnung_grundwasservorkommen)                                                |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Karst catchments <//map.geo.admin.ch/?layers=ch.bafu.karst-einzugsgebiete>`__ (ch.bafu.karst-einzugsgebiete)                                                                                       |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Karst catchment units <//map.geo.admin.ch/?layers=ch.bafu.karst-einzugsgebietseinheiten>`__ (ch.bafu.karst-einzugsgebietseinheiten)                                                                |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Karst springs and swallow holes <//map.geo.admin.ch/?layers=ch.bafu.karst-quellen_schwinden>`__ (ch.bafu.karst-quellen_schwinden)                                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Underground flow paths <//map.geo.admin.ch/?layers=ch.bafu.karst-unterirdische_fliesswege>`__ (ch.bafu.karst-unterirdische_fliesswege)                                                             |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Beizugsgebiet <//map.geo.admin.ch/?layers=ch.blw.emapis-beizugsgebiet&topic=emapis>`__ (ch.blw.emapis-beizugsgebiet)                                                                               |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Bewässerung <//map.geo.admin.ch/?layers=ch.blw.emapis-bewaesserung&topic=emapis>`__ (ch.blw.emapis-bewaesserung EMPTY LAYER)                                                                       |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Elektrizitätsversorgung <//map.geo.admin.ch/?layers=ch.blw.emapis-elektrizitaetsversorgung&topic=emapis>`__ (ch.blw.emapis-elektrizitaetsversorgung EMPTY LAYER)                                   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Water balance, soil structure <//map.geo.admin.ch/?layers=ch.blw.emapis-entwaesserung&topic=emapis>`__ (ch.blw.emapis-entwaesserung)                                                               |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hochbau <//map.geo.admin.ch/?layers=ch.blw.emapis-hochbau&topic=emapis>`__ (ch.blw.emapis-hochbau)                                                                                                 |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Milchleitung <//map.geo.admin.ch/?layers=ch.blw.emapis-milchleitung&topic=emapis>`__ (ch.blw.emapis-milchleitung EMPTY LAYER)                                                                      |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Oekologie <//map.geo.admin.ch/?layers=ch.blw.emapis-oekologie&topic=emapis>`__ (ch.blw.emapis-oekologie)                                                                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Projektschwerpunkt <//map.geo.admin.ch/?layers=ch.blw.emapis-projektschwerpunkt&topic=emapis>`__ (ch.blw.emapis-projektschwerpunkt)                                                                |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Agricultural and alpine cableways <//map.geo.admin.ch/?layers=ch.blw.emapis-seilbahnen&topic=emapis>`__ (ch.blw.emapis-seilbahnen EMPTY LAYER)                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wasserversorgung <//map.geo.admin.ch/?layers=ch.blw.emapis-wasserversorgung&topic=emapis>`__ (ch.blw.emapis-wasserversorgung)                                                                      |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Road construction <//map.geo.admin.ch/?layers=ch.blw.emapis-wegebau&topic=emapis>`__ (ch.blw.emapis-wegebau)                                                                                       |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division DHM25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.digitales-hoehenmodell_25.metadata>`__ (ch.swisstopo.digitales-hoehenmodell_25.metadata)                                            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division general geological map 200 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-generalkarte-ggk200.metadata>`__ (ch.swisstopo.geologie-generalkarte-ggk200.metadata)                 |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                          |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division special geological maps Vector <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata>`__ (ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata)  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Aeronautical Chart ICAO Raster <//map.geo.admin.ch/?layers=ch.swisstopo.luftfahrtkarten-icao.metadata>`__ (ch.swisstopo.luftfahrtkarten-icao.metadata)                                    |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Glider Chart Raster <//map.geo.admin.ch/?layers=ch.swisstopo.segelflugkarte.metadata>`__ (ch.swisstopo.segelflugkarte.metadata)                                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division swissALTI3D Raster <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d.metadata>`__ (ch.swisstopo.swissalti3d.metadata)                                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division swissBUILDINGS3D 1.0 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.swissbuildings3d_1.metadata>`__ (ch.swisstopo.swissbuildings3d_1.metadata)                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division swissTLM3D Vector <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d.metadata>`__ (ch.swisstopo.swisstlm3d.metadata)                                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division special geological maps Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-spezialkarten_schweiz.metadata>`__ (ch.swisstopo.geologie-spezialkarten_schweiz.metadata)                |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division snowshoe/ski tour maps 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.skitourenkarte-50.metadata>`__ (ch.swisstopo.skitourenkarte-50.metadata)                                         |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 100 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-pk100.metadata>`__ (ch.swisstopo.pixelkarte-pk100.metadata)                                                   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 200 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-pk200.metadata>`__ (ch.swisstopo.pixelkarte-pk200.metadata)                                                   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-pk25.metadata>`__ (ch.swisstopo.pixelkarte-pk25.metadata)                                                      |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 50 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-pk50.metadata>`__ (ch.swisstopo.pixelkarte-pk50.metadata)                                                      |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division SWISSIMAGE Raster <//map.geo.admin.ch/?layers=ch.swisstopo.images-swissimage.metadata>`__ (ch.swisstopo.images-swissimage.metadata)                                                       |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division Spot Mosaic Raster <//map.geo.admin.ch/?layers=ch.swisstopo.images-spot-5.metadata>`__ (ch.swisstopo.images-spot-5.metadata)                                                              |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spectral micro-zoning <//map.geo.admin.ch/?layers=ch.bafu.gefahren-spektral>`__ (ch.bafu.gefahren-spektral)                                                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                                             |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                                                    |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                              |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                                                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                                                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                              |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                                                                              |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                                                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                                                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                                                                          |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                                                                              |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport stops <//map.geo.admin.ch/?layers=ch.bav.haltestellen-oev>`__ (ch.bav.haltestellen-oev)                                                                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway network | Rait da viafier <//map.geo.admin.ch/?layers=ch.bav.schienennetz>`__ (ch.bav.schienennetz)                                                                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division special geological maps Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-spezialkarten_schweiz.metadata>`__ (ch.swisstopo.geologie-spezialkarten_schweiz.metadata)                |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division swissBUILDINGS3D 2.0 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.swissbuildings3d_2.metadata>`__ (ch.swisstopo.swissbuildings3d_2.metadata)                                           |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20161130:
   *******

Release 20161130 - Wednesday, November 30th 2016
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_161116...r_161130>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_161116...r_161130>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------+
| New    | `OpenData-Surveying <//map.geo.admin.ch/?layers=ch.swisstopo-vd.amtliche-vermessung>`__ (ch.swisstopo-vd.amtliche-vermessung)  |
+--------+--------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nuclear Power Plants <//map.geo.admin.ch/?layers=ch.bfe.kernkraftwerke>`__ (ch.bfe.kernkraftwerke)                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)   |
+--------+--------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20161116:
   *******

Release 20161116 - Wednesday, November 16th 2016
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_161026...r_161116>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_161026...r_161116>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Bike sharing and bicycle hire <//map.geo.admin.ch/?layers=ch.bfe.bikesharing>`__ (ch.bfe.bikesharing)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher&topic=energie>`__ (ch.bfe.solarenergie-eignung-daecher) |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy cities <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte>`__ (ch.bfe.energiestaedte)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy Cities on the Path 2000-Watt <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-aufdemweg>`__ (ch.bfe.energiestaedte-2000watt-aufdemweg)    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy-Regions <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-energieregionen>`__ (ch.bfe.energiestaedte-energieregionen)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20161026:

Release 20161026 - Wednesday, October 26th 2016
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_161019...r_161026>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_161019...r_161026>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mountain landing sites <//map.geo.admin.ch/?layers=ch.bazl.gebirgslandeplaetze>`__ (ch.bazl.gebirgslandeplaetze)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Siegfried Map 50 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-siegfried-ta50.metadata>`__ (ch.swisstopo.hiks-siegfried-ta50.metadata)            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Siegfried Map 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-siegfried-ta25.metadata>`__ (ch.swisstopo.hiks-siegfried-ta25.metadata)            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Dufour Map Raster <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-dufour.metadata>`__ (ch.swisstopo.hiks-dufour.metadata)                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Tracer tests <//map.geo.admin.ch/?layers=ch.bafu.hydrogeologie-markierversuche>`__ (ch.bafu.hydrogeologie-markierversuche)                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Spitallandeplätze <//map.geo.admin.ch?layers=ch.bazl.spitallandeplaetze>`__ (ch.bazl.spitallandeplaetze)                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Swiss Map Vector 1000 <//map.geo.admin.ch?layers=ch.swisstopo.swiss-map-vector1000.metadata>`__ (ch.swisstopo.swiss-map-vector1000.metadata)             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Swiss Map Vector 500 <//map.geo.admin.ch?layers=ch.swisstopo.swiss-map-vector500.metadata>`__ (ch.swisstopo.swiss-map-vector500.metadata)                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SPM consultation <//map.geo.admin.ch?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung&topic=sachplan>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)|
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Icing frequency <//map.geo.admin.ch?layers=ch.bfe.meteorologische-vereisung>`__ (ch.bfe.meteorologische-vereisung)                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Sectoral Plan Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft&topic=sachplan>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft) |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Inventory historical routes terrain map <//map.geo.admin.ch/?layers=ch.astra.ivs-gelaendekarte>`__ (ch.astra.ivs-gelaendekarte)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20161019:

Release 20161019 - Wednesday, October 19th 2016
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_161005...r_161019>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_161005...r_161019>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `IHR Boundaries <//map.geo.admin.ch/?layers=ch.astra.ivs-nat_abgrenzungen>`__ (ch.astra.ivs-nat_abgrenzungen)                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `IHR Elements of landscape <//map.geo.admin.ch/?layers=ch.astra.ivs-nat_wegbegleiter>`__ (ch.astra.ivs-nat_wegbegleiter)                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `IHR regional & local <//map.geo.admin.ch/?layers=ch.astra.ivs-reg_loc>`__ (ch.astra.ivs-reg_loc)                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Federal Inventory ISOS <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder)  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20161005:

Release 20161005 - Wednesday, October 5st 2016
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160921...r_161005>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160921...r_161005>`__


Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Axis of national routes <//map.geo.admin.ch/?layers=ch.astra.nationalstrassenachsen>`__ (ch.astra.nationalstrassenachsen)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160921:

Release 20160921 - Wednesday, September 21st 2016
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160831...r_160921>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160831...r_160921>`__


Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images privates <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-firmen>`__ (ch.swisstopo.lubis-luftbilder-dritte-firmen)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SÜL Anhörung <//map.geo.admin.ch/?topic=sachplan&layers=ch.bfe.sachplan-uebertragungsleitungen_anhoerung>`__ (ch.bfe.sachplan-uebertragungsleitungen_anhoerung)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Electricity lines sectoral plan <//map.geo.admin.ch/?topic=sachplan&layers=ch.bfe.sachplan-uebertragungsleitungen_kraft>`__ (ch.bfe.sachplan-uebertragungsleitungen_kraft)                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vertical Deflections <//map.geo.admin.ch/?layers=ch.swisstopo.lotabweichungen>`__ (ch.swisstopo.lotabweichungen)                                                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20160831:

Release 20160831 - Wednesday, August 31st 2016
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160817...r_160831>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- New design of draw tools
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160817...r_160831>`__


Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Basiskarte GIN <//map.geo.admin.ch/?layers=ch.bafu.gefahren-basiskarte>`__ (ch.bafu.gefahren-basiskarte)                                                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sectoral Plan Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vertical Deflections <//map.geo.admin.ch/?layers=ch.swisstopo.lotabweichungen>`__ (ch.swisstopo.lotabweichungen)                                                                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public Transportation VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr)                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forested areas <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover-wald>`__ (ch.swisstopo.vec200-landcover-wald)                                                                                                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SAIP in consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                                                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20160817:

Release 20160817 - Wednesday, August 17th 2016
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160803...r_160817>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160803...r_160817>`__


Geodata
*******

No updates


.. _releasenotes_20160803:

Release 20160803 - Wednesday, August 3rd 2016
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160713...r_160803>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160713...r_160803>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Waldschadenkarten Projektil <//map.geo.admin.ch/?layers=ch.vbs.waldschadenkarte>`__ (ch.vbs.waldschadenkarte)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas of Switzerland 1:25000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrological gauging stations <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hydromessstationen>`__ (ch.bafu.hydrologie-hydromessstationen)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cant. routes for exceptional loads <//map.geo.admin.ch/?layers=ch.astra.ausnahmetransportrouten>`__ (ch.astra.ausnahmetransportrouten)                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Broadband maps <//map.geo.admin.ch/?topic=nga>`__ (Broadband Maps)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160713:

Release 20160713 - Wednesday, July 13th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- WMTS GetCapabilities old timestamps of ch.swisstopo.pixelkarte-farbe and ch.swisstopo.pixelkarte-grau have been removed
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160629...r_160713>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160629...r_160713>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Diatoms <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen)                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Fish <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_fische>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_fische)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Macrophytes <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Macrozoobenthos <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ammonium <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_ammonium>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_ammonium)                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Dissolved Organic Carbon (DOC) <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_doc>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_doc)               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Nitrate <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_nitrat>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_nitrat)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Nitrite <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_nitrit>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_nitrit)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Phosphate <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_phosphat>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_phosphat)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Total Phosphorus <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt)     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Waldschadenkarte - Projektil <//map.geo.admin.ch/?layers=ch.vbs.waldschadenkarte>`__ (ch.vbs.waldschadenkarte)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Diffuse phosphorus inputs <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor>`__ (ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor)            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Diffuse nitrogen inputs <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff>`__ (ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff)          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160629:

Release 20160629 - Wednesday, June 29th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160615...r_160629>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160615...r_160629>`__


Geodata
*******
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                      |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                         |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar Energy - Suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                          |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spectral micro-zoning <//map.geo.admin.ch/?layers=ch.bafu.gefahren-spektral>`__ (ch.bafu.gefahren-spektral)                                                          |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160615:

Release 20160615 - Wednesday, June 15th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160601...r_160615>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160601...r_160615>`__


Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Badegewässerqualität <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160601:

Release 20160601 - Wednesday, June 1st 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160525...r_160601>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160525...r_160601>`__


Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `National Map 1:10'000 (color) <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte-farbe-10>`__ (ch.swisstopo.landeskarte-farbe-10)                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `National Map 1:10'000 (grey) <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte-grau-10>`__ (ch.swisstopo.landeskarte-grau-10)                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Availability swissBUILDINGS3D 2.0 <//map.geo.admin.ch/?layers=ch.swisstopo.swissbuildings3d_2.metadata>`__ (ch.swisstopo.swissbuildings3d_2.metadata)                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `DHM25 Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung>`__ (ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung) |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160525:

Release 20160525 - Wednesday, May 25th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160511...r_160525>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160511...r_160525>`__


Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hydrogeological map 100 <//map.geo.admin.ch/?layers=ch.bafu.hydrogeologische-karte_100>`__ (ch.bafu.hydrogeologische-karte_100)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Filling stations BEBECO <//map.geo.admin.ch/?layers=ch.vbs.bundestankstellen-bebeco>`__ (ch.vbs.bundestankstellen-bebeco)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Federal Inventory ISOS <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder) |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Simplified 3D buildings <//map.geo.admin.ch/?layers=ch.swisstopo.swissbuildings3d>`__ (ch.swisstopo.swissbuildings3d)                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:25'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk25.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk25.noscale)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:50'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk50.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk50.noscale)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:100'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk100.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk100.noscale)           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk200.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk200.noscale)           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product>`__ (ch.swisstopo.swissimage-product)                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map swissTLM (color) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-farbe>`__ (ch.swisstopo.swisstlm3d-karte-farbe)                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160511:

Release 20160511 - Wednesday, May 11th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160427...r_160511>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160427...r_160511>`__


Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wind speed 50 metres above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h50>`__ (ch.bfe.windenergie-geschwindigkeit_h50)                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wind speed 75 metres above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h75>`__ (ch.bfe.windenergie-geschwindigkeit_h75)                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wind speed 100 metres above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h100>`__ (ch.bfe.windenergie-geschwindigkeit_h100)                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wind speed 125 metres above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h125>`__ (ch.bfe.windenergie-geschwindigkeit_h125)                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wind speed 150 metres above ground <//map.geo.admin.ch/?layers=ch.bfe.windenergie-geschwindigkeit_h150>`__ (ch.bfe.windenergie-geschwindigkeit_h150)                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Gravimetric Atlas 100 - paper <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata>`__ (ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata) |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SÜL Anhörung <//map.geo.admin.ch/?layers=ch.bfe.sachplan-uebertragungsleitungen_anhoerung>`__ (ch.bfe.sachplan-uebertragungsleitungen_anhoerung)                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Übertragungsleitungen <//map.geo.admin.ch/?layers=ch.bfe.sachplan-uebertragungsleitungen_kraft>`__ (ch.bfe.sachplan-uebertragungsleitungen_kraft)                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20160427:

Release 20160427 - Wednesday, April 27th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160413...r_160427>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160413...r_160427>`__


Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. Dokumente (1000-21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2)  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. Dokumente (100-1000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2)        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. Dokumente (10-100km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10to100km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10to100km2)              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. documents (10x10km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10x10km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10x10km)                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. documents (1x1km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-1x1km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-1x1km)                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. documents (>21,000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2)             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. documents (<10km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-lt10km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-lt10km2)                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. documents (lines) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-linien>`__ (ch.swisstopo.geologie-gisgeol-linien)                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geol. documents (points) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-punkte>`__ (ch.swisstopo.geologie-gisgeol-punkte)                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart Switzerland 1:300'000 <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO Switzerland 1:500'000 <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:500'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk500.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk500.noscale)                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `General Geological Map of Switzerland 1:200,000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-generalkarte-ggk200>`__ (ch.swisstopo.geologie-generalkarte-ggk200)          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division of Geological Vector Datasets 1:25,000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas of Switzerland 1:25000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_hochwasser>`__ (ch.bafu.showme-gemeinden_hochwasser)                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_lawinen>`__ (ch.bafu.showme-gemeinden_lawinen)                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_rutschungen>`__ (ch.bafu.showme-gemeinden_rutschungen)                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: rockfall <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_sturzprozesse>`__ (ch.bafu.showme-gemeinden_sturzprozesse)                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_hochwasser>`__ (ch.bafu.showme-kantone_hochwasser)                                                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_lawinen>`__ (ch.bafu.showme-kantone_lawinen)                                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_rutschungen>`__ (ch.bafu.showme-kantone_rutschungen)                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: rockfall <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_sturzprozesse>`__ (ch.bafu.showme-kantone_sturzprozesse)                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Parks <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway network <//map.geo.admin.ch/?layers=ch.bav.schienennetz>`__ (ch.bav.schienennetz)                                                                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20160413:

Release 20160413 - Wednesday, April 13th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `New cache control service for WMTS tiles invalidation <../../../services/sdiservices.html#cache-update>`__
- `SearchServer <../../../services/sdiservices.html#search>`__ : sn25 origin has been replaced with gazetteer. Using sn25 as origin parameter will result in a 400 Bad Request error.
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160330...r_160413>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160330...r_160413>`__


Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------+
| New    | `Coordinate grid CH1903+/LV95 <//map.geo.admin.ch/?layers=org.epsg.grid_2056>`__ (org.epsg.grid_2056)      |
+--------+------------------------------------------------------------------------------------------------------------+
| New    | `Coordinate grid CH1903/LV03 <//map.geo.admin.ch/?layers=org.epsg.grid_21781>`__ (org.epsg.grid_21781)     |
+--------+------------------------------------------------------------------------------------------------------------+
| New    | `Coordinate grid WGS84 <//map.geo.admin.ch/?layers=org.epsg.grid_4326>`__ (org.epsg.grid_4326)             |
+--------+------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20160330:

Release 20160330 - Wednesday, March 30th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160316...r_160330>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160316...r_160330>`__


Geodata
*******
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division of the General Geological Map 1:200000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-generalkarte-ggk200_papier.metadata>`__ (ch.swisstopo.geologie-generalkarte-ggk200_papier.metadata)     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division of Special Geological Maps - paper <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-spezialkarten_schweiz_papier.metadata>`__ (ch.swisstopo.geologie-spezialkarten_schweiz_papier.metadata)     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Last Glacial Maximum (LGM) 1:500000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-eiszeit-lgm-raster_papier.metadata>`__ (ch.swisstopo.geologie-eiszeit-lgm-raster_papier.metadata)          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division of the Geol. Atlas of Switzerland 1:25000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_papier.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas_papier.metadata)    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Div. of Hydrogeol. Map: Groundwater Res. 1:500000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-grundwasservorkommen_papier.metadata>`__ (ch.swisstopo.geologie-grundwasservorkommen_papier.metadata) |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Div grundwater vulnerability 500 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-grundwasservulnerabilitaet_papier.metadata>`__ (ch.swisstopo.geologie-grundwasservulnerabilitaet_papier.metadata)|
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division aeronautical chart ICAO Paper <//map.geo.admin.ch/?layers=ch.swisstopo.luftfahrtkarten-icao_papier.metadata>`__ (ch.swisstopo.luftfahrtkarten-icao_papier.metadata)                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Div. of Grav. Map (Bouguer) 1:500000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geodaesie-bouguer_anomalien_papier.metadata>`__ (ch.swisstopo.geologie-geodaesie-bouguer_anomalien_papier.metadata)|
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division of Tectonic Map 1:500000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tektonische_karte_papier.metadata>`__ (ch.swisstopo.geologie-tektonische_karte_papier.metadata)                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division of Geological Map 1:500000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologische_karte_papier.metadata>`__ (ch.swisstopo.geologie-geologische_karte_papier.metadata)                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Printed Map: Road Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.strassenkarte200_papier.metadata>`__ (ch.swisstopo.strassenkarte200_papier.metadata)                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paper Map: Castles map of Switzerland 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.burgenkarte200_papier.metadata>`__ (ch.swisstopo.burgenkarte200_papier.metadata)                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paper map: Hiking Maps 1:33'333 <//map.geo.admin.ch/?layers=ch.swisstopo.wanderkarte33_papier.metadata>`__ (ch.swisstopo.wanderkarte33_papier.metadata)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division national map 50 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte50_papier.metadata>`__ (ch.swisstopo.landeskarte50_papier.metadata)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division national map 100 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte100_papier.metadata>`__ (ch.swisstopo.landeskarte100_papier.metadata)                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paper map: General Map 1:300'000 <//map.geo.admin.ch/?layers=ch.swisstopo.generalkarte300_papier.metadata>`__ (ch.swisstopo.gk300-papierkarte.metadata)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division hiking map 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.wanderkarte50_papier.metadata>`__ (ch.swisstopo.wanderkarte50_papier.metadata)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paper map: Composites Hiking Maps 1:25'000 <//map.geo.admin.ch/?layers=ch.swisstopo.wanderkarte25-zus_papier.metadata>`__ (ch.swisstopo.wanderkarte25-zus_papier.metadata)                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paper Map: Glider Chart Switzerland 1:300'000 <//map.geo.admin.ch/?layers=ch.swisstopo.segelflugkarte_papier.metadata>`__ (ch.swisstopo.segelflugkarte_papier.metadata)                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paper map: National Map 1:500'000 <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte500_papier.metadata>`__ (ch.swisstopo.landeskarte500_papier.metadata)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division national map 25 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte25_papier.metadata>`__ (ch.swisstopo.landeskarte25_papier.metadata)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Paper map: National Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte200_papier.metadata>`__ (ch.swisstopo.landeskarte200_papier.metadata)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division national map 100 Paper  <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte1000_papier.metadata>`__ (ch.swisstopo.landeskarte1000_papier.metadata)                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accidents in the annual comparison <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_jahresvergleich>`__ (ch.astra.schwerverunfallte-kanton_jahresvergleich)                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Messstandorte Gewässerzustand Bund <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser>`__ (ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser)                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mirelandscapes AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_moorlandschaften&topic=aviation>`__ (ch.bafu.schutzgebiete-aulav_moorlandschaften)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Other protected areas AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_uebrige&topic=aviation>`__ (ch.bafu.schutzgebiete-aulav_uebrige)                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: cluster <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: recommendation of vaccination <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-impfung>`__ (ch.bag.zecken-fsme-impfung)                                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Paper Map: Snowshoe and Ski Tour Map 1:50'000 <//map.geo.admin.ch/?layers=ch.swisstopo.skitourenkarte-50.metadata>`__ (ch.swisstopo.skitourenkarte-50.metadata)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20160316:

Release 20160316 - Wednesday, March 16th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- Examples migrated to CodePen
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160303...r_160316>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160303...r_160316>`__


Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20160302:

Release 20160302 - Wednesday, March 2nd 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160217...r_160303>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- New topic 'Cadastre'
- WMS Import now supports non-LV03 coordinate system WMS Services
- Layer Manager now allows the rearranging of layers via Drag and Drop
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160217...r_160303>`__


Geodata
*******
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PCP Inventory <//map.geo.admin.ch/?layers=ch.babs.kulturgueter>`__ (ch.babs.kulturgueter)                                                                |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `HQStat <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hochwasserstatistik>`__ (ch.bafu.hydrologie-hochwasserstatistik)                                   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `HUG-Messstationen <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-untersuchungsgebiete_stationen>`__ (ch.bafu.hydrologie-untersuchungsgebiete_stationen)  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `HUG Hydro. Untersuchungsgebiete <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-untersuchungsgebiete>`__ (ch.bafu.hydrologie-untersuchungsgebiete)        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Product <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product>`__ (ch.swisstopo.swissimage-product)                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE <//map.geo.admin.ch/?bgLayer=ch.swisstopo.swissimage>`__ (ch.swisstopo.swissimage)                                                            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:100'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk100.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk100.noscale)         |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:50'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk50.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk50.noscale)            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:25'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk25.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk25.noscale)            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Color Map <//map.geo.admin.ch/?bgLayer=ch.swisstopo.pixelkarte-farbe>`__ (ch.swisstopo.pixelkarte-farbe)                                                 |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Grey Map <//map.geo.admin.ch/?bgLayer=ch.swisstopo.pixelkarte-grau>`__ (ch.swisstopo.pixelkarte-grau)                                                    |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160217:

Release 20160217 - Wednesday, February 17th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- RSS Feed for Release Notes
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160210...r_160217>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- New topic 'Energy'
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160210...r_160217>`__

Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar Energy - Suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dams under federal supervision <//map.geo.admin.ch/?layers=ch.bfe.stauanlagen-bundesaufsicht>`__ (ch.bfe.stauanlagen-bundesaufsicht)            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160210:

Release 20160210 - Wednesday, February 10th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160203...r_160210>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160203...r_160210>`__

Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160203:

Release 20160203 - Wednesday, February 3rd 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160127...r_160203>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160127...r_160203>`__

Geodata
*******
+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vertical movements <//map.geo.admin.ch/?layers=ch.swisstopo.hebungsraten>`__ (ch.swisstopo.hebungsraten)                               |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                 |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Geological Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Slope over 30° <//map.geo.admin.ch/?layers=ch.swisstopo-karto.hangneigung>`__ (ch.swisstopo-karto.hangneigung)                         |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160127:

Release 20160127 - Wednesday, January 27th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_160113...r_160127>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_160113...r_160127>`__

Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images swisstopo oblique <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schraegaufnahmen>`__ (ch.swisstopo.lubis-luftbilder_schraegaufnahmen)   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability of the PLR cadastre <//map.geo.admin.ch/?layers=ch.swisstopo-vd.stand-oerebkataster>`__ (ch.swisstopo-vd.stand-oerebkataster)                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20160113:

Release 20160113 - Wednesday, January 13th 2016
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_151216...r_160113>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug Fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_151216...r_160113>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `UNESCO World cultural heritage <//map.geo.admin.ch/?layers=ch.bak.schutzgebiete-unesco_weltkulturerbe>`__ (ch.bak.schutzgebiete-unesco_weltkulturerbe)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20151216:

Release 20151216 - Wednesday, November 16th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Improved search index (better integration of Haltestellen)
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_151202...r_151216>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- 2.5D ALPHA: first version of a future 3D viewer. ALPHA version is not for operational purposes, use it with care. 2.5D ALPHA might be removed any time.
- Show walking time in profile drawing
- New Menu interface for mobile devices
- More prominent warning in case query tool has more than 200 results
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_151202...r_151216>`__


Geodata
*******
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mapping of Floodplains of National Importance <//map.geo.admin.ch/?layers=ch.bafu.auen-vegetationskarten>`__ (ch.bafu.auen-vegetationskarten)                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `HTRANS LHN95-LN02 <//map.geo.admin.ch/?layers=ch.swisstopo.transformation-bezugsrahmen_hoehe>`__ (ch.swisstopo.transformation-bezugsrahmen_hoehe)                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `LV95 Transformation accuracy <//map.geo.admin.ch/?layers=ch.swisstopo.transformationsgenauigkeit>`__ (ch.swisstopo.transformationsgenauigkeit)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations local <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal>`__ (ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal)    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet)  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Topographical catchment areas of Swiss waterbodies 2km2 <//map.geo.admin.ch/?layers=ch.bafu.wasser-teileinzugsgebiete_2>`__ (ch.bafu.wasser-teileinzugsgebiete_2)                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _releasenotes_20151202:

Release 20151202 - Wednesday, December 2nd 2015
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_151125...r_151202>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_151125...r_151202>`__


.. _releasenotes_20151125:

Release 20151125 - Wednesday, November 25th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_151111...r_151125>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Profiles now show cummulative ascend and descend numbers
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_151111...r_151125>`__



Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Flood hazard levels 24h <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-messstationen_gefahren>`__ (ch.bafu.hydrologie-messstationen_gefahren)          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Public transport stops <//map.geo.admin.ch/?layers=ch.bav.haltestellen-oev>`__ (ch.bav.haltestellen-oev)                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Periodic updating <//map.geo.admin.ch/?layers=ch.swisstopo-vd.geometa-periodische_nachfuehrung>`__ (ch.swisstopo-vd.geometa-periodische_nachfuehrung)  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20151111:

Release 20151111 - Wednesday, November 11th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_151104...r_151111>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_151104...r_151111>`__


Geodata
*******
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerial images swisstopo oblique <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schraegaufnahmen>`__ (ch.swisstopo.lubis-luftbilder_schraegaufnahmen)      |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                      |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                         |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                   |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                        |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                    |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20151104:

Release 20151104 - Wednesday, November 4th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_151021...r_151104>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_151021...r_151104>`__


Geodata
*******
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Übersicht Geomorphologie <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomorphologie>`__ (ch.swisstopo.geologie-geomorphologie)                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nighttime railway noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_nacht>`__ (ch.bafu.laerm-bahnlaerm_nacht)                                    |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Daytime railway noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_tag>`__ (ch.bafu.laerm-bahnlaerm_tag)                                          |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                     |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy cities <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte>`__ (ch.bfe.energiestaedte)                                                              |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                            |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy Cities on the Path 2000-Watt <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-aufdemweg>`__ (ch.bfe.energiestaedte-2000watt-aufdemweg)  |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy-Regions <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-energieregionen>`__ (ch.bfe.energiestaedte-energieregionen)                             |
+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20151021:

Release 20151021 - Wednesday, October 21st 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_151007...r_151021>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_151007...r_151021>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `National Gravity Network <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte>`__ (ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Gravimetric base network <//map.geo.admin.ch/?layers=ch.swisstopo.landesschwerenetz>`__ (ch.swisstopo.landesschwerenetz)                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability of the PLR cadastre <//map.geo.admin.ch/?layers=ch.swisstopo-vd.stand-oerebkataster>`__ (ch.swisstopo-vd.stand-oerebkataster)                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20151007:

Release 20151007 - Wednesday, October 7th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Support for OR and AND operators in advanced search
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150923...r_151007>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Support for OR and AND operators in advanced search
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150923...r_151007>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Water & migrant bird reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-vogelreservate>`__ (ch.bafu.bundesinventare-vogelreservate)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20150923:

Release 20150923 - Wednesday, September 23rd 2015
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150825...r_150923>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Improved layer selector
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150825...r_150923>`__

Geodata
*******
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geological Hiking Trails <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geowege>`__ (ch.swisstopo.geologie-geowege)                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Last glacial maximum (vector) 500 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-eiszeit-lgm>`__ (ch.swisstopo.geologie-eiszeit-lgm)                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Army logistics centres <//map.geo.admin.ch/?layers=ch.vbs.armeelogistikcenter>`__ (ch.vbs.armeelogistikcenter)                                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Federal filling stations BEBECO <//map.geo.admin.ch/?layers=ch.vbs.bundestankstellen-bebeco>`__ (ch.vbs.bundestankstellen-bebeco)                                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Basic disposition "Zeus" <//map.geo.admin.ch/?layers=ch.vbs.grunddispositiv-zeus>`__ (ch.vbs.grunddispositiv-zeus)                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Army logistics centre logistics areas <//map.geo.admin.ch/?layers=ch.vbs.logistikraeume-armeelogistikcenter>`__ (ch.vbs.logistikraeume-armeelogistikcenter)                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mil Airspace Chart 1:500'000 <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Patrouille des Glaciers course (A race) <//map.geo.admin.ch/?layers=ch.vbs.patrouilledesglaciers-a_rennen>`__ (ch.vbs.patrouilledesglaciers-a_rennen)                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Patrouille des Glaciers course (Z race) <//map.geo.admin.ch/?layers=ch.vbs.patrouilledesglaciers-z_rennen>`__ (ch.vbs.patrouilledesglaciers-a_rennen)                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Army arsenals <//map.geo.admin.ch/?layers=ch.vbs.retablierungsstellen>`__ (ch.vbs.retablierungsstellen)                                                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Terrestrial Radiation <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-dosisleistung-terrestrisch>`__ (ch.swisstopo.geologie-dosisleistung-terrestrisch)                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150825:

Release 20150825 - Wednesday, August 25th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150805...r_150825>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150805...r_150825>`__

Geodata
*******

No changes


.. _releasenotes_20150805:

Release 20150805 - Wednesday, August 5th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Assure that API Javascript code is not polluting global namespace.
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150722...r_150805>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150722...r_150805>`__

Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Lonicera japonica <//map.geo.admin.ch/?layers=ch.bafu.neophyten-japanisches_geissblatt>`__ (ch.bafu.neophyten-japanisches_geissblatt)                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Heracleum mantegazzianum <//map.geo.admin.ch/?layers=ch.bafu.neophyten-riesenbaerenklau>`__ (ch.bafu.neophyten-riesenbaerenklau)                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division General Geol. Map 200 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-generalkarte-ggk200.metadata>`__ (ch.swisstopo.geologie-generalkarte-ggk200.metadata)                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SWISSIMAGE <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product>`__ (ch.swisstopo.swissimage-product)                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amphibians - consultation 2015 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien_anhoerung>`__ (ch.bafu.bundesinventare-amphibien_anhoerung)                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Fens - consultation 2015 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-flachmoore_anhoerung>`__ (ch.bafu.bundesinventare-flachmoore_anhoerung)                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dry grasslands - consultation 2015 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest Reserves <//map.geo.admin.ch/?layers=ch.bafu.waldreservate>`__ (ch.bafu.waldreservate)                                                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura forest reserves <//map.geo.admin.ch/?layers=ch.pronatura.waldreservate>`__ (ch.pronatura.waldreservate)                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150722:

Release 20150722 - Wednesday, July 22th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Switch API to `OpenLayers v3.6 <https://github.com/openlayers/ol3/releases/tag/v3.6.0>`__
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150708...r_150722>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Update to angular 1.4.2
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150708...r_150722>`__

Geodata
*******

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20150708:

Release 20150708 - Wednesday, July 8th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150701...r_150708>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Official release of new drawing and measuring function
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150701...r_150708>`__


Geodata
*******

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?bgLayer=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hydrogeological sketch <//map.geo.admin.ch/?layers=ch.bafu.hydrogeologie-uebersichtskarte>`__ (ch.bafu.hydrogeologie-uebersichtskarte)           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Agricultural zones boundaries <//map.geo.admin.ch/?layers=ch.blw.landwirtschaftliche-zonengrenzen>`__ (ch.blw.landwirtschaftliche-zonengrenzen)  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Water & migrant bird reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-vogelreservate>`__ (ch.bafu.bundesinventare-vogelreservate)    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload ≥ 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150701:

Release 20150617 - Wednesday, July 1st 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Extending TileMatrixSet (zoom level 18 and 19)  for WMTS EPSG:3857
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150624...r_150701>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150624...r_150701>`__


Geodata
*******
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Gewässer der Übersichtskarte 1:2 Mio <//map.geo.admin.ch/?layers=ch.bafu.vec25-gewaessernetz_2000>`__ (ch.bafu.vec25-gewaessernetz_2000)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Seen <//map.geo.admin.ch/?layers=ch.bafu.vec25-seen>`__ (ch.bafu.vec25-seen)                                                                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Basisgebiete (Einzugsgebiete) HADES <//map.geo.admin.ch/?layers=ch.bafu.hydrologischer-atlas_basisgebiete>`__ (ch.bafu.hydrologischer-atlas_basisgebiete)                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Bilanzgebiete (Einzugsgebiete) HADES <//map.geo.admin.ch/?layers=ch.bafu.hydrologischer-atlas_bilanzgebiete>`__ (ch.bafu.hydrologischer-atlas_bilanzgebiete)                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Flussgebiete (Einzugsgebiete) HADES <//map.geo.admin.ch/?layers=ch.bafu.hydrologischer-atlas_flussgebiete>`__ (ch.bafu.hydrologischer-atlas_flussgebiete)                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `River Typology for Switzerland <//map.geo.admin.ch/?layers=ch.bafu.typisierung-fliessgewaesser>`__ (ch.bafu.typisierung-fliessgewaesser)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mean runoff and flow regime types for the river network of Switzerland <//map.geo.admin.ch/?layers=ch.bafu.mittlere-abfluesse>`__ (ch.bafu.mittlere-abfluesse)                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Grundlagen zur Bestimmung der Abflussmenge Q347 <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-q347>`__ (ch.bafu.hydrologie-q347)                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Niedrigwasserstatistik NQStat <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-niedrigwasserstatistik>`__ (ch.bafu.hydrologie-niedrigwasserstatistik)                                                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `HQStat Hochwasserstatistik <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hochwasserstatistik>`__ (ch.bafu.hydrologie-hochwasserstatistik)                                                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `HWGWP Hochwassergrenzwertpegel <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hochwassergrenzwertpegel>`__ (ch.bafu.hydrologie-hochwassergrenzwertpegel)                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `HADES 5.1.2 (kantonale Messstationen) <//map.geo.admin.ch/?layers=ch.bafu.hydrologischer-atlas_kantonale-messstationen>`__ (ch.bafu.hydrologischer-atlas_kantonale-messstationen)                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Messstationen der hydrologischen Untersuchungsgebiete <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-untersuchungsgebiete_stationen>`__ (ch.bafu.hydrologie-untersuchungsgebiete_stationen)                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hydrologische Untersuchungsgebiete <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-untersuchungsgebiete>`__ (ch.bafu.hydrologie-untersuchungsgebiete)                                                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Datenbank Geschiebefrachten (Bund) <//map.geo.admin.ch/?layers=ch.bafu.feststoffe-geschiebemessnetz>`__ (ch.bafu.feststoffe-geschiebemessnetz)                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Datenbank Querprofile (QP) - Vermessungsstrecken <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vermessungsstrecken - Querprofilmarke <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Badegewässerqualität <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Kläranlagendatenbank (ARA-DB) - Prozentanteil Abwasser im Vorfluter bei Niedrigwasser <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-klaeranlagen_anteilq347>`__ (ch.bafu.gewaesserschutz-klaeranlagen_anteilq347)  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Kläranlagendatenbank (ARA-DB) - Ausbaugrösse (EGW) <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-klaeranlagen_ausbaugroesse>`__ (ch.bafu.gewaesserschutz-klaeranlagen_ausbaugroesse)                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Kläranlagendatenbank (ARA-DB) - Reinigungstyp <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp>`__ (ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp)                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Nationale Daueruntersuchung der schweizerischen Fliessgewässer <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser>`__ (ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser)               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Strukturgüte Hochrhein (2020) <//map.geo.admin.ch/?layers=ch.bafu.strukturguete-hochrhein_linkesufer>`__ (ch.bafu.strukturguete-hochrhein_linkesufer)                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Strukturgüte Hochrhein (2020) <//map.geo.admin.ch/?layers=ch.bafu.strukturguete-hochrhein_linkesumfeld>`__ (ch.bafu.strukturguete-hochrhein_linkesumfeld)                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Strukturgüte Hochrhein (2020) <//map.geo.admin.ch/?layers=ch.bafu.strukturguete-hochrhein_rechtesufer>`__ (ch.bafu.strukturguete-hochrhein_rechtesufer)                                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Strukturgüte Hochrhein (2020) <//map.geo.admin.ch/?layers=ch.bafu.strukturguete-hochrhein_rechtesumfeld>`__ (ch.bafu.strukturguete-hochrhein_rechtesumfeld)                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Strukturgüte Hochrhein (2020) <//map.geo.admin.ch/?layers=ch.bafu.strukturguete-hochrhein_sohle>`__ (ch.bafu.strukturguete-hochrhein_sohle)                                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `PDO plant products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-konditoreiwaren>`__ (ch.blw.ursprungsbezeichnungen-konditoreiwaren)                                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public Transportation VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr)                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forested areas <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover-wald>`__ (ch.swisstopo.vec200-landcover-wald)                                                                                                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (10-100km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10to100km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10to100km2)                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (100-1000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2)                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (1000-21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2)                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PDO spirits <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-spirituosen>`__ (ch.blw.ursprungsbezeichnungen-spirituosen)                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PDO cheese <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150617:

Release 20150617 - Wednesday, June 17th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Add preview version of GeoAdmin API with Openlayers 3.6.0
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150603...r_150617>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150603...r_150617>`__


Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swissimage <//map.geo.admin.ch/?bgLayer=ch.swisstopo.swissimage>`__ (ch.swisstopo.swissimage)                                                                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150603:

Release 20150603 - Wednesday, June 3rd 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Vector layer and styling example
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150528...r_150603>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Enhanced background layer selector
- Enhanced share menu
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150528...r_150603>`__


Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sachplan Übertragungsleitungen (SÜL) <//map.geo.admin.ch/?layers=ch.bfe.sachplan-uebertragungsleitungen_kraft>`__ (ch.bfe.sachplan-uebertragungsleitungen_kraft)                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sediment thickness <//map.geo.admin.ch/?layers=ch.sgpk.maechtigkeit-lockergesteine>`__ (ch.sgpk.maechtigkeit-lockergesteine)                                                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Journey through time <//map.geo.admin.ch/?layers=ch.swisstopo.zeitreihen>`__ (ch.swisstopo.zeitreihen)                                                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissTLM-Map (gray) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-grau>`__ (ch.swisstopo.swisstlm3d-karte-grau)                                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissTLM-Map (color) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-farbe>`__ (ch.swisstopo.swisstlm3d-karte-farbe)                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Federal Inventory ISOS <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder)                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ibex colonies <//map.geo.admin.ch/?layers=ch.bafu.fauna-steinbockkolonien)>`__ (ch.bafu.fauna-steinbockkolonien)                                                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150528:

Release 20150528 - Thursday, May 28th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Example and API tooltips for GeoJSON layer
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150520...r_150528>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Edit, save and share drawing (KML)
- Add warning for third party geodata
- Improved search function
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150520...r_150528>`__

.. _releasenotes_20150520:

Release 20150520 - Wednesday, May 20th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Add support for GEOJson layers
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150506...r_150520>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Fix profile calculation and display for latest versions of FireFox
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150506...r_150520>`__


Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. 1st night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde)                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. 2nd night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde)                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. helicopters Lmax <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel)     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. helicopters Lr <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter)                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. last night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. light aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. light / large aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge)    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Noise exp. milit. aerodr. (tot.) <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aeromagnetik Aargau 1100 m 100 <//map.geo.admin.ch/?layers=ch.nagra.aeromagnetische-karte_1100>`__ (ch.nagra.aeromagnetische-karte_1100)                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aeromagnetik Aargau 1500 m 100 <//map.geo.admin.ch/?layers=ch.nagra.aeromagnetische-karte_1500>`__ (ch.nagra.aeromagnetische-karte_1500)                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Water temperature rivers <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_temperatur>`__ (ch.bafu.hydroweb-messstationen_temperatur)                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Stations hydrological forecasts <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_vorhersage>`__ (ch.bafu.hydroweb-messstationen_vorhersage)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Flood alert map <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-warnkarte_national>`__ (ch.bafu.hydroweb-warnkarte_national)                                                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `NAQUA monitoring network <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_grundwasser>`__ (ch.bafu.hydroweb-messstationen_grundwasser)                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Lage Fliessgewässer und Seen <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_zustand>`__ (ch.bafu.hydroweb-messstationen_zustand)                                                                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Flood alert small catchments <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-warnkarte_regional>`__ (ch.bafu.hydroweb-warnkarte_regional)                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hochwasser Gefahrenstufen <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_gefahren>`__ (ch.bafu.hydroweb-messstationen_gefahren)                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150506:

Release 20150506 - Wednesday, May 6th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150422...r_150506>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150422...r_150506>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150422:

Release 20150422 - Wednesday, April 22nd 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150415...r_150422>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150415...r_150422>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas 1:25'000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_hochwasser>`__ (ch.bafu.showme-gemeinden_hochwasser)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_lawinen>`__ (ch.bafu.showme-gemeinden_lawinen)                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_rutschungen>`__ (ch.bafu.showme-gemeinden_rutschungen)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: rockfall <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_sturzprozesse>`__ (ch.bafu.showme-gemeinden_sturzprozesse)                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_hochwasser>`__ (ch.bafu.showme-kantone_hochwasser)                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_lawinen>`__ (ch.bafu.showme-kantone_lawinen)                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_rutschungen>`__ (ch.bafu.showme-kantone_rutschungen)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: rockfall <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_sturzprozesse>`__ (ch.bafu.showme-kantone_sturzprozesse)                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alpine products <//map.geo.admin.ch/?layers=ch.blw.alpprodukte>`__ (ch.blw.alpprodukte)                                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountain products <//map.geo.admin.ch/?layers=ch.blw.bergprodukte>`__ (ch.blw.bergprodukte)                                                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Parks <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20150415:

Release 20150415 - Wednesday, April 15th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Upgrade API to OpenLayers v3.4.0
- Adding print at 1:300'000 scale
- Limiting the number of words in search
- Removing `SearchServer` **type=featureidentify** service
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150325...r_150415>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Displaying position and heading on mobile
- Upgrading to OpenLayers v3.4.0
- Adding keyboard navigation in search result
- Improving support for HTTPS
- Better handling of `queryable` parameter in LayerGroup
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150325...r_150415>`__



.. _releasenotes_20150325:

Release 20150325 - Wednesday, March 25th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Improving profile service
- Improving WMTS service (EPSG:2056)
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150312...r_150325>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Improving draw, profile, print and embed functions
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150312...r_150325>`__


Geodata
*******

+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Unfälle mit Personenschaden <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                 |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Unfälle mit Fahrradbeteiligung <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                  |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Unfälle mit Fussgängerbeteiligung <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)             |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Unfälle mit Getöteten <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                             |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Unfälle mit Motorradbeteiligung <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)               |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `TBE: cluster <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                            |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `TBE: recommendation of vaccination <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-impfung>`__ (ch.bag.zecken-fsme-impfung)                                                    |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20150312:

Release 20150312 - Thursday, March 12th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150304...r_150312>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- New embed page optimized for display in iframe
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150304...r_150312>`__


Geodata
*******

+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Traffic counting locations principal <//s.geo.admin.ch/63386dcd8e>`__ (ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet)                                           |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Traffic counting locations local <//s.geo.admin.ch/63386b9324>`__ (ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal)                                              |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20150304:

Release 20150304 - Wednesday, March 4th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Official support for tilematrix sets 17, 19 and 24 (WMTS services)
- WMTS GetCapabilities document now supports special characters in layer description and title
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150211...r_150304>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Improved search on mobile devices (keyboard handling)
- KML file can now include NetworkLink tags.
- Fixed application for Windows 8.1/IE11 on mobile devices (Most recent Lumia devices)
- Object Information window is now capable of showing more than 200 results
- Feature in permalink now zooms to specified feature again
- Fixed error resulting in broken viewer for Lubis pictures
- It is now possible to cancel the print
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150211...r_150304>`__


Geodata
*******

+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New       | `Background map hydrol. data <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hintergrundkarte>`__ (ch.bafu.hydrologie-hintergrundkarte)                                           |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                    |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                             |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Geologische Gutachten (Punkte) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-punkte>`__ (ch.swisstopo.geologie-gisgeol-punkte)                                      |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Geologische Gutachten (Linien) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-linien>`__ (ch.swisstopo.geologie-gisgeol-linien)                                      |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Geologische Gutachten (1x1km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-1x1km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-1x1km)                       |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Geologische Gutachten (0-10km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-lt10km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-lt10km2)                 |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Geologische Gutachten (10x10km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10x10km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10x10km)                 |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Geologische Gutachten (10-21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10to21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10to21000km2)   |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Geologische Gutachten (>21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2)         |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Mire landscapes <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-moorlandschaften>`__ (ch.bafu.bundesinventare-moorlandschaften)                                             |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Cant. routes for exceptional loads <//map.geo.admin.ch/?layers=ch.astra.ausnahmetransportrouten>`__ (ch.astra.ausnahmetransportrouten)                                          |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                       |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Pollutant releases (SwissPRTR) <//map.geo.admin.ch/?layers=ch.bafu.swissprtr>`__ (ch.bafu.swissprtr)                                                                            |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20150211:

Release 20150211 - Wednesday, February 11th 2015
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Update API version of OL3 to `v3.2.0 <https://github.com/openlayers/ol3/releases/tag/v3.2.0>`__
- Query tool improvement
- Base Python libraries update
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150128...r_150211>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Better iPod support
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150128...r_150211>`__


Geodata
*******

+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New       | `Stream order <//map.geo.admin.ch/?layers=ch.bafu.flussordnungszahlen-strahler>`__ (ch.bafu.flussordnungszahlen-strahler)                                                        |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `National Map 1:500'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk500.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk500.noscale)                                |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `National Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk200.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk200.noscale)                                |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `National Map 1:100'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk100.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk100.noscale)                                |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `National Map 1:50'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk50.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk50.noscale)                                   |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `National Map 1:25'000 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk25.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk25.noscale)                                   |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Color Map <//s.geo.admin.ch/9760998>`__ (ch.swisstopo.pixelkarte-farbe)                                                                                                         |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Grey Map <//s.geo.admin.ch/929a8e1>`__ (ch.swisstopo.pixelkarte-grau)                                                                                                           |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                         |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                           |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                         |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                     |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                     |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `SAIP in consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                            |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `SP aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Temperature monitoring stations <//s.geo.admin.ch/62a2b60afa>`__ (ch.bafu.hydrologie-wassertemperaturmessstationen)                                                             |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Protection areas <//s.geo.admin.ch/62a2b791e7>`__ (ch.bafu.grundwasserschutzareale)                                                                                             |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Protection zones <//s.geo.admin.ch/62a2c2e63a>`__ (ch.bafu.grundwasserschutzzonen)                                                                                              |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Water protection regions <//s.geo.admin.ch/62a2c387f5>`__ (ch.bafu.gewaesserschutzbereiche)                                                                                     |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20150128:

Release 20150128 - Wednesday, January 28th 2015
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150114...r_150128>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Improved query tool
- Offline mode now supports http[s] included kml files
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150114...r_150128>`__


Geodata
*******

+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `swissALTI3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)                                   |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Protection of cultural property inventory <//map.geo.admin.ch/?layers=ch.babs.kulturgueter>`__ (ch.babs.kulturgueter)                                                             |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `TWW - Anhörung 2015 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung) |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20150114:

Release 20150114 - Wednesday, January 14th 2015
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Update GeoAdmin API to be based on OpenLayers v3.0.0-beta.5-1590
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_150107...r_150114>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_150107...r_150114>`__


Geodata
*******

+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                       |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                           |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `LV95 Transformation accuracy <//map.geo.admin.ch/?layers=ch.swisstopo.transformationsgenauigkeit>`__ (ch.swisstopo.transformationsgenauigkeit)      |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _releasenotes_20150107:

Release 20150107 - Wednesday, January 7th 2015
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_141223...r_150107>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- New topic aviation
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_141223...r_150107>`__


Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Journey through time - Maps <//map.geo.admin.ch/?layers=ch.swisstopo.zeitreihen>`__ (ch.swisstopo.zeitreihen)                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Floodplains AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_auen>`__ (ch.bafu.schutzgebiete-aulav_auen)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Game reserves AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_jagdbanngebiete>`__ (ch.bafu.schutzgebiete-aulav_jagdbanngebiete)       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mirelandscapes AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_moorlandschaften>`__ (ch.bafu.schutzgebiete-aulav_moorlandschaften)    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Other protected areas AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_uebrige>`__ (ch.bafu.schutzgebiete-aulav_uebrige)               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Protected areas MIL <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-luftfahrt>`__ (ch.bafu.schutzgebiete-luftfahrt)                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air navigation obstacles <//map.geo.admin.ch/?layers=ch.bazl.luftfahrthindernis>`__ (ch.bazl.luftfahrthindernis)                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Points of interest <//map.geo.admin.ch/?layers=ch.bazl.points-of-interest>`__ (ch.bazl.points-of-interest)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20141223:

Release 20141223 - Tuesday, December 23th 2014
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_141218...r_141223>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- BETA: new query tool in object information window
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_141218...r_141223>`__

.. _releasenotes_20141218:

Release 20141218 - Thursday, December 18th 2014
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_141126...r_141218>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Drawing integrated into feedback tool
- UI improvements on dialogs
- WMS import list updated
- Support print on A3
- Support saving of KML in IE9 and naming of file in Safari
- Fixed print that contained kml
- Support LV95 in permalink paramater
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_141126...r_141218>`__

Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division Ski Tour Map <//map.geo.admin.ch/?layers=ch.swisstopo.skitourenkarte-50.metadata>`__ (ch.swisstopo.skitourenkarte-50.metadata)                                                                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Dynamic Pressure 30 <//map.geo.admin.ch/?layers=ch.bafu.sturm-staudruck_30>`__ (ch.bafu.sturm-staudruck_30)                                                                                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Dynamic Pressure 50 <//map.geo.admin.ch/?layers=ch.bafu.sturm-staudruck_50>`__ (ch.bafu.sturm-staudruck_50)                                                                                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Dynamic Pressure 100 <//map.geo.admin.ch/?layers=ch.bafu.sturm-staudruck_100>`__ (ch.bafu.sturm-staudruck_100)                                                                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Dynamic Pressure 300 <//map.geo.admin.ch/?layers=ch.bafu.sturm-staudruck_300>`__ (ch.bafu.sturm-staudruck_300)                                                                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Gusts 30 <//map.geo.admin.ch/?layers=ch.bafu.sturm-boeenspitzen_30>`__ (ch.bafu.sturm-boeenspitzen_30)                                                                                                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Gusts 50 <//map.geo.admin.ch/?layers=ch.bafu.sturm-boeenspitzen_50>`__ (ch.bafu.sturm-boeenspitzen_50)                                                                                                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Gusts 100 <//map.geo.admin.ch/?layers=ch.bafu.sturm-boeenspitzen_100>`__ (ch.bafu.sturm-boeenspitzen_100)                                                                                                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Windstorm Gusts 300 <//map.geo.admin.ch/?layers=ch.bafu.sturm-boeenspitzen_300>`__ (ch.bafu.sturm-boeenspitzen_300)                                                                                                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Emissionsplan Eisenbahnlärm 2015 N <//map.geo.admin.ch/?layers=ch.bav.laerm-emissionsplan_eisenbahn_nacht>`__ (ch.bav.laerm-emissionsplan_eisenbahn_nacht)                                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Emissionsplan Eisenbahnlärm 2015 T <//map.geo.admin.ch/?layers=ch.bav.laerm-emissionsplan_eisenbahn_tag>`__ (ch.bav.laerm-emissionsplan_eisenbahn_tag)                                                                                              |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy cities  <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte>`__ (ch.bfe.energiestaedte)                                                                                                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy Cities on the Path 2000-Watt <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-aufdemweg>`__ (ch.bfe.energiestaedte-2000watt-aufdemweg)                                                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                                                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Energy-Regions <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-energieregionen>`__ (ch.bfe.energiestaedte-energieregionen)                                                                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Heliports/mountain landing sites <//map.geo.admin.ch/?layers=ch.bazl.heliports-gebirgslandeplaetze>`__ (ch.bazl.heliports-gebirgslandeplaetze)                                                                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20141126:

Release 20141126 - Wednesday, November 26th 2014
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_141112...r_141126>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Possibility to attach drawing to feedback as kml
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_141112...r_141126>`__

Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Federal Inventory of Raised and Transition Bogs of National Importance - Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-hochmoore_anhoerung>`__ (ch.bafu.bundesinventare-hochmoore_anhoerung)                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bundesinventar der Flachmoore von nationaler Bedeutung - Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-flachmoore_anhoerung>`__ (ch.bafu.bundesinventare-flachmoore_anhoerung)                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bundesinventar der Auengebiete von nationaler Bedeutung - Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-auen_anhoerung>`__ (ch.bafu.bundesinventare-auen_anhoerung)                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bundesinventar der Amphibienlaichgebiete von nationaler Bedeutung - Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien_anhoerung>`__ (ch.bafu.bundesinventare-amphibien_anhoerung)                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bundesinventar der Amphibienlaichgebiete - Wanderobjekte - Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien_wanderobjekte_anhoerung>`__ (ch.bafu.bundesinventare-amphibien_wanderobjekte_anhoerung)                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bundesinventar der Trockenwiesen und -weiden von nationaler Bedeutung - Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung) |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20141112:

Release 20141112 - Thursday, November 12th 2014
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_141030...r_141112>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Export KML on Safari browsers
- Displays WMS GetCapabilities content as a tree
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_141030...r_141112>`__

Geodata
*******

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20141030:

Release 20141030 - Thursday, October 30th 2014
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_141015...r_141030>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Import/export KML text labels
- Improves social media sharing
- Improves responsive design with a small height screen
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_141015...r_141030>`__

Geodata
*******

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Groundwater protection zones <//map.geo.admin.ch/?layers=ch.bafu.grundwasserschutzzonen>`__ (ch.bafu.grundwasserschutzzonen)                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Water protection regions <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutzbereiche>`__ (ch.bafu.gewaesserschutzbereiche)                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Groundwater protection areas <//map.geo.admin.ch/?layers=ch.bafu.grundwasserschutzareale>`__ (ch.bafu.grundwasserschutzareale)                                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                                                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 50 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 20 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 2 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 100 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 10 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 1 Mbit/s <//map.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cant. routes for exceptional loads <//map.geo.admin.ch/?layers=ch.astra.ausnahmetransportrouten>`__ (ch.astra.ausnahmetransportrouten)                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20141015:

Release 20141015 - Wednesday, October 15th 2014
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Improve documentation
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_141001...r_141015>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Save drawings as KML file
- Improved menu navigation on mobile devices
- Use correct UTM definition for mouse coordinates
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_141001...r_141015>`__

Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Udpate    | `Energy cities <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte>`__ (ch.bfe.energiestaedte)                                                                                                      |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Energy Cities on the Path 2000-Watt <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-aufdemweg>`__ (ch.bfe.energiestaedte-2000watt-aufdemweg)                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Energy-Regions <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-energieregionen>`__ (ch.bfe.energiestaedte-energieregionen)                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update    | `Agnes <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-agnes>`__ (ch.swisstopo.fixpunkte-agnes)                                                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20141001:

Release 20141001 - Wednesday, October 1st 2014
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Fix IE10 print download
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140925...r_141001>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140925...r_141001>`__


.. _releasenotes_20140925:

Release 20140925 - Thursday, September 25th 2014
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140918_1...r_140925>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140918_1...r_140925>`__

Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Energy cities <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte>`__ (ch.bfe.energiestaedte)                                                                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `2000-Watt Sites <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-areale>`__ (ch.bfe.energiestaedte-2000watt-areale)                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Energy Cities on the Path 2000-Watt <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-2000watt-aufdemweg>`__ (ch.bfe.energiestaedte-2000watt-aufdemweg)                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Energy-Regions <//map.geo.admin.ch/?layers=ch.bfe.energiestaedte-energieregionen>`__ (ch.bfe.energiestaedte-energieregionen)                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Polluted sites civil aerodromes <//map.geo.admin.ch/?layers=ch.bazl.kataster-belasteter-standorte-zivilflugplaetze>`__ (ch.bazl.kataster-belasteter-standorte-zivilflugplaetze)                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Updated| `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Updated| `Auen - Anhoerung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-auen_anhoerung>`__ (ch.bafu.bundesinventare-auen_anhoerung)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140918:

Release 20140918 - Thursday, September 18th 2014
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140908...r_140918_1>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- BETA offline: possibility to store 1 or 2 layers locally for offline usage
- Rotation button: appears when map is rotated in order to reset the rotation
- Improve usability on mobile version
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140908...r_140918_1>`__

Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Siegfried Map First edition <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-siegfried>`__ (ch.swisstopo.hiks-siegfried)                                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140908:

Release 20140908 - Monday, September 8th 2014
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140827...r_140908>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140827...r_140908>`__

Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geocover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140827:

Release 20140827 - Wednesday, August 27th 2014
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- New localisation API example
- Added documentation specific to CMS integration of our API
- Compress content of API loader for faster loading
- Multiple bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140820...r_140827>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Beautification of feedback window
- Multiple bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140820...r_140827>`__


Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas 1:25'000 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dufour Map First edition <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-dufour>`__ (ch.swisstopo.hiks-dufour)                                                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140820:

Release 20140820 - Wednesday, August 20th 2014
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Multiple bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140814...r_140820>`__


`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Multiple bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140813...r_140820>`__


Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Pro Natura forest reserves <//map.geo.admin.ch/?layers=ch.pronatura.waldreservate>`__ (ch.pronatura.waldreservate)                                                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Polluted sites - pub. transp. <//map.geo.admin.ch/?layers=ch.bav.kataster-belasteter-standorte-oev>`__ (ch.bav.kataster-belasteter-standorte-oev)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Forest Reserves <//map.geo.admin.ch/?layers=ch.bafu.waldreservate>`__ (ch.bafu.waldreservate)                                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140813:

Release 20140813 - Wednesday, August 13th 2014
-----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- New and improved design of http://api.geo.admin.ch. It's now fully responsive.
- API Loader is now cached which improves loading time significanctly
- Find service improved performance when using exact matching
- Small bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140730...r_140813>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Last clicked popu now will stay on top of all other popups
- Feedback now allows you to attach files to your message
- Small bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140730...r_140813>`__

Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Federal Inventory of Swiss heritage sites ISOS <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder)                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140730:

Release 20140730 - Wednesday, July 30th 2014
--------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- In Search, sort feature results by geolocation
- Add new example: `Catalog <//api3.geo.admin.ch/examples/geoadmin_catalog.html>`__
- JavaScript API now has the possibility to disable tooltips on the maps in runtime.
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140717...r_140730>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Update sitemaps
- New translations in Catalogs. Corresponds to GeoCat entries now.
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140717...r_140730>`__

Geodata
********

No updates

.. _releasenotes_20140716:

Release 20140716 - Wednesday, July 16th 2014
--------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Udpate documentation to include description of output parameters in services
- Lubis tooltips and viewer now contains backlink to object in map
- Add reverse geoconding on locations. Note: this service needs registering. `Read our terms <https://www.geo.admin.ch/de/geo-services/geo-services/portrayal-services-web-mapping/programming-interface-api/order_form.html>`__.
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/rel_140702...r_140717>`__

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Remember location of popups on close
- Show wait cursor indicator during searches
- Update popup contents on language change (Metadata and Help)
- Close menu on start of application for smaller screens
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140702...r_140717>`__

Geodata
*******

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Agricultural zones boundaries <//map.geo.admin.ch/?layers=ch.blw.landwirtschaftliche-zonengrenzen>`__ (ch.blw.landwirtschaftliche-zonengrenzen)                                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Freight traffic <//map.geo.admin.ch/?layers=ch.are.belastung-gueterverkehr-bahn>`__ (ch.are.belastung-gueterverkehr-bahn)                                                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Heavy goods traffic <//map.geo.admin.ch/?layers=ch.are.belastung-gueterverkehr-strasse>`__ (ch.are.belastung-gueterverkehr-strasse)                                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Passenger traffic (public transport) <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-bahn>`__ (ch.are.belastung-personenverkehr-bahn)                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Passenger traffic <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-strasse>`__ (ch.are.belastung-personenverkehr-strasse)                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (Punkte) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-punkte>`__ (ch.swisstopo.geologie-gisgeol-punkte)                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (Linien) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-linien>`__ (ch.swisstopo.geologie-gisgeol-linien)                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (1x1km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-1x1km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-1x1km)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (0-10km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-lt10km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-lt10km2)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (10x10km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10x10km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10x10km)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (10-21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10to21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10to21000km2)                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geologische Gutachten (>21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2)                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140702:

Release 20140702 - Wednesday, July 2nd 2014
-------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Minor bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140625...r_140702>`__

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''
- Minor bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140625...r_140702>`__

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swissimage <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage>`__ (ch.swisstopo.swissimage)                                                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Release 20140625 - Wednesday, June 25th 2014
--------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Minor bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r140618...r_140625>`__

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Minor bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140618...r_140625>`__

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 50 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 20 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 2 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 100 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 10 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 1 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map3.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map3.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map3.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 50 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 20 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 2 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 100 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 10 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 1 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map3.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map3.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map3.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140618:

Release 20140618 - Wednesday, June 18th 2014
--------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Minor bug fixes
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_140611...r140618>`__

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Minor bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_140612...r_140618>`__

Geodata
********

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Topographical landscape model <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-grau>`__ (ch.swisstopo.swisstlm3d-karte-grau)                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Topographical landscape model <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-farbe>`__ (ch.swisstopo.swisstlm3d-karte-farbe)                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

Release 20140611 - Wednesday, June 11th 2014
--------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Address prefix search in `locations search <//api3.geo.admin.ch/services/sdiservices.html#response-syntax>`__
- Support several ids in `feature service <//api3.geo.admin.ch/services/sdiservices.html#feature-resource>`__
- Support "contains" parameter `find service <//api3.geo.admin.ch/services/sdiservices.html#find>`__
- Documentation for `search radius and identify <//api3.geo.admin.ch/services/sdiservices.html#simulate-a-search-radius>`__
- Minor bugfixes

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Collapsible popups
- Minor bug fixes

Geodata
********

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hochmoore – Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-hochmoore_anhoerung>`__ (ch.bafu.bundesinventare-hochmoore_anhoerung)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Auen – Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-auen_anhoerung>`__ (ch.bafu.bundesinventare-auen_anhoerung)                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Flachmoore Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-flachmoore_anhoerung>`__ (ch.bafu.bundesinventare-flachmoore_anhoerung)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Moorlandschaften – Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-moorlandschaften_anhoerung>`__ (ch.bafu.bundesinventare-moorlandschaften_anhoerung)           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TWW – Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung)  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amphibien Wanderobjekte 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien_wanderobjekte_anhoerung>`__ (ch.bafu.bundesinventare-amphibien_wanderobjekte_anhoerung) |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amphibien – Anhörung 2014 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-amphibien_anhoerung>`__ (ch.bafu.bundesinventare-amphibien_anhoerung)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `LV95 Transformation accuracy <//map.geo.admin.ch/?layers=ch.swisstopo.transformationsgenauigkeit>`__ (ch.swisstopo.transformationsgenauigkeit)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Landwirtschaftliche Zonengrenzen <////map.geo.admin.ch/?layers=ch.blw.landwirtschaftliche-zonengrenzen>`__ (ch.blw.landwirtschaftliche-zonengrenzen)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140521:

Release 20140521 -  Thursday, May 21st 2014
-------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- New API `searchbox example <//api3.geo.admin.ch/examples/geoadmin_search.html>`__
- Fix api layers shown in FAQ
- MapProxy migration from previous project
- Fixing issue in the WMTS GetCapabilities document (themes, legends)
- API: new map creation parameter to activate/deactivate tooltip
- Minor bug fixes


`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- New fullscreen mode and search box
- New location marker shown when entering coordinates
- Update google closure library url
- Minor bug fixes

Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public Transportation VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr) |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forested areas <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover-wald>`__ (ch.swisstopo.vec200-landcover-wald)                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140508:

Release 20140508 -  Thursday, May 8th 2014
------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- LUBIS Viewer: Adding permalink coordinates X, Y, zoom and rotate for better sharing
- Optimized sizes of images
- Adding OWS Checker
- Minor bug fixes

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Separated Feature and Location search
- Added location marker for search results
- Added context sensitive help
- Remove addressbar on modern iOS devices
- Swipe Ratio Fix for Firefox and IE
- Updating Geolocation point even after zoom or pan
- Minor bug fixes

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update  | `Time of travel with PT <//map.geo.admin.ch/?layers=ch.are.reisezeit-oev>`__ (ch.are.reisezeit-oev)                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update  | `Time of travel IMT <//map.geo.admin.ch/?layers=ch.are.reisezeit-miv>`__ (ch.are.reisezeit-miv)                                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update  | `Public transport connection quality <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update  | `Density of employment <//map.geo.admin.ch/?layers=ch.are.beschaeftigtendichte>`__ (ch.are.beschaeftigtendichte)                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update  | `Population density <//map.geo.admin.ch/?layers=ch.are.bevoelkerungsdichte>`__ (ch.are.bevoelkerungsdichte)                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update  | `Agglomeration and isolated cities <//map.geo.admin.ch/?layers=ch.are.agglomerationen_isolierte_staedte>`__ (ch.are.agglomerationen_isolierte_staedte)       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140430:

Release 20140430 -  Wednesday, April 30th 2014
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- `New example <//api3.geo.admin.ch/examples/geoadmin_rectangle.html>`__
- Minor bug fixes

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Support swisssearch parameter in permalink
- Add a correct native browser print
- Minor bug fixes

Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geologische Gutachten (Punkte) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-punkte>`__ (ch.swisstopo.geologie-gisgeol-punkte)                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geologische Gutachten (Linien) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-linien>`__ (ch.swisstopo.geologie-gisgeol-linien)                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geologische Gutachten (1x1km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-1x1km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-1x1km)                                           |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geologische Gutachten (0-10km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-lt10km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-lt10km2)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geologische Gutachten (10x10km) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10x10km>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10x10km)                                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geologische Gutachten (10-21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-10to21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-10to21000km2)                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geologische Gutachten (>21000km2) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2>`__ (ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2)                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `General Geological Map <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-generalkarte-ggk200>`__ (ch.swisstopo.geologie-generalkarte-ggk200)                                                        |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ecomorphology F – River reaches <//map.geo.admin.ch/?layers=ch.bafu.oekomorphologie-f_abschnitte>`__ (ch.bafu.oekomorphologie-f_abschnitte)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ecomorphology F – Drop structures <//map.geo.admin.ch/?layers=ch.bafu.oekomorphologie-f_abstuerze>`__ (ch.bafu.oekomorphologie-f_abstuerze)                                                         |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Ecomorphology F – Structures <//map.geo.admin.ch/?layers=ch.bafu.oekomorphologie-f_bauwerke>`__ (ch.bafu.oekomorphologie-f_bauwerke)                                                                |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140423:

Release 20140423 -  Wednesday, April 23th 2014
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Search: allow queries with special characters (like "Biel/Bienne")
- Search: heavily improved ranking of results
- Minor bug fixes


`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Draw: you are now able to draw icons on the map
- Import KML: improved performance for big kml files
- Time Selector: fix on mobile devices

Geodata
********

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Parks of national importance <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_hochwasser>`__ (ch.bafu.showme-gemeinden_hochwasser)                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_lawinen>`__ (ch.bafu.showme-gemeinden_lawinen)                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_rutschungen>`__ (ch.bafu.showme-gemeinden_rutschungen)                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe communes: rockfall <//map.geo.admin.ch/?layers=ch.bafu.showme-gemeinden_sturzprozesse>`__ (ch.bafu.showme-gemeinden_sturzprozesse)                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: floods <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_hochwasser>`__ (ch.bafu.showme-kantone_hochwasser)                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: avalanches <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_lawinen>`__ (ch.bafu.showme-kantone_lawinen)                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: landslides <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_rutschungen>`__ (ch.bafu.showme-kantone_rutschungen)                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ShowMe cantons: rockfall <//map.geo.admin.ch/?layers=ch.bafu.showme-kantone_sturzprozesse>`__ (ch.bafu.showme-kantone_sturzprozesse)                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Typology of municipalities ARE <//map.geo.admin.ch/?layers=ch.are.gemeindetypen>`__ (ch.are.gemeindetypen)                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140409:

Release 20140409 -  Wednesday, April 9th 2014
---------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Improve search for parcels (language dependant keyword support)
- Minor bug fixes

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Added TimeSelector tool to support layers with a time dimension
- Improved map interaction on some mobile devices
- Support UTM zone 32N coordinates for mouse position
- Minor bug fixes

Geodata
********

+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: cluster <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                                                  |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: recommendation of vaccination <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-impfung>`__ (ch.bag.zecken-fsme-impfung)                                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of seismic subgrade categories under standard SIA 261 <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Perimeters of existing spectral micro-zoning studies <//map.geo.admin.ch/?layers=ch.bafu.gefahren-spektral>`__ (ch.bafu.gefahren-spektral)                                                          |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                                   |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerial images privates <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-firmen>`__ (ch.swisstopo.lubis-luftbilder-dritte-firmen)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                                             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                               |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                                    |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Historical monuments' rocks <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke>`__ (ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke)             |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Subdivision special geological maps <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-spezialkarten_schweiz.metadata>`__ (ch.swisstopo.geologie-spezialkarten_schweiz.metadata)                     |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140319:

Release 20140319 -  Wednesday, March 19th 2014
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Minor bug fixes

`MAP <//map.geo.admin.ch>`__
''''''''''''''''''''''''''''

- Drawing tools!
- Catalog layer entries are now sorted alphabetically
- Cosmetic changes for several browsers
- Add ability to print out feature tree information
- Minor bug fixes

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road traffic noise (Lr_day) <//map.geo.admin.ch/?layers=ch.bafu.laerm-strassenlaerm_tag>`__ (ch.bafu.laerm-strassenlaerm_tag)                                                  |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (Lr_day) <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_tag>`__ (ch.bafu.laerm-bahnlaerm_tag)                                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (Lr_night) <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_nacht>`__ (ch.bafu.laerm-bahnlaerm_nacht)                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road traffic noise (Lr_night) <//map.geo.admin.ch/?layers=ch.bafu.laerm-strassenlaerm_nacht>`__ (ch.bafu.laerm-strassenlaerm_nacht)                                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PKD (proliferative kidney disease) <//map.geo.admin.ch/?layers=ch.bafu.fischerei-proliferative_nierenkrankheit>`__ (ch.bafu.fischerei-proliferative_nierenkrankheit)           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pollutant releases (SwissPRTR) <//map.geo.admin.ch/?layers=ch.bafu.swissprtr>`__ (ch.bafu.swissprtr)                                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140306:

Release 20140306 -  Thursday, March 6th 2014
--------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Adding support for internationalization of the client side
- Geo.admin.ch API RE3 is going out of beta

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeromagnetik <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz>`__ (ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz)     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Segelflugkarte Schweiz 1:300'000 <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Luftfahrtkarte ICAO Schweiz 1:500'000 <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Kulturgüterschutz Inventar <//map.geo.admin.ch/?layers=ch.babs.kulturgueter>`__ (ch.babs.kulturgueter)                                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140220:

Release 20140220 -  Thursday, February 20th 2014
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Various minor improvements and glitches

`map.geo.admin.ch <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''''''''''''''

- Add link to map in full screen
- Various minor fixes and improvements

.. _releasenotes_20140213:

Release 20140213 -  Thursday, February 13th 2014
------------------------------------------------

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Arealstatistik 2004/09 NOLU04 <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodennutzung>`__ (ch.bfs.arealstatistik-bodennutzung)                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Arealstatistik 1992/97 NOLU04 <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodennutzung-1997>`__ (ch.bfs.arealstatistik-bodennutzung-1997)                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Arealstatistik 1979/85 NOLU04 <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodennutzung-1985>`__ (ch.bfs.arealstatistik-bodennutzung-1985)                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140129:

Release 20140129 -  Wednesday, January 29th 2014
------------------------------------------------

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `WRZ Portal - Wege und Routen <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen-jagdbanngebiete-wege-routen>`__ (ch.bafu.wrz-wildruhezonen-jagdbanngebiete-wege-routen)     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Jagdbanngebiete - select <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Agricultural zones boundaries <//map.geo.admin.ch/?layers=ch.blw.landwirtschaftliche-zonengrenzen>`__ (ch.blw.landwirtschaftliche-zonengrenzen)                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20140115:

Release 20140115 -  Wednesday, January 15th 2014
------------------------------------------------

Geodata
********

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Safety zone plan <//map3.geo.admin.ch/?layers=ch.bazl.sicherheitszonenplan>`__  (ch.bazl.sicherheitszonenplan)                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Arealstatistik 2004/09 NOLC04 <//map3.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodenbedeckung>`__ (ch.bfs.arealstatistik-bodenbedeckung)                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Arealstatistik 1992/97 NOLC04 <//map3.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodenbedeckung-1997>`__ (ch.bfs.arealstatistik-bodenbedeckung-1997)                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Arealstatistik 1979/85 NOLC04 <//map3.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodenbedeckung-1985>`__ (ch.bfs.arealstatistik-bodenbedeckung-1985)                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division National Map 1:1 million (grey) <//map3.geo.admin.ch/?bgLayer=ch.swisstopo.pixelkarte-grau>`__ (ch.swisstopo.pixelkarte-grau)                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division National Map 1:1 million (color) <//map3.geo.admin.ch/?bgLayer=ch.swisstopo.pixelkarte-farbe>`__ (ch.swisstopo.pixelkarte-farbe)                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:1 million (colour) <//map3.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk1000.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk1000.noscale)                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:100'000 <//map3.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk100.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk100.noscale)                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:50'000 <//map3.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk50.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk50.noscale)                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National Map 1:25'000 <//map3.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-pk25.noscale>`__ (ch.swisstopo.pixelkarte-farbe-pk25.noscale)                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Listing all publicly available layers of the Geoadmin API: `List <//api3.geo.admin.ch/api/faq/index.html#which-layers-are-available>`__

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Documentation
- Support of HTTPS
- Various minor improvements and glitches

`map3.geo.admin.ch <//map3.geo.admin.ch>`__
'''''''''''''''''''''''''''''''''''''''''''

- Fix KML features reprojection
- Add WMS servers
- Add measure tool
- Add print area definition
- Adding graticule option to print
- Various minor fixes and improvements

.. _releasenotes_20131218:

Release 20131218 -  Wednesday, December 18th 2013
-------------------------------------------------

Geodata
********

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 50 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink50>`__ (ch.bakom.uplink50)                                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 20 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink20>`__ (ch.bakom.uplink20)                                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 2 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink2>`__ (ch.bakom.uplink2)                                                                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 100 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink100>`__ (ch.bakom.uplink100)                                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 10 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink10>`__ (ch.bakom.uplink10)                                                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Upload >= 1 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.uplink1>`__ (ch.bakom.uplink1)                                                                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability TV fixed network <//map3.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-tv>`__ (ch.bakom.verfuegbarkeit-tv)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Availability HDTV fixed netw. <//map3.geo.admin.ch/?layers=ch.bakom.verfuegbarkeit-hdtv>`__ (ch.bakom.verfuegbarkeit-hdtv)                                                                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Optical fibre <//map3.geo.admin.ch/?layers=ch.bakom.anschlussart-glasfaser>`__ (ch.bakom.anschlussart-glasfaser)                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 50 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink50>`__ (ch.bakom.downlink50)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 20 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink20>`__ (ch.bakom.downlink20)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 2 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink2>`__ (ch.bakom.downlink2)                                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 100 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink100>`__ (ch.bakom.downlink100)                                                                                                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 10 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink10>`__ (ch.bakom.downlink10)                                                                                                       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Download >= 1 Mbit/s <//map3.geo.admin.ch/?layers=ch.bakom.downlink1>`__ (ch.bakom.downlink1)                                                                                                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Copper wire <//map3.geo.admin.ch/?layers=ch.bakom.anschlussart-kupferdraht>`__ (ch.bakom.anschlussart-kupferdraht)                                                                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Coaxial cable <//map3.geo.admin.ch/?layers=ch.bakom.anschlussart-koaxialkabel>`__ (ch.bakom.anschlussart-koaxialkabel)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Number of connection providers <//map3.geo.admin.ch/?layers=ch.bakom.anbieter-eigenes_festnetz>`__ (ch.bakom.anbieter-eigenes_festnetz)                                                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Division gravimetric atlas 100 Paper <//map3.geo.admin.ch/?layers=ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata>`__  (ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata)       |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Listing all publicly available layers of the Geoadmin API :

- `List only <//s.geo.admin.ch/5d5d40a>`__
- `With Preview <//s.geo.admin.ch/ebae1145>`__

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Initial preview of the new GeoAdmin API
- Documentation
- Support of HTTPS
- Various minor improvements and glitches


`map3.geo.admin.ch <//map3.geo.admin.ch>`__
'''''''''''''''''''''''''''''''''''''''''''

- Fix KML features reprojection
- Add WMS servers
- Adding graticule option to print
- Various minor fixes and improvements


.. raw:: html

    <script>
        function relativeToAbsolute(relativeUrl) {
          var a = document.createElement('a');
            a.href = relativeUrl;
              return a.href;
              }
       var rss_url = relativeToAbsolute('rss2.xml').replace(/^http:\/\//i, 'https://');;

       setTimeout(function() {
       jQuery('<a>', {
           id: 'foo',
           href: "https://validator.w3.org/feed/check.cgi?url=" + rss_url,
           title: 'Validate my RSS feed',
           html: ' <img src="https://validator.w3.org/feed/images/valid-rss-rogers.png" alt="[Valid RSS]" title="Validate my RSS feed" />',
           alt: "[Valid RSS]"}).appendTo('#rss-feed');

       }, 1000)
    </script>
