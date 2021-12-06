# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Numeric, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['kogis']


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
    __table_args__ = ({'schema': 'fida', 'autoload': False})
    __template__ = 'templates/htmlpopup/fixpunkte_fida.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-lfp1'
    __label__ = 'id'
    id = Column('pointid', Unicode, primary_key=True)
    punktname = Column('punktname', Unicode)
    nbident = Column('nbident', Unicode)
    status = Column('status', Unicode)
    nummer = Column('nummer', Unicode)
    n95 = Column('n95', Numeric)
    e95 = Column('e95', Numeric)
    h02 = Column('h02', Numeric)
    proto_url = Column('proto_url', Unicode)
    zugang = Column('zugang', Unicode)
    ordnung = Column('ordnung', Unicode)
    l_gen_lv95 = Column('l_gen_lv95', Numeric)
    h_gen_lv95 = Column('h_gen_lv95', Numeric)
    l_zuv_lv95 = Column('l_zuv_lv95', Unicode)
    h_zuv_lv95 = Column('l_zuv_lv95', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-lfp1', FixpunkteLfp1)


class FixpunkteLfp2(Base, Vector):
    __tablename__ = 'punkt_lage_lfp2'
    __table_args__ = ({'schema': 'fpds', 'autoload': False})
    __template__ = 'templates/htmlpopup/fixpunkte.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-lfp2'
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
