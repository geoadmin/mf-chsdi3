<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%

lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')

tt_lubis_Quickview='tt_lubis_Quickview'

dataGeoAdminHost = request.registry.settings['datageoadminhost']
asset_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.tif"
preview_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.jpg"
meta_csv_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.csv"
viewer_url=asset_url
tt_lubis_Quickview='tt_lubis_Quickview_stac'

%>
<tr><td class="cell-left">${_('tt_lubis_ebkey')}</td>                                 <td>${c['featureId']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_Flugdatum')}</td>                             <td>${c['attributes']['flightdate']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_stereo_couple')}</td>        <td>${c['attributes']['stereo_couple']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_x')}</td>                    <td>${c['attributes']['x']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_y')}</td>                    <td>${c['attributes']['y']}</td></tr>
<tr><td class="cell-left">${_(f"{c['layerBodId']}.tt_lubis_schraegaufnahmen_z")}</td> <td>${c['attributes']['z']}</td></tr>
<tr><td class="cell-left">${_("zusatzinfo")}</td>
  <td>
    <a href="${meta_csv_url}" target="_blank">${_(f"{c['layerBodId']}.meta_csv_url")}</a>
  </td>
</tr>
<tr><td class="cell-left">${_(tt_lubis_Quickview)}</td>
  <td>
    <a href="${viewer_url}" target="_blank"><img src="${preview_url}" alt="quickview"></a>
  </td>
</tr>
</%def>
