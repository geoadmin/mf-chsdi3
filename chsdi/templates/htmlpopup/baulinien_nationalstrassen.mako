<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    state_val = c['attributes']['status'].lower()
    state = _('ch.astra.baulinien-nationalstrassen.%s' % state_val)
%>
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.state')}</td>                   <td>${state}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.approval_date')}</td>           <td>${c['attributes']['approval_date'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.publication_date')}</td>        <td>${c['attributes']['publication_date'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.authority')}</td>               <td>${c['attributes']['approving_authority'] or '-'}</td></tr>
</%def>

