<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.swisstopo.geologie-geotope_kantone_stand.'
%>
  <tr><td class="cell-left">${_('anlagenr')}</td> <td>${c['attributes']['anlagenr'] or '-'}</td></tr>
  <tr><td class="cell-left">${_('anlagename')}</td> <td>${c['attributes']['anlagename'] or '-'}</td></tr>
</%def>
