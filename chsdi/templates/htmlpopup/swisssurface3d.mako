<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d.metadata.tilekey')}</td>   <td>${c['id'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d.metadata.temporalkey')}</td>    <td>${c['attributes']['temporalkey'] or '-'}</td></tr>
</%def>
