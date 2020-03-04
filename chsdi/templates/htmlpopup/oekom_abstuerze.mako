# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<% 

    lang = 'fr' if lang in ('fr', 'it') else 'de'
    typ = 'typ_%s' % lang
    absttyp = 'absttyp_%s' % lang
    abstmat = 'abstmat_%s' % lang

%>

    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_abstnr', lang)}</td>             <td>${c['attributes']['abstnr']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_absttyp', lang)}</td>            <td>${c['attributes'][absttyp]}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_abstmat', lang)}</td>            <td>${c['attributes'][abstmat]}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_absthoehe', lang)}</td>          <td>${c['attributes']['absthoehe']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">

<%

    lang = 'fr' if lang in ('fr', 'it') else 'de'
    typ = 'typ_%s' % lang
  
%>

<table>

    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_bemerkung', lang)}</td>          <td>${c['attributes']['bemerkung']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_mass', lang)}</td>               <td>${c['attributes']['mass']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_rechtswert', lang)}</td>         <td>${c['attributes']['rechtswert']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_hochwert', lang)}</td>           <td>${c['attributes']['hochwert']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_abschnr', lang)}</td>            <td>${c['attributes']['abschnr']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_notizen', lang)}</td>            <td>${c['attributes']['notizen']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ch.bafu.oekomorphologie-f_abstuerze_datum', lang)}</td>              <td>${c['attributes']['datum']}</td></tr>

</table>

</%def>

