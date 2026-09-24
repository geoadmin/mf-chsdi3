<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <%
      lang = lang if lang in ('fr','it', 'en') else 'de'
   %>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.borehole_name')}</td>
      <td>${int(c['attributes']['borehole_name']) or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.max_depth')}</td>
      <td>${int(c['attributes']['max_depth']) or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.heat_flow')}</td>
      <td>${int(c['attributes']['heat_flow']) or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.reliability')}</td>
      <td>${c['attributes']['reliability_' + lang] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.uncorrected_temperature_gradient')}</td>
      <td>${int(c['attributes']['uncorrected_temperature_gradient']) or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.topography_corrected_temperature_gradient')}</td>
      <td>${int(c['attributes']['topography_corrected_temperature_gradient']) or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.thermal_conductivity')}</td>
      <td>${int(c['attributes']['thermal_conductivity']) or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.boreholes_swissgeol_ch')}</td>
      <td>${c['attributes']['boreholes_swissgeol_ch'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.assets_swissgeol_ch')}</td>
      <td>${c['attributes']['assets_swissgeol_ch'] or '-'}</td>
   </tr>
</%def>
