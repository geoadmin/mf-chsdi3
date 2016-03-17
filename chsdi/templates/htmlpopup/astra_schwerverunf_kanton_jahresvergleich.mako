<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
   <colgroup>
      <col width=80%>
      <col width=20%>
   </colgroup>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.canton')}</td>  <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.year')}</td>  <td>${c['attributes']['year'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt')}</td>  <td>${c['attributes']['acc_ugt'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_usv')}</td>  <td>${c['attributes']['acc_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_usv')}</td>  <td>${c['attributes']['acc_ugt_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_lastyear')}</td>  <td>${c['attributes']['acc_ugt_lastyear'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_usv_lastyear')}</td>  <td>${c['attributes']['acc_usv_lastyear'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_usv_lastyear')}</td>  <td>${c['attributes']['acc_ugt_usv_lastyear'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_usv_yearchangepercent')}</td>  <td>${"%.2f"%c['attributes']['acc_ugt_usv_yearchangepercent'] or '-'}</td></tr>
</%def>

