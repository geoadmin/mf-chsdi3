<%inherit file="base.mako"/>

<%!
from pyramid.url import route_url
%>

<%def name="table_body(c, lang)">
<%
shop_url = request.registry.settings['shop_url']
%>

<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.swisstopo.lubis-bildstreifen.id')}</td>          <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${_('tt_lubis_Flugdatum')}</td>       <td>${c['attributes']['flugdatum']}</td></tr>
    <tr><td class="cell-left">${_('tt_lubis_auflosung')}</td>       <td>${c['attributes']['resolution']}</td></tr>
% if   c['attributes']['gsd'] != 0.25 and c['attributes']['gsd'] != 0.5 and round(c['attributes']['gsd'],1) != 0.1:
    <tr><td class="cell-left">${_('tt_firmen_Link')}</td>          <td><a href="mailto:geodata@swisstopo.ch?subject=${_('tt_firmen_Link ')} ebkey:${c['featureId']}">geodata@swisstopo.ch</a></td></tr>
% endif
</%def>

<%def name="extended_info(c, lang)">
<%
c['stable_id'] = True
shop_url = request.registry.settings['shop_url']
protocol = request.scheme
c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
topic = request.matchdict.get('map')
lang = request.lang
%>
<title>${_('tt_lubis_ebkey')}: ${c['featureId']}</title>
<body onload="init()">

    <table class="table-with-border kernkraftwerke-extended">
        <tr><th class="cell-left">${_('tt_lubis_lineId')}</th>              <td>${c['featureId']}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_Flugdatum')}</th>           <td>${c['attributes']['flugdatum']}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_auflosung')}</th>           <td>${c['attributes']['resolution']}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_y1')}</th>                  <td>${c['attributes']['toposhop_start_x'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_x1')}</th>                  <td>${c['attributes']['toposhop_start_y'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_y2')}</th>                  <td>${c['attributes']['toposhop_end_x'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_x2')}</th>                  <td>${c['attributes']['toposhop_end_y'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_linielaenge')}</th>         <td>${c['attributes']['toposhop_length'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_project')}</th>             <td>${c['attributes']['goal'] or '-'}</td></tr>
        <tr><th class="cell-left">${_('tt_lubis_source_georef')}</th>       <td>${c['attributes']['source_georef'] or '-'}</td></tr>
% if   c['attributes']['gsd'] == 0.25 or c['attributes']['gsd'] == 0.5 or round(c['attributes']['gsd'],1) == 0.1:
        <tr><th class="cell-left">${_('link')} Online Shop</th>
        <td><a href="https:${shop_url}/${lang}/dispatcher?layer=${c['layerBodId']}&featureid=${c['featureId']}"
target="toposhop">Online Shop</a></td></tr>
% else:
        <tr><th class="cell-left">${_('tt_firmen_Link')}</th>              <td><a href="mailto:geodata@swisstopo.ch?subject=${_('tt_firmen_Link ')} ebkey:${c['featureId']}">geodata@swisstopo.ch</a></td></tr>
% endif
</table>
  <br>
<div class="chsdi-map-container table-with-border">
 <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic,'&bgLayer=ch.swisstopo.pixelkarte-grau'))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
</div>

</body>

</%def>


<%def name="extended_resources(c, lang)">
  <script type="text/javascript" src="${h.get_loaderjs_url(request)}"></script>
</%def>
