<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.Translator.translate('objektname', lang)}</td>        <td>${c['attributes']['em_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('objektnr', lang)}</td>          <td>${c['attributes']['em_obj'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('flaeche_ha', lang)}</td>        <td>${round(c['attributes']['em_gf']) or '-'}</td></tr>
</%def>

