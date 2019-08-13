# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Boolean, Date
from sqlalchemy.types import Numeric
from sqlalchemy.dialects import postgresql

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['diemo']


class DiemoLocations(Base, Vector):
    __tablename__ = 'v_evse_aggregated'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __bodId__ = 'ch.bfe.ladestellen-elektromobilitaet'
    __queryable_attributes__ = ['EvseID', 'Availability', 'QueryPlugs', 'Accessiblity', 'IsHubjectCompatible', 'QueryChargingFacilities', 'DynamicInfoAvailable',
                                'QueryChargingModes', 'MaxCapacity', 'QueryPaymentOptions', 'AdditionalInfo', 'ChargingStationID', 'ChargingStationName',
                                'Address', 'Street', 'HouseNum', 'PostalCode', 'City', 'QueryAutheticationModes', 'Latitude',
                                'Longitude', 'GeoCoordinates', 'LastUdate', 'IsOpen24Hours', 'OpeningTimes', 'OperatorID', 'OperatorName']
    __label__ = 'EvseID'
    id = Column('bgdi_id', Numeric, primary_key=True)
    EvseID = Column('loading_unit_id', Unicode)
    Availability = Column('availability', Unicode)
    Plugs = Column('plug_type', postgresql.ARRAY(Unicode))
    QueryPlugs = Column('queriable_plug_type', Unicode)
    Accessibility = Column('accessibility', Unicode)
    IsHubjectCompatible = Column('is_hubject_compatible', Boolean)
    ChargingFacilities = Column('charging_facilities', postgresql.ARRAY(Unicode))
    QueryChargingFacilities = Column('queriable_charging_facilities', Unicode)
    DynamicInfoAvailable = Column('dynamic_info_available', Unicode)
    ChargingModes = Column('charging_modes', postgresql.ARRAY(Unicode))
    QueryChargingModes = Column('queriable_charging_modes', Unicode)
    MaxCapacity = Column('max_capacity', Numeric)
    PaymentOptions = Column('payment_options', postgresql.ARRAY(Unicode))
    QueryPaymentOptions = Column('queriable_payment_options', Unicode)
    AdditionalInfo = Column('additional_info', Unicode)
    ChargingStationID = Column('location_id', Unicode)
    CharingStationName = Column('name', Unicode)
    Address = Column('queriable_address', Unicode)
    Street = Column('address_street', Unicode)
    HouseNum = Column('address_house_num', Unicode)
    PostalCode = Column('address_postal_code', Unicode)
    City = Column('address_city', Unicode)
    AuthenticationModes = Column('authentication_mode', postgresql.ARRAY(Unicode))
    QueryAuthenticationModes = Column('queriable_authentication_mode', Unicode)
    Latitude = Column('latitude', Numeric)
    Longitude = Column('longitude', Numeric)
    GeoCoordinates = Column('queriable_geocoordinates', Unicode)
    LastUpdate = Column('last_modified', Date)
    IsOpen24Hours = Column('is_open_24_hours', Boolean)
    OpeningTimes = Column('opening_times', Boolean)
    OperatorID = Column('operator_id', Unicode)
    OperatorName = Column('operator_name', Unicode)
    ProviderURL = Column('provider_url', Unicode)
    the_geom = Column(Geometry2D)

register(DiemoLocations.__bodId__, DiemoLocations)
