<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
   
%if c['attributes']['obname']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.obname', lang)}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
%endif
%if c['attributes']['pckind']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.pckind', lang)}</td><td>${c['attributes']['pckind'] or '-'}</td></tr>
%endif
%if c['attributes']['cpkind']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.cpkind', lang)}</td><td>${c['attributes']['cpkind'] or '-'}</td></tr>
%endif
%if c['attributes']['stkind']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.stkind', lang)}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
%endif
%if c['attributes']['tlyearsformatted']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.tlyearsformatted', lang)}</td><td>${c['attributes']['tlyearsformatted'] or '-'}</td></tr>
%endif
%if c['attributes']['clkind']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.clkind', lang)}</td><td>${c['attributes']['clkind'] or '-'}</td></tr>
%endif
%if c['attributes']['purl']:
   <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung.purl')}</td><td><a  target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text', lang)}</a></td></tr>
%endif
</%def>

