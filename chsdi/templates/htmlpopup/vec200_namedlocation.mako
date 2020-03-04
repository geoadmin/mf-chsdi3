<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<% c['stable_id'] = True %> 
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.vec200-names-namedlocation.objname1', lang)}</td><td>${c['attributes']['objname1']}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('name_lang2', lang)}</td><td>
    % if c['attributes']['objname2'].strip() in ['N_P','N_A']:
        -
    % else:
        ${c['attributes']['objname2'] or '-'}
    % endif
    </td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('hoehe_ueber_meer', lang)}</td><td>${c['attributes']['altitude'] or '-'}</td></tr>
</%def>
