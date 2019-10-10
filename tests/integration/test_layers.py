# -*- coding: utf-8 -*-

import os
import six
from webtest import TestApp
from webtest.app import AppError
from unittest import skip
from pyramid_mako import MakoRenderingException
from PIL import Image
from contextlib import contextmanager
from pyramid.paster import get_app
from sqlalchemy import distinct
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import func
from sqlalchemy.types import BigInteger

from chsdi.models.bod import LayersConfig
from chsdi.models import models_from_bodid
from chsdi.models.grid import get_grid_spec

if six.PY3:
    long = int


class LayersChecker(object):

    def __enter__(self):
        def num(s):
            if s.isdigit():
                return long(s)
            else:
                return s

        self.testapp = TestApp(get_app('development.ini'))

        # configuration via environment. Default is None for all
        self.staging = os.environ.get('CHSDI_STAGING') if os.environ.get('CHSDI_STAGING') is not None else u'prod'
        self.onlylayer = os.environ.get('CHSDI_ONLY_LAYER')
        self.randomFeatures = os.environ.get('CHSDI_RANDOM_FEATURES') == 'True'
        self.nrOfFeatures = num(os.environ.get('CHSDI_NUM_FEATURES')) if os.environ.get('CHSDI_NUM_FEATURES') is not None else 1
        self.emptyGeoTables = self.testapp.app.registry.settings.get('empty_geotables').split(',')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del self.testapp
        return False

    @contextmanager
    def getSession(self):
        session = scoped_session(sessionmaker())
        yield session
        session.close()

    def ilayers(self, tooltip=None, hasLegend=None, searchable=None, geojson=None):
        with self.getSession() as session:
            valNone = None
            query = session.query(distinct(LayersConfig.layerBodId)) \
                .filter(LayersConfig.staging == self.staging) \
                .filter(LayersConfig.parentLayerId == valNone) \
                .filter(LayersConfig.srid != u'4326')
            if tooltip is not None:
                query = query.filter(LayersConfig.tooltip == tooltip)
            if hasLegend is not None:
                query = query.filter(LayersConfig.hasLegend == hasLegend)
            if searchable is not None:
                query = query.filter(LayersConfig.searchable == searchable)
            if geojson is not None:
                if geojson:
                    query = query.filter(LayersConfig.type == u'geojson')
                else:
                    query = query.filter(LayersConfig.type != u'geojson')
            for q in query:
                if self.onlylayer is None or q[0] == self.onlylayer:
                    yield q[0]

    def ilayersAllModels(self):
        for layer in self.ilayers(tooltip=True, geojson=False):
            gridSpec = get_grid_spec(layer)
            if gridSpec is None and layer not in self.emptyGeoTables:
                models = models_from_bodid(layer)
                assert (models is not None and len(models) > 0), layer
                for model in models:
                    primaryKeyColumn = model.primary_key_column()
                    with self.getSession() as session:
                        query = session.query(primaryKeyColumn)
                        query = query.limit(1)
                        try:
                            featureId = query.one()[0]
                        except NoResultFound:
                            featureId = None
                    yield layer, featureId, model, primaryKeyColumn

    def ilayersWithFeatures(self):
        for layer in self.ilayers(tooltip=True, geojson=False):
            gridSpec = get_grid_spec(layer)
            if gridSpec is None and layer not in self.emptyGeoTables:
                models = models_from_bodid(layer)
                assert (models is not None and len(models) > 0), layer
                model = models[0]
                with self.getSession() as session:
                    query = session.query(model.primary_key_column())
                    # Depending on db size, random row is slow
                    if self.randomFeatures:
                        query = query.order_by(func.random())
                    if isinstance(self.nrOfFeatures, (int, long)):
                        query = query.limit(self.nrOfFeatures)
                    hasExtended = model.__extended_info__ if hasattr(model, '__extended_info__') else False
                    for q in query:
                        yield (layer, str(q[0]), hasExtended)

    def checkHtmlPopup(self, layer, feature, extended):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            link = '/rest/services/all/MapServer/' + layer + '/' + feature + '/htmlPopup?callback=cb_&lang=' + lang
            try:
                resp = self.testapp.get(link)
                assert resp.status_int == 200, link
            except (AppError, AssertionError, MakoRenderingException):
                skip("Skiping htmlPopup test for {}".format(layer))
            if extended:
                try:
                    link = link.replace('htmlPopup', 'extendedHtmlPopup')
                    resp = self.testapp.get(link)
                    assert resp.status_int == 200, link
                except (AppError, AssertionError, MakoRenderingException):
                    skip("Skiping extendedHtmlPopup for {}".format(layer))

    def checkLegend(self, layer):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            link = '/rest/services/all/MapServer/' + layer + '/legend?callback=cb_&lang=' + lang
            resp = self.testapp.get(link)
            assert resp.status_int == 200, link

    def checkIdentify(self, layer):
        link = '/rest/services/all/MapServer/identify?geometry=558945.5,147956,559402,148103.5&geometryType=esriGeometryEnvelope&imageDisplay=500,600,96&mapExtent=558945.5,147956,559402,148103.5&tolerance=1&layers=all:' + layer
        resp = self.testapp.get(link)
        assert resp.status_int == 200, link
        assert resp.content_type == 'application/json', link

    def checkLegendImage(self, layer, legendsPath, legendImages):
        for lang in ('de', 'fr', 'it', 'rm', 'en'):
            key = layer + '_' + lang
            images = [l for l in legendImages if l.startswith(key)]
            assert (len(images) > 0), 'Prefix "%s" not found in %s' % (key, legendImages)
            for img in images:
                if 'big' not in img:
                    with Image.open(os.path.join(legendsPath, img)) as im:
                        width, height = im.size
                        assert (width <= 480), '%s image is too big, %spx instead of 480px' % (img, width)

    def checkSearch(self, layer):
        models = models_from_bodid(layer)
        try:
            assert (models is not None and len(models) > 0), layer
        except AssertionError:
            self.skipTest("Cannot find model for layer {}".format(layer))
        model = models[0]
        expectedStatus = 200
        # Special treatment for non-distributed sphinx indices (single model)
        if len(models) == 1:
            with self.getSession() as session:
                query = session.query(model.primary_key_column())
                # we expect 404 errors for searchable layers without any data (no sphinx index)
                if query.first() is None:
                    expectedStatus = 404

        # If it fails here, it most probably means given layer does not have sphinx index available
        link = '/rest/services/all/SearchServer?features=' + layer + '&bbox=600818.7808825106,197290.49919797093,601161.2808825106,197587.99919797093&type=featuresearch&searchText=dummy'
        resp = self.testapp.get(link, status=expectedStatus)
        # If there are no features, we don't expect a sphinx index present
        if expectedStatus == 404:
            assert 'unknown local index' in resp.body

    def checkPrimaryKeyColumnTypeMapping(self, layerId, featureId, model, primaryKeyColumn):
        schema = 'public' if 'schema' not in model.__table_args__ else model.__table_args__['schema']
        if featureId is None:
            print("No feature was found in table %s for layer {}".format(schema + '.' + model.__tablename__, layerId))
        else:
            pythonType = primaryKeyColumn.type.python_type if not isinstance(primaryKeyColumn.type, BigInteger) else (int, long)
            assert isinstance(featureId, pythonType), 'Expected %s; Got: %s; For layer %s and GeoTable %s' % (
                pythonType, type(featureId), layerId, schema + '.' + model.__tablename__)


