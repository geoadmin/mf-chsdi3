<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it') else 'de'
        hinweis_text = 'hinweis_%s' %lang
        genh1_text = 'genh1_%s' %lang
        gwaersceh1_text = 'gwaersceh1_%s' %lang
        linkpdf_text = 'linkpdf_%s' %lang
        linkbafu_text = 'linkbafu_%s' %lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.egid')}</td>
        <td>${c['featureId'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.hinweis')}</td>
        <td>${c['attributes'][hinweis_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.co2_range')}</td>
        <td>${c['attributes']['co2_range'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.genh1')}</td>
        <td>${c['attributes'][genh1_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.gwaersceh1')}</td>
        <td>${c['attributes'][gwaersceh1_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.gexpdat')}</td>
        <td>${c['attributes']['gexpdat'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.linkco2')}</td>
        % if c['attributes']['linkco2'] == None:
            <td>-</td>
        % else:
            <td><a target="_blank" href="${c['attributes']['linkco2']}">${_('link')}</a></td>
        % endif 
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.linkpdf')}</td>
        % if c['attributes'][linkpdf_text] == None:
            <td>-</td>
        % else:
            <td><a target="_blank" href="${c['attributes'][linkpdf_text]}">${_('link')}</a></td>
        % endif 
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.klima-co2_ausstoss_gebaeude.linkbafu')}</td>
        % if c['attributes'][linkbafu_text] == None:
            <td>-</td>
        % else:
            <td><a target="_blank" href="${c['attributes'][linkbafu_text]}">${_('link')}</a></td>
        % endif 
    </tr>
</%def>
