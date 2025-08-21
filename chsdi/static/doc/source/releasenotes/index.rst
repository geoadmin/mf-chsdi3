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

.. _releasenotes_20250827:

Release 20250827 - Wednesday, August 27th 2025
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes:
- Announcements:
    - the layer *ch.bafu.gefahren-basiskarte* will be removed from chsdi services with the release of November 12th 2025
    - the layers *ch.bafu.karst-ausdehnung_grundwasservorkommen*, *ch.bafu.karst-einzugsgebiete*, *ch.bafu.karst-einzugsgebietseinheiten*, *ch.bafu.karst-quellen_schwinden* and *ch.bafu.karst-unterirdische_fliesswege* will be removed from chsdi services with the release of November 12th 2025
    - the layer *ch.swisstopo.schneeschuhwandern* will be removed from chsdi services with the release of November 2025 and replaced by a new layer
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with one of the next releases. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay.

- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2025-07-02-rc1...2025-08-27-rc1>`__

Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar: ratio worth examining <//map.geo.admin.ch/?layers=ch.are.solaranlagen-pruefenswerte_gebiete>`__ (ch.are.solaranlagen-pruefenswerte_gebiete)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar: areas worth examining <//map.geo.admin.ch/?layers=ch.are.solaranlagen-pruefenswerte_gebiete_vektor>`__ (ch.are.solaranlagen-pruefenswerte_gebiete_vektor)                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar: aspects of use <//map.geo.admin.ch/?layers=ch.are.solaranlagen-nutzungsaspekte>`__ (ch.are.solaranlagen-nutzungsaspekte)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar: protection interests <//map.geo.admin.ch/?layers=ch.are.solaranlagen-schutzinteressen>`__ (ch.are.solaranlagen-schutzinteressen)                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Top OMM <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol_hoehe_top_omm>`__ (ch.swisstopo.geologie-geomol_hoehe_top_omm)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Top OMM - Data <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geomol_hoehe_top_omm_data>`__ (ch.swisstopo.geologie-geomol_hoehe_top_omm_data)                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cities and conurbations BeSA <//map.geo.admin.ch/?layers=ch.are.agglomerationsverkehr>`__ (ch.are.agglomerationsverkehr)                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Passenger traffic (public transport) <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-bahn>`__ (ch.are.belastung-personenverkehr-bahn)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Passenger traffic <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-strasse>`__ (ch.are.belastung-personenverkehr-strasse)                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Travel time to agglos by road <//map.geo.admin.ch/?layers=ch.are.reisezeit-agglomerationen-miv>`__ (ch.are.reisezeit-agglomerationen-miv)                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Travel time to agglos by PT <//map.geo.admin.ch/?layers=ch.are.reisezeit-agglomerationen-oev>`__ (ch.are.reisezeit-agglomerationen-oev)                                                                       |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Travel time to centres by PT <//map.geo.admin.ch/?layers=ch.are.reisezeit-oev>`__ (ch.are.reisezeit-oev)                                                                                                      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Travel time to centres by road <//map.geo.admin.ch/?layers=ch.are.reisezeit-miv>`__ (ch.are.reisezeit-miv)                                                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hospital landing sites  <//map.geo.admin.ch?layers=ch.bazl.spitallandeplaetze>`__ (ch.bazl.spitallandeplaetze)                                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Meat products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cheese <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Confectionery <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-konditoreiwaren>`__ (ch.blw.ursprungsbezeichnungen-konditoreiwaren)                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Plant products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-pflanzen>`__ (ch.blw.ursprungsbezeichnungen-pflanzen)                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spirits <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-spirituosen>`__ (ch.blw.ursprungsbezeichnungen-spirituosen)                                                                                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Sectoral plan CERN consultation <//map.geo.admin.ch/?layers=ch.sbfi.sachplan-cern_anhoerung>`__ (ch.sbfi.sachplan-cern_anhoerung)                                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Reflection seismic <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-reflexionsseismik>`__ (ch.swisstopo.geologie-reflexionsseismik)                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20250702:

Release 20250702 - Wednesday, July 2nd 2025
-------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes:
- Announcements:
    - the layers *ch.are.gemeindetypen*, *ch.are.belastung-gueterverkehr-bahn* and *ch.are.belastung-gueterverkehr-strasse* have been decommissioned as previously announced.
    - the layers *ch.bafu.hydrologie-hintergrundkarte* and *ch.bafu.hydrologie-hochwassergrenzwertpegel* have been decommissioned as previously announced.
    - the layer *ch.bfs.arealstatistik-waldmischungsgrad* has been decommissioned as previously announced.
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with one of the next releases. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay.


- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2025-05-15-rc1...2025-07-02-rc1>`__

Geodata
*******

+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Organische Böden CH 2024 <//map.geo.admin.ch/?layers=ch.agroscope.abschaetzung-organische_boeden>`__ (ch.agroscope.abschaetzung-organische_boeden)                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Labour market areas and large labour market areas <//map.geo.admin.ch/?layers=ch.bfs.arbeitsmarktregionen>`__ (ch.bfs.arbeitsmarktregionen)                                                                   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Focus map agri-environmental objective birds <//map.geo.admin.ch/?layers=ch.agroscope.fokuskarte-voegel>`__ (ch.agroscope.fokuskarte-voegel)                                                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Suitability of terrestrial habitat for amphibians <//map.geo.admin.ch/?layers=ch.agroscope.amphibien-bedeutung_parzellen>`__ (ch.agroscope.amphibien-bedeutung_parzellen)                                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Dispersal map Alytes obstericans <//map.geo.admin.ch/?layers=ch.agroscope.amphibien-ausbreitungskarten_alytes_obstetricans>`__ (ch.agroscope.amphibien-ausbreitungskarten_alytes_obstetricans)                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Dispersal map Bombia variegata <//map.geo.admin.ch/?layers=ch.agroscope.amphibien-ausbreitungskarten_bombia_variegata>`__ (ch.agroscope.amphibien-ausbreitungskarten_bombia_variegata)                        |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Dispersal map Epidalea calamita <//map.geo.admin.ch/?layers=ch.agroscope.amphibien-ausbreitungskarten_epidalea_calamita>`__ (ch.agroscope.amphibien-ausbreitungskarten_epidalea_calamita)                     |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Dispersal map Hyla arborea <//map.geo.admin.ch/?layers=ch.agroscope.amphibien-ausbreitungskarten_hyla_arborea>`__ (ch.agroscope.amphibien-ausbreitungskarten_hyla_arborea)                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Dispersal map Triturus cristatus <//map.geo.admin.ch/?layers=ch.agroscope.amphibien-ausbreitungskarten_triturus_cristatus>`__ (ch.agroscope.amphibien-ausbreitungskarten_triturus_cristatus)                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lr <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde)           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 1st night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt)                 |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. helicopters Lmax <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde)         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light / large aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge)  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. milit. aerodr. (tot.) <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge)|
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. light aircrafts <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter)                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. 2nd night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde)             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Noise exp. last night hour <//map.geo.admin.ch/?layers=ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel>`__ (ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel)|
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Daytime railway noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_tag>`__ (ch.bafu.laerm-bahnlaerm_tag)                                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nighttime railway noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-bahnlaerm_nacht>`__ (ch.bafu.laerm-bahnlaerm_nacht)                                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Daytime road noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-strassenlaerm_tag>`__ (ch.bafu.laerm-strassenlaerm_tag)                                                                                          |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nighttime road noise <//map.geo.admin.ch/?layers=ch.bafu.laerm-strassenlaerm_nacht>`__ (ch.bafu.laerm-strassenlaerm_nacht)                                                                                    |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Deep wells <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                                            |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPA consultation <//map.geo.admin.ch/?layers=ch.sem.sachplan-asyl_anhoerung>`__ (ch.sem.sachplan-asyl_anhoerung)                                                                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Unterirdischer Gütertransport <//map.geo.admin.ch/?layers=ch.bav.sachplan-unterirdischer-guetertransport_kraft>`__ (ch.bav.sachplan-unterirdischer-guetertransport_kraft)                                  |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SUG Anhörung <//map.geo.admin.ch/?layers=ch.bav.sachplan-unterirdischer-guetertransport_anhoerung>`__ (ch.bav.sachplan-unterirdischer-guetertransport_anhoerung)                                              |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Jagdbanngebiete <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-jagdbanngebiete>`__ (ch.bafu.bundesinventare-jagdbanngebiete)                                                                             |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTIRegio monodirectional hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissaltiregio-reliefschattierung_monodirektional>`__ (ch.swisstopo.swissaltiregio-reliefschattierung_monodirektional)      |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTIRegio multidirectional hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissaltiregio-reliefschattierung_multidirektional>`__ (ch.swisstopo.swissaltiregio-reliefschattierung_multidirektional)   |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Thermal waters <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-thermale_waesser>`__ (ch.swisstopo.geologie-thermale_waesser)                                                                                |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                               |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Slope over 30 degrees <//map.geo.admin.ch/?layers=ch.swisstopo-karto.hangneigung>`__ (ch.swisstopo-karto.hangneigung)                                                                                         |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Slope classes over 30 degrees <//map.geo.admin.ch/?layers=ch.swisstopo.hangneigung-ueber_30>`__ (ch.swisstopo.hangneigung-ueber_30)                                                                           |
+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20250514:

Release 20250514 - Wednesday, Mai 14th 2025
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
    - Removed duplicate `cache-control` header `max-age` from WMS responses.
- Announcements:
    - the layers *ch.are.gemeindetypen*, *ch.are.belastung-gueterverkehr-bahn* and *ch.are.belastung-gueterverkehr-strasse* will be removed from chsdi services with the release of July 2nd 2025.
    - the layers *ch.bafu.hydrologie-hintergrundkarte* and *ch.bafu.hydrologie-hochwassergrenzwertpegel* will be removed from chsdi services with the release of July 2nd 2025.
    - the layer *ch.bfs.arealstatistik-waldmischungsgrad* will be removed from chsdi services with the release of July 2nd 2025.
    - the GetCapabilities document of wms.geo.admin.ch now includes direct links to geocat.ch metadata for each available geodata layer.
    - the layer ch.swisstopo.swissimage-product now supports transparency and is available as PNG tiles in the WMTS service.
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with one of the next releases. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay.


- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2025-03-12-rc1...2025-05-14-rc1>`__

Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissEO VHI vegetation <//map.geo.admin.ch/?layers=ch.swisstopo.swisseo_vhi_v100_vegetation>`__ (ch.swisstopo.swisseo_vhi_v100_vegetation)                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Territorial Limit AV <//map.geo.admin.ch/?layers=ch.swisstopo.hoheitsgrenze-landesvermessung>`__ (ch.swisstopo.hoheitsgrenze-landesvermessung)                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Points Territorial Limit AV <//map.geo.admin.ch/?layers=ch.swisstopo.hoheitsgrenzpunkte-landesvermessung>`__ (ch.swisstopo.hoheitsgrenzpunkte-landesvermessung)                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vegetation height model Lidar NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell_lidar>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell_lidar)                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vegetation height model Sentinel NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell_sentinel>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell_sentinel)            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Relief shading Sentinel NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell_relief_sentinel>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell_relief_sentinel)       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Drought warning map <//map.geo.admin.ch/?layers=ch.bafu.trockenheitswarnkarte>`__ (ch.bafu.trockenheitswarnkarte)                                                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `142 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-142_zentral>`__ (ch.bakom.notruf-142_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `142 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-142_festnetz>`__ (ch.bakom.notruf-142_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `142 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-142_mobilnetz>`__ (ch.bakom.notruf-142_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway lines MAO <//map.geo.admin.ch/?layers=ch.bav.lage-stoerfallverordnung_eisenbahnanlagen>`__ (ch.bav.lage-stoerfallverordnung_eisenbahnanlagen)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Interregional wildlife corridor <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierkorridor_national>`__ (ch.bafu.fauna-wildtierkorridor_national)                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Radon map <//map.geo.admin.ch/?layers=ch.bag.radonkarte>`__ (ch.bag.radonkarte)                                                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Future mean runoff (m³/s) and regime <//map.geo.admin.ch/?layers=ch.bafu.mittlere-abfluesse_zukunft>`__ (ch.bafu.mittlere-abfluesse_zukunft)                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Status of cadastral surveying <//map.geo.admin.ch/?layers=ch.swisstopo-vd.geometa-standav>`__ (ch.swisstopo-vd.geometa-standav)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Periodic updating (Cadastral Surveying Switzerland) <//map.geo.admin.ch/?layers=ch.swisstopo-vd.geometa-periodische_nachfuehrung>`__ (ch.swisstopo-vd.geometa-periodische_nachfuehrung)                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Gypsum <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung>`__ (ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Residential areas according to AuLaV <//map.geo.admin.ch/?layers=ch.bazl.wohngebiete-aulav>`__ (ch.bazl.wohngebiete-aulav)                                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Landwirtschaftliche Nutzungsflächen Schweiz <//map.geo.admin.ch/?layers=ch.blw.landwirtschaftliche-nutzungsflaechen>`__ (ch.blw.landwirtschaftliche-nutzungsflaechen)                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Basic statistical units level 1 <//map.geo.admin.ch/?layers=ch.bfs.statistische-grundeinheiten_stufe1>`__ (ch.bfs.statistische-grundeinheiten_stufe1)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Basic statistical units level 2 <//map.geo.admin.ch/?layers=ch.bfs.statistische-grundeinheiten_stufe2>`__ (ch.bfs.statistische-grundeinheiten_stufe2)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surveyed sections <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cross section securing point <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Deep geothermal projects <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tiefengeothermie_projekte>`__ (ch.swisstopo.geologie-tiefengeothermie_projekte)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spitallandeplätze <//map.geo.admin.ch?layers=ch.bazl.spitallandeplaetze>`__ (ch.bazl.spitallandeplaetze)                                                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Built-up areas VIL <//map.geo.admin.ch/?layers=ch.bazl.bebaute-gebiete_luftfahrtrecht>`__ (ch.bazl.bebaute-gebiete_luftfahrtrecht)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Control zones - CTR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollzonen>`__ (ch.bazl.luftraeume-kontrollzonen)                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Control areas - CTA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollbezirke>`__ (ch.bazl.luftraeume-kontrollbezirke)                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Flight information region - FIR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationsgebiet>`__ (ch.bazl.luftraeume-fluginformationsgebiet)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Flight information zones - FIZ <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationszonen>`__ (ch.bazl.luftraeume-fluginformationszonen)                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Terminal control areas - TMA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-nahkontrollbezirke>`__ (ch.bazl.luftraeume-nahkontrollbezirke)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of restricted and danger areas <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISS MIL PILOTS CHART <//map.geo.admin.ch/?layers=ch.vbs.swissmilpilotschart>`__ (ch.vbs.swissmilpilotschart)                                                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ISOS - Site records <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder)                                                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ISOS - Photos <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos)                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PCP Inventory <//map.geo.admin.ch/?layers=ch.babs.kulturgueter>`__ (ch.babs.kulturgueter)                                                                                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vegetation height model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell)                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surface model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell_relief>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell_relief)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest mix rate NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-waldmischungsgrad>`__ (ch.bafu.landesforstinventar-waldmischungsgrad)                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_zentral>`__ (ch.bakom.notruf-112_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_zentral>`__ (ch.bakom.notruf-117_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_zentral>`__ (ch.bakom.notruf-118_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_zentral>`__ (ch.bakom.notruf-143_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_zentral>`__ (ch.bakom.notruf-144_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `145 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_zentral>`__ (ch.bakom.notruf-145_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_zentral>`__ (ch.bakom.notruf-147_zentral)                                                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_festnetz>`__ (ch.bakom.notruf-117_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_festnetz>`__ (ch.bakom.notruf-143_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_festnetz>`__ (ch.bakom.notruf-144_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `145 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_festnetz>`__ (ch.bakom.notruf-145_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_festnetz>`__ (ch.bakom.notruf-147_festnetz)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_mobilnetz>`__ (ch.bakom.notruf-117_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_mobilnetz>`__ (ch.bakom.notruf-143_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_mobilnetz>`__ (ch.bakom.notruf-144_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `145 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_mobilnetz>`__ (ch.bakom.notruf-145_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_mobilnetz>`__ (ch.bakom.notruf-147_mobilnetz)                                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Sports facilities CSFNI <//map.geo.admin.ch/?layers=ch.baspo.nationales-sportanlagenkonzept>`__ (ch.baspo.nationales-sportanlagenkonzept)                                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20250312:

Release 20250312 - Wednesday, March 12th 2025
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with one of the next releases. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay.


- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2025-02-05-rc1...2025-03-12-rc1>`__

Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air pollution by Ozone <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-ozon>`__ (ch.bafu.luftreinhaltung-ozon)                                                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air pollution by particulate matter PM2.5 <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-feinstaub_pm2_5>`__ (ch.bafu.luftreinhaltung-feinstaub_pm2_5)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air pollution by particulate matter PM10 <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-feinstaub_pm10>`__ (ch.bafu.luftreinhaltung-feinstaub_pm10)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air pollution by sulfur dioxide <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-schwefeldioxid>`__ (ch.bafu.luftreinhaltung-schwefeldioxid)                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air pollution by nitrogen dioxide <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-stickstoffdioxid>`__ (ch.bafu.luftreinhaltung-stickstoffdioxid)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Area of consultation of national routes <//map.geo.admin.ch/?layers=ch.astra.konsultationsbereiche-nationalstrassen>`__ (ch.astra.konsultationsbereiche-nationalstrassen)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Current drought situation in Switzerland <//map.geo.admin.ch/?layers=ch.bafu.trockenheitsindex>`__ (ch.bafu.trockenheitsindex)                                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents in the annual comparison <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_jahresvergleich>`__ (ch.astra.schwerverunfallte-kanton_jahresvergleich)                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `NLA Natural values / habitats <//map.geo.admin.ch/?layers=ch.armasuisse.natur-landschaft_armee>`__ (ch.armasuisse.natur-landschaft_armee)                                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Reflection seismic <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-reflexionsseismik>`__ (ch.swisstopo.geologie-reflexionsseismik)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Gypsum <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung>`__ (ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wald>`__ (ch.swisstopo.swisstlm3d-wald)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional)    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional) |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tank relocation routes <//map.geo.admin.ch/?layers=ch.vbs.panzerverschiebungsrouten>`__ (ch.vbs.panzerverschiebungsrouten)                                                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Status of cadastral surveying <//map.geo.admin.ch/?layers=ch.swisstopo-vd.geometa-standav>`__ (ch.swisstopo-vd.geometa-standav)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Periodic updating (Cadastral Surveying Switzerland) <//map.geo.admin.ch/?layers=ch.swisstopo-vd.geometa-periodische_nachfuehrung>`__ (ch.swisstopo-vd.geometa-periodische_nachfuehrung)                     |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Official street index <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-strassenverzeichnis>`__ (ch.swisstopo.amtliches-strassenverzeichnis)                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Official directory of building addresses <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis>`__ (ch.swisstopo.amtliches-gebaeudeadressverzeichnis)                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20250205:

Release 20250205 - Wednesday, February 5th 2025
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with one of the next releases. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay.
    - the layer *ch.are.siedlung* has been corrected. In the production of the data published on November 15th 2024, the ARE had made a mistake in the process, which attributed areas to the settlement that were not correct. The geocommunity noticed this anomaly and helped to ensure that the process and the data could be corrected.
    - the layer *ch.bakom.notruf-112_satellit* has been decommissioned as previously announced.


- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2024-12-18-rc1...2025-02-05-rc1>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey through time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product>`__ (ch.swisstopo.swissimage-product)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Settlement <//map.geo.admin.ch/?layers=ch.are.siedlung>`__ (ch.are.siedlung)                                                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tracer tests <//map.geo.admin.ch/?layers=ch.bafu.hydrogeologie-markierversuche>`__ (ch.bafu.hydrogeologie-markierversuche)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Biological Water Status: Diatomeen <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen)                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Biological Water Status: Fische <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_fische>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_fische)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Biological Water Status: Macrophyten <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten)             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Biological Water Status: Macrozoobenthos <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos>`__ (ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos) |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Chemical Water Status: Nitrate <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_nitrat>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_nitrat)                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Chemical Water Status: Nitrite <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_nitrit>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_nitrit)                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Chemical Water Status: DOC <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_doc>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_doc)                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Chemical Water Status: Total phosphorus <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt)      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Chemical Water Status: Phosphat <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_phosphat>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_phosphat)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Assessment of the Chemical Water Status: Ammonium <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-chemischer_zustand_ammonium>`__ (ch.bafu.gewaesserschutz-chemischer_zustand_ammonium)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency meeting points <//map.geo.admin.ch/?layers=ch.babs.notfalltreffpunkte>`__ (ch.babs.notfalltreffpunkte)                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `UNESCO World cultural heritage <//map.geo.admin.ch/?layers=ch.bak.schutzgebiete-unesco_weltkulturerbe>`__ (ch.bak.schutzgebiete-unesco_weltkulturerbe)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20241218:

Release 20241218 - Wednesday, December 18th 2024
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with one of the next releases in 2025. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay
    - decommission of various vectortile styles and datasets by January 2025. Details `read here <https://www.geo.admin.ch/en/old-styles-no-longer-available-from-january-2025>`__
    - the layer *ch.bakom.notruf-112_satellit* will be decommissioned with the release of February 5th 2025
    - the fuzzy search behaviour of swisssearch will be changed. the new quorum operator will be used for the fuzzy search. this operator adds an additional fuzziness on the whole search string. the fuzzy search will therefore return more results than before when searching for multiple keywords.


- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2024-11-13-rc1...2024-12-18-rc1>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Residential areas according to AuLaV <//map.geo.admin.ch/?layers=ch.bazl.wohngebiete-aulav>`__ (ch.bazl.wohngebiete-aulav)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spitallandeplätze <//map.geo.admin.ch?layers=ch.bazl.spitallandeplaetze>`__ (ch.bazl.spitallandeplaetze)                                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Groundwater level/spring discharge <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_grundwasserzustand>`__ (ch.bafu.hydroweb-messstationen_grundwasserzustand)                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Sectoral plan CERN consultation <//map.geo.admin.ch/?layers=ch.sbfi.sachplan-cern_anhoerung>`__ (ch.sbfi.sachplan-cern_anhoerung)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Habitat Map <//map.geo.admin.ch/?layers=ch.bafu.lebensraumkarte-schweiz>`__ (ch.bafu.lebensraumkarte-schweiz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways/skilifts winter <//map.geo.admin.ch/?layers=ch.swisstopo.bahnen-winter>`__ (ch.swisstopo.bahnen-winter)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accommodations winter <//map.geo.admin.ch/?layers=ch.swisstopo.unterkuenfte-winter>`__ (ch.swisstopo.unterkuenfte-winter)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-schneeschuhrouten)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Zones) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                                                    |
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

.. _releasenotes_20241113:

Release 20241113 - Wednesday, November 13th 2024
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the layers *ch.swisstopo-karto.skitouren* and *ch.swisstopo-karto.schneeschuhrouten* have been switched from raster to vector datasets as previously announced
    - the layers *ch.swisstopo.lubis-luftbilder_schwarzweiss*, *ch.swisstopo.lubis-luftbilder_farbe*, *ch.swisstopo.lubis-luftbilder_infrarot* got the following changes as previously announced: no extended tooltip anymore and the attributes inventarnummer, bildnummer, orientierung, rotation, filesize_mb, ort, image_height and image_width have been removed
    - the layer *ch.swisstopo.lubis-luftbilder_schraegaufnahmen* got the following changes as previously announced: no extended tooltip anymore and the attributes inventory_number, medium_format, filesize_mb, contact and contact_email have been removed
    - the layer *ch.swisstopo.lubis-terrestrische_aufnahmen* got the following changes: no extended tooltip anymore and the attributes image_number, filesize_mb, medium_format, image_height and image_width have been removed
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with the release December 18th. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay
    - decommission of various vectortile styles and datasets by January 2025. Details `read here <https://www.geo.admin.ch/en/old-styles-no-longer-available-from-january-2025>`__
    - the layer *ch.bakom.notruf-112_satellit* will be decommissioned with the release of February 5th 2025


- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2024-10-09-rc1...2024-11-13-rc1>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Settlement <//map.geo.admin.ch/?layers=ch.are.siedlung>`__ (ch.are.siedlung)                                                                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reflective surfaces aerodromes <//map.geo.admin.ch/?layers=ch.bazl.reflektierende-flaechen_flugplaetze>`__ (ch.bazl.reflektierende-flaechen_flugplaetze)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Snow depth, 10 min <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-schneehoehe-automatisch-10min>`__ (ch.meteoschweiz.messwerte-schneehoehe-automatisch-10min)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Sectoral plan CERN consultation <//map.geo.admin.ch/?layers=ch.sbfi.sachplan-cern_anhoerung>`__ (ch.sbfi.sachplan-cern_anhoerung)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Cableways/skilifts winter <//map.geo.admin.ch/?layers=ch.swisstopo.bahnen-winter>`__ (ch.swisstopo.bahnen-winter)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Thermal waters <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-thermale_waesser>`__ (ch.swisstopo.geologie-thermale_waesser)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accommodations winter <//map.geo.admin.ch/?layers=ch.swisstopo.unterkuenfte-winter>`__ (ch.swisstopo.unterkuenfte-winter)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-schneeschuhrouten)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Winter national map <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-winter>`__ (ch.swisstopo.pixelkarte-farbe-winter)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Housing Inventory <//map.geo.admin.ch/?layers=ch.are.wohnungsinventar-zweitwohnungsanteil>`__ (ch.are.wohnungsinventar-zweitwohnungsanteil)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nitrogen Deposition <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-stickstoffdeposition>`__ (ch.bafu.luftreinhaltung-stickstoffdeposition)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ammonia Concentration <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-ammoniakkonzentration>`__ (ch.bafu.luftreinhaltung-ammoniakkonzentration)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissEO VHI <//map.geo.admin.ch/?layers=ch.swisstopo.swisseo_vhi_v100>`__ (ch.swisstopo.swisseo_vhi_v100)                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_zentral>`__ (ch.bakom.notruf-112_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_zentral>`__ (ch.bakom.notruf-117_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_zentral>`__ (ch.bakom.notruf-118_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_zentral>`__ (ch.bakom.notruf-143_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_zentral>`__ (ch.bakom.notruf-144_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `145 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_zentral>`__ (ch.bakom.notruf-145_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_zentral>`__ (ch.bakom.notruf-147_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Deep geothermal projects <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tiefengeothermie_projekte>`__ (ch.swisstopo.geologie-tiefengeothermie_projekte)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20241009:

Release 20241009 - Wednesday, October 9th 2024
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the layers *ch.swisstopo.geologie-geotechnik-steinbrueche_1915*, *ch.swisstopo.geologie-geotechnik-steinbrueche_1965*, *ch.swisstopo.geologie-geotechnik-steinbrueche_1995* and *ch.swisstopo.geologie-geotechnik-steinbrueche_1980* have been removed from chsdi services as previously announced
    - by the release of November 13th or December 18th the layers *ch.swisstopo-karto.skitouren* and *ch.swisstopo-karto.schneeschuhrouten* will no longer be raster maps but vector data sets
    - important information about SSL certificates and http protocol for integrated symbols, KML’s or GPX files in map.geo.admin.ch. Details `read here <https://www.geo.admin.ch/en/important-imformation-ssl-certificates-http-protocols>`__
    - the layers *ch.swisstopo.lubis-luftbilder_schwarzweiss*, *ch.swisstopo.lubis-luftbilder_farbe*, *ch.swisstopo.lubis-luftbilder_infrarot* will get the following changes by the release of November 13th: no extended tooltip anymore and the attributes inventarnummer, bildnummer, orientierung, rotation, filesize_mb, ort, image_height and image_width will be removed from chsdi services, because they are no longer filled and used.
    - the layer *ch.swisstopo.lubis-luftbilder_schraegaufnahmen* will get the following changes by the release of November 13th: no extended tooltip anymore and the attributes inventory_number, medium_format, filesize_mb, contact and contact_email will be removed from chsdi services, because they are no longer filled and used.
    - the layer *ch.swisstopo.lubis-terrestrische_aufnahmen* will get the following changes by the release of November 13th: no extended tooltip anymore and the attributes image_number, filesize_mb, medium_format, image_height and image_width will be removed from chsdi services, because they are no longer filled and used.
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with the release of November 13th or December 18th. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id’s (chsdi fields featureId and id). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay.
    - decommission of various vectortile styles and datasets by January 2025. Details `read here <https://www.geo.admin.ch/en/old-styles-no-longer-available-from-january-2025>`__
    - the layer *ch.bakom.notruf-112_satellit* will be decommissioned with one of the first releases in 2025


- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2024-08-28-rc1...2024-10-09-rc1>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Emergency meeting points <//map.geo.admin.ch/?layers=ch.babs.notfalltreffpunkte>`__ (ch.babs.notfalltreffpunkte)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amphibian migration conflicts <//map.geo.admin.ch/?layers=ch.bafu.amphibienwanderung-verkehrskonflikte>`__ (ch.bafu.amphibienwanderung-verkehrskonflikte)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vegetation height model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surface model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell_relief>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell_relief)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `CLN Exceedance <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-stickstoff_kritischer_eintrag>`__ (ch.bafu.luftreinhaltung-stickstoff_kritischer_eintrag)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Plug-in vehicles <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-fahrzeuge>`__ (ch.bfe.ladebedarfswelt-fahrzeuge)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Home charging availability - Convenient <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem>`__ (ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem)       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Home charging availability - Flexible <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_flexibel>`__ (ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_flexibel)     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Home charging availability - Planned <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_geplant>`__ (ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_geplant)        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Charging points - Convenient <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_bequem>`__ (ch.bfe.ladebedarfswelt-ladepunkte_bequem)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Charging points - Flexible <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_felxibel>`__ (ch.bfe.ladebedarfswelt-ladepunkte_felxibel)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Charging points - Planned <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_geplant>`__ (ch.bfe.ladebedarfswelt-ladepunkte_geplant)                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Power requirements <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-strombedarf>`__ (ch.bfe.ladebedarfswelt-strombedarf)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land use statistics standard <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik>`__ (ch.bfs.arealstatistik)                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land use statistics cover <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodenbedeckung>`__ (ch.bfs.arealstatistik-bodenbedeckung)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Enterprises <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dwellings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Buildings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Population (residents) <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner>`__ (ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Landwirtschaftliche Nutzungsflächen Schweiz <//map.geo.admin.ch/?layers=ch.blw.landwirtschaftliche-nutzungsflaechen>`__ (ch.blw.landwirtschaftliche-nutzungsflaechen)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected Areas swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-adminboundaries-protectedarea>`__ (ch.swisstopo.vec200-adminboundaries-protectedarea)                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Single objects swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous>`__ (ch.swisstopo.vec200-miscellaneous)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Elevations swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-miscellaneous-geodpoint>`__ (ch.swisstopo.vec200-miscellaneous-geodpoint)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Names swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-names-namedlocation>`__ (ch.swisstopo.vec200-names-namedlocation)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transportation swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-oeffentliche-verkehr>`__ (ch.swisstopo.vec200-transportation-oeffentliche-verkehr)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road system swissTLMregio <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-transportation-strassennetz>`__ (ch.swisstopo.vec200-transportation-strassennetz)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey through time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product>`__ (ch.swisstopo.swissimage-product)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division SWISSIMAGE 10 cm Raster <//map.geo.admin.ch/?layers=ch.swisstopo.images-swissimage-dop10.metadata>`__ (ch.swisstopo.images-swissimage-dop10.metadata)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata>`__ (ch.swisstopo.swissimage-product.metadata)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20240828:

Release 20240828 - Wednesday, August 28th 2024
----------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the layer *ch.swisstopo.geologie-geologischer_atlas_vector.metadata* has been removed from chsdi services as previously announced
    - the layers *ch.swisstopo.geologie-geotechnik-steinbrueche_1915*, *ch.swisstopo.geologie-geotechnik-steinbrueche_1965*, *ch.swisstopo.geologie-geotechnik-steinbrueche_1995* and *ch.swisstopo.geologie-geotechnik-steinbrueche_1980* will be removed from chsdi services with the release of October 9th 2024
    - the object ID values of the layer *ch.vbs.schiessanzeigen* will change for all objects due to geometrical changes in the source data with the release of October 9th or November 13th 2024. Existing permalinks to objects may not work anymore and will have to be replaced by the new object id's (chsdi fields *featureId* and *id*). In addition there will be a new attribute bezeichnung_ort on the dataset. The other existing attributes will stay.
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2024-07-03-rc1...2024-08-28-rc1>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Basic statistical units level 1 <//map.geo.admin.ch/?layers=ch.bfs.statistische-grundeinheiten_stufe1>`__ (ch.bfs.statistische-grundeinheiten_stufe1)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Basic statistical units level 2 <//map.geo.admin.ch/?layers=ch.bfs.statistische-grundeinheiten_stufe2>`__ (ch.bfs.statistische-grundeinheiten_stufe2)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Civil aerodromes businesses - MAO <//map.geo.admin.ch/?layers=ch.bazl.betriebe-stoerfallverordnung-zivilflugplaetze>`__ (ch.bazl.betriebe-stoerfallverordnung-zivilflugplaetze)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Landwirtschaftliche Nutzungsflächen Schweiz <//map.geo.admin.ch/?layers=ch.blw.landwirtschaftliche-nutzungsflaechen>`__ (ch.blw.landwirtschaftliche-nutzungsflaechen)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: Side of tick bite reported <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: recommendation of vaccination <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-impfung>`__ (ch.bag.zecken-fsme-impfung)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Sectoral Plan Deep Geological Repositories <//map.geo.admin.ch/?layers=ch.bfe.sachplan-geologie-tiefenlager>`__ (ch.bfe.sachplan-geologie-tiefenlager)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surveyed sections <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cross section securing point <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20240703:

