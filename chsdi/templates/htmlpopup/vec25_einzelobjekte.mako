<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('laenge_m', lang)}</td>          <td>${int(round(c['attributes']['length'])) or '-'}</td></tr>
</%def>
