from tests.integration import TestsBase


class TestRSSFeed(TestsBase):

    def test_rss(self):
        resp = self.testapp.get('/releasenotes/rss2.xml', status=200)
        self.assertTrue(resp.content_type == 'application/xml')
        rss_lxml = resp.lxml

        number_news_item = len(rss_lxml.findall(".//item"))

        # we want at least 5 news entries in the rss feed
        self.assertGreaterEqual(number_news_item, 5)
