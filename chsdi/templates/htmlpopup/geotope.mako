<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<tr><td class="cell-left">${_('name')}</td><td>${c['attributes']['nom'] or '-'}</td></tr>
<tr><td class="cell-left">${_('nummer')}</td><td>${c['attributes']['nummer'] or '-'}</td></tr>
<%
    dataGeoAdminHost = request.registry.settings['datageoadminhost']
    url_pdf = "https://" + dataGeoAdminHost + '/ch.swisstopo.geologie-geotope/PDF/geotope-CH_' + c['attributes']['fix_id'] + '.pdf'
%>
<tr><td class="cell-left">${_('link2dok')}</td>    <td><a href="${url_pdf}" target="_blank">Link</a></td></tr>
</%def>
