<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${t.translate('geocover_basisdatensatz', lang)}</td><td>${c['attributes']['basisdatensatz'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('geocover_description', lang)}</td><td>${c['attributes']['description'] or '-'}</td></tr>
</%def>
