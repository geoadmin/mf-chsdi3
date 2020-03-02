<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('ch.swisstopo.swisssurface3d.metadata.tilekey', lang)}</td>   <td>${c['id'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.swisssurface3d.metadata.temporalkey', lang)}</td>    <td>${c['attributes']['temporalkey'] or '-'}</td></tr>
</%def>
