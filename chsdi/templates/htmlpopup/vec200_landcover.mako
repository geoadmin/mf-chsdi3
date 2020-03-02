<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    % if c['attributes']['objval'].strip() in ['Gletscher', 'Stadtzentr', 'Sumpf', 'See', 'Siedl', 'Stausee']:
        <tr><th colspan=2>${_(c['attributes']['objval'])}:</th></tr>
        <tr><td class="cell-left">${Translator.translate('name_lang1', lang)}</td><td>
         % if c['attributes']['objname1'].strip() in ['N_P','N_A']:
             - 
         % else:   
             ${c['attributes']['objname1'] or '-'}
         % endif     
         </td></tr>
    % else:
    ${Translator.translate('No additional information for this object type', lang)}: ${_(c['attributes']['objval'])}
    % endif
</%def>

