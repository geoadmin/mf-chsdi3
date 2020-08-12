# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Numeric, Unicode, SmallInteger, BigInteger, Float, DateTime

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

from chsdi.models.types import DateTimeChsdi

Base = bases['kogis']


class Gebaeuderegister(Base, Vector):
    __tablename__ = 'gwr_chsdi'
    __table_args__ = ({'schema': 'bfs', 'autoload': False})
    __template__ = 'templates/htmlpopup/gebaeuderegister.mako'
    __bodId__ = 'ch.bfs.gebaeude_wohnungs_register'
    __label__ = 'strname_deinr'
    __extended_info__ = True
    # basic tooltip -> gebaeude_eingang
    id = Column('egid_edid', Unicode, primary_key=True)
    egid = Column('egid', Unicode)
    strname_deinr = Column('strname_deinr', Unicode)
    plz_plz6 = Column('plz_plz6', Unicode)
    dplzname = Column('dplzname', Unicode)
    ggdename = Column('ggdename', Unicode)
    ggdenr = Column('ggdenr', SmallInteger)
    gexpdat = Column('gexpdat', DateTimeChsdi)
    gdekt = Column('gdekt', Unicode)
    the_geom = Column(Geometry2D)
    # extended tooltip -> gebaeude
    egrid = Column('egrid', Unicode)
    lgbkr = Column('lgbkr', SmallInteger)
    lparz = Column('lparz', Unicode)
    lparzsx = Column('lparzsx', BigInteger)
    ltyp = Column('ltyp', SmallInteger)
    gebnr = Column('gebnr', Unicode)
    gbez = Column('gbez', Unicode)
    gkode = Column('gkode', Float)
    gkodn = Column('gkodn', Float)
    gksce = Column('gksce', SmallInteger)
    gstat = Column('gstat', SmallInteger)
    gkat = Column('gkat', SmallInteger)
    gklas = Column('gklas', SmallInteger)
    gbauj = Column('gbauj', SmallInteger)
    gbaum = Column('gbaum', SmallInteger)
    gbaup = Column('gbaup', SmallInteger)
    gabbj = Column('gabbj', SmallInteger)
    garea = Column('garea', Integer)
    gvol = Column('gvol', Integer)
    gvolnorm = Column('gvolnorm', SmallInteger)
    gvolsce = Column('gvolsce', SmallInteger)
    gastw = Column('gastw', SmallInteger)
    ganzwhg = Column('ganzwhg', SmallInteger)
    gazzi = Column('gazzi', SmallInteger)
    # extended tooltip -> eingang
    edid = Column('edid', SmallInteger, nullable=False)
    egaid = Column('egaid', Integer)
    deinr = Column('deinr', Unicode)
    esid = Column('esid', Integer)
    strname = Column('strname', Unicode)
    strnamk = Column('strnamk', Unicode)
    strindx = Column('strindx', Unicode)
    strsp = Column('strsp', Unicode)
    stroffiziel = Column('stroffiziel', Unicode)
    dplz4 = Column('dplz4', SmallInteger)
    dplzz = Column('dplzz', SmallInteger)
    dplzname = Column('dplzname', Unicode)
    dkode = Column('dkode', Float)
    dkodn = Column('dkodn', Float)
    doffadr = Column('doffadr', SmallInteger)
    dexpdat = Column('dexpdat', DateTimeChsdi)
    # extended tooltip -> wohnung
    ewid = Column('ewid', SmallInteger, nullable=False)
    whgnr = Column('whgnr', Unicode)
    wstwk = Column('wstwk', SmallInteger)
    wmehrg = Column('wmehrg', SmallInteger)
    weinr = Column('weinr', Unicode)
    wbez = Column('wbez', Unicode)
    wstat = Column('wstat', SmallInteger)
    wexpdat = Column('wexpdat', DateTime)

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
