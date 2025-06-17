<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr', 'it') else 'de'
        gbae_text = 'gbae_%s' % lang
    %>

    <% c['stable_id'] = True %>

    <tr>
        <td class="cell-left">${_('ch.bfs.arbeitsmarktregionen.bae_code')}</td>
        <td>${c['featureId']}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.arbeitsmarktregionen.bae_name')}</td>
        <td>${c['attributes']['bae_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.arbeitsmarktregionen.gbae_code')}</td>
        <td>${c['attributes']['gbae_code'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfs.arbeitsmarktregionen.gbae_name')}</td>
        <td>${c['attributes'][gbae_text] or '-'}</td>
    </tr>

</%def>
