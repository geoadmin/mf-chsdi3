<%inherit file="base.mako"/>
<%namespace file="seilbahnenbundeskonzession.mako" import="seilbahnen"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.bav.seilbahnen-bundeskonzession.'
%>
  ${seilbahnen()}
  <tr><td class="cell-left">${_(layer + 'bauwerkstyp')}</td> <td>${c['attributes']['bauwerkstyp'] or '-'}</td></tr>
</%def>
