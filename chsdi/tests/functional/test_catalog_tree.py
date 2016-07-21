# -*- coding: utf-8 -*-

import unittest
from chsdi.views.catalog import tree_data
import networkx as nx


class Test_CatalogTree(unittest.TestCase):

    def test_not_tree(self):
        G = nx.DiGraph()
        edge_list = [(1, 2), (1, 3), (3, 4), (5, 7)]
        G = nx.DiGraph(edge_list)
        meta = {1: {'id': 1}, 2: {'id': 2}, 3: {'id': 3}, 4: {'id': 4}, 5: {'id': 5}, 7: {'id': 7}}
        with self.assertRaises(TypeError):
            tree_data(G, 1, {'children': 'children', 'id': 'id'}, meta)

    def test_not_directed_tree(self):
        G = nx.Graph()
        edge_list = [(1, 2), (3, 1)]
        G = nx.Graph(edge_list)
        meta = {2: {'id': 2}, 1: {'id': 1}, 3: {'id': 3}}
        with self.assertRaises(TypeError):
            tree_data(G, 1, {'children': 'children', 'id': 'id'}, meta)

    def test_tree_data_attribute_names(self):
        G = nx.DiGraph()
        edge_list = [(15006, 457), (457, 458), (457, 491)]
        G = nx.DiGraph(edge_list)
        meta = {457: {u'category': u'cat72', u'staging': u'prod', 'selectedOpen': False, 'label': u'Grundlagen und Planung', u'topic': u'ech', u'depth': 1, 'orderKey': 1, 'parentId': 15006, u'path': u'root/cat72', 'id': 457}, 458: {u'category': u'cat73', u'staging': u'prod', 'selectedOpen': False, 'label': u'Basiskarten', u'topic': u'ech', u'depth': 2, 'orderKey': 1, 'parentId': 457, u'path': u'root/cat72/cat73', 'id': 458}, 491: {u'category': u'cat76', u'staging': u'prod', 'selectedOpen': False, 'label': u'Ortsangaben, Referenzsysteme', u'topic': u'ech', u'depth': 2, 'orderKey': 4, 'parentId': 457, u'path': u'root/cat72/cat76', 'id': 491}}
        with self.assertRaises(nx.NetworkXError):
            tree_data(G, 15006, {'children': 'children', 'id': 'children'}, meta)
