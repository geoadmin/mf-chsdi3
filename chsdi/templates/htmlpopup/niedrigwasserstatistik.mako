<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
    hyperlink = 'hyperlink_%s' % lang
%>
<% c['stable_id'] = True %>
<tr><td class="cell-left">${_('ch.bafu.hydrologie-niedrigwasserstatistik.name')}</td>           <td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.hydrologie-niedrigwasserstatistik.url_nqpdf')}</td>      <td><a href="${c['attributes']['url_nqpdf'] or '-'}" target="_blank">${_('PDF') or '-'}</a></td></tr>
<tr><td class="cell-left">${_('ch.bafu.hydrologie-niedrigwasserstatistik.hyperlink')}</td>      <td><a href="${c['attributes'][hyperlink] or '-'}" target="_blank">${_('link') or '-'}</a></td></tr>
</%def>
