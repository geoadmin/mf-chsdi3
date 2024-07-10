<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        if lang in ('de', 'rm', 'en'):
            lang = 'de'
        else:
            lang = 'fr'
        typ = 'typ_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bfs.statistische-grundeinheiten_stufe1.u1_id')}</td>
        <td>${c['attributes']['u1_id'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.statistische-grundeinheiten_stufe1.u1_name')}</td>
        <td>${c['attributes']['u1_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.statistische-grundeinheiten_stufe1.u1_gr_typ')}</td>
        <td>${c['attributes'][typ] or '-'}</td>
    </tr>
</%def>

