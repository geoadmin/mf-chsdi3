<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('objektname')}</td>        <td>${c['attributes']['em_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('objektnr')}</td>          <td>${c['attributes']['em_obj'] or '-'}</td></tr>
    <tr>
      <td class="cell-left">${_('flaeche_ha')}</td>
      % if c['attributes']['em_gf']:
         <td>${round(c['attributes']['em_gf'])}</td>
      % else:
         <td>-</td>
      % endif
    </tr>
</%def>

