<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c[stable_id] = True %>
    <tr><td class="cell-left">${Translator.translate('schiffbarkeit', lang)}</td><td>
    % if c['attributes']['exs'] == 'Not applicable':
    ${Translator.translate('No', lang)}
    % elif c['attributes']['exs'] == 'Naviguable and opera':
    ${Translator.translate('Yes', lang)}
    % else:
    -
    % endif
    </td></tr>
    
    <tr><td class="cell-left">${Translator.translate('hydrografische_herkunft', lang)}</td><td>
    % if c['attributes']['hoc']:
    ${_(c['attributes']['hoc'])}
    % else:
    -
    % endif
    </td></tr>
    <tr><td class="cell-left">${Translator.translate('name', lang)}</td>
    % if c['attributes']['name'].strip()== 'N_P':
      <td>-</td>
    % else:
      <td>${c['attributes']['name'].strip()}</td>
    % endif
    </tr>
</%def>

