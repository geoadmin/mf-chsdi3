<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang != 'rm' else 'de'
    lang_i = {'de':0, 'fr':1, 'it':2, 'en':3, 'rm':4}.get(lang, 0)
%>

    <tr><td class="cell-left">${_('ch.bfe.solarenergie-eignung-daecher.klasse_text')}</td>                     <td>${c['attributes']['klasse_text'].split('##')[lang_i]}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.solarenergie-eignung-daecher.flaeche')}</td>                     <td>${int(c['attributes']['flaeche'])}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.solarenergie-eignung-daecher.ausrichtung')}</td>                     <td>${(c['attributes']['ausrichtung'] + 180)}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.solarenergie-eignung-daecher.neigung')}</td>                     <td>${c['attributes']['neigung'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.solarenergie-eignung-daecher.finanzertrag')}</td>                     <td>${round(c['attributes']['finanzertrag'], -1)}</td></tr>
    <tr><td class="cell-left">${_('link_to_sonnendach')}</td>                                               <td><a href="http://www.bfe-gis.admin.ch/sonnendach/?featureId=${c['featureId']}&lang=${lang}" target="_blank">${_('sonnendach_link')}</a></td></tr>
</%def>
