# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Numeric, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D


Base = bases['bak']


class Isos(Base, Vector):
    __tablename__ = 'isos'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/isos.mako'
    __bodId__ = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder'
    __label__ = 'ortsbildname'
    id = Column('gid', Integer, primary_key=True)
    ortsbildname = Column('ortsbildname', Unicode)
    kanton = Column('kanton', Unicode)
    vergleichsrastereinheit = Column('vergleichsrastereinheit', Unicode)
    lagequalitaeten = Column('lagequalitaeten', Unicode)
    raeumliche_qualitaeten = Column('raeumliche_qualitaeten', Unicode)
    arch__hist__qualitaeten = Column('arch__hist__qualitaeten', Unicode)
    fassungsjahr = Column('fassungsjahr', Unicode)
    band_1 = Column('band_1', Unicode)
    band_2 = Column('band_2', Unicode)
    publikationsjahr_1 = Column('publikationsjahr_1', Unicode)
    publikationsjahr_2 = Column('publikationsjahr_2', Unicode)
    pdf_dokument_1 = Column('pdf_dokument_1', Unicode)
    pdf_dokument_2 = Column('pdf_dokument_2', Unicode)
    pdfspecial = Column('pdfspecial', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder', Isos)


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
