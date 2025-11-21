<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = 'de' if lang in ('de','rm') else 'fr' if lang in ('fr','it') else 'en'

        purpose = 'purpose_%s' % lang
    %>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_md')}</td><td>${c['attributes']['td_m_md'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_tvd')}</td><td>${c['attributes']['td_m_tvd'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.fm_at_td')}</td><td>${c['attributes']['fm_at_td'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.purpose')}</td><td>${c['attributes'][purpose] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.spud')}</td><td>${c['attributes']['spud'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.temp')}</td><td>${c['attributes']['temp'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c,lang)">
    <%
        lang = 'de' if lang in ('de','rm') else 'fr' if lang in ('fr','it') else 'en'

        purpose = 'purpose_%s' % lang
        discover = 'discover_%s' % lang
        status = 'status_%s' % lang
        ref_type = 'ref_type_%s' % lang
        info = 'info_%s' % lang
        swissgeol = c['attributes']['swissgeol']
        web_link = c['attributes']['web_link']
        download = c['attributes']['download']
    %>
    <table class="table-with-border bohrungen_tiefer_500-extended">
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</th><td>${c['attributes']['name'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_md')}</th><td>${c['attributes']['td_m_md'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_tvd')}</th><td>${c['attributes']['td_m_tvd'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.fm_at_td')}</th><td>${c['attributes']['fm_at_td'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.purpose')}</th><td>${c['attributes'][purpose] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.discover')}</th><td>${c['attributes'][discover] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.status')}</th><td>${c['attributes'][status] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.spud')}</th><td>${c['attributes']['spud'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.end')}</th><td>${c['attributes']['end'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.temp')}</th><td>${c['attributes']['temp'] or '-'}</td></tr>
        <tr>
            <th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.swissgeol')}</th>
            % if swissgeol != '-':
                <%
                    swissgeols = swissgeol.split(' / ')
                %>
                <td>
                    % for i in range(len(swissgeols)):
                        <a href="${swissgeols[i]}" target="_blank">${_('link')}_${i+1}</a>&nbsp;
                    % endfor
                </td>
            % else:
                <td>-</td>
            % endif
        </tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.easting')}</th><td>${c['attributes']['easting'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.northing')}</th><td>${c['attributes']['northing'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.zgl')}</th><td>${c['attributes']['zgl'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.ref_type')}</th><td>${c['attributes'][ref_type] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.zref')}</th><td>${c['attributes']['zref'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.client')}</th><td>${c['attributes']['client'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.owner')}</th><td>${c['attributes']['owner'] or '-'}</td></tr>
        <tr>
            <th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</th>
            % if download != '-':
                <td><a href="${download}" target="_blank">${_('link')}</a></td>
            % else:
                <td>-</td>
            % endif
        </tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.content')}</th><td>${c['attributes']['content'] or '-'}</td></tr>
        <tr>
            <th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link')}</th>
            % if web_link != '-':
                <%
                    web_links = web_link.split(' / ')
                %>
                <td>
                    % for i in range(len(web_links)):
                        <a href="${web_links[i]}" target="_blank">${_('link')}_${i+1}</a>&nbsp;
                    % endfor
                </td>
            % else:
                <td> - </td>
            % endif
        </tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.info')}</th><td>${c['attributes'][info] or '-'}</td></tr>
        <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.canton')}</th><td>${c['attributes']['canton'] or '-'}</td></tr>
    </table>
</%def>
