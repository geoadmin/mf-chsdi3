<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('de', 'fr', 'it', 'en') else 'de'
        name = 'name_%s' % lang
        description = 'description_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bazl.landschaftsruhezonen.name')}</td>
        <td>${c['attributes'][name] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.landschaftsruhezonen.description')}</td>
        <td>${c['attributes'][description] or '-'}</td>
    </tr>
</%def>
