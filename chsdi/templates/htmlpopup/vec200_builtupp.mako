<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${mod_translate.Translator.translate('city_name', lang)}</td><td>${c['attributes']['objname']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('einwohnerzahl', lang)}</td><td>
    % if c['attributes']['ppi']:
    ${mod_translate.Translator.translate(c['attributes']['ppi'], lang)}
    % else:
    -
    % endif
    </td></tr>
</%def>

