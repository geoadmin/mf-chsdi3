<%inherit file="base.mako"/>

<%!
import datetime

def date_to_str(datum):
    try:
        return datetime.datetime.strptime(datum.strip(), "%Y%m%d").strftime("%d-%m-%Y")
    except:
        return request.translate('None') + request.translate('Datenstand')

%>

<%def name="table_body(c, lang)">
<%

lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')

datum = date_to_str(c['attributes']['flightdate'])
tt_lubis_Quickview='tt_lubis_Quickview'
image_width = None

dataGeoAdminHost = request.registry.settings['datageoadminhost']
asset_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}_2056.tif"
preview_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.jpg"
meta_csv_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.csv"
viewer_url=asset_url
tt_lubis_Quickview='tt_lubis_Quickview_stac'

%>
<tr><td class="cell-left">${_('tt_lubis_ebkey')}</td>                               <td>${c['featureId']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_Flugdatum')}</td>                           <td>${datum}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_bildpfad')}</td>                            <td>${c['attributes']['filename']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_stereo_couple')}</td>      <td>${c['attributes']['stereo_couple']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_x')}</td>                  <td>${c['attributes']['x']}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_y')}</td>                  <td>${c['attributes']['y']}</td></tr>
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
