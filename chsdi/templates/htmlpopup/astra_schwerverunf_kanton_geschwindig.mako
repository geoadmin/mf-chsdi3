<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
   <colgroup>
      <col width=80%>
      <col width=20%>
   </colgroup>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.astra.schwerverunfallte-kanton_geschwindigkeit.canton', lang)}</td>  <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.astra.schwerverunfallte-kanton_geschwindigkeit.year', lang)}</td>  <td>${c['attributes']['year'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.astra.schwerverunfallte-kanton_geschwindigkeit.population', lang)}</td>  <td>${h.int_with_apostrophe(c['attributes']['population']) or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_ugt', lang)}</td>  <td>${c['attributes']['accspeed_ugt'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_usv', lang)}</td>  <td>${c['attributes']['accspeed_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_ugt_usv', lang)}</td>  <td>${c['attributes']['accspeed_ugt_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_ugt_usv_perpopulation', lang)}</td>  <td>${"%.2f"%c['attributes']['accspeed_ugt_usv_perpopulation'] or '-'}</td></tr>
</%def>

