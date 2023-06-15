<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<tr>
  <td class="cell-left">
    ${_('ch.bazl.intrinsisches-bodenrisiko_sora.density_pop_km2')}
  </td>
  <td>
    ${c['attributes']['density_pop_km2']}
  </td>
</tr>
</%def>
