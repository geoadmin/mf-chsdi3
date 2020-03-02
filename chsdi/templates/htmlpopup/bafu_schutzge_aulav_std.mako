<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('name', lang)}</td>                 <td>${c['attributes']['key_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_wrz_select_obj', lang)}</td>    <td>${c['attributes']['key_obj'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('typ', lang)}</td>                  <td>${c['attributes']['typ'] or '-'}</td></tr>
</%def>

