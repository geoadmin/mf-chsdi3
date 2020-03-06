<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
   <colgroup>
      <col width=80%>
      <col width=20%>
   </colgroup>
    <tr><td class="cell-left">${h.translate('ch.astra.schwerverunfallte-kanton_alkohol.canton', lang)}</td>  <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.schwerverunfallte-kanton_alkohol.year', lang)}</td>  <td>${c['attributes']['year'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.schwerverunfallte-kanton_alkohol.population', lang)}</td>  <td>${h.int_with_apostrophe(c['attributes']['population']) or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_ugt', lang)}</td>  <td>${c['attributes']['accalcohol_ugt'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_usv', lang)}</td>  <td>${c['attributes']['accalcohol_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_ugt_usv', lang)}</td>  <td>${c['attributes']['accalcohol_ugt_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_ugt_usv_perpopulation', lang)}</td>  <td>${"%.2f"%c['attributes']['accalcohol_ugt_usv_perpopulation'] or '-'}</td></tr>
</%def>

