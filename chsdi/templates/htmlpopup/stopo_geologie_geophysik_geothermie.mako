<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   <%
      lang = lang if lang in ('fr','it', 'en') else 'de'
   %>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.borehole_name')}</td>
      <td>${c['attributes']['borehole_name'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.max_depth')}</td>
      <td>${c['attributes']['max_depth'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.heat_flow')}</td>
      <td>${c['attributes']['heat_flow'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.reliability')}</td>
      <td>${c['attributes']['reliability_' + lang] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.uncorrected_temperature_gradient')}</td>
      <td>${c['attributes']['uncorrected_temperature_gradient'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.topography_corrected_temperature_gradient')}</td>
      <td>${c['attributes']['topography_corrected_temperature_gradient'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.thermal_conductivity')}</td>
      <td>${c['attributes']['thermal_conductivity'] or '-'}</td>
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.boreholes_swissgeol_ch')}</td>
      % if c['attributes']['boreholes_swissgeol_ch'] and c['attributes']['boreholes_swissgeol_ch'].startswith('http'):
         <td><a href="${c['attributes']['boreholes_swissgeol_ch']}" target="_blank">${_('link')}</a></td>
      % else:
         <td>-</td>
      % endif
   </tr>
   <tr>
      <td class="cell-left">${_(c['layerBodId'] + '.assets_swissgeol_ch')}</td>
      % if c['attributes']['assets_swissgeol_ch'] and c['attributes']['assets_swissgeol_ch'].startswith('http'):
         <td><a href="${c['attributes']['assets_swissgeol_ch']}" target="_blank">${_('link')}</a></td>
      % else:
         <td>-</td>
      % endif
   </tr>
</%def>
