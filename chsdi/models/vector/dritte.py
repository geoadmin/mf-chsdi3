# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer, Float
from sqlalchemy.types import Numeric

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['dritte']


class MaechtigkeitLockergesteine(Base, Vector):
    __tablename__ = 'maechtigkeit_lockergesteine'
    __table_args__ = ({'schema': 'sgpk', 'autoload': False})
    __template__ = 'templates/htmlpopup/maechtigkeit_lockergesteine.mako'
    __bodId__ = 'ch.sgpk.maechtigkeit-lockergesteine'
    __label__ = 'id'
    id = Column('id', Integer, primary_key=True)
    maechtigkeit = Column('maechtigkeit', Numeric)
    the_geom = Column(Geometry2D)

register('ch.sgpk.maechtigkeit-lockergesteine', MaechtigkeitLockergesteine)


class MobilityStandorte:
    __tablename__ = 'standorte_tooltip'
    __table_args__ = ({'schema': 'mobility', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/mobility_standorte.mako'
    __bodId__ = 'ch.mobility.standorte'
    __label__ = 'name'
    __returnedGeometry__ = 'the_geom_point'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    number = Column('number', Integer)
    location = Column('location', Unicode)
    lat = Column('lat', Float)
    lon = Column('lon', Float)
    street = Column('street', Unicode)
    city = Column('city', Unicode)
    categories = Column('categories', Unicode)
    the_geom_point = Column('the_geom', Geometry2D)


class MobilityStandorteZoom1(Base, MobilityStandorte, Vector):
    __minscale__ = 1
    __maxscale__ = 4000
    the_geom = Column('the_geom_click', Geometry2D)

register(MobilityStandorte.__bodId__, MobilityStandorteZoom1)


class MobilityStandorteZoom2(Base, MobilityStandorte, Vector):
    __minscale__ = 4000
    the_geom = Column('the_geom_click_overview', Geometry2D)

register(MobilityStandorte.__bodId__, MobilityStandorteZoom2)


class Notfallschutz(Base, Vector):
    __tablename__ = 'zonenplan_kernanlagen'
    __table_args__ = ({'schema': 'ensi', 'autoload': False})
    __template__ = 'templates/htmlpopup/zonenplan_kernanlagen.mako'
    __bodId__ = 'ch.ensi.zonenplan-notfallschutz-kernanlagen'
    __label__ = 'name'
    id = Column('nr', Integer, primary_key=True)
    name = Column('name', Unicode)
    zone = Column('zone', Unicode)
    sektor = Column('sektor', Unicode)
    the_geom = Column(Geometry2D)

register('ch.ensi.zonenplan-notfallschutz-kernanlagen', Notfallschutz)


class PronaturaWaldreservate(Base, Vector):
    __tablename__ = 'waldreservate'
    __table_args__ = ({'schema': 'pronatura', 'autoload': False})
    __template__ = 'templates/htmlpopup/pronatura.mako'
    __bodId__ = 'ch.pronatura.waldreservate'
    __queryable_attributes__ = ['name', 'objnummer', 'gesflaeche', 'gesflaeche', 'gisteilobjekt', 'mcpfe']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Integer)
    name = Column('name', Unicode)
    gisflaeche = Column('obj_gisflaeche', Float)
    gesflaeche = Column('obj_gesflaeche', Float)
    gisteilobjekt = Column('obj_gisteilobjekt', Float)
    mcpfe = Column('mcpfe', Unicode)
    the_geom = Column(Geometry2D)

register(PronaturaWaldreservate.__bodId__, PronaturaWaldreservate)


class PronaturaNaturschutzgebiete(Base, Vector):
    __tablename__ = 'naturschutzgebiete'
    __table_args__ = ({'schema': 'pronatura', 'autoload': False})
    __template__ = 'templates/htmlpopup/pronatura_schutzge.mako'
    __bodId__ = 'ch.pronatura.naturschutzgebiete'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    nummer = Column('nummer', Integer)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.pronatura.naturschutzgebiete', PronaturaNaturschutzgebiete)


class AeromagnetischeKarte1500(Base, Vector):
    __tablename__ = 'am_1500'
    __table_args__ = ({'schema': 'nagra', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetische_karte.mako'
    __bodId__ = 'ch.nagra.aeromagnetische-karte_1500'
    __label__ = 'id'
    id = Column('et_id', Integer, primary_key=True)
    et_fromatt_1500 = Column('et_fromatt_1500', Numeric)
    the_geom = Column(Geometry2D)

register('ch.nagra.aeromagnetische-karte_1500', AeromagnetischeKarte1500)


class AeromagnetischeKarte1100(Base, Vector):
    __tablename__ = 'am_1100'
    __table_args__ = ({'schema': 'nagra', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetische_karte.mako'
    __bodId__ = 'ch.nagra.aeromagnetische-karte_1100'
    __label__ = 'id'
    id = Column('et_id', Integer, primary_key=True)
    et_fromatt_1100 = Column('et_fromatt_1100', Numeric)
    the_geom = Column(Geometry2D)


register('ch.nagra.aeromagnetische-karte_1100', AeromagnetischeKarte1100)


class AsylFacilitiesA(Base, Vector):
    __tablename__ = 'sachplan_asyl_facilities_anhorung'
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_facilities.mako'
    __bodId__ = 'ch.sem.sachplan-asyl_anhoerung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    kindid = Column('kindid', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)
    statusid = Column('statusid', Unicode)
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    objectname_de = Column('objectname_de', Unicode)
    objectname_fr = Column('objectname_fr', Unicode)
    objectname_it = Column('objectname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)


class AsylPlanningA(Base, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_anhorung'
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_planning.mako'
    __bodId__ = 'ch.sem.sachplan-asyl_anhoerung'
    # Translatable labels in fr, it
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_bid = Column('coordlevel_bid', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    objectname_de = Column('objectname_de', Unicode)
    objectname_fr = Column('objectname_fr', Unicode)
    objectname_it = Column('objectname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)


class AsylPlanningRasterA(Base, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_r_anhorung'
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_planning.mako'
    __bodId__ = 'ch.sem.sachplan-asyl_anhoerung'
    # Translatable labels in fr, it
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_bid = Column('coordlevel_bid', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    objectname_de = Column('objectname_de', Unicode)
    objectname_fr = Column('objectname_fr', Unicode)
    objectname_it = Column('objectname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.sem.sachplan-asyl_anhoerung', AsylFacilitiesA)
register('ch.sem.sachplan-asyl_anhoerung', AsylPlanningA)
register('ch.sem.sachplan-asyl_anhoerung', AsylPlanningRasterA)


class AsylFacilitiesK(Base, Vector):
    __tablename__ = 'sachplan_asyl_facilities_kraft'
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_facilities.mako'
    __bodId__ = 'ch.sem.sachplan-asyl_kraft'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    kindid = Column('kindid', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)
    statusid = Column('statusid', Unicode)
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    objectname_de = Column('objectname_de', Unicode)
    objectname_fr = Column('objectname_fr', Unicode)
    objectname_it = Column('objectname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)


class AsylPlanningK(Base, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_kraft'
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_planning.mako'
    __bodId__ = 'ch.sem.sachplan-asyl_kraft'
    # Translatable labels in fr, it
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_bid = Column('coordlevel_bid', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    objectname_de = Column('objectname_de', Unicode)
    objectname_fr = Column('objectname_fr', Unicode)
    objectname_it = Column('objectname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    #  __minscale__ = 20005
    #  __maxscale__ = 500005
    the_geom = Column(Geometry2D)


class AsylPlanningRasterK(Base, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_r_kraft'
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_planning.mako'
    __bodId__ = 'ch.sem.sachplan-asyl_kraft'
    # Translatable labels in fr, it
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_bid = Column('coordlevel_bid', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    objectname_de = Column('objectname_de', Unicode)
    objectname_fr = Column('objectname_fr', Unicode)
    objectname_it = Column('objectname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    #  __maxscale__ = 20005
    #  __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.sem.sachplan-asyl_kraft', AsylFacilitiesK)
register('ch.sem.sachplan-asyl_kraft', AsylPlanningK)
register('ch.sem.sachplan-asyl_kraft', AsylPlanningRasterK)
