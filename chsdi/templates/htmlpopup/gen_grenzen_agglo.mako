<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
layerBodId = c['layerBodId']
%>
  <% c['stable_id'] = False %>
  <tr><td class="cell-left">${t.translate('ch.bfs.generalisierte-grenzen_agglomerationen_g1.gmdnr', lang)}</td>         <td>${c['attributes']['gmd_nr'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfs.generalisierte-grenzen_agglomerationen_g1.gmdname', lang)}</td>       <td>${c['attributes']['gmd_name'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfs.generalisierte-grenzen_agglomerationen_g1.acode', lang)}</td>         <td>${c['attributes']['acode'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfs.generalisierte-grenzen_agglomerationen_g1.aname', lang)}</td>         <td>${c['attributes']['aname'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.translate('ch.bfs.generalisierte-grenzen_agglomerationen_g1.area_ha', lang)}</td>       <td>${int(round(c['attributes']['area_ha'])) or '-'}</td></tr>
</%def>

