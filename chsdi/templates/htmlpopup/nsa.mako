<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
% if c['attributes']['type_geom'] == 'point'  : 
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.name')}</td>   <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.sortnr')}</td>   <td>${c['attributes']['sortnr']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.kilometerwert')}</td>   <td>${c['attributes']['kilometerwert']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.sektorlaenge')}</td>   <td>${c['attributes']['sektorlaenge']}</td></tr>
% elif c['attributes']['type_geom'] == 'line' :
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.eigentuemer')}</td>   <td>${c['attributes']['eigentuemer']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.segmentname')}</td>   <td>${c['attributes']['segmentname']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.strassennummer')}</td>   <td>${c['attributes']['strassennummer']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.bezeichnung')}</td>   <td>${c['attributes']['bezeichnung']}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.nationalstrassenachsen.positionscode')}</td>   <td>${c['attributes']['positionscode']}</td></tr>
% endif
</%def>
