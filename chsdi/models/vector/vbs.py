# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer, Float

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D, Geometry3D

Base = bases['vbs']


class Kulturgueter(Base, Vector):
    __tablename__ = 'kgs'
    __table_args__ = ({'schema': 'babs', 'autoload': False})
    __template__ = 'templates/htmlpopup/kgs.mako'
    __bodId__ = 'ch.babs.kulturgueter'
    __queryable_attributes__ = ['zkob']
    __extended_info__ = True
    __label__ = 'zkob'
    id = Column('kgs_nr', Integer, primary_key=True)
    zkob = Column('zkob', Unicode)
    x = Column('x', Float)
    y = Column('y', Float)
    kategorie = Column('kategorie', Unicode)
    gemeinde = Column('gemeinde', Unicode)
    gemeinde_ehemalig = Column('gemeinde_ehemalig', Unicode)
    objektart = Column('objektart', Unicode)
    hausnr = Column('hausnr', Unicode)
    adresse = Column('adresse', Unicode)
    kurztexte = Column('kurztexte', Unicode)
    kt_kz = Column('kt_kz', Unicode)
    pdf_list = Column('pdf_list', Unicode)
    link_uri = Column('link_uri', Unicode)
    link_title = Column('link_title', Unicode)
    link_2_uri = Column('link_2_uri', Unicode)
    link_2_title = Column('link_2_title', Unicode)
    link_3_uri = Column('link_3_uri', Unicode)
    link_3_title = Column('link_3_title', Unicode)
    the_geom = Column(Geometry2D)

register('ch.babs.kulturgueter', Kulturgueter)


class TERRITORIALREGIONEN(Base, Vector):
    __tablename__ = 'territorialregionen'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/territorialregionen.mako'
    __bodId__ = 'ch.vbs.territorialregionen'
    __label__ = 'name'
    id = Column('terreg_nr', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry3D)

register('ch.vbs.territorialregionen', TERRITORIALREGIONEN)


class Patrouilledesglaciers_z(Base, Vector):
    __tablename__ = 'patrouille_z'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/patrouilledesglaciers_z.mako'
    __bodId__ = 'ch.vbs.patrouilledesglaciers-z_rennen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry3D)

register('ch.vbs.patrouilledesglaciers-z_rennen', Patrouilledesglaciers_z)


class Patrouilledesglaciers_a(Base, Vector):
    __tablename__ = 'patrouille_a'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/patrouilledesglaciers_a.mako'
    __bodId__ = 'ch.vbs.patrouilledesglaciers-a_rennen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry3D)

register('ch.vbs.patrouilledesglaciers-a_rennen', Patrouilledesglaciers_a)


class Retablierungsstellen(Base, Vector):
    __tablename__ = 'retablierungsstellen'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/retablierungsstellen.mako'
    __bodId__ = 'ch.vbs.retablierungsstellen'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    url = Column('url', Unicode)
    the_geom = Column(Geometry3D)

register('ch.vbs.retablierungsstellen', Retablierungsstellen)


class Armeelogistikcenter(Base, Vector):
    __tablename__ = 'armeelogistikcenter'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/armeelogistikcenter.mako'
    __bodId__ = 'ch.vbs.armeelogistikcenter'
    __queryable_attributes__ = ['name', 'abkuerzung']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    abkuerzung = Column('abkuerzung', Unicode)
    mail = Column('email', Unicode)
    url = Column('url', Unicode)
    the_geom = Column(Geometry3D)

register('ch.vbs.armeelogistikcenter', Armeelogistikcenter)


class Bundestankstellen_bebeco(Base, Vector):
    __tablename__ = 'bundestankstellen_bebeco'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/bundestankstellen.mako'
    __bodId__ = 'ch.vbs.bundestankstellen-bebeco'
    __queryable_attributes__ = ['ort', 'plz', 'strasse']
    __label__ = 'ort'
    id = Column('bgdi_id', Integer, primary_key=True)
    strasse = Column('strasse', Unicode)
    plz = Column('plz', Integer)
    ort = Column('ort', Unicode)
    the_geom = Column(Geometry3D)

register('ch.vbs.bundestankstellen-bebeco', Bundestankstellen_bebeco)


class Logistikraeume_armeelogistikcenter(Base, Vector):
    __tablename__ = 'abschnittsregionen_armeelogistikzentren'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/logistikraeume.mako'
    __bodId__ = 'ch.vbs.logistikraeume-armeelogistikcenter'
    __queryable_attributes__ = ['kanton', 'region']
    __label__ = 'kanton'
    id = Column('bgdi_id', Integer, primary_key=True)
    kanton = Column('kantone', Unicode)
    region = Column('region', Unicode)
    the_geom = Column(Geometry3D)

register('ch.vbs.logistikraeume-armeelogistikcenter', Logistikraeume_armeelogistikcenter)


class Waldschaden(Base, Vector):
    __tablename__ = 'projektil'
    __table_args__ = ({'schema': 'wascha', 'autoload': False})
    __template__ = 'templates/htmlpopup/waldschadenkarte.mako'
    __bodId__ = 'ch.vbs.waldschadenkarte'
    __queryable_attributes__ = ['lauf_nr', 'jahr_schad', 'gde_name', 'lokalname', 'x_koord', 'y_koord']
    __label__ = 'lauf_nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    lauf_nr = Column('lauf_nr', Unicode)
    jahr_schad = Column('jahr_schad', Unicode)
    gde_name = Column('gde_name', Unicode)
    lokalname = Column('lokalname', Unicode)
    x_koord = Column('x_koord', Integer)
    y_koord = Column('y_koord', Integer)

register('ch.vbs.waldschadenkarte', Waldschaden)


class SimFacilities:
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_facilities.mako'
    id = Column('stabil_id', Unicode, primary_key=True)
    facility = Column('facility', Unicode)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    doc_web = Column('doc_web', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)


class SimFacilitiesA(Base, SimFacilities, Vector):
    __tablename__ = 'sim_fac_anhoerung'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_anhoerung'

register('ch.vbs.sachplan-infrastruktur-militaer_anhoerung', SimFacilitiesA)


class SimFacilitiesK(Base, SimFacilities, Vector):
    __tablename__ = 'sim_fac_kraft'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'

register('ch.vbs.sachplan-infrastruktur-militaer_kraft', SimFacilitiesK)


class SimPlanning:
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/sim_planning.mako'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    doc_web = Column('doc_web', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)


class SimPlanningK(Base, SimPlanning, Vector):
    __tablename__ = 'sim_pl_kraft'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'
    __minscale__ = 20005
    __maxscale__ = 500005

register('ch.vbs.sachplan-infrastruktur-militaer_kraft', SimPlanningK)


class SimPlanningA(Base, SimPlanning, Vector):
    __tablename__ = 'sim_pl_anhoerung'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_anhoerung'
    __minscale__ = 20005
    __maxscale__ = 500005

register('ch.vbs.sachplan-infrastruktur-militaer_anhoerung', SimPlanningA)


class SimPlanningRasterA(Base, SimPlanning, Vector):
    __tablename__ = 'sim_pl_r_anhoerung'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_anhoerung'
    __maxscale__ = 20005
    __minscale__ = 1

register('ch.vbs.sachplan-infrastruktur-militaer_anhoerung', SimPlanningRasterA)


class SimPlanningRasterK(Base, SimPlanning, Vector):
    __tablename__ = 'sim_pl_r_kraft'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'
    __maxscale__ = 20005
    __minscale__ = 1

register('ch.vbs.sachplan-infrastruktur-militaer_kraft', SimPlanningRasterK)
