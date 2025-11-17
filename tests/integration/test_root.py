from tests.integration import TestsBase


class TestRootView(TestsBase):

    def test_root(self):
        self.testapp.get('/', None, status=301)
