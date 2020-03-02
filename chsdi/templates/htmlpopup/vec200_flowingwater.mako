<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c[stable_id] = True %>
    <tr><td class="cell-left">${t.translate('schiffbarkeit', lang)}</td><td>
    % if c['attributes']['exs'] == 'Not applicable':
    ${t.translate('No', lang)}
    % elif c['attributes']['exs'] == 'Naviguable and opera':
    ${t.translate('Yes', lang)}
    % else:
    -
    % endif
    </td></tr>
    
    <tr><td class="cell-left">${t.translate('hydrografische_herkunft', lang)}</td><td>
    % if c['attributes']['hoc']:
    ${_(c['attributes']['hoc'])}
    % else:
    -
    % endif
    </td></tr>
    <tr><td class="cell-left">${t.translate('name', lang)}</td>
    % if c['attributes']['name'].strip()== 'N_P':
      <td>-</td>
    % else:
      <td>${c['attributes']['name'].strip()}</td>
    % endif
    </tr>
</%def>

