<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<tr><td class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.verantwortung')}</td>      <td>${c['attributes']['verantwortung'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.gwlnr')}</td>              <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.flussname')}</td>          <td>${c['attributes']['flussname'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.abschnitt')}</td>          <td>${c['attributes']['abschnitt'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.gerinnetyp')}</td>         <td>${c['attributes']['gerinnetyp'] or '-'}</td></tr>
% if c['attributes']['uebersicht_messkampagne_link']:
<tr><td class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.uebersicht_messkampagne_link')}</td>   <td><a href="${c['attributes']['uebersicht_messkampagne_link']}" target="_blank">${_('link')}</a></td></tr>
% else:
<tr><td class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.uebersicht_messkampagne_link')}</td>   <td>-</td></tr>
% endif
</%def>
