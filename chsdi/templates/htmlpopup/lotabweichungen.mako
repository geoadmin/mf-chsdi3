<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.name', lang)}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.land', lang)}</td>         <td>${c['attributes']['land'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.messjahr', lang)}</td>           <td>${c['attributes']['messjahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.instrument', lang)}</td>     <td>${c['attributes']['instrument'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.xi_ch', lang)}</td>         <td>${c['attributes']['xi_ch'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.eta_ch', lang)}</td>         <td>${c['attributes']['eta_ch'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.xi_etrf', lang)}</td>         <td>${c['attributes']['xi_etrf'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.eta_etrf', lang)}</td>         <td>${c['attributes']['eta_etrf'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.swisstopo.lotabweichungen.symbol', lang)}</td>         <td>${c['attributes']['symbol'] or '-'}</td></tr>
</%def>

