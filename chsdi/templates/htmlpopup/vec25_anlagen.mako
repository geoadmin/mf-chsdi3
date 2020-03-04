<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('flaeche_ha', lang)}</td><td>${int(round(c['attributes']['area'])) or '-'} ha</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('perimeter_m', lang)}</td>    <td>${int(round(c['attributes']['perimeter'])) or '-'} m</td></tr>
</%def>
