# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Numeric, Unicode
from sqlalchemy.dialects import postgresql

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2DLV03


Base = bases['zeitreihen']


class Zeitreihen15(Base, Vector):
    __tablename__ = 'tooltip_15'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 10.05
    __maxresolution__ = 500005
    __minscale__ = 37984.176
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Unicode)
    produkt = Column('produkt', Unicode)
    kbnum = Column('kbnum', Unicode)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Unicode)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Unicode)
    the_geom = Column(Geometry2DLV03)


class Zeitreihen20(Base, Vector):
    __tablename__ = 'tooltip_20'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 5.05
    __maxresolution__ = 10.05
    __minscale__ = 19086.576
    __maxscale__ = 37984.176
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Unicode)
    produkt = Column('produkt', Unicode)
    kbnum = Column('kbnum', Unicode)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Unicode)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Unicode)
    the_geom = Column(Geometry2DLV03)


class Zeitreihen21(Base, Vector):
    __tablename__ = 'tooltip_21'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 2.55
    __maxresolution__ = 5.05
    __minscale__ = 9637.776
    __maxscale__ = 19086.576
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Unicode)
    produkt = Column('produkt', Unicode)
    kbnum = Column('kbnum', Unicode)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Unicode)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Unicode)
    the_geom = Column(Geometry2DLV03)


class Zeitreihen22(Base, Vector):
    __tablename__ = 'tooltip_22'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/zeitreihen.mako'
    __bodId__ = 'ch.swisstopo.zeitreihen'
    __minresolution__ = 0
    __maxresolution__ = 2.55
    __minscale__ = 0
    __maxscale__ = 9637.776
    __timeInstant__ = 'years'
    __label__ = 'release_year'
    id = Column('bgdi_id', Unicode, primary_key=True)
    kbbez = Column('kbbez', Unicode)
    produkt = Column('produkt', Unicode)
    kbnum = Column('kbnum', Unicode)
    release_year = Column('release_year', Integer)
    years = Column('years', Integer)
    bv_nummer = Column('bv_nummer', Unicode)
    bgdi_order = Column('bgdi_order', Integer)
    array_release_years = Column('array_release_years', postgresql.ARRAY(Integer))
    box2d = Column('box2d', Unicode)
    the_geom = Column(Geometry2DLV03)


class DufourErst(Base, Vector):
    __tablename__ = 'view_dufour_erstausgabe'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/dufour_erst.mako'
    __bodId__ = 'ch.swisstopo.hiks-dufour'
    __label__ = 'datenstand'
    id = Column('tilenumber', Unicode, primary_key=True)
    kbbez = Column('kbbez', Unicode)
    datenstand = Column('datenstand', Integer)
    bv_nummer = Column('bv_nummer', Unicode)
    the_geom = Column(Geometry2DLV03)


class SiegfriedErst(Base, Vector):
    __tablename__ = 'view_siegfried_erstausgabe'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/siegfried_erst.mako'
    __bodId__ = 'ch.swisstopo.hiks-siegfried'
    __label__ = 'datenstand'
    id = Column('tilenumber', Unicode, primary_key=True)
    kbbez = Column('kbbez', Unicode)
    datenstand = Column('datenstand', Numeric)
    bv_nummer = Column('bv_nummer', Unicode)
    the_geom = Column(Geometry2DLV03)


register('ch.swisstopo.hiks-siegfried', SiegfriedErst)
register('ch.swisstopo.hiks-dufour', DufourErst)
register('ch.swisstopo.zeitreihen', Zeitreihen15)
register('ch.swisstopo.zeitreihen', Zeitreihen20)
register('ch.swisstopo.zeitreihen', Zeitreihen21)
register('ch.swisstopo.zeitreihen', Zeitreihen22)
