# -*- coding: utf-8 -*-

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from chsdi.models.bod import Catalog
from chsdi.lib.validation import MapNameValidation
from chsdi.lib.sqlalchemy_customs import remove_accents
from chsdi.lib.filters import filter_by_geodata_staging
from chsdi.lib.helpers import get_debug_headerlist


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
            .filter(model.topic.ilike('%%%s%%' % self.mapName))\
            .order_by(model.depth)\
            .order_by(model.orderKey)\
            .order_by(remove_accents(model.get_name_from_lang(self.lang)))
        rows = filter_by_geodata_staging(query, model.staging, self.staging).all()
        if len(rows) == 0:
            raise HTTPNotFound('No catalog with id %s is available' % self.mapName)

        self.request.response.headerlist.extend(get_debug_headerlist(
                self.request.registry.settings
        ))
        return {'results': self.tree(rows)}

    def tree(self, rows=[]):
        nodes_all = []  # index equal depth
        nodes_depth = []
        current_depth = 0

        def getListIndexFromPath(list_nodes, category):
            for i, node in enumerate(list_nodes):
                if 'category' in node:
                    if node['category'] == category:
                        return i
            return None

        def cleanNode(node):
            # Remove useless info
            node.pop('path', None)
            node.pop('depth', None)
            node.pop('topic', None)
            node.pop('orderKey', None)
            node.pop('parentId', None)
            if node['category'] == 'layer':
                node.pop('selectedOpen', None)
            return node

        nodes_final = {}

        for row in rows:
            depth = row.depth

            if current_depth == depth:
                node = row.to_dict(self.lang)
                if node['category'] != 'layer':
                    node['children'] = []
                nodes_depth.append(node)
            else:
                nodes_all.append(nodes_depth)

                nodes_depth = []
                current_depth = depth  # e.g. +1

                node = row.to_dict(self.lang)
                if node['category'] != 'layer':
                    node['children'] = []
                nodes_depth.append(node)

        # Append the last list
        nodes_all.append(nodes_depth)

        # At this point nodes are classified by hierachical level
        # The children property must contain an array of nodes
        for i in range(0, len(nodes_all)):
            for node in nodes_all[i]:
                if 'path' in node:
                    path = node['path'].split('/')
                    if len(path) > 0:
                        root = path[0]
                else:
                    return nodes_final
                node = cleanNode(node)
                if i == 0:
                    nodes_final[root] = node
                elif i == 1:
                    nodes_final[root]['children'].append(node)
                elif i == 2:
                    if len(path) >= 1:
                        idx = getListIndexFromPath(nodes_final[path[0]]['children'], path[1])
                        if idx is not None:
                            try:
                                nodes_final[root]['children'][idx]['children'].append(node)
                            except:
                                pass
                elif i == 3:
                    if len(path) >= 2:
                        idx_1 = getListIndexFromPath(nodes_final[path[0]]['children'], path[1])
                        idx_2 = getListIndexFromPath(nodes_final[path[0]]['children'][idx_1]['children'], path[2])
                        if idx_1 is not None and idx_2 is not None:
                            try:
                                nodes_final[root]['children'][idx_1]['children'][idx_2]['children'].append(node)
                            except:
                                pass
                elif i == 4:
                    if len(path) >= 3:
                        idx_1 = getListIndexFromPath(nodes_final[path[0]]['children'], path[1])
                        idx_2 = getListIndexFromPath(nodes_final[path[0]]['children'][idx_1]['children'], path[2])
                        idx_3 = getListIndexFromPath(nodes_final[path[0]]['children'][idx_1]['children'][idx_2]['children'], path[3])
                        if idx_1 is not None and idx_2 is not None and idx_3 is not None:
                            try:
                                nodes_final[root]['children'][idx_1]['children'][idx_2]['children'][idx_3]['children'].append(node)
                            except:
                                pass

        return nodes_final
