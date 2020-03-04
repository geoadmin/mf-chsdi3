<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.armeelogistikcenter.name', lang)}</td>
    <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.armeelogistikcenter.abkuerzung', lang)}</td>
    <td>${c['attributes']['abkuerzung'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.armeelogistikcenter.mail', lang)}</td>
    <td><a href="mailto:${c['attributes']['mail'] or '-'}">${mod_translate.Translator.translate('ch.vbs.armeelogistikcenter.mail', lang)}</a></td>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.vbs.armeelogistikcenter.url', lang)}</td>
    <td><a href="http://${c['attributes']['url'] or '-'}" target="_blank">${mod_translate.Translator.translate('ch.vbs.armeelogistikcenter.url', lang)}</a></td></tr>
</%def>

