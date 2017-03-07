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

    if request.lang == ('de') :
        query_layer = 'eq_ch_90d_de'
    elif request.lang == ('fr') :
        query_layer = 'eq_ch_90d_fr'
    elif request.lang == ('it') :
        query_layer = 'eq_ch_90d_it'
    else :
        query_layer = 'eq_ch_90d'

    url = "http://map.seismo.ethz.ch/cgi-bin/mapserv?map=/var/www/mapfile/sed/earthquakes_ch.map&LAYERS=eq_ch_90d_de&TRANSPARENT=TRUE&FORMAT=aggpng24&ID=eq_ch_90d_de&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetFeatureInfo&STYLES=&SRS=EPSG:21781&EXCEPTIONS=application/vnd.ogc.se_xml&BBOX=%s,%s,%s,%s&X=%s&Y=%s&INFO_FORMAT=text/html&QUERY_LAYERS=%s&FEATURE_COUNT=10&WIDTH=%s&HEIGHT=%s" % (bbox_xmin, bbox_ymin, bbox_xmax, bbox_ymax, getfeatureinfo_x, getfeatureinfo_y, query_layer, imageDisplay[0], imageDisplay[1])

    # execute getfeatureinfo
    r = requests.get(url)
%>
<style>
    .chsdi-no-print, .htmlpopup-footer, #pDebug {
      display: none;
    }
</style>

<div>
${r.content.decode('utf-8') or '-' | n}
</div>

</%def>
