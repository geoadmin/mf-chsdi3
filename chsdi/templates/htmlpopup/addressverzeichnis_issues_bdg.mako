<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = False %>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.bdg_egid')}</td>      <td>${c['attributes']['bdg_egid'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.bdg_category')}</td>     <td>${_(c['attributes']['bdg_category'] or '-')}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.bdg_gstat')}</td>     <td>${_(c['attributes']['bdg_gstat'] or '-')}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.issue_category')}</td>     <td>${_(c['attributes']['issue_category'] or '-')}</td></tr>
</%def>
