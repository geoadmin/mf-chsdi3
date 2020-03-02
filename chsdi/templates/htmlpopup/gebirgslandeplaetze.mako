<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
   lang = lang if lang in ('fr', 'it') else 'de'
   description = 'descrip_%s' % lang
%>

    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.gebirgslandeplaetze.icao', lang)}</td>         <td>${c['attributes']['icao'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.gebirgslandeplaetze.name', lang)}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.gebirgslandeplaetze.canton', lang)}</td>           <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.gebirgslandeplaetze.description', lang)}</td>     <td>${c['attributes'][description] or '-'}</td></tr>
   <tr><td class="cell-left">${t.Translator.translate('ch.bazl.gebirgslandeplaetze.arp_east', lang)}</td>           <td>${c['attributes']['arp_east'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.gebirgslandeplaetze.arp_north', lang)}</td>         <td>${c['attributes']['arp_north'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bazl.gebirgslandeplaetze.elevation', lang)}</td>         <td>${c['attributes']['elevation'] or '-'}</td></tr>
</%def>
