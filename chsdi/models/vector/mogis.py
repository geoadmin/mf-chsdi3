# -*- coding: utf-8 -*-

from sqlalchemy import Column

from sqlalchemy.types import Integer, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D


Base = bases['mogis']


class CadastralWebMap(Base, Vector):
    __tablename__ = 'view_os_realestate_cwm'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/cadastralwebmap.mako'
    __bodId__ = 'ch.kantone.cadastralwebmap-farbe'
    __label__ = 'ak'
    id = Column('id', Integer, primary_key=True)
    ak = Column('ak', Unicode)
    the_geom = Column(Geometry2D)

register('ch.kantone.cadastralwebmap-farbe', CadastralWebMap)


class CadastralWebMapOpenData(Base, Vector):
    __tablename__ = 'view_os_realestate_vd_opendata'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/cadastralwebmap_opendata.mako'
    __bodId__ = 'ch.swisstopo-vd.amtliche-vermessung'
    __label__ = 'name'
    __extended_info__ = True
    id = Column('id', Integer, primary_key=True)
    bfsnr = Column('bfsnr', Integer)
    ak = Column('ak', Unicode)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.amtliche-vermessung', CadastralWebMapOpenData)
