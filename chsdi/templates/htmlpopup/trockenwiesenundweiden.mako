<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
   <tr>
     <td class="cell-left">${_('ch.bafu.bundesinventare-trockenwiesen_trockenweiden.objnummer')}</td>
     <td>${c['attributes']['objnummer'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_('ch.bafu.bundesinventare-trockenwiesen_trockenweiden.name')}</td>
      <td>${c['attributes']['name'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_('ch.bafu.bundesinventare-trockenwiesen_trockenweiden.teilobjnummer')}</td>
      <td>${c['attributes']['teilobjnummer'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_('ch.bafu.bundesinventare-trockenwiesen_trockenweiden.singularitaet')}</td>
      <td>${c['attributes']['singularitaet'] or '-'}</td>
   </tr>
   <tr>
     <td class="cell-left">${_('ch.bafu.bundesinventare-trockenwiesen_trockenweiden.shape_area')}</td>
     % if c['attributes']['shape_area']:
        <td>${round(c['attributes']['shape_area'] / 10000, 1)}</td>
     % else:
        <td>-</td>
     % endif
   </tr>
   <tr>
      <td class="cell-left">${_('ch.bafu.bundesinventare-trockenwiesen_trockenweiden.refobjblat')}</td>
      <td><a target="_blank" href="${c['attributes']['refobjblat']}">${_('link') or '-'}</a></td>
   </tr>
</%def>