Release 20240703 - Wednesday, July 3rd 2024
-------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the layer *ch.swisstopo.geologie-geologischer_atlas_vector.metadata* will be removed from chsdi services with the release of August 28th 2024
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2024-05-15-rc1...2024-07-03-rc1>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hard rock aggregates: Production and mining sites of the hard rock industry <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-hartsteinabbau>`__ (ch.swisstopo.geologie-hartsteinabbau)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hard rock aggregates: Thickness and quality of geological occurrences <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-hartsteinvorkommen>`__ (ch.swisstopo.geologie-hartsteinvorkommen)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging stations of the Federal Administration <//map.geo.admin.ch/?layers=ch.vbs.ladestationen>`__ (ch.vbs.ladestationen)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations - principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung-uebergeordnet)                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alps with livestock guardian dogs <//map.geo.admin.ch/?layers=ch.bafu.alpweiden-herdenschutzhunde>`__ (ch.bafu.alpweiden-herdenschutzhunde)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Flussgebiete (Einzugsgebiete) HADES <//map.geo.admin.ch/?layers=ch.bafu.hydrologischer-atlas_flussgebiete>`__ (ch.bafu.hydrologischer-atlas_flussgebiete)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrological gauging stations <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hydromessstationen>`__ (ch.bafu.hydrologie-hydromessstationen)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Area outlets <//map.geo.admin.ch/?layers=ch.bafu.wasser-gebietsauslaesse>`__ (ch.bafu.wasser-gebietsauslaesse)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `2km2 sub catchment areas <//map.geo.admin.ch/?layers=ch.bafu.wasser-teileinzugsgebiete_2>`__ (ch.bafu.wasser-teileinzugsgebiete_2)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `40km2 sub catchment areas <//map.geo.admin.ch/?layers=ch.bafu.wasser-teileinzugsgebiete_40>`__ (ch.bafu.wasser-teileinzugsgebiete_40)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Type of flow regime <//map.geo.admin.ch/?layers=ch.bafu.wasser-vorfluter>`__ (ch.bafu.wasser-vorfluter)                                                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_festnetz>`__ (ch.bakom.notruf-117_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_festnetz>`__ (ch.bakom.notruf-143_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_festnetz>`__ (ch.bakom.notruf-144_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `145 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_festnetz>`__ (ch.bakom.notruf-145_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_festnetz>`__ (ch.bakom.notruf-147_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_mobilnetz>`__ (ch.bakom.notruf-117_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_mobilnetz>`__ (ch.bakom.notruf-143_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_mobilnetz>`__ (ch.bakom.notruf-144_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `145 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_mobilnetz>`__ (ch.bakom.notruf-145_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_mobilnetz>`__ (ch.bakom.notruf-147_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Sanctuaries for silence and nature for aviation <//map.geo.admin.ch/?layers=ch.bazl.landschaftsruhezonen>`__ (ch.bazl.landschaftsruhezonen)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Charging points - Convenient <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_bequem>`__ (ch.bfe.ladebedarfswelt-ladepunkte_bequem)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Charging points - Flexible <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_felxibel>`__ (ch.bfe.ladebedarfswelt-ladepunkte_felxibel)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging requirements: Charging points - Planned <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_geplant>`__ (ch.bfe.ladebedarfswelt-ladepunkte_geplant)                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land use statistics standard <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik>`__ (ch.bfs.arealstatistik)                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land use statistics cover <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodenbedeckung>`__ (ch.bfs.arealstatistik-bodenbedeckung)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accessibility of pharmacies <//map.geo.admin.ch/?layers=ch.bfs.erreichbarkeit-apotheken>`__ (ch.bfs.erreichbarkeit-apotheken)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accessibility of restaurants <//map.geo.admin.ch/?layers=ch.bfs.erreichbarkeit-restaurants>`__ (ch.bfs.erreichbarkeit-restaurants)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geothermal potential studies <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geothermische_potenzialstudien_regional>`__ (ch.swisstopo.geologie-geothermische_potenzialstudien_regional)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Crushed-rock aggregates <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau>`__ (ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau)                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `The Tectonic Map of Switzerland (GK500-Tekto) <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tektonische_karte>`__ (ch.swisstopo.geologie-tektonische_karte)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Deep geothermal projects <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tiefengeothermie_projekte>`__ (ch.swisstopo.geologie-tiefengeothermie_projekte)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Army logistics centre logistics areas <//map.geo.admin.ch/?layers=ch.vbs.logistikraeume-armeelogistikcenter>`__ (ch.vbs.logistikraeume-armeelogistikcenter)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Arsenals <//map.geo.admin.ch/?layers=ch.vbs.retablierungsstellen>`__ (ch.vbs.retablierungsstellen)                                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



.. _releasenotes_20240515:

Release 20240515 - Wednesday, May 15th 2024
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - The vectortiles style *ch.swisstopo.leichte-basiskarte.vt* has been replaced by *ch.swisstopo.lightbasemap.vt*. The new style references the vectortiles sets *ch.swisstopo.base.vt* and *ch.swisstopo.relief.vt*
    - The vectortiles style *ch.swisstopo.leichte-basiskarte-imagery.vt* has been replaced by *ch.swisstopo.imagerybasemap.vt*. The new style references the vectortiles set *ch.swisstopo.base.vt*
    - The vectortiles services *ch.swisstopo.leichte-basiskarte.vt* and *ch.swisstopo.leichte-basiskarte-imagery.vt* will no longer be updated and will be removed by the end of the year 2024
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2024-03-13-rc1...2024-05-15-rc1>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissEO VHI <//map.geo.admin.ch/?layers=ch.swisstopo.swisseo_vhi_v100>`__ (ch.swisstopo.swisseo_vhi_v100)                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissEO S2-SR <//map.geo.admin.ch/?layers=ch.swisstopo.swisseo_s2-sr_v100>`__ (ch.swisstopo.swisseo_s2-sr_v100)                                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Groundwater heat utilisation potential <//map.geo.admin.ch/?layers=ch.bfe.grundwasserwaermenutzungspotential>`__ (ch.bfe.grundwasserwaermenutzungspotential)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Thallium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_thallium>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_thallium)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Sulfur <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_schwefel>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_schwefel)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Mercury <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_quecksilber>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_quecksilber)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Sodium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_natrium>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_natrium)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Molybdenum <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_molybdaen>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_molybdaen)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Manganese <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_mangan>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_mangan)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Magnesium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_magnesium>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_magnesium)                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Iron <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_eisen>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_eisen)                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Cobalt <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_cobalt>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_cobalt)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Calcium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_calcium>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_calcium)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Lead <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_blei>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_blei)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Antimony <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_antimon>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_antimon)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Horizontal solar irradiation <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-einstrahlung_0_grad>`__ (ch.bfe.solarenergie-einstrahlung_0_grad)                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar irradiation 30° inclination south <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-einstrahlung_30_grad>`__ (ch.bfe.solarenergie-einstrahlung_30_grad)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar irradiation 75° inclination south <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-einstrahlung_75_grad>`__ (ch.bfe.solarenergie-einstrahlung_75_grad)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Solar irradiation 90° inclination south <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-einstrahlung_90_grad>`__ (ch.bfe.solarenergie-einstrahlung_90_grad)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Plug-in vehicles <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-fahrzeuge>`__ (ch.bfe.ladebedarfswelt-fahrzeuge)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Home charging availability - Convenient <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem>`__ (ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem)       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Home charging availability - Flexible <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_flexibel>`__ (ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_flexibel)     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Home charging availability - Planned <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_geplant>`__ (ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_geplant)        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Charging points - Convenient <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_bequem>`__ (ch.bfe.ladebedarfswelt-ladepunkte_bequem)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Charging points - Flexible <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_felxibel>`__ (ch.bfe.ladebedarfswelt-ladepunkte_felxibel)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Charging points - Planned <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-ladepunkte_geplant>`__ (ch.bfe.ladebedarfswelt-ladepunkte_geplant)                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Charging requirements: Power requirements <//map.geo.admin.ch/?layers=ch.bfe.ladebedarfswelt-strombedarf>`__ (ch.bfe.ladebedarfswelt-strombedarf)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `NLA Natural values / habitats <//map.geo.admin.ch/?layers=ch.armasuisse.natur-landschaft_armee>`__ (ch.armasuisse.natur-landschaft_armee)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pollutant releases (SwissPRTR) <//map.geo.admin.ch/?layers=ch.bafu.swissprtr>`__ (ch.bafu.swissprtr)                                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Control zones - CTR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollzonen>`__ (ch.bazl.luftraeume-kontrollzonen)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Control areas - CTA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollbezirke>`__ (ch.bazl.luftraeume-kontrollbezirke)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Flight information region - FIR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationsgebiet>`__ (ch.bazl.luftraeume-fluginformationsgebiet)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Flight information zones - FIZ <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationszonen>`__ (ch.bazl.luftraeume-fluginformationszonen)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Terminal control areas - TMA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-nahkontrollbezirke>`__ (ch.bazl.luftraeume-nahkontrollbezirke)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G1, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g1>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g1)                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Meat products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cheese <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Confectionery <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-konditoreiwaren>`__ (ch.blw.ursprungsbezeichnungen-konditoreiwaren)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Plant products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-pflanzen>`__ (ch.blw.ursprungsbezeichnungen-pflanzen)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spirits <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-spirituosen>`__ (ch.blw.ursprungsbezeichnungen-spirituosen)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surveyed sections <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cross section securing point <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                             |
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
| Update | `SWISS MIL PILOTS CHART <//map.geo.admin.ch/?layers=ch.vbs.swissmilpilotschart>`__ (ch.vbs.swissmilpilotschart)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of restricted and danger areas <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Waste incineration plants <//map.geo.admin.ch/?layers=ch.bfe.kehrichtverbrennungsanlagen>`__ (ch.bfe.kehrichtverbrennungsanlagen)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ISOS - Site records <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ISOS - Photos <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vectortiles set "base" <//vectortiles.geo.admin.ch/tiles/ch.swisstopo.base.vt/v1.0.0/tiles.json>`__ (ch.swisstopo.base.vt)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Base Map <//vectortiles.geo.admin.ch/styles/ch.swisstopo.basemap.vt/style.json>`__ (ch.swisstopo.basemap.vt)                                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Light Base Map <//vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json>`__ (ch.swisstopo.lightbasemap.vt)                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Imagery Base Map <//https://vectortiles.geo.admin.ch/styles/ch.swisstopo.imagerybasemap.vt/style.json>`__ (ch.swisstopo.imagerybasemap.vt)                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Base network swiss TNE <//map.geo.admin.ch/?layers=ch.swisstopo.swisstne-base>`__ (ch.swisstopo.swisstne-base)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20240313:

