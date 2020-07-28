<%inherit file="base.mako"/>
<%def name="table_body(c,lang)">
<tr><td class="cell-left">${_('ch.bfs.landschaftswandel.haupttype')}</td><td>${c['attributes']['haupttype'] or '-'}</td></tr>
</%def>
