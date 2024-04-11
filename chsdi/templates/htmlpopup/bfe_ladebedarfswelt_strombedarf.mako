<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Name_Gemeinde')}</td>
    <td>${c['attributes']['name_gemeinde'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Jahr')}</td>
    <td>${c['attributes']['jahr'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Summe_GWh')}</td>
    <td>${c['attributes']['summe_gwh'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Heim_Energie_Anteil')}</td>
    <td>${c['attributes']['heim_energie_anteil'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Arbeit_Energie_Anteil')}</td>
    <td>${c['attributes']['arbeit_energie_anteil'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Quartier_Energie_Anteil')}</td>
    <td>${c['attributes']['quartier_energie_anteil'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Zielort_Energie_Anteil')}</td>
    <td>${c['attributes']['zielort_energie_anteil'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.ladebedarfswelt-strombedarf.Schnell_Energie_Anteil')}</td>
    <td>${c['attributes']['schnell_energie_anteil'] or '-'}</td>
  </tr>
</%def>
