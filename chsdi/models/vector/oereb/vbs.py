# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode

from chsdi.models import register_oereb, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['vbs']


class OerebBase:
    id = Column('stabil_id', Unicode, primary_key=True)
    the_geom = Column(Geometry2D)
    geomType = Column('geom_type', Unicode)
    xmlData = Column('xml_data', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    data_created = Column('data_created', Unicode)


# MILITAER
class KatasterBelasteterStandorteMilitaerOereb(Base, OerebBase, Vector):
    __tablename__ = 'kataster_belasteter_standorte_militaer_oereb'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __bodId__ = 'ch.vbs.kataster-belasteter-standorte-militaer.oereb'

register_oereb(KatasterBelasteterStandorteMilitaerOereb.__bodId__, KatasterBelasteterStandorteMilitaerOereb)
