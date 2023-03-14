<%namespace name="zeitreise_map" file="zeitreihen_map.mako"/>

<%
  from pyramid.url import route_url
  import requests

  c = context
  topic = 'ech'
  request = c.get('request')
  params = c.get('params')
  release_year = c.get('release_year')
  center = c.get('center')
  lang = params.lang
  layerBodId = params.layerId
  bildnummer = c.get('bildnummer')
  title = request.translate(layerBodId)
  pageTitle = _(c.get('title')) + ': ' + bildnummer
  title += ': ' + pageTitle
  loaderUrl = h.make_agnostic(route_url('ga_api', request))

  if c.get('title') == 'kartenwerk_lk25':
      zoomlevel = 8
  elif c.get('title') == 'kartenwerk_lk50':
      zoomlevel = 7
  else:
      zoomlevel = 6

  if c.get('width') is None or c.get('height') is None:
      wh = h.imagesize_from_metafile(tileUrlBasePath, bildnummer)
      width = c.get('width') or wh[0]
      height = c.get('height') or wh[1]
  else:
      width = c.get('width')
      height = c.get('height')

  geoadminUrl = "//%s/?layers=%s&zoom=%s&Y=%s&X=%s&time=%s" % (
      request.registry.settings['geoadminhost'], layerBodId, zoomlevel, center[0], center[1], release_year)

  hist_maps_data_host = request.registry.settings.get('hist_maps_data_host')
%>

<!DOCTYPE html>
<html>
  <head>
    <link rel="apple-touch-icon" sizes="76x76" href="${request.static_url('chsdi:static/images/touch-icon-bund-76x76.png')}"/>
    <link rel="apple-touch-icon" sizes="120x120" href="${request.static_url('chsdi:static/images/touch-icon-bund-120x120.png')}"/>
    <link rel="apple-touch-icon" sizes="152x152" href="${request.static_url('chsdi:static/images/touch-icon-bund-152x152.png')}"/>
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
        text-align: center;
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
      #zeitreihenmap {
        width: 100%;
        height: 100%;
        font-size: 16px;
      }
      @media print { /* Used by Chrome */
        #zeitreihenmap, .wrapper {
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
    <link rel="shortcut icon" type="image/x-icon" href="${request.static_url('chsdi:static/images/favicon.ico')}">
  </head>
  <body onload="init()">
    <div class="header">
      <div class="pull-left">${title}</div>
      <a class="pull-right" href="${geoadminUrl}" target="_blank">${_('link to geoportal')}</a>
    </div>
    <div class="wrapper">
      <div id="zeitreihenmap"></div>
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
    </div>
    <script type="text/javascript" src="${loaderUrl}"></script>
    <script type="text/javascript">
      function init() {
        ${zeitreise_map.init_map(c.get('bildnummer'), width, height, c.get('rotation'), 'zeitreihenmap', hist_maps_data_host)}

        // FF/IE
        if ('onbeforeprint' in window) {
          var element = document.getElementById('zeitreihenmap');
          window.onbeforeprint = function() {
            var size = zeitreihenMap.getSize();
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
              zeitreihenMap.updateSize();
            } else {
              window.setTimeout(function(){zeitreihenMap.updateSize()}, 500);
            }
          });
        }

        //function from here: https://developer.mozilla.org/en-US/docs/Web/API/window.location
        var queryParameter = function(sVar) {
            return decodeURI(window.location.search.replace(new
                                RegExp("^(?:.*[&\\?]" + encodeURI(sVar).replace(/[\.\+\*]/g, "\\$&") +
                                "(?:\\=([^&]*))?)?.*$", "i"), "$1"));
        }

        var view = zeitreihenMap.getView();
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

      }
    </script>
  </body>
</html>
