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
    __queryable_attributes__ = ['EvseID', 'Availability', 'QueryPlugs', 'Accessibility', 'IsHubjectCompatible', 'QueryChargingFacilities', 'DynamicInfoAvailable',
                                'QueryChargingModes', 'ChargingPoolID', 'MaxCapacity', 'QueryPaymentOptions', 'AdditionalInfo', 'ChargingStationID', 'ChargingStationName',
                                'EnChargingStationName', 'Address', 'Street', 'HouseNum', 'Floor', 'Region', 'PostalCode', 'City', 'Timezone', 'Country', 'QueryAuthenticationModes',
                                'Latitude', 'Longitude', 'GeoCoordinates', 'EntranceLatitude', 'EntranceLongitude', 'EntranceLatitude', 'GeoChargingPointEntrance', 'lastUpdate', 'ClearinghouseID',
                                'IsOpen24Hours', 'OpeningTimes', 'HubOperatorId', 'OperatorID', 'OperatorName', 'HotlinePhoneNumber', 'deltaType', 'QueryValueAddedServices']
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
    ChargingPoolID = Column('charging_pool_id', Unicode)
    DynamicInfoAvailable = Column('dynamic_info_available', Unicode)
    ChargingModes = Column('charging_modes', postgresql.ARRAY(Unicode))
    QueryChargingModes = Column('queriable_charging_modes', Unicode)
    MaxCapacity = Column('max_capacity', Numeric)
    deltaType = Column('delta_type', Unicode)
    PaymentOptions = Column('payment_options', postgresql.ARRAY(Unicode))
    QueryPaymentOptions = Column('queriable_payment_options', Unicode)
    AdditionalInfo = Column('additional_info', Unicode)
    ValueAddedServices = Column('value_added_service', postgresql.ARRAY(Unicode))
    QueryValueAddedServices = Column('queriable_value_added_service', Unicode)
    ChargingStationID = Column('location_id', Unicode)
    ChargingStationName = Column('name', Unicode)
    EnChargingStationName = Column('name_en', Unicode)
    Address = Column('queriable_address', Unicode)
    Street = Column('address_street', Unicode)
    HouseNum = Column('address_house_num', Unicode)
    Floor = Column('address_floor', Unicode)
    Region = Column('address_region', Unicode)
    PostalCode = Column('address_postal_code', Unicode)
    City = Column('address_city', Unicode)
    Timezone = Column('address_timezone', Unicode)
    Country = Column('address_country', Unicode)
    AuthenticationModes = Column('authentication_mode', postgresql.ARRAY(Unicode))
    QueryAuthenticationModes = Column('queriable_authentication_mode', Unicode)
    Latitude = Column('latitude', Numeric)
    Longitude = Column('longitude', Numeric)
    GeoCoordinates = Column('queriable_geocoordinates', Unicode)
    EntranceLatitude = Column('entrance_latitude', Numeric)
    EntranceLongitude = Column('entrance_longitude', Numeric)
    GeoChargingPointEntrance = Column('queriable_entrance_geocoordinates', Unicode)
    lastUpdate = Column('last_modified', Date)
    IsOpen24Hours = Column('is_open_24_hours', Boolean)
    OpeningTimes = Column('opening_times', Boolean)
    OperatorID = Column('operator_id', Unicode)
    HubOperatorId = Column('hub_operator_id', Unicode)
    ClearinghouseID = Column('clearing_house_id', Unicode)
    OperatorName = Column('operator_name', Unicode)
    HotlinePhoneNumber = Column('hotline_phone_num', Unicode)
    ProviderURL = Column('provider_url', Unicode)
    the_geom = Column(Geometry2D)

register(DiemoLocations.__bodId__, DiemoLocations)
