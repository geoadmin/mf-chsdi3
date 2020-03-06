<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
% if c['attributes']['type_geom'] == 'point'  : 
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.name', lang)}</td>   <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.sortnr', lang)}</td>   <td>${c['attributes']['sortnr']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.kilometerwert', lang)}</td>   <td>${c['attributes']['kilometerwert']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.sektorlaenge', lang)}</td>   <td>${c['attributes']['sektorlaenge']}</td></tr>
% elif c['attributes']['type_geom'] == 'line' :
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.eigentuemer', lang)}</td>   <td>${c['attributes']['eigentuemer']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.segmentname', lang)}</td>   <td>${c['attributes']['segmentname']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.strassennummer', lang)}</td>   <td>${c['attributes']['strassennummer']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.bezeichnung', lang)}</td>   <td>${c['attributes']['bezeichnung']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.nationalstrassenachsen.positionscode', lang)}</td>   <td>${c['attributes']['positionscode']}</td></tr>
% endif
</%def>
