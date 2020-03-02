<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <tr><td class="cell-left">${t.translate('ch.bafu.bundesinventare-flachmoore.objnummer', lang)}</td>          <td>${c['attributes']['objnummer'] or '-'}</td></tr>
   <tr><td class="cell-left">${t.translate('ch.bafu.bundesinventare-flachmoore.name', lang)}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><td class="cell-left">${t.translate('ch.bafu.bundesinventare-flachmoore.shape_area', lang)}</td>         <td>${round(c['attributes']['shape_area']/10000,1) or '-'}</td></tr>
   <tr><td class="cell-left">${t.translate('ch.bafu.bundesinventare-flachmoore.refobjblat', lang)}</td>        <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td></tr>
</%def>

