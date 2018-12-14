<%inherit file="base.mako"/>

 <%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bfe.biomasse-nicht-verholzt.name')}</td>          <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.biomasse-nicht-verholzt.non_woody')}</td>     <td>${round(c['attributes']['non_woody'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.biomasse-nicht-verholzt.bfs_nummer')}</td>    <td>${c['attributes']['bfs_nummer'] or '-'}</td></tr>
 </%def>
