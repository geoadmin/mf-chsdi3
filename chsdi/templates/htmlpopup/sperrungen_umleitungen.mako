<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang != 'rm' else 'de'
        title = 'title_%s' % lang
        sperrungen_type = 'sperrungen_type_%s' % lang
        duration = 'duration_%s' % lang
        reason = 'reason_%s' % lang
        abstract = 'abstract_%s' % lang
        state_validate = 'state_validate_%s' % lang
        content_provider = 'content_provider_%s' % lang
        url1_link = 'url1_link_%s' % lang
        document = 'file_%s' % lang
    %>
    <% c['stable_id'] = False %>
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.title')}</td>                    <td>${c['attributes'][title] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.duration')}</td>                 <td>${c['attributes'][duration] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.reason')}</td>                   <td>${c['attributes'][reason] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.abstract')}</td>                 <td>${c['attributes'][abstract] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.state_validate')}</td>           <td>${c['attributes'][state_validate] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.content_provider')}</td>         <td>${c['attributes'][content_provider] or '-'}</td></tr>
% if c['attributes'][document]:
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.file')}</td>                     <td><a href="${c['attributes'][document]}" target="_blank">PDF</a></td></tr>
% else:
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.file')}</td>                     <td>-</td></tr>
% endif
% if c['attributes'][url1_link]:
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.url1_link')}</td>                <td><a href="${c['attributes'][url1_link]}" target="_blank">Link</a></td></tr>
%  else:
    <tr><td class="cell-left">${_('ch.astra.wanderland-sperrungen_umleitungen.url1_link')}</td>                <td>-</td></tr>
% endif

</%def>

