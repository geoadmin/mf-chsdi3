# -*- coding: utf-8 -*-


import json
from tests.integration import TestsBase


GL_STYLE = {
    'version': 8,
    'name': 'ch.swisstopo.leichte-basiskarte.vt',
    'center': [9, 46],
    'zoom': 6.5,
    'bearing': 0,
    'pitch': 5.5,
    'sources': {
        'ch.swissnames3d': {
            'url': 'https://swissnames3d.json',
            'type': 'vector'
        },
        'ch.swisstopo.swissalti3d-reliefschattierung': {
            'url': 'https://swissalti3d.json',
            'type': 'raster'
        }
    },
    'sprite': 'https://linktosprite',
    'glyphs': 'https://linktoglyphs',
    'layers': [
        {
            'id': 'background',
            'type': 'background',
            'minzoom': 6,
            'maxzoom': 24,
            'layout': {
              'visibility': 'visible'
            },
            'paint': {
                'background-color': 'rgb(255, 255, 255)'
            }
        }
    ]
}
GL_STYLE_JSON = json.dumps(GL_STYLE)
INVALID_JSON = 'toto_est_pas_beau'


# Python2/3
def to_utf8(data):
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data


class TestGLStylesView(TestsBase):

    def setUp(self):
        super(TestGLStylesView, self).setUp()
        self.headers = {'Content-Type': 'application/json',
                        'X-SearchServer-Authorized': 'true'}
        self.headers_not_auth = {'Content-Type': 'application/json',
                        'X-SearchServer-Authorized': 'false'}
        self.headers_wrong_ctype = {'Content-Type': 'application/toto_et_zozo_et_momo',
                        'X-SearchServer-Authorized': 'true'}

    def test_create_glstyle(self):
        resp = self.testapp.post('/gl-styles', GL_STYLE_JSON, headers=self.headers, status=200)
        self.assertIn('adminId', resp.json)

    def test_glstyle_not_auth(self):
        self.testapp.post('/gl-styles', GL_STYLE_JSON, headers=self.headers_not_auth, status=403)

    def test_glstyle_invalid_content_type(self):
        self.testapp.post('/gl-styles', GL_STYLE_JSON, headers=self.headers_wrong_ctype, status=415)

    def test_invalid_json(self):
        self.testapp.post('/gl-styles', INVALID_JSON, headers=self.headers, status=415)

    def test_update_glstyle(self):
        resp = self.testapp.post('/gl-styles', GL_STYLE_JSON, headers=self.headers, status=200)
        admin_id = resp.json['adminId']

        resp = self.testapp.post('/gl-styles/%s' % admin_id, GL_STYLE_JSON, headers=self.headers, status=200)
        self.assertTrue(resp.json['status'], 'updated')
        self.assertEqual(admin_id, resp.json['adminId'])

    def test_forked_glstyle(self):
        resp = self.testapp.post('/gl-styles', GL_STYLE_JSON, headers=self.headers, status=200)
        admin_id = resp.json['adminId']
        file_id = resp.json['fileId']

        resp = self.testapp.post('/gl-styles/%s' % file_id, GL_STYLE_JSON, headers=self.headers, status=200)
        self.assertEqual(resp.json['status'], 'copied')
        self.assertNotEqual(admin_id, resp.json['adminId'])
        self.assertNotEqual(file_id, resp.json['fileId'])

    def test_delete_glstyle(self):
        resp = self.testapp.post('/gl-styles', GL_STYLE_JSON, headers=self.headers, status=200)
        admin_id = resp.json['adminId']
        file_id = resp.json['fileId']

        # delete with file_id
        resp = self.testapp.delete('/gl-styles/%s' % file_id, headers=self.headers, status=401)

        # Delete with admin_id
        resp = self.testapp.delete('/gl-styles/%s' % admin_id, headers=self.headers, status=200)
        self.assertTrue(resp.json['success'])

        resp = self.testapp.delete('/files/%s' % 'this-file-is-nothing', headers=self.headers, status=404)

    def test_update_copy_glstyle(self):
        # First request, to get ids
        resp = self.testapp.post('/gl-styles', GL_STYLE_JSON, headers=self.headers, status=200)
        admin_id = resp.json['adminId']
        file_id = resp.json['fileId']

        # get file
        resp = self.testapp.get('/gl-styles/%s' % file_id, headers=self.headers, status=200)
        orig_data = to_utf8(resp.body)
        self.assertEqual(orig_data, GL_STYLE_JSON)

        # update with file_id, should copy
        new_content = json.loads(GL_STYLE_JSON)
        new_content['zoom'] = 8
        new_content = json.dumps(new_content)

        resp = self.testapp.post('/gl-styles/%s' % file_id, new_content, headers=self.headers, status=200)
        new_admin_id = resp.json['adminId']
        new_file_id = resp.json['fileId']
        modified_content = to_utf8(resp.body)

        self.assertNotEqual(admin_id, new_admin_id)
        self.assertNotEqual(file_id, new_file_id)

        # re-get first file
        resp = self.testapp.get('/gl-styles/%s' % file_id, headers=self.headers, status=200)
        new_content = to_utf8(resp.body)

        self.assertEqual(new_content, GL_STYLE_JSON)
        self.assertNotEqual(new_content, modified_content)
