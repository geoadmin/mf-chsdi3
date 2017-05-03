# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D


Base = bases['efd']


class LohnBrennereien(Base, Vector):
    __tablename__ = 'lohnbrennereien'
    __table_args__ = ({'schema': 'eav', 'autoload': False})
    __template__ = 'templates/htmlpopup/lohnbrennereien.mako'
    __bodId__ = 'ch.ezv.lohnbrennereien'
    __queryable_attributes__ = ['name', 'kanton', 'adresse', 'telefon', 'mobile', 'email', 'homepage', 'ort', 'bemerkung']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    kanton = Column('kanton', Unicode)
    adresse = Column('adresse', Unicode)
    ort = Column('ort', Unicode)
    telefon = Column('telefon', Unicode)
    mobile = Column('mobile', Unicode)
    email = Column('email', Unicode)
    homepage = Column('homepage', Unicode)
    bemerkung = Column('bemerkung', Unicode)
    the_geom = Column(Geometry2D)

register(LohnBrennereien.__bodId__, LohnBrennereien)
