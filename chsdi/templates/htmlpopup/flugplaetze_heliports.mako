<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.flugplaetze-heliports.icao', lang)}</td>           <td>${c['attributes']['icao'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.flugplaetze-heliports.name', lang)}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.flugplaetze-heliports.location', lang)}</td>           <td>${c['attributes']['location'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.flugplaetze-heliports.canton', lang)}</td>     <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.flugplaetze-heliports.arp_east', lang)}</td>         <td>${c['attributes']['arp_east'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.flugplaetze-heliports.arp_north', lang)}</td>         <td>${c['attributes']['arp_north'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.flugplaetze-heliports.elevation', lang)}</td>         <td>${c['attributes']['elevation'] or '-'}</td></tr>
</%def>
