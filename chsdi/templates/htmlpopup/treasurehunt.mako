<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr', 'it') else 'de'
    title = 'title_%s' % lang
    link = 'link_%s' % lang
    information = 'info_%s' % lang

%>
    <tr><td class="cell-left">${mod_translate.Translator.translate('title', lang)}</td><td>${c['attributes'][title] or '-'|n}</td></tr>

% if c['attributes']['type_coord'] =='info':
    <tr>
    <td class="cell-left">${mod_translate.Translator.translate('information', lang)}</td><td>${c['attributes'][information] or '-'|n}</td>
    </tr>
% else:    
    <tr>
    <td class="cell-left">${mod_translate.Translator.translate('link', lang)}<td>
    <a href="${c['attributes'][link] or '-'|n}" target="_parent">${mod_translate.Translator.translate('treasure_hunt', lang)}</a></td>
    </tr>
% endif



</%def>



        
