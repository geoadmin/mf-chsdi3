<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.name')}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.land')}</td>         <td>${c['attributes']['land'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.messjahr')}</td>           <td>${c['attributes']['messjahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.instrument')}</td>     <td>${c['attributes']['instrument'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.xi_ch')}</td>         <td>${c['attributes']['xi_ch'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.eta_ch')}</td>         <td>${c['attributes']['eta_ch'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.xi_etrf')}</td>         <td>${c['attributes']['xi_etrf'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.eta_etrf')}</td>         <td>${c['attributes']['eta_etrf'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lotabweichungen.symbol')}</td>         <td>${c['attributes']['symbol'] or '-'}</td></tr>
</%def>

