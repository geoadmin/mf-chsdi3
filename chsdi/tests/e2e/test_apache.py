
import requests

from pyramid.paster import get_app

app = get_app('development.ini')


try:
    api_url = "http:" + app.registry.settings['api_url']
except KeyError as e:
    api_url = 'http://api.geo.admin.ch'


def test_layersConfig():

    for lang in ('de', 'fr', 'it', 'rm', 'en'):
        resp = requests.get(api_url + '/rest/services/all/MapServer/layersConfig?lang={}'.format(lang))
        ori = resp.json()
        resp = requests.get(api_url + '/rest/services/all/MapServer/layersConfig.{}.json'.format(lang))
        static = resp.json()

        assert static == ori
