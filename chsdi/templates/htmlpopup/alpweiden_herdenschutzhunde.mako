<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == 'rm':
        lang = 'de'
    elif lang == 'it':
        lang = 'fr'
    code_refverhalten = c['attributes']['code_refverhalten']
    code_hundepraesenz = c['attributes']['code_hundepraesenz']
    code_hinweis = c['attributes']['code_hinweis']
%>
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.name', lang)}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.refverhalten', lang)}</td>
    % if code_refverhalten is not None:
        <td><a href="${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.refverhalten_code_%s' % code_refverhalten, lang)}" target="_blank">Link</a></td></tr>
    % endif
    % if code_hundepraesenz is not None:
        <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.hundepraesenz', lang)}</td><td>${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.hundepraesenz_code_%s' % code_hundepraesenz, lang)}</td></tr>
    % endif
    % if code_hinweis is not None:
        <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.hinweis', lang)}</td><td>${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.hinweis_code_%s' % code_hinweis, lang)}</td></tr>
    % endif
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.kontname', lang)}</td><td>${c['attributes']['kontname'].strip() or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.konttel', lang)}</td><td>${c['attributes']['konttel'].strip() or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.alpweiden-herdenschutzhunde.kontemail', lang)}</td><td>${c['attributes']['kontemail'].strip() or '-'}</td></tr>
</%def>
