<%namespace name="lubis_map" file="lubis_map.mako"/>

<%
  from pyramid.url import route_url
  try:
      from urllib2 import urlopen
  except ImportError:
      from urllib.request import urlopen
  from json import loads

  c = context
  topic = 'luftbilder'
  request = c.get('request')
  baseUrl = '//' + c.get('baseUrl')
  layerBodId = c.get('layer')
  featureId = c.get('bildnummer')
  contrast = 'true' if c.get('contrast')=='true' else 'false'
  displayLink = True
  ## This is a HACK to ensure backward compatibility
  if not layerBodId.startswith('ch.'):
      templateURL = 'http://' + request.registry.settings['host'] + request.route_path('search', map=topic, _query={'type': 'featuresearch',
          'features': 'ch.swisstopo.lubis-luftbilder_schwarzweiss,ch.swisstopo.lubis-luftbilder_farbe,ch.swisstopo.lubis-luftbilder-dritte-firmen,ch.swisstopo.lubis-luftbilder-dritte-kantone,ch.swisstopo.lubis-luftbilder_infrarot',
          'searchText': featureId})
      searchFile = None
      try:
          searchFile = urlopen(templateURL)
          res = loads(searchFile.read())
          layerBodId = res['results'][0]['attrs']['layer']
      except:
          displayLink = False
      finally:
          if searchFile:
              searchFile.close()
  lang = c.get('lang') if c.get('lang') is not None else 'de'
  title = request.translate(layerBodId) if c.get('datenherr') is None else request.translate(layerBodId) + ' (' + c.get('datenherr') + ')'
  pageTitle = c.get('title') + ': ' + featureId
  title += ': ' + pageTitle
  loaderUrl = h.make_agnostic(route_url('ga_api', request))
%>

