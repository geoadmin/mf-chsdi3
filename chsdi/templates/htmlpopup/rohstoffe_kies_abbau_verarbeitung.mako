<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
       <%
              lang = lang if lang in ('fr','it','en') else 'de'
              stkind_text = 'stkind_%s' %lang
              ltkinds_text = 'ltkinds_%s' %lang
              emkinds_text = 'emkinds_%s' %lang
       %>

       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kies_abbau_verarbeitung.production_obname')}</td>
              <td>${c['attributes']['obname'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kies_abbau_verarbeitung.production_stkind')}</td>
              <td>${c['attributes'][stkind_text] or '-'}</td>
       </tr>
       %if c['attributes']['type'] == 'mining':
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kies_abbau_verarbeitung.mining_ltkinds')}</td>
              <td>${c['attributes'][ltkinds_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kies_abbau_verarbeitung.mining_emkinds')}</td>
              <td>${c['attributes'][emkinds_text] or '-'}</td>
       </tr>
       %endif
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kies_abbau_verarbeitung.purl')}</td>
              % if 'http' not in c['attributes']['purl']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['purl']}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kies_abbau_verarbeitung.swissgeol_link')}</td>
              % if not c['attributes']['swissgeol_link'] or 'http' not in c['attributes']['swissgeol_link']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['swissgeol_link']}>${_('link')}</a></td>
              % endif
       </tr>
</%def>
