<%inherit file="base.mako"/>
<%namespace name="lubis_map" file="../luftbilder/lubis_map.mako"/>

<%!
import datetime
from pyramid.url import route_url
import chsdi.lib.helpers as h
import markupsafe
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

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
    return h.make_agnostic(route_url('luftbilder', request)) + '?' + urlencode(f)

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
image_rotation = c['attributes']['rotation'] if 'rotation' in c['attributes'] else None

if image_width is None or image_height is None:
  wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
  image_width = wh[0]
  image_height = wh[1]

if image_rotation is None:
  image_rotation = 0

datum = date_to_str(c['attributes']['flugdatum'])
params = (
    image_width,
    image_height,
    _('ch.swisstopo.lubis-luftbilder-dritte-kantone.ebkey'),
    c['featureId'],
    c['attributes']['firma'],
    c['layerBodId'],
    lang,
    image_rotation)
viewer_url = get_viewer_url(request, params)
%>
<tr>
  <td class="cell-left">${_(tt_lubis_ebkey)}</td>
  <td>${c['featureId'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('tt_lubis_Flugdatum')}</td>
  <td>${datum or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('tt_lubis_Filmart')}</td>
  <td>${c['attributes']['filmart'] or '-'}</td>
</tr>

% if 'contact_image_url' in c['attributes'] and c['attributes']['contact_image_url']:
<tr>
  <td class="cell-left">${_('tt_lubis_url_canton')}</td>
  <td><a href="${c['attributes']['contact_image_url']}" target="_blank">${c['attributes']['contact_image_url']}</a></td>
</tr>
% endif

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

% if 'contact_web' in c['attributes']:
<tr>
  <th class="cell-left">${_('tt_lubis_bildorder')}</th>
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
c['stable_id'] = True
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
orientierung = '-'
if c['attributes']['orientierung']:
    orientierung = 'True'
endif

datum = date_to_str(c['attributes']['flugdatum'])
image_width =  c['attributes']['image_width'] if 'image_width' in  c['attributes'] else None
image_height = c['attributes']['image_height'] if 'image_height' in c['attributes'] else None
image_rotation = c['attributes']['rotation'] if 'rotation' in c['attributes'] else None

if image_width is None or image_height is None:
  wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
  image_width = wh[0]
  image_height = wh[1]

if image_rotation is None:
  image_rotation = 0

params = (
    image_width,
    image_height,
    _('tt_lubis_ebkey'),
    c['featureId'],
    c['attributes']['firma'],
    c['layerBodId'],
    lang,
    image_rotation)
viewer_url = get_viewer_url(request, params)
shop_url = request.registry.settings['shop_url']
%>
<title>${_('tt_lubis_ebkey')}: ${c['featureId']}</title>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr><th class="cell-left">${_('tt_lubis_ebkey')}</th>            <td>${c['featureId'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_inventarnummer')}</th>   <td>${c['attributes']['inventarnummer'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_Flugdatum')}</th>        <td>${datum or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_flughoehe')}</th>        <td>${c['attributes']['flughoehe'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_massstab')}</th>         <td>1:${c['attributes']['massstab'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_y')}</th>                <td>${c['attributes']['x'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_x')}</th>                <td>${c['attributes']['y'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_Filmart')}</th>          <td>${c['attributes']['filmart'] or '-'}</td></tr>

% if 'contact_image_url' in c['attributes'] and c['attributes']['contact_image_url']:
<tr>
  <th class="cell-left">${_('tt_lubis_url_canton')}</th>
  <td><a href="${c['attributes']['contact_image_url']}" target="_blank">${c['attributes']['contact_image_url']}</a></td>
</tr>
% endif

    <tr><th class="cell-left">${_('tt_lubis_originalsize')}</th>     <td>${c['attributes']['originalsize'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_filesize_mb')}</th>      <td>${filesize_mb or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_bildpfad')}</th>         <td>${filename or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_orthophoto')}</th>       <td>${c['attributes']['orthophoto'] or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_orientierung')}</th>     <td>${orientierung or '-'}</td></tr>
    <tr><th class="cell-left">${_('tt_lubis_rotation')}</th>         <td>${c['attributes']['rotation'] or '-'}</td></tr>
% if 'contact_web' not in c['attributes']:
  <tr class="chsdi-no-print">
    <th class="cell-left">${_('link')} Online Shop</th>
    <td><a href="https:${shop_url}/${lang}/dispatcher?layer=${c['layerBodId']}&featureid=${c['featureId']}"
    target="toposhop">Online Shop</a></td>
  </tr>
% endif
% if 'contact_web' in c['attributes']:
  <tr class="chsdi-no-print">
    <th class="cell-left">${_('tt_lubis_bildorder')}</th>
    <td>${c['attributes']['contact'] | br } <br /> ${c['attributes']['contact_email']} <br /><a href="${c['attributes']['contact_web']}" target="_blank">${c['attributes']['contact_web']}</a></td>
  </tr>
% endif
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
