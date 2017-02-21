# -*- coding: utf-8 -*-

from chsdi.tests.integration import TestsBase


class TestFeedback(TestsBase):

    def test_feedback(self):
        self.testapp.post('/feedback', status=200)
