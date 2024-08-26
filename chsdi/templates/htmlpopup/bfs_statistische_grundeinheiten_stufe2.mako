<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        c['stable_id'] = True
    %>
    <tr>
        <td class="cell-left">${_('ch.bfs.statistische-grundeinheiten_stufe2.u2_id')}</td>
        <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.statistische-grundeinheiten_stufe2.u2_name')}</td>
        <td>${c['attributes']['u2_name'] or '-'}</td>
    </tr>
</%def>
