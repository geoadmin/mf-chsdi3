<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
   <colgroup>
      <col width=80%>
      <col width=20%>
   </colgroup>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.canton', lang)}</td>  <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.year', lang)}</td>  <td>${c['attributes']['year'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt', lang)}</td>  <td>${c['attributes']['acc_ugt'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_usv', lang)}</td>  <td>${c['attributes']['acc_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_usv', lang)}</td>  <td>${c['attributes']['acc_ugt_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_lastyear', lang)}</td>  <td>${c['attributes']['acc_ugt_lastyear'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_usv_lastyear', lang)}</td>  <td>${c['attributes']['acc_usv_lastyear'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_usv_lastyear', lang)}</td>  <td>${c['attributes']['acc_ugt_usv_lastyear'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.astra.schwerverunfallte-kanton_jahresvergleich.acc_ugt_usv_yearchangepercent', lang)}</td>  <td>${"%.2f"%c['attributes']['acc_ugt_usv_yearchangepercent'] or '-'}</td></tr>
</%def>

