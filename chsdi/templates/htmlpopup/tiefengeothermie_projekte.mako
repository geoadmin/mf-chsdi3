<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.owner')}</td><td>${c['attributes']['owner'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.status')}</td><td>${c['attributes']['status'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.system')}</td><td>${c['attributes']['system'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.use')}</td><td>${c['attributes']['use'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c,lang)">
<table class="table-with-border tiefengeothermie_projekte-extended">

   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.name')}</th><td>${c['attributes']['name'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.owner')}</th><td>${c['attributes']['owner'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.status')}</th><td>${c['attributes']['status'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.system')}</th><td>${c['attributes']['system'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.use')}</th><td>${c['attributes']['use'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.canton')}</th><td>${c['attributes']['canton'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.community')}</th><td>${c['attributes']['community'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.depth')}</th><td>${c['attributes']['depth'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.reservoir')}</th><td>${c['attributes']['reservoir'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.temp')}</th><td>${c['attributes']['temp'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.power')}</th><td>${c['attributes']['power'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.produc')}</th><td>${c['attributes']['produc'] or '-'}</td></tr>
   <tr><th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.download')}</th>
   % if c['attributes']['download'] == None or c['attributes']['download'] == "-":
       <td>-</td>
   % else:
       <td><a href="${c['attributes']['download']}" target="_blank">Zip</a></td>
   % endif
   </tr>
   <%
   weblink = c['attributes']['weblink'].split('; ')
   %>
   <tr>
     <th class="cell-left">${_('ch.swisstopo.geologie-tiefengeothermie_projekte.weblink')}</th>
     <td>
     %  for i in range(len(weblink)):
        <a href="${weblink[i]}" target="_blank">Link_${i+1}</a>&nbsp;
     %endfor
     </td>
   </tr>
</table>
</%def>
