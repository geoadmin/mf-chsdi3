<%inherit file="base.mako"/>
<%namespace file="seilbahnenbundeskonzession.mako" import="seilbahnen"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.bav.seilbahnen-bundeskonzession.'
%>
  ${seilbahnen()}
  <tr><td class="cell-left">${_(layer + 'bp_name')}</td> <td>${c['attributes']['bp_name'] or '-'}</td></tr>
  <tr><td class="cell-left">${_(layer + 'bp_nummer')}</td> <td>${c['attributes']['bp_nummer'] or '-'}</td></tr>
</%def>
