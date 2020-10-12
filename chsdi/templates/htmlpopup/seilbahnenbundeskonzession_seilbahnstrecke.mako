<%inherit file="base.mako"/>
<%namespace file="seilbahnenbundeskonzession.mako" import="seilbahnen"/>

<%def name="table_body(c,lang)">
<%
  layer = 'ch.bav.seilbahnen-bundeskonzession.'
%>
  ${seilbahnen()}
  <tr><td class="cell-left">${_(layer + 'bahntyp')}</td> <td>${c['attributes']['bahntyp'] or '-'}</td></tr>
  <tr><td class="cell-left">${_(layer + 'fahrzeugtyp')}</td> <td>${c['attributes']['fahrzeugtyp'] or '-'}</td></tr>
  <tr><td class="cell-left">${_(layer + 'hoehendifferenz')}</td> <td>${c['attributes']['hoehendifferenz'] or '-'}</td></tr>
  <tr><td class="cell-left">${_(layer + 'laengeschief')}</td> <td>${c['attributes']['laengeschief'] or '-'}</td></tr>
</%def>
