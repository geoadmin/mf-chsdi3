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

register(Nsa.__bodId__, Nsa)


class SchienennetzPoint(Base, Vector):
    __tablename__ = 'schienennetz_point'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/schienennetz_point.mako'
    __bodId__ = 'ch.bav.schienennetz'
    __label__ = 'nom_point'
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
    sperrungen_type_de = Column('type_de', Unicode)
    sperrungen_type_fr = Column('type_fr', Unicode)
    sperrungen_type_it = Column('type_it', Unicode)
    sperrungen_type_en = Column('type_en', Unicode)
    land = Column('land', Unicode)
    duration_de = Column('duration_de', Unicode)
    duration_fr = Column('duration_fr', Unicode)
    duration_it = Column('duration_it', Unicode)
    duration_en = Column('duration_en', Unicode)
    reason_de = Column('reason_de', Unicode)
    reason_fr = Column('reason_fr', Unicode)
    reason_it = Column('reason_it', Unicode)
    reason_en = Column('reason_en', Unicode)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    title_en = Column('title_en', Unicode)
    abstract_de = Column('abstract_de', Unicode)
    abstract_fr = Column('abstract_fr', Unicode)
    abstract_it = Column('abstract_it', Unicode)
    abstract_en = Column('abstract_en', Unicode)
    state_validate_de = Column('state_validate_de', Unicode)
    state_validate_fr = Column('state_validate_fr', Unicode)
    state_validate_it = Column('state_validate_it', Unicode)
    state_validate_en = Column('state_validate_en', Unicode)
    file_de = Column('file_de', Unicode)
    file_fr = Column('file_fr', Unicode)
    file_it = Column('file_it', Unicode)
    file_en = Column('file_en', Unicode)
    content_provider_de = Column('content_provider_de', Unicode)
    content_provider_fr = Column('content_provider_fr', Unicode)
    content_provider_it = Column('content_provider_it', Unicode)
    content_provider_en = Column('content_provider_en', Unicode)
    url1_link_de = Column('url1_link_de', Unicode)
    url1_link_fr = Column('url1_link_fr', Unicode)
    url1_link_it = Column('url1_link_it', Unicode)
    url1_link_en = Column('url1_link_en', Unicode)
    route_nr = Column('route_nr', Unicode)
    segment_nr = Column('segment_nr', Unicode)
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
    __bodId__ = 'ch.bav.haltestellen-oev'


