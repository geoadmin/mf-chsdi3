<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    kanal = 'kanal_%s' % lang
%>

    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ezgnr', lang)}</td>    <td>${c['attributes']['ezgnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('klwkp_gwlnr', lang)}</td>          <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_measure_2', lang)}</td>         <td>${c['attributes']['measure'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_ezgflaeche', lang)}</td>         <td>${c['attributes']['gesamtflae'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_anteil_ch', lang)}</td>         <td>${c['attributes']['anteil_ch'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('gewaesser', lang)}</td>         <td>${c['attributes']['gewaessern'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_kanal', lang)}</td>       <td>${c['attributes'][kanal] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    kanal = 'kanal_%s' % lang
%>

    <table class="table-with-border">
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_ezgnr', lang)}</th>    <td>${c['attributes']['ezgnr'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('klwkp_gwlnr', lang)}</th>          <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_measure_2', lang)}</th>         <td>${c['attributes']['measure'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_ezgflaeche', lang)}</th>         <td>${c['attributes']['gesamtflae'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_anteil_ch', lang)}</th>         <td>${c['attributes']['anteil_ch'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('gewaesser', lang)}</th>         <td>${c['attributes']['gewaessern'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_kanal', lang)}</th>       <td>${c['attributes'][kanal] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_meanalt', lang)}</th>       <td>${c['attributes']['meanalt'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_maxalt', lang)}</th>       <td>${c['attributes']['maxalt'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_mq_jahr', lang)}</th>       <td>${c['attributes']['mq_jahr'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_feuchtflae', lang)}</th>       <td>${c['attributes']['feuchtflae'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_wasserflae', lang)}</th>       <td>${c['attributes']['wasserflae'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_bebautefl', lang)}</th>       <td>${c['attributes']['bebautefl'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_landwirtsc', lang)}</th>       <td>${c['attributes']['landwirtsc'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('tt_wald_natur', lang)}</th>       <td>${c['attributes']['wald_natur'] or '-'}</td></tr>
    </table>
</%def>
