<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr',) else 'de'
    gmu = 'gmu_%s' % lang
    tecto = 'tecto_%s' % lang
    litho = 'litho_combined_%s' % lang
    chrono = 'chrono_combined_%s' % lang
    correlation = 'correlation_%s' % lang
    litstrat_bank = 'litstrat_formation_bank_%s' % lang
%>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.gmu')}</td>
        <td>${c['attributes'][gmu] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.tecto')}</td>
        <td>${c['attributes'][tecto] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.litho')}</td>
        <td>${c['attributes'][litho] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.chrono')}</td>
        <td>${c['attributes'][chrono] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.correlation')}</td>
        <td>${c['attributes'][correlation] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.litstrat_formation_bank')}</td>
        <td>${c['attributes'][litstrat_bank] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.strati_link')}</td>
        % if c['attributes']['strati_link'] and c['attributes']['strati_link'] not in ('-', ''):
            <td><a href="${c['attributes']['strati_link']}" target="_blank">${_('link')}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.erl_link')}</td>
        <td>${h.pipe_links(c['attributes'].get('erl_link')) | n}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-swissgeocover2d_bedrock.ber_link')}</td>
        <td>${h.pipe_links(c['attributes'].get('ber_link')) | n}</td>
    </tr>
</%def>
