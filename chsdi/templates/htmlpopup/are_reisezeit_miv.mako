<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.are.reisezeit-miv.verkehrszone_id')}</td><td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.reisezeit-miv.strasse_no_z')}</td><td>${c['attributes']['strasse_no_z'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.reisezeit-miv.strasse_reisezeit_z')}</td><td>${c['attributes']['strasse_reisezeit_z'] or '-'}</td></tr>
</%def>
