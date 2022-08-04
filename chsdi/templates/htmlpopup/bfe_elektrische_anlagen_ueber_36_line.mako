<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
    %>

    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.bezeichnung')}</td>
        <td>${c['attributes']['bezeichnung'] or '-'}</td>
    </tr>
</%def>

