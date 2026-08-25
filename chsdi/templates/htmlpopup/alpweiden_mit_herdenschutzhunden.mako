<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = {'rm': 'de', 'it': 'fr'}.get(lang, lang)
        name = c['attributes']['name']
        typzone = c['attributes']['typzone_%s' % lang]
        allginfo = c['attributes']['allginfo_%s' % lang]
        refverhalten = c['attributes']['refverhalten_%s' % lang]
        hundepraesenz = c['attributes']['hundepraesenz_%s' % lang]
        hinweis = c['attributes']['hinweis_%s' % lang]
        kontname = c['attributes']['kontname']
        konttel = c['attributes']['konttel']
        kontemail = c['attributes']['kontemail']
        layerid = c['layerBodId']
    %>

    <% c['stable_id'] = True %>

    <tr>
        <td class="cell-left">${_(layerid + '.Name')}</td>
        <td>${name or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.TypZone')}</td>
        <td>${typzone or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.AllgInfo')}</td>
        % if allginfo and allginfo.startswith('http'):
            <td><a href="${allginfo}" target="_blank">${_('link')}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.RefVerhalten')}</td>
        % if refverhalten and refverhalten.startswith('http'):
            <td><a href="${refverhalten}" target="_blank">${_('link')}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.HundePraesenz')}</td>
        <td>${hundepraesenz or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.Hinweis')}</td>
        <td>${hinweis or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.KontName')}</td>
        <td>${kontname or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.KontTel')}</td>
        <td>${konttel or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.KontEmail')}</td>
        <td>${kontemail or '-'}</td>
    </tr>
</%def>
