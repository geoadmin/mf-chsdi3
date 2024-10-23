<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr', 'it', 'en') else 'de'
    name = 'name_%s' % lang
    difficulty = 'difficulty_%s' % lang
    url_sac = 'url_sac_%s' % lang
%>
    <% c['stable_id'] = True %>
    % if c['attributes']['source_url']:
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.name')}</td>             <td>${c['attributes'][name] or c['attributes']['name'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.source_txt')}</td>       <td><a target="_blank" href="${c['attributes']['source_url']}">${c['attributes']['source_txt'] or 'link'}</td></tr>
    % else:
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.summit')}</td>           <td>${c['attributes']['target_name']} (${c['attributes']['target_altitude'] or '-'} m)</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.name')}</td>             <td>${c['attributes'][name] or c['attributes']['name'] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.difficulty')}</td>       <td>${c['attributes'][difficulty] or '-'}</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.ascent')}</td>           <td>${c['attributes']['ascent_time_label'] or '-'}, ${c['attributes']['ascent_altitude'] or '-'} Hm</td></tr>
        <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.descent')}</td>          <td>${c['attributes']['descent_altitude'] or '-'} Hm</td></tr>
        % if c['attributes'][url_sac]:
            <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.info')}</td>         <td><a target="_blank" href="${c['attributes'][url_sac]}">${_('ch.swisstopo-karto.skitouren.info')}</a></td></tr>
        % else:
            <tr><td class="cell-left">${_('ch.swisstopo-karto.skitouren.info')}</td>         <td>-</td></tr>
        % endif
    % endif

</%def>
