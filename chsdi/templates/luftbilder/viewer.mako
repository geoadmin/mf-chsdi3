<%namespace name="lubis_map" file="lubis_map.mako"/>

<%
  from pyramid.url import route_url
  from urllib2 import urlopen
  from json import loads

  c = context
  topic = 'luftbilder'
  request = c.get('request')
  baseUrl = '//' + c.get('baseUrl')
  layerBodId = c.get('layer')
  featureId = c.get('bildnummer')
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
        bottom: 50px;
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
      .controls{
        margin-left: 10px;
      }
      .percent{
        margin-left: 10px;
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
        height: 95%;
        font-size: 16px;
      }
      #reset {
        margin-left: 10px;
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
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </head>
  <body onload="init()">
    <div class="header">${title}</div>
    <div class="wrapper">
    <div id="lubismap"></div>
    <table class="controls" style="border-collapse: separate; border-spacing: 20px;" >
       <tr>
         <td>${_('image_contrast')}</td>
         <td>
          <button id="minus-button" class="btn btn-secondary btn-sm" style="border-radius: 50%"><i class="fa fa-minus"></i></button>
         </td>
         <td><input id="contrast" type="range" min="0" max="200" value="100"/></td>
         <td>
          <button id="plus-button"class="btn btn-secondary btn-sm" style="border-radius: 50%"><i class="fa fa-plus"></i></button>
         </td>
         <td id="contrastOut" class="percent">100%</td>
         <td><button id="reset" class="btn btn-secondary btn-sm">Reset</button></td>
       </tr>
    </table>
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

        var contrastSlider = document.getElementById("contrast");
        var contrastOut = document.getElementById("contrastOut");
        var resetbutton = document.getElementById("reset");
        var minusbutton = document.getElementById("minus-button");
        var plusbutton = document.getElementById("plus-button");

        setSliderListeners();

        var equalizedValues = undefined;
        var mean = undefined;

        function getPixelList(data){
          var pixel_list = [];
          for (var i=0; i<(data.length);i+=4){
            if (data[i+3]!=0){
              var pixel = [data[i], data[i+1], data[i+2], data[i+3]];
              pixel_list.push(pixel);
            }
          }
          return pixel_list;
        }

        function allZero(data){
          for (var key in data){
            if (data[key] != 0) return false
          }
          return true
        }

        // computes normalized histogram
        function getHistogramProperties(pixels){
          var histogram = {};
          var equalizedHistogram = {};
          var number_pixels = pixels.length;
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
            histogram[i] = histogram[i] / number_pixels;
            sum += histogram[i];
            equalizedHistogram[i] = sum;
            mean_luminance += histogram[i]*i;
          }
          return [equalizedHistogram, mean_luminance];
        }

        lubisMap.on('postrender', function(event){
          var canvas = document.getElementsByTagName('canvas')[0];
          var context = canvas.getContext('2d');
          var imageData = context.getImageData(0,0, canvas.width, canvas.height).data;
          // to prevent that recomputed every time map rendered
          if (!allZero(imageData) && !mean) {
            var pixel_list = getPixelList(imageData);
            var histogramProperties = getHistogramProperties(pixel_list);
            equalizedValues = histogramProperties[0];
            mean = histogramProperties[1];
          }
        });

        raster.on('beforeoperations', function(event) {
          var data = event.data;
          data["contrast"] = Number(contrastSlider.value);
          data["equalizedValues"] = equalizedValues;
          data["mean"] = mean;
        });

        function onSliderChange() {
          contrastOut.innerHTML = contrastSlider.value + "%";
          raster.changed();
        }

        function onReset(){
          contrastSlider.value = 100;
          contrastOut.innerHTML = "100%";
          raster.changed();
        }

        function moreContrast(){
          contrastSlider.value = parseInt(contrastSlider.value) + 5;
          contrastOut.innerHTML = contrastSlider.value + "%";
          raster.changed();
        }

        function lessContrast(){
          contrastSlider.value = parseInt(contrastSlider.value) - 5;
          contrastOut.innerHTML = contrastSlider.value + "%";
          raster.changed();
        }

       function setSliderListeners() {
          contrastSlider.addEventListener("change", onSliderChange);
          resetbutton.addEventListener("click", onReset);
          plusbutton.addEventListener("click", moreContrast);
          minusbutton.addEventListener("click", lessContrast);
        }
      }
   </script>
  </body>
</html>
