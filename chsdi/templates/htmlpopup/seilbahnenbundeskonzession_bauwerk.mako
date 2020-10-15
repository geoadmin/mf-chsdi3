<%inherit file="base.mako"/>
<%namespace name="seilbahnen" file="seilbahnenbundeskonzession.mako"/>

<%def name="table_body(c,lang)">
  ${seilbahnen.anlage()}
  ${seilbahnen.betreiber()}
  <tr><td class="cell-left">${seilbahnen.layer('bauwerkstyp')}</td> <td>${c['attributes']['bauwerkstyp'] or '-'}</td></tr>
</%def>
