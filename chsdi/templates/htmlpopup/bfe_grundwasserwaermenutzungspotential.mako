<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Name')}</td>    
    <td>${c['attributes']['name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Heat_potential_W_per_m2')}</td>    
    <td>${c['attributes']['heat_potential_w_per_m2'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Reliability')}</td>    
    <td>${c['attributes']['reliability'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Heat_atmosphere_percent')}</td>
    <td>${c['attributes']['heat_atmosphere_percent'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Heat_precipitation_percent')}</td>    
    <td>${c['attributes']['heat_precipitation_percent'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Heat_catchment_percent')}</td>
    <td>${c['attributes']['heat_catchment_percent'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Heat_geothermal_percent')}</td>
    <td>${c['attributes']['heat_geothermal_percent'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left-large">${_('ch.bfe.grundwasserwaermenutzungspotential.Comment')}</td>
    <td>${c['attributes']['comment'] or '-'}</td>
  </tr>
</%def>
