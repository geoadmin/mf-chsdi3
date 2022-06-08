<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bfe.biomasse-verholzt.name')}</td>            <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr>
      <td class="cell-left">${_('ch.bfe.biomasse-nicht-verholzt.woody')}</td>
      % if c['attributes']['woody']:
        <td>${round(c['attributes']['woody'], 2)}</td>
      % else:
        <td>-</td>
      % endif
    </tr>
    <tr><td class="cell-left">${_('ch.bfe.biomasse-verholzt.bfs_nummer')}</td>      <td>${c['attributes']['bfs_nummer'] or '-'}</td></tr>
</%def>
