<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${mod_translate.Translator.translate('konf_objekt', lang)}</td><td>${c['attributes']['fco']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('lage_objekt', lang)}</td><td>${mod_translate.Translator.translate(c['attributes']['loc'] or '-', lang)}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('typ_transpo_produkt', lang)}</td><td>
    % if c['attributes']['pro'].strip() in ['Null / No Value']:
    -
    % else:
    ${mod_translate.Translator.translate(c['attributes']['pro'] or '-', lang)}
    % endif
    </td></tr>
</%def>

