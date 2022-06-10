<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr>
      <td class="cell-left">${_('flaeche_ha')}</td>
      % if c['attributes']['area']:
         <td>${int(round(c['attributes']['area']))} ha</td>
      % else:
         <td>-</td>
      % endif
    </tr>
    <tr>
      <td class="cell-left">${_('perimeter_m')}</td>
      % if c['attributes']['perimeter']:
         <td>${round(c['attributes']['perimeter']))} m</td>
      % else:
         <td>-</td>
      % endif
    </tr>
</%def>
