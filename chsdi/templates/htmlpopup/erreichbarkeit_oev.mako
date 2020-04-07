<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.are.erreichbarkeit-oev.verkerszone_id')}</td><td>${c['attributes']['verkerszone_id'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.are.erreichbarkeit-oev.strasse_erreichb_ewap')}</td><td>${c['attributes']['oev_erreichb_ewap'] or '-'}</td></tr>
</%def>

