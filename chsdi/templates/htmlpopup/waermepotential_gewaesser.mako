<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left">${_('ch.bfe.waermepotential-gewaesser.name')}</td><td>${c['attributes']['name']}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bfe.waermepotential-gewaesser.heat_extraction_gwha')}</td><td>${c['attributes']['heat_extraction_gwha'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bfe.waermepotential-gewaesser.heat_disposal_gwha')}</td><td>${c['attributes']['heat_disposal_gwha'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bfe.waermepotential-gewaesser.further_information')}</td>
    <td><a href="${c['attributes']['further_information'] or '-'}" target="_blank">${_('ch.bfe.waermepotential-gewaesser.link')}</a></td>
  </tr>
</%def>
