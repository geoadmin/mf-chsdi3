<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.needhome', lang)}</td>            	<td>${c['attributes']['needhome'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.needservice', lang)}</td>           <td>${c['attributes']['needservice'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.needtotal', lang)}</td>             <td>${c['attributes']['needtotal'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.noga', lang)}</td>                  <td>${c['attributes']['noga'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.service', lang)}</td>               <td>${c['attributes']['service'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
    <table class="table-with-border">
        <tr><th class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentgas' , lang)}</th>             <td>${c['attributes']['percentgas'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentoil', lang)}</th>              <td>${c['attributes']['percentoil'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentpump', lang)}</th>             <td>${c['attributes']['percentpump'] or '-'}</td></tr>
        <tr><th class="cell-left">${mod_translate.Translator.translate('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude.percentremoteheat', lang)}</th>       <td>${c['attributes']['percentremoteheat'] or '-'}</td></tr>
    </table>
</%def>
