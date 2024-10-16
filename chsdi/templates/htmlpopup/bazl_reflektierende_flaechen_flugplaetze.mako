<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('de', 'fr', 'it', 'en') else 'de'
        status_text = 'status_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bazl.reflektierende-flaechen_flugplaetze.icao')}</td>
        <td>${c['attributes']['icao'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.reflektierende-flaechen_flugplaetze.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.reflektierende-flaechen_flugplaetze.status')}</td>
        <td>${c['attributes'][status_text] or '-'}</td>
    </tr>
</%def>
