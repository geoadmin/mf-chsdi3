# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% 

    lang = 'fr' if lang in ('fr','it') else 'de'
    typ = 'typ_%s' % lang
    breitenvar = 'breitenvar_%s' % lang
    sohlver = 'sohlver_%s' % lang
    oekomklasse = 'oekomklasse_%s' % lang

%>

    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_abschnr', lang)}</td>             <td>${c['attributes']['abschnr']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_gsbreite', lang)}</td>            <td>${c['attributes']['gsbreite']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_breitenvar', lang)}</td>          <td>${c['attributes'][breitenvar]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_sohlver', lang)}</td>             <td>${c['attributes'][sohlver]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_lufbebre', lang)}</td>            <td>${c['attributes']['lufbebre']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_rufbebre', lang)}</td>            <td>${c['attributes']['rufbebre']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_oekomklasse', lang)}</td>         <td>${c['attributes'][oekomklasse]}</td></tr>
</%def>

<%def name="extended_info(c, lang)">

<%

    lang = 'fr' if lang in ('fr','it') else 'de'
    typ = 'typ_%s' % lang
    breitenvar = 'breitenvar_%s' % lang
    eindol = 'eindol_%s' % lang
    vnatabst = 'vnatabst_%s' % lang
    tiefenvar = 'tiefenvar_%s' % lang
    lbukver = 'lbukver_%s' % lang
    rbukver = 'rbukver_%s' % lang
    lbukmat = 'lbukmat_%s' % lang
    rbukmat = 'rbukmat_%s' % lang
    luferber = 'luferber_%s' % lang
    ruferber = 'ruferber_%s' % lang
    lufbebew = 'lufbebew_%s' % lang
    rufbebew = 'rufbebew_%s' % lang
    bewalgen = 'bewalgen_%s' % lang
    bewmakro = 'bewmakro_%s' % lang
    totholz = 'totholz_%s' % lang

%>

<table>

    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_bemerkung', lang)}</td>           <td>${c['attributes']['bemerkung']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_anfangsmass', lang)}</td>         <td>${c['attributes']['anfangsmass']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_endmass', lang)}</td>             <td>${c['attributes']['endmass']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_anfangsrechtswert', lang)}</td>   <td>${c['attributes']['anfangsrechtswert']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_anfangshochwert', lang)}</td>     <td>${c['attributes']['anfangshochwert']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_endrechtswert', lang)}</td>       <td>${c['attributes']['endrechtswert']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_endhochwert', lang)}</td>         <td>${c['attributes']['endhochwert']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_eindol', lang)}</td>              <td>${c['attributes'][eindol]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_vnatabst', lang)}</td>            <td>${c['attributes'][vnatabst]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_tiefenvar', lang)}</td>           <td>${c['attributes'][tiefenvar]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_sohlmat', lang)}</td>             <td>${c['attributes']['sohlmat']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_lbukver', lang)}</td>             <td>${c['attributes'][lbukver]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_rbukver', lang)}</td>             <td>${c['attributes'][rbukver]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_lbukmat', lang)}</td>             <td>${c['attributes'][lbukmat]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_rbukmat', lang)}</td>             <td>${c['attributes'][rbukmat]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_luferber', lang)}</td>            <td>${c['attributes'][luferber]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_ruferber', lang)}</td>            <td>${c['attributes'][ruferber]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_lufbebew', lang)}</td>            <td>${c['attributes'][lufbebew]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_rufbebew', lang)}</td>            <td>${c['attributes'][rufbebew]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_bewalgen', lang)}</td>            <td>${c['attributes'][bewalgen]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_bewmakro', lang)}</td>            <td>${c['attributes'][bewmakro]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_totholz', lang)}</td>             <td>${c['attributes'][totholz]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_notizen', lang)}</td>             <td>${c['attributes']['notizen']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_ch.bafu.oekomorphologie-f_abschnitte_datum', lang)}</td>               <td>${c['attributes']['datum']}</td></tr>

</table>

</%def>  


