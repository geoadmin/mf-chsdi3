# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer, Boolean, Numeric

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D, Geometry3D

Base = bases['lubis']


class luftbilder_swisstopo_farbe(Base, Vector):
    __tablename__ = 'luftbilder_swisstopo_color'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_farbe'
    __queryable_attributes__ = ['id', 'ort']
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flugdatum'
    id = Column('ebkey', Text, primary_key=True)
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
    image_height = Column('image_height', Integer)
    image_width = Column('image_width', Integer)
    the_geom_footprint = Column('the_geom_footprint', Geometry3D)
    the_geom = Column(Geometry3D)

register('ch.swisstopo.lubis-luftbilder_farbe', luftbilder_swisstopo_farbe)


class luftbilder_swisstopo_ir(Base, Vector):
    __tablename__ = 'luftbilder_swisstopo_ir'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/lubis.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_infrarot'
    __queryable_attributes__ = ['id', 'ort']
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flugdatum'
    id = Column('ebkey', Text, primary_key=True)
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
    image_height = Column('image_height', Integer)
    image_width = Column('image_width', Integer)
    the_geom_footprint = Column('the_geom_footprint', Geometry3D)
    the_geom = Column(Geometry3D)

register('ch.swisstopo.lubis-luftbilder_infrarot', luftbilder_swisstopo_ir)


class luftbilder_swisstopo_sw(Base, Vector):
    __tablename__ = 'luftbilder_swisstopo_bw'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/lubis.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_schwarzweiss'
    __queryable_attributes__ = ['id', 'ort', 'filmart', 'bgdi_flugjahr']
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flugdatum'
    id = Column('ebkey', Text, primary_key=True)
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
    image_height = Column('image_height', Integer)
    image_width = Column('image_width', Integer)
    the_geom_footprint = Column('the_geom_footprint', Geometry3D)
    the_geom = Column(Geometry3D)

register('ch.swisstopo.lubis-luftbilder_schwarzweiss', luftbilder_swisstopo_sw)


class luftbilder_dritte_firmen(Base, Vector):
    __tablename__ = 'luftbilder_dritte_firmen'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder-dritte-firmen'
    __queryable_attributes__ = ['id', 'ort', 'filmart', 'bgdi_flugjahr']
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flugdatum'
    id = Column('ebkey', Text, primary_key=True)
    filename = Column('filename', Text)
    inventarnummer = Column('inventarnummer', Integer)
    bildnummer = Column('bildnummer', Integer)
    flugdatum = Column('flugdatum', Text)
    firma = Column('firma', Text)
    filmart = Column('filmart', Text)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    orientierung = Column('orientierung', Boolean)
    originalsize = Column('originalsize', Text)
    orthophoto = Column('orthophoto', Text)
    rotation = Column('rotation', Integer)
    x = Column('x', Integer)
    y = Column('y', Integer)
    flughoehe = Column('flughoehe', Integer)
    ort = Column('ort', Text)
    massstab = Column('massstab', Integer)
    filesize_mb = Column('filesize_mb', Text)
    contact = Column('contact', Text)
    contact_email = Column('contact_email', Text)
    contact_web = Column('contact_web', Text)
    bgdi_imagemode = Column('bgdi_imagemode', Text)
    the_geom_footprint = Column('the_geom_footprint', Geometry2D)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.lubis-luftbilder-dritte-firmen', luftbilder_dritte_firmen)


class luftbilder_dritte_kantone(Base, Vector):
    __tablename__ = 'luftbilder_dritte_kantone'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder-dritte-kantone'
    __queryable_attributes__ = ['id', 'ort', 'filmart', 'bgdi_flugjahr']
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flugdatum'
    id = Column('ebkey', Text, primary_key=True)
    filename = Column('filename', Text)
    inventarnummer = Column('inventarnummer', Integer)
    bildnummer = Column('bildnummer', Integer)
    flugdatum = Column('flugdatum', Text)
    firma = Column('firma', Text)
    filmart = Column('filmart', Text)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    orientierung = Column('orientierung', Boolean)
    originalsize = Column('originalsize', Text)
    orthophoto = Column('orthophoto', Text)
    rotation = Column('rotation', Integer)
    x = Column('x', Integer)
    y = Column('y', Integer)
    flughoehe = Column('flughoehe', Integer)
    ort = Column('ort', Text)
    massstab = Column('massstab', Integer)
    filesize_mb = Column('filesize_mb', Text)
    contact = Column('contact', Text)
    contact_email = Column('contact_email', Text)
    contact_web = Column('contact_web', Text)
    bgdi_imagemode = Column('bgdi_imagemode', Text)
    the_geom_footprint = Column('the_geom_footprint', Geometry2D)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.lubis-luftbilder-dritte-kantone', luftbilder_dritte_kantone)


class bildstreifen(Base, Vector):
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
    id = Column('bildstreifen_nr', Text, primary_key=True)
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

register('ch.swisstopo.lubis-bildstreifen', bildstreifen)


class LuftbilderSchraegaufnahmen(Base, Vector):
    __tablename__ = 'view_bilder'
    __table_args__ = ({'schema': 'swisstopo_oblique', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis_schraegaufnahmen.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_schraegaufnahmen'
    __timeInstant__ = 'bgdi_flugjahr'
    # Composite labels
    __label__ = 'flightdate'
    __queryable_attributes__ = ['id', 'bgdi_flugjahr', 'medium_format']
    id = Column('ebkey', Text, primary_key=True)
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
