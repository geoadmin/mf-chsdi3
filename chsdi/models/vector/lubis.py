# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Boolean, Numeric, Date
from sqlalchemy.types import Unicode
from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['lubis']


class LuftbilderBase:
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __label__ = 'flugdatum'
    id = Column('ebkey', Unicode, primary_key=True)
    filename = Column('filename', Unicode)
    flugdatum = Column('flugdatum', Unicode)
    firma = Column('firma', Unicode)
    filmart = Column('filmart', Unicode)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    orthophoto = Column('orthophoto', Unicode)
    originalsize = Column('originalsize', Unicode)
    x = Column('x', Integer)
    y = Column('y', Integer)
    flughoehe = Column('flughoehe', Integer)
    bgdi_imagemode = Column('bgdi_imagemode', Unicode)
    the_geom_footprint = Column('the_geom_footprint', Geometry2D)
    the_geom = Column(Geometry2D)


class LuftbilderBaseDritte(LuftbilderBase):
    __template__ = 'templates/htmlpopup/lubis.mako'
    inventarnummer = Column('inventarnummer', Integer)
    bildnummer = Column('bildnummer', Unicode)
    orientierung = Column('orientierung', Boolean)
    rotation = Column('rotation', Integer)
    ort = Column('ort', Unicode)
    massstab = Column('massstab', Integer)
    filesize_mb = Column('filesize_mb', Unicode)


class LuftbilderBaseSwisstopo(LuftbilderBase):
    __template__ = 'templates/htmlpopup/lubis_stac.mako'
    ebkey_old = Column('ebkey_old', Unicode)
    feature_id = Column('feature_id', Unicode)
    acquired = Column('acquired', Date)
    film_type = Column('film_type', Unicode)
    orthofilename = Column('orthofilename', Unicode)
    e = Column('e', Numeric)
    n = Column('n', Numeric)
    z = Column('z', Numeric)


class LuftbilderSwisstopoFarbe(Base, LuftbilderBaseSwisstopo, Vector):
    __tablename__ = 'luftbilder_swisstopo_color'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_farbe'

register('ch.swisstopo.lubis-luftbilder_farbe', LuftbilderSwisstopoFarbe)


class LuftbilderSwisstopoIr(Base, LuftbilderBaseSwisstopo, Vector):
    __tablename__ = 'luftbilder_swisstopo_ir'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_infrarot'

register('ch.swisstopo.lubis-luftbilder_infrarot', LuftbilderSwisstopoIr)


class LuftbilderSwisstopoSw(Base, LuftbilderBaseSwisstopo, Vector):
    __tablename__ = 'luftbilder_swisstopo_bw'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_schwarzweiss'

register('ch.swisstopo.lubis-luftbilder_schwarzweiss', LuftbilderSwisstopoSw)


class LuftbilderDritteFirmen(Base, LuftbilderBaseDritte, Vector):
    __tablename__ = 'luftbilder_dritte_firmen'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder-dritte-firmen'
    contact = Column('contact', Unicode)
    contact_email = Column('contact_email', Unicode)
    contact_web = Column('contact_web', Unicode)
    doi_link = Column('doi_link', Unicode)

register('ch.swisstopo.lubis-luftbilder-dritte-firmen', LuftbilderDritteFirmen)


class LuftbilderDritteKantone(Base, LuftbilderBaseDritte, Vector):
    __tablename__ = 'luftbilder_dritte_kantone'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder-dritte-kantone'
    contact = Column('contact', Unicode)
    contact_email = Column('contact_email', Unicode)
    contact_web = Column('contact_web', Unicode)
    contact_image_url = Column('url', Unicode)

register('ch.swisstopo.lubis-luftbilder-dritte-kantone', LuftbilderDritteKantone)


class Bildstreifen(Base, Vector):
    __tablename__ = 'view_bildstreifen'
    __table_args__ = ({'schema': 'ads40', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis_bildstreifen.mako'
    __bodId__ = 'ch.swisstopo.lubis-bildstreifen'
    __returnedGeometry__ = 'the_geom_footprint'
    __timeInstant__ = 'bgdi_flugjahr'
    __extended_info__ = True
    # Composite labels
    __label__ = 'flugdatum'
    id = Column('bildstreifen_nr', Unicode, primary_key=True)
    flugdatum = Column('flugdatum', Unicode)
    firma = Column('firma', Unicode)
    filmart = Column('filmart', Unicode)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    resolution = Column('resolution', Unicode)
    objectid = Column('objectid', Unicode)
    area = Column('area', Unicode)
    gsd = Column('gsd', Numeric)
    toposhop_length = Column('toposhop_length', Numeric)
    toposhop_start_x = Column('toposhop_start_x', Integer)
    toposhop_start_y = Column('toposhop_start_y', Integer)
    toposhop_end_x = Column('toposhop_end_x', Integer)
    toposhop_end_y = Column('toposhop_end_y', Integer)
    toposhop_date = Column('toposhop_date', Unicode)
    goal = Column('goal', Unicode)
    source_georef = Column('georef_source', Unicode)
    the_geom_footprint = Column('the_geom_footprint', Geometry2D)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.lubis-bildstreifen', Bildstreifen)


class LuftbilderSchraegaufnahmen(Base, Vector):
    __tablename__ = 'view_bilder'
    __table_args__ = ({'schema': 'swisstopo_oblique', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis_schraegaufnahmen.mako'
    __bodId__ = 'ch.swisstopo.lubis-luftbilder_schraegaufnahmen'
    __timeInstant__ = 'bgdi_flugjahr'
    __label__ = 'flightdate'
    id = Column('ebkey', Unicode, primary_key=True)
    ebkey_old = Column('ebkey_old', Unicode)
    flightdate = Column('flightdate', Unicode)
    filename = Column('filename', Unicode)
    filmart = Column('filmart', Unicode)
    stereo_couple = Column('stereo_couple', Unicode)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    x = Column('x', Integer)
    y = Column('y', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.lubis-luftbilder_schraegaufnahmen', LuftbilderSchraegaufnahmen)


class LuftbilderTerrA(Base, Vector):
    __tablename__ = 'view_bilder'
    __table_args__ = ({'schema': 'swisstopo_terrestrial', 'autoload': False})
    __template__ = 'templates/htmlpopup/lubis_terra.mako'
    __bodId__ = 'ch.swisstopo.lubis-terrestrische_aufnahmen'
    __timeInstant__ = 'bgdi_flugjahr'
    __returnedGeometry__ = 'the_geom_footprint'
    __label__ = 'flugdatum'
    id = Column('inventory_number', Unicode, primary_key=True)
    inventarnummer_old = Column('inventarnummer_old', Unicode)
    inventarnummer = Column('objectid', Integer)
    flugdatum = Column('bgdi_flugdatum', Unicode)
    bgdi_flugjahr = Column('year', Integer)
    filmart = Column('filmart', Unicode)
    ort = Column('operate_name', Unicode)
    station = Column('station', Unicode)
    base_uuid = Column('base_uuid', Unicode)
    x = Column('easting', Numeric)
    y = Column('northing', Numeric)
    filename = Column('filename', Unicode)
    bgdi_imagemode = Column('bgdi_imagemode', Unicode)
    smapshot_id = Column('smapshot_id', Integer)
    expert_sheet_url = Column('expert_sheet_url', Unicode)
    the_geom_footprint = Column('the_geom_footprint', Geometry2D)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.lubis-terrestrische_aufnahmen', LuftbilderTerrA)
