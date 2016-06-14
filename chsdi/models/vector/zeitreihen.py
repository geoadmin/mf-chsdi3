# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer
from sqlalchemy.types import Numeric, Unicode
from sqlalchemy.dialects import postgresql

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D


Base = bases['zeitreihen']


class Zeitreihen_15(Base, Vector):
    __tablename__ = 'tooltip_15'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 10.05
    __maxresolution__ = 500005
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Text)
    produkt = Column('produkt', Text)
    kbnum = Column('kbnum', Text)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Text)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Text)
    the_geom = Column(Geometry2D)


class Zeitreihen_20(Base, Vector):
    __tablename__ = 'tooltip_20'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 5.05
    __maxresolution__ = 10.05
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Text)
    produkt = Column('produkt', Text)
    kbnum = Column('kbnum', Text)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Text)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Text)
    the_geom = Column(Geometry2D)


class Zeitreihen_21(Base, Vector):
    __tablename__ = 'tooltip_21'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 2.55
    __maxresolution__ = 5.05
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Text)
    produkt = Column('produkt', Text)
    kbnum = Column('kbnum', Text)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Text)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Text)
    the_geom = Column(Geometry2D)


class Zeitreihen_22(Base, Vector):
    __tablename__ = 'tooltip_22'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 0
    __maxresolution__ = 2.55
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Text)
    produkt = Column('produkt', Text)
    kbnum = Column('kbnum', Text)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Text)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Text)
    the_geom = Column(Geometry2D)


class DufourErst(Base, Vector):
    __tablename__ = 'view_dufour_erstausgabe'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/dufour_erst.mako'
    __bodId__ = 'ch.swisstopo.hiks-dufour'
    __label__ = 'datenstand'
    id = Column('tilenumber', Unicode, primary_key=True)
    kbbez = Column('kbbez', Text)
    datenstand = Column('datenstand', Integer)
    bv_nummer = Column('bv_nummer', Text)
    the_geom = Column(Geometry2D)


class SiegfriedErst(Base, Vector):
    __tablename__ = 'view_siegfried_erstausgabe'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/siegfried_erst.mako'
    __bodId__ = 'ch.swisstopo.hiks-siegfried'
    __label__ = 'datenstand'
    id = Column('tilenumber', Unicode, primary_key=True)
    kbbez = Column('kbbez', Text)
    datenstand = Column('datenstand', Numeric)
    bv_nummer = Column('bv_nummer', Text)
    the_geom = Column(Geometry2D)


register('ch.swisstopo.hiks-siegfried', SiegfriedErst)
register('ch.swisstopo.hiks-dufour', DufourErst)
register('ch.swisstopo.zeitreihen', Zeitreihen_15)
register('ch.swisstopo.zeitreihen', Zeitreihen_20)
register('ch.swisstopo.zeitreihen', Zeitreihen_21)
register('ch.swisstopo.zeitreihen', Zeitreihen_22)
