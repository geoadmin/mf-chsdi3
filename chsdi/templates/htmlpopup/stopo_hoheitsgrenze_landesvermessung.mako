<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
      <td class="cell-left">${_('ch.swisstopo.hoheitsgrenze-landesvermessung.gueltigkeit')}</td>
      <td>${c['attributes']['gueltigkeit'] or '-'}</td>
    </tr>
</%def>
