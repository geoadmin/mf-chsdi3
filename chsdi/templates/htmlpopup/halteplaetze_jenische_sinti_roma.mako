<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it') else 'de'
    %>
    <tr>
        <td class="cell-left">${_('ch.bafu.bundesinventare-hochmoore.objnummer')}</td>
        <td>${c['attributes']['kanton'] or '-'}</td>
    </tr>
</%def>

