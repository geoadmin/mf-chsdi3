<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
       <%
              lang = lang if lang in ('fr','it','en') else 'de'
              rskind_text = 'rskind_%s' %lang
              is_crm_eu_text = 'is_crm_eu_%s' %lang
              crm_etransition_text = 'crm_etransition_%s' %lang
              mat_min_link_text = 'mat_min_link_%s' %lang
       %>

       <% c['stable_id'] = True %>

       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.obname')}</td>
              <td>${c['attributes']['obname'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.rskind')}</td>
              <td>${c['attributes'][rskind_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.is_crm_eu')}</td>
              <td>${c['attributes'][is_crm_eu_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.crm_etransition')}</td>
              <td>${c['attributes'][crm_etransition_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.crm_factsheet_link')}</td>
              <td>${c['attributes']['crm_factsheet_link'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.mat_min_link')}</td>
              <td>${c['attributes'][mat_min_link_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.purl')}</td>
              % if c['attributes']['purl'] is None or c['attributes']['purl'] == '-':
                     <td>-</td>
              % else:
                     <td><a target="_blank" href=${c['attributes']['purl']}>${_('link')}</a></td>
              % endif
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.swissgeol_link')}</td>
              % if c['attributes']['swissgeol_link'] is None or c['attributes']['swissgeol_link'] == '-':
                     <td>-</td>
              % else:
                     <td><a target="_blank" href=${c['attributes']['swissgeol_link']}>${_('link')}</a></td>
              % endif
       </tr>
</%def>
