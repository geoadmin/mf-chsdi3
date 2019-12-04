# -*- coding: utf-8 -*-

import requests

from pyramid.paster import get_app

app = get_app('development.ini')


try:
    api_url = "http:" + app.registry.settings['api_url']
except KeyError:
    api_url = 'http://api3.geo.admin.ch'


def test_getcap_21781():
    resp = requests.get(api_url + '/1.0.0/WMTSCapabilities.xml?lang=de', headers={'User-Agent': 'mf-geoadmin/python'})

    words = ['Alpenkonvention', 'Schweiz', 'Verkehrswege ', 'Flachmoor']
    for w in words:
        assert w in resp.text, w


def test_getcap_de():
    resp = requests.get(api_url + '/1.0.0/WMTSCapabilities.EPSG.4326.xml?lang=de', headers={'User-Agent': 'mf-geoadmin/python'})

    words = ['Alpenkonvention', 'Schweiz', 'Verkehrswege ', 'Flachmoor']
    for w in words:
        assert w in resp.text, w


def test_getcap_fr():
    resp = requests.get(api_url + '/1.0.0/WMTSCapabilities.EPSG.4326.xml?lang=fr', headers={'User-Agent': 'mf-geoadmin/python'})

    words = ['Convention', 'Suisse', 'voies', u'marécage']
    for w in words:
        assert w in resp.text, w
