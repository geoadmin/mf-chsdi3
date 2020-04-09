<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.are.reisezeit-agglomerationen-oev.oev_no_agglo')}</td><td>${c['attributes']['oev_no_agglo'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.reisezeit-agglomerationen-oev.oev_reisezeit_agglo')}</td><td>${c['attributes']['oev_reisezeit_agglo'] or '-'}</td></tr>
</%def>
