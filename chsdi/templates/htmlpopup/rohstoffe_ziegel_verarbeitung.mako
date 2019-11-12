<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   
%if c['attributes']['obname']:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.obname')}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
%endif
%if c['attributes']['pckind']:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.pckind')}</td><td>${c['attributes']['pckind'] or '-'}</td></tr>
%endif
%if c['attributes']['cpkind']:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.cpkind')}</td><td>${c['attributes']['cpkind'] or '-'}</td></tr>
%endif
%if c['attributes']['stkind']:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.stkind')}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
%endif
%if c['attributes']['tlyearsformatted']:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.tlyearsformatted')}</td><td>${c['attributes']['tlyearsformatted'] or '-'}</td></tr>
%endif
%if c['attributes']['clkind']:
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.clkind')}</td><td>${c['attributes']['clkind'] or '-'}</td></tr>
%endif
%if c['attributes']['purl']:
   <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.purl')}</td><td><a  target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text')}</a></td></tr>
%endif
</%def>

