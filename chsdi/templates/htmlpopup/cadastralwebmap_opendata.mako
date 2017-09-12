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
  from chsdi.models.vector import get_scale
  from chsdi.lib.validation.identify import IdentifyServiceValidation
  request = context.get('request')
  protocol = request.scheme
  defaultExtent = '42000,30000,350000,900000'
  defaultImageDisplay = '400,600,96'
  defaultCoord = ['600000', '200000']
  fallbackLang = 'fr' if request.lang in ('fr', 'it') else 'de'
  class CadastralWebMapParams(IdentifyServiceValidation):
      def __init__(self, request):
          self.mapExtent = request.params.get('mapExtent', defaultExtent)
          self.imageDisplay = request.params.get('imageDisplay', defaultImageDisplay)
  params = CadastralWebMapParams(request)
  c['bbox'] = params.mapExtent.bounds
  c['bboxlv95'] = [2000000 + c['bbox'][0], 1000000 + c['bbox'][1], 2000000 + c['bbox'][2], 1000000 + c['bbox'][3]]
  c['scale']  = get_scale(params.imageDisplay, params.mapExtent)
  topic = request.matchdict.get('map')
  baseUrl = request.registry.settings['api_url']
  coord = request.params.get('coord').split(',') if request.params.get('coord') else defaultCoord
  lat = coord[0]
  lon = coord[1]
  pdf_url = "%s://geodata01.admin.ch/order/jPqrueQazrt/av_pdf.igs?pos=%s/%s" % (protocol, lat, lon)
  shp_url = "%s://%s/ch.swisstopo-vd.amtliche-vermessung/DM01AVCH24D/SHP/%s/%s.zip" % (protocol, request.registry.settings['datageoadminhost'], c['attributes']['ak'],c['attributes']['bfsnr'])
  itf_url = "%s://%s/ch.swisstopo-vd.amtliche-vermessung/DM01AVCH24D/ITF/%s/%s.zip" % (protocol, request.registry.settings['datageoadminhost'], c['attributes']['ak'],c['attributes']['bfsnr'])
  defaultCoord = [(c['bbox'][0]+c['bbox'][2])/2, (c['bbox'][1]+c['bbox'][3])/2]
  clickCoord = request.params.get('coord').split(',') if request.params.get('coord') else defaultCoord
%>

${partials.table_body_cadastral(c, lang, fallbackLang, clickCoord)}

<tr>
    <td class="cell-left">${_('ch.swisstopo-vd.amtliche-vermessung.pdf')}</td><td>
        <a href="${h.make_agnostic(request.route_url('extendedHtmlPopup', map=topic, layerId=c['layerBodId'], featureId=str(c['featureId'])))}?lang=${lang}&download_url=${pdf_url}" target="_blank">
            PDF</a>
    </td>
</tr>
<tr>
    <td class="cell-left">${_('ch.swisstopo-vd.amtliche-vermessung.shape')}</td><td>
% if requests.head(shp_url, headers={'User-Agent': 'mf-geoadmin/python'}).status_code == 200:
        <a href="${shp_url}" target="_blank">
            SHP</a>
% else:
        ${_('ch.swisstopo-vd.amtliche-vermessung.noshape')}
% endif
    </td>
</tr>
<tr>
    <td class="cell-left">${_('ch.swisstopo-vd.amtliche-vermessung.itf')}</td><td>
% if requests.head(itf_url, headers={'User-Agent': 'mf-geoadmin/python'}).status_code == 200:
        <a href="${itf_url}" target="_blank">
            ITF</a>
% else:
        ${_('ch.swisstopo-vd.amtliche-vermessung.noitf')}
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

        $('#pdf_download').html('<p>${_("ch.swisstopo-vd.amtliche-vermessung.waitpdf")}<br/><br/><img src="${h.versioned(request.static_url("chsdi:static/images/loading.gif"))}" width="40px" />');
        (function next() {
            t = setTimeout(function() {
                if (counter++ > maxLoops) {
                    $('#pdf_download').html("<p>${_('ch.swisstopo-vd.amtliche-vermessung.nopdf')}");
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
    <p>${_('ch.swisstopo-vd.amtliche-vermessung.nopdf')}
</div>
</body>

</%def>

<%def name="extended_resources(c, lang)">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</%def>
