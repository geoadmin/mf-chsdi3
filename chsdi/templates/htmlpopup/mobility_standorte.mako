<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == 'rm':
        lang = 'de'
    elif lang == 'it':
        lang = 'fr'
%>
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${Translator.translate('ch.mobility.standorte.name', lang)}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.mobility.standorte.number', lang)}</td>         <td>${c['attributes']['number'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.mobility.standorte.location', lang)}</td>       <td>${c['attributes']['street'] or '-'}, ${c['attributes']['location'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.mobility.standorte.lon', lang)}</td>            <td>${c['attributes']['lon'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.mobility.standorte.lat', lang)}</td>            <td>${c['attributes']['lat'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.mobility.standorte.link', lang)}</td>           <td><a target="_blank" href="https://www.mobility.ch/${lang}/return/stations/?stationQuery=${c['attributes']['number'] or ''}">Link</a></td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.mobility.standorte.categories', lang)}</td>            <td>${c['attributes']['categories'] or '-'}</td></tr>
</%def>

