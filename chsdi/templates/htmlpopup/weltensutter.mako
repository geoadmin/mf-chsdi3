<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('wsname', lang)}</td>    <td>${c['attributes']['nom'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('wsnummer', lang)}</td>    <td>${c['attributes']['no_surface'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('wstyp', lang)}</td>    <td>${c['attributes']['ty_surface'] or '-'}</td></tr>
</%def>

