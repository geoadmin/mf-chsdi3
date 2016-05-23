# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestShortenerView(TestsBase):

    def test_shortener_toolong_url_insert(self):
        test_url = 'https://map.geo.admin.ch/?topic=ech&lang=en&bgLayer=ch.swisstopo.pixelkarte-farbe' \
            '&layers=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bafu.wrz-wildruhezonen_portal,' \
            'ch.swisstopo.swisstlm3d-wanderwege,KML%7C%7Chttps:%2F%2Fpublic.geo.admin.ch' \
            '%2F0z2auM61R1i-Q2IZTh_L1w,WMS%7C%7C2000-Watt%20Sites%7C%7Chttps:%2F%2Fwms.geo.admin.ch' \
            '%2F%7C%7Cch.bfe.energiestaedte-2000watt-areale,WMS%7C%7C2015%20rail%20noise%20emiss.%20plan,' \
            '%20night%7C%7Chttps:%2F%2Fwms.geo.admin.ch%2F%7C%7Cch.bav.laerm-emissionsplan_eisenbahn_nacht,' \
            'WMS%7C%7C2015%20rail%20noise%20emissions%20plan,%20day%7C%7Chttps:%2F%2Fwms.geo.admin.ch' \
            '%2F%7C%7Cch.bav.laerm-emissionsplan_eisenbahn_tag,WMS%7C%7C2km2%20sub%20catchment%20areas' \
            '%7C%7Chttps:%2F%2Fwms.geo.admin.ch%2F%7C%7Cch.bafu.wasser-teileinzugsgebiete_2,' \
            'WMS%7C%7C3G%20antenna%20locations%20(UMTS)%7C%7Chttps:%2F%2Fwms.geo.admin.ch' \
            '%2F%7C%7Cch.bakom.mobil-antennenstandorte-umts,WMS%7C%7C40km2%20sub%20catchment' \
            '%20areas%7C%7Chttps:%2F%2Fwms.geo.admin.ch%2F%7C%7Cch.bafu.wasser-teileinzugsgebiete_40,' \
            'WMS%7C%7C4G%20antenna%20locations%20(LTE)%7C%7Chttps:%2F%2Fwms.geo.admin.ch' \
            '%2F%7C%7Cch.bakom.mobil-antennenstandorte-lte,WMS%7C%7CAbandonment%20of%20hydropower%7C%7Chttps:' \
            '%2F%2Fwms.geo.admin.ch%2F%7C%7Cch.bfe.abgeltung-wasserkraftnutzung,' \
            'WMS%7C%7CAerial%20Images%20swisstopo%20b%2Fw%7C%7Chttps:%2F%2Fwms.geo.admin.ch' \
            '%2F%7C%7Cch.swisstopo.lubis-luftbilder_schwarzweiss,WMS%7C%7CAerial%20Images%20swisstopo' \
            '%20IR%7C%7Chttps:%2F%2Fwms.geo.admin.ch%2F%7C%7Cch.swisstopo.lubis-luftbilder_infrarot,' \
            'WMS%7C%7CAeromagnetics%7C%7Chttps:%2F%2Fwms.geo.admin.ch%2F%7C%7C' \
            'ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz,WMS%7C%7CAptitude:' \
            '%20Cropland%7C%7Chttps:%2F%2Fwms.geo.admin.ch%2F%7C%7Cch.blw.bodeneignung-kulturland,' \
            'ch.swisstopo.pixelkarte-farbe-pk1000.noscale,ch.swisstopo.pixelkarte-farbe-pk500.noscale,' \
            'ch.swisstopo.pixelkarte-farbe-pk200.noscale,ch.swisstopo.pixelkarte-farbe-pk100.noscale,' \
            'ch.swisstopo.pixelkarte-pk50.metadata&layers_timestamp=19961231,,,,,,,,,,,,,,,,,,,,,' \
            '&X=172839.76&Y=662412.05&zoom=3&time=1996&layers_opacity=0.25,1,1,0.4,1,1,1,1,1,1,1,1,1,1,1,' \
            '0.55,0.45,1,1,1,1,1&catalogNodes=457,458'
        resp = self.testapp.get('/shorten.json', params={'url': test_url}, status=200)
        self.assertTrue(resp.json['shorturl'].endswith('toolong'))

    def test_shortener_shorturl_not_exists(self):
        self.testapp.get('/shorten/blw', status=404)

    def test_shortener_moved_permanently(self):
        self.testapp.get('/shorten/6863fbb96f', status=301)

    def test_shortener_too_long_get(self):
        self.testapp.get('/shorten/toolong', status=302)

    def test_url_short(self):
        test_url = 'https://map.geo.admin.ch/?topic=ech&lang=en&bgLayer=ch.swisstopo.pixelkarte-farbe&layers' \
            '=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bafu.wrz-wildruhezonen_portal,' \
            'ch.swisstopo.swisstlm3d-wanderwege&layers_visibility=false,false,false,false&layers_timestamp=' \
            '18641231,,,&X=214128.92&Y=823805.99&zoom=2'
        self.testapp.get('/shorten.json', params={'url': test_url}, status=200)

    def test_shorten_json_example(self):
        test_url = 'http://api3.geo.admin.ch/shorten.json?url=https:%2F%2Fmf-geoadmin3.int.bgdi.ch' \
            '%2F%3FX%3D164565.22%26Y%3D620538.74%26zoom%3D2%26lang%3Den%26topic%3Dlubis%26bgLayer%3Dch.' \
            'swisstopo.pixelkarte-grau%26catalogNodes%3D1179,1180,1184,1186%26layers%3Dch.swisstopo.lubis-bildstreifen'
        self.testapp.get('/shorten.json', params={'url': test_url}, status=200)

    def test_request_host(self):
        test_url = 'http://s.geo.admin.ch/shorten/6bea6cebcd'
        self.testapp.get('/shorten.json', params={'url': test_url}, status=200)
