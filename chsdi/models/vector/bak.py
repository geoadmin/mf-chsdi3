# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Numeric, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D


Base = bases['bak']


class IsosBase:
    __template__ = 'templates/htmlpopup/isos.mako'
    __table_args__ = ({'autoload': False, 'extend_existing': True})
    id = Column('xtf_id', Unicode, primary_key=True)
    kantone = Column('kantone', Unicode)
    nummer = Column('id', Integer)
    name = Column('name', Unicode)
    siedlungskategorie = Column('siedlungskategorie', Unicode)
    url = Column('url', Unicode)
    the_geom = Column(Geometry2D)


class IsosOrtsbild(Base, IsosBase, Vector):
    __tablename__ = 'isos_ortsbild'
    __bodId__ = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder'
    __label__ = 'name'
    __minscale__ = 50001


class IsosOrtsbildPerimeter(Base, IsosBase, Vector):
    __tablename__ = 'view_isos_perimeter'
    __bodId__ = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder'
    __label__ = 'name'
    __maxscale__ = 50000
    __minscale__ = 25001


class IsosOrtsbildTeil(Base, IsosBase, Vector):
    __tablename__ = 'view_isos_ortsbildteil'
    __bodId__ = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder'
    __label__ = 'teil_name'
    __maxscale__ = 25000
    # __minscale__ = 5000
    teil_nummer = Column('teil_id', Integer)
    teil_name = Column('teil_name', Unicode)


class IsosOrtsbildHinweis(Base, IsosBase, Vector):
    __tablename__ = 'view_isos_hinweis'
    __bodId__ = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder'
    __label__ = 'teil_name'
    __maxscale__ = 5000
    hinweis_nummer = Column('hinweis_id', Unicode)
    hinweis_name = Column('hinweis_name', Unicode)
    siehe_auch = Column('siehe_auch', Unicode)
    teil_nummer = Column('teil_id', Integer)
    teil_name = Column('teil_name', Unicode)

register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder', IsosOrtsbild)
register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder', IsosOrtsbildPerimeter)
register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder', IsosOrtsbildTeil)
register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder', IsosOrtsbildHinweis)


class IsosFotoBase(IsosBase):
    __bodId__ = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos'
    __label__ = 'name'


class IsosFotoOrtsbild(Base, IsosFotoBase, Vector):
    __tablename__ = 'view_isos_foto'
    __minscale__ = 50001


class IsosFotoOB(Base, IsosFotoBase, Vector):
    __tablename__ = 'view_isos_foto_ob'
    __maxscale__ = 50000
    __minscale__ = 25001


class IsosFotoOBT(Base, IsosFotoBase, Vector):
    __tablename__ = 'view_isos_foto_obt'
    __maxscale__ = 25000
    __minscale__ = 5001


class IsosFotoOBTH(Base, IsosFotoBase, Vector):
    __tablename__ = 'view_isos_foto_obth'
    __maxscale__ = 5000

register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos', IsosFotoOrtsbild)
register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos', IsosFotoOB)
register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos', IsosFotoOBT)
register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder_fotos', IsosFotoOBTH)


class Unesco(Base, Vector):
    __tablename__ = 'unesco'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/unesco_bak.mako'
    __bodId__ = 'ch.bak.schutzgebiete-unesco_weltkulturerbe'
    __label__ = 'name_de'
    __returnedGeometry__ = 'the_geom_simplified_tolerance_3'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_fr = Column('name_fr', Unicode)
    name_de = Column('bgdi_name', Unicode)
    name_it = Column('name_it', Unicode)
    name_en = Column('name_en', Unicode)
    name_rm = Column('name_rm', Unicode)
    type_fr = Column('type_fr', Unicode)
    type_de = Column('type_de', Unicode)
    type_it = Column('type_it', Unicode)
    type_en = Column('type_en', Unicode)
    type_rm = Column('type_rm', Unicode)
    bgdi_surface = Column('bgdi_surface', Numeric)
    the_geom = Column(Geometry2D)
    the_geom_simplified_tolerance_3 = Column('the_geom_simplified_tolerance_3', Geometry2D)

register('ch.bak.schutzgebiete-unesco_weltkulturerbe', Unesco)


class HalteplaetzeJenischeSintiRoma(Base, Vector):
    __tablename__ = 'halteplaetze_jenische_sinti_roma'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/halteplaetze_jenische_sinti_roma.mako'
    __bodId__ = 'ch.bak.halteplaetze-jenische_sinti_roma'
    __label__ = 'standort'
    id = Column('bgdi_id', Integer, primary_key=True)
    kanton = Column('kanton', Unicode)
    nr_kanton = Column('nr_kanton', Numeric)
    plz = Column('plz', Numeric)
    gemeinde = Column('gemeinde', Unicode)
    standort = Column('standort', Unicode)
    adresse = Column('adresse', Unicode)
    platzart = Column('platzart', Numeric)
    platzart_de = Column('platzart_de', Unicode)
    platzart_fr = Column('platzart_fr', Unicode)
    platzart_it = Column('platzart_it', Unicode)
    platz_status = Column('platz_status', Numeric)
    platz_status_de = Column('platz_status_de', Unicode)
    platz_status_fr = Column('platz_status_fr', Unicode)
    platz_status_it = Column('platz_status_it', Unicode)
    anzahl_stellplaetze = Column('anzahl_stellplaetze', Numeric)
    bemerkungen_de = Column('bemerkungen_de', Unicode)
    bemerkungen_fr = Column('bemerkungen_fr', Unicode)
    bemerkungen_it = Column('bemerkungen_it', Unicode)
    x_koordinate = Column('x_koordinate', Numeric)
    y_koordinate = Column('y_koordinate', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bak.halteplaetze-jenische_sinti_roma', HalteplaetzeJenischeSintiRoma)
