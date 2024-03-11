<%inherit file="base.mako"/>
<%namespace name="lubis_map" file="../luftbilder/lubis_map.mako"/>

<%!
import datetime
import urllib
from pyramid.url import route_url
import chsdi.lib.helpers as h
import markupsafe

def br(text):
    return text.replace('\n', markupsafe.Markup('<br />'))

def determinePreviewUrl(tileUrlBasePath, ebkey):

    tileUrlBasePath = tileUrlBasePath

    def getPreviewImageUrl(ebkey):
        return tileUrlBasePath + '/' + ebkey + '/quickview.jpg'

    def getZeroTileUrl(ebkey):
        return tileUrlBasePath + '/' + ebkey + '/1/0/0.jpg'

    headers = {'Referer': 'http://admin.ch'}
    url = getPreviewImageUrl(ebkey)
    #testing these 2 url could be done more python like
    if not h.resource_exists(url, headers):
         url = getZeroTileUrl(ebkey)

    return url

def date_to_str(datum):
    try:
        return datetime.datetime.strptime(datum.strip(), "%Y%m%d").strftime("%d-%m-%Y")
    except:
        pass

    try:
        return datetime.datetime.strptime(datum.strip(), "%Y%m").strftime("%m-%Y")
    except:
        return datum

def get_viewer_url(request, params):
    f = {
        'width': params[0],
        'height': params[1],
        'title': params[2].encode('utf8'),
        'bildnummer': params[3],
        'datenherr': params[4].encode('utf8'),
        'layer': params[5].encode('utf8'),
        'lang': params[6],
        'rotation': params[7]
    }
    return h.make_agnostic(route_url('luftbilder', request)) + '?' + urllib.parse.urlencode(f)

%>

<%def name="table_body(c, lang)">
<%

tt_lubis_ebkey = c['layerBodId'] + '.' + 'id'
lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')

aerialimages_data_host = request.registry.settings['aerialimages_data_host']
tileUrlBasePath = aerialimages_data_host + '/tiles'
preview_url = determinePreviewUrl(tileUrlBasePath, c['featureId'])


# set true if featureId comes from stac
isStac = c['featureId'].startswith('lubis-terrestrische_aufnahmen')

datum = date_to_str(c['attributes']['flugdatum'])
if isStac:
  dataGeoAdminHost = request.registry.settings['datageoadminhost']
  asset_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.tif"
  preview_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.jpg"
  meta_csv_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.csv"
  viewer_url=asset_url
  tt_lubis_Quickview='tt_lubis_Quickview_stac'
  url_pdf = dataGeoAdminHost + "/" + c['layerBodId'] + "/pdf/" + c['attributes']['base_uuid'] + '.pdf'
  pdf = h.resource_exists(url_pdf) or None
  url_smapshot= "https://smapshot.heig-vd.ch/map/?imageId={}".format(c['attributes']['smapshot_id'])
# legacy: old ebkeys with fullresviewer in aerialimages bucket
# this part can be removed when the migration of the aerialimages bucket to stac/data.geo.admin.ch is finished
else:
  image_rotation = 0
  firma = '-'
  wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
  image_width = wh[1]
  image_height = wh[0]
  params = (
      image_width,
      image_height,
      _('tt_lubis_ebkey'),
      c['featureId'],
      firma,
      c['layerBodId'],
      lang,
      image_rotation)
  viewer_url = get_viewer_url(request, params)

%>
% if isStac: # STAC Tooltips
<tr><td class="cell-left">${_(tt_lubis_ebkey)}</td>                       <td>${c['attributes']['image_number'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_lubis_aufnahmedatum')}</td><td>${datum or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_bildpfad')}</td>                  <td>${c['attributes']['filename'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.operate_name')}</td>      <td>${c['attributes']['ort'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.station')}</td>      <td>${c['attributes']['station'] or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_x')}</td>        <td>${c['attributes']['x'] or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_schraegaufnahmen_y')}</td>        <td>${c['attributes']['y'] or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_Filmart')}</td>                   <td>${c['attributes']['filmart'] or '-'}</td></tr>
% if pdf:
<tr><td class="cell-left">${_('link')}</td><td><a href="${url_pdf}" target="_blank">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.expertenlink')} - pdf</a></td></tr>
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
% else: # OLD Tooltips with GDWH datasource
<tr><td class="cell-left">${_(tt_lubis_ebkey)}</td>                       <td>${c['attributes']['image_number'] or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_inventarnummer')}</td>            <td>${c['attributes']['inventarnummer'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_lubis_aufnahmedatum')}</td><td>${datum or '-'}</td></tr>
<tr><td class="cell-left">${_('tt_lubis_Filmart')}</td><td>${c['attributes']['filmart'] or '-'}</td></tr>

