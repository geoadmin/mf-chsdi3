<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${_(c['layerBodId'] + '.nr')}</td>
        <td>${c['attributes']['nr'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.titel')}</td>
        <td>${c['attributes']['titel'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.jahr')}</td>
        <td>${c['attributes']['jahr'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.autor')}</td>
        <td>${c['attributes']['autor'] or '-'}</td>
    </tr>
</%def>