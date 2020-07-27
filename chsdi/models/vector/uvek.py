# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer, Date
from sqlalchemy.types import Numeric, Float, Boolean

from chsdi.models import register, bases
from chsdi.models.types import JsonChsdi
from chsdi.models.vector import Vector, Geometry2D


Base = bases['uvek']


class Nsa(Base, Vector):
    __tablename__ = 'nsa'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/nsa.mako'
    __bodId__ = 'ch.astra.nationalstrassenachsen'
    __label__ = 'id'
    __queryable_attributes__ = ['strassennummer', 'name']
    id = Column('bgdi_id', Integer, primary_key=True)
    eigentuemer = Column('eigentuemer', Unicode)
    segmentname = Column('segmentname', Unicode)
    strassennummer = Column('strassennummer', Unicode)
    bezeichnung = Column('bezeichnung', Unicode)
    positionscode = Column('positionscode', Unicode)
    name = Column('name', Unicode)
    sortnr = Column('sortnr', Unicode)
    kilometerwert = Column('kilometerwert', Unicode)
    sektorlaenge = Column('sektorlaenge', Unicode)
    type_geom = Column('type_geom', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.nationalstrassenachsen', Nsa)


class SchienennetzPoint(Base, Vector):
    __tablename__ = 'schienennetz_point'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/schienennetz_point.mako'
    __bodId__ = 'ch.bav.schienennetz'
    __label__ = 'nom_point'
    __queryable_attributes__ = ['numero', 'nom_point', 'abreviation']
    id = Column('xtf_id', Integer, primary_key=True)
    xtf_id_tooltip = Column('xtf_id_tooltip', Unicode)
    numero = Column('numero', Integer)
    nom_point = Column('nom_point', Unicode)
    abreviation = Column('abreviation', Unicode)
    the_geom = Column(Geometry2D)

register(SchienennetzPoint.__bodId__, SchienennetzPoint)


class SchienennetzSegment(Base, Vector):
    __tablename__ = 'schienennetz_segment'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/schienennetz_segment.mako'
    __bodId__ = 'ch.bav.schienennetz'
    __label__ = 'nom_segment'
    __queryable_attributes__ = ['nom_segment']
    id = Column('id', Integer, primary_key=True)
    xtf_id_tooltip = Column('xtf_id_tooltip', Unicode)
    numeroet = Column('numeroet', Integer)
    nom_segment = Column('nom_segment', Unicode)
    point_debut_nom = Column('point_debut_nom', Unicode)
    point_debut_nummero = Column('point_debut_nummero', Unicode)
    point_fin_nom = Column('point_fin_nom', Unicode)
    point_fin_nummero = Column('point_fin_nummero', Unicode)
    kmdebut = Column('kmdebut', Numeric)
    kmfin = Column('kmfin', Numeric)
    kmtext = Column('kmtext', Unicode)
    kmnummero = Column('kmnumero', Unicode)
    abreviationet = Column('abreviationet', Unicode)
    nombrevoies = Column('nombrevoies', Integer)
    ecartement = Column('ecartement', Unicode)
    electrification_fr = Column('electrification_fr', Unicode)
    electrification_de = Column('electrification_de', Unicode)
    debutvalidite = Column('debutvalidite', Unicode)
    finvalidite = Column('finvalidite', Unicode)
    the_geom = Column(Geometry2D)

register(SchienennetzSegment.__bodId__, SchienennetzSegment)


class SperrungenUmleitungen:
    __table_args__ = ({'schema': 'astra', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/sperrungen_umleitungen.mako'
    __label__ = 'sperrungen_type'
    id = Column('bgdi_id', Integer, primary_key=True)
    sperrungen_type = Column('type', Unicode)
    land = Column('land', Unicode)
    duration_de = Column('duration_de', Unicode)
    duration_fr = Column('duration_fr', Unicode)
    duration_it = Column('duration_it', Unicode)
    duration_en = Column('duration_en', Unicode)
    reason = Column('reason', Numeric)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    title_en = Column('title_en', Unicode)
    abstract_de = Column('abstract_de', Unicode)
    abstract_fr = Column('abstract_fr', Unicode)
    abstract_it = Column('abstract_it', Unicode)
    abstract_en = Column('abstract_en', Unicode)
    state_validate = Column('state_validate', Unicode)
    file_de = Column('file_de', Unicode)
    file_fr = Column('file_fr', Unicode)
    file_it = Column('file_it', Unicode)
    file_en = Column('file_en', Unicode)
    content_provider = Column('content_provider')
    url1_link_de = Column('url1_link_de', Unicode)
    url1_link_fr = Column('url1_link_fr', Unicode)
    url1_link_it = Column('url1_link_it', Unicode)
    url1_link_en = Column('url1_link_en', Unicode)
    url1_text_de = Column('url1_text_de', Unicode)
    url1_text_fr = Column('url1_text_fr', Unicode)
    url1_text_it = Column('url1_text_it', Unicode)
    url1_text_en = Column('url1_text_en', Unicode)
    the_geom = Column('the_geom', Geometry2D)


class WanderlandSperrungenUmleitungen(Base, SperrungenUmleitungen, Vector):
    __tablename__ = 'v_sperrungen_umleitungen_line_wanderland'
    __bodId__ = 'ch.astra.wanderland-sperrungen_umleitungen'

register(WanderlandSperrungenUmleitungen.__bodId__, WanderlandSperrungenUmleitungen)


class VelolandSperrungenUmleitungen(Base, SperrungenUmleitungen, Vector):
    __tablename__ = 'v_sperrungen_umleitungen_line_veloland'
    __bodId__ = 'ch.astra.veloland-sperrungen_umleitungen'

register(VelolandSperrungenUmleitungen.__bodId__, VelolandSperrungenUmleitungen)


class SkatinglandSperrungenUmleitungen(Base, SperrungenUmleitungen, Vector):
    __tablename__ = 'v_sperrungen_umleitungen_line_skatingland'
    __bodId__ = 'ch.astra.skatingland-sperrungen_umleitungen'

register(SkatinglandSperrungenUmleitungen.__bodId__, SkatinglandSperrungenUmleitungen)


class MountainbikelandSperrungenUmleitungen(Base, SperrungenUmleitungen, Vector):
    __tablename__ = 'v_sperrungen_umleitungen_line_mtbland'
    __bodId__ = 'ch.astra.mountainbikeland-sperrungen_umleitungen'

register(MountainbikelandSperrungenUmleitungen.__bodId__, MountainbikelandSperrungenUmleitungen)


class OevHaltestellen:
    __tablename__ = 'oev_haltestellen_tooltip'
    __table_args__ = ({'schema': 'bav', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/oev_haltestellen.mako'
    __bodId__ = 'ch.bav.haltestellen-oev'
    __label__ = 'name'
    __extended_info__ = True
    __queryable_attributes__ = ['id', 'name']
    __returnedGeometry__ = 'the_geom_point'
    id = Column('nummer', Integer, primary_key=True)
    name = Column('name', Unicode)
    abkuerzung = Column('abkuerzung', Unicode)
    tuabkuerzung = Column('tuabkuerzung', Unicode)
    betriebspunkttyp = Column('betriebspunkttyp', Unicode)
    verkehrsmittel = Column('verkehrsmittel', Unicode)
    # point geometry hilight
    the_geom_point = Column('the_geom', Geometry2D)


class OevHaltestellenZoom1(Base, OevHaltestellen, Vector):
    __minscale__ = 1
    __maxscale__ = 3000
    the_geom = Column('bgdi_geom_poly', Geometry2D)

register(OevHaltestellen.__bodId__, OevHaltestellenZoom1)


class OevHaltestellenZoom2(Base, OevHaltestellen, Vector):
    __minscale__ = 3000
    the_geom = Column('bgdi_geom_poly_overview', Geometry2D)

register(OevHaltestellen.__bodId__, OevHaltestellenZoom2)


# IVS NAT and REG use the same template
class SicherheitsZonenPlan (Base, Vector):
    __tablename__ = 'sichereitszonen'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sicherheitszoneneplan.mako'
    __bodId__ = 'ch.bazl.sicherheitszonenplan'
    __extended_info__ = True
    __label__ = 'id'
    id = Column('stabil_id', Unicode, primary_key=True)
    zone = Column('zone', Unicode)
    zonetype_tid = Column('zonetype_tid', Unicode)
    type_id = Column('type_id', Unicode)
    zonetype_de = Column('zonetype_de', Unicode)
    zonetype_fr = Column('zonetype_fr', Unicode)
    zonetype_it = Column('zonetype_it', Unicode)
    zone_name = Column('zone_name', Unicode)
    zone_valid_from = Column('zone_valid_from', Date)
    zone_description = Column('zone_description', Unicode)
    originator = Column('originator', Unicode)
    canton = Column('canton', Unicode)
    municipality = Column('municipality', Unicode)
    approval_date = Column('approval_date', Date)
    status_id = Column('status_id', Unicode)
    legalstatus_tid = Column('legalstatus_tid', Unicode)
    legalstatus_de = Column('legalstatus_de', Unicode)
    legalstatus_fr = Column('legalstatus_fr', Unicode)
    legalstatus_it = Column('legalstatus_it', Unicode)
    title = Column('title', Unicode)
    weblink = Column('weblink', Unicode)
    valid_from = Column('valid_from', Date)
    valid_until = Column('valid_until', Date)
    latest_modification = Column('latest_modification', Date)
    doc_description = Column('doc_description', Unicode)
    doc_id = Column('doc_id', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.sicherheitszonenplan', SicherheitsZonenPlan)


class IVSNat(Base, Vector):
    __tablename__ = 'ivs_nat_tt'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-nat'
    __queryable_attributes__ = ['ivs_slaname', 'ivs_nummer', 'ivs_signatur']
    __label__ = 'id'
    id = Column('nat_id', Integer, primary_key=True)
    ivs_slaname = Column('ivs_slaname', Unicode)
    ivs_nummer = Column('ivs_nummer', Unicode)
    ivs_signatur = Column('ivs_signatur', Unicode)
    ivs_signatur_fr = Column('ivs_signatur_fr', Unicode)
    ivs_signatur_it = Column('ivs_signatur_it', Unicode)
    ivs_signatur_de = Column('ivs_signatur_de', Unicode)
    ivs_kanton = Column('ivs_kanton', Unicode)
    ivs_sladatehist = Column('ivs_sladatehist', Integer)
    ivs_sladatemorph = Column('ivs_sladatemorph', Integer)
    ivs_slabedeutung = Column('ivs_slabedeutung', Integer)
    ivs_sortsla = Column('ivs_sortsla', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.ivs-nat', IVSNat)


class IVSNatVerlaeufe(Base, Vector):
    __tablename__ = 'ivs_nat_verlaeufe_tt'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-nat-verlaeufe'
    __queryable_attributes__ = ['ivs_slaname', 'ivs_nummer', 'ivs_signatur']
    __label__ = 'id'
    id = Column('nat_id', Integer, primary_key=True)
    ivs_slaname = Column('ivs_slaname', Unicode)
    ivs_nummer = Column('ivs_nummer', Unicode)
    ivs_signatur = Column('ivs_signatur', Unicode)
    ivs_signatur_fr = Column('ivs_signatur_fr', Unicode)
    ivs_signatur_it = Column('ivs_signatur_it', Unicode)
    ivs_signatur_de = Column('ivs_signatur_de', Unicode)
    ivs_kanton = Column('ivs_kanton', Unicode)
    ivs_sladatehist = Column('ivs_sladatehist', Integer)
    ivs_sladatemorph = Column('ivs_sladatemorph', Integer)
    ivs_slabedeutung = Column('ivs_slabedeutung', Integer)
    ivs_sortsla = Column('ivs_sortsla', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.ivs-nat-verlaeufe', IVSNatVerlaeufe)


class IVSRegLoc(Base, Vector):
    __tablename__ = 'ivs_reg_loc'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-reg_loc'
    __queryable_attributes__ = ['ivs_slaname', 'ivs_nummer', 'ivs_signatur']
    __label__ = 'ivs_nummer'
    id = Column('reg_loc_id', Integer, primary_key=True)
    ivs_slaname = Column('ivs_slaname', Unicode)
    ivs_nummer = Column('ivs_nummer', Unicode)
    ivs_signatur = Column('ivs_signatur', Unicode)
    ivs_signatur_fr = Column('ivs_signatur_fr', Unicode)
    ivs_signatur_it = Column('ivs_signatur_it', Unicode)
    ivs_signatur_de = Column('ivs_signatur_de', Unicode)
    ivs_kanton = Column('ivs_kanton', Unicode)
    ivs_sladatehist = Column('ivs_sladatehist', Integer)
    ivs_sladatemorph = Column('ivs_sladatemorph', Integer)
    ivs_slabedeutung = Column('ivs_slabedeutung', Integer)
    ivs_sortsla = Column('ivs_sortsla', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.ivs-reg_loc', IVSRegLoc)


class BaulinienNationalstrassen(Base, Vector):
    __tablename__ = 'baulinien_nationalstrassen_line'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/baulinien_nationalstrassen.mako'
    __bodId__ = 'ch.astra.baulinien-nationalstrassen'
    __label__ = 'status'
    id = Column('bgdi_id', Integer, primary_key=True)
    status = Column('status', Unicode)
    approval_date = Column('approval_date', Date)
    publication_date = Column('publication_date', Date)
    approving_authority = Column('approving_authority', Unicode)
    the_geom = Column(Geometry2D)

register(BaulinienNationalstrassen.__bodId__, BaulinienNationalstrassen)


class Zaehlstellenregloc(Base, Vector):
    __tablename__ = 'verkehr_reg_loc'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/verkehrszaehlstellen.mako'
    __bodId__ = 'ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal'
    __queryable_attributes__ = ['id', 'zaehlstellen_bezeichnung']
    __extended_info__ = True
    __label__ = 'zaehlstellen_bezeichnung'
    id = Column('nr', Integer, primary_key=True)
    zaehlstellen_bezeichnung = Column('zaehlstellen_bezeichnung', Unicode)
    uno_zaehlstelle = Column('uno_zaehlstelle', Unicode)
    zst_physisch_virtuell = Column('zst_physisch_virtuell', Unicode)
    messstellentyp = Column('messstellentyp', Unicode)
    koordinate_ost = Column('koordinate_ost', Integer)
    koordinate_nord = Column('koordinate_nord', Integer)
    kanton = Column('kanton', Unicode)
    swiss_10 = Column('swiss_10', Integer)
    netz = Column('netz', Unicode)
    status = Column('status', Unicode)
    strasse = Column('strasse', Unicode)
    richtung_1 = Column('richtung_1', Unicode)
    richtung_2 = Column('richtung_2', Unicode)
    inbetriebnahme = Column('inbetriebnahme', Unicode)
    anzahl_fahrstreifen_tot = Column('anzahl_fahrstreifen_tot', Integer)
    bulletins_sasvz = Column('bulletins_sasvz', Unicode)
    ssvz_2005 = Column('ssvz_2005', Unicode)
    jahresauswertung = Column('jahresauswertung', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal', Zaehlstellenregloc)


class Zaehstellenueber(Base, Vector):
    __tablename__ = 'verkehr_ueber'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/verkehrszaehlstellen.mako'
    __bodId__ = 'ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet'
    __queryable_attributes__ = ['id', 'zaehlstellen_bezeichnung']
    __extended_info__ = True
    __label__ = 'zaehlstellen_bezeichnung'
    id = Column('nr', Integer, primary_key=True)
    zaehlstellen_bezeichnung = Column('zaehlstellen_bezeichnung', Unicode)
    uno_zaehlstelle = Column('uno_zaehlstelle', Unicode)
    zst_physisch_virtuell = Column('zst_physisch_virtuell', Unicode)
    messstellentyp = Column('messstellentyp', Unicode)
    koordinate_ost = Column('koordinate_ost', Integer)
    koordinate_nord = Column('koordinate_nord', Integer)
    kanton = Column('kanton', Unicode)
    swiss_10 = Column('swiss_10', Integer)
    netz = Column('netz', Unicode)
    status = Column('status', Unicode)
    strasse = Column('strasse', Unicode)
    richtung_1 = Column('richtung_1', Unicode)
    richtung_2 = Column('richtung_2', Unicode)
    inbetriebnahme = Column('inbetriebnahme', Unicode)
    anzahl_fahrstreifen_tot = Column('anzahl_fahrstreifen_tot', Integer)
    bulletins_sasvz = Column('bulletins_sasvz', Unicode)
    ssvz_2005 = Column('ssvz_2005', Unicode)
    jahresauswertung = Column('jahresauswertung', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet', Zaehstellenueber)


class Zaehlstellenuebergeordnet(Base, Vector):
    __tablename__ = 'strassenverkehrszaehlung_uebergeordnet'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/verkehrszaehlung_uebergeordnet.mako'
    __bodId__ = 'ch.astra.strassenverkehrszaehlung-uebergeordnet'
    __extended_info__ = True
    __label__ = 'mlocname'
    id = Column('bgdi_id', Integer, primary_key=True)
    mlocname = Column('mlocname', Unicode)
    mlocnr = Column('mlocnr', Unicode)
    canton = Column('canton', Unicode)
    streetdesignation = Column('streetdesignation', Unicode)
    targetlocation1 = Column('targetlocation1', Unicode)
    targetlocation2 = Column('targetlocation2', Unicode)
    numberoflanes1 = Column('numberoflanes1', Integer)
    numberoflanes2 = Column('numberoflanes2', Integer)
    locationlv95 = Column('locationlv95', Unicode)
    de_networktype = Column('de_networktype', Unicode)
    fr_networktype = Column('fr_networktype', Unicode)
    it_networktype = Column('it_networktype', Unicode)
    en_networktype = Column('en_networktype', Unicode)
    rm_networktype = Column('rm_networktype', Unicode)
    year = Column('year', Integer)
    dtv = Column('dtv', Integer)
    dwv = Column('dwv', Integer)
    msp = Column('msp', Integer)
    asp = Column('asp', Integer)
    mspw = Column('mspw', Integer)
    aspw = Column('aspw', Integer)
    nt = Column('nt', Integer)
    nn = Column('nn', Integer)
    prctheavytraffic = Column('prctheavytraffic', Float)
    prctheavytrafficday = Column('prctheavytrafficday', Float)
    prctheavytrafficnight = Column('prctheavytrafficnight', Float)
    the_geom = Column(Geometry2D)

register('ch.astra.strassenverkehrszaehlung-uebergeordnet', Zaehlstellenuebergeordnet)


class Unf:
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_unfaelle.mako'
    __label__ = 'accidenttype_de'
    __timeInstant__ = 'accidentyear'
    __queryable_attributes__ = ['accidenttype_de', 'accidenttype_fr', 'accidenttype_it', 'accidenttype_en',
                                'accidenttypecode', 'accidentday_de', 'accidentday_fr', 'accidentday_it', 'accidentday_en',
                                'accidentmonth_de', 'accidentmonth_fr', 'accidentmonth_it', 'accidentmonth_en',
                                'accidenthour', 'accidenthour_text',
                                'accidentyear', 'severitycategory_de', 'severitycategory_fr', 'severitycategory_it', 'severitycategory_en',
                                'severitycategorycode', 'roadtype_de', 'roadtype_fr', 'roadtype_it', 'roadtype_en',
                                'roadtypecode', 'canton', 'fsocommunecode']
    id = Column('uuid', Unicode, primary_key=True)
    accidenttype_de = Column('accidenttype_de', Unicode)
    accidenttype_fr = Column('accidenttype_fr', Unicode)
    accidenttype_it = Column('accidenttype_it', Unicode)
    accidenttype_en = Column('accidenttype_en', Unicode)
    accidenttypecode = Column('accidenttypecode', Integer)
    involving_pedestrian = Column('involving_pedestrian', Boolean)
    involving_bicycle = Column('involving_bicycle', Boolean)
    involving_motorcycle = Column('involving_motorcycle', Boolean)
    accidentyear = Column('accidentyear', Integer)
    accidentmonth_de = Column('accidentmonth_de', Unicode)
    accidentmonth_fr = Column('accidentmonth_fr', Unicode)
    accidentmonth_it = Column('accidentmonth_it', Unicode)
    accidentmonth_en = Column('accidentmonth_en', Unicode)
    accidentday_de = Column('accidentday_de', Unicode)
    accidentday_fr = Column('accidentday_fr', Unicode)
    accidentday_it = Column('accidentday_it', Unicode)
    accidentday_en = Column('accidentday_en', Unicode)
    accidenthour = Column('accidenthour', Unicode)
    accidenthour_text = Column('accidenthour_text', Unicode)
    severitycategory_de = Column('severitycategory_de', Unicode)
    severitycategory_fr = Column('severitycategory_fr', Unicode)
    severitycategory_it = Column('severitycategory_it', Unicode)
    severitycategory_en = Column('severitycategory_en', Unicode)
    severitycategorycode = Column('severitycategorycode', Unicode)
    roadtype_de = Column('roadtype_de', Unicode)
    roadtype_fr = Column('roadtype_fr', Unicode)
    roadtype_it = Column('roadtype_it', Unicode)
    roadtype_en = Column('roadtype_en', Unicode)
    roadtypecode = Column('roadtypecode', Integer)
    canton = Column('canton', Unicode)
    fsocommunecode = Column('fsocommunecode', Unicode)
    the_geom = Column(Geometry2D)


class UnfPersAlle(Base, Unf, Vector):
    __tablename__ = 'v_unf_pers_alle'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_alle'

register(UnfPersAlle.__bodId__, UnfPersAlle)


class UnfPersCasualties(Base, Unf, Vector):
    __tablename__ = 'v_unf_pers_getoetete'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_getoetete'

register(UnfPersCasualties.__bodId__, UnfPersCasualties)


class UnfPersFuss(Base, Unf, Vector):
    __tablename__ = 'v_unf_pers_fussgaenger'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_fussgaenger'

register(UnfPersFuss.__bodId__, UnfPersFuss)


class UnfPersMoto(Base, Unf, Vector):
    __tablename__ = 'v_unf_pers_motorraeder'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_motorraeder'

register(UnfPersMoto.__bodId__, UnfPersMoto)


class UnfPersVelo(Base, Unf, Vector):
    __tablename__ = 'v_unf_pers_fahrraeder'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_fahrraeder'

register(UnfPersVelo.__bodId__, UnfPersVelo)


class Hauptstrassennetz(Base, Vector):
    __tablename__ = 'hauptstrassennetz'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __bodId__ = 'ch.astra.hauptstrassennetz'
    __template__ = 'templates/htmlpopup/astra_hauptstrassennetz.mako'
    __label__ = 'roadnumber'
    id = Column('bgdi_id', Integer, primary_key=True)
    roadnumber = Column('roadnumber', Integer)
    segmentdescription = Column('segmentdescription', Unicode)
    canton = Column('canton', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.hauptstrassennetz', Hauptstrassennetz)


class Schwerverunf:
    __tablename__ = 'unf_schwer'
    __table_args__ = ({'schema': 'astra', 'autoload': False, 'extend_existing': True})
    __label__ = 'canton'
    id = Column('bgdi_id', Integer, primary_key=True)
    canton = Column('canton', Unicode)
    year = Column('year', Integer)
    the_geom = Column(Geometry2D)


class SchwerverunfKantonAlkohol(Base, Schwerverunf, Vector):
    __template__ = 'templates/htmlpopup/astra_schwerverunf_kanton_alkohol.mako'
    __bodId__ = 'ch.astra.schwerverunfallte-kanton_alkohol'
    population = Column('population', Integer)
    accalcohol_ugt = Column('accalcohol_ugt', Integer)
    accalcohol_usv = Column('accalcohol_usv', Integer)
    accalcohol_ugt_usv = Column('accalcohol_ugt_usv', Integer)
    accalcohol_ugt_usv_perpopulation = Column('accalcohol_ugt_usv_perpopulation', Numeric)

register('ch.astra.schwerverunfallte-kanton_alkohol', SchwerverunfKantonAlkohol)


class SchwerverunfKantonGeschwindig(Base, Schwerverunf, Vector):
    __template__ = 'templates/htmlpopup/astra_schwerverunf_kanton_geschwindig.mako'
    __bodId__ = 'ch.astra.schwerverunfallte-kanton_geschwindigkeit'
    population = Column('population', Integer)
    accspeed_ugt = Column('accspeed_ugt', Integer)
    accspeed_usv = Column('accspeed_usv', Integer)
    accspeed_ugt_usv = Column('accspeed_ugt_usv', Integer)
    accspeed_ugt_usv_perpopulation = Column('accspeed_ugt_usv_perpopulation', Numeric)

register('ch.astra.schwerverunfallte-kanton_geschwindigkeit', SchwerverunfKantonGeschwindig)


class SchwerverunfKantonJahresvergleich(Base, Schwerverunf, Vector):
    __template__ = 'templates/htmlpopup/astra_schwerverunf_kanton_jahresvergleich.mako'
    __bodId__ = 'ch.astra.schwerverunfallte-kanton_jahresvergleich'
    acc_ugt = Column('acc_ugt', Integer)
    acc_usv = Column('acc_usv', Integer)
    acc_ugt_usv = Column('acc_ugt_usv', Integer)
    acc_ugt_lastyear = Column('acc_ugt_lastyear', Integer)
    acc_usv_lastyear = Column('acc_usv_lastyear', Integer)
    acc_ugt_usv_lastyear = Column('acc_ugt_usv_lastyear', Integer)
    acc_ugt_usv_yearchangepercent = Column('acc_ugt_usv_yearchangepercent', Numeric)

register('ch.astra.schwerverunfallte-kanton_jahresvergleich', SchwerverunfKantonJahresvergleich)


class SchwerverunfKantonProEinwohner(Base, Schwerverunf, Vector):
    __template__ = 'templates/htmlpopup/astra_schwerverunf_kanton_pro_einwohner.mako'
    __bodId__ = 'ch.astra.schwerverunfallte-kanton_pro_einwohner'
    population = Column('population', Integer)
    acc_ugt = Column('acc_ugt', Integer)
    acc_usv = Column('acc_usv', Integer)
    acc_ugt_usv = Column('acc_ugt_usv', Integer)
    acc_ugt_usv_perpopulation = Column('acc_ugt_usv_perpopulation', Numeric)

register('ch.astra.schwerverunfallte-kanton_pro_einwohner', SchwerverunfKantonProEinwohner)


class KatasterBelasteterStandorte(Base, Vector):
    __tablename__ = 'kataster_belasteter_standorte_oev'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/kataster_belasteter_standorte_oev.mako'
    __bodId__ = 'ch.bav.kataster-belasteter-standorte-oev'
    __queryable_attributes__ = ['katasternummer']
    __label__ = 'id'
    id = Column('vflz_id', Integer, primary_key=True)
    katasternummer = Column('katasternummer', Unicode)
    standorttyp_de = Column('standorttyp_de', Unicode)
    standorttyp_fr = Column('standorttyp_fr', Unicode)
    standorttyp_it = Column('standorttyp_it', Unicode)
    statusaltlv_de = Column('statusaltlv_de', Unicode)
    statusaltlv_fr = Column('statusaltlv_fr', Unicode)
    statusaltlv_it = Column('statusaltlv_it', Unicode)
    untersuchungsstand_de = Column('untersuchungsstand_de', Unicode)
    untersuchungsstand_fr = Column('untersuchungsstand_fr', Unicode)
    untersuchungsstand_it = Column('untersuchungsstand_it', Unicode)
    url = Column('url', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.kataster-belasteter-standorte-oev', KatasterBelasteterStandorte)


class AbgeltungWasserkraftnutzung(Base, Vector):
    __tablename__ = 'abgeltung_wasserkraftnutzung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/abgeltungwasserkraftnutzung.mako'
    __bodId__ = 'ch.bfe.abgeltung-wasserkraftnutzung'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('objectnumber', Integer, primary_key=True)
    area = Column('area', Numeric)
    name = Column('name', Unicode)
    perimeter = Column('perimeter', Numeric)
    startprotectioncommitment = Column('startprotectioncommitment', Unicode)
    endprotectioncommitment = Column('endprotectioncommitment', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.abgeltung-wasserkraftnutzung', AbgeltungWasserkraftnutzung)


class FernwaermeWohn (Base, Vector):
    __tablename__ = 'fernwaerme_wohn'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/fernwaerme_wohn.mako'
    __bodId__ = 'ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude'
    __extended_info__ = True
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    needhome = Column('needhome', Float)
    needservice = Column('needservice', Float)
    needtotal = Column('needtotal', Float)
    service = Column('service', Unicode)
    noga = Column('noga', Unicode)
    percentgas = Column('percentgas', Float)
    percentoil = Column('percentoil', Float)
    percentpump = Column('percentpump', Float)
    percentremoteheat = Column('percentremoteheat', Float)
    objectid = Column('objectid', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfe.fernwaerme-nachfrage_wohn_dienstleistungsgebaeude', FernwaermeWohn)


class FernwaermeIndustrie (Base, Vector):
    __tablename__ = 'fernwaerme_industrie'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/fernwaerme_industrie.mako'
    __bodId__ = 'ch.bfe.fernwaerme-nachfrage_industrie'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    needindustry = Column('needindustry', Integer)
    industry = Column('industry', Unicode)
    noga = Column('noga', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.fernwaerme-nachfrage_industrie', FernwaermeIndustrie)


class Energieberatungsstellen (Base, Vector):
    __tablename__ = 'energieberatungsstellen'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energieberatungsstellen.mako'
    __bodId__ = 'ch.bfe.energieberatungsstellen'
    __queryable_attributes__ = ['name', 'management']
    __label__ = 'name'
    id = Column('xtf_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    management = Column('management', Unicode)
    category = Column('category', Unicode)
    category_text_it = Column('category_text_it', Unicode)
    category_text_de = Column('category_text_de', Unicode)
    category_text_fr = Column('category_text_fr', Unicode)
    address1 = Column('address1', Unicode)
    address2 = Column('address2', Unicode)
    postofficebox = Column('postofficebox', Unicode)
    pc_place = Column('pc_place', Unicode)
    telephonenumber = Column('telephonenumber', Unicode)
    mail = Column('mail', Unicode)
    webaddress = Column('webaddress', Unicode)
    paidconsultation_de = Column('paidconsultation_de', Unicode)
    paidconsultation_fr = Column('paidconsultation_fr', Unicode)
    paidconsultation_it = Column('paidconsultation_it', Unicode)
    freeconsultation_de = Column('freeconsultation_de', Unicode)
    freeconsultation_fr = Column('freeconsultation_fr', Unicode)
    freeconsultation_it = Column('freeconsultation_it', Unicode)
    clientprivatepersons = Column('clientprivatepersons', Boolean)
    clientcompanies = Column('clientcompanies', Boolean)
    clientmunicipalities = Column('clientmunicipalities', Boolean)
    topicbuildings = Column('topicbuildings', Boolean)
    topicelectricdeviceslighting = Column('topicelectricdeviceslighting', Boolean)
    topicmobility = Column('topicmobility', Boolean)
    the_geom = Column(Geometry2D)

register('ch.bfe.energieberatungsstellen', Energieberatungsstellen)


class Energiestaedte(Base, Vector):
    __tablename__ = 'energiestaedte'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte.mako'
    __bodId__ = 'ch.bfe.energiestaedte'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    punktezahl = Column('punktezahl', Numeric)
    einwohner = Column('einwohner', Numeric)
    energiestadtseit = Column('energiestadtseit', Unicode)
    beteiligtegemeinde = Column('beteiligtegemeinde', Unicode)
    anzahlaudits = Column('anzahlaudits', Numeric)
    berater = Column('berater', Unicode)
    linkenergiestadtweb = Column('linkenergiestadtweb', Unicode)
    bfsnr = Column('bfsnr', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte', Energiestaedte)


class EnergiestaedteRegionen(Base, Vector):
    __tablename__ = 'energiestaedte_energieregionen'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte_energieregionen.mako'
    __bodId__ = 'ch.bfe.energiestaedte-energieregionen'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    kategorie = Column('kategorie', Unicode)
    beteiligtegemeinden = Column('beteiligtegemeinden', Unicode)
    linkenergieregion = Column('linkenergieregion', Unicode)
    berater = Column('berater', Unicode)
    mailberater  = Column('mailberater', Unicode)
    bezeichnung_kat_de = Column('bezeichnung_kat_de', Unicode)
    bezeichnung_kat_fr = Column('bezeichnung_kat_fr', Unicode)
    bezeichnung_kat_it = Column('bezeichnung_kat_it', Unicode)
    bezeichnung_kat_en = Column('bezeichnung_kat_en', Unicode)
    projektportraittext_de = Column('projektportraittext_de', Unicode)
    projektportraittext_fr = Column('projektportraittext_fr', Unicode)
    projektportraittext_it = Column('projektportraittext_it', Unicode)
    projektportraittext_en = Column('projektportraittext_en', Unicode)
    projektportraitlink_de = Column('projektportraitlink_de', Unicode)
    projektportraitlink_fr = Column('projektportraitlink_fr', Unicode)
    projektportraitlink_it = Column('projektportraitlink_it', Unicode)
    projektportraitlink_en = Column('projektportraitlink_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte-energieregionen', EnergiestaedteRegionen)


class Energiestaedte2000wattAreale(Base, Vector):
    __tablename__ = 'energiestaedte_2000watt_areale'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte_2000watt_areale.mako'
    __bodId__ = 'ch.bfe.energiestaedte-2000watt-areale'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    kategorie = Column('kategorie', Unicode)
    bezeichnung_kat_de = Column('bezeichnung_kat_de', Unicode)
    bezeichnung_kat_fr = Column('bezeichnung_kat_fr', Unicode)
    bezeichnung_kat_it = Column('bezeichnung_kat_it', Unicode)
    bezeichnung_kat_en = Column('bezeichnung_kat_en', Unicode)
    gemeinde = Column('gemeinde', Unicode)
    berater = Column('berater', Unicode)
    linkberater = Column('linkberater', Unicode)
    linkfaktenblatt_de = Column('linkfaktenblatt_de', Unicode)
    linkfaktenblatt_fr = Column('linkfaktenblatt_fr', Unicode)
    linkfaktenblatt_it = Column('linkfaktenblatt_it', Unicode)
    linkfaktenblatt_en = Column('linkfaktenblatt_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte-2000watt-areale', Energiestaedte2000wattAreale)


class Energieforschung(Base, Vector):
    __tablename__ = 'energieforschung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energieforschung.mako'
    __bodId__ = 'ch.bfe.energieforschung'
    __extended_info__ = True
    __queryable_attributes__ = ['projektnummer', 'titel']
    __label__ = 'titel'
    id = Column('bgdi_id', Integer, primary_key=True)
    titel = Column('titel', Unicode)
    leuchtturm = Column('leuchtturm', Integer)
    beschreibung = Column('beschreibung', Unicode)
    projektstatus_fr = Column('projektstatus_fr', Unicode)
    projektstatus_de = Column('projektstatus_de', Unicode)
    projektstatus_it = Column('projektstatus_it', Unicode)
    projektstatus_en = Column('projektstatus_en', Unicode)
    projektnummer = Column('projektnummer', Unicode)
    projektbeginn = Column('projektbeginn', Unicode)
    projektende = Column('projektende', Unicode)
    oberthema_fr = Column('oberthema_fr', Unicode)
    oberthema_de = Column('oberthema_de', Unicode)
    oberthema_it = Column('oberthema_it', Unicode)
    oberthema_en = Column('oberthema_en', Unicode)
    unterthema_fr = Column('unterthema_fr', Unicode)
    unterthema_de = Column('unterthema_de', Unicode)
    unterthema_it = Column('unterthema_it', Unicode)
    unterthema_en = Column('unterthema_en', Unicode)
    bericht = Column('bericht', Unicode)
    fachartikel = Column('fachartikel', Unicode)
    infoclip = Column('infoclip', Unicode)
    projektpartner = Column('projektpartner', Unicode)
    kontakt = Column('kontakt', Unicode)
    plz = Column('plz', Unicode)
    ort = Column('ort', Unicode)
    kanton = Column('kanton', Unicode)
    bild0 = Column('bild0', Unicode)
    bild1 = Column('bild1', Unicode)
    bild2 = Column('bild2', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.energieforschung', Energieforschung)


class FernWaermeAngebot(Base, Vector):
    __tablename__ = 'fernwaerme_angebot'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/fernwaerme_angebot.mako'
    __bodId__ = 'ch.bfe.fernwaerme-angebot'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    heatpotential = Column('heatpotential', Float)
    heat_supplier_category = Column('heat_supplier_category', Integer)
    bezeichnung_de = Column('bezeichnung_de', Unicode)
    bezeichnung_fr = Column('bezeichnung_fr', Unicode)
    bezeichnung_it = Column('bezeichnung_it', Unicode)
    bezeichnung_en = Column('bezeichnung_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.fernwaerme-angebot', FernWaermeAngebot)


class KomoProjekte(Base, Vector):
    __tablename__ = 'komo_projekte'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/komo.mako'
    __bodId__ = 'ch.bfe.komo-projekte'
    __label__ = 'id'
    id = Column('xtf_id', Integer, primary_key=True)
    project_title_de = Column('project_title_de', Unicode)
    project_title_fr = Column('project_title_fr', Unicode)
    project_title_it = Column('project_title_it', Unicode)
    project_title_en = Column('project_title_en', Unicode)
    projectstart = Column('projectstart', Integer)
    projectend = Column('projectend', Integer)
    amount_sponsored = Column('amount_sponsored', Float)
    total_cost = Column('total_cost', Float)
    tid_topic = Column('tid_topic', Integer)
    web_de = Column('web_de', Unicode)
    web_fr = Column('web_fr', Unicode)
    web_it = Column('web_it', Unicode)
    web_en = Column('web_en', Unicode)
    report = Column('report', Unicode)
    mail = Column('mail', Unicode)
    aim_de = Column('aim_de', Unicode)
    aim_fr = Column('aim_fr', Unicode)
    aim_it = Column('aim_it', Unicode)
    aim_en = Column('aim_en', Unicode)
    measure_de = Column('measure_de', Unicode)
    measure_fr = Column('measure_fr', Unicode)
    measure_it = Column('measure_it', Unicode)
    measure_en = Column('measure_en', Unicode)
    subtitle_de = Column('subtitle_de', Unicode)
    subtitle_fr = Column('subtitle_fr', Unicode)
    subtitle_it = Column('subtitle_it', Unicode)
    subtitle_en = Column('subtitle_en', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    description_en = Column('description_en', Unicode)
    topic_de = Column('topic_de', Unicode)
    topic_fr = Column('topic_fr', Unicode)
    topic_it = Column('topic_it', Unicode)
    topic_en = Column('topic_en', Unicode)
    project_sponsor = Column('project_sponsor', Unicode)
    sponsor_type_de = Column('sponsor_type_de', Unicode)
    sponsor_type_fr = Column('sponsor_type_fr', Unicode)
    sponsor_type_it = Column('sponsor_type_it', Unicode)
    sponsor_type_en = Column('sponsor_type_en', Unicode)
    status_de = Column('status_de', Unicode)
    status_fr = Column('status_fr', Unicode)
    status_it = Column('status_it', Unicode)
    status_en = Column('status_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.komo-projekte', KomoProjekte)


class MinergieGebaeude(Base, Vector):
    __tablename__ = 'minergiegebaeude'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/minergiegebaeude.mako'
    __bodId__ = 'ch.bfe.minergiegebaeude'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    certificate = Column('certificate', Unicode)
    standard = Column('standard', Unicode)
    street = Column('street', Unicode)
    streetnr = Column('streetnr', Unicode)
    postcode = Column('postcode', Integer)
    place = Column('place', Unicode)
    canton = Column('canton', Unicode)
    buildinginfo_de = Column('buildinginfo_de', Unicode)
    buildinginfo_fr = Column('buildinginfo_fr', Unicode)
    buildinginfo_it = Column('buildinginfo_it', Unicode)
    buildinginfo_en = Column('buildinginfo_en', Unicode)
    ebf = Column('ebf', Integer)
    http_de = Column('http_de', Unicode)
    http_fr = Column('http_fr', Unicode)
    http_it = Column('http_it', Unicode)
    http_en = Column('http_en', Unicode)
    the_geom = Column(Geometry2D)

register(MinergieGebaeude.__bodId__, MinergieGebaeude)


class StatistikwasserkraftanlagenNew(Base, Vector):
    __tablename__ = 'statistik_wasserkraftanlagen_powerplant'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/statistikwasserkraftanlagen.mako'
    __bodId__ = 'ch.bfe.statistik-wasserkraftanlagen'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('wastanumber', Integer, primary_key=True)
    name = Column('name', Unicode)
    location = Column('location', Unicode)
    canton = Column('canton', Unicode)
    hydropowerplantoperationalstatus_it = Column('hydropowerplantoperationalstatus_it', Unicode)
    hydropowerplanttype_it = Column('hydropowerplanttype_it', Unicode)
    hydropowerplantoperationalstatus_fr = Column('hydropowerplantoperationalstatus_fr', Unicode)
    hydropowerplanttype_fr = Column('hydropowerplanttype_fr', Unicode)
    hydropowerplantoperationalstatus_de = Column('hydropowerplantoperationalstatus_de', Unicode)
    hydropowerplanttype_de = Column('hydropowerplanttype_de', Unicode)
    beginningofoperation = Column('beginningofoperation', Integer)
    endofoperation = Column('endofoperation', Integer)
    dateofstatistic = Column('dateofstatistic', Unicode)
    performanceturbinemaximum = Column('performanceturbinemaximum', Float)
    performancegeneratormaximum = Column('performancegeneratormaximum', Float)
    productionexpected = Column('productionexpected', Float)
    pumpspowerinputmaximum = Column('pumpspowerinputmaximum', Float)
    enginepowerdemand = Column('enginepowerdemand', Float)
    fallheight = Column('fallheight', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.statistik-wasserkraftanlagen', StatistikwasserkraftanlagenNew)


class Erneuerbarheizen(Base, Vector):
    __tablename__ = 'renewable_heating'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/erneuerbarheizen.mako'
    __bodId__ = 'ch.bfe.erneuerbarheizen'
    __label__ = 'company'
    id = Column('xtf_id', Integer, primary_key=True)
    firstname = Column('firstname', Unicode)
    name = Column('name', Unicode)
    company = Column('company', Unicode)
    firstname_name = Column('firstname_name', Unicode)
    email = Column('email', Unicode)
    phonenumber = Column('phonenumber', Unicode)
    street = Column('street', Unicode)
    streetnumber = Column('streetnumber', Unicode)
    street_streetnumber = Column('street_streetnumber', Unicode)
    postalcode = Column('postalcode', Integer)
    place = Column('place', Unicode)
    pc_place = Column('pc_place', Unicode)
    website = Column('website', Unicode)
    privatecontrol = Column('privatecontrol', Unicode)
    additionalinformation = Column('additionalinformation', Unicode)
    de_consulting_type = Column('de_consulting_type', Unicode)
    fr_consulting_type = Column('fr_consulting_type', Unicode)
    it_consulting_type = Column('it_consulting_type', Unicode)
    en_consulting_type = Column('en_consulting_type', Unicode)
    rm_consulting_type = Column('rm_consulting_type', Unicode)
    de_language = Column('de_language', Unicode)
    fr_language = Column('fr_language', Unicode)
    it_language = Column('it_language', Unicode)
    en_language = Column('en_language', Unicode)
    rm_language = Column('rm_language', Unicode)
    de_consultant_cat = Column('de_consultant_cat', Unicode)
    fr_consultant_cat = Column('fr_consultant_cat', Unicode)
    it_consultant_cat = Column('it_consultant_cat', Unicode)
    en_consultant_cat = Column('en_consultant_cat', Unicode)
    rm_consultant_cat = Column('rm_consultant_cat', Unicode)
    consultingcosts = Column('consultingcosts', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.erneuerbarheizen', Erneuerbarheizen)


class StauanlagenBundesaufsicht(Base, Vector):
    __tablename__ = 'stauanlagen_bundesaufsicht'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/stauanlagenbundesaufsicht.mako'
    __bodId__ = 'ch.bfe.stauanlagen-bundesaufsicht'
    __extended_info__ = True
    __queryable_attributes__ = ['damname', 'damtype_de', 'damtype_fr', 'damtype_en']
    __label__ = 'damname'
    id = Column('dam_stabil_id', Integer, primary_key=True)
    damname = Column('damname', Unicode)
    damtype_fr = Column('damtype_fr', Unicode)
    damtype_en = Column('damtype_en', Unicode)
    damtype_de = Column('damtype_de', Unicode)
    damheight = Column('damheight', Integer)
    crestlevel = Column('crestlevel', Integer)
    crestlength = Column('crestlength', Integer)
    facilityname = Column('facilityname', Unicode)
    beginningofoperation = Column('beginningofoperation', Unicode)
    startsupervision = Column('startsupervision', Unicode)
    reservoirname = Column('reservoirname', Unicode)
    impoundmentvolume = Column('impoundmentvolume', Unicode)
    impoundmentlevel = Column('impoundmentlevel', Integer)
    storagelevel = Column('storagelevel', Integer)
    facaim_fr = Column('facaim_fr', Unicode)
    facaim_en = Column('facaim_en', Unicode)
    facaim_de = Column('facaim_de', Unicode)
    has_picture = Column('has_picture', Integer)
    baujahr = Column('baujahr', Integer)
    facility_stabil_id = Column('facility_stabil_id', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfe.stauanlagen-bundesaufsicht', StauanlagenBundesaufsicht)


class Wpsm (Base, Vector):
    __tablename__ = 'wpsm_qualifizierte_firmen'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/wpsm.mako'
    __bodId__ = 'ch.bfe.wpsm-qualifizierte_firmen'
    __queryable_attributes__ = ['company', 'contactperson']
    __label__ = 'company'
    id = Column('xtf_id', Integer, primary_key=True)
    company = Column('company', Unicode)
    contactperson = Column('contactperson', Unicode)
    address1 = Column('address1', Unicode)
    address2 = Column('address2', Unicode)
    postofficebox = Column('postofficebox', Unicode)
    pc_place = Column('pc_place', Unicode)
    telephonenumber = Column('telephonenumber', Unicode)
    mail = Column('mail', Unicode)
    webaddress = Column('webaddress', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.wpsm-qualifizierte_firmen', Wpsm)


class Kleinwasserkraftpotentiale(Base, Vector):
    __tablename__ = 'kleinwasserkraftpotentiale'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/kleinwasserkraftpotentiale.mako'
    __bodId__ = 'ch.bfe.kleinwasserkraftpotentiale'
    __label__ = 'gwlnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    kwprometer = Column('kwprometer', Numeric)
    laenge = Column('laenge', Numeric)
    gwlnr = Column('gwlnr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.kleinwasserkraftpotentiale', Kleinwasserkraftpotentiale)


class WindenergieanlagenFacility(Base, Vector):
    __tablename__ = 'view_windenergieanlagen_facility'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/windenergieanlagen_facility.mako'
    __bodId__ = 'ch.bfe.windenergieanlagen'
    __extended_info__ = True
    __queryable_attributes__ = ['fac_name']
    __label__ = 'fac_name'
    id = Column('fac_id', Unicode, primary_key=True)
    fac_name = Column('fac_name', Unicode)
    fac_type_de = Column('fac_type_de', Unicode)
    fac_type_fr = Column('fac_type_fr', Unicode)
    fac_type_it = Column('fac_type_it', Unicode)
    fac_operator = Column('fac_operator', Unicode)
    fac_website = Column('fac_website', Unicode)
    fac_power = Column('fac_power', Unicode)
    fac_xml_prod = Column('fac_xml_prod', Unicode)
    fac_initial = Column('fac_initial', Unicode)
    fac_y = Column('fac_y', Integer)
    fac_x = Column('fac_x', Integer)
    turbines = Column('turbines', Unicode)
    the_geom = Column(Geometry2D)
    __minscale__ = 100005
    __maxscale__ = 100000005

register('ch.bfe.windenergieanlagen', WindenergieanlagenFacility)


class WindenergieanlagenTurbine(Base, Vector):
    __tablename__ = 'view_windenergieanlagen_turbine'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/windenergieanlagen_turbine.mako'
    __bodId__ = 'ch.bfe.windenergieanlagen'
    __extended_info__ = True
    __queryable_attributes__ = ['fac_name']
    __label__ = 'tur_year'
    id = Column('tur_id', Unicode, primary_key=True)
    fac_name = Column('fac_name', Unicode)
    fac_type_de = Column('fac_type_de', Unicode)
    fac_type_fr = Column('fac_type_fr', Unicode)
    fac_type_it = Column('fac_type_it', Unicode)
    fac_operator = Column('fac_operator', Unicode)
    fac_website = Column('fac_website', Unicode)
    fac_power = Column('fac_power', Unicode)
    fac_xml_prod = Column('fac_xml_prod', Unicode)
    fac_initial = Column('fac_initial', Unicode)
    tur_y = Column('tur_y', Integer)
    tur_x = Column('tur_x', Integer)
    turbines = Column('turbines', Unicode)
    tur_manufacturer = Column('tur_manufacturer', Unicode)
    tur_model = Column('tur_model', Unicode)
    tur_diameter = Column('tur_diameter', Unicode)
    tur_hubheight = Column('tur_hubheight', Unicode)
    tur_power = Column('tur_power', Unicode)
    tur_altitude = Column('tur_altitude', Unicode)
    tur_year = Column('tur_year', Numeric)
    the_geom = Column(Geometry2D)
    __minscale__ = 1
    __maxscale__ = 100005

register('ch.bfe.windenergieanlagen', WindenergieanlagenTurbine)


class MeteoVereisung(Base, Vector):
    __tablename__ = 'meteorologische_vereisung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/meteo_vereisung.mako'
    __bodId__ = 'ch.bfe.meteorologische-vereisung'
    id = Column('bgdi_id', Integer, primary_key=True)
    vereisung = Column('vereisung', Integer, nullable=False)
    hoehe = Column('hoehe', Unicode, nullable=False)
    the_geom = Column(Geometry2D)

register('ch.bfe.meteorologische-vereisung', MeteoVereisung)


class BakomNotruf112Fest(Base, Vector):
    __tablename__ = 'notruf_fn_112'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_fn_112.mako'
    __bodId__ = 'ch.bakom.notruf-112_festnetz'
    __queryable_attributes__ = ['festnetz_112', 'fn_addresse_112']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    festnetz_112 = Column('festnetz_112', Unicode)
    fn_gemeinde_112 = Column('fn_gemeinde_112', Unicode)
    fn_addresse_112 = Column('fn_addresse_112', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-112_festnetz', BakomNotruf112Fest)


class BakomNotruf117Fest(Base, Vector):
    __tablename__ = 'notruf_fn_117'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_fn_117.mako'
    __bodId__ = 'ch.bakom.notruf-117_festnetz'
    __queryable_attributes__ = ['festnetz_117', 'fn_addresse_117']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    festnetz_117 = Column('festnetz_117', Unicode)
    fn_gemeinde_117 = Column('fn_gemeinde_117', Unicode)
    fn_addresse_117 = Column('fn_addresse_117', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-117_festnetz', BakomNotruf117Fest)


class BakomNotruf118Fest(Base, Vector):
    __tablename__ = 'notruf_fn_118'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_fn_118.mako'
    __bodId__ = 'ch.bakom.notruf-118_festnetz'
    __queryable_attributes__ = ['festnetz_118', 'fn_addresse_118']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    festnetz_118 = Column('festnetz_118', Unicode)
    fn_gemeinde_118 = Column('fn_gemeinde_118', Unicode)
    fn_addresse_118 = Column('fn_addresse_118', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-118_festnetz', BakomNotruf118Fest)


class BakomNotruf143Fest(Base, Vector):
    __tablename__ = 'notruf_fn_143'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_fn_143.mako'
    __bodId__ = 'ch.bakom.notruf-143_festnetz'
    __queryable_attributes__ = ['festnetz_143', 'fn_addresse_143']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    festnetz_143 = Column('festnetz_143', Unicode)
    fn_gemeinde_143 = Column('fn_gemeinde_143', Unicode)
    fn_addresse_143 = Column('fn_addresse_143', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-143_festnetz', BakomNotruf143Fest)


class BakomNotruf144Fest(Base, Vector):
    __tablename__ = 'notruf_fn_144'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_fn_144.mako'
    __bodId__ = 'ch.bakom.notruf-144_festnetz'
    __queryable_attributes__ = ['festnetz_144', 'fn_addresse_144']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    festnetz_144 = Column('festnetz_144', Unicode)
    fn_gemeinde_144 = Column('fn_gemeinde_144', Unicode)
    fn_addresse_144 = Column('fn_addresse_144', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-144_festnetz', BakomNotruf144Fest)


class BakomNotruf147Fest(Base, Vector):
    __tablename__ = 'notruf_fn_147'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_fn_147.mako'
    __bodId__ = 'ch.bakom.notruf-147_festnetz'
    __queryable_attributes__ = ['festnetz_147', 'fn_addresse_147']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    festnetz_147 = Column('festnetz_147', Unicode)
    fn_gemeinde_147 = Column('fn_gemeinde_147', Unicode)
    fn_addresse_147 = Column('fn_addresse_147', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-147_festnetz', BakomNotruf147Fest)


class BakomNotruf112Mobil(Base, Vector):
    __tablename__ = 'notruf_mo_112'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_mo_112.mako'
    __bodId__ = 'ch.bakom.notruf-112_mobilnetz'
    __queryable_attributes__ = ['mobile_112', 'mo_addresse_112']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    mobile_112 = Column('mobile_112', Unicode)
    mo_gemeinde_112 = Column('mo_gemeinde_112', Unicode)
    mo_addresse_112 = Column('mo_addresse_112', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-112_mobilnetz', BakomNotruf112Mobil)


class BakomNotruf117Mobil(Base, Vector):
    __tablename__ = 'notruf_mo_117'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_mo_117.mako'
    __bodId__ = 'ch.bakom.notruf-117_mobilnetz'
    __queryable_attributes__ = ['mobile_117', 'mo_addresse_117']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    mobile_117 = Column('mobile_117', Unicode)
    mo_gemeinde_117 = Column('mo_gemeinde_117', Unicode)
    mo_addresse_117 = Column('mo_addresse_117', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-117_mobilnetz', BakomNotruf117Mobil)


class BakomNotruf118Mobil(Base, Vector):
    __tablename__ = 'notruf_mo_118'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_mo_118.mako'
    __bodId__ = 'ch.bakom.notruf-118_mobilnetz'
    __queryable_attributes__ = ['mobile_118', 'mo_addresse_118']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    mobile_118 = Column('mobile_118', Unicode)
    mo_gemeinde_118 = Column('mo_gemeinde_118', Unicode)
    mo_addresse_118 = Column('mo_addresse_118', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-118_mobilnetz', BakomNotruf118Mobil)


class BakomNotruf144Mobil(Base, Vector):
    __tablename__ = 'notruf_mo_144'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_mo_144.mako'
    __bodId__ = 'ch.bakom.notruf-144_mobilnetz'
    __queryable_attributes__ = ['mobile_144', 'mo_addresse_144']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    mobile_144 = Column('mobile_144', Unicode)
    mo_gemeinde_144 = Column('mo_gemeinde_144', Unicode)
    mo_addresse_144 = Column('mo_addresse_144', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-144_mobilnetz', BakomNotruf144Mobil)


class BakomNotruf147Mobil(Base, Vector):
    __tablename__ = 'notruf_mo_147'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_mo_147.mako'
    __bodId__ = 'ch.bakom.notruf-147_mobilnetz'
    __queryable_attributes__ = ['mobile_147', 'mo_addresse_147']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    mobile_147 = Column('mobile_147', Unicode)
    mo_gemeinde_147 = Column('mo_gemeinde_147', Unicode)
    mo_addresse_147 = Column('mo_addresse_147', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-147_mobilnetz', BakomNotruf147Mobil)


class BakomNotruf143Mobil(Base, Vector):
    __tablename__ = 'notruf_mo_143'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_mo_143.mako'
    __bodId__ = 'ch.bakom.notruf-143_mobilnetz'
    __queryable_attributes__ = ['mobile_143', 'mo_addresse_143']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    mobile_143 = Column('mobile_143', Unicode)
    mo_gemeinde_143 = Column('mo_gemeinde_143', Unicode)
    mo_addresse_143 = Column('mo_addresse_143', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-143_mobilnetz', BakomNotruf143Mobil)


class BakomNotruf112Sat(Base, Vector):
    __tablename__ = 'notruf_sa_112'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_sa_112.mako'
    __bodId__ = 'ch.bakom.notruf-112_satellit'
    __queryable_attributes__ = ['satellit_112', 'sa_addresse_112']
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    satellit_112 = Column('satellit_112', Unicode)
    sa_gemeinde_112 = Column('sa_gemeinde_112', Unicode)
    sa_addresse_112 = Column('sa_addresse_112', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-112_satellit', BakomNotruf112Sat)


class BakomNotruf(Base, Vector):
    __tablename__ = 'notruf'
    __table_args__ = ({'schema': 'bakom', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/notruf.mako'
    __bodId__ = 'ch.bakom.notruf'
    __queryable_attributes__ = ['mobile_112', 'mo_addresse_112',
                                'mobile_117', 'mo_addresse_117',
                                'mobile_118', 'mo_addresse_118',
                                'mobile_144', 'mo_addresse_144',
                                'mobile_147', 'mo_addresse_147',
                                'mobile_143', 'mo_addresse_147',
                                'mobile_143', 'mo_addresse_143',
                                'satellit_112', 'sa_addresse_112',
                                'festnetz_112', 'fn_addresse_112',
                                'festnetz_117', 'fn_addresse_117',
                                'festnetz_118', 'fn_addresse_118',
                                'festnetz_143', 'fn_addresse_143',
                                'festnetz_144', 'fn_addresse_144',
                                'festnetz_147', 'fn_addresse_147']
    __extended_info__ = True
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    name = Column('name', Unicode)
    mobile_112 = Column('mobile_112', Unicode)
    mo_gemeinde_112 = Column('mo_gemeinde_112', Unicode)
    mo_addresse_112 = Column('mo_addresse_112', Unicode)
    mobile_117 = Column('mobile_117', Unicode)
    mo_gemeinde_117 = Column('mo_gemeinde_117', Unicode)
    mo_addresse_117 = Column('mo_addresse_117', Unicode)
    mobile_118 = Column('mobile_118', Unicode)
    mo_gemeinde_118 = Column('mo_gemeinde_118', Unicode)
    mo_addresse_118 = Column('mo_addresse_118', Unicode)
    mobile_144 = Column('mobile_144', Unicode)
    mo_gemeinde_144 = Column('mo_gemeinde_144', Unicode)
    mo_addresse_144 = Column('mo_addresse_144', Unicode)
    mobile_147 = Column('mobile_147', Unicode)
    mo_gemeinde_147 = Column('mo_gemeinde_147', Unicode)
    mo_addresse_147 = Column('mo_addresse_147', Unicode)
    mobile_143 = Column('mobile_143', Unicode)
    mo_gemeinde_143 = Column('mo_gemeinde_143', Unicode)
    mo_addresse_143 = Column('mo_addresse_143', Unicode)
    satellit_112 = Column('satellit_112', Unicode)
    sa_gemeinde_112 = Column('sa_gemeinde_112', Unicode)
    sa_addresse_112 = Column('sa_addresse_112', Unicode)
    festnetz_112 = Column('festnetz_112', Unicode)
    fn_gemeinde_112 = Column('fn_gemeinde_112', Unicode)
    fn_addresse_112 = Column('fn_addresse_112', Unicode)
    festnetz_117 = Column('festnetz_117', Unicode)
    fn_gemeinde_117 = Column('fn_gemeinde_117', Unicode)
    fn_addresse_117 = Column('fn_addresse_117', Unicode)
    festnetz_118 = Column('festnetz_118', Unicode)
    fn_gemeinde_118 = Column('fn_gemeinde_118', Unicode)
    fn_addresse_118 = Column('fn_addresse_118', Unicode)
    festnetz_143 = Column('festnetz_143', Unicode)
    fn_gemeinde_143 = Column('fn_gemeinde_143', Unicode)
    fn_addresse_143 = Column('fn_addresse_143', Unicode)
    festnetz_144 = Column('festnetz_144', Unicode)
    fn_gemeinde_144 = Column('fn_gemeinde_144', Unicode)
    fn_addresse_144 = Column('fn_addresse_144', Unicode)
    festnetz_147 = Column('festnetz_147', Unicode)
    fn_gemeinde_147 = Column('fn_gemeinde_147', Unicode)
    fn_addresse_147 = Column('fn_addresse_147', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf', BakomNotruf)


class BakomNotruf112Zentral(Base, Vector):
    __tablename__ = 'notruf'
    __table_args__ = ({'schema': 'bakom', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/notruf_zentral_112.mako'
    __bodId__ = 'ch.bakom.notruf-112_zentral'
    __queryable_attributes__ = []
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    gemeinde_112 = Column('gemeinde_112', Unicode)
    festnetz_112 = Column('festnetz_112', Unicode)
    fn_zentrale_112 = Column('fn_zentrale_112', Unicode)
    mobile_112 = Column('mobile_112', Unicode)
    mo_zentrale_112 = Column('mo_zentrale_112', Unicode)
    satellit_112 = Column('satellit_112', Unicode)
    sa_zentrale_112 = Column('sa_zentrale_112', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-112_zentral', BakomNotruf112Zentral)


class BakomNotruf117Zentral(Base, Vector):
    __tablename__ = 'notruf'
    __table_args__ = ({'schema': 'bakom', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/notruf_zentral_117.mako'
    __bodId__ = 'ch.bakom.notruf-117_zentral'
    __queryable_attributes__ = []
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    gemeinde_117 = Column('gemeinde_112', Unicode)
    festnetz_117 = Column('festnetz_117', Unicode)
    fn_zentrale_117 = Column('fn_zentrale_117', Unicode)
    mobile_117 = Column('mobile_117', Unicode)
    mo_zentrale_117 = Column('mo_zentrale_117', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-117_zentral', BakomNotruf117Zentral)


class BakomNotruf118Zentral(Base, Vector):
    __tablename__ = 'notruf'
    __table_args__ = ({'schema': 'bakom', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/notruf_zentral_118.mako'
    __bodId__ = 'ch.bakom.notruf-118_zentral'
    __queryable_attributes__ = []
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    gemeinde_118 = Column('gemeinde_112', Unicode)
    festnetz_118 = Column('festnetz_118', Unicode)
    fn_zentrale_118 = Column('fn_zentrale_118', Unicode)
    mobile_118 = Column('mobile_118', Unicode)
    mo_zentrale_118 = Column('mo_zentrale_118', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.notruf-118_zentral', BakomNotruf118Zentral)


class Bakomfernsehsender(Base, Vector):
    __tablename__ = 'nisdb_bro'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomfernsehsender.mako'
    __bodId__ = 'ch.bakom.radio-fernsehsender'
    __extended_info__ = True
    __queryable_attributes__ = ['name', 'code']
    __label__ = 'code'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode)
    code = Column('code', Unicode)
    power = Column('power', Unicode)
    service = Column('service', Unicode)
    program = Column('program', Unicode)
    freqchan = Column('freqchan', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.radio-fernsehsender', Bakomfernsehsender)


class RichtfunkVerbindungen(Base, Vector):
    __tablename__ = 'richtfunkverbindungen'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/richtfunkverbindungen.mako'
    __bodId__ = 'ch.bakom.richtfunkverbindungen'
    __label__ = 'link_class'
    id = Column('id', Integer, primary_key=True)
    link_class = Column('link_class', Unicode)
    the_geom = Column(Geometry2D)

register(RichtfunkVerbindungen.__bodId__, RichtfunkVerbindungen)


class Bakomtv(Base, Vector):
    __tablename__ = 'tv_gebiet'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomtv.mako'
    __bodId__ = 'ch.bakom.versorgungsgebiet-tv'
    __queryable_attributes__ = ['prog']
    __label__ = 'prog'
    id = Column('gid', Integer, primary_key=True)
    prog = Column('prog', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.versorgungsgebiet-tv', Bakomtv)


class Bakomukw(Base, Vector):
    __tablename__ = 'ukw_gebiet'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomukw.mako'
    __bodId__ = 'ch.bakom.versorgungsgebiet-ukw'
    __queryable_attributes__ = ['prog']
    __label__ = 'prog'
    id = Column('gid', Integer, primary_key=True)
    prog = Column('prog', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.versorgungsgebiet-ukw', Bakomukw)


class EinschraenkungenDrohnen(Base, Vector):
    __tablename__ = 'einschraenkungen_drohnen'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/einschraenkungen_drohnen.mako'
    __bodId__ = 'ch.bazl.einschraenkungen-drohnen'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_de = Column('name_de', Unicode)
    name_fr = Column('name_fr', Unicode)
    name_it = Column('name_it', Unicode)
    name_en = Column('name_en', Unicode)
    restr_de = Column('restr_de', Unicode)
    restr_fr = Column('restr_fr', Unicode)
    restr_it = Column('restr_it', Unicode)
    restr_en = Column('restr_en', Unicode)
    bew_st_de = Column('bew_st_de', Unicode)
    bew_st_fr = Column('bew_st_fr', Unicode)
    bew_st_it = Column('bew_st_it', Unicode)
    bew_st_en = Column('bew_st_en', Unicode)
    bew_li_de = Column('bew_li_de', Unicode)
    bew_li_fr = Column('bew_li_fr', Unicode)
    bew_li_it = Column('bew_li_it', Unicode)
    bew_li_en = Column('bew_li_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.einschraenkungen-drohnen', EinschraenkungenDrohnen)


class ProjFlughafenanlagen(Base, Vector):
    __tablename__ = 'projektierungszonen'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/projflughafenanlagen.mako'
    __bodId__ = 'ch.bazl.projektierungszonen-flughafenanlagen'
    __label__ = 'municipality'
    id = Column('stabil_id', Integer, primary_key=True)
    zonekind_text_de = Column('zonekind_text_de', Unicode)
    zonekind_text_fr = Column('zonekind_text_fr', Unicode)
    zonekind_text_it = Column('zonekind_text_it', Unicode)
    canton = Column('canton', Unicode)
    municipality = Column('municipality', Unicode)
    legalstatus_text_de = Column('legalstatus_text_de', Unicode)
    legalstatus_text_fr = Column('legalstatus_text_fr', Unicode)
    legalstatus_text_it = Column('legalstatus_text_it', Unicode)
    applicant = Column('applicant', Unicode)
    validfrom = Column('validfrom', Unicode)
    durationofeffect = Column('durationofeffect', Unicode)
    description = Column('description', Unicode)
    weblink_origin = Column('weblink_origin', Unicode)
    bgdi_id = Column('bgdi_id', Integer)
    the_geom = Column(Geometry2D)

register('ch.bazl.projektierungszonen-flughafenanlagen', ProjFlughafenanlagen)


class Luftfahrthindernis(Base, Vector):
    __tablename__ = 'view_luftfahrthindernis'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/luftfahrthindernisse.mako'
    __bodId__ = 'ch.bazl.luftfahrthindernis'
    __extended_info__ = True
    __queryable_attributes__ = ['registrationnumber', 'state', 'maxheightagl', 'startofconstruction',
                                'topelevationamsl', 'totallength', 'bgdi_activesince', 'abortionaccomplished']
    # Must be equal to the mapped value of the column
    __label__ = 'registrationnumber'
    id = Column('bgdi_id', Integer, primary_key=True)
    sanctiontext = Column('sanctiontext', Unicode)
    registrationnumber = Column('registrationnumber', Unicode)
    lk100 = Column('lk100', Unicode)
    obstacletype = Column('obstacletype', Unicode)
    state = Column('state', Unicode)
    maxheightagl = Column('maxheightagl', Integer)
    topelevationamsl = Column('topelevationamsl', Integer)
    totallength = Column('totallength', Integer)
    startofconstruction = Column('startofconstruction', Date)
    bgdi_activesince = Column('bgdi_activesince', Date)
    duration = Column('duration', Unicode)
    geomtype = Column('geomtype', Unicode)
    abortionaccomplished = Column('abortionaccomplished', Date)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.luftfahrthindernis', Luftfahrthindernis)


class LuftfahrtRecht(Base, Vector):
    __tablename__ = 'bebaute_gebiete'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.bebaute-gebiete_luftfahrtrecht'
    id = Column('bgdi_id', Integer, primary_key=True)
    bebaut = Column('bebaut', Boolean)
    the_geom = Column(Geometry2D)

register(LuftfahrtRecht.__bodId__, LuftfahrtRecht)


class LuftraeumeBase:
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/luftraeume_fluginformationsgebiet.mako'
    __label__ = u'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    designator = Column('designator', Unicode)
    type = Column('type', Unicode)
    loli_value = Column('loli_value', Integer)
    loli_type = Column('loli_type', Unicode)
    upli_value = Column('upli_value', Integer)
    upli_type = Column('upli_type', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)


class LuftraeumeFluginformationsGebiet(Base, LuftraeumeBase, Vector):
    __returnedGeometry__ = 'the_geom_highlight'
    __tablename__ = 'luftraeume_fluginformationsgebiet'
    __bodId__ = 'ch.bazl.luftraeume-fluginformationsgebiet'
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bazl.luftraeume-fluginformationsgebiet', LuftraeumeFluginformationsGebiet)


class LuftraeumeFluginformationsZonen(Base, LuftraeumeBase, Vector):
    __tablename__ = 'luftraeume_fluginformationszonen'
    __bodId__ = 'ch.bazl.luftraeume-fluginformationszonen'

register('ch.bazl.luftraeume-fluginformationszonen', LuftraeumeFluginformationsZonen)


class LuftraeumeKontrollBezirke(Base, LuftraeumeBase, Vector):
    __returnedGeometry__ = 'the_geom_highlight'
    __tablename__ = 'luftraeume_kontrollbezirke'
    __bodId__ = 'ch.bazl.luftraeume-kontrollbezirke'
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bazl.luftraeume-kontrollbezirke', LuftraeumeKontrollBezirke)


class LuftraeumeKontrollZonen(Base, LuftraeumeBase, Vector):
    __tablename__ = 'luftraeume_kontrollzonen'
    __bodId__ = 'ch.bazl.luftraeume-kontrollzonen'

register('ch.bazl.luftraeume-kontrollzonen', LuftraeumeKontrollZonen)


class LuftraeumeNahKontrollBezirke(Base, LuftraeumeBase, Vector):
    __tablename__ = 'luftraeume_nahkontrollbezirke'
    __bodId__ = 'ch.bazl.luftraeume-nahkontrollbezirke'

register('ch.bazl.luftraeume-nahkontrollbezirke', LuftraeumeNahKontrollBezirke)


class HindernisbegrenzungsflaechenPerimeter(Base, Vector):
    __tablename__ = 'hindernisbegrenzungsflaechen_perimeter'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __bodId__ = 'ch.bazl.hindernisbegrenzungsflaechen-perimeter'
    id = Column('bgdi_id', Integer, primary_key=True)
    feature_id = Column('id', Integer)
    icao = Column('icao', Unicode)
    name = Column('name', Unicode)
    status = Column('status', Integer)
    the_geom = Column(Geometry2D)

register('ch.bazl.hindernisbegrenzungsflaechen-perimeter', HindernisbegrenzungsflaechenPerimeter)


class AstraStrasseFacilitiesA(Base, Vector):
    __tablename__ = 'sachplan_strasse_fac_anhorung'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_strasse_facilities.mako'
    __bodId__ = 'ch.astra.sachplan-infrastruktur-strasse_anhoerung'
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    fackind_tid = Column('fackind_tid', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)
    facstatus_tid = Column('facstatus_tid', Unicode)
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    doc_web = Column('doc_web', Unicode)
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)


class AstraStrassePlanningA(Base, Vector):
    __tablename__ = 'sachplan_strasse_pl_anhorung'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_strasse_planning.mako'
    __bodId__ = 'ch.astra.sachplan-infrastruktur-strasse_anhoerung'
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_tid = Column('coordlevel_tid', Unicode)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)


class AstraStrassePlanningRasterA(Base, Vector):
    __tablename__ = 'sachplan_strasse_pl_r_anhorung'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_strasse_planning.mako'
    __bodId__ = 'ch.astra.sachplan-infrastruktur-strasse_anhoerung'
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_tid = Column('coordlevel_tid', Unicode)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 1
    __maxscale__ = 20005
    the_geom = Column(Geometry2D)

register('ch.astra.sachplan-infrastruktur-strasse_anhoerung', AstraStrasseFacilitiesA)
register('ch.astra.sachplan-infrastruktur-strasse_anhoerung', AstraStrassePlanningA)
register('ch.astra.sachplan-infrastruktur-strasse_anhoerung', AstraStrassePlanningRasterA)


class AstraStrasseFacilitiesK(Base, Vector):
    __tablename__ = 'sachplan_strasse_fac_kraft'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_strasse_facilities.mako'
    __bodId__ = 'ch.astra.sachplan-infrastruktur-strasse_kraft'
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    fackind_tid = Column('fackind_tid', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)
    facstatus_tid = Column('facstatus_tid', Unicode)
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    doc_web = Column('doc_web', Unicode)
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)


class AstraStrassePlanningK(Base, Vector):
    __tablename__ = 'sachplan_strasse_pl_kraft'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_strasse_planning.mako'
    __bodId__ = 'ch.astra.sachplan-infrastruktur-strasse_kraft'
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_tid = Column('coordlevel_tid', Unicode)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)


class AstraStrassePlanningRasterK(Base, Vector):
    __tablename__ = 'sachplan_strasse_pl_r_kraft'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_strasse_planning.mako'
    __bodId__ = 'ch.astra.sachplan-infrastruktur-strasse_kraft'
    __label__ = 'plname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    meastype_tid = Column('meastype_tid', Unicode)
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_tid = Column('coordlevel_tid', Unicode)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 1
    __maxscale__ = 20005
    the_geom = Column(Geometry2D)

register('ch.astra.sachplan-infrastruktur-strasse_kraft', AstraStrasseFacilitiesK)
register('ch.astra.sachplan-infrastruktur-strasse_kraft', AstraStrassePlanningK)
register('ch.astra.sachplan-infrastruktur-strasse_kraft', AstraStrassePlanningRasterK)


class BiogasFacilities(Base, Vector):
    __tablename__ = 'biogasanlagen'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/bfe_biogasanlagen.mako'
    __bodId__ = 'ch.bfe.biogasanlagen'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    plant_id = Column('plant_id', Integer)
    name = Column('name', Unicode)
    place = Column('place', Unicode)
    operator = Column('operator', Unicode)
    beginingofoperation = Column('beginingofoperation', Integer)
    web = Column('web', Unicode)
    combinedheatandpower = Column('combinedheatandpower', Integer)
    upgradingcapacity = Column('upgradingcapacity', Integer)
    facilitykind = Column('facilitykind', Integer)
    facilitykind_en = Column('facilitykind_en', Unicode)
    facilitykind_de = Column('facilitykind_de', Unicode)
    facilitykind_fr = Column('facilitykind_fr', Unicode)
    facilitykind_it = Column('facilitykind_it', Unicode)
    upgradingtechnology = Column('upgradingtechnology', Integer)
    upgradingtechnology_en = Column('upgradingtechnology_en', Unicode)
    upgradingtechnology_de = Column('upgradingtechnology_de', Unicode)
    upgradingtechnology_fr = Column('upgradingtechnology_fr', Unicode)
    upgradingtechnology_it = Column('upgradingtechnology_it', Unicode)
    valorizationtype = Column('valorizationtype', Integer)
    valorizationtype_en = Column('valorizationtype_en', Unicode)
    valorizationtype_de = Column('valorizationtype_de', Unicode)
    valorizationtype_fr = Column('valorizationtype_fr', Unicode)
    valorizationtype_it = Column('valorizationtype_it', Unicode)
    yearly_production = Column('yearly_production', JsonChsdi)
    the_geom = Column(Geometry2D)

register('ch.bfe.biogasanlagen', BiogasFacilities)


class SachPGFacilities(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_fac_pt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['facptname_de', 'facptname_fr', 'facptname_it']
    # Translatable labels in fr, it
    __label__ = 'facptname_de'
    id = Column('facpt_id', Integer, primary_key=True)
    facptname_de = Column('facptname_de', Unicode)
    facptname_fr = Column('facptname_fr', Unicode)
    facptname_it = Column('facptname_it', Unicode)
    fackind_de = Column('fackind_de', Unicode)
    fackind_fr = Column('fackind_fr', Unicode)
    fackind_it = Column('fackind_it', Unicode)
    planningstatus_de = Column('planningstatus_de', Unicode)
    planningstatus_fr = Column('planningstatus_fr', Unicode)
    planningstatus_it = Column('planningstatus_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    description = Column('description', Unicode)
    web_de = Column('web_de', Unicode)
    web_fr = Column('web_fr', Unicode)
    web_it = Column('web_it', Unicode)
    __minscale__ = 99999
    the_geom = Column(Geometry2D)


class SachPGPlanning(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_pm_pt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning_pt.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['pmname_de', 'pmname_fr', 'pmname_it']
    # Translatable labels in fr, it
    __label__ = 'pmname_de'
    id = Column('pmpt_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    pmname_fr = Column('pmname_fr', Unicode)
    pmname_it = Column('pmname_it', Unicode)
    pmname_de = Column('pmname_de', Unicode)
    pmkind_de = Column('pmkind_de', Unicode)
    pmkind_fr = Column('pmkind_fr', Unicode)
    pmkind_it = Column('pmkind_it', Unicode)
    coordlevel_de = Column('coordlevel_de', Unicode)
    coordlevel_fr = Column('coordlevel_fr', Unicode)
    coordlevel_it = Column('coordlevel_it', Unicode)
    planningstatus_de = Column('planningstatus_de', Unicode)
    planningstatus_fr = Column('planningstatus_fr', Unicode)
    planningstatus_it = Column('planningstatus_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description = Column('description', Unicode)
    web_de = Column('web_de', Unicode)
    web_fr = Column('web_fr', Unicode)
    web_it = Column('web_it', Unicode)
    __minscale__ = 24999
    __maxscale__ = 499999


class SachPGAreaPlanningNotMT6(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_pm_area_not_mt6'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['pmname_de', 'pmname_fr', 'pmname_it']
    # Translatable labels in fr, it
    __label__ = 'pmname_de'
    id = Column('pmarea_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    pmname_fr = Column('pmname_fr', Unicode)
    pmname_it = Column('pmname_it', Unicode)
    pmname_de = Column('pmname_de', Unicode)
    pmkind_de = Column('pmkind_de', Unicode)
    pmkind_fr = Column('pmkind_fr', Unicode)
    pmkind_it = Column('pmkind_it', Unicode)
    coordlevel_de = Column('coordlevel_de', Unicode)
    coordlevel_fr = Column('coordlevel_fr', Unicode)
    coordlevel_it = Column('coordlevel_it', Unicode)
    planningstatus_de = Column('planningstatus_de', Unicode)
    planningstatus_fr = Column('planningstatus_fr', Unicode)
    planningstatus_it = Column('planningstatus_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description = Column('description', Unicode)
    web_de = Column('web_de', Unicode)
    web_fr = Column('web_fr', Unicode)
    web_it = Column('web_it', Unicode)
    __maxscale__ = 499999


class SachPGAreaPlanningMT6(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_pm_area_mt6'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['pmname_de', 'pmname_fr', 'pmname_it']
    # Translatable labels in fr, it
    __label__ = 'pmname_de'
    id = Column('pmarea_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    pmname_fr = Column('pmname_fr', Unicode)
    pmname_it = Column('pmname_it', Unicode)
    pmname_de = Column('pmname_de', Unicode)
    pmkind_de = Column('pmkind_de', Unicode)
    pmkind_fr = Column('pmkind_fr', Unicode)
    pmkind_it = Column('pmkind_it', Unicode)
    coordlevel_de = Column('coordlevel_de', Unicode)
    coordlevel_fr = Column('coordlevel_fr', Unicode)
    coordlevel_it = Column('coordlevel_it', Unicode)
    planningstatus_de = Column('planningstatus_de', Unicode)
    planningstatus_fr = Column('planningstatus_fr', Unicode)
    planningstatus_it = Column('planningstatus_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description = Column('description', Unicode)
    web_de = Column('web_de', Unicode)
    web_fr = Column('web_fr', Unicode)
    web_it = Column('web_it', Unicode)
    __maxscale__ = 24999

register('ch.bfe.sachplan-geologie-tiefenlager', SachPGFacilities)
register('ch.bfe.sachplan-geologie-tiefenlager', SachPGPlanning)
register('ch.bfe.sachplan-geologie-tiefenlager', SachPGAreaPlanningNotMT6)
register('ch.bfe.sachplan-geologie-tiefenlager', SachPGAreaPlanningMT6)


class SilFacilitiesA(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_facilities_anhorung'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_facilities.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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


class SilPlanningA(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_plmeasures_anhorung'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_planning.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    measuretype_text_de = Column('measuretype_text_de', Unicode)
    measuretype_text_fr = Column('measuretype_text_fr', Unicode)
    measuretype_text_it = Column('measuretype_text_it', Unicode)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Unicode)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Unicode)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Unicode)
    planningstatus_text_de = Column('planningstatus_text_de', Unicode)
    planningstatus_text_fr = Column('planningstatus_text_fr', Unicode)
    planningstatus_text_it = Column('planningstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)


class SilPlanningRasterA(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_plmeasures_r_anhorung'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_planning.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    measuretype_text_de = Column('measuretype_text_de', Unicode)
    measuretype_text_fr = Column('measuretype_text_fr', Unicode)
    measuretype_text_it = Column('measuretype_text_it', Unicode)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Unicode)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Unicode)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Unicode)
    planningstatus_text_de = Column('planningstatus_text_de', Unicode)
    planningstatus_text_fr = Column('planningstatus_text_fr', Unicode)
    planningstatus_text_it = Column('planningstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung', SilFacilitiesA)
register('ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung', SilPlanningA)
register('ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung', SilPlanningRasterA)


class SilFacilitiesK(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_facilities_kraft'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_facilities.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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


class SilPlanningK(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_plmeasures_kraft'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_planning.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    measuretype_text_de = Column('measuretype_text_de', Unicode)
    measuretype_text_fr = Column('measuretype_text_fr', Unicode)
    measuretype_text_it = Column('measuretype_text_it', Unicode)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Unicode)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Unicode)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Unicode)
    planningstatus_text_de = Column('planningstatus_text_de', Unicode)
    planningstatus_text_fr = Column('planningstatus_text_fr', Unicode)
    planningstatus_text_it = Column('planningstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)


class SilPlanningRasterK(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_plmeasures_r_kraft'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_planning.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    plname_de = Column('plname_de', Unicode)
    plname_fr = Column('plname_fr', Unicode)
    plname_it = Column('plname_it', Unicode)
    measuretype_text_de = Column('measuretype_text_de', Unicode)
    measuretype_text_fr = Column('measuretype_text_fr', Unicode)
    measuretype_text_it = Column('measuretype_text_it', Unicode)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Unicode)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Unicode)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Unicode)
    planningstatus_text_de = Column('planningstatus_text_de', Unicode)
    planningstatus_text_fr = Column('planningstatus_text_fr', Unicode)
    planningstatus_text_it = Column('planningstatus_text_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    validuntil = Column('validuntil', Unicode)
    description_text_de = Column('description_text_de', Unicode)
    description_text_fr = Column('description_text_fr', Unicode)
    description_text_it = Column('description_text_it', Unicode)
    document_web = Column('document_web', Unicode)
    document_title = Column('document_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)


register('ch.bazl.sachplan-infrastruktur-luftfahrt_kraft', SilFacilitiesK)
register('ch.bazl.sachplan-infrastruktur-luftfahrt_kraft', SilPlanningK)
register('ch.bazl.sachplan-infrastruktur-luftfahrt_kraft', SilPlanningRasterK)


class NgaAnbieter(Base, Vector):
    __tablename__ = 'nga_anbieter'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/ngamapping.mako'
    __bodId__ = 'ch.bakom.anbieter-eigenes_festnetz'
    __label__ = 'alias'
    id = Column('cellid', Integer, primary_key=True)
    alias = Column('alias', Unicode)
    fdaurl = Column('fdaurl', Unicode)
    nbofprovider = Column('nbofprovider', Integer)
    the_geom = Column(Geometry2D)

register('ch.bakom.anbieter-eigenes_festnetz', NgaAnbieter)


class Kernkraftwerke(Base, Vector):
    __tablename__ = 'kernkraftwerke'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/kernkraftwerke.mako'
    __bodId__ = 'ch.bfe.kernkraftwerke'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('plant_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    operator = Column('operator', Unicode)
    owner = Column('owner', Unicode)
    enforcement_1 = Column('enforcement_1', Unicode)
    enforcement_2 = Column('enforcement_2', Unicode)
    enforcement_3 = Column('enforcement_3', Unicode)
    regulatory = Column('regulatory', Unicode)
    license_de = Column('license_de', Unicode)
    license_fr = Column('license_fr', Unicode)
    license_it = Column('license_it', Unicode)
    license_en = Column('license_en', Unicode)
    municipality = Column('municipality', Unicode)
    canton = Column('canton', Unicode)
    reactor_name = Column('reactor_name', Unicode)
    reactors = Column('reactors', Integer)
    life_phase_de = Column('life_phase_de', Unicode)
    life_phase_fr = Column('life_phase_fr', Unicode)
    life_phase_it = Column('life_phase_it', Unicode)
    life_phase_en = Column('life_phase_en', Unicode)
    reactor_type_de = Column('reactor_type_de', Unicode)
    reactor_type_fr = Column('reactor_type_fr', Unicode)
    reactor_type_it = Column('reactor_type_it', Unicode)
    reactor_type_en = Column('reactor_type_en', Unicode)
    cooling_type_de = Column('cooling_type_de', Unicode)
    cooling_type_fr = Column('cooling_type_fr', Unicode)
    cooling_type_it = Column('cooling_type_it', Unicode)
    cooling_type_en = Column('cooling_type_en', Unicode)
    nominal_thermal_output = Column('nominal_thermal_output', Unicode)
    gross_el_output = Column('gross_el_output', Unicode)
    net_el_output = Column('net_el_output', Unicode)
    construction_phase = Column('construction_phase', Unicode)
    commissioning_phase = Column('commissioning_phase', Unicode)
    operation_phase = Column('operation_phase', Unicode)
    decontamination_phase = Column('decontamination_phase', Unicode)
    dismantling_phase = Column('dismantling_phase', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.kernkraftwerke', Kernkraftwerke)


class Kehrichtverbrennungsanlagen(Base, Vector):
    __tablename__ = 'kehrichtverbrennungsanlagen'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/kehrichtverbrennungsanlagen.mako'
    __bodId__ = 'ch.bfe.kehrichtverbrennungsanlagen'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    wasteincinerationplantr = Column('wasteincinerationplantr', Unicode)
    xtf_id = Column('xtf_id', Unicode)
    number_id = Column('number_id', Integer)
    name = Column('name', Unicode)
    place = Column('place', Unicode)
    beginningofoperation = Column('beginningofoperation', Integer)
    web = Column('web', Unicode)
    year = Column('year', Integer)
    recycledwaste = Column('recycledwaste', Float)
    electricity = Column('electricity', Float)
    heat = Column('heat', Float)
    the_geom = Column(Geometry2D)

register('ch.bfe.kehrichtverbrennungsanlagen', Kehrichtverbrennungsanlagen)


class ThermischeNetzeGeometry(Base, Vector):
    __tablename__ = 'thermische_netze_geometry'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/thermischenetze.mako'
    __bodId__ = 'ch.bfe.thermische-netze'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('xtf_id', Unicode, primary_key=True)
    name = Column('name', Unicode)
    operator = Column('operator', Unicode)
    contact = Column('contact', Unicode)
    de_enersource_main = Column('de_enersource_main', Unicode)
    fr_enersource_main = Column('fr_enersource_main', Unicode)
    it_enersource_main = Column('it_enersource_main', Unicode)
    en_enersource_main = Column('en_enersource_main', Unicode)
    zip = Column('zip', Integer)
    place = Column('place', Unicode)
    operatoraddress = Column('operatoraddress', Unicode)
    phone = Column('phone', Unicode)
    web = Column('web', Unicode)
    mail = Column('mail', Unicode)
    beginningofoperation = Column('beginningofoperation', Integer)
    power = Column('power', Float)
    energy = Column('energy', Integer)
    houseconnections = Column('houseconnections', Integer)
    netlength = Column('netlength', Float)
    de_energysource = Column('de_energysource', Unicode)
    fr_energysource = Column('fr_energysource', Unicode)
    it_energysource = Column('it_energysource', Unicode)
    en_energysource = Column('en_energysource', Unicode)
    de_positionaccuracy = Column('de_positionaccuracy', Unicode)
    fr_positionaccuracy = Column('fr_positionaccuracy', Unicode)
    it_positionaccuracy = Column('it_positionaccuracy', Unicode)
    en_positionaccuracy = Column('en_positionaccuracy', Unicode)
    x = Column('x', Float)
    y = Column('y', Float)
    the_geom = Column(Geometry2D)

register('ch.bfe.thermische-netze', ThermischeNetzeGeometry)


class SisFacilitiesA(Base, Vector):
    __tablename__ = 'sis_fac_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_anhorung'
    __template__ = 'templates/htmlpopup/sis_facilities.mako'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schiene_anhorung', SisFacilitiesA)


class SisPlanningA(Base, Vector):
    __tablename__ = 'sis_pl_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_anhorung'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schiene_anhorung', SisPlanningA)


class SisAngaben(Base, Vector):
    __tablename__ = 'sis_angaben'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_angaben.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_ausgangslage'
    __queryable_attributes__ = ['name', 'description_fr', 'description_it', 'description_de']
    __label__ = 'name'
    id = Column('anlage_id', Unicode, primary_key=True)
    name = Column('name', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)
    valid_from = Column('valid_from', Unicode)
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schiene_ausgangslage', SisAngaben)


class SisPlanningRasterA(Base, Vector):
    __tablename__ = 'sis_pl_r_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_anhorung'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schiene_anhorung', SisPlanningRasterA)


class SisFacilitiesK(Base, Vector):
    __tablename__ = 'sis_fac_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_facilities.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_kraft'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schiene_kraft', SisFacilitiesK)


class SisPlanningK(Base, Vector):
    __tablename__ = 'sis_pl_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_kraft'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schiene_kraft', SisPlanningK)


class SisPlanningRasterK(Base, Vector):
    __tablename__ = 'sis_pl_r_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_kraft'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schiene_kraft', SisPlanningRasterK)


class KbsZivilflugpl(Base, Vector):
    __tablename__ = 'kataster_belasteter_standorte_zivflpl'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/kataster_belasteter_standorte_zivflpl.mako'
    __bodId__ = 'ch.bazl.kataster-belasteter-standorte-zivilflugplaetze'
    __queryable_attributes__ = ['katasternummer']
    __label__ = 'katasternummer'
    id = Column('vflz_id', Integer, primary_key=True)
    katasternummer = Column('katasternummer', Unicode)
    standorttyp_de = Column('standorttyp_de', Unicode)
    standorttyp_fr = Column('standorttyp_fr', Unicode)
    standorttyp_it = Column('standorttyp_it', Unicode)
    statusaltlv_de = Column('statusaltlv_de', Unicode)
    statusaltlv_fr = Column('statusaltlv_fr', Unicode)
    statusaltlv_it = Column('statusaltlv_it', Unicode)
    untersuchungsstand_de = Column('untersuchungsstand_de', Unicode)
    untersuchungsstand_fr = Column('untersuchungsstand_fr', Unicode)
    untersuchungsstand_it = Column('untersuchungsstand_it', Unicode)
    url = Column('url', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.kataster-belasteter-standorte-zivilflugplaetze', KbsZivilflugpl)


class SchutzgebieteAulavLiechtenstein(Base, Vector):
    __tablename__ = 'schutzgebiete_aulav_liechtenstein'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/schutzgebiete_aulav_liechtenstein.mako'
    __bodId__ = 'ch.bazl.schutzgebiete-aulav_liechtenstein'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bazl.schutzgebiete-aulav_liechtenstein', SchutzgebieteAulavLiechtenstein)


class AnlageSchienengueterverkehr:
    __tablename__ = 'anlagen_schienengueterverkehr_tooltip'
    __table_args__ = ({'schema': 'bav', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/anlagen_schienengueterverkehr.mako'
    __bodId__ = 'ch.bav.anlagen-schienengueterverkehr'
    __queryable_attributes__ = ['dst_nr', 'name', 'dst_abk']
    __label__ = 'name'
    __returnedGeometry__ = 'the_geom_point'
    id = Column('bgdi_id', Integer, primary_key=True)
    dst_nr = Column('dst_nr', Integer)
    name = Column('name', Unicode)
    dst_abk = Column('dst_abk', Unicode)
    isb = Column('isb', Unicode)
    typ = Column('typ', Integer)
    typ_de = Column('typ_de', Unicode)
    typ_fr = Column('typ_fr', Unicode)
    typ_it = Column('typ_it', Unicode)
    the_geom_point = Column('the_geom', Geometry2D)


class AnlageSchienengueterverkehrZoom1(Base, AnlageSchienengueterverkehr, Vector):
    __minscale__ = 1
    __maxscale__ = 4000
    the_geom = Column('the_geom_click', Geometry2D)

register(AnlageSchienengueterverkehr.__bodId__, AnlageSchienengueterverkehrZoom1)


class AnlageSchienengueterverkehrZoom2(Base, AnlageSchienengueterverkehr, Vector):
    __minscale__ = 4000
    the_geom = Column('the_geom_click_overview', Geometry2D)

register(AnlageSchienengueterverkehr.__bodId__, AnlageSchienengueterverkehrZoom2)


class LaermBelastungEinsenbahnTatsaechlicheEmissionTag(Base, Vector):
    __tablename__ = 'laerm_eisenbahn_tatsaechliche_emissionen_tag'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_tatsaechliche_emissionen_tag.mako'
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    kml_number = Column('kml_number', Integer)
    km_from = Column('km_from', Float)
    km_to = Column('km_to', Float)
    lre_day = Column('lre_day', Float)
    enmodel_railway = Column('enmodel_railway', Unicode)
    enmodelrailway_de = Column('enmodelrailway_de', Unicode)
    enmodelrailway_fr = Column('enmodelrailway_fr', Unicode)
    enmodelrailway_it = Column('enmodelrailway_it', Unicode)
    enmodelrailway_en = Column('enmodelrailway_en', Unicode)
    level_correction_day = Column('level_correction_day', Float)
    train_number_day = Column('train_number_day', Float)
    train_number_freight_d = Column('train_number_freight_d', Float)
    lre_remark = Column('lre_remark', Unicode)
    year_evaluation = Column('year_evaluation', Integer)
    the_geom = Column(Geometry2D)

register('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_tag', LaermBelastungEinsenbahnTatsaechlicheEmissionTag)


class LaermBelastungEinsenbahnTatsaechlicheEmissionNacht(Base, Vector):
    __tablename__ = 'laerm_eisenbahn_tatsaechliche_emissionen_nacht'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_tatsaechliche_emissionen_nacht.mako'
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    kml_number = Column('kml_number', Integer)
    km_from = Column('km_from', Float)
    km_to = Column('km_to', Float)
    lre_night = Column('lre_night', Float)
    enmodel_railway = Column('enmodel_railway', Unicode)
    enmodelrailway_de = Column('enmodelrailway_de', Unicode)
    enmodelrailway_fr = Column('enmodelrailway_fr', Unicode)
    enmodelrailway_it = Column('enmodelrailway_it', Unicode)
    enmodelrailway_en = Column('enmodelrailway_en', Unicode)
    level_correction_night = Column('level_correction_night', Float)
    train_number_night = Column('train_number_night', Float)
    train_number_freight_n = Column('train_number_freight_n', Float)
    lre_remark = Column('lre_remark', Unicode)
    year_evaluation = Column('year_evaluation', Integer)
    the_geom = Column(Geometry2D)

register('ch.bav.laermbelastung-eisenbahn_tatsaechliche_emissionen_nacht', LaermBelastungEinsenbahnTatsaechlicheEmissionNacht)


class LaermBelastungEinsenbahnFestgelegteEmissionTag(Base, Vector):
    __tablename__ = 'laerm_eisenbahn_festgelegte_emissionen_tag'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_festgelegte_emissionen_tag.mako'
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    kml_number = Column('kml_number', Integer)
    km_from = Column('km_from', Float)
    km_to = Column('km_to', Float)
    lre_max_day = Column('lre_max_day', Float)
    lre_max_remark = Column('lre_max_remark', Unicode)
    lre_max_date = Column('lre_max_date', Date)
    lre_max_year = Column('lre_max_year', Integer)
    lre_remark = Column('lre_remark', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_tag', LaermBelastungEinsenbahnFestgelegteEmissionTag)


class LaermBelastungEinsenbahnFestgelegteEmissionNacht(Base, Vector):
    __tablename__ = 'laerm_eisenbahn_festgelegte_emissionen_nacht'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_festgelegte_emissionen_nacht.mako'
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    kml_number = Column('kml_number', Integer)
    km_from = Column('km_from', Float)
    km_to = Column('km_to', Float)
    lre_max_night = Column('lre_max_night', Float)
    lre_max_remark = Column('lre_max_remark', Unicode)
    lre_max_date = Column('lre_max_date', Date)
    lre_max_year = Column('lre_max_year', Integer)
    lre_remark = Column('lre_remark', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.laermbelastung-eisenbahn_festgelegte_emissionen_nacht', LaermBelastungEinsenbahnFestgelegteEmissionNacht)


class LaermBelastungEisenbahnEffektiveImmissionen:
    __tablename__ = 'laermbelastung_eisenbahn_eff_immissionen'
    __table_args__ = ({'schema': 'bav', 'autoload': False, 'extend_existing': True})
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    de_es = Column('de_es', Unicode)
    fr_es = Column('fr_es', Unicode)
    it_es = Column('it_es', Unicode)
    en_es = Column('en_es', Unicode)
    rm_es = Column('rm_es', Unicode)
    de_pointofdetermination = Column('de_pointofdetermination', Unicode)
    fr_pointofdetermination = Column('fr_pointofdetermination', Unicode)
    it_pointofdetermination = Column('it_pointofdetermination', Unicode)
    en_pointofdetermination = Column('en_pointofdetermination', Unicode)
    rm_pointofdetermination = Column('rm_pointofdetermination', Unicode)
    de_operation_status = Column('de_operation_status', Unicode)
    fr_operation_status = Column('fr_operation_status', Unicode)
    it_operation_status = Column('it_operation_status', Unicode)
    en_operation_status = Column('en_operation_status', Unicode)
    rm_operation_status = Column('rm_operation_status', Unicode)
    floor = Column('floor', Unicode)
    receptor = Column('receptor', Unicode)
    the_geom = Column(Geometry2D)


class LaermBelastungEisenbahnEffektiveImmissionenNacht(Base, LaermBelastungEisenbahnEffektiveImmissionen, Vector):
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht'
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_effektive_immissionen_nacht.mako'
    lr_night = Column('lr_night', Float)

register('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_nacht', LaermBelastungEisenbahnEffektiveImmissionenNacht)


class LaermBelastungEisenbahnEffektiveImmissionenTag(Base, LaermBelastungEisenbahnEffektiveImmissionen, Vector):
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag'
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_effektive_immissionen_tag.mako'
    lr_day = Column('lr_day', Float)

register('ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag', LaermBelastungEisenbahnEffektiveImmissionenTag)


class LaermBelastungEisenbahnZulaessigeImmissionen:
    __tablename__ = 'laerm_eisenbahn_zulaessig_immissionen'
    __table_args__ = ({'schema': 'bav', 'autoload': False, 'extend_existing': True})
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    lr_max_year = Column('lr_max_year', Integer)
    de_es = Column('de_es', Unicode)
    fr_es = Column('fr_es', Unicode)
    it_es = Column('it_es', Unicode)
    en_es = Column('en_es', Unicode)
    rm_es = Column('rm_es', Unicode)
    de_pointofdetermination_t = Column('de_pointofdetermination_t', Unicode)
    fr_pointofdetermination_t = Column('fr_pointofdetermination_t', Unicode)
    it_pointofdetermination_t = Column('it_pointofdetermination_t', Unicode)
    en_pointofdetermination_t = Column('en_pointofdetermination_t', Unicode)
    rm_pointofdetermination_t = Column('rm_pointofdetermination_t', Unicode)
    floor = Column('floor', Unicode)
    the_geom = Column(Geometry2D)


class LaermBelastungEisenbahnZulaessigeImmissionenNacht(Base, LaermBelastungEisenbahnZulaessigeImmissionen, Vector):
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht'
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_zulaessige_immissionen_nacht.mako'
    lr_max_night = Column('lr_max_night', Float)

register('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_nacht', LaermBelastungEisenbahnZulaessigeImmissionenNacht)


class LaermBelastungEisenbahnZulaessigeImmissionenTag(Base, LaermBelastungEisenbahnZulaessigeImmissionen, Vector):
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag'
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_zulaessige_immissionen_tag.mako'
    lr_max_day = Column('lr_max_day', Float)

register('ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag', LaermBelastungEisenbahnZulaessigeImmissionenTag)


class SifFacilitiesA(Base, Vector):
    __tablename__ = 'sif_fac_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung'
    __template__ = 'templates/htmlpopup/sif_facilities.mako'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung', SifFacilitiesA)


class SifFacilitiesK(Base, Vector):
    __tablename__ = 'sif_fac_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_kraft'
    __template__ = 'templates/htmlpopup/sif_facilities.mako'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_kraft', SifFacilitiesK)


class SifPlanningA(Base, Vector):
    __tablename__ = 'sif_pl_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung', SifPlanningA)


class SifPlanningK(Base, Vector):
    __tablename__ = 'sif_pl_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_kraft'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_kraft', SifPlanningK)


class SifPlanningRasterA(Base, Vector):
    __tablename__ = 'sif_pl_r_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung', SifPlanningRasterA)


class SifPlanningRasterK(Base, Vector):
    __tablename__ = 'sif_pl_r_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_kraft'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_kraft', SifPlanningRasterK)


class SifAusgangslage(Base, Vector):
    __tablename__ = 'sif_ausgangslage'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_angaben.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_ausgangslage'
    __queryable_attributes__ = ['name', 'description_fr', 'description_it', 'description_de']
    __label__ = 'name'
    id = Column('anlage_id', Unicode, primary_key=True)
    name = Column('name', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    facstatus = Column('facstatus', Unicode)
    fackind = Column('fackind', Unicode)
    valid_from = Column('valid_from', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_ausgangslage', SifAusgangslage)


class BazlLaermErsteNachtstunde(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_erste_nachtstunde'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde', BazlLaermErsteNachtstunde)


class BazlLaermHelikopterMaximalpegel(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_helikopter_maxpegel'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel', BazlLaermHelikopterMaximalpegel)


class BazlLaermHelikopter(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_helikopter'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter', BazlLaermHelikopter)


class BazlLaermKleinGrossflugzeuge(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_klein_grossflugzeuge'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge', BazlLaermKleinGrossflugzeuge)


class BazlLaermKleinluftfahrzeuge(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_kleinluftfahrzeuge'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge', BazlLaermKleinluftfahrzeuge)


class BazlLaermLetzteNachtstunde(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_letzte_nachtstunde'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde', BazlLaermLetzteNachtstunde)


class BazlLaermMilitaerGesamt(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_militaer_gesamt'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt', BazlLaermMilitaerGesamt)


class BazlLaermZweiteNachtstunde(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_zweite_nachtstunde'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Unicode)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Unicode)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Unicode)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Unicode)
    exposurecurve_level_db = Column('exposurecurve_level_db', Unicode)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde', BazlLaermZweiteNachtstunde)


class SuelFacAnhorung(Base, Vector):
    __tablename__ = 'suel_fac_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_anhoerung', SuelFacAnhorung)


class SuelPlAnhorung(Base, Vector):
    __tablename__ = 'suel_pl_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it']
    # Translatable labels in fr, it
    __label__ = 'plname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_anhoerung', SuelPlAnhorung)


class SuelFacRAnhorung(Base, Vector):
    __tablename__ = 'suel_fac_r_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_anhoerung', SuelFacRAnhorung)


class SuelPlRAnhorung(Base, Vector):
    __tablename__ = 'suel_pl_r_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it']
    # Translatable labels in fr, it
    __label__ = 'plname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_anhoerung', SuelPlRAnhorung)


class SuelFacKraft(Base, Vector):
    __tablename__ = 'suel_fac_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_kraft', SuelFacKraft)


class SuelPlKraft(Base, Vector):
    __tablename__ = 'suel_pl_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it']
    __label__ = 'plname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_kraft', SuelPlKraft)


class SuelFacRKraft(Base, Vector):
    __tablename__ = 'suel_fac_r_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
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
    doc_title = Column('doc_title', Unicode)
    objname_de = Column('objname_de', Unicode)
    objname_fr = Column('objname_fr', Unicode)
    objname_it = Column('objname_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_kraft', SuelFacRKraft)


class SuelPlRKraft(Base, Vector):
    __tablename__ = 'suel_pl_r_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
    __queryable_attributes__ = ['plname_de', 'plname_fr', 'plname_it']
    # Translatable labels in fr, it
    __label__ = 'plname_de'
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
    doc_title = Column('doc_title', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-uebertragungsleitungen_kraft', SuelPlRKraft)


class ChmobilVeloland (Base, Vector):
    __tablename__ = 'chmobil_veloland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.veloland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    chmobil_has_segment = Column('has_segment', Boolean)
    the_geom = Column(Geometry2D)

register('ch.astra.veloland', ChmobilVeloland)


class ChmobilWanderland (Base, Vector):
    __tablename__ = 'chmobil_wanderland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.wanderland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    chmobil_has_segment = Column('has_segment', Boolean)
    the_geom = Column(Geometry2D)

register('ch.astra.wanderland', ChmobilWanderland)


class ChmobilSkatingland (Base, Vector):
    __tablename__ = 'chmobil_skatingland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.skatingland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    chmobil_has_segment = Column('has_segment', Boolean)
    the_geom = Column(Geometry2D)

register('ch.astra.skatingland', ChmobilSkatingland)


class ChmobilMountainbikeland (Base, Vector):
    __tablename__ = 'chmobil_mountainbikeland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.mountainbikeland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    chmobil_has_segment = Column('has_segment', Boolean)
    the_geom = Column(Geometry2D)

register('ch.astra.mountainbikeland', ChmobilMountainbikeland)


class ChmobilSchneeschuhWanderland (Base, Vector):
    __tablename__ = 'chmobil_schneeschuhwanderland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.swisstopo.schneeschuhwandern'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    chmobil_has_segment = Column('has_segment', Boolean)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.schneeschuhwandern', ChmobilSchneeschuhWanderland)


class FlugplaetzeHeliports(Base, Vector):
    __tablename__ = 'flugplaetze_heliports'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/flugplaetze_heliports.mako'
    __bodId__ = 'ch.bazl.flugplaetze-heliports'
    id = Column('bgdi_id', Integer, primary_key=True)
    icao = Column('icao', Unicode)
    name = Column('name', Unicode)
    location = Column('location', Unicode)
    canton = Column('canton', Unicode)
    arp_east = Column('arp_east', Float)
    arp_north = Column('arp_north', Float)
    elevation = Column('elevation', Float)
    the_geom = Column(Geometry2D)

register('ch.bazl.flugplaetze-heliports', FlugplaetzeHeliports)


class Gebirgslandeplaetze(Base, Vector):
    __tablename__ = 'gebirgslandeplaetze'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/gebirgslandeplaetze.mako'
    __bodId__ = 'ch.bazl.gebirgslandeplaetze'
    id = Column('oid', Integer, primary_key=True)
    icao = Column('icao', Unicode)
    name = Column('name', Unicode)
    canton = Column('canton', Unicode)
    descrip_de = Column('descrip_de', Unicode)
    descrip_fr = Column('descrip_fr', Unicode)
    descrip_it = Column('descrip_it', Unicode)
    arp_east = Column('arp_east', Integer)
    arp_north = Column('arp_north', Integer)
    elevation = Column('elevation', Integer)
    the_geom = Column(Geometry2D)

register('ch.bazl.gebirgslandeplaetze', Gebirgslandeplaetze)


class Spitallandeplaetze(Base, Vector):
    __tablename__ = 'spitallandeplaetze'
    __table_args__ = ({'schema': 'bazl', 'autoload': True})
    __template__ = 'templates/htmlpopup/spitallandeplaetze.mako'
    __bodId__ = 'ch.bazl.spitallandeplaetze'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode, nullable=False)
    location = Column('location', Unicode, nullable=False)
    canton = Column('canton', Unicode, nullable=False)
    arp_east = Column('arp_east', Integer, nullable=False)
    arp_north = Column('arp_north', Integer, nullable=False)
    the_geom = Column(Geometry2D)

register('ch.bazl.spitallandeplaetze', Spitallandeplaetze)


class Bikesharing:
    __table_args__ = ({'schema': 'bfe', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bikesharing.mako'
    __bodId__ = 'ch.bfe.bikesharing'
    id = Column('bgdi_id', Integer, primary_key=True)
    id_provider = Column('id_provider', Integer)
    provider_de = Column('provider_de', Unicode)
    provider_fr = Column('provider_fr', Unicode)
    provider_it = Column('provider_it', Unicode)
    provider_en = Column('provider_en', Unicode)
    providerlink_de = Column('providerlink_de', Unicode)
    providerlink_fr = Column('providerlink_fr', Unicode)
    providerlink_it = Column('providerlink_it', Unicode)
    providerlink_en = Column('providerlink_en', Unicode)
    address = Column('address', Unicode)
    postcode = Column('postcode', Integer)
    city = Column('city', Unicode)
    time_de = Column('time_de', Unicode)
    time_fr = Column('time_fr', Unicode)
    time_it = Column('time_it', Unicode)
    time_en = Column('time_en', Unicode)
    rent_de = Column('rent_de', Unicode)
    rent_fr = Column('rent_fr', Unicode)
    rent_it = Column('rent_it', Unicode)
    rent_en = Column('rent_en', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    description_en = Column('description_en', Unicode)
    id_return = Column('id_return', Integer)
    return_de = Column('return_de', Unicode)
    return_fr = Column('return_fr', Unicode)
    return_it = Column('return_it', Unicode)
    return_en = Column('return_en', Unicode)
    feedback_de = Column('feedback_de', Unicode)
    feedback_fr = Column('feedback_fr', Unicode)
    feedback_it = Column('feedback_it', Unicode)
    feedback_en = Column('feedback_en', Unicode)
    the_geom = Column(Geometry2D)


class BikesharingPolygon (Base, Bikesharing, Vector):
    __tablename__ = 'bikesharing_polygon'

register('ch.bfe.bikesharing', BikesharingPolygon)


class BikesharingPoint (Base, Bikesharing, Vector):
    __tablename__ = 'bikesharing_point'

register('ch.bfe.bikesharing', BikesharingPoint)


class Biomasse:
    __tablename__ = 'biomasse'
    __table_args__ = ({'schema': 'bfe', 'autoload': False, 'extend_existing': True})
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    bfs_nummer = Column('bfs_nummer', Integer)
    the_geom = Column(Geometry2D)


class BiomasseVerholzt (Base, Biomasse, Vector):
    __template__ = 'templates/htmlpopup/biomasseverholzt.mako'
    __bodId__ = 'ch.bfe.biomasse-verholzt'
    woody = Column('woody', Float)

register(BiomasseVerholzt.__bodId__, BiomasseVerholzt)


class BiomasseNichtVerholzt (Base, Biomasse, Vector):
    __template__ = 'templates/htmlpopup/biomassenichtverholzt.mako'
    __bodId__ = 'ch.bfe.biomasse-nicht-verholzt'
    non_woody = Column('non_woody', Float)

register(BiomasseNichtVerholzt.__bodId__, BiomasseNichtVerholzt)
