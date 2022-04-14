<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${_(c['layerBodId'] + '.gsk_nr')}</td>
        <td>${c['attributes']['gsk_nr'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.titel')}</td>
        <td>${c['attributes']['titel'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.jahrgang')}</td>
        <td>${c['attributes']['jahrgang'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.massstab')}</td>
        <td>${c['attributes']['massstab'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.autoren')}</td>
        <td>${c['attributes']['autoren'] or '-'}</td>
    </tr>
</%def>