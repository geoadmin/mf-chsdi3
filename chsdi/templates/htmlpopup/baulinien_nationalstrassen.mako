<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <% c['stable_id'] = False %>

    % if 'status' in c['attributes']:
        <%
        state_val = c['attributes']['status'].lower()
        state = _('ch.astra.baulinien-nationalstrassen.%s' % state_val)
        %>
        <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.state')}</td>                   <td>${state}</td></tr>
        <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.approval_date')}</td>           <td>${c['attributes']['approval_date'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.publication_date_from')}</td>        <td>${c['attributes']['publication_date_from'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.authority')}</td>               <td>${c['attributes']['approving_authority'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.planning_approval_name')}</td>  <td>${c['attributes']['planning_approval_name'] or '-'}</td></tr>
    % else:
        <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.vertical_limit_upward')}</td>   <td>${c['attributes']['vertical_limit_upward'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.astra.baulinien-nationalstrassen.vertical_limit_downward')}</td><td>${c['attributes']['vertical_limit_downward'] or '-'}</td></tr>
    % endif
</%def>

