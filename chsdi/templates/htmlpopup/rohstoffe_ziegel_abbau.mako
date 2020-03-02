<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

%if c['attributes']['obname']:   
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.obname', lang)}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
%endif
%if c['attributes']['tckinds']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.tckinds', lang)}</td><td>${c['attributes']['tckinds']}</td></tr>
%endif
%if c['attributes']['ltkinds']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.ltkinds', lang)}</td><td>${c['attributes']['ltkinds'] or '-'}</td></tr>
%endif
%if c['attributes']['stkind']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.stkind', lang)}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
%endif
%if c['attributes']['tlyearsformatted']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.tlyearsformatted', lang)}</td><td>${c['attributes']['tlyearsformatted'] or '-'}</td></tr>
%endif
%if c['attributes']['clkind']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.clkind', lang)}</td><td>${c['attributes']['clkind'] or '-'}</td></tr>
%endif
%if c['attributes']['purl']:
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.geologie-rohstoffe-ziegel_abbau.purl')}</td><td><a  target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text', lang)}</a></td></tr>
%endif
</%def>
