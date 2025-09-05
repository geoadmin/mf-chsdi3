<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        layer = c['layerBodId']
        lang = lang if lang in ('fr','it','en') else 'de'
        grkind_text = 'grkind_%s' %lang
        crm_relevance_text = 'crm_relevance_%s' %lang
        mat_min_link_text = 'mat_min_link_%s' %lang
        empty_values = (None, '', '-')
    %>
    <tr>
        <td class="cell-left">${_(layer + '.obname')}</td>
        <td>${c['attributes']['obname'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.grkind')}</td>
        <td>${c['attributes'][grkind_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.rselids')}</td>
        <td>${c['attributes']['rselids'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.crm_relevance')}</td>
        <td>${c['attributes'][crm_relevance_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.crm_factsheets_link')}</td>
        % if c['attributes']['crm_factsheets_link'] in empty_values:
            <td>-</td>
        % else:
            <td><a target="_blank" href="${c['attributes']['crm_factsheets_link']}">${_('link')}</a></td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.mat_min_link')}</td>
        % if c['attributes'][mat_min_link_text] in empty_values:
            <td>-</td>
        % else:
            <td><a target="_blank" href="${c['attributes'][mat_min_link_text]}">${_('link')}</a></td>
        % endif
        </tr>
    <tr>
        <td class="cell-left">${_(layer + '.purl')}</td>
        % if c['attributes']['purl'] in empty_values:
            <td>-</td>
        % else:
            <td><a target="_blank" href="${c['attributes']['purl']}">${_('link')}</a></td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(layer + '.swissgeol_link')}</td>
        % if c['attributes']['swissgeol_link'] in empty_values:
            <td>-</td>
        % else:
            <td><a target="_blank" href="${c['attributes']['swissgeol_link']}">${_('link')}</a></td>
        % endif
    </tr>
</%def>
