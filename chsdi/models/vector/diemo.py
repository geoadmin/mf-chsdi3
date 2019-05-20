# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Boolean
from sqlalchemy.types import Numeric
from sqlalchemy.dialects import postgresql

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['diemo']


class DiemoLocations(Base, Vector):
    __tablename__ = 'v_evse'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __bodId__ = 'ch.bfe.ladestellen-elektromobilitaet'
    __queryable_attributes__ = ['queriable_authentication_mode', 'fk_operator_id', 'station_id', 'name', 'address_street', 'address_house_num', 'address_postal_code', 'address_city', 'is_open_24_hours']
    __label__ = 'name'
    id = Column('bgdi_id', Numeric, primary_key=True)
    fk_operator_id = Column('fk_operator_id', Unicode)
    station_id = Column('station_id', Unicode)
    name = Column('name', Unicode)
    address_street = Column('address_street', Unicode)
    address_house_num = Column('address_house_num', Unicode)
    address_postal_code = Column('address_postal_code', Unicode)
    address_city = Column('address_city', Unicode)
    latitude = Column('latitude', Numeric)
    longitude = Column('longitude', Numeric)
    authentication_mode = Column('authentication_mode', postgresql.ARRAY(Unicode))
    queriable_authentication_mode = Column('queriable_authentication_mode', Unicode)
    is_open_24_hours = Column('is_open_24_hours', Boolean)
    the_geom = Column(Geometry2D)

register(DiemoLocations.__bodId__, DiemoLocations)
