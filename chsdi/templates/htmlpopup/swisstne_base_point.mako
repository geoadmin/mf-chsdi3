<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstne-base.uuid')}</td>
      <td>${c['attributes']['uuid'] or '-'}</td>
    </tr>
</%def>
