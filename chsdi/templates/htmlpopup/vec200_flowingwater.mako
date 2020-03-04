<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c[stable_id] = True %>
    <tr><td class="cell-left">${mod_translate.Translator.translate('schiffbarkeit', lang)}</td><td>
    % if c['attributes']['exs'] == 'Not applicable':
    ${mod_translate.Translator.translate('No', lang)}
    % elif c['attributes']['exs'] == 'Naviguable and opera':
    ${mod_translate.Translator.translate('Yes', lang)}
    % else:
    -
    % endif
    </td></tr>
    
    <tr><td class="cell-left">${mod_translate.Translator.translate('hydrografische_herkunft', lang)}</td><td>
    % if c['attributes']['hoc']:
    ${mod_translate.Translator.translate(c['attributes']['hoc'], lang)}
    % else:
    -
    % endif
    </td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('name', lang)}</td>
    % if c['attributes']['name'].strip()== 'N_P':
      <td>-</td>
    % else:
      <td>${c['attributes']['name'].strip()}</td>
    % endif
    </tr>
</%def>

