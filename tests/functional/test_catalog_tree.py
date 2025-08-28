# -*- coding: utf-8 -*-

import unittest
from chsdi.views.catalog import tree_data
import networkx as nx


class TestCatalogTree(unittest.TestCase):

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
        meta = {457: {
            'category': 'cat72',
            'staging': 'prod',
                        'selectedOpen': False,
                        'label': 'Grundlagen und Planung',
                        'topic': 'ech',
                        'orderKey': 1,
                        'parentId': 15006,
                        'id': 457
        },
            458: {
            'category': 'cat73',
            'staging': 'prod',
                        'selectedOpen': False,
                        'label': 'Basiskarten',
                        'topic': 'ech',
                        'orderKey': 1,
                        'parentId': 457,
                        'id': 458},
            491: {
            'category': 'cat76',
            'staging': 'prod',
                        'selectedOpen': False,
                        'label': 'Ortsangaben, Referenzsysteme',
                        'topic': 'ech',
                        'orderKey': 4,
                        'parentId': 457,
                        'id': 491
        }
        }
        with self.assertRaises(nx.NetworkXError):
            tree_data(G, 15006, {'children': 'children', 'id': 'children'}, meta)
