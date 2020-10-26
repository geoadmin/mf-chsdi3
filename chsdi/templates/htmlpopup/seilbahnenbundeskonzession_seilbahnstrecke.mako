<%inherit file="base.mako"/>
<%namespace name="seilbahnen" file="seilbahnenbundeskonzession.mako"/>

<%def name="table_body(c,lang)">
  ${seilbahnen.anlage()}
  ${seilbahnen.betreiber()}
  <tr><td class="cell-left">${seilbahnen.layer('bahntyp')}</td> <td>${c['attributes']['bahntyp'] or '-'}</td></tr>
  <tr><td class="cell-left">${seilbahnen.layer('fahrzeugtyp')}</td> <td>${c['attributes']['fahrzeugtyp'] or '-'}</td></tr>
  <tr><td class="cell-left">${seilbahnen.layer('hoehendifferenz')}</td> <td>${c['attributes']['hoehendifferenz'] or '-'}</td></tr>
  <tr><td class="cell-left">${seilbahnen.layer('laengeschief')}</td> <td>${c['attributes']['laengeschief'] or '-'}</td></tr>
</%def>
