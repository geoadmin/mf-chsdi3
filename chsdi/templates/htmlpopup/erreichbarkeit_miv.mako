<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.are.erreichbarkeit-miv.verkerszone_id')}</td><td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.erreichbarkeit-miv.strasse_erreichb_ewap')}</td><td>${c['attributes']['strasse_erreichb_ewap'] or '-'}</td></tr>
</%def>

