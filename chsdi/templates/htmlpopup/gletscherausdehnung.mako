<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.swisstopo.geologie-gletscherausdehnung.'
%>
<tr><td class="cell-left">${_(layer + 'name')}</td> <td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'sgi-id')}</td> <td>${c['attributes']['sgi_id'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'area_km2')}</td> <td>${c['attributes']['area_km2'] or '-'}</td></tr>
</%def>
