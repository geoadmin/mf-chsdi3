# -*- coding: utf-8 -*-

<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
  c['stable_id'] = True
  street_key = 'strname1'
  url_pdf = '/https/www.housing-stat.ch/regbl/resources/public/geb_public/%s?lang=%s' % (str(c['attributes']['egid']), lang)
  lang = lang if lang in ('fr', 'it', 'rm') else 'de'
  topic = request.matchdict.get('map')
  route_url_test = "%s?lang=%s&download_url=%s" % (h.make_agnostic(request.route_url('extendedHtmlPopup', map=topic, layerId=c['layerBodId'], featureId=str(c['featureId']))), lang, url_pdf)
  if 'strname_de' in c['attributes']:
    if c['attributes']['strname_%s' % lang]:
      street_key = 'strname_%s' % lang
%>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.egid')}</td>       <td>${c['attributes']['egid'] or '-'}</td></tr>
    % if c['attributes']['strname1'] <> '':
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.strname1')}</td>    <td>${c['attributes'][street_key]}</td></tr>
    % else:
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.strname1')}</td>    <td>${c['attributes']['deinr'] or '-'}</td></tr>
    % endif
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.deinr')}</td>         <td>${c['attributes']['deinr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.plz4')}</td>        <td>${c['attributes']['plz4'] or '-'}</td></tr>
    <tr><td class="cell-left">PLZ6</td><td>${c['attributes']['plz6'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.plzname')}</td>        <td>${c['attributes']['plzname'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfs.gebaeude_wohnungs_register.gdename')}</td>   <td>${c['attributes']['gdename'] or '-'}</td></tr>
    <tr><td class="cell-left">PDF</td>   <td><a href="${route_url_test}">Link</a></td></tr>
    <tr><td class="cell-left">${_('bfsnr')}</td>      <td>${c['attributes']['gdenr'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    import requests
    request = context.get('request')
    stage = 'dev' if  request.registry.settings['geodata_staging'] == 'test' else request.registry.settings['geodata_staging']
    download_url = 'https://service-proxy.%s.bgdi.ch%s' %(stage, context.get('request').params.get('download_url'))
%>

<body>
  <style>
    html body * {
       visibility: hidden;
    }

    div#pdf_download * {
      visibility: visible;
    }
  </style>

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

        $.ajax("${download_url}", { type: "HEAD"}).done(
        function (data, textStatus, jqXHR) {
          if (jqXHR.status == 200) {
            // wait 1s before opening the pdf
            setTimeout(function(){
              window.open("${download_url}", '_self');
            }, 1000);
            stopPolling();
          }
        });
        next();
      }, 1000);
    })();
  });
</script>


<div id="pdf_download">
    <p>${_('ch.swisstopo-vd.amtliche-vermessung.nopdf')}${context.get('request').params} </p
  </div>
</body>

</%def>

<%def name="extended_resources(c, lang)">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</%def>

