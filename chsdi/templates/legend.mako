# -*- coding: utf-8 -*-

<%
  c = legend['layer']
  hasLegend = legend['hasLegend']
  host = h.make_agnostic(request.host_url + request.uscript_name)
  lang = request.lang
  pdf_legends = ('ch.bafu.typisierung-fliessgewaesser',
                 'ch.swisstopo.geologie-eiszeit-lgm-raster',
                 'ch.swisstopo.geologie-geologische_karte',
                 'ch.swisstopo.geologie-gravimetrischer_atlas',
                 'ch.swisstopo.geologie-hydrogeologische_karte-grundwasservorkommen',
                 'ch.swisstopo.geologie-hydrogeologische_karte-grundwasservulnerabilitaet',
                 'ch.swisstopo.geologie-tektonische_karte',
                 'ch.astra.ivs-gelaendekarte',
                 'ch.astra.ausnahmetransportrouten',
                 'ch.bazl.luftfahrtkarten-icao',
                 'ch.bazl.segelflugkarte',
                 'ch.kantone.cadastralwebmap-farbe',
                 'ch.swisstopo.swisstlm3d-karte-farbe',
                 'ch.swisstopo.swisstlm3d-karte-grau',
                 'ch.swisstopo.pixelkarte-farbe-pk1000.noscale',
                 'ch.swisstopo.pixelkarte-farbe-pk500.noscale',
                 'ch.swisstopo.pixelkarte-farbe-pk200.noscale',
                 'ch.swisstopo.pixelkarte-farbe-pk100.noscale',
                 'ch.swisstopo.pixelkarte-farbe-pk50.noscale',
                 'ch.swisstopo.pixelkarte-farbe-pk25.noscale',
                 'ch.swisstopo.landeskarte-farbe-10',
                 'ch.swisstopo.landeskarte-grau-10',
                 'ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200',
                 'ch.vbs.grunddispositiv-zeus',
                 'ch.swisstopo-karto.skitouren',
                 'ch.swisstopo-karto.schneeschuhrouten',
                 'ch.vbs.milairspacechart')
  if c['layerBodId'] in pdf_legends:
      legend_url_pdf = host + '/static/images/legends/' + c['layerBodId'] + '_' + lang + '_big.pdf'
  else:
      legend_url_pdf = False
  legend_url = host + '/static/images/legends/' + c['layerBodId'] + '_' + lang + '.png'
  times = c['attributes']['dataStatus'] if 'dataStatus' in c['attributes'] else '-'

  if 'wmsUrlResource' in c['attributes']:
      wms_urls = c['attributes']['wmsUrlResource']
      wms_url = wms_urls.split(' ', 1)[0]

%>
<div class="legend-container">
<div class="legend-header">
% if 'dataOwner' in c['attributes']:
  <p class='bod-title'><span>${c['fullName'] or '-'}</span> (${c['attributes']['dataOwner'] or '-'})</p>
% endif
% if 'abstract' in c['attributes']:
  <p class='legend-abstract'>${c['attributes']['abstract'] or '-'|n}</p>
% endif
</div>
<div class="legend-footer">
% if hasLegend:
  <br>
  <span>${_('Legend')}</span><br>
% if legend_url_pdf:
  <a href="${legend_url_pdf}" target="_blank"><img src="${legend_url}"></img></a><br>
% else:
  <div class="img-container">
    <img src=${legend_url} alt="layer legend img"/>
  </div>
  <br><br>
% endif
% endif
  <span>${_('Information')}</span><br>
  <table>
    <tr><td>${_('geobasisdatensatz')}</td> <td>${c['attributes']['bundCollectionNumber'] if 'bundCollectionNumber' in c['attributes'] else '-'}</td></tr>
% if 'scaleLimit' in c['attributes']:
    <tr><td>${_('Gueltiger Massstabsbereich')}</td> <td>${c['attributes']['scaleLimit']}</td></tr>
% endif
    <tr><td>${_('Metadaten')}</td>
% if 'idGeoCat' in c:
  % if lang in ('de', 'rm'):
      <td><a target="_blank" href="http://www.geocat.ch/geonetwork/srv/deu/metadata.show?uuid=${c['idGeoCat']}&currTab=simple">
  % elif lang == 'fr':
      <td><a target="_blank" href="http://www.geocat.ch/geonetwork/srv/fra/metadata.show?uuid=${c['idGeoCat']}&currTab=simple">
  % elif lang == 'it':
      <td><a target="_blank" href="http://www.geocat.ch/geonetwork/srv/ita/metadata.show?uuid=${c['idGeoCat']}&currTab=simple">
  % else:
      <td><a target="_blank" href="http://www.geocat.ch/geonetwork/srv/eng/metadata.show?uuid=${c['idGeoCat']}&currTab=simple">
  % endif
      ${_('layer_geocat_text')}</a></td>
% else:
      <td>-</td>
% endif
    </tr>
    <tr>
      <td>${_('Detailbeschreibung')}</td>
% if 'urlDetails' in c['attributes']:
      <td><a href="${c['attributes']['urlDetails']}" target="new">${_('layer_url_text')}</a></td>
% else:
      <td>-</td>
% endif
    </tr>
    <tr>
      <td>${_('Datenbezug')}</td>
% if 'downloadUrl' in c['attributes']:
      <td><a href="${c['attributes']['downloadUrl']}" target="new">${_('layer_url_download_text')}</a></td>
% else:
      <td>-</td>
% endif
    </tr>
    <tr>
      <td>${_('Thematisches Geoportal')}</td>
% if 'urlApplication' in c['attributes']:
      <td><a href="${c['attributes']['urlApplication']}" target="new">${_('layer_url_portal_text')}</a></td>
% else:
      <td>-</td>
% endif
    </tr>
    <tr>
      <td>${_('WMS Dienst')}</td>
% if 'wmsUrlResource' in c['attributes']:
      <td><a href="${wms_url}" target="new">${_('wms_resource_text')}</a></td>
% else:
      <td>-</td>
% endif
    </tr>
    <tr>
      <td>${_('Datenstand')}</td>
      <td>${h.parse_date_datenstand(times)}</td>
    </tr>
  </table>
</div>
</div>
