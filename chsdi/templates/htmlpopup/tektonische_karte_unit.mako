<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        lang = lang if lang in ('de', 'fr', 'it', 'en') else 'de'
        litho = 'litho_%s' % lang
        legende = 'legende_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Litho')}</td>
        <td>${c['attributes'][litho] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Notice')}</td>
        % if 'http' not in c['attributes']['notice']:
            <td>${c['attributes']['notice'] or '-'}</td>
        % else:
            <td><a target="_blank" href=${c['attributes']['notice']}>Link</a></td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Legende')}</td>
        % if 'http' not in c['attributes'][legende]:
            <td>${c['attributes'][legende] or '-'}</td>
        % else:
            <td><a target="_blank" href=${c['attributes'][legende]}>Link</a></td>
        % endif
    </tr>
</%def>

