<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        layer = c['layerBodId']
    %>

    <tr><td class="cell-left">${_(layer + '.n_bilanz_kg_ha')}</td> <td>${c['attributes']['n_bilanz_kg_ha'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.jahr')}</td> <td>${c['attributes']['jahr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.n_bilanz_kg_ha_cat')}</td> <td>${c['attributes']['n_bilanz_kg_ha_cat'] or '-'}</td></tr>
</%def>

