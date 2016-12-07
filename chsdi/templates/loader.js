# -*- coding: utf-8 -*-

<%
lang = pageargs['lang']
data = pageargs['data']
api_url = pageargs['api_url']
ignore_polyfill = pageargs['ignore_polyfill']
layersconfig = """window.GeoAdmin.getConfig  = function(){ return %s } """ % data
%>
(function() {
if (typeof window['GeoAdmin'] == 'undefined') window.GeoAdmin = {};
window.GeoAdmin.lang = "${lang}";
window.GeoAdmin.serviceUrl = "${api_url}";
${layersconfig|n}

document.write('<link rel="stylesheet" type="text/css" href="${ol_css}" />');
document.write('<link rel="stylesheet" type="text/css" href="${ga_css}" />');
if ('${ignore_polyfill}' != 'true') {
  document.write('<scr' + 'ipt type="text/javascript" src="//cdn.polyfill.io/v2/polyfill.min.js?features=fetch,requestAnimationFrame,Element.prototype.classList,URL"></scr' + 'ipt>');
}
document.write('<scr' + 'ipt type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/proj4js/2.2.1/proj4.js"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="${epsg_21781_js}"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="${epsg_2056_js}"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="${ga_js}"></scr' + 'ipt>');
})();
