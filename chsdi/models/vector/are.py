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


class Agglomerationsverkehr(Base, Vector):
    __tablename__ = 'agglomerationsverkehr'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/agglomerationsverkehr.mako'
    __bodId__ = 'ch.are.agglomerationsverkehr'
    __label__ = 'name'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode)
    gem_no = Column('gem_no', Integer)
    agglo_no = Column('agglo_no', Integer)
    agglo_name = Column('agglo_name', Unicode)
    land = Column('land', Unicode)
    the_geom = Column(Geometry2D)

register('ch.are.agglomerationsverkehr', Agglomerationsverkehr)


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


class Bauzonen(Base, Vector):
    __tablename__ = 'bauzonen'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/bauzonen.mako'
    __bodId__ = 'ch.are.bauzonen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    ch_code_hn = Column('ch_code_hn', Unicode)
    kt_kz = Column('kt_kz', Unicode)
    bfs_no = Column('bfs_no', Unicode)
    kt_no = Column('kt_no', Unicode)
    flaeche = Column('flaeche', Float)
    ch_bez_f = Column('ch_bez_f', Unicode)
    ch_bez_d = Column('ch_bez_d', Unicode)
    the_geom = Column(Geometry2D)

register('ch.are.bauzonen', Bauzonen)


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
    __tablename__ = 'zweitwohnungsanteil'
    __table_args__ = ({'schema': 'raumplanung', 'autoload': False})
    __template__ = 'templates/htmlpopup/zweitwohnungsanteil.mako'
    __bodId__ = 'ch.are.wohnungsinventar-zweitwohnungsanteil'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    gemeinde_name = Column('gemeinde_name', Unicode)
    gemeinde_nummer = Column('gemeinde_nummer', Integer)
    status = Column('status', Integer)
    verfahren = Column('verfahren', Integer)
    zwg_3150 = Column('zwg_3150', Integer)
    zwg_3010 = Column('zwg_3010', Integer)
    zwg_3100 = Column('zwg_3100', Integer)
    zwg_3110 = Column('zwg_3110', Float)
    zwg_3120 = Column('zwg_3120', Float)
    the_geom = Column(Geometry2D)

register('ch.are.wohnungsinventar-zweitwohnungsanteil', ZweitwohnungsAnteil)


