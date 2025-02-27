<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang_select = lang if lang in ('fr','it','en') else 'de'
        name_text = 'name_%s' % lang_select
        info_text = 'info_%s' % lang_select
    %>
    <tr>
        <td class="cell-left">${_('ch.bafu.trockenheitsindex.name')}</td>
        <td>${c['attributes'][name_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.trockenheitsindex.info')}</td>
        <td>${c['attributes'][info_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.trockenheitsindex.valid_from')}</td>
        <td>${c['attributes']['valid_from'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.trockenheitsindex.valid_to')}</td>
        <td>${c['attributes']['valid_to'] or '-'}</td>
    </tr>

</%def>
