<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.obname')}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.ockind')}</td><td>${c['attributes']['ockind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.ltkinds')}</td><td>${c['attributes']['ltkinds'] or '-'}</td></tr>
%if c['attributes']['edltkinds']:
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.edltkinds')}</td><td>${c['attributes']['edltkinds'] or '-'}</td></tr>
%endif
%if c['attributes']['emkinds']:
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.emkinds')}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
%endif
%if c['attributes']['pckind']:
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.pckind')}</td><td>${c['attributes']['pckind'] or '-'}</td></tr>
%endif
%if c['attributes']['cpkind']:
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.cpkind')}</td><td>${c['attributes']['cpkind'] or '-'}</td></tr>
%endif
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.stkind')}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.clkind')}</td><td>${c['attributes']['clkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung.purl')}</td><td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text')}</a></td></tr>
</%def>