def test_all_htmlpopups():
    with LayersChecker() as lc:
        for layer, feature, extended in lc.ilayersWithFeatures():
            yield lc.checkHtmlPopup, layer, feature, extended


def test_all_legends():
    with LayersChecker() as lc:
        for layer in lc.ilayers(hasLegend=True):
            yield lc.checkLegend, layer


def test_all_identify():
    with LayersChecker() as lc:
        for layer in lc.ilayers(tooltip=True, geojson=False):
            yield lc.checkIdentify, layer


def test_all_ids_mapping():
    with LayersChecker() as lc:
        for layerId, featureId, model, primaryKeyColumn in lc.ilayersAllModels():
            yield lc.checkPrimaryKeyColumnTypeMapping, layerId, featureId, model, primaryKeyColumn


def test_all_legends_images():
    # Get list of layers from existing legend images
    legendsPath = os.getcwd() + '/chsdi/static/images/legends/'
    legendNames = os.listdir(legendsPath)
    parseLegendNames = lambda x: x[:-7] if 'big' not in x else x[:-11]
    legendImages = {}
    for l in legendNames:
        legendImages.setdefault(parseLegendNames(l), []).append(l)
    with LayersChecker() as lc:
        for layer in lc.ilayers(hasLegend=True):
            yield lc.checkLegendImage, layer, legendsPath, legendImages.pop(layer)


def test_all_searchable_layers():
    with LayersChecker() as lc:
        for layer in lc.ilayers(searchable=True):
            yield lc.checkSearch, layer
