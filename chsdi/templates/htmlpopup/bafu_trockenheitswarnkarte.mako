<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        name_text = 'name_%s' %lang
        info_text = 'info_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bafu.trockenheitswarnkarte.name')}</td>
        <td>${c['attributes'][name_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.trockenheitswarnkarte.info')}</td>
        <td>${c['attributes'][info_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.trockenheitswarnkarte.valid_from')}</td>
        <td>${c['attributes']['valid_from'] or '-'}</td>
    </tr>
</%def>
