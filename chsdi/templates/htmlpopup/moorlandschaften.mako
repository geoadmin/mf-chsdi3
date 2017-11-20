<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-moorlandschaften.objnummer')}</td>           <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-moorlandschaften.name')}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-moorlandschaften.shape_area')}</td>         <td>${round(c['attributes']['shape_area']/10000,1) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.bundesinventare-moorlandschaften.refobjblat')}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

