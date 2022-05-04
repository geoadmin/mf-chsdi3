<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_map_nb')}</td>
        <td>${c['attributes']['msh_map_nb'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_map_ti')}</td>
        <td>${c['attributes']['msh_map_ti'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_scale')}</td>
        <td>${c['attributes']['msh_scale'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_edit')}</td>
        <td>${c['attributes']['msh_edit'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_versio')}</td>
        <td>${c['attributes']['msh_versio'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_basis')}</td>
        <td>${c['attributes']['msh_basis'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_author')}</td>
        <td>${c['attributes']['msh_author'] or '-'}</td>
    </tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.msh_rev')}</td>
        <td>${c['attributes']['msh_rev'] or '-'}</td>
    </tr>
</%def>
