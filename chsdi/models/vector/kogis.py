# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Numeric, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D


Base = bases['kogis']


class Gebaeuderegister(Base, Vector):
    __tablename__ = 'view_adr'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/gebaeuderegister.mako'
    __bodId__ = 'ch.bfs.gebaeude_wohnungs_register'
    __queryable_attributes__ = ['strname1', 'deinr', 'plz4', 'plzname', 'gdename', 'egid', 'gdenr']
    # __minscale__ = 5001
    # due to https://redmine.bgdi.admin.ch/issues/3146 ltmoc  __maxscale__ = 25000
    # Composite labels
    __label__ = 'strname1'
    id = Column('egid_edid', Unicode, primary_key=True)
    egid = Column('egid', Integer)
    strname1 = Column('strname1', Unicode)
    deinr = Column('deinr', Unicode)
    plz4 = Column('plz4', Integer, nullable=False)
    plz6 = Column('plz6', Integer, nullable=False)
    plzname = Column('plzname', Unicode)
    gdename = Column('gdename', Unicode)
    gdekt = Column('gdekt', Unicode)
    dstrid = Column('dstrid', Integer)
    gkplaus = Column('gkplaus', Integer)
    gstat = Column('gstat', Integer)
    gdenr = Column('gdenr', Integer)
    ggbkr = Column('ggbkr', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfs.gebaeude_wohnungs_register', Gebaeuderegister)


class Agnes(Base, Vector):
    __tablename__ = 'agnes'
    __table_args__ = ({'schema': 'fpds', 'autoload': False})
    __template__ = 'templates/htmlpopup/agnes.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-agnes'
    __label__ = 'id'
    id = Column('no', Unicode, primary_key=True)
    url = Column('url', Unicode)
    bgdi_id = Column('bgdi_id', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-agnes', Agnes)


class FixpunkteLfp1(Base, Vector):
    __tablename__ = 'punkt_lage_lfp1'
    __table_args__ = ({'schema': 'fpds', 'autoload': False})
    __template__ = 'templates/htmlpopup/fixpunkte.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-lfp1'
    __queryable_attributes__ = ['id']
    __label__ = 'id'
    id = Column('pointid', Unicode, primary_key=True)
    punktname = Column('punktname', Unicode)
    nummer = Column('nummer', Unicode)
    status = Column('status', Unicode)
    nbident = Column('nbident', Unicode)
    x03 = Column('x03', Numeric)
    y03 = Column('y03', Numeric)
    n95 = Column('n95', Numeric)
    e95 = Column('e95', Numeric)
    h02 = Column('h02', Numeric)
    zugang = Column('zugang', Unicode)
    url = Column('url', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-lfp1', FixpunkteLfp1)


class FixpunkteLfp2(Base, Vector):
    __tablename__ = 'punkt_lage_lfp2'
    __table_args__ = ({'schema': 'fpds', 'autoload': False})
    __template__ = 'templates/htmlpopup/fixpunkte.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-lfp2'
    __queryable_attributes__ = ['id']
    __label__ = 'id'
    id = Column('pointid', Unicode, primary_key=True)
    nbident = Column('nbident', Unicode)
    punktname = Column('punktname', Unicode)
    status = Column('status', Unicode)
    nummer = Column('nummer', Unicode)
    x03 = Column('x03', Numeric)
    y03 = Column('y03', Numeric)
    n95 = Column('n95', Numeric)
    e95 = Column('e95', Numeric)
    h02 = Column('h02', Numeric)
    zugang = Column('zugang', Unicode)
    url = Column('url', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-lfp2', FixpunkteLfp2)


class FixpunkteHfp1(Base, Vector):
    __tablename__ = 'punkt_hoehe_hfp1'
    __table_args__ = ({'schema': 'fpds', 'autoload': True})
    __template__ = 'templates/htmlpopup/fixpunkte.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-hfp1'
    __queryable_attributes__ = ['id', 'bgdi_label']
    __label__ = 'id'
    id = Column('pointid', Unicode, primary_key=True)
    bgdi_label = Column('bgdi_label', Unicode)
    nbident = Column('nbident', Unicode)
    punktname = Column('punktname', Unicode)
    status = Column('status', Unicode)
    nummer = Column('nummer', Unicode)
    x03 = Column('x03', Numeric)
    y03 = Column('y03', Numeric)
    n95 = Column('n95', Numeric)
    e95 = Column('e95', Numeric)
    h02 = Column('h02', Numeric)
    zugang = Column('zugang', Unicode)
    url = Column('url', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-hfp1', FixpunkteHfp1)


class FixpunkteHfp2(Base, Vector):
    __tablename__ = 'punkt_hoehe_hfp2'
    __table_args__ = ({'schema': 'fpds', 'autoload': True})
    __template__ = 'templates/htmlpopup/fixpunkte.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-hfp2'
    __queryable_attributes__ = ['id']
    __label__ = 'id'
    id = Column('pointid', Unicode, primary_key=True)
    nbident = Column('nbident', Unicode)
    punktname = Column('punktname', Unicode)
    status = Column('status', Unicode)
    nummer = Column('nummer', Unicode)
    x03 = Column('x03', Numeric)
    y03 = Column('y03', Numeric)
    n95 = Column('n95', Numeric)
    e95 = Column('e95', Numeric)
    h02 = Column('h02', Numeric)
    zugang = Column('zugang', Unicode)
    url = Column('url', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-hfp2', FixpunkteHfp2)


# This address model is just used in the sitemap service
# It contains different attributes than the standard
# Gebaeuderegister model for the layer 'ch.bfs.gebaeude_wohnungs_register'
# This model is not registered
class SitemapGebaeuderegister(Gebaeuderegister):
    X = Column('gkody', Numeric)
    Y = Column('gkodx', Numeric)
