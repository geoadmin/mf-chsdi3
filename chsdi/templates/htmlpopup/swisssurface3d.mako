<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d.metadata.tilekey')}</td>   <td>${c['id'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d.metadata.gpstime_min')}</td>    <td>${c['attributes']['gpstime_min'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d.metadata.gpstime_max')}</td>    <td>${c['attributes']['gpstime_max'] or '-'}</td></tr>
</%def>
