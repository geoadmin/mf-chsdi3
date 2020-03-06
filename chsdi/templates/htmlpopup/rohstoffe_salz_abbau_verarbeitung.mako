<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.obname', lang)}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.obnamealt', lang)}</td><td>${c['attributes']['obnamealt'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.ockind', lang)}</td><td>${c['attributes']['ockind'] or '-'}</td></tr>
%if c['attributes']['ltkind']:
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.ltkind', lang)}</td><td>${c['attributes']['ltkind'] or '-'}</td></tr>
%endif
%if c['attributes']['emkinds']:
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.emkinds', lang)}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
%endif
%if c['attributes']['pckind']:
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.pckind', lang)}</td><td>${c['attributes']['pckind'] or '-'}</td></tr>
%endif
%if c['attributes']['cpkind']:
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.cpkind', lang)}</td><td>${c['attributes']['cpkind'] or '-'}</td></tr>
%endif
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.stkind', lang)}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.clkind', lang)}</td><td>${c['attributes']['clkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.purl', lang)}</td><td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${h.translate('layer_url_portal_text', lang)}</a></td></tr>
</%def>
