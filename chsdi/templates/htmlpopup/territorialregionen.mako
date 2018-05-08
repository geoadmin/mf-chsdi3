# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.vbs.territorialregionen.terreg_nr')}</td>      <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.vbs.territorialregionen.name')}</td>        <td>${c['attributes']['name']}</td></tr>
</%def>
