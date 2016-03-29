<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">
   <colgroup>
      <col width=80%>
      <col width=20%>
   </colgroup>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_geschwindigkeit.canton')}</td>  <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_geschwindigkeit.year')}</td>  <td>${c['attributes']['year'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_geschwindigkeit.population')}</td>  <td>${c['attributes']['population'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_ugt')}</td>  <td>${c['attributes']['accspeed_ugt'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_usv')}</td>  <td>${c['attributes']['accspeed_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_ugt_usv')}</td>  <td>${c['attributes']['accspeed_ugt_usv'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.schwerverunfallte-kanton_geschwindigkeit.accspeed_ugt_usv_perpopulation')}</td>  <td>${"%.2f"%c['attributes']['accspeed_ugt_usv_perpopulation'] or '-'}</td></tr>
</%def>

