<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.are.reisezeit-agglomerationen-miv.verkehrszone_id')}</td><td>${c['attributes']['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.reisezeit-agglomerationen-miv.strasse_no_agglo')}</td><td>${c['attributes']['strasse_no_agglo'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.reisezeit-agglomerationen-miv.strasse_reisezeit_agglo')}</td><td>${c['attributes']['strasse_reisezeit_agglo'] or '-'}</td></tr>
</%def>
