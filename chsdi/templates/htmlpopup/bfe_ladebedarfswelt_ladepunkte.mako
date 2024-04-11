<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Name_Gemeinde')}</td>
    <td>${c['attributes']['name_gemeinde'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Jahr')}</td>
    <td>${c['attributes']['jahr'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Allgemein_zugaenglich_Anzahl_Ladepunkte')}</td>
    <td>${c['attributes']['allgemein_zugaenglich_anzahl_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Quartier_AC_Ladepunkte')}</td>
    <td>${c['attributes']['quartier_ac_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Zielort_AC_Ladepunkte')}</td>
    <td>${c['attributes']['zielort_ac_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Quartier_DC_150_Ladepunkte')}</td>
    <td>${c['attributes']['quartier_dc_150_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Schnell_DC_150_Ladepunkte')}</td>
    <td>${c['attributes']['schnell_dc_150_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Schnell_DC_350_Ladepunkte')}</td>
    <td>${c['attributes']['schnell_dc_350_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Heim_AC_Ladepunkte')}</td>
    <td>${c['attributes']['heim_ac_ladepunkte'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-ladepunkte.Arbeit_AC_Ladepunkte')}</td>
    <td>${c['attributes']['arbeit_ac_ladepunkte'] or '-'}</td>
  </tr>
</%def>
