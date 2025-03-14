<%
from platform import python_version
version = python_version()
%>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">

    <style type="text/css">
      html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
      }
    </style>
    <title>CHSDI 3</title>
  </head>
  <body>
      <h1>Python version: ${version}</h1>
      <h1>Build info</h1>
          <a href="info.json">info.json</a> <br>
      <h1 id="title">Python translations</h1>
          <a href="testi18n?lang=de">Default to de</a> <br>
          <a href="testi18n?lang=en">En to en</a> <br>
          <a href="testi18n?lang=toto">If not in available languages to browser default (or de)</a> <br>
      <h1 id="title">Services</h1>
      <h2 id="loaderjs">Loader js</h2>
          <a href="loader.js">Link to api</a> <br>
          <a href="loader.js?lang=fr">Link to api in french</a> <br>
          <a href="loader.js?mode=debug">Link to api in debug mode</a> <br>
      <h2 id="checkers">Checkers</h2>
          <a href="checker">Checker for home page</a> <br>
          <a href="checker_dev">Checker for dev page</a> <br>
      <h2 id="mapservices">Map Services</h2>
          <h3>Mapservice (Layer metadata)</h3>
          <a href="rest/services/ech/MapServer">Topic (ech)</a> <br>
          <a href="rest/services/ech/MapServer?searchText=bern">Topic with fulltext search on the column "volltextsuche, bod id and geocat id"</a> <br>
          <h3>Identify</h3>
          <a href="rest/services/ech/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=545000,145000,555000,155000&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bafu.bundesinventare-bln">Identify using an envelope (bbox)</a> <br>
          <a href="rest/services/ech/MapServer/identify?geometryType=esriGeometryPoint&geometry=653246,173129&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln">Identify using a simple point and a tolerance of 5 pixels</a> <br>
          <a href='rest/services/ech/MapServer/identify?geometryType=esriGeometryPoint&geometry={"x":653246,"y":173129,"spatialReference":{"wkid":21781}}&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln'>Identify using a complexe point  {x:, y:, spatialReference: } </a> <br>
          <a href='rest/services/ech/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=630000,245000,645000,265000&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=5&layers=all:ch.bafu.bundesinventare-bln'>Identify using an bbox and tolerance of 5 pixels </a> <br>
          <a href='rest/services/all/MapServer/identify?geometryType=esriGeometryPoint&geometry=630853.809670509,170647.93120352627&geometryFormat=geojson&imageDisplay=1920,734,96&mapExtent=134253.80967050896,-21102.06879647367,1382253.8096705088,455997.9312035263&tolerance=5&layers=all:ch.swisstopo.zeitreihen&timeInstant=1936'>Identify using time instant on layer zeitreihen</a> <br>
          <a href='rest/services/ech/MapServer/identify?geometryType=esriGeometryPolygon&geometry={"rings"%20:%20[[%20[630000,%20245000],%20[645000,245000],%20[645000,265000],%20[630000,265000],%20[630000,%20245000]%20]],"spatialReference"%20:%20{"wkid"%20:%2021781}}&imageDisplay=500,600,96&mapExtent=548945.5,147956,549402,148103.5&tolerance=1&layers=all:ch.bafu.bundesinventare-bln'>Identify using a polygon</a> <br>
          <a href="rest/services/ech/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=630000,245000,645000,265000&imageDisplay=500,600,96&layers=all:ch.bafu.bundesinventare-bln&mapExtent=548945.5,147956,549402,148103.5&tolerance=1">Identify (default to esri geojson)</a> <br>
          <a href="rest/services/ech/MapServer/identify?geometryFormat=geojson&geometryType=esriGeometryEnvelope&geometry=630000,245000,645000,265000&imageDisplay=500,600,96&layers=all:ch.bafu.bundesinventare-bln&mapExtent=548945.5,147956,549402,148103.5&tolerance=1">Identify (requesting geometryFormat=geojson)</a> <br>
          <a href="rest/services/inspire/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=630000,245000,645000,265000&imageDisplay=500,350,96&mapExtent=545132.87362333,147068.69380758,550132.87362333,150568.69380758&tolerance=1&searchText=AG 19.0.3&layers=all:ch.astra.ivs-nat">Identify on mutiple queryable attributes</a> <br>
          <a href="rest/services/ech/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=630000,245000,645000,265000&imageDisplay=500,350,96&mapExtent=545132.87362333,147068.69380758,550132.87362333,150568.69380758&tolerance=1&layers=all&callback=cb">Identify - example with callback</a> <br>
          <a href="/rest/services/ech/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=630000,245000,645000,265000&imageDisplay=500,600,96&mapExtent=545132.87362333,147068.69380758,550132.87362333,150568.69380758&tolerance=1&layers=all&returnGeometry=false">Identify - without geometry</a> <br>
          <a href="/rest/services/api/MapServer/identify?geometry=618953,170093&geometryType=esriGeometryPoint&imageDisplay=1920,576,96&layers=all:ch.bav.kataster-belasteter-standorte-oev_v2_0.oereb&mapExtent=671164.31244,253770,690364.31244,259530&tolerance=5&geometryFormat=interlis">Identify - geometryFormat=interlis on Oereb layers</a>
          <h3>Indentify: with query</h3>
          <a href="/rest/services/api/MapServer/identify?geometryType=esriGeometryEnvelope&geometry=502722.0065086734,36344.074765040714,745822.0065086735,253444.07476504074&imageDisplay=0,0,0&mapExtent=0,0,0,0&tolerance=0&layers=all:ch.bazl.luftfahrthindernis&returnGeometry=true&geometryFormat=geojson&obstacletype=%27Antenna%27">Query 'ch.bazl.luftfahrthindernis' for 'Antenna' with a bbox</a> <br>
          <a href="rest/services/api/MapServer/ch.bazl.luftfahrthindernis/attributes/obstacletype">Get some values for attribute 'obstacletype'</a> <br>
          <h3>Get the attributes of layer</h3>
          <a href="/rest/services/ech/MapServer/ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata">Returns all the attributes of the layer ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata</a>
          <h3>Find</h3>
          <a href="rest/services/ech/MapServer/find?layer=ch.bafu.bundesinventare-bln&searchText=Lavaux&searchField=bln_name&returnGeometry=false">Find Lavaux in the field bln_name of the layer ch.bafu.bundesinventare-bln</a> <br>
          <h3>Releases Service</h3>
          <a href="rest/services/ech/MapServer/ch.swisstopo.zeitreihen/releases?geometry=548945.5,147956,549402,148103.5&geometryType=esriGeometryEnvelope&mapExtent=611399.9999999999,158650,690299.9999999999,198150&imageDisplay=500,500,96">Zeitreihen Layer</a> <br>
          <a
          href="rest/services/ech/MapServer/ch.swisstopo.zeitreihen/releases?geometry=618953,170093&geometryType=esriGeometryPoint&mapExtent=647570.722,187429.722,653229.277,183690.277&imageDisplay=800,530,96">Zeitreihen
          Layer2</a> <br>

          <h3>Varia</h3>
          <a href="rest/services/ech/MapServer/ch.bafu.nabelstationen/LAU">Get Feature with id LAU</a> <br>
          <a href="rest/services/ech/MapServer/ch.bafu.nabelstationen/LAU/htmlPopup">Html Popup Ex LAU</a> <br>
          <a href="rest/services/ech/MapServer/ch.bafu.bundesinventare-jagdbanngebiete/1/htmlPopup?lang=fr&callback=cb">Html Popup Ex 2 with callback</a> <br>
          <a href="rest/services/ech/MapServer/ch.astra.ivs-reg_loc/54967/htmlPopup">Html Popup Ex 3</a> <br>
          <a href="rest/services/ech/MapServer/ch.kantone.cadastralwebmap-farbe/11/htmlPopup?lang=it">Html popup Ex 4 cadastral web map</a> <br>
          <a href="rest/services/ech/MapServer/ch.bakom.radio-fernsehsender/5/extendedHtmlPopup">Extended html content Ex 1</a> <br>
          <a href="rest/services/ech/MapServer/ch.bafu.bundesinventare-bln/legend">Get Legend Ex 1</a> <br>
          <a href="rest/services/ech/MapServer/ch.bafu.bundesinventare-jagdbanngebiete/legend?lang=fr&callback=cb">Get Legend Ex 2 with callback</a> <br>
          <a href='rest/services/inspire/1.0.0/WMTSCapabilities.xml'>WMTS capabilities inspire</a> <br>

      <h2>New style config (in directory "configs")</h2>
      <em>Only behind Apache!</em>
      layersConfig<a href='configs/fr/layersConfig.json'>configs/fr/layersConfig.json</a><br />
      Server-side translation (gettext)<a href='configs/fr/translations.json'>configs/fr/translations.json</a><br />
      Topics catalog <a href='configs/fr/catalog.bafu.json'>configs/fr/catalog.bafu.json</a><br />
      Services (topic list)<a href='configs/services.json'>configs/services.json</a><br />

      <h2>Topic Listing</h2>
          <a href='rest/services'>List all the available topics</a> <br>

      <h2>Layers Configuration</h2>
          <a href='rest/services/ech/MapServer/layersConfig'>Get the layers configuration for topic ech</a> <br>
          <a href='rest/services/all/MapServer/layersConfig'>Get the layers configuration for all topics</a> <br>

      <h2>CatalogService (non ESRI)</h2>
          <a href="rest/services/blw/CatalogServer?callback=callback">Catalog for topic 'blw'</a>

      <h2>Search</h2>
      <h3>Layers Search (type=layers)</h3>
          <a href="rest/services/inspire/SearchServer?searchText=wand&type=layers">Search for layers only</a> <br>
          <a href="rest/services/inspire/SearchServer?searchText=bois&type=layers&lang=fr">Search for layers only (lang fr)</a> <br>
      <h3>Locations Search (type=locations)</h3>
      <h4>Locations (no bounding box)</h4>
          <a href="rest/services/inspire/SearchServer?searchText=wasser&type=locations">Search for 'Wasser' in SwissSearch in Inpsire</a> <br>
          <a
          href="rest/services/blw/SearchServer?searchText=wasser&type=locations">Search for 'Wasser' in SwissSearch in Blw</a> <br>
      <h3>Feature Search (type=featuresearch)</h3>
      <h4>Features (bounding box for features only)</h4>
          <a href="rest/services/inspire/SearchServer?searchText=vd
          446&features=ch.astra.ivs-reg_loc&type=featuresearch&bbox=551306.5625,167918.328125,551754.125,168514.625">Search for
          features in ch.astra.ivs-reg_loc (without bbox, features within the bbox)</a> <br>
      <h4>Features and time </h4>
          <a
          href="rest/services/inspire/SearchServer?searchText=19810590048970&features=ch.swisstopo.lubis-luftbilder_farbe&type=featuresearch&bbox=542199.5,206799.5,542200.5,206800.5&timeInstant=1981&timeEnabled=true">Search for features
          in ch.swisstopo.lubis-luftbilder_farbe with timeInstant parameter (1 result)</a> <br>
          <a
          href="rest/services/inspire/SearchServer?searchText=19810590048970&features=ch.swisstopo.lubis-luftbilder_farbe&type=featuresearch&bbox=542199.5,206799.5,542200.5,206800.5&timeInstant=1981&timeEnabled=true">Search for features
          in ch.swisstopo.lubis-luftbilder_farbe with timeStamps parameter (1 result)</a> <br>
          <a
          href="rest/services/inspire/SearchServer?searchText=19810590048970&features=ch.swisstopo.lubis-luftbilder_farbe&type=featuresearch&bbox=542199.5,206799.5,542200.5,206800.5&timeStamps=1953&timeEnabled=true">Search for features
          in ch.swisstopo.lubis-luftbilder_farbe with time parameter (no  results)</a> <br>
          <a
          href="rest/services/inspire/SearchServer?searchText=19&features=ch.swisstopo.lubis-luftbilder_farbe&type=featuresearch&bbox=568465,187823,606865,201423&timeInstant=1998&timeEnabled=true">Search for features
          in ch.swisstopo.lubis-luftbilder_farbe
          with time parameter (several  results)</a> <br>
          <a href="rest/services/inspire/SearchServer?features=ch.bafu.hydrologie-gewaesserzustandsmessstationen&type=featuresearch&searchText=4331">Search for features using that matches a given searchText in their search fields</a> <br>
      <h2>Attributes values</h2>
      <a href="rest/services/api/MapServer/ch.bazl.luftfahrthindernis/attributes/obstacletype">Possible values for attribute 'obstacletype' of layer 'ch.bazl.luftfahrthindernis'</a><br />
      <a href="rest/services/api/MapServer/ch.bazl.luftfahrthindernis/attributes/startofconstruction">Possible values for attribute 'startofconstruction' of layer 'ch.bazl.luftfahrthindernis'</a><br />
      <h2>Attributes description</h2>
      <a href="rest/services/api/MapServer/ch.bazl.luftfahrthindernis">Attributes of layer 'ch.bazl.luftfahrthindernis'</a><br />
      <br/>
      <br/>
  </body>
</html>
