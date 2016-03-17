<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
<%
   import locale
   locale.setlocale(locale.LC_ALL, 'fr_CH.utf-8')
%>
   <colgroup>
      <col width=80%>
      <col width=20%>
   </colgroup>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_alkohol.canton')}</td>  <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_alkohol.year')}</td>  <td>${c['attributes']['year'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_alkohol.population')}</td>  <td>${locale.format('%d',c['attributes']['population'],1) or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_ugt')}</td>  <td>${c['attributes']['accalcohol_ugt'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_usv')}</td>  <td>${c['attributes']['accalcohol_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_ugt_usv')}</td>  <td>${c['attributes']['accalcohol_ugt_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_alkohol.accalcohol_ugt_usv_perpopulation')}</td>  <td>${"%.2f"%c['attributes']['accalcohol_ugt_usv_perpopulation'] or '-'}</td></tr>
</%def>

