<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <% c['stable_id'] = True %>
    
    <tr><th colspan=2>${t.Translator.translate(c['attributes']['objval'], lang)}:</th></tr>
    <tr><td class="cell-left">${t.Translator.translate('name', lang)}</td><td>
    % if c['attributes']['objname'].strip() in ['N_A','N_P']:
        -
    % else:
        ${c['attributes']['objname'] or '-'}
    % endif
    </td></tr>
    % if c['attributes']['objval'].strip() in ['Kraftwerk']:
    <tr><td class="cell-left">${t.Translator.translate('typ_kraftwerk', lang)}</td><td>${t.Translator.translate(c['attributes']['ppc'] or '-', lang)}</td></tr>
    % endif

    % if c['attributes']['objval'].strip() in ['Verarbeitungsanlage','Deponie','Pumpwerk']:
    <tr><td class="cell-left">${t.Translator.translate('typ_produkt', lang)}</td><td>${t.Translator.translate(c['attributes']['pro'] or '-', lang)}</td></tr>
    % endif
</%def>

