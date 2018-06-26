<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr>
         <td class="cell-left">${_('ch.astra.hauptstrassennetz.roadnumber')}</td>
         <td>${c['attributes']['roadnumber'] or '-'}</td>
       </tr>
       <tr>
         <td class="cell-left">${_('ch.astra.hauptstrassennetz.segmentid')}</td>
         <td>${c['attributes']['segmentid'] or '-'}</td>
       </tr>
       <tr>
         <td class="cell-left">${_('ch.astra.hauptstrassennetz.canton')}</td>
         <td>${c['attributes']['canton'] or '-'}</td>
       </tr>
</%def>
