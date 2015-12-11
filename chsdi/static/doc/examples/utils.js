
var WMTS = {'mf-chsdi3.dev.bgdi.ch': '//wmts20.dev.bgdi.ch',
            'mf-chsdi3.int.bgdi.ch': '//wmts20.int.bgdi.ch',
            'api3.geo.admin.ch': '//wmts10.geo.admin.ch'
            }
function getWMTSSource() {
    var hostname = location.host;
    var hostnames = Object.keys(WMTS);
    if (hostnames.indexOf(hostname) > -1) {
        return  WMTS[hostname];
    } else {
        return WMTS['api3.geo.admin.ch'];
    }
}
