# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% 
    lang = 'fr' if lang in ('fr', 'it') else 'de'
    typ = 'typ_%s' % lang
    bauwtyp = 'bauwtyp_%s' % lang
    
%>

    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_bauwnr', lang)}</td>             <td>${c['attributes']['bauwnr']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_bauwtyp', lang)}</td>            <td>${c['attributes'][bauwtyp]}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_bauwhoehe', lang)}</td>          <td>${c['attributes']['bauwhoehe']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">

<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
    typ = 'typ_%s' % lang

%>

<table>

    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_mass', lang)}</td>               <td>${c['attributes']['mass']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_rechtswert', lang)}</td>         <td>${c['attributes']['rechtswert']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_hochwert', lang)}</td>           <td>${c['attributes']['hochwert']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_abschnr', lang)}</td>            <td>${c['attributes']['abschnr']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_bemerkung', lang)}</td>          <td>${c['attributes']['bemerkung']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_notizen', lang)}</td>            <td>${c['attributes']['notizen']}</td></tr>
    <tr><td class="cell-left">${Translator.translate('tt_ch.bafu.oekomorphologie-f_bauwerke_datum', lang)}</td>              <td>${c['attributes']['datum']}</td></tr>

</table>

</%def>





