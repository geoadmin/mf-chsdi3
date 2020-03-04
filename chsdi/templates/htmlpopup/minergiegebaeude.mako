<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = 'de' if lang == 'rm' else lang
    info = c['attributes']['buildinginfo_%s' % lang] or '-'
    http = c['attributes']['http_%s' % lang]
%>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.minergiegebaeude.zertifikat', lang)}</td><td>${c['attributes']['certificate'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.minergiegebaeude.standard', lang)}</td><td>${c['attributes']['standard'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.minergiegebaeude.adresse', lang)}</td><td>${c['attributes']['street'] or ''}&nbsp;${c['attributes']['streetnr'] or ''}</td></tr>
    <tr><td class="cell-left">&nbsp;</td><td>${c['attributes']['postcode'] or ''}&nbsp;${c['attributes']['place'] or ''}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.minergiegebaeude.kanton', lang)}</td><td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.minergiegebaeude.gebaeude', lang)}&nbsp;(${mod_translate.Translator.translate('ch.bfe.minergiegebaeude.energiebezugsflaeche', lang)}&nbsp;m<sup>2</sup>)</td><td>${info}&nbsp;(${c['attributes']['ebf'] or '-'}&nbsp;m<sup>2</sup>)</td></tr>
    % if http is not None:
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bfe.minergiegebaeude.weitere_informationen', lang)}</td><td><a href="${http}" target="_blank">${mod_translate.Translator.translate('ch.bfe.minergiegebaeude', lang)}</a></td></tr>
    % endif

</%def>
