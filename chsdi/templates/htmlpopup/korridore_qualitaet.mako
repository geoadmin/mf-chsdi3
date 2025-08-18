<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        layer = c['layerBodId']
    %>

    <tr><td class="cell-left">${_(layer + '.Euc_Dist')}</td> <td>${c['attributes']['euc_dist'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.CW_Dist')}</td> <td>${c['attributes']['cw_dist'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.Path_Length')}</td> <td>${c['attributes']['path_length'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.Cost_to_EucDist_Ratio')}</td> <td>${c['attributes']['cost_to_euc_dist_ratio'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(layer + '.Current_Flow_Centrality')}</td> <td>${c['attributes']['current_flow_centrality'] or '-'}</td></tr>
</%def>

