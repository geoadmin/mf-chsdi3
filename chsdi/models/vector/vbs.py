# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer, Float, Boolean

from sqlalchemy.dialects import postgresql
from chsdi.models.types import DateTimeChsdi

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D, Geometry3D

Base = bases['vbs']


class Kulturgueter(Base, Vector):
    __tablename__ = 'kgs'
    __table_args__ = ({'schema': 'babs', 'autoload': False})
    __template__ = 'templates/htmlpopup/kgs.mako'
    __bodId__ = 'ch.babs.kulturgueter'
    __extended_info__ = True
    __label__ = 'beschreibung'
    id = Column('objekt_nr', Integer, primary_key=True)
    kgs_nr = Column('kgs_nr', Unicode)
    beschreibung = Column('beschreibung', Unicode)
    x = Column('x', Integer)
    y = Column('y', Integer)
    gemeinde = Column('gemeinde', Unicode)
    kanton = Column('kanton', Unicode)
    kgs_kategorie = Column('kgs_kategorie', Unicode)
    ehemaligegemeinde = Column('ehemaligegemeinde', Unicode)
    adresse_list = Column('adresse_list', Unicode)
    objektart_de_list = Column('objektart_de_list', Unicode)
    objektart_fr_list = Column('objektart_fr_list', Unicode)
    objektart_it_list = Column('objektart_it_list', Unicode)
    pdf_files_list = Column('pdf_files_list', Unicode)
    weblinks_list = Column('weblinks_list', Unicode)
    bemerkung_list = Column('bemerkung_list', Unicode)
    bild_nr_list = Column('bild_nr_list', Unicode)
    bild_url_list = Column('bild_url_list', Unicode)
    copyright = Column('copyright', Unicode)
    fotograf = Column('fotograf', Unicode)
    kurztext = Column('kurztext', Unicode)
    the_geom = Column(Geometry2D)

register(Kulturgueter.__bodId__, Kulturgueter)


class NationalesSportanlagenkonzept(Base, Vector):
    __tablename__ = 'nationales_sportanlagenkonzept'
    __table_args__ = ({'schema': 'baspo', 'autoload': False})
    __template__ = 'templates/htmlpopup/nationales_sportanlagenkonzept.mako'
    __bodId__ = 'ch.baspo.nationales-sportanlagenkonzept'
    __label__ = 'name_der_anlage'
    id = Column('bgdi_id', Integer, primary_key=True)
    nasak_nr = Column('nasak_nr', Unicode, nullable=False)
    kategorie_de = Column('kategorie_de', Unicode, nullable=False)
    sportaktivitaet = Column('art_der_anlage', Unicode, nullable=False)
    name_der_anlage = Column('name_der_anlage', Unicode, nullable=False)
    ort = Column('ort', Unicode, nullable=False)
    website = Column('website', Unicode, nullable=False, default=u'')
    the_geom = Column(Geometry2D)

register(NationalesSportanlagenkonzept.__bodId__, NationalesSportanlagenkonzept)


