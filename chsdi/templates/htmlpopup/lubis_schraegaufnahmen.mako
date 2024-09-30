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
        return tileUrlBasePath + '/' + ebkey + '/0/0/0.jpg'

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
        return request.translate('None') + request.translate('Datenstand')

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

lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
request = context.get('request')
aerialimages_data_host = request.registry.settings['aerialimages_data_host']
tileUrlBasePath = aerialimages_data_host + '/tiles'

datum = date_to_str(c['attributes']['flightdate'])
tt_lubis_Quickview='tt_lubis_Quickview'
image_width = None

# set true if featureId comes from stac
isStac = c['featureId'].startswith('lubis-luftbilder_schraegaufnahmen')
# new feature ids start with: lubis-luftbilder
# simply create a link to the stac browser
# there is no way to open to activate the orthophoto with the link parameters
if isStac:
  dataGeoAdminHost = request.registry.settings['datageoadminhost']
  asset_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}_2056.tif"
  preview_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.jpg"
  meta_csv_url=f"{dataGeoAdminHost}/{c['layerBodId']}/{c['featureId']}/{c['featureId']}.csv"
  viewer_url=asset_url
  tt_lubis_Quickview='tt_lubis_Quickview_stac'
# legacy: old ebkeys with fullresviewer in aerialimages bucket
# this part can be removed when the migration of the aerialimages bucket to stac/data.geo.admin.ch is finished
else:
  preview_url = determinePreviewUrl(tileUrlBasePath, c['featureId'])
  image_rotation = 0
  wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
  image_width = wh[0]
  image_height = wh[1]

  params = (
      image_width,
      image_height,
      _('tt_lubis_ebkey'),
      c['featureId'],
      'swisstopo',
      c['layerBodId'],
      lang,
      image_rotation)
  viewer_url = get_viewer_url(request, params)

%>
% if isStac: # STAC Tooltips
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
% else: # OLD Tooltips with GDWH datasource
    <tr><td class="cell-left">${_('tt_lubis_ebkey')}</td>                               <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${_('tt_lubis_inventarnummer')}</td>                      <td>${c['attributes']['inventory_number']}</td></tr>
    <tr><td class="cell-left">${_('tt_lubis_Flugdatum')}</td>                           <td>${datum}</td></tr>

% if preview_url != "" and image_width != None:
<tr>
  <td class="cell-left">${_('tt_lubis_Quickview')}</td>
  <td><a href="${viewer_url}" target="_blank"><img src="${preview_url}" alt="quickview"></a></td>
</tr>
% else:
<tr>
  <td class="cell-left">${_('tt_lubis_Quickview')}</td>
  <td>${_('tt_lubis_noQuickview')}</td>
</tr>
% endif

% endif
</tr>
</%def>


<%def name="extended_info(c, lang)">
<%
# TODO: extended tooltip can be completely removed after the migration to stac
c['stable_id'] = True
protocol = request.scheme
c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
topic = request.matchdict.get('map')
lang = request.lang

datum = date_to_str(c['attributes']['flightdate'])

isStac = c['featureId'].startswith('lubis-luftbilder_schraegaufnahmen')
if not isStac:
  aerialimages_data_host = request.registry.settings['aerialimages_data_host']
  tileUrlBasePath =  aerialimages_data_host + '/tiles'
  preview_url = determinePreviewUrl(tileUrlBasePath, c['featureId'])
  image_rotation = 0
  wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
  image_width = wh[0]
  image_height = wh[1]
  params = (
      image_width,
      image_height,
      _('tt_lubis_ebkey'),
      c['featureId'],
      'swisstopo',
      c['layerBodId'],
      lang,
      image_rotation)
  viewer_url = get_viewer_url(request, params)
%>

% if isStac: # STAC Tooltips
<title>${_('tt_lubis_ebkey')}: ${c['featureId']}</title>
<body>
  <table class="table-with-border kernkraftwerke-extended">
    <tr><th class="cell-left">${_('tt_lubis_ebkey')}</th>                               <td>${c['featureId']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_Flugdatum')}</th>                           <td>${datum}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_bildpfad')}</th>                            <td>${c['attributes']['filename']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_stereo_couple')}</th>      <td>${c['attributes']['stereo_couple']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_x')}</th>                  <td>${c['attributes']['x']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_y')}</th>                  <td>${c['attributes']['y']}</td></tr>
  </table>
</body>
% else: # quickview and iframe are only activated for the old images
<title>${_('tt_lubis_ebkey')}: ${c['featureId']}</title>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr><th class="cell-left">${_('tt_lubis_ebkey')}</th>                               <td>${c['featureId']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_inventarnummer')}</th>                      <td>${c['attributes']['inventory_number']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_Flugdatum')}</th>                           <td>${datum}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_originalsize')}</th>                        <td>${c['attributes']['medium_format']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_filesize_mb')}</th>                         <td>${c['attributes']['filesize_mb']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_bildpfad')}</th>                            <td>${c['attributes']['filename']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_stereo_couple')}</th>      <td>${c['attributes']['stereo_couple']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_x')}</th>                  <td>${c['attributes']['x']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_schraegaufnahmen_y')}</th>                  <td>${c['attributes']['y']}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_bildorder')}</th>                           <td>${c['attributes']['contact'] | br } <br/>${c['attributes']['contact_email']}</td></tr>
  </table>
  <br>
<div class="chsdi-map-container table-with-border">
 <iframe src="${''.join((c['baseUrl'], '/embed.html', '?', c['layerBodId'], '=', str(c['featureId']), '&lang=', lang, '&topic=', topic,'&bgLayer=ch.swisstopo.pixelkarte-grau'))}" width='580' height='300' style="width: 100%;" frameborder='0' style='border:0'></iframe>
</div>
  <br>
% if preview_url != "" and image_width != None:
<div class="chsdi-map-container table-with-border">
    <div id="lubismap"></div>
  </div>
% endif
  <script type="text/javascript">
    function init() {
% if preview_url != "" and image_width != None:
     ${lubis_map.init_map(c['featureId'], image_width, image_height, image_rotation, 'lubismap', aerialimages_data_host)}
%endif
    }
  </script>

</body>
% endif

</%def>

<%def name="extended_resources(c, lang)">
  <script type="text/javascript" src="${h.get_loaderjs_url(request, '3.18.2')}"></script>
</%def>
