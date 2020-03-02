<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('flaeche_ha', lang)}</td>    <td>${int(round(c['attributes']['flaeche_ha'])) or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('stand', lang)}</td>    <td>${int(round(c['attributes']['stand'])) or '-'}</td></tr>
</%def>
