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
    __queryable_attributes__ = ['aviailability', 'accessibility', 'queriable_plug_type', 'queriable_charging_facilities',
                                'queriable_authentication_mode', 'fk_operator_id', 'is_hubjet_compatible',
                                'location_id', 'name', 'address_street', 'address_house_num',
                                'address_postal_code', 'address_city', 'is_open_24_hours']
    __label__ = 'name'
    id = Column('bgdi_id', Numeric, primary_key=True)
    fk_operator_id = Column('fk_operator_id', Unicode)
    location_id = Column('location_id', Unicode)
    name = Column('name', Unicode)
    accessibility = Column('accessibility', Unicode)
    aviailability = Column('availability', Unicode)
    address_street = Column('address_street', Unicode)
    address_house_num = Column('address_house_num', Unicode)
    address_postal_code = Column('address_postal_code', Unicode)
    address_city = Column('address_city', Unicode)
    latitude = Column('latitude', Numeric)
    longitude = Column('longitude', Numeric)
    authentication_mode = Column('authentication_mode', postgresql.ARRAY(Unicode))
    plug_type = Column('plug_type', postgresql.ARRAY(Unicode))
    charging_facilities = Column('charging_facilities', postgresql.ARRAY(Unicode))
    queriable_authentication_mode = Column('queriable_authentication_mode', Unicode)
    queriable_plug_type = Column('queriable_plug_type', Unicode)
    queriable_charging_facilities = Column('queriable_charging_facilities', Unicode)
    is_open_24_hours = Column('is_open_24_hours', Boolean)
    is_hubject_compatible = Column('is_hubject_compatible', Boolean)
    the_geom = Column(Geometry2D)

register(DiemoLocations.__bodId__, DiemoLocations)
