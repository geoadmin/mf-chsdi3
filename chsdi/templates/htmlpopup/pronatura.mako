<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.objnummer', lang)}</td>                         <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.name', lang)}</td>                         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.gisflaeche', lang)}</td>                   <td>${round(c['attributes']['gisflaeche'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.obj_gesflaeche', lang)}</td>                   <td>${round(c['attributes']['gesflaeche'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.gisteilobjekt', lang)}</td>                   <td>${round(c['attributes']['gisteilobjekt'],2) or '-'}</td></tr>
% if c['attributes']['mcpfe'].strip()== 'MCPFE1.1':
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.mcpfe', lang)}</td>                        <td>${mod_translate.Translator.translate('ch.pronatura.waldreservate.tt_pronatura_e1', lang)}</td></tr>
% elif c['attributes']['mcpfe'].strip()== 'MCPFE1.2':
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.mcpfe', lang)}</td>                        <td>${mod_translate.Translator.translate('ch.pronatura.waldreservate.tt_pronatura_e2', lang)}</td></tr>
% elif c['attributes']['mcpfe'].strip()== 'MCPFE1.3':
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.mcpfe', lang)}</td>                        <td>${mod_translate.Translator.translate('ch.pronatura.waldreservate.tt_pronatura_e3', lang)}</td></tr>
% else:
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.pronatura.waldreservate.mcpfe', lang)}</td>                        <td>-</td></tr>
% endif
</%def>
