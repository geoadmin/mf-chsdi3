<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('ch.bfe.biomasse-verholzt.name', lang)}</td>            <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bfe.biomasse-verholzt.woody', lang)}</td>           <td>${round(c['attributes']['woody'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bfe.biomasse-verholzt.bfs_nummer', lang)}</td>      <td>${c['attributes']['bfs_nummer'] or '-'}</td></tr>
</%def>
