<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        lang = land if lang in ('de', 'fr', 'it', 'en') else 'de'
        version_text = 'version_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.map_nbr')}</td>
        <td>${c['attributes']['map_nbr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.map_title')}</td>
        <td>${c['attributes']['map_title'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.scale')}</td>
        <td>${c['attributes']['scale'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.version')}</td>
        <td>${c['attributes'][version_text] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-geocover.metadata.basis')}</td>
        <td>${c['attributes']['basis'] or '-'}</td>
    </tr>
</%def>
