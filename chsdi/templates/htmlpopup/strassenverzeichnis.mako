<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
    c['stable_id'] = True
    official = 'yesText' if c['attributes']['str_official'] == 1 else 'noText'
    %>

    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.esid')}</td>
        <td>${c['featureId']}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.label')}</td>
        <td>${c['attributes']['stn_label'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.plzo')}</td>
        <td>${c['attributes']['zip_label'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.gdenr')}</td>
        <td>${c['attributes']['com_fosnr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.gdename')}</td>
        <td>${c['attributes']['com_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.type')}</td>
        <td>${_(c['attributes']['str_type'] or '-')}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.status')}</td>
        <td>${_(c['attributes']['str_status'] or '-')}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.official')}</td>
        <td>${_(official)}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.modified')}</td>
        <td>${_(c['attributes']['str_modified'] or '-')}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.children')}</td>
        <td>${_(c['attributes']['str_children'] or c['attributes']['str_parent'] or '-')}</td>
    </tr>
</%def>
