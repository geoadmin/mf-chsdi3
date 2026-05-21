<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left">${_('ch.bfe.rohrleitungsanlagen.operatorname')}</td>
    <td>${c['attributes']['operator_name'] or '-'}</td>
  </tr>
</%def>
