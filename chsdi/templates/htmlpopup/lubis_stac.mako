<%inherit file="base.mako"/>

<%!
import datetime
%>

<%def name="table_body(c, lang)">
<%

tt_lubis_ebkey = f"{c['layerBodId']}.id"
lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')

tt_lubis_Quickview='tt_lubis_Quickview'

datum = datetime.datetime.strptime(c['attributes']['acquired'], '%Y-%m-%d').strftime("%d-%m-%Y")
dataGeoAdminHost = request.registry.settings['datageoadminhost']
aerialimages_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['attributes']['filename']}"
meta_csv_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.csv"
orthophoto_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['attributes']['orthofilename']}"
preview_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.jpg"

viewer_url=aerialimages_url
tt_lubis_Quickview='tt_lubis_Quickview_stac'
%>

<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.id")}</td>
  <td>
    <a href="${aerialimages_url}" target="_blank">${c['featureId'] or '-'}</a>
  </td>
</tr>
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.acquired")}</td>
  <td>${datum or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.film_type")}</td>
  <td>${c['attributes']['filmart'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.orthofilename")}</td>
% if c['attributes']['orthofilename']:
  <td>
    <a href="${orthophoto_url}" target="_blank">${c['attributes']['orthofilename']}</a>
  </td>
% else:
  <td>-</td>
% endif
</tr>
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.e")}</td>
  <td>${c['attributes']['e'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.n")}</td>
  <td>${c['attributes']['n'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_(f"{c['layerBodId']}.z")}</td>
  <td>${c['attributes']['z'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_("zusatzinfo")}</td>
  <td>
    <a href="${meta_csv_url}" target="_blank">${_(f"{c['layerBodId']}.meta_csv_url")}</a>
  </td>
</tr>

<tr>
  <td class="cell-left">${_(tt_lubis_Quickview)}</td>
  <td>
    <a href="${viewer_url}" target="_blank"><img src="${preview_url}" alt="quickview"></a>
  </td>
</tr>

</%def>
