<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-flachmoore.objnummer')}</td>          <td>${c['attributes']['objnummer'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-flachmoore.name')}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-flachmoore.shape_area')}</td>         <td>${round(c['attributes']['shape_area']/10000,1) or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-flachmoore.refobjblat')}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

