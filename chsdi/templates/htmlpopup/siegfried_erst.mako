<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
   <% c['stable_id'] = True %>
   <tr><td class="cell-left">${_('tilenumber')}</td> <td>${c['featureId'] or '-'}</td></tr>
   <tr><td class="cell-left">${_('sheetname')}</td> <td>${c['attributes']['kbbez']}</td></tr>
   <tr>
      <td class="cell-left">${_('Datenstand')}</td>
      % if c['attributes']['datenstand']:
         <td>${int(round(c['attributes']['datenstand']))}</td>
      % else:
         <td>-</td>
      % endif
   </tr>
   <tr><td class="cell-left">${_('alexandria')}</td> <td><a href="https://swisscovery.slsp.ch/discovery/search?query=any,contains,${c['attributes']['bv_nummer']}&tab=41SLSP_NETWORK&search_scope=DN_and_CI&vid=41SLSP_NETWORK:VU1_UNION&offset=0" target="_blank" >${c['attributes']['kbbez'] or '-'}</a></td>
</%def>
