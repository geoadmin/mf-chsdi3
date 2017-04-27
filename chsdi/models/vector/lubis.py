# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer, Boolean, Numeric
from sqlalchemy.types import Unicode
from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry3D

Base = bases['lubis']


class LuftbilderBase:
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis.mako'
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    __label__ = 'flugdatum'
    id = Column('ebkey', Unicode, primary_key=True)
    filename = Column('filename', Text)
    inventarnummer = Column('inventarnummer', Integer)
    bildnummer = Column('bildnummer', Integer)
    flugdatum = Column('flugdatum', Text)
    firma = Column('firma', Text)
    filmart = Column('filmart', Text)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    orientierung = Column('orientierung', Boolean)
    rotation = Column('rotation', Integer)
    orthophoto = Column('orthophoto', Text)
    originalsize = Column('originalsize', Text)
    x = Column('x', Integer)
    y = Column('y', Integer)
    flughoehe = Column('flughoehe', Integer)
    ort = Column('ort', Text)
    massstab = Column('massstab', Integer)
    filesize_mb = Column('filesize_mb', Text)
    bgdi_imagemode = Column('bgdi_imagemode', Text)
    the_geom_footprint = Column('the_geom_footprint', Geometry3D)
    the_geom = Column(Geometry3D)


class LuftbilderSwisstopoFarbe(Base, LuftbilderBase, Vector):
    __tablename__ = 'luftbilder_swisstopo_color'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_farbe'
    __queryable_attributes__ = ['id', 'ort']
    image_height = Column('image_height', Integer)
    image_width = Column('image_width', Integer)

register('ch.swisstopo.lubis-luftbilder_farbe', LuftbilderSwisstopoFarbe)


class LuftbilderSwisstopoIr(Base, LuftbilderBase, Vector):
    __tablename__ = 'luftbilder_swisstopo_ir'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_infrarot'
    __queryable_attributes__ = ['id', 'ort']
    image_height = Column('image_height', Integer)
    image_width = Column('image_width', Integer)

register('ch.swisstopo.lubis-luftbilder_infrarot', LuftbilderSwisstopoIr)


class LuftbilderSwisstopoSw(Base, LuftbilderBase, Vector):
    __tablename__ = 'luftbilder_swisstopo_bw'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_schwarzweiss'
    __queryable_attributes__ = ['id', 'ort', 'filmart', 'bgdi_flugjahr']
    image_height = Column('image_height', Integer)
    image_width = Column('image_width', Integer)

register('ch.swisstopo.lubis-luftbilder_schwarzweiss', LuftbilderSwisstopoSw)


class LuftbilderDritteFirmen(Base, LuftbilderBase, Vector):
    __tablename__ = 'luftbilder_dritte_firmen'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder-dritte-firmen'
    __queryable_attributes__ = ['id', 'ort', 'filmart', 'bgdi_flugjahr']
    contact = Column('contact', Text)
    contact_email = Column('contact_email', Text)
    contact_web = Column('contact_web', Text)

register('ch.swisstopo.lubis-luftbilder-dritte-firmen', LuftbilderDritteFirmen)


class LuftbilderDritteKantone(Base, LuftbilderBase, Vector):
    __tablename__ = 'luftbilder_dritte_kantone'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder-dritte-kantone'
    __queryable_attributes__ = ['id', 'ort', 'filmart', 'bgdi_flugjahr']
    contact = Column('contact', Text)
    contact_email = Column('contact_email', Text)
    contact_web = Column('contact_web', Text)
    contact_image_url = Column('url', Text)

register('ch.swisstopo.lubis-luftbilder-dritte-kantone', LuftbilderDritteKantone)


class Bildstreifen(Base, Vector):
    __tablename__ = 'view_bildstreifen'
    __table_args__ = ({'schema': 'ads40', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis_bildstreifen.mako'
    __bodId__ = 'ch.swisstopo.lubis-bildstreifen'
    __queryable_attributes__ = ['id']
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flugdatum'
    id = Column('bildstreifen_nr', Unicode, primary_key=True)
    flugdatum = Column('flugdatum', Text)
    firma = Column('firma', Text)
    filmart = Column('filmart', Text)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    resolution = Column('resolution', Text)
    objectid = Column('objectid', Text)
    area = Column('area', Text)
    gsd = Column('gsd', Numeric)
    toposhop_length = Column('toposhop_length', Numeric)
    toposhop_start_x = Column('toposhop_start_x', Integer)
    toposhop_start_y = Column('toposhop_start_y', Integer)
    toposhop_end_x = Column('toposhop_end_x', Integer)
    toposhop_end_y = Column('toposhop_end_y', Integer)
    toposhop_date = Column('toposhop_date', Text)
    goal = Column('goal', Text)
    source_georef = Column('georef_source', Text)
    the_geom_footprint = Column('the_geom_footprint', Geometry3D)
    the_geom = Column(Geometry3D)

register('ch.swisstopo.lubis-bildstreifen', Bildstreifen)


class LuftbilderSchraegaufnahmen(Base, Vector):
    __tablename__ = 'view_bilder'
    __table_args__ = ({'schema': 'swisstopo_oblique', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis_schraegaufnahmen.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_schraegaufnahmen'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flightdate'
    __queryable_attributes__ = ['id', 'bgdi_flugjahr', 'medium_format']
    id = Column('ebkey', Unicode, primary_key=True)
    inventory_number = Column('inventory_number', Text)
    flightdate = Column('flightdate', Text)
    medium_format = Column('medium_format', Text)
    filesize_mb = Column('filesize_mb', Text)
    filename = Column('filename', Text)
    stereo_couple = Column('stereo_couple', Text)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    x = Column('x', Integer)
    y = Column('y', Integer)
    contact = Column('contact', Text)
    contact_email = Column('contact_email', Text)
    the_geom = Column(Geometry3D)

register('ch.swisstopo.lubis-luftbilder_schraegaufnahmen', LuftbilderSchraegaufnahmen)
