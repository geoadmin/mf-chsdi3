# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>
<%namespace name="partials" file="cadastralwebmap.include.mako"/>

<%def name="table_body(c, lang)">
<style>
    .${c['htmlpopup_class']} table tr:nth-last-child(1) {
        display: none;
    }
</style>

<%
  import requests
  from gatilegrid import getTileGrid
  from chsdi.models.vector import get_scale
  from chsdi.lib.validation.identify import IdentifyServiceValidation
  from chsdi.lib.helpers import shift_to
  request = context.get('request')
  protocol = request.scheme
  fallbackLang = 'fr' if request.lang in ('fr', 'it') else 'de'
  
  class CadastralWebMapParams(IdentifyServiceValidation):
      def __init__(self, request):
          self.srid = request.params.get('sr', '21781')
          grid = getTileGrid(self.srid)()
          defaultExtent = ','.join(map(str, grid.extent))
          defaultImageDisplay = '400,600,96'
          self.mapExtent = request.params.get('mapExtent', defaultExtent)
          self.imageDisplay = request.params.get('imageDisplay', defaultImageDisplay)
          self.coord = request.params.get('coord')
  
  params = CadastralWebMapParams(request)
  c['scale']  = get_scale(params.imageDisplay, params.mapExtent)
  topic = request.matchdict.get('map')
  baseUrl = request.registry.settings['api_url']
  

  if params.srid == 2056:
      c['bboxlv95'] =  list(params.mapExtent.bounds)
      c['bboxlv03'] =  shift_to(c['bboxlv95'], 21781)
      defaultCoordLv95 = [(c['bboxlv95'][0] + c['bboxlv95'][2]) / 2,
                          (c['bboxlv95'][1] + c['bboxlv95'][3]) / 2]

      c['clickCoordLv95'] = [float(a) for a in params.coord.split(',')] if params.coord else defaultCoordLv95
      c['clickCoordLv03'] = shift_to(c['clickCoordLv95'], 21781)
  else:
      c['bboxlv03'] =  list(params.mapExtent.bounds)
      c['bboxlv95'] =  shift_to(c['bboxlv03'], 2056)

      defaultCoordLv03 = [(c['bboxlv03'][0] + c['bboxlv03'][2]) / 2,
                          (c['bboxlv03'][1] + c['bboxlv03'][3]) / 2]
      c['clickCoordLv03'] = [float(a) for a in params.coord.split(',')] if params.coord else defaultCoordLv03
      c['clickCoordLv95'] = shift_to(c['clickCoordLv03'], 2056)

  pdf_url = "%s://geodata01.admin.ch/order/jPqrueQazrt/av_pdf.igs?pos=%s/%s" % (protocol, c['clickCoordLv03'][0] , c['clickCoordLv03'][1])
  shp_url = "%s://%s/ch.swisstopo-vd.amtliche-vermessung/DM01AVCH24D/SHP/%s/%s.zip" % (protocol, request.registry.settings['datageoadminhost'], c['attributes']['ak'],c['attributes']['bfsnr'])
  itf_url = "%s://%s/ch.swisstopo-vd.amtliche-vermessung/DM01AVCH24D/ITF/%s/%s.zip" % (protocol, request.registry.settings['datageoadminhost'], c['attributes']['ak'],c['attributes']['bfsnr'])
%>

${partials.table_body_cadastral(c, lang, fallbackLang)}

<tr>
    <td class="cell-left">${h.translate('ch.swisstopo-vd.amtliche-vermessung.pdf', lang)}</td><td>
        <a href="${h.make_agnostic(request.route_url('extendedHtmlPopup', map=topic, layerId=c['layerBodId'], featureId=str(c['featureId'])))}?lang=${lang}&download_url=${pdf_url}" target="_blank">
            PDF</a>
    </td>
</tr>
<tr>
    <td class="cell-left">${h.translate('ch.swisstopo-vd.amtliche-vermessung.shape', lang)}</td><td>
% if requests.head(shp_url, headers={'User-Agent': 'mf-geoadmin/python'}).status_code == 200:
        <a href="${shp_url}" target="_blank">
            SHP</a>
% else:
        ${h.translate('ch.swisstopo-vd.amtliche-vermessung.noshape', lang)}
% endif
    </td>
</tr>
<tr>
    <td class="cell-left">${h.translate('ch.swisstopo-vd.amtliche-vermessung.itf', lang)}</td><td>
% if requests.head(itf_url, headers={'User-Agent': 'mf-geoadmin/python'}).status_code == 200:
        <a href="${itf_url}" target="_blank">
            ITF</a>
% else:
        ${h.translate('ch.swisstopo-vd.amtliche-vermessung.noitf', lang)}
% endif
    </td>
</tr>

</%def>


<%def name="extended_info(c, lang)">

<%
    import requests
    request = context.get('request')
    protocol = request.scheme
    download_url = context.get('request').params.get('download_url')
    pdf = False
    try:
        # For some reason, the new SSL certificate can't be verified. So we do
        # without verification
        r = requests.get(download_url, verify = False)
        download_url = h.make_agnostic(r.text.strip())
        if r.status_code == 200:
            pdf = True
    except:
        pass

%>

<title>${c['fullName']}</title>
<body>
    <style>
        html body * {
            visibility: hidden;
        }

        div#pdf_download * {
            visibility: visible;
        }

    </style>

% if pdf:
<script>
    $(document).ready(function() {
        var maxLoops = 60;
        var counter = 0;
        var t;

        function stopPolling() {
            clearTimeout(t);
        }

        $('#pdf_download').html('<p>${h.translate('ch.swisstopo-vd.amtliche-vermessung.waitpdf', lang)}<br/><br/><img src="${h.versioned(request.static_url("chsdi:static/images/loading.gif"))}" width="40px" />');
        (function next() {
            t = setTimeout(function() {
                if (counter++ > maxLoops) {
                    $('#pdf_download').html("<p>${h.translate('ch.swisstopo-vd.amtliche-vermessung.nopdf', lang)}");
                    return;
                }
                jQuery.ajax("${download_url}", { type: "HEAD"}).done(
                function (data, textStatus, jqXHR) {
                    if (jqXHR.status == 200) {
                        // wait 1s before opening the pdf
                        setTimeout(function(){
                            window.open("${download_url}", '_self');
                        }, 1000);
                        stopPolling();
                    }
                }
                );
                next();
            }, 1000);
        })();
    });
</script>

% endif

<div id="pdf_download">
    <p>${h.translate('ch.swisstopo-vd.amtliche-vermessung.nopdf', lang)}
</div>
</body>

</%def>

<%def name="extended_resources(c, lang)">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</%def>
