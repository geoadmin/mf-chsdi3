<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
        url_sac = 'url_sac_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.unterkuenfte-winter.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    %if c['attributes'][url_sac]:
    <tr>
        <td class="cell-left">${_('ch.swisstopo.unterkuenfte-winter.url_sac')}</td>
        % if c['attributes'][url_sac].startswith('http'):
            <td><a href="${c['attributes'][url_sac]}" target="_blank">${_('sac_tourenportal')}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    %endif
</%def>

