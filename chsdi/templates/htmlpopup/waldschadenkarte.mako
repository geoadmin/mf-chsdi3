<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.waldschadenkarte.lauf_nr', lang)}</td>	         <td>${c['attributes']['lauf_nr'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.waldschadenkarte.jahr_schad', lang)}</td>            <td>${c['attributes']['jahr_schad'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.waldschadenkarte.gde_name', lang)}</td>              <td>${c['attributes']['gde_name'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.waldschadenkarte.lokalname', lang)}</td>            <td>${c['attributes']['lokalname'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.waldschadenkarte.x_koord', lang)}</td>               <td>${c['attributes']['x_koord'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.waldschadenkarte.y_koord', lang)}</td>               <td>${c['attributes']['y_koord'] or '-'}</td></tr>
</%def>

