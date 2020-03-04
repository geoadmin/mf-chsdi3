# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<%
translate_type = 'ads_name_' + c['attributes']['ads_name']
%>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-geomorphologie.ads_name', lang)}</td>        <td>${mod_translate.Translator.translate(translate_type, lang)}</td></tr>
</%def>
