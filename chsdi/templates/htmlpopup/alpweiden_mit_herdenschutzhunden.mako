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
        <td class="cell-left">${_(layerid + '.name')}</td>
        <td>${name or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.typzone')}</td>
        <td>${typzone or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.allginfo')}</td>
        <td>${allginfo or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.refverhalten')}</td>
        <td>${refverhalten or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.hundepraesenz')}</td>
        <td>${hundepraesenz or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.hinweis')}</td>
        <td>${hinweis or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.kontname')}</td>
        <td>${kontname or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.konttel')}</td>
        <td>${konttel or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(layerid + '.kontemail')}</td>
        <td>${kontemail or '-'}</td>
    </tr>
</%def>
