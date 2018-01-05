<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
layerBodId = c['layerBodId']
%>
  <% c['stable_id'] = False %>
  <tr><td class="cell-left">${_('ch.bfs.generalisierte-grenzen_agglomerationen_g1.gmdnr')}</td>         <td>${c['attributes']['gmd_nr'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfs.generalisierte-grenzen_agglomerationen_g1.gmdname')}</td>       <td>${c['attributes']['gmd_name'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfs.generalisierte-grenzen_agglomerationen_g1.acode')}</td>         <td>${c['attributes']['acode'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfs.generalisierte-grenzen_agglomerationen_g1.aname')}</td>         <td>${c['attributes']['aname'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('ch.bfs.generalisierte-grenzen_agglomerationen_g1.area_ha')}</td>       <td>${int(round(c['attributes']['area_ha'])) or '-'}</td></tr>
</%def>

