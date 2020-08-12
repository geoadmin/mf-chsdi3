<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.gmde')}</td>
  <td colspan="4">${c['attributes']['gmde'] or '-'}</td>
</tr>

<tr>
  <td class="cell-left">${_('ch.bfs.landschaftswandel.swissnames')}</td>
  <td colspan="4">${c['attributes']['swissnames'] or '-'}</td>
</tr>

</%def>
