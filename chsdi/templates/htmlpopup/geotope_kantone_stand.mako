<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.swisstopo.geologie-geotope_kantone_stand.'
%>
<tr><td class="cell-left">${_(layer + 'name')}</td> <td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${_(layer + 'sigel')}</td> <td>${c['attributes']['sigel'] or '-'}</td></tr>

<%
  url_path = c['attributes']['dataviewer'] or '-'
%>
<tr>
<td class="cell-left">${_(layer + 'dataviewer')}</td>
% if url_path == '-':
<td> ${url_path} </td>
% else:
<td><a href=${url_path} target="_blank">${url_path}</a></td>
% endif
</tr>
</%def>
