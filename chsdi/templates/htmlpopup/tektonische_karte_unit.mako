<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        lang = lang if lang in ('de', 'fr', 'it', 'en') else 'de'
        tecto_1 = 'tecto_1_%s' % lang
        tecto_2 = 'tecto_2_%s' % lang
        tecto_3 = 'tecto_3_%s' % lang
        tecto_4 = 'tecto_4_%s' % lang
        origin = 'origin_%s' % lang
        litho = 'litho_%s' % lang
        chrono = 'chrono_%s' % lang
        lith = 'lith_%s' % lang
        legende = 'legende_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Tecto_1')}</td>
        <td>${c['attributes'][tecto_1] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Tecto_2')}</td>
        <td>${c['attributes'][tecto_2] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Tecto_3')}</td>
        <td>${c['attributes'][tecto_3] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Tecto_4')}</td>
        <td>${c['attributes'][tecto_4] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Litho')}</td>
        <td>${c['attributes'][litho] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-tektonische_karte.Origin')}</td>
        <td>${c['attributes'][origin] or '-'}</td>
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

