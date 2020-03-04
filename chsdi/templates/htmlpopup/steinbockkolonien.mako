<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('objektname', lang)}</td>         <td>${c['attributes']['sb_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('objektnr', lang)}</td>          <td>${c['attributes']['sb_obj'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('kanton', lang)}</td>         <td>${c['attributes']['sb_kt'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('flaeche_ha', lang)}</td>          <td>${c['attributes']['sb_fl'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('gesamtflaeche_ha', lang)}</td>         <td>${c['attributes']['sb_gf'] or '-'}</td></tr>
</%def>
