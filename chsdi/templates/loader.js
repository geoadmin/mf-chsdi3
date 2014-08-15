# -*- coding: utf-8 -*-

<%
from chsdi.lib.helpers import versioned

lang = pageargs['lang']
mode = pageargs['mode']
data = pageargs['data'].replace('\n', '').replace('\r', '').replace(' ', '').replace('\'', '&quot;')
serviceurl = pageargs['serviceurl']

%>
(function() {
// Load css
document.write('<link rel="stylesheet" type="text/css" href="' + "${h.versioned(request.static_url('chsdi:static/css/ga.css'))}" + '" />');
// Load js
document.write('<scr' + 'ipt type="text/javascript" src="' + "${h.versioned(request.static_url('chsdi:static/js/proj4js-compressed.js'))}" + '"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="' + "${h.versioned(request.static_url('chsdi:static/js/EPSG21781.js'))}" + '"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="' + "${h.versioned(request.static_url('chsdi:static/js/EPSG2056.js'))}" + '"></scr' + 'ipt>');
% if mode == 'debug':
document.write('<scr' + 'ipt type="text/javascript" src="' + "${h.versioned(request.static_url('chsdi:static/js/ga-whitespace.js'))}" + '"></scr' + 'ipt>');
% elif mode == 'waf':
document.write('<scr' + 'ipt type="text/javascript" src="' + "${h.versioned(request.static_url('chsdi:static/js/ga-waf.js'))}" + '"></scr' + 'ipt>');
% elif mode == 'wafint':
document.write('<scr' + 'ipt type="text/javascript" src="' + "${h.versioned(request.static_url('chsdi:static/js/ga-wafint.js'))}" + '"></scr' + 'ipt>');
% else:
document.write('<scr' + 'ipt type="text/javascript" src="' + "${h.versioned(request.static_url('chsdi:static/js/ga.js'))}" + '"></scr' + 'ipt>');
% endif
// Setting language
document.write('<scr' + 'ipt type="text/javascript">ga.Lang.setCode("${lang|n}");</scr' + 'ipt>');
// Setting service Url
document.write('<scr' + 'ipt type="text/javascript">ga.setServiceUrl("${serviceurl|n}");</scr' + 'ipt>');
// Setting Configuration
document.write('<scr' + 'ipt type="text/javascript">ga.layer.setConfig(${data|n});</scr' + 'ipt>');
})();

