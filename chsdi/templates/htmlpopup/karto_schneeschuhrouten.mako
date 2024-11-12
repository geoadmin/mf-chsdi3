<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    name = 'name_%s' % lang
    difficulty = 'difficulty_%s' % lang
    url_sac = 'url_sac_%s' % lang
    ascent_time_label = '%s, ' % c['attributes']['ascent_time_label'] if c['attributes']['ascent_time_label'] else ''
    target_altitude = ' (%s m)' % c['attributes']['target_altitude'] if c['attributes']['target_altitude'] else ''
%>
    % if c['attributes']['target_name']:
        <% c['stable_id'] = True %>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.summit')}</td>           <td>${c['attributes']['target_name'] or '-'}${target_altitude}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.name')}</td>             <td>${c['attributes'][name] or c['attributes']['name'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.difficulty')}</td>       <td>${c['attributes'][difficulty] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.ascent')}</td>           <td>${ascent_time_label}${c['attributes']['ascent_altitude'] or '-'} ${_('ch.swisstopo-karto.skitouren.height')}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.schneeschuhrouten.descent')}</td>          <td>${c['attributes']['descent_altitude'] or '-'} ${_('ch.swisstopo-karto.skitouren.height')}</td></tr>
        % if c['attributes'][url_sac]:
            <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.info')}</td>         <td><a target="_blank" href="${c['attributes'][url_sac]}">${_('ch.swisstopo-karto.skitouren.sac')}</a> (${_('ch.swisstopo-karto.skitouren.costs')})</td></tr>
        % else:
            <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.info')}</td>         <td>-</td></tr>
        % endif
    % else:
        <% c['stable_id'] = False %>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.name')}&nbsp;</td>             <td>${c['attributes'][name] or c['attributes']['name'] or '-'}</td></tr>
        % if c['attributes']['source_url']:
            <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.source_txt')}</td>   <td><a target="_blank" href="${c['attributes']['source_url']}">${c['attributes']['source_txt'] or 'link'}</td></tr>
        % endif
    % endif
</%def>
