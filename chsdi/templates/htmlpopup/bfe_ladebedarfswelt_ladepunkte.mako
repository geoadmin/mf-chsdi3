<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Name_Gemeinde')}</td>
    <td>${c['attributes']['name_gemeinde'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Jahr')}</td>
    <td>${c['attributes']['jahr'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Allg_zugaenglich_Anzahl_Ladepunkte')}</td>
    <td>${c['attributes']['allgemein_zugaenglich_anzahl_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Quartier_AC_Ladepunkte')}</td>
    <td>${c['attributes']['quartier_ac_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Zielort_AC_Ladepunkte')}</td>
    <td>${c['attributes']['zielort_ac_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Zielort_DC_50_Ladepunkte')}</td>
    <td>${c['attributes']['zielort_dc_50_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Quartier_DC_150_Ladepunkte')}</td>
    <td>${c['attributes']['quartier_dc_150_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Schnell_DC_150_Ladepunkte')}</td>
    <td>${c['attributes']['schnell_dc_150_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Schnell_DC_350_Ladepunkte')}</td>
    <td>${c['attributes']['schnell_dc_350_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Heim_AC_Ladepunkte')}</td>
    <td>${c['attributes']['heim_ac_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte_bequem.Arbeit_AC_Ladepunkte')}</td>
    <td>${c['attributes']['arbeit_ac_ladepunkte'] or '-'}</td>
  </tr>
</%def>
