<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr>
        <td class="cell-left">${_('ch.bfs.statistische-grundeinheiten_stufe2.u2_id')}</td>
        <td>${c['attributes']['u2_id'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.statistische-grundeinheiten_stufe2.u2_name')}</td>
        <td>${c['attributes']['u2_name'] or '-'}</td>
    </tr>
</%def>
