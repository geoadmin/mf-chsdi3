<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    import requests
    request = context.get('request')
    defaultCoord = ['600000', '200000']
    defaultBbox = ['600000', '200000', '650000', '250000']
    topic = request.matchdict.get('map')
    baseUrl = request.registry.settings['api_url']

    # generate getfeatureinfo request
    coord_x, coord_y = [float(x) for x in request.params['coord'].split(",")] if request.params['coord'] else defaultCoord
    bbox_xmin, bbox_ymin, bbox_xmax, bbox_ymax = [float(x) for x in request.params['mapExtent'].split(",")] if request.params['mapExtent'] else defaultBbox
    imageDisplay = [int(x) for x in request.params['imageDisplay'].split(",")]
    getfeatureinfo_x = int(((coord_x - bbox_xmin)/(bbox_xmax-bbox_xmin))*imageDisplay[0])
    getfeatureinfo_y = int(((bbox_ymax - coord_y)/(bbox_ymax-bbox_ymin))*imageDisplay[1])

    if request.lang in ['de', 'fr', 'it'] :
        query_layer = 'eq_ch_90d_%s.s10000' % request.lang
    else :
        query_layer = 'eq_ch_90d.s10000'

    url = "http://map.seismo.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/swisstopo/eventpage_ch.map&LAYERS=eq_ch_90d_de&TRANSPARENT=TRUE&FORMAT=aggpng24&ID=eq_ch_90d_de&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetFeatureInfo&STYLES=&SRS=EPSG:2056&EXCEPTIONS=application/vnd.ogc.se_xml&BBOX=%s,%s,%s,%s&X=%s&Y=%s&INFO_FORMAT=text/html&QUERY_LAYERS=%s&FEATURE_COUNT=10&WIDTH=%s&HEIGHT=%s" % (bbox_xmin, bbox_ymin, bbox_xmax, bbox_ymax, getfeatureinfo_x, getfeatureinfo_y, query_layer, imageDisplay[0], imageDisplay[1])

    # execute getfeatureinfo
    try:
        r = requests.get(url)
        response = r.content.decode('utf-8')
        # Consider any status other than 2xx as error or mapserver 200 responses with MapServer Message in body
        if not r.status_code // 100 == 2 or "MapServer Message" in r.content:
            response = "invalid service repsonse:<br/>response: {}<br/>http status: {}<br/>Url: {}".format(response, r.status_code, url)
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        response = "service is unavailable<br/>Error: {}<br/>Url: {}".format(e.__doc__, url)
%>
<style>
    .chsdi-no-print, .htmlpopup-footer, #pDebug {
      display: none;
    }
</style>

<div>
${response or '-' | n}
</div>

</%def>
