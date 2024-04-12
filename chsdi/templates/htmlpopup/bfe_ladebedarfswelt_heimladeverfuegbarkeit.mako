<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem.Name_Gemeinde')}</td>
    <td>${c['attributes']['name_gemeinde'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem.Jahr')}</td>
    <td>${c['attributes']['jahr'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem.Ladewelt')}</td>
    <td>${c['attributes']['ladewelt'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem.Anteil_weder_Heim_noch_Arbeit')}</td>
    <td>${c['attributes']['anteil_weder_heim_noch_arbeit'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem.Anteil_kein_Heim')}</td>
    <td>${c['attributes']['anteil_kein_heim'] or '-'}</td>
  </tr>
</%def>
