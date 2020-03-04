<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
    hyperlink = 'hyperlink_%s' % lang
%>
<% c['stable_id'] = True %>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-niedrigwasserstatistik.name', lang)}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-niedrigwasserstatistik.url_nqpdf', lang)}</td>      <td><a href="${c['attributes']['url_nqpdf'] or '-'}" target="_blank">${_('PDF') or '-'}</a></td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.hydrologie-niedrigwasserstatistik.hyperlink', lang)}</td>      <td><a href="${c['attributes'][hyperlink] or '-'}" target="_blank">${_('link') or '-'}</a></td></tr>
</%def>