Release 20240313 - Wednesday, March 13th 2024
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- **HTTP** **POST**, **PUT** and **DELETE** on api3.geo.admin.ch/rest/services/<topic>/MapServer/* are **no longer accepted**. This behavior has already been documented in the official API documentation and has been `announced <https://groups.google.com/g/geoadmin-api/c/OtsTDxpKDtM/m/IAqSrm3DBQAJ>`__ last year in September. All API REST endpoints support only the following HTTP methods (unless specified): GET, HEAD and OPTIONS
- Announcements:
    - the layer *ch.swisstopo-vd.ortschaftenverzeichnis_plz* has now the additional attributes 'status' and 'modification', as previously announced
    - the layer *ch.bfs.generalisierte-grenzen_agglomerationen_g2* has been removed from chsdi services as previously announced
    - the layers *ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200* and *ch.swisstopo.geologie-geotechnik-gk200* have been removed from chsdi services as previously announced
    - the layers *ch.bakom.mobil-antennenstandorte-5g, ch.bakom.mobil-antennenstandorte-gsm, ch.bakom.mobil-antennenstandorte-umts, ch.bakom.mobil-antennenstandorte-lte* have been removed from chsdi services as previously announced
    - following attributes for the layers *ch.swisstopo.lubis-luftbilder_schwarzweiss*, *ch.swisstopo.lubis-luftbilder_farbe* and *ch.swisstopo.lubis-luftbilder_infrarot* will be removed from chsdi services later this year: 'inventarnummer', 'bildnummer', 'orientierung', 'rotation', 'filesize_mb', 'ort', 'image_height' and 'image_width'
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/>`__

Geodata
*******

+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `NLA Natural values / habitats <//map.geo.admin.ch/?layers=ch.armasuisse.natur-landschaft_armee>`__ (ch.armasuisse.natur-landschaft_armee)                                                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissALTIRegio monodirectional hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissaltiregio-reliefschattierung_monodirektional>`__ (ch.swisstopo.swissaltiregio-reliefschattierung_monodirektional)    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `swissALTIRegio multidirectional hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissaltiregio-reliefschattierung_multidirektional>`__ (ch.swisstopo.swissaltiregio-reliefschattierung_multidirektional) |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Large-scale photovoltaik systems <//map.geo.admin.ch/?layers=ch.bfe.photovoltaik-grossanlagen>`__ (ch.bfe.photovoltaik-grossanlagen)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Mobile phone base stations <//map.geo.admin.ch/?layers=ch.bakom.standorte-mobilfunkanlagen>`__ (ch.bakom.standorte-mobilfunkanlagen)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Obstacle limitation surfaces <//map.geo.admin.ch/?layers=ch.bazl.hindernisbegrenzungsflaechen-kataster>`__ (ch.bazl.hindernisbegrenzungsflaechen-kataster)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Enterprises <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                                                           |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dwellings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen)                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Buildings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude)                                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Population (residents) <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner>`__ (ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner)                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                                                 |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)                                   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                                          |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                                              |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                                                    |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                                                  |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                                            |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                                      |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                             |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wald>`__ (ch.swisstopo.swisstlm3d-wald)                                                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `CO2 Emissions Buildings (SIA 380/1) <//map.geo.admin.ch/?layers=ch.bafu.klima-co2_ausstoss_gebaeude>`__ (ch.bafu.klima-co2_ausstoss_gebaeude)                                                               |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pollutant releases (SwissPRTR) <//map.geo.admin.ch/?layers=ch.bafu.swissprtr>`__ (ch.bafu.swissprtr)                                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                                         |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of restricted and danger areas <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Heat flux 500 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geophysik-geothermie>`__ (ch.swisstopo.geologie-geophysik-geothermie)                                                                       |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SUG Consultation <//map.geo.admin.ch/?layers=ch.bav.sachplan-unterirdischer-guetertransport_anhoerung>`__ (ch.bav.sachplan-unterirdischer-guetertransport_anhoerung)                                        |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Underground freight transport <//map.geo.admin.ch/?layers=ch.bav.sachplan-unterirdischer-guetertransport_kraft>`__ (ch.bav.sachplan-unterirdischer-guetertransport_kraft)                                |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20240131:

Release 20240131 - Wednesday, January 31st 2024
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the layer *ch.swisstopo-vd.ortschaftenverzeichnis_plz* will have the following changes on its data model by the release of March 13th 2024: *additional* attributes 'status' and 'modification'
    - the layer *ch.bfs.generalisierte-grenzen_agglomerationen_g2* will be removed from chsdi services with the release of March 13th 2024.
    - the layers *ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200* and *ch.swisstopo.geologie-geotechnik-gk200* will be removed from chsdi services with the release of March 13th 2024.
    - the layers *ch.bakom.mobil-antennenstandorte-5g, ch.bakom.mobil-antennenstandorte-gsm, ch.bakom.mobil-antennenstandorte-umts, ch.bakom.mobil-antennenstandorte-lte* will be removed from chsdi services with the release of March 13th 2024.
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2023-12-20-rc1...2024-01-31-rc1>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SUG Consultation <//map.geo.admin.ch/?layers=ch.bav.sachplan-unterirdischer-guetertransport_anhoerung>`__ (ch.bav.sachplan-unterirdischer-guetertransport_anhoerung)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SP Underground freight transport <//map.geo.admin.ch/?layers=ch.bav.sachplan-unterirdischer-guetertransport_kraft>`__ (ch.bav.sachplan-unterirdischer-guetertransport_kraft)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surveyed sections <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cross section securing point <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `River typology <//map.geo.admin.ch/?layers=ch.bafu.typisierung-fliessgewaesser>`__ (ch.bafu.typisierung-fliessgewaesser)                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20231220:

Release 20231220 - Wednesday, December 20th 2023
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''

- Bug fixes
- Announcements:
    - the layer *ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill* has now been switched to time-enabled, data till back to 1850 available
    - the layers *ch.swisstopo.geologie-geotechnik-zementindustrie_1965*, *ch.swisstopo.geologie-geotechnik-zementindustrie_1995*, *ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung* and *ch.swisstopo.geologie-geotechnik-ziegeleien_1907* have been removed from chsdi services as previously announced
    - the layer *ch.swisstopo-vd.ortschaftenverzeichnis_plz* will have some changes on its data model probably in March 2024. More information tba
    - the removal of the layers *ch.bakom.mobil-antennenstandorte-5g, ch.bakom.mobil-antennenstandorte-gsm, ch.bakom.mobil-antennenstandorte-umts, ch.bakom.mobil-antennenstandorte-lte* has been postponed to 2024. A detailed planning will be communicated later.

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hanglagen Abschwemmung <//map.geo.admin.ch/?layers=ch.blw.hanglagen-abschwemmung>`__ (ch.blw.hanglagen-abschwemmung)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Arsenic <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_arsen>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_arsen)                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Chromium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_chrom>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_chrom)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Cadmium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_cadmium>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_cadmium)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Copper <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_kupfer>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_kupfer)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Nickel <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_nickel>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_nickel)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Uranium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_uran>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_uran)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Vanadium <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_vanadium>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_vanadium)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geochemical soil atlas of Switzerland: Zink <//map.geo.admin.ch/?layers=ch.bafu.geochemischer-bodenatlas_schweiz_zink>`__ (ch.bafu.geochemischer-bodenatlas_schweiz_zink)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Railway Installations MAO <//map.geo.admin.ch/?layers=ch.bav.betriebe-stoerfallverordnung_eisenbahnanlagen>`__ (ch.bav.betriebe-stoerfallverordnung_eisenbahnanlagen)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Consultation <//map.geo.admin.ch/?layers=ch.bfe.sachplan-uebertragungsleitungen_anhoerung>`__ (ch.bfe.sachplan-uebertragungsleitungen_anhoerung)                                                                 |
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
| Update | `Road Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.strassenkarte-200>`__ (ch.swisstopo.strassenkarte-200)                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Stocking of river banks <//map.geo.admin.ch/?layers=ch.bafu.gewaesser-uferbestockung>`__ (ch.bafu.gewaesser-uferbestockung)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kantion-flaeche.fill)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Stocking map <//map.geo.admin.ch/?layers=ch.bafu.gewaesser-uferbestockung_vegetation>`__ (ch.bafu.gewaesser-uferbestockung_vegetation)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Winter national map | LK10, LK25, LK50, LK100 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-winter>`__ (ch.swisstopo.pixelkarte-farbe-winter)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tank relocation routes <//map.geo.admin.ch/?layers=ch.vbs.panzerverschiebungsrouten>`__ (ch.vbs.panzerverschiebungsrouten)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Built-up areas VIL <//map.geo.admin.ch/?layers=ch.bazl.bebaute-gebiete_luftfahrtrecht>`__ (ch.bazl.bebaute-gebiete_luftfahrtrecht)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=ch.bafu.wrz-wildruhezonen_portal>`__ (ch.bafu.wrz-wildruhezonen_portal)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Interregional wildlife corridor <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierkorridor_national>`__ (ch.bafu.fauna-wildtierkorridor_national)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dam <//map.geo.admin.ch/?layers=ch.bfe.stauanlagen-bundesaufsicht>`__ (ch.bfe.stauanlagen-bundesaufsicht)                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Slope over 30 degrees <//map.geo.admin.ch/?layers=ch.swisstopo-karto.hangneigung>`__ (ch.swisstopo-karto.hangneigung)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Slope classes over 30 degrees <//map.geo.admin.ch/?layers=ch.swisstopo.hangneigung-ueber_30>`__ (ch.swisstopo.hangneigung-ueber_30)                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung_monodirektional>`__ (ch.swisstopo.swissalti3d-reliefschattierung_monodirektional)                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway Lines MAO <//map.geo.admin.ch/?layers=ch.bav.lage-stoerfallverordnung_eisenbahnanlagen>`__ (ch.bav.lage-stoerfallverordnung_eisenbahnanlagen)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Height control points HFP1 <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-hfp1>`__ (ch.swisstopo.fixpunkte-hfp1)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Planimetric control points LFP1 <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-lfp1>`__ (ch.swisstopo.fixpunkte-lfp1)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20231101:

Release 20231101 - Wednesday, November 1st 2023
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcements:
    - the layer *ch.bafu.hydroweb-warnkarte_regional* has been removed from chsdi services as previously announced
    - the layers *ch.swisstopo.geologie-geotechnik-zementindustrie_1965*, *ch.swisstopo.geologie-geotechnik-zementindustrie_1995*, *ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung* and *ch.swisstopo.geologie-geotechnik-ziegeleien_1907* will be removed from chsdi services with the release of December 20st 2023
    - the removal of the layers *ch.bakom.mobil-antennenstandorte-5g, ch.bakom.mobil-antennenstandorte-gsm, ch.bakom.mobil-antennenstandorte-umts, ch.bakom.mobil-antennenstandorte-lte* has been postponed to 2024. A detailed planning will be communicated later.
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2023-09-06-rc1...2023-11-01-rc1>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reflection seismic <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-reflexionsseismik>`__ (ch.swisstopo.geologie-reflexionsseismik)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wetness potential in the agricultural land, vector ( <//map.geo.admin.ch/?layers=ch.agroscope.feuchtflaechenpotential-kulturlandschaft>`__ (ch.agroscope.feuchtflaechenpotential-kulturlandschaft)               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Wildlife Passages <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierpassagen>`__ (ch.bafu.fauna-wildtierpassagen)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Milchmarktregionen <//map.geo.admin.ch/?layers=ch.blw.milchmarktregionen>`__ (ch.blw.milchmarktregionen)                                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Profiles GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_profile>`__ (ch.swisstopo.geologie-geologischer_atlas_profile)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Safety zone plan <//map.geo.admin.ch/?layers=ch.bazl.sicherheitszonenplan>`__ (ch.bazl.sicherheitszonenplan)                                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Protected Areas VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-adminboundaries-protectedarea>`__ (ch.swisstopo.vec200-adminboundaries-protectedarea)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building generalized VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-building>`__ (ch.swisstopo.vec200-building)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrology VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-hydrography>`__ (ch.swisstopo.vec200-hydrography)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land cover VECTOR200 <//map.geo.admin.ch/?layers=ch.swisstopo.vec200-landcover>`__ (ch.swisstopo.vec200-landcover)                                                                                               |
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
| Update | `Viticulture on slopes <//map.geo.admin.ch/?layers=ch.blw.steil_terrassenlagen_rebbau>`__ (ch.blw.steil_terrassenlagen_rebbau)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hillsides and slopes <//map.geo.admin.ch/?layers=ch.blw.hang_steillagen>`__ (ch.blw.hang_steillagen)                                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Consultation <//map.geo.admin.ch/?layers=ch.bfe.sachplan-uebertragungsleitungen_anhoerung>`__ (ch.bfe.sachplan-uebertragungsleitungen_anhoerung)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Housing Inventory <//map.geo.admin.ch/?layers=ch.are.wohnungsinventar-zweitwohnungsanteil>`__ (ch.are.wohnungsinventar-zweitwohnungsanteil)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20230906:

Release 20230906 - Wednesday, September 6th 2023
------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcements:
    - the mapviewer topic "geothermie" has been removed from map.geo.admin.ch as previously announced
    - the layer *ch.bafu.hydrologie-messstationen_gefahren* has been removed from chsdi services as previously announced
    - the layer *ch.bafu.hydroweb-warnkarte_regional* will be removed from chsdi services with the release of November 1st 2023
    - the layers *ch.bakom.mobil-antennenstandorte-5g, ch.bakom.mobil-antennenstandorte-gsm, ch.bakom.mobil-antennenstandorte-umts, ch.bakom.mobil-antennenstandorte-lte* will be removed from chsdi services with the release of November 1st 2023
    - Since August 2023 swisstopo publishes its aerial images for download step by step. A first group of 30000 images, orthophotos (if available) and metadata is already available. The remaining images will follow in the course of the next year. For aerial images that can now be downloaded, swisstopo has replaced the preview function in the map.geo.admin.ch viewer by a direct download. This offer is part of swisstopo's Open Government Data (OGD) strategy.

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Groundwater temperature <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_grundwassertemperatur>`__ (ch.bafu.hydroweb-messstationen_grundwassertemperatur)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `SORA Ground Risk <//map.geo.admin.ch/?layers=ch.bazl.intrinsisches-bodenrisiko_sora>`__ (ch.bazl.intrinsisches-bodenrisiko_sora)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Situation of rivers and lakes <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_zustand>`__ (ch.bafu.hydroweb-messstationen_zustand)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Water temperature rivers <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_temperatur>`__ (ch.bafu.hydroweb-messstationen_temperatur)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Flood hazard levels <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_gefahren>`__ (ch.bafu.hydroweb-messstationen_gefahren)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Groundwater level/spring discharge <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_grundwasserzustand>`__ (ch.bafu.hydroweb-messstationen_grundwasserzustand)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Stations hydrological forecasts <//map.geo.admin.ch/?layers=ch.bafu.hydroweb-messstationen_vorhersage>`__ (ch.bafu.hydroweb-messstationen_vorhersage)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Waste incineration plants <//map.geo.admin.ch/?layers=ch.bfe.kehrichtverbrennungsanlagen>`__ (ch.bfe.kehrichtverbrennungsanlagen)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cross section securing point <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surveyed sections <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hunting Ban Reserves AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_jagdbanngebiete>`__ (ch.bafu.schutzgebiete-aulav_jagdbanngebiete)                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Other protected areas AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_uebrige>`__ (ch.bafu.schutzgebiete-aulav_uebrige)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: Side of tick bite reported <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tracer tests <//map.geo.admin.ch/?layers=ch.bafu.hydrogeologie-markierversuche>`__ (ch.bafu.hydrogeologie-markierversuche)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Interregional wildlife corridor <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierkorridor_national>`__ (ch.bafu.fauna-wildtierkorridor_national)                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Flood statistics <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-hochwasserstatistik>`__ (ch.bafu.hydrologie-hochwasserstatistik)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low-flow statistics <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-niedrigwasserstatistik>`__ (ch.bafu.hydrologie-niedrigwasserstatistik)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `HUG hydrological study areas <//map.geo.admin.ch/?layers=ch.bafu.hydrologie-untersuchungsgebiete>`__ (ch.bafu.hydrologie-untersuchungsgebiete)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Water & migrant bird reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-vogelreservate>`__ (ch.bafu.bundesinventare-vogelreservate)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vegetation height model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Surface model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell_relief>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell_relief)                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations - principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung-uebergeordnet)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=2022&time=2022>`__ (ch.swisstopo.swissimage-product)                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=2022&time=2022>`__ (ch.swisstopo.swissimage-product.metadata)        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest reserves <//map.geo.admin.ch/?layers=ch.bafu.waldreservate>`__ (ch.bafu.waldreservate)                                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2023-06-28-rc1...2023-09-06-rc1>`__

.. _releasenotes_20230628:

Release 20230628 - Wednesday, June 28th 2023
--------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcements:
    - the downloads for *ch.bfs.gebaeude_wohnungs_register* have been removed from data.geo.admin.ch as previously announced. Downloads for the Federal Register of Buildings and Dwellings are officially available via https://www.housing-stat.ch/fr/madd/public.html
    - the layers *ch.bafu.hydrologie-messstationen_gefahren* and *ch.bafu.hydroweb-warnkarte_regional* will be removed from chsdi services with the release of September 6th 2023
    - the mapviewer topic "geothermie" will be removed from map.geo.admin.ch with the release of September 6th 2023

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vector representation of relief <//vectortiles.geo.admin.ch/tiles/ch.swisstopo.relief.vt/v1.0.0/tiles.json>`__ (ch.swisstopo.relief.vt), a new vector based terrain (vector tiles)             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, zuläss. Immission T <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag)     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, zuläss. Immission N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nach>`__ (ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nach)   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, tats. Immission N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht)     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, tats. Immission T <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag)         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, tats. Emission T <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag)    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, tats. Emission N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht)|
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, festgel. Emission T <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag)     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, festgel. Emission N <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht) |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Eisenbahnlärm, Lärmschutzwände <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_laermschutzwaende>`__  (ch.bav.laermbelastung-eisenbahn_laermschutzwaende)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Konsultationsbereiche Rohrleitungen <//map.geo.admin.ch/?layers=ch.bfe.rohrleitungen-konsultationsbereiche>`__ (ch.bfe.rohrleitungen-konsultationsbereiche)                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cities and conurbations BeSA <//map.geo.admin.ch/?layers=ch.are.agglomerationsverkehr>`__ (ch.are.agglomerationsverkehr)                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alps with livestock guardian dogs <//map.geo.admin.ch/?layers=ch.bafu.alpweiden-herdenschutzhunde>`__ (ch.bafu.alpweiden-herdenschutzhunde)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Status of Cantonal Geotope Inventories <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geotope_kantone_stand>`__ (ch.swisstopo.geologie-geotope_kantone_stand)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spectral micro-zoning <//map.geo.admin.ch/?layers=ch.bafu.gefahren-spektral>`__ (ch.bafu.gefahren-spektral)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Electricity Transmission Lines sectoral plan <//map.geo.admin.ch/?layers=ch.bfe.sachplan-uebertragungsleitungen_kraft>`__ (ch.bfe.sachplan-uebertragungsleitungen_kraft)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hunting Ban Reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-jagdbanngebiete>`__ (ch.bafu.bundesinventare-jagdbanngebiete)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2023-05-10-rc1...2023-06-28-rc1>`__

.. _releasenotes_20230510:

Release 20230510 - Wednesday, May 10th 2023
-------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcements:
    - The WMTS in `WGS84 (EPSG:4326) <https://wmts.geo.admin.ch/EPSG/4326/1.0.0/WMTSCapabilities.xml>`__ is now in **lat/lon order**

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Base network swiss TNE <//map.geo.admin.ch/?layers=ch.swisstopo.swisstne-base>`__ (ch.swisstopo.swisstne-base)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Canton NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-kantone>`__ (ch.bafu.landesforstinventar-kantone)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Diffuse total phosphorus inputs <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-diffuse_eintraege_gesamt_phosphor>`__ (ch.bafu.gewaesserschutz-diffuse_eintraege_gesamt_phosphor)          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G1, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g1>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g1)                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G2, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g2>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g2)                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Control zones - CTR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollzonen>`__ (ch.bazl.luftraeume-kontrollzonen)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISS MIL PILOTS CHART <//map.geo.admin.ch/?layers=ch.vbs.swissmilpilotschart>`__ (ch.vbs.swissmilpilotschart)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of restricted and danger areas <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Housing Inventory <//map.geo.admin.ch/?layers=ch.are.wohnungsinventar-zweitwohnungsanteil>`__ (ch.are.wohnungsinventar-zweitwohnungsanteil)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ISOS - Site records <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ISOS - Photos <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Overland flow map <//map.geo.admin.ch/?layers=ch.bafu.gefaehrdungskarte-oberflaechenabfluss>`__ (ch.bafu.gefaehrdungskarte-oberflaechenabfluss)                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map swissTLM (color) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-farbe>`__ (ch.swisstopo.swisstlm3d-karte-farbe)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map swissTLM (grey) <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-karte-grau>`__ (ch.swisstopo.swisstlm3d-karte-grau)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Catchment <//map.geo.admin.ch/?layers=ch.bafu.wasser-entnahme>`__ (ch.bafu.wasser-entnahme)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hunting Ban Reserves <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-jagdbanngebiete>`__ (ch.bafu.bundesinventare-jagdbanngebiete)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Total total nitrogen inputs <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff>`__ (ch.bafu.gewaesserschutz-diffuse_eintraege_stickstoff)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Diffuse dissolved phosphorus inputs <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor>`__ (ch.bafu.gewaesserschutz-diffuse_eintraege_phosphor)                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wells > 500m <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-bohrungen_tiefer_500>`__ (ch.swisstopo.geologie-bohrungen_tiefer_500)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2023-03-15-rc1...2023-05-10-rc1>`__

.. _releasenotes_20230315:

Release 20230315 - Wednesday, March 15th 2022
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcements:
   - the API of the layer **ch.bfe.ladestellen-elektromobilitaet** has been removed from FSDI services as previously announced. For more information about the new service please contact geoinformation@bfe.admin.ch
   - generic solution for technical group WMS layers in wms.geo.admin.ch: Technical groups are now visible in the GetCapbilities document as a group with one single Layer having the same name as the group. The new structure of technical groups allows an easier use of GetFeatureInfo in most GIS clients. All remaining layers have been reorganized accordingly as previously announced
   - the layer **ch.pronatura.waldreservate** has been removed from chsdi services as previously announced
   - the layer **ch.bafu.wald-vegetationshoehenstufen_1995** will be removed from chsdi services with the release of May 10th 2023
   - the downloads for **ch.bfs.gebaeude_wohnungs_register** available via https://data.geo.admin.ch/ch.bfs.gebaeude_wohnungs_register/data.zip will be removed with the deploy of June 28th 2023. Downloads for the Federal Register of Buildings and Dwellings are officially available via https://www.housing-stat.ch/fr/madd/public.html
   - the layers **ch.bafu.hydrologie-messstationen_gefahren** and **ch.bafu.hydroweb-warnkarte_regional** will be removed from chsdi services with the release of June 28th 2023

- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2022-12-14-rc1...2023-03-15-rc1>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Forest fire prevention measures <//map.geo.admin.ch/?layers=ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone>`__ (ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Forest fire danger <//map.geo.admin.ch/?layers=ch.bafu.gefahren-waldbrand_warnung>`__ (ch.bafu.gefahren-waldbrand_warnung)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Tranquillity Areas <//map.geo.admin.ch/?layers=ch.bafu.tranquillity-gebiete>`__ (ch.bafu.tranquillity-gebiete)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Tranquillity Map <//map.geo.admin.ch/?layers=ch.bafu.tranquillity-karte>`__ (ch.bafu.tranquillity-karte)                                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `RBD: energy/heat source heating <//map.geo.admin.ch/?layers=ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung>`__ (ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `CO2 Emissions Buildings (SIA 380/1) <//map.geo.admin.ch/?layers=ch.bafu.klima-co2_ausstoss_gebaeude>`__ (ch.bafu.klima-co2_ausstoss_gebaeude)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pollen stations <//map.geo.admin.ch/?layers=ch.meteoschweiz.messnetz-pollen>`__ (ch.meteoschweiz.messnetz-pollen)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Road accidents <//map.geo.admin.ch/?topic=vu>`__ (complete topic Road accidents)                                                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Journey through time <//map.geo.admin.ch/?layers=ch.swisstopo.zeitreihen>`__ (ch.swisstopo.zeitreihen)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Height control points HFP1 <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-hfp1>`__ (ch.swisstopo.fixpunkte-hfp1)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Planimetric control points LFP1 <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-lfp1>`__ (ch.swisstopo.fixpunkte-lfp1)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cities and conurbations BeSA <//map.geo.admin.ch/?layers=ch.are.agglomerationsverkehr>`__ (ch.are.agglomerationsverkehr)                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vermessungsstrecken - Querprofilmarke <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Datenbank Querprofile (QP) - Vermessungsstrecken <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=bafu.wrz-wildruhezonen_portal>`__ (bafu.wrz-wildruhezonen_portal)                                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Habitat Map <//map.geo.admin.ch/?layers=ch.bafu.lebensraumkarte-schweiz>`__ (ch.bafu.lebensraumkarte-schweiz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geothermal potential studies <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geothermische_potenzialstudien_regional>`__ (ch.swisstopo.geologie-geothermische_potenzialstudien_regional)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Deep geothermal projects <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-tiefengeothermie_projekte>`__ (ch.swisstopo.geologie-tiefengeothermie_projekte)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wald>`__ (ch.swisstopo.swisstlm3d-wald)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of restricted and danger areas <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (fixed) N emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht)                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (fixed) D emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) N emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht)                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise (act.) D emissions <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag>`__ (ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag)                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway noise protection walls <//map.geo.admin.ch/?layers=ch.bav.laermbelastung-eisenbahn_laermschutzwaende>`__ (ch.bav.laermbelastung-eisenbahn_laermschutzwaende)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20230222:

Release 20230222 - Thursday, February 22th 2023
-----------------------------------------------

API & applications
******************

The API of the layer ch.bfe.ladestellen-elektromobilitaet is expected to be removed from FSDI services on March 15th. For more information on the exact schedule and the new service, please contact geoinformation@bfe.admin.ch .

.. _releasenotes_20221214:

Release 20221214 - Wednesday, December 14th 2022
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcements:

  - the layer **ch.bazl.einschraenkungen-drohnen** has changed its **data and representation model** as previously announced. New attributes on this layer: zone_name_de, zone_name_fr, zone_name_it, zone_name_en, zone_restriction_de, zone_restriction_fr, zone_restriction_it, zone_restriction_en, zone_message_de, zone_message_fr, zone_message_it, zone_message_en, auth_url, auth_name, auth_contact, auth_service, auth_email, auth_phone, auth_intervalbefore, air_vol_lower_limit, air_vol_lower_vref, air_vol_upper_limit, air_vol_upper_vref, time_permanent, time_start, time_end, period_day, period_start, period_end. Further information: `model description <https://www.bazl.admin.ch/bazl/de/home/themen/geoinformation_statistik/geoinformation/geofachdaten/uaszones.html>`__
  - the layer **ch.bazl.luftfahrthindernis** has changed in its content and its representation model: Small obstacles near airports are now published in a seperate layer ch.bazl.luftfahrthindernis-klein
  - the layer **ch.bfs.gebaeude_wohnungs_register** has new download links. Downloads are now provided from the `MADD platform provided by the Federal Statistical Office <https://www.housing-stat.ch/de/madd/public.html>`__
  - the WMS of the layer **ch.bfe.ladestellen-elektromobilitaet** has been removed from FSDI services as previously announced
  - the layers **ch.astra.baulinien-nationalstrassen.oereb**, **ch.astra.projektierungszonen-nationalstrassen.oereb**, **ch.bav.baulinien-eisenbahnanlagen.oereb**, **ch.bav.kataster-belasteter-standorte-oev.oereb**, **ch.bav.projektierungszonen-eisenbahnanlagen.oereb**, **ch.bazl.baulinien-flughafenanlagen.oereb**, **ch.bazl.kataster-belasteter-standorte-zivilflugplaetze.oereb**, **ch.bazl.projektierungszonen-flughafenanlagen.oereb**, **ch.bazl.sicherheitszonenplan.oereb** and **ch.vbs.kataster-belasteter-standorte-militaer.oereb** have been removed from FSDI services (WMS and OEREB Feature Service)
  - the WMS layers **ch.swisstopo.swissboundaries3d.inspire** and **ch.swisstopo.swissnames3d.inspire** have been removed from FSDI services
  - generic solution for technical group WMS layers. Technical groups will now be visible in the GetCapbilities Document as a group with one single Layer having the same name as the group. The new structure of technical groups will allow an easier use of GetFeatureInfo in most GIS clients. Following layers have been reorganized accordingly and many more to follow with the release on March 15th 2023: **ch.astra.mountainbikeland**, **ch.astra.skatingland**, **ch.astra.veloland**, **ch.astra.wanderland**, **ch.bfe.solarenergie-eignung-daecher**, **ch.bfe.solarenergie-eignung-fassaden**, **ch.swisstopo.geologie-geocover**, **ch.swisstopo.geologie-geologische_karte**, **ch.swisstopo.geologie-geologischer_atlas**, **ch.swisstopo.lubis-luftbilder_schraegaufnahmen**, **ch.swisstopo.lubis-terrestrische_aufnahmen**, **ch.swisstopo.swissbathy3d-reliefschattierung** and **ch.swisstopo.swissimage-product.metadata**
  - the layer **ch.pronatura.waldreservate** will be removed from FSDI services with the release of March 15th 2023

- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2022-10-26-rc1...2022-12-14-rc1>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Habitat Map <//map.geo.admin.ch/?layers=ch.bafu.lebensraumkarte-schweiz>`__ (ch.bafu.lebensraumkarte-schweiz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Stocking of river banks <//map.geo.admin.ch/?layers=ch.bafu.gewaesser-uferbestockung>`__ (ch.bafu.gewaesser-uferbestockung)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Stocking map <//map.geo.admin.ch/?layers=ch.bafu.gewaesser-uferbestockung_vegetation>`__ (ch.bafu.gewaesser-uferbestockung_vegetation)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Plätze für Jenische, Sinti und Roma <//map.geo.admin.ch/?layers=ch.bak.halteplaetze-jenische_sinti_roma>`__ (ch.bak.halteplaetze-jenische_sinti_roma)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Aerodrome obstacles < 25 / 60 m <//map.geo.admin.ch/?layers=ch.bazl.luftfahrthindernis-klein>`__ (ch.bazl.luftfahrthindernis-klein)                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building zones Switzerland (harmonized) <//map.geo.admin.ch/?layers=ch.are.bauzonen>`__ (ch.are.bauzonen)                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Housing Inventory <//map.geo.admin.ch/?layers=ch.are.wohnungsinventar-zweitwohnungsanteil>`__ (ch.are.wohnungsinventar-zweitwohnungsanteil)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division swissSURFACE3D Raster <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-raster.metadata>`__ (ch.swisstopo.swisssurface3d-raster.metadata)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional)         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional)      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vermessungsstrecken - Querprofilmarke <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Datenbank Querprofile (QP) - Vermessungsstrecken <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=bafu.wrz-wildruhezonen_portal>`__ (bafu.wrz-wildruhezonen_portal)                                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Low distortion area <//map.geo.admin.ch/?layers=ch.swisstopo-vd.spannungsarme-gebiete>`__ (ch.swisstopo-vd.spannungsarme-gebiete)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ILNM <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-bln>`__ (ch.bafu.bundesinventare-bln)                                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Floodplains <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-auen>`__ (ch.bafu.bundesinventare-auen)                                                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Register of Buildings and Dwellings <//map.geo.admin.ch/?layers=ch.bfs.gebaeude_wohnungs_register>`__ (ch.bfs.gebaeude_wohnungs_register)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Air navigation obstacles <//map.geo.admin.ch/?layers=ch.bazl.luftfahrthindernis>`__ (ch.bazl.luftfahrthindernis)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dwellings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Buildings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Population (residents) <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner>`__ (ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Winter national map | LK10, LK25, LK50, LK100 <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-farbe-winter>`__ (ch.swisstopo.pixelkarte-farbe-winter)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP rail infrastructure <//map.geo.admin.ch/?layers=ch.bav.sachplan-infrastruktur-schiene_kraft>`__ (ch.bav.sachplan-infrastruktur-schiene_kraft)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL Anhörung <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20221026:

Release 20221026 - Wednesday, October 26th 2022
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcements:
- the layer **ch.bazl.einschraenkungen-drohnen** will change its **data and representation model** with the release on December 14th 2022. New attributes on this layer (**current attributes won't be supported anymore!**): zone_name_de, zone_name_fr, zone_name_it, zone_name_en, zone_restriction_de, zone_restriction_fr, zone_restriction_it, zone_restriction_en, zone_message_de, zone_message_fr, zone_message_it, zone_message_en, auth_url, auth_name, auth_contact, auth_service, auth_email, auth_phone, auth_intervalbefore, air_vol_lower_limit, air_vol_lower_vref, air_vol_upper_limit, air_vol_upper_vref, time_permanent, time_start, time_end, period_day, period_start, period_end. Further information: `model description <https://www.bazl.admin.ch/bazl/de/home/themen/geoinformation_statistik/geoinformation/geofachdaten/uaszones.html>`__
- the WMS of the layer **ch.bfe.ladestellen-elektromobilitaet** will be removed from FSDI services with the release on December 14th 2022
- the layers **ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal** and **ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet** have been removed from FSDI services as previously announced
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2022-09-07-rc1...2022-10-26-rc1>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_220907...r_221026>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ammonia Concentration <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-ammoniakkonzentration>`__ (ch.bafu.luftreinhaltung-ammoniakkonzentration)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Nitrogen Deposition <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-stickstoffdeposition>`__ (ch.bafu.luftreinhaltung-stickstoffdeposition)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `CLN Exceedance <//map.geo.admin.ch/?layers=ch.bafu.luftreinhaltung-stickstoff_kritischer_eintrag>`__ (ch.bafu.luftreinhaltung-stickstoff_kritischer_eintrag)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dam <//map.geo.admin.ch/?layers=ch.bfe.stauanlagen-bundesaufsicht>`__ (ch.bfe.stauanlagen-bundesaufsicht)                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                        |
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
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional)         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional)      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=1946&time=1946>`__ (ch.swisstopo.swissimage-product)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=1946&time=1946>`__ (ch.swisstopo.swissimage-product.metadata)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20220907:

Release 20220907 - Wednesday, September 7th 2022
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement:
- the layers **ch.astra.mountainbikeland-sperrungen_umleitungen, ch.astra.skatingland-sperrungen_umleitungen, ch.astra.veloland-sperrungen_umleitungen and ch.astra.wanderland-sperrungen_umleitungen have the following changes on their CHSDI data model with this release as previously announced: **Attributes to be removed**: content_provider, reason, state_validate, type, url1_text. **Attributes to be added**: content_provider_de, content_provider_fr, content_provider_it, content_provider_en, reason_de, reason_fr, reason_it, reason_en, state_validate_de, state_validate_fr, state_validate_it, state_validate_en (all text instead of coded values), route_nr, segment_nr, type_de, type_fr, type_it, type_en
- the layers **ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal** and **ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet** will be removed from FSDI services with the release on October 26th 2022
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2022-06-29-rc32...2022-09-07-rc1>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_220629...r_220907>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Upper timberline <//map.geo.admin.ch/?layers=ch.bafu.wald-obere-waldgrenze>`__ (ch.bafu.wald-obere-waldgrenze)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Frequency of Föhn <//map.geo.admin.ch/?layers=ch.bafu.wald-foehnhaeufigkeit_jahr>`__ (ch.bafu.wald-foehnhaeufigkeit_jahr)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Continentality 1000 m 1995 <//map.geo.admin.ch/?layers=ch.bafu.wald-kontinentalitaet_jahr_1000m_1981_2010>`__ (ch.bafu.wald-kontinentalitaet_jahr_1000m_1981_2010)                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Continentality 1000 m July 1995 <//map.geo.admin.ch/?layers=ch.bafu.wald-kontinentalitaet_juli_1000m_1981_2010>`__ (ch.bafu.wald-kontinentalitaet_juli_1000m_1981_2010)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rel. air humidity July, 1981-2010 <//map.geo.admin.ch/?layers=ch.bafu.wald-relative_luftfeuchte_juli_1981_2010>`__ (ch.bafu.wald-relative_luftfeuchte_juli_1981_2010)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Rel. air humidity year, 1981-2010 <//map.geo.admin.ch/?layers=ch.bafu.wald-relative_luftfeuchte_jahr_1981_2010>`__ (ch.bafu.wald-relative_luftfeuchte_jahr_1981_2010)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation summer 2085, RCP 8.5 <//map.geo.admin.ch/?layers=ch.bafu.wald-niederschlag_sommer_2085_stark>`__ (ch.bafu.wald-niederschlag_sommer_2085_stark)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation summer 2085, RCP 4.5 <//map.geo.admin.ch/?layers=ch.bafu.wald-niederschlag_sommer_2085_maessig>`__ (ch.bafu.wald-niederschlag_sommer_2085_maessig)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation summer 2085, RCP 2.6 <//map.geo.admin.ch/?layers=ch.bafu.wald-niederschlag_sommer_2085_gering>`__ (ch.bafu.wald-niederschlag_sommer_2085_gering)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation Appril-August 2085, RCP 8.5 <//map.geo.admin.ch/?layers=ch.bafu.wald-niederschlag_april_august_2085_stark>`__ (ch.bafu.wald-niederschlag_april_august_2085_stark)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation Appril-August 2085, RCP 4.5 <//map.geo.admin.ch/?layers=ch.bafu.wald-niederschlag_april_august_2085_maessig>`__ (ch.bafu.wald-niederschlag_april_august_2085_maessig)                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Precipitation Appril-August 2085, RCP 2.6 <//map.geo.admin.ch/?layers=ch.bafu.wald-niederschlag_april_august_2085_gering>`__ (ch.bafu.wald-niederschlag_april_august_2085_gering)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air temperature July 2085, RCP 8.5 <//map.geo.admin.ch/?layers=ch.bafu.wald-lufttemperatur_juli_2085_stark>`__ (ch.bafu.wald-lufttemperatur_juli_2085_stark)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air temperature July 2085, RCP 4.5 <//map.geo.admin.ch/?layers=ch.bafu.wald-lufttemperatur_juli_2085_maessig>`__ (ch.bafu.wald-lufttemperatur_juli_2085_maessig)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air temperature July 2085, RCP 2.6 <//map.geo.admin.ch/?layers=ch.bafu.wald-lufttemperatur_juli_2085_gering>`__ (ch.bafu.wald-lufttemperatur_juli_2085_gering)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air temperature July 2085, 1981-2010 <//map.geo.admin.ch/?layers=ch.bafu.wald-lufttemperatur_juli_1981_2010>`__ (ch.bafu.wald-lufttemperatur_juli_1981_2010)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Air temperature July 2085, 1961-1990 <//map.geo.admin.ch/?layers=ch.bafu.wald-lufttemperatur_juli_1961_1990>`__ (ch.bafu.wald-lufttemperatur_juli_1961_1990)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vermessungsstrecken - Querprofilmarke <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Datenbank Querprofile (QP) - Vermessungsstrecken <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                   |
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
| Update | `Traffic counting locations - principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung-uebergeordnet)                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=2021&time=2021>`__ (ch.swisstopo.swissimage-product)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=2021&time=2021>`__ (ch.swisstopo.swissimage-product.metadata)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Planimetric control points LFP1 <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-lfp1>`__ (ch.swisstopo.fixpunkte-lfp1)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo color <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_farbe>`__ (ch.swisstopo.lubis-luftbilder_farbe)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo b / w <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_schwarzweiss>`__ (ch.swisstopo.lubis-luftbilder_schwarzweiss)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial Images swisstopo infrared <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder_infrarot>`__ (ch.swisstopo.lubis-luftbilder_infrarot)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images privates <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-firmen>`__ (ch.swisstopo.lubis-luftbilder-dritte-firmen)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _releasenotes_20220629:

Release 20220629 - Wednesday, June 29th 2022
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement:
    - **ch.astra.mountainbikeland-sperrungen_umleitungen, ch.astra.skatingland-sperrungen_umleitungen, ch.astra.veloland-sperrungen_umleitungen and ch.astra.wanderland-sperrungen_umleitungen will get the following changes on their CHSDI data model with the release on September 7th 2022: **Attributes to be removed**: content_provider, reason, state_validate, type, url1_text. **Attributes to be added**: content_provider_de, content_provider_fr, content_provider_it, content_provider_en, reason_de, reason_fr, reason_it, reason_en, state_validate_de, state_validate_fr, state_validate_it, state_validate_en (all text instead of coded values), route_nr, segment_nr, type_de, type_fr, type_it, type_en
    - **ch.swisstopo.uebersicht-gemeinden** and **ch.swisstopo.uebersicht-schweiz** have been removed from FSDI services as previously announced
    - **ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2, ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2, ch.swisstopo.geologie-gisgeol-flaechen-10to100km2 ch.swisstopo.geologie-gisgeol-flaechen-10x10km, ch.swisstopo.geologie-gisgeol-flaechen-1x1km, ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2, ch.swisstopo.geologie-gisgeol-flaechen-lt10km2, ch.swisstopo.geologie-gisgeol-linien** and **ch.swisstopo.geologie-gisgeol-punkte** have been removed from FSDI services as previously announced
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2022-05-18-rc33...2022-06-29-rc1>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_220518...r_220629>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 100 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-pk100.metadata>`__ (ch.swisstopo.pixelkarte-pk100.metadata)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 50 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-pk50.metadata>`__ (ch.swisstopo.pixelkarte-pk50.metadata)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division national map 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.pixelkarte-pk25.metadata>`__ (ch.swisstopo.pixelkarte-pk25.metadata)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Gravimetric base network <//map.geo.admin.ch/?layers=ch.swisstopo.landesschwerenetz>`__ (ch.swisstopo.landesschwerenetz)                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Height control points HFP1 <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-hfp1>`__ (ch.swisstopo.fixpunkte-hfp1)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Image strips swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-bildstreifen>`__ (ch.swisstopo.lubis-bildstreifen)                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Zones) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional)         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional)      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Erosion risk crop qualitative <//map.geo.admin.ch/?layers=ch.blw.erosion>`__ (ch.blw.erosion)                                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Erosion risk crop quantitative <//map.geo.admin.ch/?layers=ch.blw.erosion-quantitativ>`__ (ch.blw.erosion-quantitativ)                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20220518:

Release 20220518 - Wednesday, Mai 18th 2022
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- XYZ Service Request Structure Documentation: http://api.geo.admin.ch/services/sdiservices.html#XYZ
- Announcement:
    - **ch.bazl.luftfahrthindernis** has changed its data model as previously announced: Attributes removed: abortionaccomplished, duration, lk100, sanctiontext, startofconstruction, totallength. Attributes added: airport, effectivedate, group, lighting, marking, radius, uuid.
    - **ch.swisstopo.amtliches-strassenverzeichnis** has changed its complete data model as previously announced. New model according to the official `model description <https://www.cadastre.ch/content/cadastre-internet/de/services/service/registry/street/_jcr_content/contentPar/tabs_copy/items/dokumente/tabPar/downloadlist/downloadItems/314_1614004254682.download/Spezifikation-DE.pdf>`__ Attributes removed: id, label, plzo, gdenr, gdename, type, status, official, validated, modified. Attributes added: str_esid, stn_label, zip_label, com_fosnr, com_name, str_type, str_status, str_official, str_valid, str_modified
    - **ch.swisstopo.wanderkarte50_papier.metadata, ch.swisstopo.wanderkarte33_papier.metadata, ch.swisstopo.wanderkarte25-zus_papier.metadata, ch.swisstopo.skitourenkarte-50.metadata, ch.swisstopo.strassenkarte200_papier.metadata,ch.swisstopo.burgenkarte200_papier.metadata, ch.swisstopo.landeskarte25_papier.metadata, ch.swisstopo.landeskarte50_papier.metadata, ch.swisstopo.landeskarte100_papier.metadata, ch.swisstopo.landeskarte200_papier.metadata, ch.swisstopo.generalkarte300_papier.metadata, ch.swisstopo.landeskarte500_papier.metadata, ch.swisstopo.landeskarte1000_papier.metadata, ch.swisstopo.luftfahrtkarten-icao_papier.metadata, ch.swisstopo.segelflugkarte_papier.metadata, ch.swisstopo.geologie-geologischer_atlas_papier.metadata, ch.swisstopo.geologie-spezialkarten_schweiz_papier.metadata, ch.swisstopo.geologie-geologische_karte_papier.metadata, ch.swisstopo.geologie-tektonische_karte_papier.metadata, ch.swisstopo.geologie-grundwasservorkommen_papier.metadata, ch.swisstopo.geologie-geodaesie-bouguer_anomalien_papier.metadata, ch.swisstopo.geologie-eiszeit-lgm-raster_papier.metadata, ch.swisstopo.geologie-grundwasservulnerabilitaet_papier.metadata, ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata** have been removed from FSDI services as previously announced
    - **ch.swisstopo.uebersicht-gemeinden** and **ch.swisstopo.uebersicht-schweiz** will be removed from FSDI services with the release on June 29th 2022
    - **ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2, ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2, ch.swisstopo.geologie-gisgeol-flaechen-10to100km2 ch.swisstopo.geologie-gisgeol-flaechen-10x10km, ch.swisstopo.geologie-gisgeol-flaechen-1x1km, ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2, ch.swisstopo.geologie-gisgeol-flaechen-lt10km2, ch.swisstopo.geologie-gisgeol-linien** and **ch.swisstopo.geologie-gisgeol-punkte** will be removed from FSDI services with the release on June 29th 2022
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/2022-03-16-rc9...2022-05-18-rc1>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_220316...r_220518>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Geological Profiles GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_profile>`__ (ch.swisstopo.geologie-geologischer_atlas_profile)                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Latest changes of obstacles <//map.geo.admin.ch/?layers=ch.bazl.luftfahrthindernis-aenderungen>`__ (ch.bazl.luftfahrthindernis-aenderungen)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: Side of tick bite reported <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Control areas - CTA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollbezirke>`__ (ch.bazl.luftraeume-kontrollbezirke)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Control zones - CTR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollzonen>`__ (ch.bazl.luftraeume-kontrollzonen)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Flight information region - FIR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationsgebiet>`__ (ch.bazl.luftraeume-fluginformationsgebiet)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Flight information zones - FIZ <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationszonen>`__ (ch.bazl.luftraeume-fluginformationszonen)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces: Terminal control areas - TMA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-nahkontrollbezirke>`__ (ch.bazl.luftraeume-nahkontrollbezirke)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISS MIL PILOTS CHART <//map.geo.admin.ch/?layers=ch.vbs.swissmilpilotschart>`__ (ch.vbs.swissmilpilotschart)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of restricted and danger areas <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alp. Floodplains outside Fed. Inv. <//map.geo.admin.ch/?layers=ch.bafu.auen-ausserhalb_bundesinventar_alpin>`__ (ch.bafu.auen-ausserhalb_bundesinventar_alpin)                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| update | `Contaminated military sites V2.0 PLR (ch.vbs.kataster-belasteter-standorte-militaer_v2_0.oereb) WMS and OEREB FS only`                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Official street index <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-strassenverzeichnis>`__ (ch.swisstopo.amtliches-strassenverzeichnis)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Housing Inventory <//map.geo.admin.ch/?layers=ch.are.wohnungsinventar-zweitwohnungsanteil>`__ (ch.are.wohnungsinventar-zweitwohnungsanteil)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Air navigation obstacles <//map.geo.admin.ch/?layers=ch.bazl.luftfahrthindernis>`__ (ch.bazl.luftfahrthindernis)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division Dufour Map Raster <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-dufour.metadata>`__ (ch.swisstopo.hiks-dufour.metadata)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division Siegfried Map 50 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-siegfried-ta50.metadata>`__ (ch.swisstopo.hiks-siegfried-ta50.metadata)                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division Siegfried Map 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.hiks-siegfried-ta25.metadata>`__ (ch.swisstopo.hiks-siegfried-ta25.metadata)                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20220316:


Release 20220316 - Wednesday, March 16th 2022
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: the layer ch.bazl.luftfahrthindernis will change its data model with the FSDI Release on May 18th 2022: Attributes to be removed: abortionaccomplished, bbox, coordinates, duration, lk100, sanctiontext, startofconstruction, totallength. Attributes to be added: airport, effectivedate, group, lighting, marking, radius, uuid. More info will follow soon  `here <https://www.bazl.admin.ch/bazl/de/home/fachleute/flugplaetze/luftfahrthindernisse.html>`__
- Announcement: the layer ch.swisstopo.amtliches-strassenverzeichnis will change its complete data model with the FSDI release on May 18th 2022. New model according to the official `model description <https://www.cadastre.ch/content/cadastre-internet/de/services/service/registry/street/_jcr_content/contentPar/tabs_copy/items/dokumente/tabPar/downloadlist/downloadItems/314_1614004254682.download/Spezifikation-DE.pdf>`__ Attributes to be removed: id, label, plzo, gdenr, gdename, type, status, official, validated, modified. Attributes to be added: str_esid, stn_label, zip_label, com_fosnr, com_name, str_type, str_status, str_official, str_valid, str_modified
- Announcement: the layers ch.swisstopo.wanderkarte50_papier.metadata, ch.swisstopo.wanderkarte33_papier.metadata, ch.swisstopo.wanderkarte25-zus_papier.metadata, ch.swisstopo.skitourenkarte-50.metadata, ch.swisstopo.strassenkarte200_papier.metadata,ch.swisstopo.burgenkarte200_papier.metadata, ch.swisstopo.landeskarte25_papier.metadata, ch.swisstopo.landeskarte50_papier.metadata, ch.swisstopo.landeskarte100_papier.metadata, ch.swisstopo.landeskarte200_papier.metadata, ch.swisstopo.generalkarte300_papier.metadata, ch.swisstopo.landeskarte500_papier.metadata, ch.swisstopo.landeskarte1000_papier.metadata, ch.swisstopo.luftfahrtkarten-icao_papier.metadata, ch.swisstopo.segelflugkarte_papier.metadata, ch.swisstopo.geologie-geologischer_atlas_papier.metadata, ch.swisstopo.geologie-spezialkarten_schweiz_papier.metadata, ch.swisstopo.geologie-geologische_karte_papier.metadata, ch.swisstopo.geologie-tektonische_karte_papier.metadata, ch.swisstopo.geologie-grundwasservorkommen_papier.metadata, ch.swisstopo.geologie-geodaesie-bouguer_anomalien_papier.metadata, ch.swisstopo.geologie-eiszeit-lgm-raster_papier.metadata, ch.swisstopo.geologie-grundwasservulnerabilitaet_papier.metadata, ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata will be removed from FSDI services on May 18th 2022.
- Announcement: the layers ch.bfs.arealstatistik-1985, ch.bfs.arealstatistik-1997, ch.bfs.arealstatistik-bodenbedeckung-1985, ch.bfs.arealstatistik-bodenbedeckung-1997, ch.bfs.arealstatistik-bodennutzung, ch.bfs.arealstatistik-bodennutzung-1985, ch.bfs.arealstatistik-bodennutzung-1997 and ch.bfs.arealstatistik-hintergrund have been removed from FSDI services as previously announced
- Announcement: the layer ch.swisstopo.amtliches-gebaeudeadressverzeichnis has the following attributes replaced according to the `official model <https://www.cadastre.ch/content/cadastre-internet/de/services/service/registry/street/_jcr_content/contentPar/tabs_copy/items/dokumente/tabPar/downloadlist/downloadItems/314_1614004254682.download/Spezifikation-DE.pdf>`__ : id is now adr_egaid, str_label is now stn_label, adr_zip is now zip_label
- Announcement the layer ch.bfs.gebaeude_wohnungs_register has the following additional attributes: gschutzr, gebf, gwaerzh1, genh1, gwaersceh1, gwaerdath1, gwaerzh2, genh2, gwaersceh2, gwaerdath2, gwaerzw1, genw1, gwaerscew1, gwaerdatw1, gwaerzw2, genw2, gwaerscew2, gwaerdatw2, wbauj, wabbj, warea, wazim, wkche
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_211215...r_220316>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_211215...r_220316>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reserved zones airports modification V2.0 PLR (ch.bazl.projektierungszonen-flughafenanlagen_aenderung_v2_0.oereb) WMS only`                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Safety zone plan modification V2.0 PLR (ch.bazl.sicherheitszonenplan_aenderung_v2_0.oereb) WMS only`                                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dwellings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Buildings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Population (residents) <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner>`__ (ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner)                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Enterprises <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents in the annual comparison <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_jahresvergleich>`__ (ch.astra.schwerverunfallte-kanton_jahresvergleich)                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Public transport connection quality ARE <//map.geo.admin.ch/?layers=ch.are.gueteklassen_oev>`__ (ch.are.gueteklassen_oev)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Other protected areas AuLaV <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-aulav_uebrige>`__ (ch.bafu.schutzgebiete-aulav_uebrige)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vermessungsstrecken - Querprofilmarke <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Datenbank Querprofile (QP) - Vermessungsstrecken <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIS starting point <//map.geo.admin.ch/?layers=ch.bav.sachplan-infrastruktur-schiene_ausgangslage>`__ (ch.bav.sachplan-infrastruktur-schiene_ausgangslage)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL starting point <//map.geo.admin.ch/?layers=ch.bav.sachplan-infrastruktur-schiene_kraft>`__ (ch.bav.sachplan-infrastruktur-schiene_kraft)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Reserved zones aiports <//map.geo.admin.ch/?layers=ch.bazl.projektierungszonen-flughafenanlagen>`__ (ch.bazl.projektierungszonen-flughafenanlagen)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIL consultation <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Aviation infrastructure <//map.geo.admin.ch/?layers=ch.bazl.sachplan-infrastruktur-luftfahrt_kraft>`__ (ch.bazl.sachplan-infrastruktur-luftfahrt_kraft)                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Safety zone plan <//map.geo.admin.ch/?layers=ch.bazl.sicherheitszonenplan>`__ (ch.bazl.sicherheitszonenplan)                                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Charging points for electric cars <//map.geo.admin.ch/?layers=ch.bfe.ladestellen-elektromobilitaet>`__ (ch.bfe.ladestellen-elektromobilitaet)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Minergie <//map.geo.admin.ch/?layers=ch.bfe.minergiegebaeude>`__ (ch.bfe.minergiegebaeude)                                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Register of Buildings and Dwellings <//map.geo.admin.ch/?layers=ch.bfs.gebaeude_wohnungs_register>`__ (ch.bfs.gebaeude_wohnungs_register)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G1, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g1>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g1)                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G2, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g2>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g2)                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Meat products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cheese <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Confectionery <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-konditoreiwaren>`__ (ch.blw.ursprungsbezeichnungen-konditoreiwaren)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Plant products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-pflanzen>`__ (ch.blw.ursprungsbezeichnungen-pflanzen)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spirits <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-spirituosen>`__ (ch.blw.ursprungsbezeichnungen-spirituosen)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Climate normals sunshine duration 1961-1990 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-sonnenscheindauer_1961_1990>`__ (ch.meteoschweiz.klimanormwerte-sonnenscheindauer_1961_1990)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Climate normals sunshine duration 1981-2010 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-sonnenscheindauer_aktuelle_periode>`__ (ch.meteoschweiz.klimanormwerte-sonnenscheindauer_aktuelle_periode)|
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Climate normals temperature 1961-1990 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-temperatur_1961_1990>`__ (ch.meteoschweiz.klimanormwerte-temperatur_1961_1990)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Climate normals temperature 1981-2010 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-temperatur_aktuelle_periode>`__ (ch.meteoschweiz.klimanormwerte-temperatur_aktuelle_periode)                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Climate normals precipitation 1961-1990 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-niederschlag_1961_1990>`__ (ch.meteoschweiz.klimanormwerte-niederschlag_1961_1990)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Climate normals precipitation 1981-2010 <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimanormwerte-niederschlag_aktuelle_periode>`__ (ch.meteoschweiz.klimanormwerte-niederschlag_aktuelle_periode)              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `AGNES <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-agnes>`__ (ch.swisstopo.fixpunkte-agnes)                                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Planimetric control points LFP1 <//map.geo.admin.ch/?layers=ch.swisstopo.fixpunkte-lfp1>`__ (ch.swisstopo.fixpunkte-lfp1)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Paper map: National Map 1:500'000 <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte500_papier.metadata>`__ (ch.swisstopo.landeskarte500_papier.metadata)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissALTI3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swissalti3d-reliefschattierung>`__ (ch.swisstopo.swissalti3d-reliefschattierung)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `National boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-land-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-land-flaeche.fill)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cantonal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-kanton-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-kanton-flaeche.fill)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `District boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wald>`__ (ch.swisstopo.swisstlm3d-wald)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division hiking map 50 Paper <//map.geo.admin.ch/?layers=ch.swisstopo.wanderkarte50_papier.metadata>`__ (ch.swisstopo.wanderkarte50_papier.metadata)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Journey through time <//map.geo.admin.ch/?layers=ch.swisstopo.zeitreihen>`__ (ch.swisstopo.zeitreihen)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20211215:


Release 20211215 - Wednesday, December 15th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: the layer ch.babs.kulturgueter-anhoerung has been removed from FSDI services as previously announced
- Announcement: the layer ch.bakom.downlink3 has been removed from FSDI services as previously announced
- Announcement: the layers ch.bfs.arealstatistik-1985, ch.bfs.arealstatistik-1997, ch.bfs.arealstatistik-bodenbedeckung-1985, ch.bfs.arealstatistik-bodenbedeckung-1997, ch.bfs.arealstatistik-bodennutzung, ch.bfs.arealstatistik-bodennutzung-1985, ch.bfs.arealstatistik-bodennutzung-1997 and ch.bfs.arealstatistik-hintergrund will be removed from FSDI services on March 16th 2022
- Announcement: the layer ch.swisstopo.fixpunkte-lfp1 has the following structural changes: Removed attributes: y03, x03. Newly added attributes: l_gen_lv95, h_gen_lv95, l_zuv_lv95, h_zuv_lv95 as announced in the api google group
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_211027...r_211215>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_211027...r_211215>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Passenger traffic rail 2050 <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-bahn_zukunft>`__ (ch.are.belastung-personenverkehr-bahn_zukunft)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Passenger/freight traffic road 2050 <//map.geo.admin.ch/?layers=ch.are.belastung-personenverkehr-strasse_zukunft>`__ (ch.are.belastung-personenverkehr-strasse_zukunft)                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Building lines for motorways V2.0 PLR (ch.astra.baulinien-nationalstrassen_v2_0.oereb) WMS and OEREB FS only`                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Building lines for motorways mod. V2.0 PLR (ch.astra.baulinien-nationalstrassen_aenderung_v2_0.oereb) WMS only`                                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reserved zones for motorways V2.0 PLR (ch.astra.projektierungszonen-nationalstrassen_v2_0.oereb) WMS and OEREB FS only`                                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Building lines for railways V2.0 PLR (ch.bav.baulinien-eisenbahnanlagen_v2_0.oereb) WMS and OEREB FS only`                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `CCS public transports V2.0 PLR (ch.bav.kataster-belasteter-standorte-oev_v2_0.oereb) WMS and OEREB FS only`                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reserved zones for public transport facilities V2.0 PLR (ch.bav.projektierungszonen-eisenbahnanlagen_v2_0.oereb) WMS and OEREB FS only`                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Building lines for airports V2.0 PLR (ch.bazl.baulinien-flughafenanlagen_v2_0.oereb) WMS and OEREB FS only`                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `CCS civil aerodromes V2.0 PLR (ch.bazl.kataster-belasteter-standorte-zivilflugplaetze_v2_0.oereb) WMS and OEREB FS only`                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Reserved zones airports V2.0 PLR (ch.bazl.projektierungszonen-flughafenanlagen_v2_0.oereb) WMS and OEREB FS only`                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Safety zone plan V2.0 PLR (ch.bazl.sicherheitszonenplan_v2_0.oereb) WMS and OEREB FS only`                                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Safety zone plan modification V2.0 PLR (ch.bazl.sicherheitszonenplan_aenderung_v2_0.oereb) WMS only`                                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Baulinien Starkstrom V2 ÖREB (ch.bfe.baulinien-starkstromanlagen_v2_0.oereb) WMS and OEREB FS only`                                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Baulinien Starkstroma Änd. V2 ÖREB (ch.bfe.baulinien-starkstromanlagen_aenderung_v2_0.oereb) WMS only`                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Projektierungszonen Starkstrom V2 ÖREB (ch.bfe.projektierungszonen-starkstromanlagen_v2_0.oereb) WMS and OEREB FS only`                                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Projektierungszonen Starkstrom Änd. V2 ÖREB (ch.bfe.projektierungszonen-starkstromanlagen_aenderung_v2_0.oereb) WMS only`                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Climate scenarios indoor climate <//map.geo.admin.ch/?layers=ch.meteoschweiz.klimaszenarien-raumklima>`__ (ch.meteoschweiz.klimaszenarien-raumklima)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Road Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.strassenkarte-200>`__ (ch.swisstopo.strassenkarte-200)                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Contaminated military sites V2.0 PLR (ch.vbs.kataster-belasteter-standorte-militaer_v2_0.oereb) WMS and OEREB FS only`                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Building lines for motorways <//map.geo.admin.ch/?layers=ch.astra.baulinien-nationalstrassen>`__ (ch.astra.baulinien-nationalstrassen)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `PCP Inventory <//map.geo.admin.ch/?layers=ch.babs.kulturgueter>`__ (ch.babs.kulturgueter)                                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Paper map: National Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.landeskarte200_papier.metadata>`__ (ch.swisstopo.landeskarte200_papier.metadata)                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Printed Map: Road Map 1:200'000 <//map.geo.admin.ch/?layers=ch.swisstopo.strassenkarte200_papier.metadata>`__ (ch.swisstopo.strassenkarte200_papier.metadata)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Paper map: General Map 1:300'000 <//map.geo.admin.ch/?layers=ch.swisstopo.generalkarte300_papier.metadata>`__ (ch.swisstopo.generalkarte300_papier.metadata)                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Zones) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Swiss Parks (Perimeter) <//map.geo.admin.ch/?layers=ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter>`__ (ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter)                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Flussgebiete (Einzugsgebiete) HADES <//map.geo.admin.ch/?layers=ch.bafu.hydrologischer-atlas_flussgebiete>`__ (ch.bafu.hydrologischer-atlas_flussgebiete)                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ibex colonies <//map.geo.admin.ch/?layers=ch.bafu.fauna-steinbockkolonien)>`__ (ch.bafu.fauna-steinbockkolonien)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Ski routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.skitouren>`__ (ch.swisstopo-karto.skitouren)                                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe routes <//map.geo.admin.ch/?layers=ch.swisstopo-karto.schneeschuhrouten>`__ (ch.swisstopo-karto.schneeschuhrouten)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Designated wildlife areas <//map.geo.admin.ch/?layers=bafu.wrz-wildruhezonen_portal>`__ (bafu.wrz-wildruhezonen_portal)                                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wildlife reserves <//map.geo.admin.ch/?layers=ch.bafu.wrz-jagdbanngebiete_select>`__ (ch.bafu.wrz-jagdbanngebiete_select)                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway network <//map.geo.admin.ch/?layers=ch.bav.schienennetz>`__ (ch.bav.schienennetz)                                                                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land use statistics standard <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik>`__ (ch.bfs.arealstatistik)                                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Land use statistics cover <//map.geo.admin.ch/?layers=ch.bfs.arealstatistik-bodennutzung>`__ (ch.bfs.arealstatistik-bodennutzung)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tank relocation routes <//map.geo.admin.ch/?layers=ch.vbs.panzerverschiebungsrouten>`__ (ch.vbs.panzerverschiebungsrouten)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissBATHY3D Hillshade <//map.geo.admin.ch/?layers=ch.swisstopo.swissbathy3d-reliefschattierung>`__ (ch.swisstopo.swissbathy3d-reliefschattierung)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Meat products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cheese <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Confectionery <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-konditoreiwaren>`__ (ch.blw.ursprungsbezeichnungen-konditoreiwaren)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Plant products <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-pflanzen>`__ (ch.blw.ursprungsbezeichnungen-pflanzen)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spirits <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-spirituosen>`__ (ch.blw.ursprungsbezeichnungen-spirituosen)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Snowshoe trekking <//map.geo.admin.ch/?layers=ch.swisstopo.schneeschuhwandern>`__ (ch.swisstopo.schneeschuhwandern)                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20211027:


Release 20211027 - Wednesday, October 27th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: the layer ch.babs.kulturgueter-anhoerung will completely be removed from FSDI services on December 15th 2021
- Announcement: the layer ch.bakom.downlink3 will completely be removed from FSDI services on December 15th 2021
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_210908...r_211027>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_210908...r_211027>`__

Geodata
*******
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Altitudinal zones 1975 <//map.geo.admin.ch/?layers=ch.bafu.wald-vegetationshoehenstufen_1975>`__ (ch.bafu.wald-vegetationshoehenstufen_1975)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Potential heat use of water bodies <//map3.geo.admin.ch/?layers=ch.bfe.waermepotential-gewaesser>`__ (ch.bfe.waermepotential-gewaesser)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hail hazard (size), 100 years <//map.geo.admin.ch/?layers=ch.meteoschweiz.hagelgefaehrdung-korngroesse_100_jahre>`__ (ch.meteoschweiz.hagelgefaehrdung-korngroesse_100_jahre)                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Armee- und Kriegsdenkmäler <//map.geo.admin.ch/?layers=ch.vbs.armee-kriegsdenkmaeler>`__ (ch.vbs.armee-kriegsdenkmaeler)                                                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Terrestrial images swisstopo <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-terrestrische_aufnahmen>`__ (ch.swisstopo.lubis-terrestrische_aufnahmen)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Altitudinal zones 2085 less dry <//map.geo.admin.ch/?layers=ch.bafu.wald-vegetationshoehenstufen_2085_weniger_trocken>`__ (ch.bafu.wald-vegetationshoehenstufen_2085_weniger_trocken)                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Altitudinal zones 2085 dry <//map.geo.admin.ch/?layers=ch.bafu.wald-vegetationshoehenstufen_2085_trocken>`__ (ch.bafu.wald-vegetationshoehenstufen_2085_trocken)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Arsenals <//map.geo.admin.ch/?layers=ch.vbs.retablierungsstellen>`__ (ch.vbs.retablierungsstellen)                                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SP Military <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_kraft>`__ (ch.vbs.sachplan-infrastruktur-militaer_kraft)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SPM consultation <//map.geo.admin.ch/?layers=ch.vbs.sachplan-infrastruktur-militaer_anhoerung>`__ (ch.vbs.sachplan-infrastruktur-militaer_anhoerung)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20210908:


Release 20210908 - Wednesday, September 8th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: ...
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_210630...r_210908>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_210630...r_210908>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `145 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_zentral>`__ (ch.bakom.notruf-145_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `145 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_festnetz>`__ (ch.bakom.notruf-145_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `145 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-145_mobilnetz>`__ (ch.bakom.notruf-145_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_zentral>`__ (ch.bakom.notruf-112_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_zentral>`__ (ch.bakom.notruf-117_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_zentral>`__ (ch.bakom.notruf-118_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_zentral>`__ (ch.bakom.notruf-143_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_zentral>`__ (ch.bakom.notruf-144_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_zentral>`__ (ch.bakom.notruf-147_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_festnetz>`__ (ch.bakom.notruf-117_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_festnetz>`__ (ch.bakom.notruf-143_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_festnetz>`__ (ch.bakom.notruf-144_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_festnetz>`__ (ch.bakom.notruf-147_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_mobilnetz>`__ (ch.bakom.notruf-117_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_mobilnetz>`__ (ch.bakom.notruf-143_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_mobilnetz>`__ (ch.bakom.notruf-144_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_mobilnetz>`__ (ch.bakom.notruf-147_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest mix rate NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-waldmischungsgrad>`__ (ch.bafu.landesforstinventar-waldmischungsgrad)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Thermal networks <//map.geo.admin.ch/?layers=ch.bfe.thermische-netze>`__ (ch.bfe.thermische-netze)                                                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Fleischwaren (GGA) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-fleisch>`__ (ch.blw.ursprungsbezeichnungen-fleisch)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Käse (GUB) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-kaese>`__ (ch.blw.ursprungsbezeichnungen-kaese)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Konditoreiwaren (GGA) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-konditoreiwaren>`__ (ch.blw.ursprungsbezeichnungen-konditoreiwaren)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pflanziche Produkte (GUB) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-pflanzen>`__ (ch.blw.ursprungsbezeichnungen-pflanzen)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spirituosen (GUB) <//map.geo.admin.ch/?layers=ch.blw.ursprungsbezeichnungen-spirituosen>`__ (ch.blw.ursprungsbezeichnungen-spirituosen)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of forest damage – projectile <//map.geo.admin.ch/?layers=ch.vbs.waldschadenkarte>`__ (ch.vbs.waldschadenkarte)                                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20210630:


Release 20210630 - Wednesday, June 30th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: the layer ch.swisstopo.konsultation-lk10-landeskarte will completely be removed from FSDI services on Sept. 8th 2021
- Announcement: the layer ch.bafu.bundesinventare-flachmoore_regional has been removed from the FSDI services as previously announced
- Announcement: the layers ch.bafu.showme-gemeinden_hochwasser, ch.bafu.showme-gemeinden_lawinen, ch.bafu.showme-gemeinden_rutschungen, ch.bafu.showme-gemeinden_sturzprozesse, ch.bafu.showme-kantone_hochwasser, ch.bafu.showme-kantone_lawinen, ch.bafu.showme-kantone_rutschungen and ch.bafu.showme-kantone_sturzprozesse have been removed from the FSDI services as previously announced
- `Full changelog <https://github.com/geoadmin/mf-chsdi3/compare/r_210505...r_210630>`__

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_210505...r_210630>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Radioactivity in the atmosphere <//map.geo.admin.ch/?layers=ch.bag.radioaktivitaet-atmosphaere>`__ (ch.bag.radioaktivitaet-atmosphaere)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Vegetation height model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell)                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Surface model NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-vegetationshoehenmodell_relief>`__ (ch.bafu.landesforstinventar-vegetationshoehenmodell_relief)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Forest mix rate NFI <//map.geo.admin.ch/?layers=ch.bafu.landesforstinventar-waldmischungsgrad>`__ (ch.bafu.landesforstinventar-waldmischungsgrad)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accessibility of pharmacies <//map.geo.admin.ch/?layers=ch.bfs.erreichbarkeit-apotheken>`__ (ch.bfs.erreichbarkeit-apotheken)                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Accessibility of restaurants <//map.geo.admin.ch/?layers=ch.bfs.erreichbarkeit-restaurants>`__ (ch.bfs.erreichbarkeit-restaurants)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solar energy: suitability of roofs <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-daecher>`__ (ch.bfe.solarenergie-eignung-daecher)                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Zeckenstichmodell <//map.geo.admin.ch/?layers=ch.bag.zeckenstichmodell>`__ (ch.bag.zeckenstichmodell)                                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product&layers_timestamp=2020&time=2020>`__ (ch.swisstopo.swissimage-product)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tiling SWISSIMAGE Journey thru time <//map.geo.admin.ch/?layers=ch.swisstopo.swissimage-product.metadata&layers_timestamp=2020&time=2020>`__ (ch.swisstopo.swissimage-product.metadata)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Tank relocation routes <//map.geo.admin.ch/?layers=ch.vbs.panzerverschiebungsrouten>`__ (ch.vbs.panzerverschiebungsrouten)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SIN consultation <//map.geo.admin.ch/?layers=ch.astra.sachplan-infrastruktur-strasse_anhoerung>`__ (ch.astra.sachplan-infrastruktur-strasse_anhoerung)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Fens <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-flachmoore>`__ (ch.bafu.bundesinventare-flachmoore)                                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Bathing water quality <//map.geo.admin.ch/?layers=ch.bafu.gewaesserschutz-badewasserqualitaet>`__ (ch.bafu.gewaesserschutz-badewasserqualitaet)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Emergency calls by comune <//map.geo.admin.ch/?layers=ch.bakom.notruf>`__ (ch.bakom.notruf)                                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_festnetz>`__ (ch.bakom.notruf-112_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_mobilnetz>`__ (ch.bakom.notruf-112_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Satellite network <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_satellit>`__ (ch.bakom.notruf-112_satellit)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_festnetz>`__ (ch.bakom.notruf-117_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_mobilnetz>`__ (ch.bakom.notruf-117_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_festnetz>`__ (ch.bakom.notruf-118_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_mobilnetz>`__ (ch.bakom.notruf-118_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_festnetz>`__ (ch.bakom.notruf-143_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_mobilnetz>`__ (ch.bakom.notruf-143_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_festnetz>`__ (ch.bakom.notruf-144_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_mobilnetz>`__ (ch.bakom.notruf-144_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Fixed network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_festnetz>`__ (ch.bakom.notruf-147_festnetz)                                                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Mobile network <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_mobilnetz>`__ (ch.bakom.notruf-147_mobilnetz)                                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `112 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-112_zentral>`__ (ch.bakom.notruf-112_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `117 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-117_zentral>`__ (ch.bakom.notruf-117_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `118 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-118_zentral>`__ (ch.bakom.notruf-118_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `143 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-143_zentral>`__ (ch.bakom.notruf-143_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `144 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-144_zentral>`__ (ch.bakom.notruf-144_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `147 Alarm centers <//map.geo.admin.ch/?layers=ch.bakom.notruf-147_zentral>`__ (ch.bakom.notruf-147_zentral)                                                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Waste incineration plants <//map.geo.admin.ch/?layers=ch.bfe.kehrichtverbrennungsanlagen>`__ (ch.bfe.kehrichtverbrennungsanlagen)                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `GeoCover - Vector Datasets <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover>`__ (ch.swisstopo.geologie-geocover)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division GeoCover <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geocover.metadata>`__ (ch.swisstopo.geologie-geocover.metadata)                                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geological Atlas GA25 <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas>`__ (ch.swisstopo.geologie-geologischer_atlas)                                                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Raster <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas.metadata)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Vector <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_vector.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas_vector.metadata)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division geological atlas 25 Papier <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-geologischer_atlas_papier.metadata>`__ (ch.swisstopo.geologie-geologischer_atlas_papier.metadata)                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Division swissSURFACE3D Raster <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-raster.metadata>`__ (ch.swisstopo.swisssurface3d-raster.metadata)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Monodirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung_monodirektional)         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `swissSURFACE3D Hillshade Multidirectional <//map.geo.admin.ch/?layers=ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional>`__ (ch.swisstopo.swisssurface3d-reliefschattierung-multidirektional)      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Vermessungsstrecken - Querprofilmarke <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-querprofilmarken>`__ (ch.bafu.wasserbau-querprofilmarken)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Datenbank Querprofile (QP) - Vermessungsstrecken <//map.geo.admin.ch/?layers=ch.bafu.wasserbau-vermessungsstrecken>`__ (ch.bafu.wasserbau-vermessungsstrecken)                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Geographical Names swissNAMES3D <//map.geo.admin.ch/?layers=ch.swisstopo.swissnames3d>`__ (ch.swisstopo.swissnames3d)                                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Alps with livestock guardian dogs <//map.geo.admin.ch/?layers=ch.bafu.alpweiden-herdenschutzhunde>`__ (ch.bafu.alpweiden-herdenschutzhunde)                                                                      |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura: Nature Preserves <//map.geo.admin.ch/?layers=ch.pronatura.naturschutzgebiete>`__ (ch.pronatura.naturschutzgebiete)                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20210505:


Release 20210505 - Wednesday, May 5th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: the layers ch.bfe.bikesharing, ch.mobility.standorte and ch.bfe.energiestaedte-energieregionen have been removed from the FSDI services as previously announced
- Announcement: the layer ch.bafu.bundesinventare-flachmoore_regional will be completely removed from the FSDI services in June 2021
- Announcement: the layers ch.bafu.showme-gemeinden_hochwasser, ch.bafu.showme-gemeinden_lawinen, ch.bafu.showme-gemeinden_rutschungen, ch.bafu.showme-gemeinden_sturzprozesse, ch.bafu.showme-kantone_hochwasser, ch.bafu.showme-kantone_lawinen, ch.bafu.showme-kantone_rutschungen and ch.bafu.showme-kantone_sturzprozesse will be completely removed from the FSDI services in June 2021

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_210317...r_210505>`__

Geodata
*******

+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hail hazard (size), 10 years <//map.geo.admin.ch/?layers=ch.meteoschweiz.hagelgefaehrdung-korngroesse_10_jahre>`__ (ch.meteoschweiz.hagelgefaehrdung-korngroesse_10_jahre)                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hail hazard (size), 20 years <//map.geo.admin.ch/?layers=ch.meteoschweiz.hagelgefaehrdung-korngroesse_20_jahre>`__ (ch.meteoschweiz.hagelgefaehrdung-korngroesse_20_jahre)                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hail hazard (size), 50 years <//map.geo.admin.ch/?layers=ch.meteoschweiz.hagelgefaehrdung-korngroesse_50_jahre>`__ (ch.meteoschweiz.hagelgefaehrdung-korngroesse_50_jahre)                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Amphibienwanderungen mit Verkehrskonflikten <//map.geo.admin.ch/?layers=ch.bafu.amphibienwanderung-verkehrskonflikte>`__ (ch.bafu.amphibienwanderung-verkehrskonflikte)                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `ISOS - Photos <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos)                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images cantons <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-kantone>`__ (ch.swisstopo.lubis-luftbilder-dritte-kantone)                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountainbiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.mountainbikeland>`__ (ch.astra.mountainbikeland)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Skating in Switzerland <//map.geo.admin.ch/?layers=ch.astra.skatingland>`__ (ch.astra.skatingland)                                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cycling in Switzerland <//map.geo.admin.ch/?layers=ch.astra.veloland>`__ (ch.astra.veloland)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking in Switzerland <//map.geo.admin.ch/?layers=ch.astra.wanderland>`__ (ch.astra.wanderland)                                                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Interregional wildlife corridor <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierkorridor_national>`__ (ch.bafu.fauna-wildtierkorridor_national)                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Seismic subsoil classes <//map.geo.admin.ch/?layers=ch.bafu.gefahren-baugrundklassen>`__ (ch.bafu.gefahren-baugrundklassen)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `TBE: Side of tick bite reported <//map.geo.admin.ch/?layers=ch.bag.zecken-fsme-faelle>`__ (ch.bag.zecken-fsme-faelle)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Restrictions for drones <//map.geo.admin.ch/?layers=ch.bazl.einschraenkungen-drohnen>`__ (ch.bazl.einschraenkungen-drohnen)                                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerodromes + Heliports <//map.geo.admin.ch/?layers=ch.bazl.flugplaetze-heliports>`__ (ch.bazl.flugplaetze-heliports)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronautical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glider Chart <//map.geo.admin.ch/?layers=ch.bazl.segelflugkarte>`__ (ch.bazl.segelflugkarte)                                                                                                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mil Airspace Chart <//map.geo.admin.ch/?layers=ch.vbs.milairspacechart>`__ (ch.vbs.milairspacechart)                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `SWISS MIL PILOTS CHART <//map.geo.admin.ch/?layers=ch.vbs.swissmilpilotschart>`__ (ch.vbs.swissmilpilotschart)                                                                                 |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Mountain landing sites <//map.geo.admin.ch/?layers=ch.bazl.gebirgslandeplaetze>`__ (ch.bazl.gebirgslandeplaetze)                                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - TMA <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-nahkontrollbezirke>`__ (ch.bazl.luftraeume-nahkontrollbezirke)                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - FIZ <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationszonen>`__ (ch.bazl.luftraeume-fluginformationszonen)                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - FIR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-fluginformationsgebiet>`__ (ch.bazl.luftraeume-fluginformationsgebiet)                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Airspaces - CTR <//map.geo.admin.ch/?layers=ch.bazl.luftraeume-kontrollzonen>`__ (ch.bazl.luftraeume-kontrollzonen)                                                                            |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aeronatutical Chart ICAO <//map.geo.admin.ch/?layers=ch.bazl.luftfahrtkarten-icao>`__ (ch.bazl.luftfahrtkarten-icao)                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Map of restricted and danger areas <//map.geo.admin.ch/?layers=ch.vbs.sperr-gefahrenzonenkarte>`__ (ch.vbs.sperr-gefahrenzonenkarte)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Spitallandeplätze <//map.geo.admin.ch?layers=ch.bazl.spitallandeplaetze>`__ (ch.bazl.spitallandeplaetze)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pro Natura forest reserves <//map.geo.admin.ch/?layers=ch.pronatura.waldreservate>`__ (ch.pronatura.waldreservate)                                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Gravimetric base network <//map.geo.admin.ch/?layers=ch.swisstopo.landesschwerenetz>`__ (ch.swisstopo.landesschwerenetz)                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Glacier Thickness <//map.geo.admin.ch/?layers=ch.swisstopo.geologie-gletschermaechtigkeit>`__ (ch.swisstopo.geologie-gletschermaechtigkeit)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydrography swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-gewaessernetz>`__ (ch.swisstopo.swisstlm3d-gewaessernetz)                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Railway swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-eisenbahnnetz>`__ (ch.swisstopo.swisstlm3d-eisenbahnnetz)                                                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cableways swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-uebrigerverkehr>`__ (ch.swisstopo.swisstlm3d-uebrigerverkehr)                                                         |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Roads and Tracks swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-strassen>`__ (ch.swisstopo.swisstlm3d-strassen)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hiking trails <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wanderwege>`__ (ch.swisstopo.swisstlm3d-wanderwege)                                                                          |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Forest swissTLM3D <//map.geo.admin.ch/?layers=ch.swisstopo.swisstlm3d-wald>`__ (ch.swisstopo.swisstlm3d-wald)                                                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Pollutant releases (SwissPRTR) <//map.geo.admin.ch/?layers=ch.bafu.swissprtr>`__ (ch.bafu.swissprtr)                                                                                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Wind energy plants <//map.geo.admin.ch/?layers=ch.bfe.windenergieanlagen>`__ (ch.bfe.windenergieanlagen)                                                                                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `ISOS - Site records <//map.geo.admin.ch/?layers=ch.bak.bundesinventar-schuetzenswerte-ortsbilder>`__ (ch.bak.bundesinventar-schuetzenswerte-ortsbilder)                                        |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Municipal boundaries <//map.geo.admin.ch/?layers=ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill>`__ (ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill)                               |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Built-up areas VIL <//map.geo.admin.ch/?layers=ch.bazl.bebaute-gebiete_luftfahrtrecht>`__ (ch.bazl.bebaute-gebiete_luftfahrtrecht)                                                             |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations - principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung-uebergeordnet)                       |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Main roads network <//map.geo.admin.ch/?layers=ch.astra.hauptstrassennetz>`__ (ch.astra.hauptstrassennetz)                                                                                     |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Hydropower statistics <//map.geo.admin.ch/?layers=ch.bfe.statistik-wasserkraftanlagen>`__ (ch.bfe.statistik-wasserkraftanlagen)                                                                |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations local <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal>`__ (ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal)   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Traffic counting locations principal <//map.geo.admin.ch/?layers=ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet>`__ (ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet) |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Employment (FTE) <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente>`__ (ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente)                   |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Enterprises <//map.geo.admin.ch/?layers=ch.bfs.betriebszaehlungen-arbeitsstaetten>`__ (ch.bfs.betriebszaehlungen-arbeitsstaetten)                                                              |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Dwellings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_wohnungen)                                                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Buildings <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude>`__ (ch.bfs.volkszaehlung-gebaeudestatistik_gebaeude)                                                    |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Population (residents) <//map.geo.admin.ch/?layers=ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner>`__ (ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner)                           |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G1, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g1>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g1)                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Administrative borders G2, agglomerations <//map.geo.admin.ch/?layers=ch.bfs.generalisierte-grenzen_agglomerationen_g2>`__ (ch.bfs.generalisierte-grenzen_agglomerationen_g2)                  |
+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20210317:

Release 20210317 - Wednesday, March 17th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- Announcement: Changes in SEARCH Service http://api.geo.admin.ch/services/sdiservices.html#search taking effect on 05.05.2021: in the response "weight:" results will change (improved weighting and correct merge of exact + wildcard results). Test the new behaviour on our intgeration plattform (not for operational use):
  - INT SEARCH Service: http://mf-chsdi3.int.bgdi.ch/feature_BGDIINF_SB-1527_fix_search/rest/services/ech/SearchServer
  - INT SEARCH Service example: http://mf-chsdi3.int.bgdi.ch/feature_BGDIINF_SB-1527_fix_search/rest/services/ech/SearchServer?sr=2056&searchText=Hardturmstrasse%20105%208005%20Z%C3%BCrich&lang=de&type=locations
  - INT SEARCH Service example: http://mf-chsdi3.int.bgdi.ch/feature_BGDIINF_SB-1527_fix_search/rest/services/ech/SearchServer?sr=2056&searchText=rotten&lang=de&type=locations
  - CHANGES are documented in the PULL REQUEST: https://github.com/geoadmin/mf-chsdi3/pull/3657
- Announcement: the layers ch.bafu.grundwasserschutzareale, ch.bafu.grundwasserschutzzonen and ch.bafu.gewaesserschutzbereiche have been removed from the FSDI services as previously announced
- Announcement: the layers ch.blw.emapis-beizugsgebiet, ch.blw.emapis-bewaesserung, ch.blw.emapis-elektrizitaetsversorgung, ch.blw.emapis-entwaesserung, ch.blw.emapis-hochbau, ch.blw.emapis-milchleitung, ch.blw.emapis-oekologie, ch.blw.emapis-projektschwerpunkt, ch.blw.emapis-seilbahnen, ch.blw.emapis-wasserversorgung, ch.blw.emapis-wegebau and ch.blw.emapis-zusammenfassung have been removed from the FSDI services as previously announced
- Announcement: the layers ch.bfe.bikesharing, ch.mobility.standorte and ch.bfe.energiestaedte-energieregionen will be completely removed from the FSDI services in May 2021
- Announcement: the layer ch.bafu.bundesinventare-flachmoore_regional will be completely removed from the FSDI services in June 2021
- Announcement: the layers ch.bafu.showme-gemeinden_hochwasser, ch.bafu.showme-gemeinden_lawinen, ch.bafu.showme-gemeinden_rutschungen, ch.bafu.showme-gemeinden_sturzprozesse, ch.bafu.showme-kantone_hochwasser, ch.bafu.showme-kantone_lawinen, ch.bafu.showme-kantone_rutschungen and ch.bafu.showme-kantone_sturzprozesse will be completely removed from the FSDI services in June 2021

`MAP <//map.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_210224...r_210317>`__

Geodata
*******

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Electricity production plants <//map.geo.admin.ch/?layers=ch.bfe.elektrizitaetsproduktionsanlagen>`__ (ch.bfe.elektrizitaetsproduktionsanlagen)                                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Heating advice large apartments <//map.geo.admin.ch/?layers=ch.bfe.erneuerbarheizen-mehrfamilienhaeuser>`__ (ch.bfe.erneuerbarheizen-mehrfamilienhaeuser)                            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hourly average pollen concentration (Beech) <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-pollen-buche-1h>`__ (ch.meteoschweiz.messwerte-pollen-buche-1h)                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hourly average pollen concentration (Oak) <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-pollen-eiche-1h>`__ (ch.meteoschweiz.messwerte-pollen-eiche-1h)                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hourly average pollen concentration (Alder) <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-pollen-erle-1h>`__ (ch.meteoschweiz.messwerte-pollen-erle-1h)                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hourly average pollen concentration (Ash) <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-pollen-esche-1h>`__ (ch.meteoschweiz.messwerte-pollen-esche-1h)                      |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hourly average pollen concentration (Grasses) <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-pollen-graeser-1h>`__ (ch.meteoschweiz.messwerte-pollen-graeser-1h)              |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hourly average pollen concentration (Birche) <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-pollen-birke-1h>`__ (ch.meteoschweiz.messwerte-pollen-birke-1h)                   |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Hourly average pollen concentration (Hazel) <//map.geo.admin.ch/?layers=ch.meteoschweiz.messwerte-pollen-hasel-1h>`__ (ch.meteoschweiz.messwerte-pollen-hasel-1h)                    |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Advice on renewable energy <//map.geo.admin.ch/?layers=ch.bfe.erneuerbarheizen>`__ (ch.bfe.erneuerbarheizen)                                                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Solarenergie: Eignung Fassaden <//map.geo.admin.ch/?layers=ch.bfe.solarenergie-eignung-fassaden>`__ (ch.bfe.solarenergie-eignung-fassaden)                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Official street index <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-strassenverzeichnis>`__ (ch.swisstopo.amtliches-strassenverzeichnis)                                        |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Amtliches Gebäudeadressverzeichnis <//map.geo.admin.ch/?layers=ch.swisstopo.amtliches-gebaeudeadressverzeichnis>`__ (ch.swisstopo.amtliches-gebaeudeadressverzeichnis)               |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Aerial images privates <//map.geo.admin.ch/?layers=ch.swisstopo.lubis-luftbilder-dritte-firmen>`__ (ch.swisstopo.lubis-luftbilder-dritte-firmen)                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a bicycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fahrraeder>`__ (ch.astra.unfaelle-personenschaeden_fahrraeder)                          |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with fatalities <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_getoetete>`__ (ch.astra.unfaelle-personenschaeden_getoetete)                                |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents with personal injury <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_alle>`__ (ch.astra.unfaelle-personenschaeden_alle)                                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a pedestrian <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_fussgaenger>`__ (ch.astra.unfaelle-personenschaeden_fussgaenger)                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents involving a motorcycle <//map.geo.admin.ch/?layers=ch.astra.unfaelle-personenschaeden_motorraeder>`__ (ch.astra.unfaelle-personenschaeden_motorraeder)                     |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_pro_einwohner>`__ (ch.astra.schwerverunfallte-kanton_pro_einwohner)                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Speeding <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_geschwindigkeit>`__ (ch.astra.schwerverunfallte-kanton_geschwindigkeit)            |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents per inhabitant - Alcohol <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_alkohol>`__ (ch.astra.schwerverunfallte-kanton_alkohol)                             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Accidents in the annual comparison <//map.geo.admin.ch/?layers=ch.astra.schwerverunfallte-kanton_jahresvergleich>`__ (ch.astra.schwerverunfallte-kanton_jahresvergleich)             |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


.. _releasenotes_20210224:

Release 20210224 - Wednesday, February 24th 2021
-------------------------------------------------

API & applications
******************

`API <//api3.geo.admin.ch>`__
'''''''''''''''''''''''''''''
- Bug fixes
- All services are now freely accessible, no registration required, no referer checks in place. We updated our terms of use: https://www.geo.admin.ch/terms-of-use, taking effect on 1.3.2021. We still do recommend that you sign-up for our mailing list / forum http://groups.google.com/group/geoadmin-api to get notified regarding announcements.
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
- `Full changelog <https://github.com/geoadmin/mf-geoadmin3/compare/r_201209...r_210224>`__

Geodata
*******

+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Tank relocation routes <//map.geo.admin.ch/?layers=ch.vbs.panzerverschiebungsrouten>`__ (ch.vbs.panzerverschiebungsrouten)                                                           |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| New    | `Future mean runoff (m³/s) and regime <//map.geo.admin.ch/?layers=ch.bafu.mittlere-abfluesse_zukunft>`__ (ch.bafu.mittlere-abfluesse_zukunft)                                         |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Cleantech projects <//map.geo.admin.ch/?layers=ch.bfe.energieforschung>`__ (ch.bfe.energieforschung)                                                                                 |
+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Update | `Interregional wildlife corridor <//map.geo.admin.ch/?layers=ch.bafu.fauna-wildtierkorridor_national>`__ (ch.bafu.fauna-wildtierkorridor_national)                                    |
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
| Update | `Dry grasslands appendix 2 <//map.geo.admin.ch/?layers=ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2>`__ (ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2)  |
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

