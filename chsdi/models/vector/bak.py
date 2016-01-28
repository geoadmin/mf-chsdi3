# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer
from sqlalchemy.types import Numeric

from geoalchemy2.types import Geometry

from chsdi.models import register, bases
from chsdi.models.vector import Vector


Base = bases['bak']


class ISOS(Base, Vector):
    __tablename__ = 'isos'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/isos.mako'
    __bodId__ = 'ch.bak.bundesinventar-schuetzenswerte-ortsbilder'
    __label__ = 'ortsbildname'
    id = Column('gid', Integer, primary_key=True)
    ortsbildname = Column('ortsbildname', Text)
    kanton = Column('kanton', Text)
    vergleichsrastereinheit = Column('vergleichsrastereinheit', Text)
    lagequalitaeten = Column('lagequalitaeten', Text)
    raeumliche_qualitaeten = Column('raeumliche_qualitaeten', Text)
    arch__hist__qualitaeten = Column('arch__hist__qualitaeten', Text)
    fassungsjahr = Column('fassungsjahr', Text)
    band_1 = Column('band_1', Text)
    band_2 = Column('band_2', Text)
    publikationsjahr_1 = Column('publikationsjahr_1', Text)
    publikationsjahr_2 = Column('publikationsjahr_2', Text)
    pdf_dokument_1 = Column('pdf_dokument_1', Text)
    pdf_dokument_2 = Column('pdf_dokument_2', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.bak.bundesinventar-schuetzenswerte-ortsbilder', ISOS)


class UNESCO(Base, Vector):
    __tablename__ = 'unesco'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/unesco_bak.mako'
    __bodId__ = 'ch.bak.schutzgebiete-unesco_weltkulturerbe'
    __label__ = 'name_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_fr = Column('name_fr', Text)
    name_de = Column('bgdi_name', Text)
    name_it = Column('name_it', Text)
    name_en = Column('name_en', Text)
    name_rm = Column('name_rm', Text)
    type_fr = Column('type_fr', Text)
    type_de = Column('type_de', Text)
    type_it = Column('type_it', Text)
    type_en = Column('type_en', Text)
    type_rm = Column('type_rm', Text)
    bgdi_surface = Column('bgdi_surface', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.bak.schutzgebiete-unesco_weltkulturerbe', UNESCO)
