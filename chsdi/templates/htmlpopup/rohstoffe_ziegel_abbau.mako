<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
       <%
              lang = lang if lang in ('fr','it', 'en') else 'de'
              stkind_text = 'stkind_%s' %lang
              ltkinds_text = 'ltkinds_%s' %lang
              infos_url_text = 'infos_url_%s' %lang
       %>

       %if c['attributes']['type'] == 'production':
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.production_obname')}</td>
              <td>${c['attributes']['obname'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.production_cpkind')}</td>
              <td>${c['attributes']['cpkind'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.production_stkind')}</td>
              <td>${c['attributes'][stkind_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.production_infos_url')}</td>
              % if 'http' not in c['attributes'][infos_url_text]:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes'][infos_url_text]}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.production_purl')}</td>
              % if 'http' not in c['attributes']['purl']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['purl']}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.production_swissgeol_link')}</td>
              % if 'http' not in c['attributes']['swissgeol_link']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['swissgeol_link']}>${_('link')}</a></td>
              % endif
       </tr>
       % else:
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_obname')}</td>
              <td>${c['attributes']['obname'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_edkinds')}</td>
              <td>${c['attributes']['edkinds'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_cpkind')}</td>
              <td>${c['attributes']['cpkind'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_stkind')}</td>
              <td>${c['attributes'][stkind_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_ltkinds')}</td>
              <td>${c['attributes'][ltkinds_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_infos_url')}</td>
              % if 'http' not in c['attributes'][infos_url_text]:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes'][infos_url_text]}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_purl')}</td>
              % if 'http' not in c['attributes']['purl']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['purl']}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.mining_swissgeol_link')}</td>
              % if 'http' not in c['attributes']['swissgeol_link']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['swissgeol_link']}>${_('link')}</a></td>
              % endif
       </tr>
       %endif

</%def>
