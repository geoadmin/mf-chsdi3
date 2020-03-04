<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td>${mod_translate.Translator.translate('linkzurlegende', lang)}</td>
        <td><a href="${c['attributes']['url_legend']}" target="_blank">${c['attributes']['titel']}</a>
     </td>
    </tr>
</%def>

