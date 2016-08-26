<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('tt_name')}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_land')}</td>         <td>${c['attributes']['land'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_messjahr')}</td>           <td>${c['attributes']['messjahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_instrument')}</td>     <td>${c['attributes']['instrument'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_xi_ch')}</td>         <td>${c['attributes']['xi_ch'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_eta_ch')}</td>         <td>${c['attributes']['eta_ch'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_xi_etrf')}</td>         <td>${c['attributes']['xi_etrf'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_eta_etrf')}</td>         <td>${c['attributes']['eta_etrf'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('tt_symbol')}</td>         <td>${c['attributes']['symbol'] or '-'}</td></tr>
</%def>

