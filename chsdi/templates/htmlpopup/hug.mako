<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == ('de') :
        url = 'stationsseite_de'
    elif lang == ('fr') :
        url = 'stationsseite_fr'
    elif lang == ('it') :
        url = 'stationsseite_fr'
    elif lang == ('en') :
        url = 'stationsseite_de'
    else :
        url = 'stationsseite_de'
%>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.name', lang)}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.einzugsgebietsflaeche', lang)}</td>
      <td>${c['attributes']['einzugsgebietsflaeche'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.mit_hoe', lang)}</td>
      <td>${c['attributes']['mit_hoe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.min_hoe', lang)}</td>
      <td>${c['attributes']['min_hoe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.max_hoe', lang)}</td>
      <td>${c['attributes']['max_hoe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.antv_ab86', lang)}</td>
      <td>${c['attributes']['antv_ab86'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.regimetyp', lang)}</td>
      <td>${c['attributes']['regimtyp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.hyperlink', lang)}</td>
      <td><a href="${c['attributes']['hyperlink'] or '-'}" target="_blank">${c['attributes']['hyperlink'] or '-'}</a></td>
    </tr>
    <tr>
      <td class="cell-left">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.stationseite', lang)}</td>
      <td><a href="${c['attributes'][url] or '-'}" target="_blank">${h.translate('ch.bafu.hydrologie-untersuchungsgebiete.stationseite', lang)}</a></td>
    </tr>
</%def>
