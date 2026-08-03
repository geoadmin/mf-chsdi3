<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        layer = c['layerBodId']
    %>

    <tr><td class="cell-left">${_(layer + '.thg_emissionen_t_co2eq_ha')}</td> <td>${c['attributes']['thg_emissionen_t_co2eq_ha'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.jahr')}</td> <td>${c['attributes']['jahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.thg_emissionen_t_co2eq_ha_cat')}</td> <td>${c['attributes']['thg_emissionen_t_co2eq_ha_cat'] or '-'}</td></tr>
</%def>

