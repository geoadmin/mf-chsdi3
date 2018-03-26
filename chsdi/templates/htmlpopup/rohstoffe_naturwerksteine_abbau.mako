<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>

       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau.obname')}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau.tckind')}</td><td>${c['attributes']['tckind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau.ltkinds')}</td><td>${c['attributes']['ltkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau.emkinds')}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau.stkind')}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau.clkind')}</td><td>${c['attributes']['clkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau.purl')}</td><td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text')}</a></td></tr>
</%def>
