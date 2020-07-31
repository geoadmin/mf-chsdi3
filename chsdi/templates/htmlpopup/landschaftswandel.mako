<%inherit file="base.mako"/>
<%def name="table_body(c,lang)">
<tr><td class="cell-left">${_('ch.bfs.landschaftswandel.haupttyp')}</td><td>${c['attributes']['haupttyp'] or '-'}</td></tr>
<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.typ1')}</td><td>${c['attributes']['typ1'] or '-'}</td>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.typ2')}</td><td>${c['attributes']['typ2'] or '-'}</td>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.typ3')}</td><td>${c['attributes']['typ3'] or '-'}</td>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.typ4')}</td><td>${c['attributes']['typ4'] or '-'}</td>
</tr>
</%def>

