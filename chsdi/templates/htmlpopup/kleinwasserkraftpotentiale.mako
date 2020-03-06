<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${h.translate('klwkp_kwprometer', lang)}</td>       <td>${"%.3f" %c['attributes']['kwprometer'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('laenge_m', lang)}</td>               <td>${int(round(c['attributes']['laenge'])) or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('klwkp_gwlnr', lang)}</td>            <td>${c['attributes']['gwlnr']}</td></tr>
</%def>
