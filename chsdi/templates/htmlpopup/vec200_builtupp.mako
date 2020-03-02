<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${t.Translator.translate('city_name', lang)}</td><td>${c['attributes']['objname']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('einwohnerzahl', lang)}</td><td>
    % if c['attributes']['ppi']:
    ${t.Translator.translate(c['attributes']['ppi'], lang)}
    % else:
    -
    % endif
    </td></tr>
</%def>

