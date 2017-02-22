# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer, Date
from sqlalchemy.types import Numeric, BigInteger
from sqlalchemy.dialects import postgresql

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D


Base = bases['uvek_solarkataster']


class SolarClass:
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __label__ = 'id'
    __maxscale__ = 100005
    building_id = Column('building_id', Integer)
    a_param = Column('a_param', postgresql.ARRAY(Numeric))
    b_param = Column('b_param', postgresql.ARRAY(Numeric))
    c_param = Column('c_param', postgresql.ARRAY(Numeric))
    heizgradtage = Column('heizgradtage', postgresql.ARRAY(Numeric))
    bedarf_heizung = Column('bedarf_heizung', Integer)
    bedarf_warmwasser = Column('bedarf_warmwasser', Integer)
    datum_aenderung = Column('datum_aenderung', Date)
    datum_erstellung = Column('datum_erstellung', Date)
    dg_heizung = Column('dg_heizung', Integer)
    dg_waermebedarf = Column('dg_waermebedarf', Integer)
    duschgaenge = Column('duschgaenge', Integer)
    flaeche_kollektoren = Column('flaeche_kollektoren', Numeric)
    gstrahlung = Column('gstrahlung', Integer)
    mstrahlung = Column('mstrahlung', Integer)
    sb_datum_aenderung = Column('sb_datum_aenderung', Date)
    sb_datum_erstellung = Column('sb_datum_erstellung', Date)
    sb_objektart = Column('sb_objektart', Integer)
    volumen_speicher = Column('volumen_speicher', Integer)
    waermeertrag = Column('waermeertrag', Integer)
    monate = Column('monat', postgresql.ARRAY(Numeric))
    klasse = Column('klasse', Integer)
    flaeche = Column('flaeche', Numeric)
    ausrichtung = Column('ausrichtung', Integer)
    finanzertrag = Column('finanzertrag', Numeric)
    stromertrag = Column('stromertrag', Integer)
    monats_ertrag = Column('monats_ertrag', postgresql.ARRAY(Numeric))
    gs_serie_start = Column('gs_serie_start', Date)
    klasse_text = Column('klasse_text', Text)
    the_geom = Column(Geometry2D)


class SolarOverview:
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __label__ = 'id'
    __minscale__ = 100005
    id = Column('av_id', Integer, primary_key=True)
    de = Column('de', Text)
    fr = Column('fr', Text)
    it = Column('it', Text)
    en = Column('en', Text)
    the_geom = Column(Geometry2D)


class eignungDaecher (Base, SolarClass, Vector):
    __tablename__ = 'view_solarenergie_daecher_gs'
    __template__ = 'templates/htmlpopup/solareignungdaecher.mako'
    __bodId__ = 'ch.bfe.solarenergie-eignung-daecher'
    __queryable_attributes__ = ['df_uid', 'building_id']
    id = Column('df_uid', BigInteger, primary_key=True)
    df_nummer = Column('df_nummer', Integer)
    neigung = Column('neigung', Integer)

register(eignungDaecher.__bodId__, eignungDaecher)


class eignungDaecherOverview (Base, SolarOverview, Vector):
    __tablename__ = 'solarenergie_availability'
    __template__ = 'templates/htmlpopup/solareignungdaecher_av.mako'
    __parentLayerId__ = eignungDaecher.__bodId__
    __bodId__ = 'ch.bfe.solarenergie-eignung-daecher'

register(eignungDaecherOverview.__bodId__, eignungDaecherOverview)


class eignungFassaden (Base, SolarClass, Vector):
    __tablename__ = 'view_solarenergie_fassaden_gs'
    __template__ = 'templates/htmlpopup/solareignungfassaden.mako'
    __bodId__ = 'ch.bfe.solarenergie-eignung-fassaden'
    __queryable_attributes__ = ['ff_nummer', 'gwr_egid', 'building_id']
    id = Column('ff_uuid', BigInteger, primary_key=True)
    ff_nummer = Column('ff_nummer', Integer)
    gwr_egid = Column('gwr_egid', Integer)

register(eignungFassaden.__bodId__, eignungFassaden)


class eignungFassadenOverview (Base, SolarOverview, Vector):
    __tablename__ = 'solarenergie_fassaden_availability'
    __template__ = 'templates/htmlpopup/solareignungdaecher_av.mako'
    __parentLayerId__ = eignungFassaden.__bodId__
    __bodId__ = 'ch.bfe.solarenergie-eignung-fassaden'

register(eignungFassadenOverview.__bodId__, eignungFassadenOverview)