class OevHaltestellenZoom1(Base, OevHaltestellen, Vector):
    __tablename__ = 'oev_haltestellen_tooltip'
    __table_args__ = ({'schema': 'bav', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/oev_haltestellen.mako'
    __minscale__ = 1
    __maxscale__ = 3000
    __label__ = 'name'
    __extended_info__ = True
    __returnedGeometry__ = 'the_geom_point'
    id = Column('nummer', Integer, primary_key=True)
    name = Column('name', Unicode)
    abkuerzung = Column('abkuerzung', Unicode)
    tuabkuerzung = Column('transportunternehmen_abkuerzung', Unicode)
    betriebspunkttyp_de = Column('betriebspunkttyp_bezeichnung_de', Unicode)
    betriebspunkttyp_fr = Column('betriebspunkttyp_bezeichnung_fr', Unicode)
    verkehrsmittel_de = Column('verkehrsmittel_bezeichnung_de', Unicode)
    verkehrsmittel_fr = Column('verkehrsmittel_bezeichnung_fr', Unicode)
    # point geometry hilight
    the_geom_point = Column('the_geom', Geometry2D)
    the_geom = Column('bgdi_geom_poly', Geometry2D)

register(OevHaltestellen.__bodId__, OevHaltestellenZoom1)


class OevHaltestellenZoom2(Base, OevHaltestellen, Vector):
    __tablename__ = 'oev_haltestellen_tooltip'
    __table_args__ = ({'schema': 'bav', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/oev_haltestellen.mako'
    __minscale__ = 3000
    __label__ = 'name'
    __extended_info__ = True
    __returnedGeometry__ = 'the_geom_point'
    id = Column('nummer', Integer, primary_key=True)
    name = Column('name', Unicode)
    abkuerzung = Column('abkuerzung', Unicode)
    tuabkuerzung = Column('transportunternehmen_abkuerzung', Unicode)
    betriebspunkttyp_de = Column('betriebspunkttyp_bezeichnung_de', Unicode)
    betriebspunkttyp_fr = Column('betriebspunkttyp_bezeichnung_fr', Unicode)
    verkehrsmittel_de = Column('verkehrsmittel_bezeichnung_de', Unicode)
    verkehrsmittel_fr = Column('verkehrsmittel_bezeichnung_fr', Unicode)
    # point geometry hilight
    the_geom_point = Column('the_geom', Geometry2D)
    the_geom = Column('bgdi_geom_poly_overview', Geometry2D)

register(OevHaltestellen.__bodId__, OevHaltestellenZoom2)


class OevHaltekante(Base, OevHaltestellen, Vector):
    __tablename__ = 'oev_haltekante_tooltip'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/oev_haltekante.mako'
    __label__ = 'haltestelle'
    __maxscale__ = 4000
    id = Column('nummer', Unicode, primary_key=True)
    nummer_text = Column('nummer_text', Unicode)
    bezeichnung_de = Column('bezeichnung_de', Unicode)
    bezeichnung_fr = Column('bezeichnung_fr', Unicode)
    betrieblichebezeichnung = Column('betrieblichebezeichnung', Unicode)
    laenge = Column('laenge', Float)
    kantenhoehe = Column('kantenhoehe', Float)
    haltestelle = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register(OevHaltestellen.__bodId__, OevHaltekante)


# IVS NAT and REG use the same template
class SicherheitsZonenPlan(Base, Vector):
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

register(SicherheitsZonenPlan.__bodId__, SicherheitsZonenPlan)


class IVSNat(Base, Vector):
    __tablename__ = 'ivs_nat_tt'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-nat'
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

register(IVSNat.__bodId__, IVSNat)


class IVSNatVerlaeufe(Base, Vector):
    __tablename__ = 'ivs_nat_verlaeufe_tt'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-nat-verlaeufe'
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

register(IVSNatVerlaeufe.__bodId__, IVSNatVerlaeufe)


class IVSRegLoc(Base, Vector):
    __tablename__ = 'ivs_reg_loc'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-reg_loc'
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

register(IVSRegLoc.__bodId__, IVSRegLoc)


class BaulinienNationalstrassen():
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/baulinien_nationalstrassen.mako'
    __bodId__ = 'ch.astra.baulinien-nationalstrassen'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class BaulinienNationalstrassenLine(Base, BaulinienNationalstrassen, Vector):
    __tablename__ = 'baulinien_nationalstrassen_line'
    __label__ = 'status'
    status = Column('status', Unicode)
    approval_date = Column('approval_date', Date)
    publication_date_from = Column('publication_date_from', Date)
    approving_authority = Column('approving_authority', Unicode)
    planning_approval_name = Column('planning_approval_name', Unicode)

register(BaulinienNationalstrassenLine.__bodId__, BaulinienNationalstrassenLine)


class BaulinienNationalstrassenArea(Base, BaulinienNationalstrassen, Vector):
    __tablename__ = 'baulinien_nationalstrassen_area'
    __label__ = 'id'
    vertical_limit_upward = Column('vertical_limit_upward', Unicode)
    vertical_limit_downward = Column('vertical_limit_downward', Unicode)

register(BaulinienNationalstrassenArea.__bodId__, BaulinienNationalstrassenArea)


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

register(Hauptstrassennetz.__bodId__, Hauptstrassennetz)


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

register(SchwerverunfKantonAlkohol.__bodId__, SchwerverunfKantonAlkohol)


class SchwerverunfKantonGeschwindig(Base, Schwerverunf, Vector):
    __template__ = 'templates/htmlpopup/astra_schwerverunf_kanton_geschwindig.mako'
    __bodId__ = 'ch.astra.schwerverunfallte-kanton_geschwindigkeit'
    population = Column('population', Integer)
    accspeed_ugt = Column('accspeed_ugt', Integer)
    accspeed_usv = Column('accspeed_usv', Integer)
    accspeed_ugt_usv = Column('accspeed_ugt_usv', Integer)
    accspeed_ugt_usv_perpopulation = Column('accspeed_ugt_usv_perpopulation', Numeric)

register(SchwerverunfKantonGeschwindig.__bodId__, SchwerverunfKantonGeschwindig)


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

register(SchwerverunfKantonJahresvergleich.__bodId__, SchwerverunfKantonJahresvergleich)


class SchwerverunfKantonProEinwohner(Base, Schwerverunf, Vector):
    __template__ = 'templates/htmlpopup/astra_schwerverunf_kanton_pro_einwohner.mako'
    __bodId__ = 'ch.astra.schwerverunfallte-kanton_pro_einwohner'
    population = Column('population', Integer)
    acc_ugt = Column('acc_ugt', Integer)
    acc_usv = Column('acc_usv', Integer)
    acc_ugt_usv = Column('acc_ugt_usv', Integer)
    acc_ugt_usv_perpopulation = Column('acc_ugt_usv_perpopulation', Numeric)

register(SchwerverunfKantonProEinwohner.__bodId__, SchwerverunfKantonProEinwohner)


class KatasterBelasteterStandorte(Base, Vector):
    __tablename__ = 'kataster_belasteter_standorte_oev'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/kataster_belasteter_standorte_oev.mako'
    __bodId__ = 'ch.bav.kataster-belasteter-standorte-oev'
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
    url_de = Column('url_de', Unicode)
    url_fr = Column('url_fr', Unicode)
    url_it = Column('url_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register(KatasterBelasteterStandorte.__bodId__, KatasterBelasteterStandorte)


class AbgeltungWasserkraftnutzung(Base, Vector):
    __tablename__ = 'abgeltung_wasserkraftnutzung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/abgeltungwasserkraftnutzung.mako'
    __bodId__ = 'ch.bfe.abgeltung-wasserkraftnutzung'
    __label__ = 'name'
    id = Column('objectnumber', Integer, primary_key=True)
    area = Column('area', Numeric)
    name = Column('name', Unicode)
    perimeter = Column('perimeter', Numeric)
    startprotectioncommitment = Column('startprotectioncommitment', Unicode)
    endprotectioncommitment = Column('endprotectioncommitment', Unicode)
    the_geom = Column(Geometry2D)

register(AbgeltungWasserkraftnutzung.__bodId__, AbgeltungWasserkraftnutzung)


class FernwaermeWohn(Base, Vector):
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

register(FernwaermeWohn.__bodId__, FernwaermeWohn)


class FernwaermeIndustrie(Base, Vector):
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

register(FernwaermeIndustrie.__bodId__, FernwaermeIndustrie)


class Energieberatungsstellen(Base, Vector):
    __tablename__ = 'energieberatungsstellen'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energieberatungsstellen.mako'
    __bodId__ = 'ch.bfe.energieberatungsstellen'
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

register(Energieberatungsstellen.__bodId__, Energieberatungsstellen)


class Energiestaedte(Base, Vector):
    __tablename__ = 'energiestaedte'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte.mako'
    __bodId__ = 'ch.bfe.energiestaedte'
    __extended_info__ = True
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

register(Energiestaedte.__bodId__, Energiestaedte)


class Energiestaedte2000wattAreale(Base, Vector):
    __tablename__ = 'energiestaedte_2000watt_areale'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte_2000watt_areale.mako'
    __bodId__ = 'ch.bfe.energiestaedte-2000watt-areale'
    __extended_info__ = True
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

register(Energiestaedte2000wattAreale.__bodId__, Energiestaedte2000wattAreale)


class Energieforschung(Base, Vector):
    __tablename__ = 'energieforschung_projekte'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energieforschung.mako'
    __bodId__ = 'ch.bfe.energieforschung'
    __label__ = 'title_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    title_en = Column('title_en', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    description_en = Column('description_en', Unicode)
    topic_de = Column('topic_de', Unicode)
    topic_fr = Column('topic_fr', Unicode)
    topic_it = Column('topic_it', Unicode)
    topic_en = Column('topic_en', Unicode)
    status_de = Column('status_de', Unicode)
    status_fr = Column('status_fr', Unicode)
    status_it = Column('status_it', Unicode)
    status_en = Column('status_en', Unicode)
    duration = Column('duration', Unicode)
    link_de = Column('link_de', Unicode)
    link_fr = Column('link_fr', Unicode)
    link_it = Column('link_it', Unicode)
    link_en = Column('link_en', Unicode)
    the_geom = Column(Geometry2D)

register(Energieforschung.__bodId__, Energieforschung)


class FernWaermeAngebot(Base, Vector):
    __tablename__ = 'fernwaerme_angebot'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/fernwaerme_angebot.mako'
    __bodId__ = 'ch.bfe.fernwaerme-angebot'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    heatpotential = Column('heatpotential', Float)
    the_geom = Column(Geometry2D)

register(FernWaermeAngebot.__bodId__, FernWaermeAngebot)


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

register(KomoProjekte.__bodId__, KomoProjekte)


class MinergieGebaeude(Base, Vector):
    __tablename__ = 'minergiegebaeude'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/minergiegebaeude.mako'
    __bodId__ = 'ch.bfe.minergiegebaeude'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    certificate = Column('certificate', Unicode)
    standard = Column('standard', Unicode)
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

register(StatistikwasserkraftanlagenNew.__bodId__, StatistikwasserkraftanlagenNew)


class Erneuerbarheizen(Base, Vector):
    __tablename__ = 'renewable_heating_efh'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/erneuerbarheizen.mako'
    __bodId__ = 'ch.bfe.erneuerbarheizen'
    __label__ = 'company'
    id = Column('xtf_id', Integer, primary_key=True)
    company = Column('company', Unicode)
    firstname_name = Column('firstname_name', Unicode)
    email = Column('email', Unicode)
    phonenumber = Column('phonenumber', Unicode)
    street_streetnumber = Column('street_streetnumber', Unicode)
    pc_place = Column('pc_place', Unicode)
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
    # Website is intenionally defined only in the model and not used for the htmlpopup
    website = Column('website', Unicode)
    the_geom = Column(Geometry2D)

register(Erneuerbarheizen.__bodId__, Erneuerbarheizen)


class ErneuerbarheizenMFH(Base, Vector):
    __tablename__ = 'renewable_heating_mfh'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/erneuerbarheizen_mfh.mako'
    __bodId__ = 'ch.bfe.erneuerbarheizen-mehrfamilienhaeuser'
    __label__ = 'company'
    id = Column('bgdi_id', Integer, primary_key=True)
    company = Column('company', Unicode)
    firstname_name = Column('firstname_name', Unicode)
    email = Column('email', Unicode)
    phonenumber = Column('phonenumber', Unicode)
    street_streetnumber = Column('street_streetnumber', Unicode)
    pc_place = Column('pc_place', Unicode)
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
    # Website is intenionally defined only in the model and not used for the htmlpopup
    website = Column('website', Unicode)
    the_geom = Column(Geometry2D)

register(ErneuerbarheizenMFH.__bodId__, ErneuerbarheizenMFH)


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

register(Zaehlstellenuebergeordnet.__bodId__, Zaehlstellenuebergeordnet)


class StauanlagenBundesaufsicht(Base, Vector):
    __tablename__ = 'stauanlagen_bundesaufsicht'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/stauanlagenbundesaufsicht.mako'
    __bodId__ = 'ch.bfe.stauanlagen-bundesaufsicht'
    __extended_info__ = True
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

register(StauanlagenBundesaufsicht.__bodId__, StauanlagenBundesaufsicht)


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

register(Kleinwasserkraftpotentiale.__bodId__, Kleinwasserkraftpotentiale)


class WindenergieanlagenFacility(Base, Vector):
    __tablename__ = 'view_windenergieanlagen_facility'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/windenergieanlagen_facility.mako'
    __bodId__ = 'ch.bfe.windenergieanlagen'
    __extended_info__ = True
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

register(WindenergieanlagenFacility.__bodId__, WindenergieanlagenFacility)


class WindenergieanlagenTurbine(Base, Vector):
    __tablename__ = 'view_windenergieanlagen_turbine'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/windenergieanlagen_turbine.mako'
    __bodId__ = 'ch.bfe.windenergieanlagen'
    __extended_info__ = True
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

register(WindenergieanlagenTurbine.__bodId__, WindenergieanlagenTurbine)


class MeteoVereisung(Base, Vector):
    __tablename__ = 'meteorologische_vereisung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/meteo_vereisung.mako'
    __bodId__ = 'ch.bfe.meteorologische-vereisung'
    id = Column('bgdi_id', Integer, primary_key=True)
    vereisung = Column('vereisung', Integer, nullable=False)
    hoehe = Column('hoehe', Unicode, nullable=False)
    the_geom = Column(Geometry2D)

register(MeteoVereisung.__bodId__, MeteoVereisung)


class BakomNotruf(Base, Vector):
    __tablename__ = 'notruf'
    __table_args__ = ({'schema': 'bakom', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bakom_notruf.mako'
    __bodId__ = 'ch.bakom.notruf'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bfs_nummer', Integer, primary_key=True)
    name = Column('name', Unicode)
    sprache = Column('sprache', Unicode)
    objektart = Column('objektart', Unicode)
    mobile_112 = Column('mobile_112', Unicode)
    mo_gemeinde_112 = Column('mo_gemeinde_112', Unicode)
    mo_addresse_112 = Column('mo_addresse_112', Unicode)
    mobile_117 = Column('mobile_117', Unicode)
    mo_gemeinde_117 = Column('mo_gemeinde_117', Unicode)
    mo_addresse_117 = Column('mo_addresse_117', Unicode)
    mobile_118 = Column('mobile_118', Unicode)
    mo_gemeinde_118 = Column('mo_gemeinde_118', Unicode)
    mo_addresse_118 = Column('mo_addresse_118', Unicode)
    mobile_142 = Column('mobile_142', Unicode)
    mo_gemeinde_142 = Column('mo_gemeinde_142', Unicode)
    mo_addresse_142 = Column('mo_addresse_142', Unicode)
    mobile_143 = Column('mobile_143', Unicode)
    mo_gemeinde_143 = Column('mo_gemeinde_143', Unicode)
    mo_addresse_143 = Column('mo_addresse_143', Unicode)
    mobile_144 = Column('mobile_144', Unicode)
    mo_gemeinde_144 = Column('mo_gemeinde_144', Unicode)
    mo_addresse_144 = Column('mo_addresse_144', Unicode)
    mobile_145 = Column('mobile_145', Unicode)
    mo_gemeinde_145 = Column('mo_gemeinde_145', Unicode)
    mo_addresse_145 = Column('mo_addresse_145', Unicode)
    mobile_147 = Column('mobile_147', Unicode)
    mo_gemeinde_147 = Column('mo_gemeinde_147', Unicode)
    mo_addresse_147 = Column('mo_addresse_147', Unicode)
    festnetz_112 = Column('festnetz_112', Unicode)
    fn_gemeinde_112 = Column('fn_gemeinde_112', Unicode)
    fn_addresse_112 = Column('fn_addresse_112', Unicode)
    festnetz_117 = Column('festnetz_117', Unicode)
    fn_gemeinde_117 = Column('fn_gemeinde_117', Unicode)
    fn_addresse_117 = Column('fn_addresse_117', Unicode)
    festnetz_118 = Column('festnetz_118', Unicode)
    fn_gemeinde_118 = Column('fn_gemeinde_118', Unicode)
    fn_addresse_118 = Column('fn_addresse_118', Unicode)
    festnetz_142 = Column('festnetz_142', Unicode)
    fn_gemeinde_142 = Column('fn_gemeinde_142', Unicode)
    fn_addresse_142 = Column('fn_addresse_142', Unicode)
    festnetz_143 = Column('festnetz_143', Unicode)
    fn_gemeinde_143 = Column('fn_gemeinde_143', Unicode)
    fn_addresse_143 = Column('fn_addresse_143', Unicode)
    festnetz_144 = Column('festnetz_144', Unicode)
    fn_gemeinde_144 = Column('fn_gemeinde_144', Unicode)
    fn_addresse_144 = Column('fn_addresse_144', Unicode)
    festnetz_145 = Column('festnetz_145', Unicode)
    fn_gemeinde_145 = Column('fn_gemeinde_145', Unicode)
    fn_addresse_145 = Column('fn_addresse_145', Unicode)
    festnetz_147 = Column('festnetz_147', Unicode)
    fn_gemeinde_147 = Column('fn_gemeinde_147', Unicode)
    fn_addresse_147 = Column('fn_addresse_147', Unicode)
    satellit_112 = Column('satellit_112', Unicode)
    sa_gemeinde_112 = Column('sa_gemeinde_112', Unicode)
    sa_addresse_112 = Column('sa_addresse_112', Unicode)
    the_geom = Column(Geometry2D)

register(BakomNotruf.__bodId__, BakomNotruf)


class BakomNotrufLayer:
    __table_args__ = ({'schema': 'bakom', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bakom_notruf_layers.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    routing_nr = Column('routing_nr', Unicode)
    name = Column('name', Unicode)
    chg_date = Column('chg_date', Unicode)
    the_geom = Column(Geometry2D)


class BakomNotruf112Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-112_festnetz'
    __tablename__ = 'fn_112_tooltip'

register(BakomNotruf112Fest.__bodId__, BakomNotruf112Fest)


class BakomNotruf117Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-117_festnetz'
    __tablename__ = 'fn_117_tooltip'

register(BakomNotruf117Fest.__bodId__, BakomNotruf117Fest)


class BakomNotruf118Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-118_festnetz'
    __tablename__ = 'fn_118_tooltip'

register(BakomNotruf118Fest.__bodId__, BakomNotruf118Fest)


class BakomNotruf142Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-142_festnetz'
    __tablename__ = 'fn_142_tooltip'

register(BakomNotruf142Fest.__bodId__, BakomNotruf142Fest)


class BakomNotruf143Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-143_festnetz'
    __tablename__ = 'fn_143_tooltip'

register(BakomNotruf143Fest.__bodId__, BakomNotruf143Fest)


class BakomNotruf144Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-144_festnetz'
    __tablename__ = 'fn_144_tooltip'

register(BakomNotruf144Fest.__bodId__, BakomNotruf144Fest)


class BakomNotruf145Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-145_festnetz'
    __tablename__ = 'fn_145_tooltip'

register(BakomNotruf145Fest.__bodId__, BakomNotruf145Fest)


class BakomNotruf147Fest(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-147_festnetz'
    __tablename__ = 'fn_147_tooltip'

register(BakomNotruf147Fest.__bodId__, BakomNotruf147Fest)


class BakomNotruf112Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-112_mobilnetz'
    __tablename__ = 'mo_112_tooltip'

register(BakomNotruf112Mobil.__bodId__, BakomNotruf112Mobil)


class BakomNotruf117Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-117_mobilnetz'
    __tablename__ = 'mo_117_tooltip'

register(BakomNotruf117Mobil.__bodId__, BakomNotruf117Mobil)


class BakomNotruf118Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-118_mobilnetz'
    __tablename__ = 'mo_118_tooltip'

register(BakomNotruf118Mobil.__bodId__, BakomNotruf118Mobil)


class BakomNotruf142Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-142_mobilnetz'
    __tablename__ = 'mo_142_tooltip'

register(BakomNotruf142Mobil.__bodId__, BakomNotruf142Mobil)


class BakomNotruf143Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-143_mobilnetz'
    __tablename__ = 'mo_143_tooltip'

register(BakomNotruf143Mobil.__bodId__, BakomNotruf143Mobil)


class BakomNotruf144Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-144_mobilnetz'
    __tablename__ = 'mo_144_tooltip'

register(BakomNotruf144Mobil.__bodId__, BakomNotruf144Mobil)


class BakomNotruf145Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-145_mobilnetz'
    __tablename__ = 'mo_145_tooltip'

register(BakomNotruf145Mobil.__bodId__, BakomNotruf145Mobil)


class BakomNotruf147Mobil(Base, BakomNotrufLayer, Vector):
    __bodId__ = 'ch.bakom.notruf-147_mobilnetz'
    __tablename__ = 'mo_147_tooltip'

register(BakomNotruf147Mobil.__bodId__, BakomNotruf147Mobil)


class BakomNotruf112Sat(Base, Vector):
    __tablename__ = 'sa_112_tooltip'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/notruf_sa_112.mako'
    __bodId__ = 'ch.bakom.notruf-112_satellit'
    __label__ = 'id'
    id = Column('bfs_nummer', Integer, primary_key=True)
    satellit_112 = Column('phone_number', Unicode)
    sa_gemeinde_112 = Column('name', Unicode)
    sa_addresse_112 = Column('address', Unicode)
    the_geom = Column(Geometry2D)

register(BakomNotruf112Sat.__bodId__, BakomNotruf112Sat)


class BakomNotrufZentral:
    __table_args__ = ({'schema': 'bakom', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/bakom_notruf_zentrale.mako'
    __label__ = 'alarmzentrale'
    id = Column('bgdi_id', Integer, primary_key=True)
    alarmzentrale = Column('alarmzentrale', Unicode)
    strasse = Column('strasse', Unicode)
    nummer = Column('nummer', Unicode)
    plz = Column('plz', Unicode)
    ort = Column('ort', Unicode)
    kt = Column('kt', Unicode)
    routing_nr = Column('routing_nr', Unicode)
    chg_date = Column('chg_date', Unicode)
    the_geom = Column(Geometry2D)


class BakomNotruf112Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-112_zentral'
    __tablename__ = 'ze_112_tooltip'

register(BakomNotruf112Zentral.__bodId__, BakomNotruf112Zentral)


class BakomNotruf117Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-117_zentral'
    __tablename__ = 'ze_117_tooltip'

register(BakomNotruf117Zentral.__bodId__, BakomNotruf117Zentral)


class BakomNotruf118Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-118_zentral'
    __tablename__ = 'ze_118_tooltip'

register(BakomNotruf118Zentral.__bodId__, BakomNotruf118Zentral)


class BakomNotruf142Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-142_zentral'
    __tablename__ = 'ze_142_tooltip'

register(BakomNotruf142Zentral.__bodId__, BakomNotruf142Zentral)


class BakomNotruf143Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-143_zentral'
    __tablename__ = 'ze_143_tooltip'

register(BakomNotruf143Zentral.__bodId__, BakomNotruf143Zentral)


class BakomNotruf144Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-144_zentral'
    __tablename__ = 'ze_144_tooltip'

register(BakomNotruf144Zentral.__bodId__, BakomNotruf144Zentral)


class BakomNotruf145Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-145_zentral'
    __tablename__ = 'ze_145_tooltip'

register(BakomNotruf145Zentral.__bodId__, BakomNotruf145Zentral)


class BakomNotruf147Zentral(Base, BakomNotrufZentral, Vector):
    __bodId__ = 'ch.bakom.notruf-147_zentral'
    __tablename__ = 'ze_147_tooltip'

register(BakomNotruf147Zentral.__bodId__, BakomNotruf147Zentral)


class Bakomfernsehsender(Base, Vector):
    __tablename__ = 'nisdb_bro'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomfernsehsender.mako'
    __bodId__ = 'ch.bakom.radio-fernsehsender'
    __extended_info__ = True
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

register(Bakomfernsehsender.__bodId__, Bakomfernsehsender)


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
    __label__ = 'prog'
    id = Column('zone_id', Integer, primary_key=True)
    prog = Column('prog', Unicode)
    the_geom = Column(Geometry2D)

register(Bakomtv.__bodId__, Bakomtv)


class Bakomukw(Base, Vector):
    __tablename__ = 'ukw_gebiet'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomukw.mako'
    __bodId__ = 'ch.bakom.versorgungsgebiet-ukw'
    __label__ = 'prog'
    id = Column('zone_id', Integer, primary_key=True)
    prog = Column('prog', Unicode)
    the_geom = Column(Geometry2D)

register(Bakomukw.__bodId__, Bakomukw)


class EinschraenkungenDrohnen(Base, Vector):
    __tablename__ = 'gebietsbeschraenkungen_drohnen'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/einschraenkungen_drohnen.mako'
    __bodId__ = 'ch.bazl.einschraenkungen-drohnen'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    zone_name_de = Column('zone_name_de', Unicode)
    zone_name_fr = Column('zone_name_fr', Unicode)
    zone_name_it = Column('zone_name_it', Unicode)
    zone_name_en = Column('zone_name_en', Unicode)
    zone_restriction_id = Column('zone_restriction_id', Unicode)
    zone_reason_id = Column('zone_reason_id', Unicode)
    zone_restriction_de = Column('zone_restriction_de', Unicode)
    zone_restriction_fr = Column('zone_restriction_fr', Unicode)
    zone_restriction_it = Column('zone_restriction_it', Unicode)
    zone_restriction_en = Column('zone_restriction_en', Unicode)
    zone_message_de = Column('zone_message_de', Unicode)
    zone_message_fr = Column('zone_message_fr', Unicode)
    zone_message_it = Column('zone_message_it', Unicode)
    zone_message_en = Column('zone_message_en', Unicode)
    auth_url_de = Column('auth_url_de', Unicode)
    auth_url_fr = Column('auth_url_fr', Unicode)
    auth_url_it = Column('auth_url_it', Unicode)
    auth_url_en = Column('auth_url_en', Unicode)
    auth_name_de = Column('auth_name_de', Unicode)
    auth_name_fr = Column('auth_name_fr', Unicode)
    auth_name_it = Column('auth_name_it', Unicode)
    auth_name_en = Column('auth_name_en', Unicode)
    auth_contact = Column('auth_contact', Unicode)
    auth_service_de = Column('auth_service_de', Unicode)
    auth_service_fr = Column('auth_service_fr', Unicode)
    auth_service_it = Column('auth_service_it', Unicode)
    auth_service_en = Column('auth_service_en', Unicode)
    auth_email = Column('auth_email', Unicode)
    auth_phone = Column('auth_phone', Unicode)
    auth_intervalbefore = Column('auth_intervalbefore', Unicode)
    air_vol_lower_vref = Column('air_vol_lower_vref', Unicode)
    air_vol_lower_limit = Column('air_vol_lower_limit', Unicode)
    air_vol_upper_vref = Column('air_vol_upper_vref', Unicode)
    air_vol_upper_limit = Column('air_vol_upper_limit', Unicode)
    time_permanent = Column('time_permanent', Unicode)
    time_start = Column('time_start', Unicode)
    time_end = Column('time_end', Unicode)
    period_day = Column('period_day', Unicode)
    period_start = Column('period_start', Unicode)
    period_end = Column('period_end', Unicode)
    the_geom = Column(Geometry2D)

register(EinschraenkungenDrohnen.__bodId__, EinschraenkungenDrohnen)


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

register(ProjFlughafenanlagen.__bodId__, ProjFlughafenanlagen)


class LuftfahrthindernisBase:
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __label__ = 'registrationnumber'
    __template__ = 'templates/htmlpopup/luftfahrthindernisse.mako'
    id = Column('bgdi_id', Integer, primary_key=True)
    airport = Column('airport', Unicode)
    registrationnumber = Column('registrationnumber', Unicode)
    obstacletype = Column('obstacletype', Unicode)
    maxheightagl = Column('maxheightagl', Unicode)
    topelevationamsl = Column('topelevationamsl', Float)
    radius = Column('radius', Float)
    effectivedate = Column('effectivedate', Date)
    marking = Column('marking', Unicode)
    lighting = Column('lighting', Unicode)
    group = Column('group', Unicode)
    uuid = Column('uuid', Unicode)
    the_geom = Column(Geometry2D)


class LuftfahrthindernisBig(Base, LuftfahrthindernisBase, Vector):
    __bodId__ = 'ch.bazl.luftfahrthindernis'
    __tablename__ = 'view_obstacles_big'

register(LuftfahrthindernisBig.__bodId__, LuftfahrthindernisBig)


class LuftfahrthindernisSmall(Base, LuftfahrthindernisBase, Vector):
    __bodId__ = 'ch.bazl.luftfahrthindernis-klein'
    __tablename__ = 'view_obstacles_small'

register(LuftfahrthindernisSmall.__bodId__, LuftfahrthindernisSmall)


class LuftfahrthindernisAktuell(Base, LuftfahrthindernisBase, Vector):
    __bodId__ = 'ch.bazl.luftfahrthindernis-aenderungen'
    __tablename__ = 'view_obstacles_active'

register(LuftfahrthindernisAktuell.__bodId__, LuftfahrthindernisAktuell)


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
    __label__ = 'name'
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

register(LuftraeumeFluginformationsGebiet.__bodId__, LuftraeumeFluginformationsGebiet)


class LuftraeumeFluginformationsZonen(Base, LuftraeumeBase, Vector):
    __tablename__ = 'luftraeume_fluginformationszonen'
    __bodId__ = 'ch.bazl.luftraeume-fluginformationszonen'

register(LuftraeumeFluginformationsZonen.__bodId__, LuftraeumeFluginformationsZonen)


class LuftraeumeKontrollBezirke(Base, LuftraeumeBase, Vector):
    __returnedGeometry__ = 'the_geom_highlight'
    __tablename__ = 'luftraeume_kontrollbezirke'
    __bodId__ = 'ch.bazl.luftraeume-kontrollbezirke'
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register(LuftraeumeKontrollBezirke.__bodId__, LuftraeumeKontrollBezirke)


class LuftraeumeKontrollZonen(Base, LuftraeumeBase, Vector):
    __tablename__ = 'luftraeume_kontrollzonen'
    __bodId__ = 'ch.bazl.luftraeume-kontrollzonen'

register(LuftraeumeKontrollZonen.__bodId__, LuftraeumeKontrollZonen)


class LuftraeumeNahKontrollBezirke(Base, LuftraeumeBase, Vector):
    __tablename__ = 'luftraeume_nahkontrollbezirke'
    __bodId__ = 'ch.bazl.luftraeume-nahkontrollbezirke'

register(LuftraeumeNahKontrollBezirke.__bodId__, LuftraeumeNahKontrollBezirke)


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

register(HindernisbegrenzungsflaechenPerimeter.__bodId__, HindernisbegrenzungsflaechenPerimeter)


class HindernisbegrenzungsflaechenKataster:
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/hindernisbegrenzungsflaechen_kataster.mako'
    __bodId__ = 'ch.bazl.hindernisbegrenzungsflaechen-kataster'
    id = Column('bgdi_id', Integer, primary_key=True)
    icaoloc = Column('icaoloc', Unicode)
    surfacetype = Column('surfacetype', Unicode)
    document = Column('document', Unicode)
    geom_type = Column('geom_type', Unicode)
    the_geom = Column(Geometry2D)


class HindernisbegrenzungsflaechenKatasterArea(Base, HindernisbegrenzungsflaechenKataster, Vector):
    __tablename__ = 'hindernisbegrenzungsflaechen_kataster_area'

register(HindernisbegrenzungsflaechenKatasterArea.__bodId__, HindernisbegrenzungsflaechenKatasterArea)


class HindernisbegrenzungsflaechenKatasterOlsLine(Base, HindernisbegrenzungsflaechenKataster, Vector):
    __tablename__ = 'hindernisbegrenzungsflaechen_kataster_olsline'

register(HindernisbegrenzungsflaechenKatasterOlsLine.__bodId__, HindernisbegrenzungsflaechenKatasterOlsLine)


class IntrinsischesBodenrisikoSora(Base, Vector):
    __tablename__ = 'intrinsisches_bodenrisiko_sora'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_intrinsisches_bodenrisiko.mako'
    __bodId__ = 'ch.bazl.intrinsisches-bodenrisiko_sora'
    id = Column('id', Integer, primary_key=True)
    density_pop_km2 = Column('density_pop_km2', Integer)
    the_geom = Column(Geometry2D)

register(IntrinsischesBodenrisikoSora.__bodId__, IntrinsischesBodenrisikoSora)


class AstraStrasseFacilitiesA(Base, Vector):
    __tablename__ = 'sachplan_strasse_fac_anhoerung'
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

register(AstraStrasseFacilitiesA.__bodId__, AstraStrasseFacilitiesA)


class AstraStrassePlanningA(Base, Vector):
    __tablename__ = 'sachplan_strasse_pl_anhoerung'
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

register(AstraStrassePlanningA.__bodId__, AstraStrassePlanningA)


class AstraStrassePlanningRasterA(Base, Vector):
    __tablename__ = 'sachplan_strasse_pl_r_anhoerung'
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

register(AstraStrassePlanningRasterA.__bodId__, AstraStrassePlanningRasterA)


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

register(AstraStrasseFacilitiesK.__bodId__, AstraStrasseFacilitiesK)


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

register(AstraStrassePlanningK.__bodId__, AstraStrassePlanningK)


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

register(AstraStrassePlanningRasterK.__bodId__, AstraStrassePlanningRasterK)


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

register(BiogasFacilities.__bodId__, BiogasFacilities)


class SachPGFacilities(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_fac_pt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
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

register(SachPGFacilities.__bodId__, SachPGFacilities)


class SachPGPlanning(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_pm_pt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning_pt.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
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

register(SachPGPlanning.__bodId__, SachPGPlanning)


class SachPGAreaPlanningNotMT6(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_pm_area_not_mt6'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
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

register(SachPGAreaPlanningNotMT6.__bodId__, SachPGAreaPlanningNotMT6)


class SachPGAreaPlanningMT6(Base, Vector):
    __tablename__ = 'sachplan_geologie_tiefenlager_pm_area_mt6'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
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

register(SachPGAreaPlanningMT6.__bodId__, SachPGAreaPlanningMT6)


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

register(SilFacilitiesA.__bodId__, SilFacilitiesA)


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
    the_geom = Column(Geometry2D)

register(SilPlanningA.__bodId__, SilPlanningA)


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

register(SilFacilitiesK.__bodId__, SilFacilitiesK)


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
    the_geom = Column(Geometry2D)

register(SilPlanningK.__bodId__, SilPlanningK)


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

register(NgaAnbieter.__bodId__, NgaAnbieter)


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

register(Kernkraftwerke.__bodId__, Kernkraftwerke)


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

register(Kehrichtverbrennungsanlagen.__bodId__, Kehrichtverbrennungsanlagen)


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

register(ThermischeNetzeGeometry.__bodId__, ThermischeNetzeGeometry)


class SisFacilitiesA(Base, Vector):
    __tablename__ = 'sis_fac_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_anhorung'
    __template__ = 'templates/htmlpopup/sis_facilities.mako'
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

register(SisFacilitiesA.__bodId__, SisFacilitiesA)


class SisPlanningA(Base, Vector):
    __tablename__ = 'sis_pl_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_anhorung'
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
    the_geom = Column(Geometry2D)

register(SisPlanningA.__bodId__, SisPlanningA)


class SisAngaben(Base, Vector):
    __tablename__ = 'sis_angaben'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_angaben.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_ausgangslage'
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

register(SisAngaben.__bodId__, SisAngaben)


class SisFacilitiesK(Base, Vector):
    __tablename__ = 'sis_fac_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_facilities.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_kraft'
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

register(SisFacilitiesK.__bodId__, SisFacilitiesK)


class SisPlanningK(Base, Vector):
    __tablename__ = 'sis_pl_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sis_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schiene_kraft'
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
    the_geom = Column(Geometry2D)

register(SisPlanningK.__bodId__, SisPlanningK)


class SugBaseClass:
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __label__ = 'facname_de'
    id = Column('xtf_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    validfrom = Column('validfrom', Unicode)
    doc_objektblatt_title = Column('doc_objektblatt_title', Unicode)
    doc_objektblatt_web = Column('doc_objektblatt_web', Unicode)
    doc_gesamtbericht_title = Column('doc_gesamtbericht_title', Unicode)
    doc_gesamtbericht_web = Column('doc_gesamtbericht_web', Unicode)
    the_geom = Column(Geometry2D)


class SugPlanignAnhoerung(Base, SugBaseClass, Vector):
    __tablename__ = 'sug_pl_anhorung'
    __template__ = 'templates/htmlpopup/sug_planning.mako'
    __bodId__ = 'ch.bav.sachplan-unterirdischer-guetertransport_anhoerung'
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validuntil = Column('validuntil', Unicode)

register(SugPlanignAnhoerung.__bodId__, SugPlanignAnhoerung)


class SugFacilityAnhoerung(Base, SugBaseClass, Vector):
    __tablename__ = 'sug_fac_anhorung'
    __template__ = 'templates/htmlpopup/sug_facilities.mako'
    __bodId__ = 'ch.bav.sachplan-unterirdischer-guetertransport_anhoerung'
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)

register(SugFacilityAnhoerung.__bodId__, SugFacilityAnhoerung)


class SugPlanignKraft(Base, SugBaseClass, Vector):
    __tablename__ = 'sug_pl_kraft'
    __template__ = 'templates/htmlpopup/sug_planning.mako'
    __bodId__ = 'ch.bav.sachplan-unterirdischer-guetertransport_kraft'
    meastype_text_de = Column('meastype_text_de', Unicode)
    meastype_text_fr = Column('meastype_text_fr', Unicode)
    meastype_text_it = Column('meastype_text_it', Unicode)
    coordlevel_text_de = Column('coordlevel_text_de', Unicode)
    coordlevel_text_fr = Column('coordlevel_text_fr', Unicode)
    coordlevel_text_it = Column('coordlevel_text_it', Unicode)
    plstatus_text_de = Column('plstatus_text_de', Unicode)
    plstatus_text_fr = Column('plstatus_text_fr', Unicode)
    plstatus_text_it = Column('plstatus_text_it', Unicode)
    validuntil = Column('validuntil', Unicode)

register(SugPlanignKraft.__bodId__, SugPlanignKraft)


class SugFacilityKraft(Base, SugBaseClass, Vector):
    __tablename__ = 'sug_fac_kraft'
    __template__ = 'templates/htmlpopup/sug_facilities.mako'
    __bodId__ = 'ch.bav.sachplan-unterirdischer-guetertransport_kraft'
    facstatus_text_de = Column('facstatus_text_de', Unicode)
    facstatus_text_fr = Column('facstatus_text_fr', Unicode)
    facstatus_text_it = Column('facstatus_text_it', Unicode)
    fackind_text_de = Column('fackind_text_de', Unicode)
    fackind_text_fr = Column('fackind_text_fr', Unicode)
    fackind_text_it = Column('fackind_text_it', Unicode)

register(SugFacilityKraft.__bodId__, SugFacilityKraft)


class KbsZivilflugpl(Base, Vector):
    __tablename__ = 'kataster_belasteter_standorte_zivflpl'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/kataster_belasteter_standorte_zivflpl.mako'
    __bodId__ = 'ch.bazl.kataster-belasteter-standorte-zivilflugplaetze'
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
    url_de = Column('url_de', Unicode)
    url_fr = Column('url_fr', Unicode)
    url_it = Column('url_it', Unicode)
    the_geom = Column(Geometry2D)

register(KbsZivilflugpl.__bodId__, KbsZivilflugpl)


class SchutzgebieteAulavLiechtenstein(Base, Vector):
    __tablename__ = 'schutzgebiete_aulav_liechtenstein'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/schutzgebiete_aulav_liechtenstein.mako'
    __bodId__ = 'ch.bazl.schutzgebiete-aulav_liechtenstein'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register(SchutzgebieteAulavLiechtenstein.__bodId__, SchutzgebieteAulavLiechtenstein)


class AnlageSchienengueterverkehr:
    __tablename__ = 'anlagen_schienengueterverkehr_tooltip'
    __table_args__ = ({'schema': 'bav', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/anlagen_schienengueterverkehr.mako'
    __bodId__ = 'ch.bav.anlagen-schienengueterverkehr'
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

register(LaermBelastungEinsenbahnTatsaechlicheEmissionTag.__bodId__, LaermBelastungEinsenbahnTatsaechlicheEmissionTag)


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

register(LaermBelastungEinsenbahnTatsaechlicheEmissionNacht.__bodId__, LaermBelastungEinsenbahnTatsaechlicheEmissionNacht)


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

register(LaermBelastungEinsenbahnFestgelegteEmissionTag.__bodId__, LaermBelastungEinsenbahnFestgelegteEmissionTag)


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

register(LaermBelastungEinsenbahnFestgelegteEmissionNacht.__bodId__, LaermBelastungEinsenbahnFestgelegteEmissionNacht)


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

register(LaermBelastungEisenbahnEffektiveImmissionenNacht.__bodId__, LaermBelastungEisenbahnEffektiveImmissionenNacht)


class LaermBelastungEisenbahnEffektiveImmissionenTag(Base, LaermBelastungEisenbahnEffektiveImmissionen, Vector):
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_effektive_immissionen_tag'
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_effektive_immissionen_tag.mako'
    lr_day = Column('lr_day', Float)

register(LaermBelastungEisenbahnEffektiveImmissionenTag.__bodId__, LaermBelastungEisenbahnEffektiveImmissionenTag)


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

register(LaermBelastungEisenbahnZulaessigeImmissionenNacht.__bodId__, LaermBelastungEisenbahnZulaessigeImmissionenNacht)


class LaermBelastungEisenbahnZulaessigeImmissionenTag(Base, LaermBelastungEisenbahnZulaessigeImmissionen, Vector):
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_zulaessige_immissionen_tag'
    __template__ = 'templates/htmlpopup/laerm_eisenbahn_zulaessige_immissionen_tag.mako'
    lr_max_day = Column('lr_max_day', Float)

register(LaermBelastungEisenbahnZulaessigeImmissionenTag.__bodId__, LaermBelastungEisenbahnZulaessigeImmissionenTag)


class LaermbelastungEinsenbahnLaermschutzwaende(Base, Vector):
    __tablename__ = 'laermbelastung_eisenbahn_laermschutzwaende'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/laermbelastung_eisenbahn_laermschutzwaende.mako'
    __bodId__ = 'ch.bav.laermbelastung-eisenbahn_laermschutzwaende'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisebarrierheight = Column('noisebarrierheight', Float)
    height_above_track = Column('height_above_track', Float)
    noisebarriertype_de = Column('noisebarriertype_de', Unicode)
    noisebarriertype_fr = Column('noisebarriertype_fr', Unicode)
    noisebarriertype_it = Column('noisebarriertype_it', Unicode)
    noisebarriertype_en = Column('noisebarriertype_en', Unicode)
    material_de = Column('material_de', Unicode)
    material_fr = Column('material_fr', Unicode)
    material_it = Column('material_it', Unicode)
    material_en = Column('material_en', Unicode)
    has_glass = Column('has_glass', Boolean)
    year_construction = Column('year_construction', Integer)
    year_legal = Column('year_legal', Integer)
    the_geom = Column(Geometry2D)

register(LaermbelastungEinsenbahnLaermschutzwaende.__bodId__, LaermbelastungEinsenbahnLaermschutzwaende)


class SifFacilitiesA(Base, Vector):
    __tablename__ = 'sif_fac_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung'
    __template__ = 'templates/htmlpopup/sif_facilities.mako'
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

register(SifFacilitiesA.__bodId__, SifFacilitiesA)


class SifFacilitiesK(Base, Vector):
    __tablename__ = 'sif_fac_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_kraft'
    __template__ = 'templates/htmlpopup/sif_facilities.mako'
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

register(SifFacilitiesK.__bodId__, SifFacilitiesK)


class SifPlanningA(Base, Vector):
    __tablename__ = 'sif_pl_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung'
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
    the_geom = Column(Geometry2D)

register(SifPlanningA.__bodId__, SifPlanningA)


class SifPlanningK(Base, Vector):
    __tablename__ = 'sif_pl_kraft'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_planning.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_kraft'
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
    the_geom = Column(Geometry2D)

register(SifPlanningK.__bodId__, SifPlanningK)


class SifAusgangslage(Base, Vector):
    __tablename__ = 'sif_ausgangslage'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/sif_angaben.mako'
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_ausgangslage'
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

register(SifAusgangslage.__bodId__, SifAusgangslage)


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

register(BazlLaermErsteNachtstunde.__bodId__, BazlLaermErsteNachtstunde)


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

register(BazlLaermHelikopterMaximalpegel.__bodId__, BazlLaermHelikopterMaximalpegel)


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

register(BazlLaermHelikopter.__bodId__, BazlLaermHelikopter)


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

register(BazlLaermKleinGrossflugzeuge.__bodId__, BazlLaermKleinGrossflugzeuge)


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

register(BazlLaermKleinluftfahrzeuge.__bodId__, BazlLaermKleinluftfahrzeuge)


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

register(BazlLaermLetzteNachtstunde.__bodId__, BazlLaermLetzteNachtstunde)


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

register(BazlLaermMilitaerGesamt.__bodId__, BazlLaermMilitaerGesamt)


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

register(BazlLaermZweiteNachtstunde.__bodId__, BazlLaermZweiteNachtstunde)


class SuelFacAnhorung(Base, Vector):
    __tablename__ = 'suel_fac_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
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

register(SuelFacAnhorung.__bodId__, SuelFacAnhorung)


class SuelPlAnhorung(Base, Vector):
    __tablename__ = 'suel_pl_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
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

register(SuelPlAnhorung.__bodId__, SuelPlAnhorung)


class SuelFacRAnhorung(Base, Vector):
    __tablename__ = 'suel_fac_r_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
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

register(SuelFacRAnhorung.__bodId__, SuelFacRAnhorung)


class SuelPlRAnhorung(Base, Vector):
    __tablename__ = 'suel_pl_r_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
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

register(SuelPlRAnhorung.__bodId__, SuelPlRAnhorung)


class SuelFacKraft(Base, Vector):
    __tablename__ = 'suel_fac_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
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

register(SuelFacKraft.__bodId__, SuelFacKraft)


class SuelPlKraft(Base, Vector):
    __tablename__ = 'suel_pl_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
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

register(SuelPlKraft.__bodId__, SuelPlKraft)


class SuelFacRKraft(Base, Vector):
    __tablename__ = 'suel_fac_r_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
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

register(SuelFacRKraft.__bodId__, SuelFacRKraft)


class SuelPlRKraft(Base, Vector):
    __tablename__ = 'suel_pl_r_kraft'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/suel_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_kraft'
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

register(SuelPlRKraft.__bodId__, SuelPlRKraft)


class ChmobilVeloland(Base, Vector):
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

register(ChmobilVeloland.__bodId__, ChmobilVeloland)


class ChmobilWanderland(Base, Vector):
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

register(ChmobilWanderland.__bodId__, ChmobilWanderland)


class ChmobilSkatingland(Base, Vector):
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

register(ChmobilSkatingland.__bodId__, ChmobilSkatingland)


class ChmobilMountainbikeland(Base, Vector):
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

register(ChmobilMountainbikeland.__bodId__, ChmobilMountainbikeland)


class ChmobilSchneeschuhWanderland(Base, Vector):
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

register(ChmobilSchneeschuhWanderland.__bodId__, ChmobilSchneeschuhWanderland)


class FlugplaetzeHeliports(Base, Vector):
    __tablename__ = 'flugplaetze_heliports'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/flugplaetze_heliports.mako'
    __bodId__ = 'ch.bazl.flugplaetze-heliports'
    id = Column('ident', Unicode, primary_key=True)
    icao = Column('icao', Unicode)
    name = Column('name', Unicode)
    location = Column('location', Unicode)
    canton = Column('canton', Unicode)
    arp_east = Column('arp_east', Float)
    arp_north = Column('arp_north', Float)
    elevation = Column('elevation', Float)
    the_geom = Column(Geometry2D)

register(FlugplaetzeHeliports.__bodId__, FlugplaetzeHeliports)


class Gebirgslandeplaetze(Base, Vector):
    __tablename__ = 'gebirgslandeplaetze'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/gebirgslandeplaetze.mako'
    __bodId__ = 'ch.bazl.gebirgslandeplaetze'
    id = Column('ident', Unicode, primary_key=True)
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

register(Gebirgslandeplaetze.__bodId__, Gebirgslandeplaetze)


class Spitallandeplaetze(Base, Vector):
    __tablename__ = 'spitallandeplaetze'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
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

register(Spitallandeplaetze.__bodId__, Spitallandeplaetze)


class Biomasse:
    __tablename__ = 'biomasse'
    __table_args__ = ({'schema': 'bfe', 'autoload': False, 'extend_existing': True})
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    bfs_nummer = Column('bfs_nummer', Integer)
    the_geom = Column(Geometry2D)


class BiomasseVerholzt(Base, Biomasse, Vector):
    __template__ = 'templates/htmlpopup/biomasseverholzt.mako'
    __bodId__ = 'ch.bfe.biomasse-verholzt'
    woody = Column('woody', Float)

register(BiomasseVerholzt.__bodId__, BiomasseVerholzt)


class BiomasseNichtVerholzt(Base, Biomasse, Vector):
    __template__ = 'templates/htmlpopup/biomassenichtverholzt.mako'
    __bodId__ = 'ch.bfe.biomasse-nicht-verholzt'
    non_woody = Column('non_woody', Float)

register(BiomasseNichtVerholzt.__bodId__, BiomasseNichtVerholzt)


class SeilbahnenBundeskonzession:
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.seilbahnen-bundeskonzession'
    __label__ = 'anlagename'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    anlagenr = Column('anlagenr', Unicode)
    anlagename = Column('anlagename', Unicode)
    betreiber_tuabkuerzung = Column('betreiber_tuabkuerzung', Unicode)


class SeilbahnenBundeskonzessionBauwerk(Base, SeilbahnenBundeskonzession, Vector):
    __tablename__ = 'seilbahnen_bundeskonzession_bauwerk'
    __template__ = 'templates/htmlpopup/seilbahnenbundeskonzession_bauwerk.mako'
    bauwerkstyp = Column('bauwerkstyp', Unicode)

register(SeilbahnenBundeskonzessionBauwerk.__bodId__, SeilbahnenBundeskonzessionBauwerk)


class SeilbahnenBundeskonzessioSeilbahnstreke(Base, SeilbahnenBundeskonzession, Vector):
    __tablename__ = 'seilbahnen_bundeskonzession_seilbahnstrecke'
    __template__ = 'templates/htmlpopup/seilbahnenbundeskonzession_seilbahnstrecke.mako'
    bahntyp = Column('bahntyp', Unicode)
    fahrzeugtyp = Column('fahrzeugtyp', Unicode)
    hoehendifferenz = Column('hoehendifferenz', Unicode)
    laengeschief = Column('laengeschief', Unicode)

register(SeilbahnenBundeskonzessioSeilbahnstreke.__bodId__, SeilbahnenBundeskonzessioSeilbahnstreke)


class SeilbahnenBundeskonzessioStation(Base, SeilbahnenBundeskonzession, Vector):
    __tablename__ = 'seilbahnen_bundeskonzession_station'
    __template__ = 'templates/htmlpopup/seilbahnenbundeskonzession_station.mako'
    bp_nummer = Column('bp_nummer', Unicode)
    bp_name = Column('bp_name', Unicode)
    stationstyp = Column('stationstyp', Unicode)

register(SeilbahnenBundeskonzessioStation.__bodId__, SeilbahnenBundeskonzessioStation)


class Elektrizitaetsproduktionsanlagen(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'elektrizitaetsproduktionsanlagen'
    __template__ = 'templates/htmlpopup/elektrizitaetsproduktionsanlagen.mako'
    __extended_info__ = True
    __bodId__ = 'ch.bfe.elektrizitaetsproduktionsanlagen'
    __label__ = 'id'
    id = Column('xtf_id', Unicode, primary_key=True)
    address = Column('address', Unicode)
    canton = Column('canton', Unicode)
    beginning_of_operation = Column('beginning_of_operation', Unicode)
    initial_power = Column('initial_power', Unicode)
    total_power = Column('total_power', Unicode)
    main_category_de = Column('main_category_de', Unicode)
    main_category_fr = Column('main_category_fr', Unicode)
    main_category_it = Column('main_category_it', Unicode)
    main_category_en = Column('main_category_en', Unicode)
    sub_category_de = Column('sub_category_de', Unicode)
    sub_category_fr = Column('sub_category_fr', Unicode)
    sub_category_it = Column('sub_category_it', Unicode)
    sub_category_en = Column('sub_category_en', Unicode)
    plant_type_de = Column('plant_type_de', Unicode)
    plant_type_fr = Column('plant_type_fr', Unicode)
    plant_type_it = Column('plant_type_it', Unicode)
    plant_type_en = Column('plant_type_en', Unicode)
    detail_date = Column('detail_date', Unicode)
    detail_power = Column('detail_power', Unicode)
    detail_inclination = Column('detail_inclination', Unicode)
    detail_plant_type_de = Column('detail_plant_type_de', Unicode)
    detail_plant_type_fr = Column('detail_plant_type_fr', Unicode)
    detail_plant_type_it = Column('detail_plant_type_it', Unicode)
    detail_plant_type_en = Column('detail_plant_type_en', Unicode)
    detail_orientation_de = Column('detail_orientation_de', Unicode)
    detail_orientation_fr = Column('detail_orientation_fr', Unicode)
    detail_orientation_it = Column('detail_orientation_it', Unicode)
    detail_orientation_en = Column('detail_orientation_en', Unicode)
    the_geom = Column(Geometry2D)

register(Elektrizitaetsproduktionsanlagen.__bodId__, Elektrizitaetsproduktionsanlagen)


class WaermepotentialGewaesser(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'waermepotential_gewaesser'
    __template__ = 'templates/htmlpopup/waermepotential_gewaesser.mako'
    __bodId__ = 'ch.bfe.waermepotential-gewaesser'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    heat_extraction_gwha = Column('heat_extraction_gwha', Integer)
    heat_disposal_gwha = Column('heat_disposal_gwha', Integer)
    further_information = Column('further_information', Unicode)
    the_geom = Column(Geometry2D)

register(WaermepotentialGewaesser.__bodId__, WaermepotentialGewaesser)


class ElektrischeAnlagenUeber36Line(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'elektrische_anlagen_ueber_36_line'
    __template__ = 'templates/htmlpopup/bfe_elektrische_anlagen_ueber_36_line.mako'
    __bodId__ = 'ch.bfe.elektrische-anlagen_ueber_36'
    __label__ = 'fid'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Unicode)
    bezeichnung = Column('bezeichnung', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    stromnetztyp = Column('stromnetztyp', Unicode)
    leitungtyp = Column('leitungtyp', Unicode)
    spannung = Column('spannung', Unicode)
    spannungandere = Column('spannungandere', Unicode)
    frequenz = Column('frequenz', Unicode)
    the_geom = Column(Geometry2D)

register(ElektrischeAnlagenUeber36Line.__bodId__, ElektrischeAnlagenUeber36Line)


class ElektrischeAnlagenUeber36Point(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'elektrische_anlagen_ueber_36_point'
    __template__ = 'templates/htmlpopup/bfe_elektrische_anlagen_ueber_36_point.mako'
    __bodId__ = 'ch.bfe.elektrische-anlagen_ueber_36'
    __label__ = 'fid'
    __maxscale__ = 50000
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    stromnetztyp = Column('stromnetztyp', Unicode)
    masttyp = Column('masttyp', Unicode)
    hoehe = Column('hoehe', Integer)
    the_geom = Column(Geometry2D)

register(ElektrischeAnlagenUeber36Point.__bodId__, ElektrischeAnlagenUeber36Point)


class ElektrischeAnlagenUeber36Station:
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __bodId__ = 'ch.bfe.elektrische-anlagen_ueber_36'
    __template__ = 'templates/htmlpopup/bfe_elektrische_anlagen_ueber_36_station.mako'
    __label__ = 'fid'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Unicode)
    bezeichnung = Column('bezeichnung', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    stromnetztyp = Column('stromnetztyp', Unicode)
    stationtyp = Column('stationtyp', Unicode)
    the_geom = Column(Geometry2D)


class ElektrischeAnlagenUeber36StationPoly(Base, ElektrischeAnlagenUeber36Station, Vector):
    __tablename__ = 'elektrische_anlagen_ueber_36_station_poly'
    __minscale__ = 1
    __maxscale__ = 25000

register(ElektrischeAnlagenUeber36StationPoly.__bodId__, ElektrischeAnlagenUeber36StationPoly)


class ElektrischeAnlagenUeber36StationPointWithPoly(Base, ElektrischeAnlagenUeber36Station, Vector):
    __tablename__ = 'elektrische_anlagen_ueber_36_station_point_with_poly'
    __minscale__ = 25000


register(ElektrischeAnlagenUeber36StationPointWithPoly.__bodId__, ElektrischeAnlagenUeber36StationPointWithPoly)


class ElektrischeAnlagenUeber36StationPointNoPoly(Base, ElektrischeAnlagenUeber36Station, Vector):
    __tablename__ = 'elektrische_anlagen_ueber_36_station_point_no_poly'


register(ElektrischeAnlagenUeber36StationPointNoPoly.__bodId__, ElektrischeAnlagenUeber36StationPointNoPoly)


class BetriebeStoerfallverordnungEisenbahnanlagen(Base, Vector):
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __tablename__ = 'stoerfallverordnung_eisenbahnanlagen_betriebe'
    __template__ = 'templates/htmlpopup/bav_betriebe_stoerfallverordnung_eisenbahnanlagen.mako'
    __bodId__ = 'ch.bav.betriebe-stoerfallverordnung_eisenbahnanlagen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register(BetriebeStoerfallverordnungEisenbahnanlagen.__bodId__, BetriebeStoerfallverordnungEisenbahnanlagen)


class LageStoerfallverordnungEisenbahnanlagen(Base, Vector):
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __tablename__ = 'stoerfallverordnung_eisenbahnanlagen_lage'
    __template__ = 'templates/htmlpopup/bav_lage_stoerfallverordnung_eisenbahnanlagen.mako'
    __bodId__ = 'ch.bav.lage-stoerfallverordnung_eisenbahnanlagen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    geom_type = Column('geom_type', Unicode)
    the_geom = Column(Geometry2D)

register(LageStoerfallverordnungEisenbahnanlagen.__bodId__, LageStoerfallverordnungEisenbahnanlagen)


class BakomchStandorteMobilfunkanlagen(Base, Vector):
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __tablename__ = 'standorte_mobilfunkanlagen'
    __template__ = 'templates/htmlpopup/bakom_standorte_mobilfunkanlagen.mako'
    __bodId__ = 'ch.bakom.standorte-mobilfunkanlagen'
    __label__ = 'station'
    id = Column('bgdi_id', Integer, primary_key=True)
    station = Column('station', Unicode)
    typ_de = Column('typ_de', Unicode)
    typ_fr = Column('typ_fr', Unicode)
    typ_it = Column('typ_it', Unicode)
    typ_en = Column('typ_en', Unicode)
    koord = Column('koord', Unicode)
    power_de = Column('power_de', Unicode)
    power_fr = Column('power_fr', Unicode)
    power_it = Column('power_it', Unicode)
    power_en = Column('power_en', Unicode)
    techno_de = Column('techno_de', Unicode)
    techno_fr = Column('techno_fr', Unicode)
    techno_it = Column('techno_it', Unicode)
    techno_en = Column('techno_en', Unicode)
    adaptiv_de = Column('adaptiv_de', Unicode)
    adaptiv_fr = Column('adaptiv_fr', Unicode)
    adaptiv_it = Column('adaptiv_it', Unicode)
    adaptiv_en = Column('adaptiv_en', Unicode)
    bewilligung_de = Column('bewilligung_de', Unicode)
    bewilligung_fr = Column('bewilligung_fr', Unicode)
    bewilligung_it = Column('bewilligung_it', Unicode)
    bewilligung_en = Column('bewilligung_en', Unicode)
    agw_de = Column('agw_de', Unicode)
    agw_fr = Column('agw_fr', Unicode)
    agw_it = Column('agw_it', Unicode)
    agw_en = Column('agw_en', Unicode)
    the_geom = Column(Geometry2D)

register(BakomchStandorteMobilfunkanlagen.__bodId__, BakomchStandorteMobilfunkanlagen)


class PhotovoltaikGrossanlagen(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'photovoltaik_grossanlagen'
    __template__ = 'templates/htmlpopup/bfe_photovoltaik_grossanlagen.mako'
    __bodId__ = 'ch.bfe.photovoltaik-grossanlagen'
    __label__ = 'projectname'
    id = Column('bgdi_id', Integer, primary_key=True)
    projectname = Column('projectname', Unicode)
    projectmanagement = Column('projectmanagement', Unicode)
    projectweb = Column('projectweb', Unicode)
    elevation = Column('elevation', Integer)
    power = Column('power', Unicode)
    annualproduction = Column('annualproduction', Unicode)
    winterproduction = Column('winterproduction', Unicode)
    specificannualproduction = Column('specificannualproduction', Unicode)
    specificwinterproduction = Column('specificwinterproduction', Unicode)
    ref_status = Column('ref_status', Unicode)
    statuscategory_de = Column('statuscategory_de', Unicode)
    statuscategory_fr = Column('statuscategory_fr', Unicode)
    statuscategory_it = Column('statuscategory_it', Unicode)
    statuscategory_en = Column('statuscategory_en', Unicode)
    the_geom = Column(Geometry2D)

register(PhotovoltaikGrossanlagen.__bodId__, PhotovoltaikGrossanlagen)


class SolarenergieEinstrahlung:
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __extended_info__ = True
    __label__ = 'id'
    id = Column('id', Integer, primary_key=True)
    x = Column('x', Integer)
    y = Column('y', Integer)
    globalstrahlung_jahressumme_kwhm2 = Column('globalstrahlung_jahressumme_kwhm2', Integer)
    globalstrahlung_wintersumme_kwhm2 = Column('globalstrahlung_wintersumme_kwhm2', Integer)
    globalstrahlung_januar_kwhm2 = Column('globalstrahlung_januar_kwhm2', Integer)
    globalstrahlung_februar_kwhm2 = Column('globalstrahlung_februar_kwhm2', Integer)
    globalstrahlung_maerz_kwhm2 = Column('globalstrahlung_maerz_kwhm2', Integer)
    globalstrahlung_april_kwhm2 = Column('globalstrahlung_april_kwhm2', Integer)
    globalstrahlung_mai_kwhm2 = Column('globalstrahlung_mai_kwhm2', Integer)
    globalstrahlung_juni_kwhm2 = Column('globalstrahlung_juni_kwhm2', Integer)
    globalstrahlung_juli_kwhm2 = Column('globalstrahlung_juli_kwhm2', Integer)
    globalstrahlung_august_kwhm2 = Column('globalstrahlung_august_kwhm2', Integer)
    globalstrahlung_september_kwhm2 = Column('globalstrahlung_september_kwhm2', Integer)
    globalstrahlung_oktober_kwhm2 = Column('globalstrahlung_oktober_kwhm2', Integer)
    globalstrahlung_november_kwhm2 = Column('globalstrahlung_november_kwhm2', Integer)
    globalstrahlung_dezember_kwhm2 = Column('globalstrahlung_dezember_kwhm2', Integer)
    pvproduktion_jahressumme_kwhkwp = Column('pvproduktion_jahressumme_kwhkwp', Integer)
    pvproduktion_wintersumme_kwhkwp = Column('pvproduktion_wintersumme_kwhkwp', Integer)
    pvproduktion_januar_kwhkwp = Column('pvproduktion_januar_kwhkwp', Integer)
    pvproduktion_februar_kwhkwp = Column('pvproduktion_februar_kwhkwp', Integer)
    pvproduktion_maerz_kwhkwp = Column('pvproduktion_maerz_kwhkwp', Integer)
    pvproduktion_april_kwhkwp = Column('pvproduktion_april_kwhkwp', Integer)
    pvproduktion_mai_kwhkwp = Column('pvproduktion_mai_kwhkwp', Integer)
    pvproduktion_juni_kwhkwp = Column('pvproduktion_juni_kwhkwp', Integer)
    pvproduktion_juli_kwhkwp = Column('pvproduktion_juli_kwhkwp', Integer)
    pvproduktion_august_kwhkwp = Column('pvproduktion_august_kwhkwp', Integer)
    pvproduktion_september_kwhkwp = Column('pvproduktion_september_kwhkwp', Integer)
    pvproduktion_oktober_kwhkwp = Column('pvproduktion_oktober_kwhkwp', Integer)
    pvproduktion_november_kwhkwp = Column('pvproduktion_november_kwhkwp', Integer)
    pvproduktion_dezember_kwhkwp = Column('pvproduktion_dezember_kwhkwp', Integer)
    the_geom = Column(Geometry2D)


class SolarenergieEinstrahlung0Grad(Base, SolarenergieEinstrahlung, Vector):
    __tablename__ = 'solarenergie_einstrahlung_0_grad'
    __bodId__ = 'ch.bfe.solarenergie-einstrahlung_0_grad'
    __template__ = 'templates/htmlpopup/bfe_solarenergie_einstrahlung_0_grad.mako'

register(SolarenergieEinstrahlung0Grad.__bodId__, SolarenergieEinstrahlung0Grad)


class SolarenergieEinstrahlung30Grad(Base, SolarenergieEinstrahlung, Vector):
    __tablename__ = 'solarenergie_einstrahlung_30_grad'
    __bodId__ = 'ch.bfe.solarenergie-einstrahlung_30_grad'
    __template__ = 'templates/htmlpopup/bfe_solarenergie_einstrahlung_30_grad.mako'

register(SolarenergieEinstrahlung30Grad.__bodId__, SolarenergieEinstrahlung30Grad)


class SolarenergieEinstrahlung75Grad(Base, SolarenergieEinstrahlung, Vector):
    __tablename__ = 'solarenergie_einstrahlung_75_grad'
    __bodId__ = 'ch.bfe.solarenergie-einstrahlung_75_grad'
    __template__ = 'templates/htmlpopup/bfe_solarenergie_einstrahlung_75_grad.mako'

register(SolarenergieEinstrahlung75Grad.__bodId__, SolarenergieEinstrahlung75Grad)


class SolarenergieEinstrahlung90Grad(Base, SolarenergieEinstrahlung, Vector):
    __tablename__ = 'solarenergie_einstrahlung_90_grad'
    __bodId__ = 'ch.bfe.solarenergie-einstrahlung_90_grad'
    __template__ = 'templates/htmlpopup/bfe_solarenergie_einstrahlung_90_grad.mako'

register(SolarenergieEinstrahlung90Grad.__bodId__, SolarenergieEinstrahlung90Grad)


class Grundwasserwaermenutzungspotential(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'grundwasserwaermenutzungspotential'
    __template__ = 'templates/htmlpopup/bfe_grundwasserwaermenutzungspotential.mako'
    __bodId__ = 'ch.bfe.grundwasserwaermenutzungspotential'
    __label__ = 'uuid'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('fid', Integer)
    name = Column('name', Unicode)
    uuid = Column('uuid', Unicode)
    area_m2 = Column('area_m2', Float)
    groundwater_thickness_m = Column('groundwater_thickness_m', Float)
    volume_m3 = Column('volume_m3', Float)
    groundwater_depth_m = Column('groundwater_depth_m', Float)
    multi_layer_aquifer = Column('multi_layer_aquifer', Unicode)
    confined = Column('confined', Unicode)
    energy_potential_kwh = Column('energy_potential_kwh', Float)
    heat_potential_kw = Column('heat_potential_kw', Float)
    heat_potential_w_per_m2 = Column('heat_potential_w_per_m2', Float)
    reliability = Column('reliability', Unicode)
    quality_heat_atmosphere = Column('quality_heat_atmosphere', Float)
    heat_atmosphere_percent = Column('heat_atmosphere_percent', Float)
    heat_atmosphere_kw = Column('heat_atmosphere_kw', Float)
    heat_precipitation_percent = Column('heat_precipitation_percent', Float)
    heat_precipitation_kw = Column('heat_precipitation_kw', Float)
    heat_catchment_percent = Column('heat_catchment_percent', Float)
    heat_catchment_kw = Column('heat_catchment_kw', Float)
    catchment_area_m2 = Column('catchment_area_m2', Float)
    heat_geothermal_percent = Column('heat_geothermal_percent', Float)
    heat_geothermal_kw = Column('heat_geothermal_kw', Float)
    comment = Column('comment', Unicode)
    the_geom = Column(Geometry2D)

register(Grundwasserwaermenutzungspotential.__bodId__, Grundwasserwaermenutzungspotential)


class LadebedarfsweltFahrzeuge(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'ladebedarfswelt_fahrzeuge'
    __template__ = 'templates/htmlpopup/bfe_ladebedarfswelt_fahrzeuge.mako'
    __bodId__ = 'ch.bfe.ladebedarfswelt-fahrzeuge'
    __label__ = 'name_gemeinde'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_gemeinde = Column('name_gemeinde', Unicode)
    jahr = Column('jahr', Integer)
    anzahl_fahrzeugbestand_personenwagen_phev = Column('anzahl_fahrzeugbestand_personenwagen_phev', Float)
    anzahl_fahrzeugbestand_personenwagen_bev = Column('anzahl_fahrzeugbestand_personenwagen_bev', Float)
    anteil_fahrzeugbestand_personenwagen_steckerfahrzeuge = Column('anteil_fahrzeugbestand_personenwagen_steckerfahrzeuge', Float)
    the_geom = Column(Geometry2D)

register(LadebedarfsweltFahrzeuge.__bodId__, LadebedarfsweltFahrzeuge)


class LadebedarfsweltHeimladeverfuegbarkeit:
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/bfe_ladebedarfswelt_heimladeverfuegbarkeit.mako'
    __label__ = 'name_gemeinde'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_gemeinde = Column('name_gemeinde', Unicode)
    jahr = Column('jahr', Integer)
    ladewelt = Column('ladewelt', Unicode)
    anteil_weder_heim_noch_arbeit = Column('anteil_weder_heim_noch_arbeit', Float)
    anteil_kein_heim = Column('anteil_kein_heim', Float)
    the_geom = Column(Geometry2D)


class LadebedarfsweltHeimladeverfuegbarkeitBequem(Base, LadebedarfsweltHeimladeverfuegbarkeit, Vector):
    __bodId__ = 'ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_bequem'
    __tablename__ = 'ladebedarfswelt_heimladeverfuegbarkeit_bequem'

register(LadebedarfsweltHeimladeverfuegbarkeitBequem.__bodId__, LadebedarfsweltHeimladeverfuegbarkeitBequem)


class LadebedarfsweltHeimladeverfuegbarkeitFlexibel(Base, LadebedarfsweltHeimladeverfuegbarkeit, Vector):
    __bodId__ = 'ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_flexibel'
    __tablename__ = 'ladebedarfswelt_heimladeverfuegbarkeit_flexibel'

register(LadebedarfsweltHeimladeverfuegbarkeitFlexibel.__bodId__, LadebedarfsweltHeimladeverfuegbarkeitFlexibel)


class LadebedarfsweltHeimladeverfuegbarkeitGeplant(Base, LadebedarfsweltHeimladeverfuegbarkeit, Vector):
    __bodId__ = 'ch.bfe.ladebedarfswelt-heimladeverfuegbarkeit_geplant'
    __tablename__ = 'ladebedarfswelt_heimladeverfuegbarkeit_geplant'

register(LadebedarfsweltHeimladeverfuegbarkeitGeplant.__bodId__, LadebedarfsweltHeimladeverfuegbarkeitGeplant)


class LadebedarfsweltLadepunkte:
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/bfe_ladebedarfswelt_ladepunkte.mako'
    __label__ = 'name_gemeinde'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_gemeinde = Column('name_gemeinde', Unicode)
    jahr = Column('jahr', Integer)
    allgemein_zugaenglich_anzahl_ladepunkte = Column('allgemein_zugaenglich_anzahl_ladepunkte', Float)
    quartier_ac_ladepunkte = Column('quartier_ac_ladepunkte', Float)
    zielort_ac_ladepunkte = Column('zielort_ac_ladepunkte', Float)
    zielort_dc_50_ladepunkte = Column('zielort_dc_50_ladepunkte', Float)
    quartier_dc_150_ladepunkte = Column('quartier_dc_150_ladepunkte', Float)
    schnell_dc_150_ladepunkte = Column('schnell_dc_150_ladepunkte', Float)
    schnell_dc_350_ladepunkte = Column('schnell_dc_350_ladepunkte', Float)
    heim_ac_ladepunkte = Column('heim_ac_ladepunkte', Float)
    arbeit_ac_ladepunkte = Column('arbeit_ac_ladepunkte', Float)
    the_geom = Column(Geometry2D)


class LadebedarfsweltLadepunkteBequem(Base, LadebedarfsweltLadepunkte, Vector):
    __tablename__ = 'ladebedarfswelt_ladepunkte_bequem'
    __bodId__ = 'ch.bfe.ladebedarfswelt-ladepunkte_bequem'

register(LadebedarfsweltLadepunkteBequem.__bodId__, LadebedarfsweltLadepunkteBequem)


class LadebedarfsweltLadepunkteFlexibel(Base, LadebedarfsweltLadepunkte, Vector):
    __tablename__ = 'ladebedarfswelt_ladepunkte_flexibel'
    __bodId__ = 'ch.bfe.ladebedarfswelt-ladepunkte_flexibel'

register(LadebedarfsweltLadepunkteFlexibel.__bodId__, LadebedarfsweltLadepunkteFlexibel)


class LadebedarfsweltLadepunkteGeplant(Base, LadebedarfsweltLadepunkte, Vector):
    __tablename__ = 'ladebedarfswelt_ladepunkte_geplant'
    __bodId__ = 'ch.bfe.ladebedarfswelt-ladepunkte_geplant'

register(LadebedarfsweltLadepunkteGeplant.__bodId__, LadebedarfsweltLadepunkteGeplant)


class LadebedarfsweltStrombedarf(Base, Vector):
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __tablename__ = 'ladebedarfswelt_strombedarf'
    __template__ = 'templates/htmlpopup/bfe_ladebedarfswelt_strombedarf.mako'
    __bodId__ = 'ch.bfe.ladebedarfswelt-strombedarf'
    __label__ = 'name_gemeinde'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_gemeinde = Column('name_gemeinde', Unicode)
    jahr = Column('jahr', Integer)
    summe_gwh = Column('summe_gwh', Float)
    heim_energie_anteil = Column('heim_energie_anteil', Float)
    arbeit_energie_anteil = Column('arbeit_energie_anteil', Float)
    quartier_energie_anteil = Column('quartier_energie_anteil', Float)
    zielort_energie_anteil = Column('zielort_energie_anteil', Float)
    schnell_energie_anteil = Column('schnell_energie_anteil', Float)
    the_geom = Column(Geometry2D)

register(LadebedarfsweltStrombedarf.__bodId__, LadebedarfsweltStrombedarf)


class Landschaftsruhezonen(Base, Vector):
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __tablename__ = 'landschaftsruhezonen'
    __template__ = 'templates/htmlpopup/bazl_landschaftsruhezonen.mako'
    __bodId__ = 'ch.bazl.landschaftsruhezonen'
    __label__ = 'name_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_de = Column('name_de', Unicode)
    name_fr = Column('name_fr', Unicode)
    name_it = Column('name_it', Unicode)
    name_en = Column('name_en', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    description_en = Column('description_en', Unicode)
    the_geom = Column(Geometry2D)

register(Landschaftsruhezonen.__bodId__, Landschaftsruhezonen)


class ReflektierendeFlaechenFlugplaetze(Base, Vector):
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __tablename__ = 'reflektierende_flaechen_flugplaetze'
    __template__ = 'templates/htmlpopup/bazl_reflektierende_flaechen_flugplaetze.mako'
    __bodId__ = 'ch.bazl.reflektierende-flaechen_flugplaetze'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    icao = Column('icao', Unicode)
    name = Column('name', Unicode)
    status_de = Column('status_de', Unicode)
    status_fr = Column('status_fr', Unicode)
    status_it = Column('status_it', Unicode)
    status_en = Column('status_en', Unicode)
    the_geom = Column(Geometry2D)

register(ReflektierendeFlaechenFlugplaetze.__bodId__, ReflektierendeFlaechenFlugplaetze)
