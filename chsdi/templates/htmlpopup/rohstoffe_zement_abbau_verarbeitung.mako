<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
       <%
              lang = lang if lang in ('fr','it', 'en') else 'de'
              stkind_text = 'stkind_%s' %lang
              info_url_text = 'info_url_%s' %lang
              ltkinds_text = 'ltkinds_%s' %lang
              infos_url_text = 'infos_url_%s' %lang
       %>

       %if c['attributes']['type'] == 'production':
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.production_obname')}</td>
              <td>${c['attributes']['obname'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.production_cpkind')}</td>
              <td>${c['attributes']['cpkind'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.production_stkind')}</td>
              <td>${c['attributes'][stkind_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.production_info_url')}</td>
              % if 'http' not in c['attributes'][info_url_text]:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes'][info_url_text]}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.production_purl')}</td>
              % if 'http' not in c['attributes']['purl']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['purl']}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.production_swissgeol_link')}</td>
              % if 'http' not in c['attributes']['swissgeol_link']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['swissgeol_link']}>${_('link')}</a></td>
              % endif
       </tr>
       % else:
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.mining_obname')}</td>
              <td>${c['attributes']['obname'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.mining_cpkind')}</td>
              <td>${c['attributes']['cpkind'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.mining_stkind')}</td>
              <td>${c['attributes'][stkind_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.mining_ltkinds')}</td>
              <td>${c['attributes'][ltkinds_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.mining_infos_url')}</td>
              % if 'http' not in c['attributes'][infos_url_text]:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes'][infos_url_text]}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.mining_purl')}</td>
              % if 'http' not in c['attributes']['purl']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['purl']}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung.mining_swissgeol_link')}</td>
              % if 'http' not in c['attributes']['swissgeol_link']:
              <td>-</td>
              % else:
              <td><a target="_blank" href=${c['attributes']['swissgeol_link']}>${_('link')}</a></td>
              % endif
       </tr>
       %endif

</%def>
