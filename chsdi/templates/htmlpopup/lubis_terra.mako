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

tileUrlBasePath = 'http://aerialimages0.geo.admin.ch/tiles'

def determinePreviewUrl(ebkey):

    def getPreviewImageUrl(ebkey):
        return tileUrlBasePath + '/' + ebkey + '/quickview.jpg'

    def getZeroTileUrl(ebkey):
        return tileUrlBasePath + '/' + ebkey + '/1/0/0.jpg'

    headers = {'Referer': 'http://admin.ch'}
    url = getPreviewImageUrl(ebkey)
    #testing these 2 url could be done more python like
    if not h.resource_exists(url, headers):
         url = getZeroTileUrl(ebkey)

    return h.make_agnostic(url)

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
    return h.make_agnostic(route_url('luftbilder', request)) + '?' + urllib.urlencode(f)

%>

<%def name="table_body(c, lang)">
<%

tt_lubis_ebkey = c['layerBodId'] + '.' + 'id'
lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True

toposhopscan = 'nein'
if c['attributes']['filename'] :
    toposhopscan = 'ja'
preview_url = determinePreviewUrl(c['featureId'])

image_width = c['attributes']['image_width'] if 'image_width' in  c['attributes'] else None
image_height = c['attributes']['image_height'] if 'image_height' in c['attributes'] else None
image_rotation = 0
firma = '-'

if image_width is None or image_height is None:
  wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
  image_width = wh[1]
  image_height = wh[0]


datum = date_to_str(c['attributes']['flugdatum'])
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
<tr>
  <td class="cell-left">${mod_translate.Translator.translate(tt_lubis_ebkey, lang)}</td>
  <td>${c['attributes']['image_number'] or '-'}</td>
</tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('tt_lubis_inventarnummer', lang)}</td>          <td>${c['attributes']['inventarnummer'] or '-'}</td></tr>
<tr>
  <td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_lubis_aufnahmedatum', lang)}</td>
  <td>${datum or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${mod_translate.Translator.translate('tt_lubis_Filmart', lang)}</td>
  <td>${c['attributes']['filmart'] or '-'}</td>
</tr>

% if 'contact_image_url' in c['attributes'] and c['attributes']['contact_image_url']:
<tr>
  <td class="cell-left">${mod_translate.Translator.translate('tt_lubis_url_canton', lang)}</td>
  <td><a href="${c['attributes']['contact_image_url']}" target="_blank">${c['attributes']['contact_image_url']}</a></td>
</tr>
% endif

% if preview_url != "" and image_width != None:
<tr>
  <td class="cell-left">${mod_translate.Translator.translate('tt_lubis_Quickview', lang)}</td>
  <td>
    <a href="${viewer_url}" target="_blank"><img src="${preview_url}" alt="quickview"></a>
  </td>
</tr>
% else:
<tr>
  <td class="cell-left">${mod_translate.Translator.translate('tt_lubis_Quickview', lang)}</td>
  <td>${mod_translate.Translator.translate('tt_lubis_noQuickview', lang)}</td>
</tr>
% endif

% if 'contact_web' in c['attributes']:
<tr>
  <th class="cell-left">${mod_translate.Translator.translate('tt_lubis_bildorder', lang)}</th>
  <td>
    ${c['attributes']['contact'] | br }
    <br/>
    ${c['attributes']['contact_email']}
    <br/>

% if  c['attributes']['contact_web'] != '-':
    <a href="${c['attributes']['contact_web']}" target="_blank">
% endif

    ${c['attributes']['contact_web']}

% if  c['attributes']['contact_web'] != '-':
    </a>
% endif

  </td>
</tr>
% endif
</%def>


<%def name="extended_info(c, lang)">
<%
from chsdi.lib.helpers import resource_exists

c['stable_id'] = True
if c['layerBodId'] == 'ch.swisstopo.lubis-luftbilder_farbe':
    imgtype = 1
elif c['layerBodId'] == 'ch.swisstopo.lubis-luftbilder_infrarot':
    imgtype = 2
else:
    imgtype = 0
endif
protocol = request.scheme
c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
topic = request.matchdict.get('map')
lang = request.lang

preview_url = determinePreviewUrl(c['featureId'])

filesize_mb = '-'
toposhopscan = 'nein'
filename = c['attributes']['filename']
if filename:
    filesize_mb = c['attributes']['filesize_mb']
    toposhopscan = 'ja'
endif

datum = date_to_str(c['attributes']['flugdatum'])
image_width =  c['attributes']['image_width'] if 'image_width' in  c['attributes'] else None
image_height = c['attributes']['image_height'] if 'image_height' in c['attributes'] else None
image_rotation = 0
firma = '-'

if image_width is None or image_height is None:
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
shop_url = request.registry.settings['shop_url']

dataPath = 'ch.swisstopo.lubis-terrestrische_aufnahmen/'
dataGeoAdminHost = request.registry.settings['datageoadminhost']
pdf = None

url_pdf = "https://" + dataGeoAdminHost + "/" + dataPath + "pdf/" + c['attributes']['base_uuid'] + '.pdf'
pdf = resource_exists(url_pdf)

url_smapshot= "https://smapshot.heig-vd.ch/map/?imageId={}".format(c['attributes']['smapshot_id'])
%>
<title>${mod_translate.Translator.translate('tt_lubis_ebkey', lang)}: ${c['featureId']}</title>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr><th class="cell-left">${mod_translate.Translator.translate('tt_lubis_ebkey', lang)}</th>                   <td>${c['attributes']['image_number'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('tt_lubis_inventarnummer', lang)}</th>          <td>${c['attributes']['inventarnummer'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_lubis_aufnahmedatum', lang)}</th>           <td>${datum or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.lubis-terrestrische_aufnahmen.operate_name', lang)}</th>      <td>${c['attributes']['ort'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.lubis-terrestrische_aufnahmen.station', lang)}</th>      <td>${c['attributes']['station'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('tt_lubis_schraegaufnahmen_x', lang)}</th>      <td>${c['attributes']['x'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('tt_lubis_schraegaufnahmen_y', lang)}</th>      <td>${c['attributes']['y'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('tt_lubis_Filmart', lang)}</th>                 <td>${c['attributes']['filmart'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.lubis-luftbilder_schraegaufnahmen.tt_lubis_schraegaufnahmen_medium_format', lang)}</th>                 <td>${c['attributes']['medium_format'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.lubis-terrestrische_aufnahmen.tt_filesize', lang)}</th>                 <td>${c['attributes']['filesize_mb'] or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('tt_lubis_bildpfad', lang)}</th>         <td>${filename or '-'}</td></tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('link', lang)}</th>
        <td>
% if pdf:
    <a href="${url_pdf}" target="_blank">${mod_translate.Translator.translate('ch.swisstopo.lubis-terrestrische_aufnahmen.expertenlink', lang)} - pdf</a>
% else:
    -
% endif
        </td>
    </tr>
    <tr><th class="cell-left">${mod_translate.Translator.translate('link', lang)} smapshot</th>         <td><a href="${url_smapshot}" target="_blank">${mod_translate.Translator.translate('link', lang)} smapshot</a></td></tr>
  <tr class="chsdi-no-print">
    <th class="cell-left">${mod_translate.Translator.translate('link', lang)} Online Shop</th>
    <td><a href="https:${shop_url}/${lang}/dispatcher?layer=${c['layerBodId']}&featureid=${c['featureId']}"
    target="toposhop">Online Shop</a></td>
  </tr>
  </table>
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
     ${lubis_map.init_map(c['featureId'], image_width, image_height, image_rotation, 'lubismap')}
%endif
    }
  </script>

</body>
</%def>


<%def name="extended_resources(c, lang)">
  <script type="text/javascript" src="${h.get_loaderjs_url(request, '3.18.2')}"></script>
</%def>
