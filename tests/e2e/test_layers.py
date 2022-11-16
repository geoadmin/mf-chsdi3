import os
from contextlib import contextmanager
from unittest import SkipTest

from chsdi.models import models_from_bodid
from chsdi.models.bod import LayersConfig
from chsdi.models.grid import get_grid_spec
from pyramid.paster import get_app
from sqlalchemy import distinct
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import func
from sqlalchemy.types import BigInteger
from tests.integration import s3_tests
from webtest import TestApp


class LayersChecker(object):

    def __enter__(self):
        def num(s):
            if s.isdigit():
                return int(s)
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
            gridSpec = None
            if s3_tests:
                gridSpec = get_grid_spec(layer)
            if gridSpec is None and layer not in self.emptyGeoTables:
                models = models_from_bodid(layer)
                if not s3_tests and models is None:
                    raise SkipTest("Skip Layer, no model found for layer <{}>".format(layer))
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



    def checkPrimaryKeyColumnTypeMapping(self, layerId, featureId, model, primaryKeyColumn):
        schema = 'public' if 'schema' not in model.__table_args__ else model.__table_args__['schema']
        if featureId is None:
            print("No feature was found in table {} for layer {}".format(schema + '.' + model.__tablename__, layerId))
        else:
            pythonType = primaryKeyColumn.type.python_type if not isinstance(primaryKeyColumn.type, BigInteger) else (int, int)
            assert isinstance(featureId, pythonType), 'Expected %s; Got: %s; For layer %s and GeoTable %s' % (
                pythonType, type(featureId), layerId, schema + '.' + model.__tablename__)

def test_all_ids_mapping():
    with LayersChecker() as lc:
        for layerId, featureId, model, primaryKeyColumn in lc.ilayersAllModels():
            yield lc.checkPrimaryKeyColumnTypeMapping, layerId, featureId, model, primaryKeyColumn

