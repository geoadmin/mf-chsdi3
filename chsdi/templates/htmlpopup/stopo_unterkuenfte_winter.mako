<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
        url_sac = 'url_sac_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.unterkuenfte-winter.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.unterkuenfte-winter.url_sac')}</td>
        <td>${c['attributes'][url_sac] or '-'}</td>
    </tr>
</%def>

