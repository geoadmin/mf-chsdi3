<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.objnummer', lang)}</td>                    <td>${c['attributes']['objnummer'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.name', lang)}</td>                         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.gisflaeche', lang)}</td>                   <td>${round(c['attributes']['gisflaeche'],2) or '-'}</td></tr>
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.obj_gesflaeche', lang)}</td>
      % if c['attributes']['gesflaeche'] is not None:
        <td>${round(c['attributes']['gesflaeche'],2)}</td></tr>
      % else:
        <td>-</td></tr>
      % endif
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.gisteilobjekt', lang)}</td>                <td>${round(c['attributes']['gisteilobjekt'],2) or '-'}</td></tr>
% if c['attributes']['mcpfe'].strip()== 'MCPFE1.1':
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.mcpfe')}</td>                        <td>${_('ch.bafu.waldreservate.waldreservate_1_1', lang)}</td></tr>
% elif c['attributes']['mcpfe'].strip()== 'MCPFE1.2':
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.mcpfe')}</td>                        <td>${_('ch.bafu.waldreservate.waldreservate_1_2', lang)}</td></tr>
% elif c['attributes']['mcpfe'].strip()== 'MCPFE1.3':
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.mcpfe')}</td>                        <td>${_('ch.bafu.waldreservate.waldreservate_1_3', lang)}</td></tr>
% else:
    <tr><td class="cell-left">${Translator.translate('ch.bafu.waldreservate.mcpfe', lang)}</td>                        <td>-</td></tr>
% endif
</%def>
