<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('name', lang)}</td>                 <td>${c['attributes']['key_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_wrz_select_obj', lang)}</td>    <td>${c['attributes']['key_obj'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('typ', lang)}</td>                  <td>${c['attributes']['typ'] or '-'}</td></tr>
</%def>

