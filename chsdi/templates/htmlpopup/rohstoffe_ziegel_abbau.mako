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
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.obname')}</td>
              <td>${c['attributes']['obname'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.cpkind')}</td>
              <td>${c['attributes']['cpkind'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.stkind')}</td>
              <td>${c['attributes'][stkind_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.info_url')}</td>
              <td>${c['attributes'][infos_url_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.purl')}</td>
              <td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text')}</a></td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.swissgeol_link')}</td>
              <td>${c['attributes']['swissgeol_link'] or '-'}</td>
       </tr>
% else:
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.edkinds')}</td>
              <td>${c['attributes']['edkinds'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.cpkind')}</td>
              <td>${c['attributes']['cpkind'] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.stkind')}</td>
              <td>${c['attributes'][stkind_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.ltkinds')}</td>
              <td>${c['attributes'][ltkinds_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.infos_url')}</td>
              <td>${c['attributes'][infos_url_text] or '-'}</td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.purl')}</td>
              <td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text')}</a></td>
       </tr>
       <tr>
              <td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.swissgeol_link')}</td>
              <td>${c['attributes']['swissgeol_link'] or '-'}</td>
       </tr>
%endif

</%def>
