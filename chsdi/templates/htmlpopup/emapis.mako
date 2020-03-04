<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    status = 'status_%s' % lang
    typ = 'typ_%s' % lang
%>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.blw.emapis.typ', lang)}</td>               <td>${c['attributes'][typ]}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.blw.emapis.status', lang)}</td>            <td>${c['attributes'][status] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('ch.blw.emapis.geschaeftsnummer', lang)}</td>  <td>${c['attributes']['geschaeftsnummer'] or '-'}</td></tr>
</%def>
