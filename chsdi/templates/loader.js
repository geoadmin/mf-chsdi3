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

document.write('<link rel="stylesheet" type="text/css" href="${ga_css}" />');
% if disable_polyfill=='false':
if ('${ignore_polyfill}' != 'true') {
  document.write('<scr' + 'ipt type="text/javascript" src="${polyfill_url}"></scr' + 'ipt>');
}
% endif
document.write('<scr' + 'ipt type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/proj4js/2.2.1/proj4.js"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="${epsg_21781_js}"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="${epsg_2056_js}"></scr' + 'ipt>');
document.write('<scr' + 'ipt type="text/javascript" src="${ga_js}"></scr' + 'ipt>');
})();
