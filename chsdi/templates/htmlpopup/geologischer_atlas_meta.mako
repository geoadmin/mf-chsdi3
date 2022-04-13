<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${_(c['layerBodId'] + '.nummer')}</td>
        <td>${c['attributes']['nummer'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.massstab')}</td>
        <td>${c['attributes']['massstab'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.ausgabejahr')}</td>
        <td>${c['attributes']['ausgabejahr'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_(c['layerBodId'] + '.autoren')}</td>
        <td>${c['attributes']['autoren'] or '-'}</td>
    </tr>
</%def>
