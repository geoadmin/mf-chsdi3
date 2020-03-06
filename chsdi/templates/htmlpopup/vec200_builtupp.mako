<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${h.translate('city_name', lang)}</td><td>${c['attributes']['objname']}</td></tr>
    <tr><td class="cell-left">${h.translate('einwohnerzahl', lang)}</td><td>
    % if c['attributes']['ppi']:
    ${h.translate(c['attributes']['ppi'], lang)}
    % else:
    -
    % endif
    </td></tr>
</%def>

