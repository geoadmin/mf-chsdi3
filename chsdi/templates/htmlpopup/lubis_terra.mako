<%inherit file="base.mako"/>

<%!
import datetime
import chsdi.lib.helpers as h

def br(text):
    return text.replace('\n', markupsafe.Markup('<br />'))

def date_to_str(datum):
    try:
        return datetime.datetime.strptime(datum.strip(), "%Y%m%d").strftime("%d-%m-%Y")
    except:
        pass

    try:
        return datetime.datetime.strptime(datum.strip(), "%Y%m").strftime("%m-%Y")
    except:
        return datum

%>

<%def name="table_body(c, lang)">
<%

tt_lubis_ebkey = c['layerBodId'] + '.' + 'id'
lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')

datum = date_to_str(c['attributes']['flugdatum'])
dataGeoAdminHost = request.registry.settings['datageoadminhost']
asset_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.tif"
preview_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.jpg"
meta_csv_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.csv"
viewer_url=asset_url
tt_lubis_Quickview='tt_lubis_Quickview_stac'
pdf = h.resource_exists(c['attributes']['expert_sheet_url']) if c['attributes']['expert_sheet_url'] else None
url_smapshot= "https://smapshot.heig-vd.ch/map/?imageId={}".format(c['attributes']['smapshot_id'])
# legacy: old ebkeys with fullresviewer in aerialimages bucket
# this part can be removed when the migration of the aerialimages bucket to stac/data.geo.admin.ch is finished
%>
<tr><td class="cell-left">${_(tt_lubis_ebkey)}</td>                       <td><a href="${asset_url}" target="_blank">${c['featureId'] or '-'}</a></td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_lubis_aufnahmedatum')}</td><td>${datum or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.operate_name')}</td>      <td>${c['attributes']['ort'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.station')}</td>      <td>${c['attributes']['station'] or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_x')}</td>        <td>${c['attributes']['x'] or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_y')}</td>        <td>${c['attributes']['y'] or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_Filmart')}</td>                   <td>${c['attributes']['filmart'] or '-'}</td></tr>
% if pdf:
<tr><td class="cell-left">${_('link')}</td><td><a href="${c['attributes']['expert_sheet_url']}" target="_blank">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.expertenlink')} - pdf</a></td></tr>
% endif
<tr><td class="cell-left">${_('link')} smapshot</td>                    <td><a href="${url_smapshot}" target="_blank">${_('link')} smapshot</a></td></tr>
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
