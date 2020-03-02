<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('objektname', lang)}</td>         <td>${c['attributes']['sb_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('objektnr', lang)}</td>          <td>${c['attributes']['sb_obj'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('kanton', lang)}</td>         <td>${c['attributes']['sb_kt'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('flaeche_ha', lang)}</td>          <td>${c['attributes']['sb_fl'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('gesamtflaeche_ha', lang)}</td>         <td>${c['attributes']['sb_gf'] or '-'}</td></tr>
</%def>
