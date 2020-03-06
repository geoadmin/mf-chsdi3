<%inherit file="base.mako"/>

<%def name="table_body(c, land)">
    <tr><td class="cell-left">${h.translate('gewaessername', lang)}</td>    <td>${c['attributes']['gewaesser'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('krebsart', lang)}</td>    <td>${c['attributes']['art_lat'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('nachweisjahr', lang)}</td>    <td>${c['attributes']['jahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('nachweisnummer', lang)}</td>    <td>${c['attributes']['kennummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('nachweisort', lang)}</td>    <td>${c['attributes']['ort'] or '-'}</td></tr>
</%def>

