<%inherit file="base.mako"/>

<%!
import datetime
import urllib
from pyramid.url import route_url
import chsdi.lib.helpers as h
import markupsafe

tileUrlBasePath = 'http://historicalmaps.geo.admin.ch/tiles'

def determinePreviewUrl(bvnummer):

    def getPreviewImageUrl(bvnummer):
        return tileUrlBasePath + '/' + bvnummer + '/quickview.jpg'

    def getZeroTileUrl(bvnummer):
        return tileUrlBasePath + '/' + bvnummer + '/0/0/0.jpg'

    headers = {'Referer': 'http://admin.ch'}
    url = getPreviewImageUrl(bvnummer)
    if not h.resource_exists(url, headers):
        url = getZeroTileUrl(bvnummer)
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
        'layer': params[4].encode('utf8'),
        'lang': params[5],
        'release_year': params[6]
    }
    return h.make_agnostic(route_url('historicalmaps', request)) + '?' + urllib.urlencode(f)

%>

<%def name="table_body(c,lang)">
  <%
    product = c['attributes']['produkt']
    productName = 'kartenwerk_%s' % product

    image_rotation = 0

    # Get Image Preview URL and Image Size from Metafile
    preview_url = determinePreviewUrl(c['attributes']['bv_nummer'])
    wh = h.imagesize_from_metafile(tileUrlBasePath, c['attributes']['bv_nummer'])
    image_width = wh[0]
    image_height = wh[1]

    params = (
        image_width, 
        image_height, 
        productName,
        c['attributes']['bv_nummer'],
        c['layerBodId'],
        lang,
        c['attributes']['release_year'])

    viewer_url = get_viewer_url(request, params)
    c['bbox'] = request.params.get('mapExtent')
  %>
  <tr>
    <td class="cell-left">${_('kartenwerk')}</td>
    <td>${_(productName)}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('kbnum')}</td>
    <td>${c['attributes']['kbnum'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('kbbez')}</td>
    <td>${c['attributes']['kbbez'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('release_year')}</td>
    <td>${c['attributes']['release_year'] or '-'}</td></tr>
  <tr>
    <td class="cell-left">${_('blattbezeichnung')}</td>
    <td><a target="_blank" href="http://www.alexandria.ch/primo_library/libweb/action/dlSearch.do?institution=BIG&vid=ALEX&scope=default_scope&query=lsr07,contains,${c['attributes']['bv_nummer']}">${c['attributes']['kbbez'] or '-'}</a></td>
  </tr>

% if viewer_url != "" and preview_url != "" and image_width != None:
<tr>
  <td class="cell-left">${_('tt_zeitreihen_FullResView')}</td>
  <td>
    <a href="${viewer_url}" target="_blank" title="${_('tt_zeitreihen_FullResView')} - ${c['attributes']['kbbez']} - ${c['attributes']['kbnum']} - ${c['attributes']['release_year']} - ${c['attributes']['bv_nummer']}"><img src="${preview_url}" alt="${_('tt_zeitreihen_FullResView')} - ${c['attributes']['kbbez']} - ${c['attributes']['release_year']} - ${c['attributes']['bv_nummer']}"></a>
  </td>
</tr>
% else:
<tr>
  <td class="cell-left">${_('tt_zeitreihen_FullResView')}</td>
  <td>-</td>
</tr>
% endif
</%def>