class Territorialregionen(Base, Vector):
    __tablename__ = 'territorialregionen'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/territorialregionen.mako'
    __bodId__ = 'ch.vbs.territorialregionen'
    __label__ = 'name'
    id = Column('terreg_nr', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register(Territorialregionen.__bodId__, Territorialregionen)


class SchiessAnzeigen(Base, Vector):
    __tablename__ = 'schiessanzeigen'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/schiessanzeigen.mako'
    __bodId__ = 'ch.vbs.schiessanzeigen'
    __label__ = 'bezeichnung'
    id = Column('belplan_id', Unicode, primary_key=True)
    bezeichnung = Column('bezeichnung', Unicode)
    infobezeichnung = Column('infobezeichnung', Unicode)
    infotelefonnr = Column('infotelefonnr', Unicode)
    infoemail = Column('infoemail', Unicode)
    url_de = Column('url_de', Unicode)
    url_fr = Column('url_fr', Unicode)
    url_it = Column('url_it', Unicode)
    url_en = Column('url_en', Unicode)
    belegungsdatum = Column('belegungsdatum', postgresql.ARRAY(DateTimeChsdi))
    wochentag = Column('belegungsdatum_wochentag', postgresql.ARRAY(Integer))
    zeit_von = Column('zeit_von', postgresql.ARRAY(Unicode))
    zeit_bis = Column('zeit_bis', postgresql.ARRAY(Unicode))
    anmerkung = Column('anmerkung', postgresql.ARRAY(Unicode))
    pdf_de = Column('pdf_de', postgresql.ARRAY(Unicode))
    pdf_fr = Column('pdf_fr', postgresql.ARRAY(Unicode))
    pdf_it = Column('pdf_it', postgresql.ARRAY(Unicode))
    pdf_en = Column('pdf_en', postgresql.ARRAY(Unicode))
    kein_schiessen = Column('kein_schiessen', postgresql.ARRAY(Boolean))
    the_geom = Column(Geometry2D)

register(SchiessAnzeigen.__bodId__, SchiessAnzeigen)


class PatrouilledesglaciersZ(Base, Vector):
    __tablename__ = 'patrouille_z'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/patrouilledesglaciers_z.mako'
    __bodId__ = 'ch.vbs.patrouilledesglaciers-z_rennen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register(PatrouilledesglaciersZ.__bodId__, PatrouilledesglaciersZ)


class PatrouilledesglaciersA(Base, Vector):
    __tablename__ = 'patrouille_a'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/patrouilledesglaciers_a.mako'
    __bodId__ = 'ch.vbs.patrouilledesglaciers-a_rennen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register(PatrouilledesglaciersA.__bodId__, PatrouilledesglaciersA)


class Retablierungsstellen(Base, Vector):
    __tablename__ = 'retablierungsstellen'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/retablierungsstellen.mako'
    __bodId__ = 'ch.vbs.retablierungsstellen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    url = Column('url', Unicode)
    the_geom = Column(Geometry2D)

register(Retablierungsstellen.__bodId__, Retablierungsstellen)


class Armeelogistikcenter(Base, Vector):
    __tablename__ = 'armeelogistikcenter'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/armeelogistikcenter.mako'
    __bodId__ = 'ch.vbs.armeelogistikcenter'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    abkuerzung = Column('abkuerzung', Unicode)
    mail = Column('email', Unicode)
    the_geom = Column(Geometry2D)

register(Armeelogistikcenter.__bodId__, Armeelogistikcenter)


class BundestankstellenBebeco:
    __tablename__ = 'v_bundestankstellen_bebeco'
    __table_args__ = ({'schema': 'militaer', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bundestankstellen.mako'
    __bodId__ = 'ch.vbs.bundestankstellen-bebeco'
    __label__ = 'ort'
    __returnedGeometry__ = 'the_geom_point'
    id = Column('bgdi_id', Integer, primary_key=True)
    standort = Column('standort', Unicode)
    adresse = Column('adresse', Unicode)
    plz = Column('plz', Integer)
    ort = Column('ort', Unicode)
    oeffnungszeiten = Column('oeffnungszeiten', Unicode)
    produkt_de = Column('produkt_de', Unicode)
    produkt_fr = Column('produkt_fr', Unicode)
    produkt_it = Column('produkt_it', Unicode)
    hinweis_de = Column('hinweis_de', Unicode)
    hinweis_fr = Column('hinweis_fr', Unicode)
    hinweis_it = Column('hinweis_it', Unicode)
    kontakt = Column('kontakt', Unicode)
    x = Column('x', Float)
    y = Column('y', Float)
    the_geom_point = Column('the_geom', Geometry2D)


class BundestankstellenBebecoZoom1(Base, BundestankstellenBebeco, Vector):
    __minscale__ = 1
    __maxscale__ = 10000
    the_geom = Column('the_geom_tooltip_2', Geometry2D)

register(BundestankstellenBebeco.__bodId__, BundestankstellenBebecoZoom1)


class BundestankstellenBebecoZoom2(Base, BundestankstellenBebeco, Vector):
    __minscale__ = 10000
    the_geom = Column('the_geom_tooltip', Geometry2D)

register(BundestankstellenBebeco.__bodId__, BundestankstellenBebecoZoom2)


class Notfalltreffpunkte:
    __tablename__ = 'v_notfalltreffpunkte'
    __table_args__ = ({'schema': 'babs', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/notfalltreffpunkte.mako'
    __bodId__ = 'ch.babs.notfalltreffpunkte'
    __label__ = 'id'
    __returnedGeometry__ = 'the_geom_point'
    id = Column('ntp_id', Unicode, primary_key=True)
    gebbezeichnung = Column('gebbezeichnung', Unicode)
    strasse = Column('strasse', Unicode)
    haus_nummer = Column('haus_nummer', Unicode)
    plz = Column('plz', Integer)
    ort = Column('ort', Unicode)
    gemeinde = Column('gemeinde', Unicode)
    kanton = Column('kanton', Unicode)
    xkoord = Column('xkoord', Integer)
    ykoord  = Column('ykoord', Integer)
    linkkanton = Column('linkkanton', Unicode)
    linkbabs  = Column('linkbabs', Unicode)
    bemerkungen = Column('bemerkungen', Unicode)
    the_geom_point = Column('the_geom', Geometry2D)


class NotfalltreffpunkteZoom1(Base, Notfalltreffpunkte, Vector):
    __minscale__ = 1
    __maxscale__ = 100000
    the_geom = Column('the_geom_tooltip_2', Geometry2D)

register(NotfalltreffpunkteZoom1.__bodId__, NotfalltreffpunkteZoom1)


class NotfalltreffpunkteZoom2(Base, Notfalltreffpunkte, Vector):
    __minscale__ = 100000
    the_geom = Column('the_geom_tooltip', Geometry2D)

register(NotfalltreffpunkteZoom2.__bodId__, NotfalltreffpunkteZoom2)


class LogistikraeumeArmeelogistikcenter(Base, Vector):
    __tablename__ = 'abschnittsregionen_armeelogistikzentren'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/logistikraeume.mako'
    __bodId__ = 'ch.vbs.logistikraeume-armeelogistikcenter'
    __label__ = 'kanton'
    id = Column('bgdi_id', Integer, primary_key=True)
    kanton = Column('kantone', Unicode)
    region = Column('region', Unicode)
    the_geom = Column(Geometry3D)

register(LogistikraeumeArmeelogistikcenter.__bodId__, LogistikraeumeArmeelogistikcenter)


class Waldschaden(Base, Vector):
    __tablename__ = 'projektil'
    __table_args__ = ({'schema': 'wascha', 'autoload': False})
    __template__ = 'templates/htmlpopup/waldschadenkarte.mako'
    __bodId__ = 'ch.vbs.waldschadenkarte'
    __label__ = 'lauf_nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    lauf_nr = Column('lauf_nr', Unicode)
    jahr_schad = Column('jahr_schad', Unicode)
    gde_name = Column('gde_name', Unicode)
    lokalname = Column('lokalname', Unicode)
    x_koord = Column('x_koord', Integer)
    y_koord = Column('y_koord', Integer)

register(Waldschaden.__bodId__, Waldschaden)


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

register(SimFacilitiesA.__bodId__, SimFacilitiesA)


class SimFacilitiesK(Base, SimFacilities, Vector):
    __tablename__ = 'sim_fac_kraft'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_kraft'

register(SimFacilitiesK.__bodId__, SimFacilitiesK)


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

register(SimPlanningK.__bodId__, SimPlanningK)


class SimPlanningA(Base, SimPlanning, Vector):
    __tablename__ = 'sim_pl_anhoerung'
    __bodId__ = 'ch.vbs.sachplan-infrastruktur-militaer_anhoerung'

register(SimPlanningA.__bodId__, SimPlanningA)


class KatasterBelasteterStandorteMilitaer(Base, Vector):
    __tablename__ = 'kataster_belasteter_standorte_militaer'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/kataster_belasteter_standorte_militaer.mako'
    __bodId__ = 'ch.vbs.kataster-belasteter-standorte-militaer'
    __label__ = 'katasternummer'
    id = Column('bgdi_id', Integer, primary_key=True)
    katasternummer = Column('katasternummer', Unicode)
    standorttyp_de = Column('standorttyp_de', Unicode)
    standorttyp_fr = Column('standorttyp_fr', Unicode)
    standorttyp_it = Column('standorttyp_it', Unicode)
    statusaltlv_de = Column('status_altlv_de', Unicode)
    statusaltlv_fr = Column('status_altlv_fr', Unicode)
    statusaltlv_it = Column('status_altlv_it', Unicode)
    untersuchungsmassnahmen_de = Column('untersuchungsmassnahmen_de', Unicode)
    untersuchungsmassnahmen_fr = Column('untersuchungsmassnahmen_fr', Unicode)
    untersuchungsmassnahmen_it = Column('untersuchungsmassnahmen_it', Unicode)
    url_de = Column('url_kbs_auszug_de', Unicode)
    url_fr = Column('url_kbs_auszug_fr', Unicode)
    url_it = Column('url_kbs_auszug_it', Unicode)
    the_geom = Column(Geometry2D)

register(KatasterBelasteterStandorteMilitaer.__bodId__, KatasterBelasteterStandorteMilitaer)


class Panzerverschiebungsrouten(Base, Vector):
    __tablename__ = 'panzerverschiebungsrouten_kunstbauten'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/panzerverschiebungsrouten.mako'
    __bodId__ = 'ch.vbs.panzerverschiebungsrouten'
    __label__ = 'tonnage'
    id = Column('bgdi_id', Integer, primary_key=True)
    tonnage = Column('tonnage', Unicode)
    the_geom = Column(Geometry2D)

register(Panzerverschiebungsrouten.__bodId__, Panzerverschiebungsrouten)


class ArmeeKriegsdenkmaeler(Base, Vector):
    __tablename__ = 'armee_kriegsdenkmaeler'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/armee_kriegsdenkmaeler.mako'
    __bodId__ = 'ch.vbs.armee-kriegsdenkmaeler'
    __label__ = 'inventar_nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    inventar_nr = Column('inventar_nr', Unicode)
    kanton = Column('kanton', Unicode)
    standort = Column('standort', Unicode)
    bezeichnung = Column('bezeichnung', Unicode)
    kategorie = Column('kategorie', Unicode)
    thema = Column('thema', Unicode)
    zeitraum = Column('zeitraum', Unicode)
    form = Column('form', Unicode)
    baujahr = Column('baujahr', Unicode)
    link_zum_objekt = Column('link_zum_objekt', Unicode)
    link_zum_gesamtinventar = Column('link_zum_gesamtinventar', Unicode)
    the_geom = Column(Geometry2D)

register(ArmeeKriegsdenkmaeler.__bodId__, ArmeeKriegsdenkmaeler)


class Ladestationen(Base, Vector):
    __tablename__ = 'elektrotankstellen'
    __table_args__ = ({'schema': 'militaer', 'autoload': False})
    __template__ = 'templates/htmlpopup/vbs_ladestationen.mako'
    __bodId__ = 'ch.vbs.ladestationen'
    __label__ = 'standort'
    id = Column('bgdi_id', Integer, primary_key=True)
    standort = Column('standort', Unicode)
    strasse = Column('strasse', Unicode)
    plz = Column('plz', Integer)
    ort = Column('ort', Unicode)
    oeffnungszeiten = Column('oeffnungszeiten', Unicode)
    anzahl_ladepunkte = Column('anzahl_ladepunkte', Unicode)
    leistung = Column('leistung', Unicode)
    typ_stecker = Column('typ_stecker', Unicode)
    hinweis = Column('hinweis', Unicode)
    kontakt = Column('kontakt', Unicode)
    x_koordinate = Column('x_koordinate', Integer)
    y_koordinate = Column('y_koordinate', Integer)
    bemerkungen = Column('bemerkungen', Unicode)
    the_geom = Column(Geometry2D)

register(Ladestationen.__bodId__, Ladestationen)
