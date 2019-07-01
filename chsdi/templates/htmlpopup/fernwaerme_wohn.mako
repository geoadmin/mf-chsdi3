<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.needhome')}</td>            	<td>${c['attributes']['needhome'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.needservice')}</td>           <td>${c['attributes']['needservice'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.needtotal')}</td>             <td>${c['attributes']['needtotal'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.noga')}</td>                  <td>${c['attributes']['noga'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.service')}</td>               <td>${c['attributes']['service'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
    <table class="table-with-border">
        <tr><th class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentgas' )}</th>             <td>${c['attributes']['percentgas'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentoil')}</th>              <td>${c['attributes']['percentoil'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentpump')}</th>             <td>${c['attributes']['percentpump'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentremoteheat')}</th>       <td>${c['attributes']['percentremoteheat'] or '-'}</td></tr>
    </table>
</%def>
