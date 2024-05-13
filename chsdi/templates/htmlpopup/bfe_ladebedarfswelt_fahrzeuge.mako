<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-fahrzeuge.Name_Gemeinde')}</td>
    <td>${c['attributes']['name_gemeinde'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-fahrzeuge.Jahr')}</td>
    <td>${c['attributes']['jahr'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-fahrzeuge.Anzahl_Fahrzeugbestand_Personenwagen_PHEV')}</td>
    <td>${c['attributes']['anzahl_fahrzeugbestand_personenwagen_phev'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-fahrzeuge.Anzahl_Fahrzeugbestand_Personenwagen_BEV')}</td>
    <td>${c['attributes']['anzahl_fahrzeugbestand_personenwagen_bev'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-fahrzeuge.Anteil_Fahrzeugbestand_Personenwagen_Steckerfahrzeuge')}</td>
    <td>${c['attributes']['anteil_fahrzeugbestand_personenwagen_steckerfahrzeuge'] or '-'}</td>
  </tr>
</%def>
