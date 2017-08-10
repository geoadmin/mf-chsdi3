# -*- coding: utf-8 -*-

from unittest import TestCase
from pyramid import testing
from webtest import TestApp
from gatilegrid import getTileGrid
from contextlib import contextmanager
from chsdi.models import models_from_bodid
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql.expression import func


def shift_to_lv95(string_coords):
    coords = string_coords.split(',')
    for idx, coord in enumerate(coords):
        if idx % 2:
            coords[idx] = float(coords[idx]) + 1e6
        else:
            coords[idx] = float(coords[idx]) + 2e6
    return ','.join([str(c) for c in coords])


class TestsBase(TestCase):

    def setUp(self):
        from pyramid.paster import get_app
        app = get_app('development.ini')
        self.testapp = TestApp(app)
        self.grids = {
            '21781': getTileGrid(21781),
            '2056': getTileGrid(2056)
        }

    def tearDown(self):
        testing.tearDown()
        del self.testapp
        del self.grids

    @contextmanager
    def getSession(self):
        session = scoped_session(sessionmaker())
        yield session
        session.close()

    def getRandomFeatureId(self, bodId):
        models = models_from_bodid(bodId)
        with self.getSession() as session:
            t = session.query(models[0]).limit(500).subquery('t')
            query = session.query(t).order_by(func.random()).limit(1)
            reslt = query.one()
        return reslt[0]

    def assertGeojsonFeature(self, feature, srid, hasGeometry=True):
        self.assertIn('id', feature)
        self.assertIn('properties', feature)
        self.assertNotIn('attributes', feature)
        self.assertIn('layerBodId', feature)
        self.assertIn('layerName', feature)
        if hasGeometry:
            self.assertIn('geometry', feature)
            self.assertIn('type', feature)
            self.assertIn('type', feature['geometry'])
            self.assertIn('bbox', feature)
            self.assertBBoxValidity(feature['bbox'], srid)

    def assertEsrijsonFeature(self, feature, srid, hasGeometry=True):
        self.assertIn('id', feature)
        self.assertNotIn('properties', feature)
        self.assertIn('attributes', feature)
        self.assertIn('layerBodId', feature)
        self.assertIn('layerName', feature)
        if hasGeometry:
            self.assertIn('geometry', feature)
            self.assertIn('bbox', feature)
            self.assertEqual(feature['geometry']['spatialReference']['wkid'], srid)
            self.assertBBoxValidity(feature['bbox'], srid)

    def assertBBoxValidity(self, bbox, srid):
        if srid == 21781:
            self.assertLess(bbox[0], self.grids['2056'].MINX)
            self.assertLess(bbox[1], self.grids['2056'].MINY)
        if srid == 2056:
            self.assertGreater(bbox[0], self.grids['2056'].MINX)
            self.assertGreater(bbox[1], self.grids['2056'].MINY)
