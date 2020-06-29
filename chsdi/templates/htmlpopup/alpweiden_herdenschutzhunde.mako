<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    if lang == 'rm':
        lang = 'de'
    elif lang == 'it':
        lang = 'fr'
    code_refverhalten = c['attributes']['code_refverhalten']
    code_hundepraesenz = c['attributes']['code_hundepraesenz']
    code_hinweis = c['attributes']['code_hinweis']
%>
    <% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.bafu.alpweiden-herdenschutzhunde.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.alpweiden-herdenschutzhunde.refverhalten')}</td>
    % if code_refverhalten is not None:
        <td><a href="${_('ch.bafu.alpweiden-herdenschutzhunde.refverhalten_code_%s' % code_refverhalten)}" target="_blank">Link</a></td></tr>
    % endif
    % if code_hundepraesenz is not None:
        <tr><td class="cell-left">${_('ch.bafu.alpweiden-herdenschutzhunde.hundepraesenz')}</td><td>${_('ch.bafu.alpweiden-herdenschutzhunde.hundepraesenz_code_%s' % code_hundepraesenz)}</td></tr>
    % endif
    % if code_hinweis is not None:
        <tr><td class="cell-left">${_('ch.bafu.alpweiden-herdenschutzhunde.hinweis')}</td><td>${_('ch.bafu.alpweiden-herdenschutzhunde.hinweis_code_%s' % code_hinweis)}</td></tr>
    % endif
    <tr><td class="cell-left">${_('ch.bafu.alpweiden-herdenschutzhunde.kontname')}</td><td>${c['attributes']['kontname'] or '-'.strip()}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.alpweiden-herdenschutzhunde.konttel')}</td><td>${c['attributes']['konttel'] or '-'.strip()}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.alpweiden-herdenschutzhunde.kontemail')}</td><td>${c['attributes']['kontemail'] or '-'.strip()}</td></tr>
</%def>
