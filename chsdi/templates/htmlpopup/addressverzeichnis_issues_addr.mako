<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = False %>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.adr_egaid')}</td>      <td>${c['attributes']['adr_egaid'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.stn_label')}</td>      <td>${c['attributes']['stn_label'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.adr_number')}</td>     <td>${c['attributes']['adr_number'] or '-'}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.zip_label')}</td>      <td>${_(c['attributes']['zip_label'] or '-')}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.com_fosnr')}</td>      <td>${_(c['attributes']['com_fosnr'] or '-')}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.com_canton')}</td>      <td>${_(c['attributes']['com_canton'] or '-')}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.issue_description')}</td>     <td>${_(c['attributes']['issue_description'] or '-')}</td></tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.issue_category')}</td>     <td>${_(c['attributes']['issue_category'] or '-')}</td></tr>
</%def>
