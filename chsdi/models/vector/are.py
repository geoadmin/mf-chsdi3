# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Float, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D, Geometry3D


Base = bases['are']


class Landschaftstypen(Base, Vector):
    __tablename__ = 'landschaftstypen'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/landschaftstypen.mako'
    __bodId__ = 'ch.are.landschaftstypen'
    __label__ = 'typ_nr'
    id = Column('object', Unicode, primary_key=True)
    typ_nr = Column('typ_nr', Integer)
    typname_de = Column('typname_de', Unicode)
    typname_fr = Column('typname_fr', Unicode)
    regname_de = Column('regname_de', Unicode)
    regname_fr = Column('regname_fr', Unicode)
    object_are = Column('object_are', Float)
    typ_area = Column('typ_area', Float)
    stand = Column('stand', Unicode)
    the_geom = Column(Geometry2D)

register('ch.are.landschaftstypen', Landschaftstypen)


class Alpenkonvention(Base, Vector):
    __tablename__ = 'alpenkonvention'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/alpenkonvention.mako'
    __bodId__ = 'ch.are.alpenkonvention'
    __label__ = 'stand'
    id = Column('row_id', Integer, primary_key=True)
    flaeche_ha = Column('flaeche_ha', Float)
    stand = Column('stand', Float)
    the_geom = Column(Geometry3D)

register('ch.are.alpenkonvention', Alpenkonvention)


