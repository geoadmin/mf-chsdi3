<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.fernwaerme-nachfrage_industrie.needindustry', lang)}</td>    	<td>${c['attributes']['needindustry'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.fernwaerme-nachfrage_industrie.industry', lang)}</td>         <td>${c['attributes']['industry'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bfe.fernwaerme-nachfrage_industrie.noga', lang)}</td>             <td>${c['attributes']['noga'] or '-'}</td></tr>
</%def>

