# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['kogis']


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
