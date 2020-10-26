<%def name="anlage()">
  <tr><td class="cell-left">${layer('anlagenr')}</td> <td>${c['attributes']['anlagenr'] or '-'}</td></tr>
  <tr><td class="cell-left">${layer('anlagename')}</td> <td>${c['attributes']['anlagename'] or '-'}</td></tr>
</%def>

<%def name="betreiber()">
  <tr><td class="cell-left">${layer('betreiber_tuabkuerzung')}</td> <td>${c['attributes']['betreiber_tuabkuerzung'] or '-'}</td></tr>
</%def>

<%def name="layer(translation)">
  ${_('ch.bav.seilbahnen-bundeskonzession.' + translation)}
</%def>
