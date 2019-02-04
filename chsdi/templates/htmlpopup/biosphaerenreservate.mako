<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-biosphaerenreservate.name')}</td>             <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-biosphaerenreservate.objnummer')}</td>        <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-biosphaerenreservate.version')}</td>          <td>${c['attributes']['version'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.schutzgebiete-biosphaerenreservate.shape_area_ha')}</td>    <td>${c['attributes']['shape_area_ha'] or '-'}</td></tr>
</%def>
