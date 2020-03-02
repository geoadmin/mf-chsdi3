<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr>
         <td class="cell-left">${t.translate('ch.astra.hauptstrassennetz.roadnumber', lang)}</td>
         <td>${c['attributes']['roadnumber'] or '-'}</td>
       </tr>
       <tr>
         <td class="cell-left">${t.translate('ch.astra.hauptstrassennetz.segmentid', lang)}</td>
         <td>${c['attributes']['segmentdescription'] or '-'}</td>
       </tr>
       <tr>
         <td class="cell-left">${t.translate('ch.astra.hauptstrassennetz.canton', lang)}</td>
         <td>${c['attributes']['canton'] or '-'}</td>
       </tr>
</%def>
