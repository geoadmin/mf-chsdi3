<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    dataGeoAdminHost = request.registry.settings['datageoadminhost']
    dataPath = 'ch.swisstopo.geologie-geotechnik-gk200/PDF'
    url_pdf = "https://" + dataGeoAdminHost + "/" + dataPath + "/" + c['attributes']['file_name'] + '_' + lang + '.pdf'
%>
    <tr><td colspan="3">&nbsp;</tr>
    <tr>
      <td>${h.translate('Legend', lang)}</td>
      <td width="20">&nbsp;</td>
      <td><a href="${url_pdf}" target="_blank">${h.translate('tt_geotechnik_gk200', lang)}</a></td>
    </tr>
    <tr><td colspan="3">&nbsp;</tr>
</%def>
