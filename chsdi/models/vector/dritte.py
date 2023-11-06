# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer
from sqlalchemy.types import Numeric

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D

Base = bases['dritte']


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


class AsylFacilities:
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_facilities.mako'
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


class AsylFacilitiesAnhoerung(Base, AsylFacilities, Vector):
    __tablename__ = 'sachplan_asyl_facilities_anhorung'
    __bodId__ = 'ch.sem.sachplan-asyl_anhoerung'


class AsylFacilitiesKraft(Base, AsylFacilities, Vector):
    __tablename__ = 'sachplan_asyl_facilities_kraft'
    __bodId__ = 'ch.sem.sachplan-asyl_kraft'


register('ch.sem.sachplan-asyl_anhoerung', AsylFacilitiesAnhoerung)
register('ch.sem.sachplan-asyl_kraft', AsylFacilitiesKraft)


class AsylPlanning:
    __table_args__ = ({'schema': 'sem', 'autoload': False})
    __template__ = 'templates/htmlpopup/asyl_planning.mako'
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
    the_geom = Column(Geometry2D)


class AsylPlanningAnhoerung(Base, AsylPlanning, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_anhorung'
    __bodId__ = 'ch.sem.sachplan-asyl_anhoerung'
    __minscale__ = 20005
    __maxscale__ = 500005


class AsylPlanningRasterAnhoerung(Base, AsylPlanning, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_r_anhorung'
    __bodId__ = 'ch.sem.sachplan-asyl_anhoerung'
    __maxscale__ = 20005
    __minscale__ = 1


class AsylPlanningKraft(Base, AsylPlanning, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_kraft'
    __bodId__ = 'ch.sem.sachplan-asyl_kraft'
    __minscale__ = 20005
    __maxscale__ = 500005


class AsylPlanningRasterKraft(Base, AsylPlanning, Vector):
    __tablename__ = 'sachplan_asyl_plmeasures_r_kraft'
    __bodId__ = 'ch.sem.sachplan-asyl_kraft'
    __maxscale__ = 20005
    __minscale__ = 1


register('ch.sem.sachplan-asyl_anhoerung', AsylPlanningAnhoerung)
register('ch.sem.sachplan-asyl_anhoerung', AsylPlanningRasterAnhoerung)
register('ch.sem.sachplan-asyl_kraft', AsylPlanningKraft)
register('ch.sem.sachplan-asyl_kraft', AsylPlanningRasterKraft)
