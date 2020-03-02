# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<%
translate_type = 'ads_name_' + c['attributes']['ads_name']
%>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.geologie-geomorphologie.ads_name', lang)}</td>        <td>${_(translate_type)}</td></tr>
</%def>
