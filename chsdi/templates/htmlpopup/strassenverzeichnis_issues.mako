<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.str_esid')}</td>
        <td>${c['attributes']['str_esid'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.stn_label')}</td>
        <td>${c['attributes']['stn_label'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.zip_label')}</td>
        <td>${c['attributes']['zip_label'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.com_fosnr')}</td>
        <td>${c['attributes']['com_fosnr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.com_canton')}</td>
        <td>${c['attributes']['com_canton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.issue_status')}</td>
        <td>${_(c['attributes']['issue_status'] or '-')}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.issue_category')}</td>
        <td>${_(c['attributes']['issue_category'] or '-')}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.issue_description')}</td>
        <td>${_(c['attributes']['issue_description'] or '-')}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.issue_solution')}</td>
        <td>${_(c['attributes']['issue_solution'] or '-')}</td>
    </tr>
</%def>
