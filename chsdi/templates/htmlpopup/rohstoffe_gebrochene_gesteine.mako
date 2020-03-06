<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>

       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau.obname', lang)}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau.tckind', lang)}</td><td>${c['attributes']['tckind'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau.ltkinds', lang)}</td><td>${c['attributes']['ltkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau.emkinds', lang)}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau.stkind', lang)}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau.clkind', lang)}</td><td>${c['attributes']['clkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau.purl', lang)}</td><td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${h.translate('layer_url_portal_text', lang)}</a></td></tr>
</%def>
