<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<tr><td class="cell-left">${_('name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${_('siegel')}</td><td>${c['attributes']['siegel'] or '-'}</td></tr>
<tr><td class="cell-left">${_('inventar')}</td><td>${c['attributes']['inventar'] or '-'}</td></tr>
<tr><td class="cell-left">${_('dataviewer')}</td><td>${c['attributes']['dataviewer'] or '-'}</td></tr>
<%
    dataGeoAdminHost = request.registry.settings['datageoadminhost']
    url_pdf = "https://" + dataGeoAdminHost + '/ch.swisstopo.geologie-geotope/PDF/geotope-CH_' + c['attributes']['fix_id'] + '.pdf'
%>
<tr><td class="cell-left">${_('dataviewer')}</td>    <td><a href="${dataviewer}"target="_blank">Link</a></td></tr>
</%def>
