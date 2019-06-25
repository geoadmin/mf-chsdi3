<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_industrie.needindustry')}</td>    	<td>${c['attributes']['needindustry'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_industrie.industry')}</td>         <td>${c['attributes']['industry'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-nachfrage_industrie.noga')}</td>             <td>${c['attributes']['noga'] or '-'}</td></tr>
</%def>