<!DOCTYPE html>
<html>
  <head>
    <link rel="apple-touch-icon" sizes="76x76" href="${h.versioned(request.static_url('chsdi:static/images/touch-icon-bund-76x76.png'))}"/>
    <link rel="apple-touch-icon" sizes="120x120" href="${h.versioned(request.static_url('chsdi:static/images/touch-icon-bund-120x120.png'))}"/>
    <link rel="apple-touch-icon" sizes="152x152" href="${h.versioned(request.static_url('chsdi:static/images/touch-icon-bund-152x152.png'))}"/>
    <!--[if !HTML5]>
    <meta http-equiv="X-UA-Compatible" content="IE=9,IE=10,IE=edge,chrome=1"/>
    <![endif]-->
    <title>${pageTitle}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="apple-mobile-web-app-capable" content="yes">

    <style>
      body {
        margin: 10px;
        color: #333;
        font-size: 12px;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      }
      .pull-right {
        float: right;
      }
      .pull-left {
        float: left;
      }
      .header {
        height: 30px;
        line-height: 30px;
        margin: 10px 0px;
        font-size: 14px;
        font-weight: bold;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        background-color:#e9e9e9;
      }
      .wrapper {
        position: absolute;
        top: 60px;
        right: 10px;
        bottom: 65px;
        left: 10px;
        border: 1px solid #EFEFEF;
      }
      .footer {
        position: absolute;
        right: 0px;
        bottom: 0px;
        left: 0px;
        height: 30px;
        margin: 10px 0px;
        text-align:center;
      }
      .btn {
        display: inline-block;
        margin-bottom: 0;
        font-weight: normal;
        text-align: center;
        vertical-align: middle;
        -ms-touch-action: manipulation;
        touch-action: manipulation;
        cursor: pointer;
        background-image: none;
        border: 1px solid transparent;
        white-space: nowrap;
        padding: 6px 12px;
        font-size: 14px;
        line-height: 1.42857143;
        border-radius: 4px;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }
      .btn-sm {
        padding: 5px 10px;
        font-size: 12px;
        line-height: 1.5;
        border-radius: 3px;
      }
      .btn-secondary {
        color: #fff;
        background-color: #6c757d;
        border-color: #6c757d;
      }
      .button{
        width:150px;
        position: absolute;
        right: 0px;
        bottom: 0px;
        left: 50%;
        height: 30px;
        margin: 10px 0px;
        text-align:center;
        z-index:10;
      }
      .footer a {
        padding: 0px 10px;
      }
      #messagectrl {
        display: inline-block;
      }
      .link-red {
        color: red;
      }
      #lubismap {
        width: 100%;
        height: 100%;
        font-size: 16px;
      }
      @media print { /* Used by Chrome */
        #lubismap, .wrapper {
          width: 650px;
          height: 650px;
        }
        .footer a {
          display: none;
        }
      }
      @media screen and (max-width: 635px) {
        #messagectrl {
          display: none!important;
        }
      }

    </style>
    <link rel="shortcut icon" type="image/x-icon" href="${h.versioned(request.static_url('chsdi:static/images/favicon.ico'))}">
  </head>
  <body onload="init()">
    <div class="header">${title}</div>
    <div class="wrapper">
      <div id="lubismap">
        <button id="contrast_activate" class="button btn btn-secondary btn-sm d-block">${_('image_contrast_activate')}</button>
      </div>
    </div>
    <div class="footer">
      <a class="pull-left" href="${_('disclaimer url')}" target="_blank">Copyright</a>
      <div id="messagectrl"></div>
      <script>
        if ( !/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
          if (navigator.platform.substr(0,3) == 'Mac') {
            document.getElementById("messagectrl").innerHTML = "${_('rotation key apple')}";
          } else {
            document.getElementById("messagectrl").innerHTML = "${_('rotation key')}";
          }
        }
      </script>
  % if displayLink:
      <div class="pull-right">
        <a class="link-red" href="${''.join((baseUrl, '?', layerBodId, '=', str(featureId), '&lang=', lang, '&topic=', topic))}" target="new">${_('Link to object')}</a>
      </div>
  % endif
    </div>
    <script type="text/javascript" src="${loaderUrl}?version=3.18.2"></script>
    <script type="text/javascript">
      function init() {
        ${lubis_map.init_map(c.get('bildnummer'), c.get('width'), c.get('height'), c.get('rotation'), 'lubismap')}

        // FF/IE
        if ('onbeforeprint' in window) {
          var element = document.getElementById('lubismap');
          window.onbeforeprint = function() {
            var size = lubisMap.getSize();
            element.style.width = "650px";
            element.style.height = (650 * size[1] / size[0]) + 'px';
          };
          window.onafterprint = function() {
            element.style.width =  '100%';
            element.style.height = '100%';
          };
        }
        // Chrome
        if (window.matchMedia) {
          window.matchMedia('print').addListener(function(mql) {
            if (mql.matches) {
              lubisMap.updateSize();
            } else {
              window.setTimeout(function(){lubisMap.updateSize()}, 500);
            }
          });
        }

        //function from here: https://developer.mozilla.org/en-US/docs/Web/API/window.location
        var queryParameter = function(sVar) {
            return decodeURI(window.location.search.replace(new
                                RegExp("^(?:.*[&\\?]" + encodeURI(sVar).replace(/[\.\+\*]/g, "\\$&") +
                                "(?:\\=([^&]*))?)?.*$", "i"), "$1"));
        }

        var view = lubisMap.getView();
        //Establishing view with x/z and zoom from parameters
        var x = parseFloat(queryParameter('x'));
        var y = parseFloat(queryParameter('y'));
        var zoom = parseInt(queryParameter('zoom'), 10);
        if (!isNaN(x) && !isNaN(y)) {
          view.setCenter([x, y]);
        }
        if (!isNaN(zoom)) {
          view.setZoom(zoom);
        }

        //taken from angularj
        var lowercase = function(s) {
          return s.toLowerCase();
        };
        var boxee = /Boxee/i.test((window.navigator || {}).userAgent);
        var android = parseInt((/android (\d+)/.exec(lowercase((window.navigator || {}).userAgent)) || [])[1], 10);
        var hasHistory = !!(window.history && window.history.pushState && !(android < 4) && !boxee);

        //function from here: http://stackoverflow.com/questions/5999118/add-or-update-query-string-parameter
        var updateQueryStringParameter = function(uri, key, value) {
          var re = new RegExp("([?|&])" + key + "=.*?(&|#|$)", "i");
          if (uri.match(re)) {
            return uri.replace(re, '$1' + key + "=" + value + '$2');
          } else {
            var hash =  '';
            var separator = uri.indexOf('?') !== -1 ? "&" : "?";
            if( uri.indexOf('#') !== -1 ){
                hash = uri.replace(/.*#/, '#');
                uri = uri.replace(/#.*/, '');
            }
            return uri + separator + key + "=" + value + hash;
          }
        }


        var updateUrl = function() {
          if (!hasHistory || document.fullscreenElement ||
              document.msFullscreenElement ||
              document.mozFullScreen ||
              document.webkitIsFullScreen) {
            return;
          }
          var center = view.getCenter();
          var zoom = view.getZoom();
          if (center && zoom !== undefined &&
              !isNaN(zoom) && !isNaN(center[0]) &&
              !isNaN(center[1])) {
            var x = center[0].toFixed(2);
            var y = center[1].toFixed(2);
            var rotation = parseInt(view.getRotation() * 180 / Math.PI) % 360;

            var newHref = updateQueryStringParameter(window.location.href, 'x', x);
            newHref = updateQueryStringParameter(newHref, 'y', y);
            newHref = updateQueryStringParameter(newHref, 'zoom', zoom);
            newHref = updateQueryStringParameter(newHref, 'rotation', rotation);
            window.history.replaceState(null, '', newHref);
          }
        };

        var debounce = function(fnc) {
          var debounceTimeout = undefined;
          return function() {
            if (debounceTimeout) {
              clearTimeout(debounceTimeout);
            }
            debounceTimeout = setTimeout(function() {
              fnc();
              debounceTimeout = undefined;
            }, 500);
          };
        };

        view.on('propertychange', debounce(updateUrl));
        updateUrl();

        var contrastButtonActivate = document.getElementById("contrast_activate");

        setButtonListener();

        var equalizedValues = undefined;
        var mean = undefined;

        function isBlack(pixel){
          return pixel[0]==255 && pixel[1]==255 && pixel[2]==255
        }

        function isWhite(pixel){
          return pixel[0]==0 && pixel[1]==0 && pixel[2]==0
        }

       function getPixelList(data){
          var pixelList = [];
          for (var i=0; i<(data.length);i+=4){
            //data-.slice() doesnt work for E11
            pixel_values = [data[i], data[i+1], data[i+2], data[i+3]];
            if (pixel_values[3]!=0 && !(isBlack(pixel_values) || isWhite(pixel_values))){
              var pixel = [pixel_values[0], pixel_values[1], pixel_values[2], pixel_values[3]];
              pixelList.push(pixel);
            }
          }
          return pixelList;
        }

        function allZero(data){
          for (var i = 0; i < data.length; i += 4){
            if (data[i] != 0) return false
          }
          return true
        }

        // computes normalized histogram
        function getHistogramProperties(pixels){
          var histogram = {};
          var equalizedHistogram = {};
          var numberPixels = pixels.length;
          var sum = 0;
          var mean_luminance = 0;

          //initialize histogram
          for (var i = 0; i < 101; i++){
            histogram[i] = 0;
          }

          for (var p in pixels){
            // convert to hcl
            var pix = pixels[p];
            var hcl = rgb2hcl(pix);
            // get luminance values
            var l = parseInt(hcl[2]);
            // augment count
            histogram[l] = histogram[l] + 1;
          }

          //normalization of histogram + compute equalized Values and Mean
          for (var i in histogram){
            histogram[i] = histogram[i] / numberPixels;
            sum += histogram[i];
            equalizedHistogram[i] = sum;
            mean_luminance += histogram[i]*i;
          }
          return [equalizedHistogram, mean_luminance];
        }

        lubisMap.on('postrender', function(event){
          if (mean) {
            return;
          }
          var canvas = document.getElementsByTagName('canvas')[0];
          var context = canvas.getContext('2d');
          var imageData = context.getImageData(0,0, canvas.width, canvas.height).data;
          // to prevent that recomputed every time map rendered
          if (!allZero(imageData) && !mean) {
            var pixelList = getPixelList(imageData);
            var histogramProperties = getHistogramProperties(pixelList);
            equalizedValues = histogramProperties[0];
            mean = histogramProperties[1];
          }
        });

        raster.on('beforeoperations', function(event) {
          var data = event.data;
          data["equalizedValues"] = equalizedValues;
          data["mean"] = mean;
        });

        function onButtonChange() {
          if (contrastLayer.getVisible() == true){
            contrastLayer.setVisible(false);
            contrastButtonActivate.innerHTML = "${_('image_contrast_activate')}";
            setContrastPermalink('false')
          } else{
            contrastLayer.setVisible(true);
            contrastButtonActivate.innerHTML = "${_('image_contrast_deactivate')}";
            setContrastPermalink('true')
          }
        }
        var contrast = ${contrast};
        if (contrast) {
          onButtonChange();
        }
        function setButtonListener() {
          contrastButtonActivate.addEventListener("click", onButtonChange);
        }

        function setContrastPermalink(state){
          var newHref = updateQueryStringParameter(window.location.href, 'contrast', state);
          window.history.replaceState(null, '', newHref);
        }
      }
   </script>
  </body>
</html>
