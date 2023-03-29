<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
        purpose = 'purpose_%s' % lang
        discover = 'discover_%s' % lang
        status = 'status_%s' % lang
    %>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_md')}</td><td>${c['attributes']['td_m_md'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_tvd')}</td><td>${c['attributes']['td_m_tvd'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.fm_at_td')}</td><td>${c['attributes']['fm_at_td'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.purpose')}</td><td>${c['attributes'][purpose] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.discover')}</td><td>${c['attributes'][discover] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.status')}</td><td>${c['attributes'][status] or '-'}</td></tr>
</%def>

<%def name="extended_info(c,lang)">
    <%
        lang = lang if lang in ('fr','it','en', 'rm') else 'de'
        purpose = 'purpose_%s' % lang
        discover = 'discover_%s' % lang
        status = 'status_%s' % lang
        ref_type = 'ref_type_%s' % lang
        info = 'info_%s' % lang
        download = c['attributes']['download']
        web_link = c['attributes']['web_link']
    %>
    <table class="table-with-border bohrungen_tiefer_500-extended">
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_md')}</td><td>${c['attributes']['td_m_md'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.td_m_tvd')}</td><td>${c['attributes']['td_m_tvd'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.fm_at_td')}</td><td>${c['attributes']['fm_at_td'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.purpose')}</td><td>${c['attributes'][purpose] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.discover')}</td><td>${c['attributes'][discover] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.status')}</td><td>${c['attributes'][status] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.spud')}</td><td>${c['attributes']['spud'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.end')}</td><td>${c['attributes']['end'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.temp')}</td><td>${c['attributes']['temp'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.swissgeol')}</td><td>${c['attributes']['swissgeol'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.easting')}</td><td>${c['attributes']['easting'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.northing')}</td><td>${c['attributes']['northing'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.zgl')}</td><td>${c['attributes']['zgl'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.ref_type')}</td><td>${c['attributes'][ref_type] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.zref')}</td><td>${c['attributes']['zref'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.client')}</td><td>${c['attributes']['client'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.owner')}</td><td>${c['attributes']['owner'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.content')}</td><td>${c['attributes']['content'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.info')}</td><td>${c['attributes'][info] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.canton')}</td><td>${c['attributes']['canton'] or '-'}</td></tr>
        % if c['attributes']['web_link'] != '-':
            <%
                weblink = c['attributes']['web_link'].split('##')
            %>
            <tr>
                <th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link')}</th>
                <td>
                    % for i in range(len(weblink)):
                        <a href="${weblink[i]}" target="_blank">Link_${i+1}</a>&nbsp;
                    % endfor
                </td>
            </tr>
        % else:
            <tr>
                <th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.web_link')}</th>
                <td> - </td>
            </tr>
        % endif
        % if download != '-':
            <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</th>       <td><a href="${download}" target="_blank">Zip</a></td></tr>
        % else:
            <tr><th class="cell-left">${_('ch.swisstopo.geologie-bohrungen_tiefer_500.download')}</th>       <td>-</td></tr>
        % endif
    </table>
</%def>


