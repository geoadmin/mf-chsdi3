# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${t.translate('ch.vbs.territorialregionen.terreg_nr', lang)}</td>      <td>${c['featureId'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.vbs.territorialregionen.name', lang)}</td>        <td>${c['attributes']['name']}</td></tr>
</%def>
