<%inherit file="base.mako"/>

 <%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('ch.bfe.biomasse-nicht-verholzt.name', lang)}</td>          <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bfe.biomasse-nicht-verholzt.non_woody', lang)}</td>     <td>${round(c['attributes']['non_woody'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bfe.biomasse-nicht-verholzt.bfs_nummer', lang)}</td>    <td>${c['attributes']['bfs_nummer'] or '-'}</td></tr>
 </%def>
