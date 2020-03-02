<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${Translator.translate('name', lang)}</td><td>
    % if c['attributes']['name'].strip() in ['N_P','A_P']:
    -
    % else:
    ${c['attributes']['name'].strip()}
    % endif
    </td></tr>
    <tr><td class="cell-left">${Translator.translate('hoehe_see', lang)}</td><td>
    % if c['attributes']['seesph'] < 0:
    -
    % else:
    ${c['attributes']['seesph'] or '-'}
    % endif
    </td></tr>
</%def>

