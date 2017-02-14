# -*- coding: utf-8 -*-

from pyramid.view import view_config
import networkx as nx
from itertools import chain
from pyramid.httpexceptions import HTTPInternalServerError, HTTPNotFound

from chsdi.models.bod import Catalog
from chsdi.lib.validation import MapNameValidation
from chsdi.lib.filters import filter_by_geodata_staging


# Custom networkx like function
# Inspired by https://github.com/networkx/networkx/blob/master/networkx/readwrite/json_graph/tree.py#L16
def tree_data(G, root, attrs, meta):
    if G.number_of_nodes() != G.number_of_edges() + 1:
        raise TypeError("G is not a tree.")
    if not G.is_directed():
        raise TypeError("G is not directed.")

    id_ = attrs['id']
    children = attrs['children']
    if id_ == children:
        raise nx.NetworkXError('Attribute names are not unique.')

    def add_children(n, G):
        distinct_order_keys = set()
        order_key = lambda x: x['orderKey']
        label_key = lambda x: x['label'].replace(u'Ü', u'U').replace(u'Ä', u'A')
        nbrs = G[n]
        if len(nbrs) == 0:
            return []
        children_ = []
        nbrs = sorted(nbrs)
        for child in nbrs:
            d = dict(chain(G.node[child].items(), [(id_, child)]))
            d['category'] = meta[d['id']]['category']
            d['staging'] = meta[d['id']]['staging']
            d['label'] = meta[d['id']]['label']
            # only for sorting according to 'orderKey'
            if 'orderKey' in meta[d['id']]:
                d['orderKey'] = meta[d['id']]['orderKey']
            if (d['category'] == 'layer'):
                d['layerBodId'] = meta[d['id']]['layerBodId']
            else:
                d['selectedOpen'] = meta[d['id']]['selectedOpen']
            c = add_children(child, G)
            if c:
                d[children] = c
            elif d['category'] != 'layer':
                d[children] = []
            children_.append(d)
            if 'orderKey' in d:
                distinct_order_keys.add(d['orderKey'])

        if len(distinct_order_keys) > 1:
            children_ = sorted(children_, key=order_key)
        else:
            children_ = sorted(children_, key=label_key)

        for d in children_:
            d.pop('orderKey', None)
        return children_

    data = dict(chain(G.node[root].items(), [(id_, root)]))
    data[children] = add_children(root, G)
    return data


def initialize_graph(G, rows, lang):
    root_id = None
    meta = {}
    for r in rows:
        node_parent_id = getattr(r, 'parentId')
        node_id = getattr(r, 'id')
        if node_id not in meta:
            meta[node_id] = r.to_dict(lang)
        G.add_edge(node_parent_id, node_id)
        if getattr(r, 'category') == 'root':
            root_id = node_id
    if root_id is None:
        raise HTTPInternalServerError('%s is missing root_id!' % r.topic)
    return G, meta, root_id


def create_digraph(rows, lang):
    G = nx.DiGraph()
    graph, meta, root_id = initialize_graph(G, rows, lang)
    edge_list = list(nx.bfs_edges(graph, root_id))
    G = nx.DiGraph(edge_list)
    return G, meta, root_id


class CatalogService(MapNameValidation):

    def __init__(self, request):
        self.lang = request.lang
        self.mapName = request.matchdict.get('map')  # The topic
        self.hasMap(request.db, self.mapName)
        self.request = request
        self.staging = request.registry.settings['geodata_staging']

    @view_config(route_name='catalog', renderer='jsonp')
    def catalog(self):
        model = Catalog
        query = self.request.db.query(model)\
            .filter(model.topic.like('%%%s%%' % self.mapName.lower()))
        rows = filter_by_geodata_staging(query, model.staging, self.staging).all()
        if len(rows) == 0:
            raise HTTPNotFound('No catalog with id %s is available' % self.mapName)

        G, meta, root_id = create_digraph(rows, self.lang)

        if len(rows) != len(G.nodes()):
            raise HTTPInternalServerError('Catalog tree for topic %s has unconnected leaves' % self.mapName)
        data = tree_data(G, root_id, {'children': 'children', 'id': 'id'}, meta)
        data['category'] = meta[root_id]['category']
        data['staging'] = meta[root_id]['staging']
        data = {'results': {'root': data}}
        return data
