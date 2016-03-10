# -*- coding: utf-8  -*-

from chsdi.tests.integration import TestsBase
from chsdi.lib.sphinxapi import sphinxapi


class Test_SphinxApi(TestsBase):

    def _callFUT(self):
        api = sphinxapi.SphinxClient()
        return api

    def test_sphinx_api(self):
        api = self._callFUT()
        docs = ['this is my test text to be highlighted', 'this is another test text to be highlighted']
        words = 'test text'
        index = 'layers'
        opts = {'before_match': '<b>', 'after_match': '</b>', 'chunk_separator': ' ... ', 'limit': 400, 'around': 15}
        res = api.BuildExcerpts(docs, index, words, opts)
        self.assertFalse(res)

    def test_sphinx_api_query(self):
        api = self._callFUT()
        q = 'doma'
        mode = sphinxapi.SPH_MATCH_EXTENDED
        host = self.testapp.app.registry.settings['sphinxhost']
        port = 9312
        index = 'swisssearch_preview'
        filtercol = 'rank'
        filtervals = [1, 2]
        sortby = ''
        groupby = ''
        groupsort = '@rank ASC'
        limit = 1

        api.SetServer(host, port)
        api.SetWeights([100, 1])
        api.SetMatchMode(mode)
        if filtervals:
            api.SetFilter(filtercol, filtervals)
        if groupby:
            api.SetGroupBy(groupby, sphinxapi.SPH_GROUPBY_ATTR, groupsort)
        if sortby:
            api.SetSortMode(sphinxapi.SPH_SORT_EXTENDED, sortby)
        if limit:
            api.SetLimits(0, limit, max(limit, 1000))
        res = api.Query(q, index=index)
        self.assertIsInstance(res, dict)
