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
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.einzugsgebietsflaeche')}</td>
      <td>${c['attributes']['einzugsgebietsflaeche'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.mit_hoe')}</td>
      <td>${c['attributes']['mit_hoe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.min_hoe')}</td>
      <td>${c['attributes']['min_hoe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.max_hoe')}</td>
      <td>${c['attributes']['max_hoe'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.antv_ab86')}</td>
      <td>${c['attributes']['antv_ab86'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.regimetyp')}</td>
      <td>${c['attributes']['regimtyp'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.hyperlink')}</td>
      <td><a href="${c['attributes']['hyperlink'] or '-'}" target="_blank">${c['attributes']['hyperlink'] or '-'}</a></td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.bafu.hydrologie-untersuchungsgebiete.stationseite')}</td>
      <td><a href="${c['attributes'][url] or '-'}" target="_blank">${_('ch.bafu.hydrologie-untersuchungsgebiete.stationseite')}</a></td>
    </tr>
</%def>
