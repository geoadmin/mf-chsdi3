<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${h.translate('ch.bafu.schutzgebiete-biosphaerenreservate.name', lang)}</td>             <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.schutzgebiete-biosphaerenreservate.objnummer', lang)}</td>        <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.schutzgebiete-biosphaerenreservate.version', lang)}</td>          <td>${c['attributes']['version'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.schutzgebiete-biosphaerenreservate.shape_area_ha', lang)}</td>    <td>${c['attributes']['shape_area_ha'] or '-'}</td></tr>
</%def>
