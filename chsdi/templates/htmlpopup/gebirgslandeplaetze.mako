<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
   lang = lang if lang in ('fr', 'it') else 'de'
   description = 'descrip_%s' % lang
%>

    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.icao')}</td>         <td>${c['attributes']['icao'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.name')}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.canton')}</td>           <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.description')}</td>     <td>${c['attributes'][description] or '-'}</td></tr>
   <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.arp_east')}</td>           <td>${c['attributes']['arp_east'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.arp_north')}</td>         <td>${c['attributes']['arp_north'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.elevation')}</td>         <td>${c['attributes']['elevation'] or '-'}</td></tr>
</%def>
