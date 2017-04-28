# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Unicode, Integer, Float
from sqlalchemy.types import Numeric

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['dritte']


class MaechtigkeitLockergesteine(Base, Vector):
    __tablename__ = 'maechtigkeit_lockergesteine'
    __table_args__ = ({'schema': 'sgpk', 'autoload': False})
    __template__ = 'templates/htmlpopup/maechtigkeit_lockergesteine.mako'
    __bodId__ = 'ch.sgpk.maechtigkeit-lockergesteine'
    __label__ = 'id'
    id = Column('id', Integer, primary_key=True)
    maechtigkeit = Column('maechtigkeit', Numeric)
    the_geom = Column(Geometry2D)

register('ch.sgpk.maechtigkeit-lockergesteine', MaechtigkeitLockergesteine)


class Feuerstellen(Base, Vector):
    __tablename__ = 'feuerstellen'
    __table_args__ = ({'schema': 'tamedia', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissmap_online_feuerstellen.mako'
    __bodId__ = 'ch.tamedia.schweizerfamilie-feuerstellen'
    __label__ = 'gemeinde'
    id = Column('nr', Integer, primary_key=True)
    gemeinde = Column('gemeinde', Text)
    ort = Column('ort', Text)
    kanton = Column('kanton', Text)
    karte = Column('karte', Text)
    url = Column('url', Text)
    koordinate_lv03 = Column('koordinate_lv03', Text)
    the_geom = Column(Geometry2D)

register('ch.tamedia.schweizerfamilie-feuerstellen', Feuerstellen)


class MobilityStandorte:
    __tablename__ = 'standorte_tooltip'
    __table_args__ = ({'schema': 'mobility', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/mobility_standorte.mako'
    __bodId__ = 'ch.mobility.standorte'
    __label__ = 'name'
    __returnedGeometry__ = 'the_geom_point'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    number = Column('number', Integer)
    location = Column('location', Unicode)
    lat = Column('lat', Float)
    lon = Column('lon', Float)
    street = Column('street', Unicode)
    city = Column('city', Unicode)
    categories = Column('categories', Unicode)
    the_geom_point = Column('the_geom', Geometry2D)


class MobilityStandorteZoom1(Base, MobilityStandorte, Vector):
    __minscale__ = 1
    __maxscale__ = 4000
    the_geom = Column('the_geom_click', Geometry2D)

register(MobilityStandorte.__bodId__, MobilityStandorteZoom1)


class MobilityStandorteZoom2(Base, MobilityStandorte, Vector):
    __minscale__ = 4000
    the_geom = Column('the_geom_click_overview', Geometry2D)

register(MobilityStandorte.__bodId__, MobilityStandorteZoom2)


class Notfallschutz(Base, Vector):
    __tablename__ = 'zonenplan_kernanlagen'
    __table_args__ = ({'schema': 'ensi', 'autoload': False})
    __template__ = 'templates/htmlpopup/zonenplan_kernanlagen.mako'
    __bodId__ = 'ch.ensi.zonenplan-notfallschutz-kernanlagen'
    __label__ = 'name'
    id = Column('nr', Integer, primary_key=True)
    name = Column('name', Text)
    zone = Column('zone', Text)
    sektor = Column('sektor', Text)
    the_geom = Column(Geometry2D)

register('ch.ensi.zonenplan-notfallschutz-kernanlagen', Notfallschutz)


class PronaturaWaldreservate(Base, Vector):
    __tablename__ = 'waldreservate'
    __table_args__ = ({'schema': 'pronatura', 'autoload': False})
    __template__ = 'templates/htmlpopup/pronatura.mako'
    __bodId__ = 'ch.pronatura.waldreservate'
    __queryable_attributes__ = ['name', 'objnummer', 'gesflaeche', 'gesflaeche', 'gisteilobjekt', 'mcpfe']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Integer)
    name = Column('name', Unicode)
    gisflaeche = Column('obj_gisflaeche', Float)
    gesflaeche = Column('obj_gesflaeche', Float)
    gisteilobjekt = Column('obj_gisteilobjekt', Float)
    mcpfe = Column('mcpfe', Unicode)
    the_geom = Column(Geometry2D)

register(PronaturaWaldreservate.__bodId__, PronaturaWaldreservate)


class PronaturaNaturschutzgebiete(Base, Vector):
    __tablename__ = 'naturschutzgebiete'
    __table_args__ = ({'schema': 'pronatura', 'autoload': False})
    __template__ = 'templates/htmlpopup/pronatura_schutzge.mako'
    __bodId__ = 'ch.pronatura.naturschutzgebiete'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    nummer = Column('nummer', Integer)
    name = Column('name', Text)
    the_geom = Column(Geometry2D)

register('ch.pronatura.naturschutzgebiete', PronaturaNaturschutzgebiete)


class AeromagnetischeKarte1500(Base, Vector):
    __tablename__ = 'am_1500'
    __table_args__ = ({'schema': 'nagra', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetische_karte.mako'
    __bodId__ = 'ch.nagra.aeromagnetische-karte_1500'
    __label__ = 'id'
    id = Column('et_id', Integer, primary_key=True)
    et_fromatt_1500 = Column('et_fromatt_1500', Numeric)
    the_geom = Column(Geometry2D)

register('ch.nagra.aeromagnetische-karte_1500', AeromagnetischeKarte1500)


class AeromagnetischeKarte1100(Base, Vector):
    __tablename__ = 'am_1100'
    __table_args__ = ({'schema': 'nagra', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetische_karte.mako'
    __bodId__ = 'ch.nagra.aeromagnetische-karte_1100'
    __label__ = 'id'
    id = Column('et_id', Integer, primary_key=True)
    et_fromatt_1100 = Column('et_fromatt_1100', Numeric)
    the_geom = Column(Geometry2D)


register('ch.nagra.aeromagnetische-karte_1100', AeromagnetischeKarte1100)
