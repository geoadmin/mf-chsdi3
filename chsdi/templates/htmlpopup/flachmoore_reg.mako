<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-flachmoore_regional.objnummer')}</td>          <td>${c['attributes']['objnummer'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-flachmoore_regional.name')}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bafu.bundesinventare-flachmoore_regional.shape_area')}</td>         <td>${round(c['attributes']['shape_area']/10000, 1) or '-'}</td></tr>
</%def>

