<%inherit file="base.mako"/>
<%namespace name="lubis_map" file="../luftbilder/lubis_map.mako"/>

<%!
import datetime
import urllib
from pyramid.url import route_url
import chsdi.lib.helpers as h
import markupsafe

tileUrlBasePath = 'http://aerialimages0.geo.admin.ch/tiles'

def br(text):
    return text.replace('\n', markupsafe.Markup('<br />'))

def determinePreviewUrl(ebkey):

    def getPreviewImageUrl(ebkey):
        return tileUrlBasePath + '/' + ebkey + '/quickview.jpg'

    def getZeroTileUrl(ebkey):
        return tileUrlBasePath + '/' + ebkey + '/0/0/0.jpg'

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
    return h.make_agnostic(route_url('luftbilder', request)) + '?' + urllib.urlencode(f)

%>

<%def name="table_body(c, lang)">
<%

lang = lang if lang in ('fr','it','en') else 'de'
c['stable_id'] = True
preview_url = determinePreviewUrl(c['featureId'])

image_rotation = 0
wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
image_width = wh[0]
image_height = wh[1]

datum = date_to_str(c['attributes']['flightdate'])
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
    <tr><td class="cell-left">${t.Translator.translate('tt_lubis_ebkey', lang)}</td>                               <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_lubis_inventarnummer', lang)}</td>                      <td>${c['attributes']['inventory_number']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('tt_lubis_Flugdatum', lang)}</td>                           <td>${datum}</td></tr>

% if preview_url != "" and image_width != None:
<tr>
  <td class="cell-left">${t.Translator.translate('tt_lubis_Quickview', lang)}</td>
  <td>
    <a href="${viewer_url}" target="_blank"><img src="${preview_url}" alt="quickview"></a>
  </td>
</tr>
% else:
<tr>
  <td class="cell-left">${t.Translator.translate('tt_lubis_Quickview', lang)}</td>
  <td>${t.Translator.translate('tt_lubis_noQuickview', lang)}</td>
</tr>
% endif

</tr>
</%def>

<%def name="extended_info(c, lang)">
<%
c['stable_id'] = True
protocol = request.scheme
c['baseUrl'] = h.make_agnostic(''.join((protocol, '://', request.registry.settings['geoadminhost'])))
topic = request.matchdict.get('map')
lang = request.lang

preview_url = determinePreviewUrl(c['featureId'])
image_rotation = 0
wh = h.imagesize_from_metafile(tileUrlBasePath, c['featureId'])
image_width = wh[0]
image_height = wh[1]
datum = date_to_str(c['attributes']['flightdate'])
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

<title>${t.Translator.translate('tt_lubis_ebkey', lang)}: ${c['featureId']}</title>

<body onload="init()">
  <table class="table-with-border kernkraftwerke-extended">
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_ebkey', lang)}</th>                               <td>${c['featureId']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_inventarnummer', lang)}</th>                      <td>${c['attributes']['inventory_number']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_Flugdatum', lang)}</th>                           <td>${datum}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_originalsize', lang)}</th>                        <td>${c['attributes']['medium_format']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_filesize_mb', lang)}</th>                         <td>${c['attributes']['filesize_mb']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_bildpfad', lang)}</th>                            <td>${c['attributes']['filename']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_schraegaufnahmen_stereo_couple', lang)}</th>      <td>${c['attributes']['stereo_couple']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_schraegaufnahmen_x', lang)}</th>                  <td>${c['attributes']['x']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_schraegaufnahmen_y', lang)}</th>                  <td>${c['attributes']['y']}</td></tr>
    <tr><th class="cell-left">${t.Translator.translate('tt_lubis_bildorder', lang)}</th>                           <td>${c['attributes']['contact'] | br } <br/>${c['attributes']['contact_email']}</td></tr>
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
     ${lubis_map.init_map(c['featureId'], image_width, image_height, image_rotation, 'lubismap')}
%endif
    }
  </script>

</body>
</%def>

<%def name="extended_resources(c, lang)">
  <script type="text/javascript" src="${h.get_loaderjs_url(request, '3.18.2')}"></script>
</%def>
