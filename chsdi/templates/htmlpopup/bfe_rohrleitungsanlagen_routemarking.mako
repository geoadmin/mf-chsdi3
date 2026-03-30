<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.operator_uid')}</td>
    <td>${c['attributes']['operator_uid'] or '-'}</td>
  </tr>
</%def>