class AggloIsoStaedte(Base, Vector):
    __tablename__ = 'agglomerationen_isolierte_staedte'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/aggloisostaedte.mako'
    __bodId__ = 'ch.are.agglomerationen_isolierte_staedte'
    __label__ = 'name'
    id = Column('row_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    klasse_de = Column('klasse_de', Unicode)
    klasse_fr = Column('klasse_fr', Unicode)
    flaeche_ha = Column('flaeche_ha', Float)
    the_geom = Column(Geometry2D)

register('ch.are.agglomerationen_isolierte_staedte', AggloIsoStaedte)


class GueteklasseOev(Base, Vector):
    __tablename__ = 'gueteklassen'
    __table_args__ = ({'schema': 'oeffentlicher_verkehr', 'autoload': False})
    __template__ = 'templates/htmlpopup/gueteklasseoev.mako'
    __bodId__ = 'ch.are.gueteklassen_oev'
    __label__ = 'klasse_fr'
    id = Column('id', Integer, primary_key=True)
    klasse_de = Column('klasse_de', Unicode)
    klasse_fr = Column('klasse_fr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.are.gueteklassen_oev', GueteklasseOev)


class Bevoelkerungsdichte(Base, Vector):
    __tablename__ = 'bevoelkerungsdichte'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/bevoelkerungsdichte.mako'
    __bodId__ = 'ch.are.bevoelkerungsdichte'
    __label__ = 'popt_ha'  # Composite labels
    id = Column('row_id', Integer, primary_key=True)
    popt_ha = Column('popt_ha', Float)
    stand = Column('stand', Float)
    the_geom = Column(Geometry2D)

register('ch.are.bevoelkerungsdichte', Bevoelkerungsdichte)


class Beschaeftigtendichte(Base, Vector):
    __tablename__ = 'beschaeftigtendichte'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/beschaeftigtendichte.mako'
    __bodId__ = 'ch.are.beschaeftigtendichte'
    __label__ = 'empt_ha'
    id = Column('row_id', Integer, primary_key=True)
    empt_ha = Column('empt_ha', Float)
    stand = Column('stand', Float)
    the_geom = Column(Geometry2D)

register('ch.are.beschaeftigtendichte', Beschaeftigtendichte)


class Bauzonen(Base, Vector):
    __tablename__ = 'bauzonen_2007'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/bauzonen.mako'
    __bodId__ = 'ch.are.bauzonen-2007'
    id = Column('row_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    nutz_de = Column('nutz_de', Unicode)
    nutz_fr = Column('nutz_fr', Unicode)
    kt_kz = Column('kt_kz', Unicode)
    flaeche_qm = Column('flaeche_qm', Float)
    the_geom = Column(Geometry2D)

register('ch.are.bauzonen-2007', Bauzonen)


class Bauzonen_2012(Base, Vector):
    __tablename__ = 'bauzonen_2012'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/bauzonen_2012.mako'
    __bodId__ = 'ch.are.bauzonen'
    __label__ = 'name_'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_ = Column('name_', Unicode)
    ch_code_hn = Column('ch_code_hn', Unicode)
    kt_kz = Column('kt_kz', Unicode)
    bfs_no = Column('bfs_no', Unicode)
    kt_no = Column('kt_no', Unicode)
    flaeche = Column('flaeche', Float)
    ch_bez_f = Column('ch_bez_f', Unicode)
    ch_bez_d = Column('ch_bez_d', Unicode)
    the_geom = Column(Geometry2D)

register('ch.are.bauzonen', Bauzonen_2012)


class Gemeindetyp(Base, Vector):
    __tablename__ = 'gemeindetyp_1990_9klassen'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/gemeindetyp.mako'
    __bodId__ = 'ch.are.gemeindetyp-1990-9klassen'
    __label__ = 'name'
    id = Column('gde_no', Integer, primary_key=True)
    name = Column('name', Unicode)
    nom = Column('nom', Unicode)
    the_geom = Column(Geometry2D)

register('ch.are.gemeindetyp-1990-9klassen', Gemeindetyp)


class Gemeindetypen_2012(Base, Vector):
    __tablename__ = 'gemeindetypologie_2012'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/gemeindetypen_2012.mako'
    __bodId__ = 'ch.are.gemeindetypen'
    __label__ = 'name_'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_ = Column('name_', Unicode)
    typ_code = Column('typ_code', Unicode)
    typ_bez_d = Column('typ_bez_d', Unicode)
    typ_bez_f = Column('typ_bez_f', Unicode)
    bfs_no = Column('bfs_no', Unicode)
    kt_no = Column('kt_no', Unicode)
    kt_kz = Column('kt_kz', Unicode)
    flaeche_ha = Column('flaeche_ha', Float)
    the_geom = Column(Geometry2D)

register('ch.are.gemeindetypen', Gemeindetypen_2012)


class WindenergieBundesinteressen(Base, Vector):
    __tablename__ = 'windenergie_bundesinteressen'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/windenergie_bundesinteressen.mako'
    __bodId__ = 'ch.are.windenergie-bundesinteressen'
    __label__ = 'kbik'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    kbik = Column('kbik', Integer)
    bik1_5_d = Column('bik1_5_d', Unicode)
    bik1_5_fr = Column('bik1_5_fr', Unicode)
    bik1_5_it = Column('bik1_5_it', Unicode)
    bik2_d = Column('bik2_d', Unicode)
    bik2_fr = Column('bik2_fr', Unicode)
    bik2_it = Column('bik2_it', Unicode)
    bik3_d = Column('bik3_d', Unicode)
    bik3_fr = Column('bik3_fr', Unicode)
    bik3_it = Column('bik3_it', Unicode)
    bik4_d = Column('bik4_d', Unicode)
    bik4_fr = Column('bik4_fr', Unicode)
    bik4_it = Column('bik4_it', Unicode)
    the_geom = Column(Geometry2D)

register(WindenergieBundesinteressen.__bodId__, WindenergieBundesinteressen)


class ZweitwohnungsAnteil(Base, Vector):
    __tablename__ = 'wohnungsinventar_zweitwohnungsanteil'
    __table_args__ = ({'schema': 'raumplanung', 'autoload': False})
    __template__ = 'templates/htmlpopup/zweitwohnungsanteil.mako'
    __bodId__ = 'ch.are.wohnungsinventar-zweitwohnungsanteil'
    __label__ = 'id'
    id = Column('objectid', Integer, primary_key=True)
    gemeinde_name = Column('gemeinde_name', Unicode)
    zwg_3150 = Column('zwg_3150', Integer)
    zwg_3010 = Column('zwg_3010', Integer)
    zwg_3100 = Column('zwg_3100', Integer)
    zwg_3110 = Column('zwg_3110', Float)
    zwg_3120 = Column('zwg_3120', Float)
    zwg_3200_de = Column('zwg_3200_de', Unicode)
    zwg_3200_fr = Column('zwg_3200_fr', Unicode)
    zwg_3200_it = Column('zwg_3200_it', Unicode)
    zwg_3200_rm = Column('zwg_3200_rm', Unicode)
    zwg_3200_en = Column('zwg_3200_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.are.wohnungsinventar-zweitwohnungsanteil', ZweitwohnungsAnteil)
