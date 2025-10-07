from tests.integration import TestsBase


class TestCheckerView(TestsBase):

    def test_checker(self):
        response = self.testapp.get(
            '/checker', params={'url': 'http://s.geo.admin.ch/e83c57af1'}, status=200
        )
        self.assertIn('Cache-Control', response.headers)
        self.assertEqual(
            response.headers['Cache-Control'].replace(' ', ''),
            self.app_settings['default_cache_control'].replace(' ', '')
        )

    def test_checker_dev(self):
        self.testapp.get('/checker_dev', params={'url': 'http://s.geo.admin.ch/e83c57af1'}, status=200)
