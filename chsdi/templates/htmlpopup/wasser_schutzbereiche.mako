<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    typ_text = 'typ_%s' % lang
%>

    <tr><td class="cell-left">${mod_translate.Translator.translate('typ', lang)}</td>              <td>${c['attributes'][typ_text] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('gemkanton', lang)}</td>        <td>${c['attributes']['kanton'] or '-'}</td></tr>
    <tr><td class="cell-left">${mod_translate.Translator.translate('tt_source', lang)}</td>        <td>${c['attributes']['source'] or '-'}</td></tr>

</%def>

