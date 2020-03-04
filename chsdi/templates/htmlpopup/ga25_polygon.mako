<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('geocover_basisdatensatz', lang)}</td><td>${c['attributes']['basisdatensatz'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('geocover_description', lang)}</td><td>${c['attributes']['description'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('geocover_tecto', lang)}</td><td>${c['attributes']['tecto'] or '-'}</td></tr>
    <tr><td class="cell-left"></td><td><a href="${c['attributes']['url_legend']}" target="_blank">${mod_translate.Translator.translate('linkzurlegende', lang)}</a></td></tr>
</%def>
