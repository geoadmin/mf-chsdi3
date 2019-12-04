# -*- coding: utf-8 -*-

from tests.integration import TestsBase
from chsdi.models.bod import Catalog
from sqlalchemy.orm import scoped_session, sessionmaker
from chsdi.views.catalog import create_digraph
from chsdi.lib.filters import filter_by_geodata_staging


class TestCatalogService(TestsBase):

    def test_nodes_connection(self):
        try:
            geodata_staging = self.testapp.app.registry.settings['geodata_staging']
            session = scoped_session(sessionmaker())
            topics = self.testapp.get('/rest/services', status=200)
            for t in topics.json['topics']:
                topic = t.get('id')
                query = session.query(Catalog).filter(Catalog.topic == topic)\
                    .order_by(Catalog.orderKey)
                query = filter_by_geodata_staging(query, Catalog.staging, geodata_staging)
                rows = query.all()
                if (rows):
                    graph, meta, root_id = create_digraph(rows, 'fr')
                    nodes = graph.nodes()
                    if len(nodes) != len(rows):
                        for row in rows:
                            if row.id not in nodes:
                                raise Exception('%s %s %s is unconnected leaf' % (topic, row.category, row.layerBodId))
        finally:
            if session:
                session.close()

    def test_catalog_no_params(self):
        resp = self.testapp.get('/rest/services/blw/CatalogServer', status=200)
        self.assertTrue(resp.content_type == 'application/json')
        self.assertTrue('root' in resp.json['results'])
        self.assertTrue('children' in resp.json['results']['root'])
        self.assertTrue('selectedOpen' in resp.json['results']['root']['children'][0])
        self.assertTrue('category' in resp.json['results']['root'])

    def test_catalog_with_callback(self):
        resp = self.testapp.get('/rest/services/blw/CatalogServer', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_catalog_existing_map_no_catalog(self):
        self.testapp.get('/rest/services/all/CatalogServer', status=404)

    def test_catalog_wrong_map(self):
        self.testapp.get('/rest/services/foo/CatalogServer', status=400)

    def test_catalog_ordering(self):
        resp = self.testapp.get('/rest/services/inspire/CatalogServer', params={'lang': 'en'}, status=200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertTrue('AGNES' in resp.json['results']['root']['children'][0]['children'][0]['children'][0]['label'])
        self.assertTrue('Geoid in CH1903' in resp.json['results']['root']['children'][0]['children'][0]['children'][1]['label'])

    def test_catalog_languages(self):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            link = '/rest/services/ech/CatalogServer?lang=' + lang
            resp = self.testapp.get(link)
            self.assertEqual(resp.status_int, 200, link)

    def test_layersconfig_with_callback(self):
        resp = self.testapp.get('/rest/services/blw/MapServer/layersConfig', params={'callback': 'cb_'}, status=200)
        self.assertEqual(resp.content_type, 'application/javascript')

    def test_all_catalogs(self):

        def existInList(node, l):
            found = False
            for entry in l:
                if entry.id == node.get('id'):
                    found = True
                    break

            if not found:
                print(node.get('id'))
                return False

            if 'children' in node:
                for child in node.get('children'):
                    if not existInList(child, l):
                        return False
            return True

        from chsdi.models.bod import Catalog
        from sqlalchemy.orm import scoped_session, sessionmaker
        DBSession = scoped_session(sessionmaker())
        old_staging = self.testapp.app.registry.settings['geodata_staging']
        # We fix staging for next calls to prod
        self.testapp.app.registry.settings['geodata_staging'] = u'prod'
        try:
            topics = self.testapp.get('/rest/services', status=200)
            for t in topics.json['topics']:
                topic = t.get('id')
                # Get catalog
                catalog = self.testapp.get('/rest/services/' + topic + '/CatalogServer', status=200)
                # Get flat catalog table entries
                query = DBSession.query(Catalog).filter(Catalog.topic == topic).filter(Catalog.staging == u'prod')
                entries = query.all()
                # Check if every node in the catalog is in view_catalog of db
                self.assertTrue(existInList(catalog.json['results']['root'], entries))

        finally:
            # reset staging to previous setting
            self.testapp.app.registry.settings['geodata_staging'] = old_staging
            DBSession.close()

    def test_catalogs_with_layersconfig(self):

        def existInList(node, l):
            if node.get('category') != 'layer':
                return True

            found = False
            for entry in l:
                if entry == node.get('layerBodId'):
                    found = True
                    break

            if not found:
                print(node.get('layerBodId'))
                return False

            if 'children' in node:
                for child in node.get('children'):
                    if not existInList(child, l):
                        return False
            return True

        from sqlalchemy.orm import scoped_session, sessionmaker
        DBSession = scoped_session(sessionmaker())
        old_staging = self.testapp.app.registry.settings['geodata_staging']
        # We fix staging for next calls to prod
        self.testapp.app.registry.settings['geodata_staging'] = u'prod'
        try:
            topics = self.testapp.get('/rest/services', status=200)
            for t in topics.json['topics']:
                topic = t.get('id')
                # Get catalog
                catalog = self.testapp.get('/rest/services/' + topic + '/CatalogServer', status=200)
                # Get LayersConfig for this topic
                layersconf = self.testapp.get('/rest/services/' + topic + '/MapServer/layersConfig', status=200)
                # Check if all layers of catalog are in LayersConfig
                self.assertTrue(existInList(catalog.json['results']['root'], layersconf.json), 'For Topic: ' + topic)

        finally:
            # reset staging to previous setting
            self.testapp.app.registry.settings['geodata_staging'] = old_staging
            DBSession.close()
