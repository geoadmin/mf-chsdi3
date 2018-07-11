<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == 'rm':
        lang = 'de'
    elif lang == 'it':
        lang = 'fr'
%>
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.state')}</td>                   <td>${c['attributes']['status'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.approval_date')}</td>           <td>${c['attributes']['approval_date'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.publication_date')}</td>        <td>${c['attributes']['publication_date'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.authority')}</td>               <td>${c['attributes']['approving_authority'] or '-'}</td></tr>
</%def>

