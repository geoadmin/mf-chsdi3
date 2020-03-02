<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c[stable_id] = True %>
    <tr><td class="cell-left">${t.Translator.translate('schiffbarkeit', lang)}</td><td>
    % if c['attributes']['exs'] == 'Not applicable':
    ${t.Translator.translate('No', lang)}
    % elif c['attributes']['exs'] == 'Naviguable and opera':
    ${t.Translator.translate('Yes', lang)}
    % else:
    -
    % endif
    </td></tr>
    
    <tr><td class="cell-left">${t.Translator.translate('hydrografische_herkunft', lang)}</td><td>
    % if c['attributes']['hoc']:
    ${t.Translator.translate(c['attributes']['hoc'], lang)}
    % else:
    -
    % endif
    </td></tr>
    <tr><td class="cell-left">${t.Translator.translate('name', lang)}</td>
    % if c['attributes']['name'].strip()== 'N_P':
      <td>-</td>
    % else:
      <td>${c['attributes']['name'].strip()}</td>
    % endif
    </tr>
</%def>

