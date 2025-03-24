<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <% c['stable_id'] = True %>
    <%
        lang = lang if lang in ('fr', 'it', 'en') else 'de'
        url_text = 'url_%s' % lang
    %>

    <tr>
        <td class="cell-left">${_('ch.bafu.nabelstationen.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.nabelstationen.nabeltyp')}</td>
        <td>${c['attributes']['typ'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.nabelstationen.werte')}</td>
        <td>${c['attributes']['desc'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.nabelstationen.url')}</td>
        % if c['attributes'][url_text] and c['attributes'][url_text].startswith('http'):
            <td><a href="${c['attributes'][url_text]}" target="_blank">${_('link')}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>

