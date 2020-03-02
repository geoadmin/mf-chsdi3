<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang != 'rm' else 'de'
    lang_i = {'de':0, 'fr':1, 'it':2, 'en':3, 'rm':4}.get(lang, 0)
%>

    <tr><td class="cell-left">${t.translate('ch.bfe.solarenergie-eignung-fassaden.klasse', lang)}</td>                     <td>${c['attributes']['klasse_text'].split('##')[lang_i]}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bfe.solarenergie-eignung-fassaden.flaeche', lang)}</td>                     <td>${int(c['attributes']['flaeche'])}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bfe.solarenergie-eignung-fassaden.ausrichtung', lang)}</td>                     <td>${(c['attributes']['ausrichtung'] + 180)}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.bfe.solarenergie-eignung-fassaden.finanzertrag', lang)}</td>                     <td>${round(c['attributes']['finanzertrag'], -1)}</td></tr>
    <tr><td class="cell-left">${t.translate('link_to_sonnendach')}</td>                                               <td><a href="https://www.uvek-gis.admin.ch/BFE/sonnenfassade/?featureId=${c['featureId']}&lang=${lang}" target="_blank">${_('sonnenfassaden_link', lang)}</a></td></tr>
</%def>
