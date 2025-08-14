<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        layer = c['layerBodId']
    %>

    <tr><td class="cell-left">${_(layer + '.euc_dist')}</td> <td>${c['attributes']['euc_dist'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.cw_dist')}</td> <td>${c['attributes']['cw_dist'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.path_length')}</td> <td>${c['attributes']['path_length'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.cost_to_euc_dist_ratio')}</td> <td>${c['attributes']['cost_to_euc_dist_ratio'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.current_flow_centrality')}</td> <td>${c['attributes']['current_flow_centrality'] or '-'}</td></tr>
</%def>

