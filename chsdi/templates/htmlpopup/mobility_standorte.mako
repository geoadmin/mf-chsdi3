<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == 'rm':
        lang = 'de'
    elif lang == 'it':
        lang = 'fr'
%>
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.mobility.standorte.name')}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.mobility.standorte.number')}</td>         <td>${c['attributes']['number'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.mobility.standorte.location')}</td>       <td>${c['attributes']['street'] or '-'}, ${c['attributes']['location'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.mobility.standorte.lon')}</td>            <td>${c['attributes']['lon'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.mobility.standorte.lat')}</td>            <td>${c['attributes']['lat'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.mobility.standorte.link')}</td>           <td><a target="_blank" href="https://www.mobility.ch/${lang}/privatkunden/standorte?station_id=${c['attributes']['number'] or ''}">Link</a></td></tr>
    <tr><td class="cell-left">${_('ch.mobility.standorte.categories')}</td>            <td>${c['attributes']['categories'] or '-'}</td></tr>
</%def>

