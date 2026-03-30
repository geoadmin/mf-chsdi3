<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.legalprovision')}</td>
    <td>${c['attributes']['legalprovision'] or '-'}</td>
  </tr>
</%def>
