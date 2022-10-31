from tests.integration import TestsBase


class TestDoc(TestsBase):

    def test_index(self):
        r = self.testapp.get('/', status=200)
        self.assertEqual(r.content_type, 'text/html')
        self.assertIn("The GeoAdmin API allows the integration in web pages of geospatial information provided by the Swiss Confederation.", r.text)
