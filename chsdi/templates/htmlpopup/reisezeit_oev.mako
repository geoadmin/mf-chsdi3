<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.are.reisezeit-oev.verkehrszone_id')}</td><td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.reisezeit-oev.oev_no_z')}</td><td>${c['attributes']['oev_no_z'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.reisezeit-oev.oev_reisezeit_z')}</td><td>${c['attributes']['oev_reisezeit_z'] or '-'}</td></tr>
</%def>