class ReisezeitAgglomerationen:
    __tablename__ = 'reisezeit_agglomerationen'
    id = Column('verkehrszone_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class Reisezeit:
    __tablename__ = 'reisezeit'
    id = Column('verkehrszone_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class Erreichbarkeit:
    __tablename__ = 'erreichbarkeit'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    __label__ = 'id'
    id = Column('verkehrszone_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class ReisezeitAgglomerationenOev(Base, ReisezeitAgglomerationen, Vector):
    __bodId__ = 'ch.are.reisezeit-agglomerationen-oev'
    __template__ = 'templates/htmlpopup/reisezeit_agglomerationen_oev.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    oev_reisezeit_agglo = Column('oev_reisezeit_agglo', Integer)
    oev_no_agglo = Column('oev_no_agglo', Integer)

register('ch.are.reisezeit-agglomerationen-oev', ReisezeitAgglomerationenOev)


class ReisezeitAgglomerationenMiv(Base, ReisezeitAgglomerationen, Vector):
    __bodId__ = 'ch.are.reisezeit-agglomerationen-miv'
    __template__ = 'templates/htmlpopup/reisezeit_agglomerationen_miv.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    strasse_reisezeit_agglo = Column('strasse_reisezeit_agglo', Integer)
    strasse_no_agglo = Column('strasse_no_agglo', Integer)

register('ch.are.reisezeit-agglomerationen-miv', ReisezeitAgglomerationenMiv)


class ReisezeitOev(Base, Reisezeit, Vector):
    __bodId__ = 'ch.are.reisezeit-oev'
    __template__ = 'templates/htmlpopup/reisezeit_oev.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    oev_reisezeit_z = Column('oev_reisezeit_z', Integer)
    oev_no_z = Column('oev_no_z', Integer)

register('ch.are.reisezeit-oev', ReisezeitOev)


class ReisezeitMiv(Base, Reisezeit, Vector):
    __bodId__ = 'ch.are.reisezeit-miv'
    __template__ = 'templates/htmlpopup/reisezeit_miv.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    strasse_reisezeit_z = Column('strasse_reisezeit_z', Integer)
    strasse_no_z = Column('strasse_no_z', Integer)

register('ch.are.reisezeit-miv', ReisezeitMiv)


class ErreichbarkeitOev(Base, Erreichbarkeit, Vector):
    __bodId__ = 'ch.are.erreichbarkeit-oev'
    __template__ = 'templates/htmlpopup/erreichbarkeit_oev.mako'
    oev_erreichb_ewap = Column('oev_erreichb_ewap', Integer)

register('ch.are.erreichbarkeit-oev', ErreichbarkeitOev)


class ErreichbarkeitMiv(Base, Erreichbarkeit, Vector):
    __bodId__ = 'ch.are.erreichbarkeit-miv'
    __template__ = 'templates/htmlpopup/erreichbarkeit_miv.mako'
    strasse_erreichb_ewap = Column('strasse_erreichb_ewap', Integer)

register('ch.are.erreichbarkeit-miv', ErreichbarkeitMiv)


class BelastungPersonenverkehrStrasse(Base, Vector):
    __tablename__ = 'belastung_personenverkehr'
    __table_args__ = ({'schema': 'strassen', 'autoload': False})
    __template__ = 'templates/htmlpopup/personenverkehr_strasse.mako'
    __bodId__ = 'ch.are.belastung-personenverkehr-strasse'
    __label__ = 'nr'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    nr = Column('nr', Integer)
    dwv_fzg = Column('dwv_fzg', Integer)
    dwv_pw = Column('dwv_pw', Integer)
    dwv_li = Column('dwv_li', Integer)
    dwv_lw = Column('dwv_lw', Integer)
    dwv_lz = Column('dwv_lz', Integer)
    dtv_fzg = Column('dtv_fzg', Integer)
    dtv_pw = Column('dtv_pw', Integer)
    dtv_li = Column('dtv_li', Integer)
    dtv_lw = Column('dtv_lw', Integer)
    dtv_lz = Column('dtv_lz', Integer)
    msp_fzg = Column('msp_fzg', Integer)
    msp_pw = Column('msp_pw', Integer)
    msp_li = Column('msp_li', Integer)
    msp_lw = Column('msp_lw', Integer)
    msp_lz = Column('msp_lz', Integer)
    asp_fzg = Column('asp_fzg', Integer)
    asp_pw = Column('asp_pw', Integer)
    asp_li = Column('asp_li', Integer)
    asp_lw = Column('asp_lw', Integer)
    asp_lz = Column('asp_lz', Integer)
    the_geom = Column(Geometry2D)
register(BelastungPersonenverkehrStrasse.__bodId__, BelastungPersonenverkehrStrasse)


class BelastungPersonenverkehrBahn(Base, Vector):
    __tablename__ = 'belastung_personenverkehr'
    __table_args__ = ({'schema': 'oeffentlicher_verkehr', 'autoload': False})
    __template__ = 'templates/htmlpopup/personenverkehr_bahn.mako'
    __bodId__ = 'ch.are.belastung-personenverkehr-bahn'
    __label__ = 'nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr = Column('nr', Integer)
    dwv_oev = Column('dwv_oev', Integer)
    dtv_oev = Column('dtv_oev', Integer)
    msp_oev = Column('msp_oev', Integer)
    asp_oev = Column('asp_oev', Integer)
    the_geom = Column(Geometry2D)

register(BelastungPersonenverkehrBahn.__bodId__, BelastungPersonenverkehrBahn)
