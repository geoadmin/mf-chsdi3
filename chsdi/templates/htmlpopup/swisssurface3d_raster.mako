<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d-raster.metadata.tilekey')}</td>   <td>${c['id'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d-raster.metadata.fly_y_min')}</td>    <td>${c['attributes']['fly_y_min'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swisssurface3d-raster.metadata.fly_y_max')}</td>    <td>${c['attributes']['fly_y_max'] or '-'}</td></tr>
</%def>