% if preview_url != "" and image_width != None:
<tr>
  <td class="cell-left">${_('tt_lubis_Quickview')}</td>
  <td>
    <a href="${viewer_url}" target="_blank"><img src="${preview_url}" alt="quickview"></a>
  </td>
</tr>
% else:
<tr>
  <td class="cell-left">${_('tt_lubis_Quickview')}</td>
  <td>${_('tt_lubis_noQuickview')}</td>
</tr>
% endif
% endif
</%def>


<%def name="extended_info(c, lang)">
<%
# TODO: extended tooltip can be completely removed after the migration to stac
from chsdi.lib.helpers import resource_exists

c['stable_id'] = True
protocol = request.scheme
c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
topic = request.matchdict.get('map')
lang = request.lang

aerialimages_data_host = request.registry.settings['aerialimages_data_host']
tileUrlBasePath = aerialimages_data_host + '/tiles'
preview_url = determinePreviewUrl(tileUrlBasePath, c['featureId'])

filename = c['attributes']['filename'] or '-'
filesize_mb = c['attributes']['filesize_mb'] or '-'

datum = date_to_str(c['attributes']['flugdatum'])
image_rotation = 0
firma = '-'
wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
image_width = wh[1]
image_height = wh[0]
params = (
    image_width,
    image_height,
    _('tt_lubis_ebkey'),
    c['featureId'],
    firma,
    c['layerBodId'],
    lang,
    image_rotation)
viewer_url = get_viewer_url(request, params)

dataPath = 'ch.swisstopo.lubis-terrestrische_aufnahmen/'
dataGeoAdminHost = request.registry.settings['datageoadminhost']
pdf = None
url_pdf = dataGeoAdminHost + "/" + dataPath + "pdf/" + c['attributes']['base_uuid'] + '.pdf'
pdf = resource_exists(url_pdf)

url_smapshot= "https://smapshot.heig-vd.ch/map/?imageId={}".format(c['attributes']['smapshot_id'])

isStac = c['featureId'].startswith('lubis-terrestrische_aufnahmen')
%>
<title>${_('tt_lubis_ebkey')}: ${c['featureId']}</title>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr><th class="cell-left">${_('tt_lubis_ebkey')}</th>                   <td>${c['attributes']['image_number'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_inventarnummer')}</th>          <td>${c['attributes']['inventarnummer'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_lubis_aufnahmedatum')}</th>           <td>${datum or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.operate_name')}</th>      <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.station')}</th>      <td>${c['attributes']['station'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_x')}</th>      <td>${c['attributes']['x'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_y')}</th>      <td>${c['attributes']['y'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_Filmart')}</th>                 <td>${c['attributes']['filmart'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.lubis-luftbilder_schraegaufnahmen.tt_lubis_schraegaufnahmen_medium_format')}</th>                 <td>${c['attributes']['medium_format'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_filesize')}</th>                 <td>${c['attributes']['filesize_mb'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_bildpfad')}</th>         <td>${filename or '-'}</td></tr>
    <tr><th class="cell-left">${_('link')}</th>
        <td>
% if pdf:
    <a href="${url_pdf}" target="_blank">${_('ch.swisstopo.lubis-terrestrische_aufnahmen.expertenlink')} - pdf</a>
% else:
    -
% endif
        </td>
    </tr>
    <tr><th class="cell-left">${_('link')} smapshot</th>         <td><a href="${url_smapshot}" target="_blank">${_('link')} smapshot</a></td></tr>
  </table>
% if not isStac:
  <br>
<div class="chsdi-map-container table-with-border">
 <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic,'&bgLayer=ch.swisstopo.pixelkarte-grau'))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
</div>
  <br>
% if preview_url != "" and image_width != None:
  <div class="chsdi-map-container table-with-border" >
    <div id="lubismap"></div>
  </div>
% endif
  <br>
  <script type="text/javascript">
    function init() {
% if preview_url != "" and image_width != None:
     ${lubis_map.init_map(c['featureId'], image_width, image_height, image_rotation, 'lubismap', aerialimages_data_host)}
%endif
    }
  </script>
% endif
</body>
</%def>


<%def name="extended_resources(c, lang)">
  <script type="text/javascript" src="${h.get_loaderjs_url(request, '3.18.2')}"></script>
</%def>
