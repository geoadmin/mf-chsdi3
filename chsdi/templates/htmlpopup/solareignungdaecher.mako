<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang != 'rm' else 'de'
    lang_i = {'de':0, 'fr':1, 'it':2, 'en':3, 'rm':4}.get(lang, 0)
%>

    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.solarenergie-eignung-daecher.klasse_text', lang)}</td>                     <td>${c['attributes']['klasse_text'].split('##')[lang_i]}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.solarenergie-eignung-daecher.flaeche', lang)}</td>                     <td>${int(c['attributes']['flaeche'])}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.solarenergie-eignung-daecher.ausrichtung', lang)}</td>                     <td>${(c['attributes']['ausrichtung'] + 180)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.solarenergie-eignung-daecher.neigung', lang)}</td>                     <td>${c['attributes']['neigung'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.solarenergie-eignung-daecher.finanzertrag', lang)}</td>                     <td>${round(c['attributes']['finanzertrag'], -1)}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('link_to_sonnendach')}</td>                                               <td><a href="https://www.uvek-gis.admin.ch/BFE/sonnendach/?featureId=${c['featureId']}&lang=${lang}" target="_blank">${_('sonnendach_link', lang)}</a></td></tr>
</%def>
