<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c[stable_id] = True %>
    <tr><td width="150">${_('name')}</td><td>
    % if c['attributes']['name'].strip() in ['N_P','A_P']:
    -
    % else:
    ${c['attributes']['name'].strip()}
    % endif
    </td></tr>
    <tr><td width="150">${_('hoehe_see')}</td><td>
    % if c['attributes']['seesph'] < 0:
    -
    % else:
    ${c['attributes']['seesph'] or '-'}
    % endif
    </td></tr>
</%def>

