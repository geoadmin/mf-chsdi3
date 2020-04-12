# -*- coding: utf-8 -*-

import time
from random import randint
from tests.integration import TestsBase, dynamodb_tests


class TestShortenerView(TestsBase):
    def setUp(self):
        if not dynamodb_tests:
            self.skipTest("Service shortener requires access to AWS DynamoDB")
        super(TestShortenerView, self).setUp()

    # Slow down the tests, 1 read capacity unit = 1 strongly consistent read per second (max 4 KB per read)
    def tearDown(self):
        time.sleep(randint(1, 5))

    def test_shortener_toolong_url_insert_and_read(self):
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
        # DynamoDB indices cannot be larger than 2048
        self.assertTrue(len(test_url) > 2048)
        resp = self.testapp.get('/shorten.json', params={'url': test_url}, status=200)
        self.assertTrue(resp.json['shorturl'].endswith('toolong'))
        # Now read, the short hash should exist
        self.testapp.get('/shorten/toolong', status=302)

    def test_shortener_shorturl_not_exists(self):
        self.testapp.get('/shorten/blw', status=404)

    # Only geo.admin.ch url may be shortened
    def test_shortener_forbidden_link(self):
        forbidden_url = 'https://very.naughty.website.com/'
        self.testapp.get('/shorten.json', params={'url': forbidden_url}, status=400)

    def test_url_short(self):
        test_url = 'https://map.geo.admin.ch/?topic=ech&lang=en&bgLayer=ch.swisstopo.pixelkarte-farbe&layers' \
            '=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bafu.wrz-wildruhezonen_portal,' \
            'ch.swisstopo.swisstlm3d-wanderwege&layers_visibility=false,false,false,false&layers_timestamp=' \
            '18641231,,,&X=214128.92&Y=823805.99&zoom=2'
        resp = self.testapp.get('/shorten.json', params={'url': test_url}, status=200)
        shorturl = resp.json['shorturl']
        shorthash = shorturl.split('/')[-1]
        # The reverse, get the url from the short hash
        resp2  = self.testapp.get('/shorten/{}'.format(shorthash), status=301)
        back_url = resp2.headers.get('location')
        self.assertEqual(test_url, back_url)

    # Identical url should have the same hash
    def test_url_short_hash_reuse(self):
        random_url = 'https://map.geo.admin.ch?_dc={}'.format(time.time())
        resp = self.testapp.get('/shorten.json', params={'url': random_url}, status=200)
        resp2 = self.testapp.get('/shorten.json', params={'url': random_url}, status=200)
        self.assertEqual(resp.json['shorturl'], resp2.json['shorturl'])

    def test_shorten_json_example(self):
        test_url = 'http://api3.geo.admin.ch/shorten.json?url=https:%2F%2Fmf-geoadmin3.int.bgdi.ch' \
            '%2F%3FX%3D164565.22%26Y%3D620538.74%26zoom%3D2%26lang%3Den%26topic%3Dlubis%26bgLayer%3Dch.' \
            'swisstopo.pixelkarte-grau%26catalogNodes%3D1179,1180,1184,1186%26layers%3Dch.swisstopo.lubis-bildstreifen'
        self.testapp.get('/shorten.json', params={'url': test_url}, status=200)

    def test_request_host(self):
        test_url = 'http://s.geo.admin.ch/shorten/6bea6cebcd'
        self.testapp.get('/shorten.json', params={'url': test_url}, status=200)
