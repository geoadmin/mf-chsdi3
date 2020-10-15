<%inherit file="base.mako"/>
<%namespace name="seilbahnen" file="seilbahnenbundeskonzession.mako"/>

<%def name="table_body(c,lang)">
  ${seilbahnen.anlage()}
  <tr><td class="cell-left">${seilbahnen.layer('bp_nummer')}</td> <td>${c['attributes']['bp_nummer'] or '-'}</td></tr>
  <tr><td class="cell-left"> ${seilbahnen.layer('bp_name')}</td> <td>${c['attributes']['bp_name'] or '-'}</td></tr>
  ${seilbahnen.betreiber()}
  <tr><td class="cell-left">${seilbahnen.layer('stationstyp')}</td> <td>${c['attributes']['stationstyp'] or '-'}</td></tr>
</%def>
