# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer, Date
from sqlalchemy.types import Numeric, Float

from chsdi.models import register, bases
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
    originator = Column('originator', Unicode)
    canton = Column('canton', Unicode)
    municipality = Column('municipality', Unicode)
    approval_date = Column('approval_date', Unicode)
    status_id = Column('status_id', Unicode)
    legalstatus_tid = Column('legalstatus_tid', Unicode)
    legalstatus_de = Column('legalstatus_de', Unicode)
    legalstatus_fr = Column('legalstatus_fr', Unicode)
    legalstatus_it = Column('legalstatus_it', Unicode)
    title = Column('title', Unicode)
    weblink = Column('weblink', Unicode)
    valid_from = Column('valid_from', Unicode)
    valid_until = Column('valid_until', Unicode)
    latest_modification = Column('latest_modification', Unicode)
    doc_description = Column('doc_description', Unicode)
    doc_id = Column('doc_id', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.sicherheitszonenplan', SicherheitsZonenPlan)


class IVSNat(Base, Vector):
    __tablename__ = 'ivs_nat'
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
register('ch.astra.ivs-nat-verlaeufe', IVSNat)


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


class Ausnahmetransportrouten(Base, Vector):
    __tablename__ = 'ausnahmetransportrouten'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ausnahmetransportrouten.mako'
    __bodId__ = 'ch.astra.ausnahmetransportrouten'
    __label__ = 'id'
    id = Column('id', Integer, primary_key=True)
    bgdi_id = Column('bgdi_id', Integer)
    ri_getrenn = Column('ri_getrenn', Unicode)
    anz_spuren = Column('anz_spuren', Integer)
    strassen_typ = Column('strassen_typ', Unicode)
    routentyp_id = Column('routentyp_id', Integer)
    the_geom = Column(Geometry2D)

register('ch.astra.ausnahmetransportrouten', Ausnahmetransportrouten)


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


class Unf:
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/astra_unfaelle.mako'
    __label__ = 'accidenttype_de'
    __timeInstant__ = 'accidentyear'
    __queryable_attributes__ = ['accidenttype_de', 'accidenttype_fr', 'accidenttype_it',
                                'accidenttypecode', 'accidentday_de', 'accidentday_fr', 'accidentday_it',
                                'accidentyear', 'severitycategory_de', 'severitycategory_fr', 'severitycategory_it',
                                'severitycategorycode', 'roadtype_de', 'roadtype_fr', 'roadtype_it',
                                'roadtypecode', 'canton', 'fsocommunecode']
    id = Column('uuid', Unicode, primary_key=True)
    accidenttype_de = Column('accidenttype_de', Unicode)
    accidenttype_fr = Column('accidenttype_fr', Unicode)
    accidenttype_it = Column('accidenttype_it', Unicode)
    accidenttypecode = Column('accidenttypecode', Integer)
    accidentday_de = Column('accidentday_de', Unicode)
    accidentday_fr = Column('accidentday_fr', Unicode)
    accidentday_it = Column('accidentday_it', Unicode)
    accidentyear = Column('accidentyear', Integer)
    severitycategory_de = Column('severitycategory_de', Unicode)
    severitycategory_fr = Column('severitycategory_fr', Unicode)
    severitycategory_it = Column('severitycategory_it', Unicode)
    severitycategorycode = Column('severitycategorycode', Unicode)
    roadtype_de = Column('roadtype_de', Unicode)
    roadtype_fr = Column('roadtype_fr', Unicode)
    roadtype_it = Column('roadtype_it', Unicode)
    roadtypecode = Column('roadtypecode', Integer)
    canton = Column('canton', Unicode)
    fsocommunecode = Column('fsocommunecode', Unicode)
    the_geom = Column(Geometry2D)


class UnfPersAlle(Base, Unf, Vector):
    __tablename__ = 'unf_pers_alle'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_alle'

register('ch.astra.unfaelle-personenschaeden_alle', UnfPersAlle)


class UnfPersCasualties(Base, Unf, Vector):
    __tablename__ = 'unf_pers_getoetete'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_getoetete'

register('ch.astra.unfaelle-personenschaeden_getoetete', UnfPersCasualties)


class UnfPersFuss(Base, Unf, Vector):
    __tablename__ = 'unf_pers_fussgaenger'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_fussgaenger'

register('ch.astra.unfaelle-personenschaeden_fussgaenger', UnfPersFuss)


class UnfPersMoto(Base, Unf, Vector):
    __tablename__ = 'unf_pers_motorraeder'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_motorraeder'

register('ch.astra.unfaelle-personenschaeden_motorraeder', UnfPersMoto)


class UnfPersVelo(Base, Unf, Vector):
    __tablename__ = 'unf_pers_fahrraeder'
    __bodId__ = 'ch.astra.unfaelle-personenschaeden_fahrraeder'

register('ch.astra.unfaelle-personenschaeden_fahrraeder', UnfPersVelo)


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
    bfsnr = Column('bfsnr', Integer)
    punktezahl = Column('punktezahl', Numeric)
    einwohner = Column('einwohner', Numeric)
    energiestadtseit = Column('energiestadtseit', Unicode)
    beteiligtegemeinde = Column('beteiligtegemeinde', Unicode)
    anzahlaudits = Column('anzahlaudits', Numeric)
    berater = Column('berater', Unicode)
    linkberater = Column('linkberater', Unicode)
    linkfaktenblatt = Column('linkfaktenblatt', Unicode)
    linkenergiestadtweb = Column('linkenergiestadtweb', Unicode)
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
    bet_energiestaedte = Column('bet_energiestaedte', Unicode)
    bet_traegerverein = Column('bet_traegerverein', Unicode)
    berater = Column('berater', Unicode)
    linkberater = Column('linkberater', Unicode)
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
    gemeinde = Column('gemeinde', Unicode)
    berater = Column('berater', Unicode)
    linkberater = Column('linkberater', Unicode)
    linkfaktenblatt_de = Column('linkfaktenblatt_de', Unicode)
    linkfaktenblatt_fr = Column('linkfaktenblatt_fr', Unicode)
    linkfaktenblatt_it = Column('linkfaktenblatt_it', Unicode)
    linkfaktenblatt_en = Column('linkfaktenblatt_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte-2000watt-areale', Energiestaedte2000wattAreale)


class EnergiestaedteAufdemweg2000watt(Base, Vector):
    __tablename__ = 'energiestaedte_aufdemweg_2000watt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte_2000watt_auf_dem_weg.mako'
    __bodId__ = 'ch.bfe.energiestaedte-2000watt-aufdemweg'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    kategorie = Column('kategorie', Unicode)
    berater = Column('berater', Unicode)
    linkberater = Column('linkberater', Unicode)
    linkfaktenblatt = Column('linkfaktenblatt', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte-2000watt-aufdemweg', EnergiestaedteAufdemweg2000watt)


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


class Bakomfernsehsender(Base, Vector):
    __tablename__ = 'nisdb_bro_tooltip'
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


class Bakomgsm(Base, Vector):
    __tablename__ = 'nisdb_gsm'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomgsm.mako'
    __bodId__ = 'ch.bakom.mobil-antennenstandorte-gsm'
    __label__ = 'powercode'
    id = Column('id', Integer, primary_key=True)
    powercode = Column('powercode', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.mobil-antennenstandorte-gsm', Bakomgsm)


class Bakomumts(Base, Vector):
    __tablename__ = 'nisdb_umts'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomumts.mako'
    __bodId__ = 'ch.bakom.mobil-antennenstandorte-umts'
    __label__ = 'powercode'
    id = Column('id', Integer, primary_key=True)
    powercode = Column('powercode', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.mobil-antennenstandorte-umts', Bakomumts)


class Bakomlte(Base, Vector):
    __tablename__ = 'nisdb_lte'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomlte.mako'
    __bodId__ = 'ch.bakom.mobil-antennenstandorte-lte'
    __label__ = 'powercode'
    id = Column('id', Integer, primary_key=True)
    powercode = Column('powercode', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bakom.mobil-antennenstandorte-lte', Bakomlte)


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
    name = Column('name', Unicode)
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
    __tablename__ = 'luftfahrthindernis'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/luftfahrthindernisse.mako'
    __bodId__ = 'ch.bazl.luftfahrthindernis'
    __extended_info__ = True
    __queryable_attributes__ = ['registrationnumber', 'state', 'maxheightagl',
                                'topelevationamsl', 'totallength', 'startofconstruction', 'abortionaccomplished']
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
    duration = Column('duration', Unicode)
    geomtype = Column('geomtype', Unicode)
    abortionaccomplished = Column('abortionaccomplished', Date)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bazl.luftfahrthindernis', Luftfahrthindernis)


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


class SgtFacilities(Base, Vector):
    __tablename__ = 'geologische_tiefenlager_fac'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
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
    description = Column('description', Unicode)
    web = Column('web', Unicode)
    objname_text_de = Column('objname_text_de', Unicode)
    objname_text_fr = Column('objname_text_fr', Unicode)
    objname_text_it = Column('objname_text_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 80005
    __maxscale__ = 100000005
    the_geom = Column(Geometry2D)


class SgtPlanning(Base, Vector):
    __tablename__ = 'geologische_tiefenlager'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    facname_de = Column('facname_de', Unicode)
    measurename_de = Column('measurename_de', Unicode)
    measurename_fr = Column('measurename_fr', Unicode)
    measurename_it = Column('measurename_it', Unicode)
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
    description = Column('description', Unicode)
    web = Column('web', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005


class SgtPlanningRaster(Base, Vector):
    __tablename__ = 'geologische_tiefenlager_raster'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    measurename_de = Column('measurename_de', Unicode)
    measurename_fr = Column('measurename_fr', Unicode)
    measurename_it = Column('measurename_it', Unicode)
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
    description = Column('description', Unicode)
    web = Column('web', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-geologie-tiefenlager', SgtFacilities)
register('ch.bfe.sachplan-geologie-tiefenlager', SgtPlanning)
register('ch.bfe.sachplan-geologie-tiefenlager', SgtPlanningRaster)


class PtFacilities(Base, Vector):
    __tablename__ = 'geologische_tief_vernehm_fac_pt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/vernehm_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung'
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


class PtPlanning(Base, Vector):
    __tablename__ = 'geologische_tief_vernehm_pm_pt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/vernehm_planning_pt.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung'
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


class AreaPlanningNotMT6(Base, Vector):
    __tablename__ = 'geologische_tief_vernehm_pm_area_not_mt6'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/vernehm_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung'
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


class AreaPlanningMT6(Base, Vector):
    __tablename__ = 'geologische_tief_vernehm_pm_area_mt6'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/vernehm_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung'
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

register('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung', PtFacilities)
register('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung', PtPlanning)
register('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung', AreaPlanningNotMT6)
register('ch.bfe.sachplan-geologie-tiefenlager_vernehmlassung', AreaPlanningMT6)


class SgtFacilitiesTd(Base, Vector):
    __tablename__ = 'geologische_tiefenlager_fac'
    __table_args__ = ({'schema': 'bfe', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/sgt_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
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
    description = Column('description', Unicode)
    web = Column('web', Unicode)
    objname_text_de = Column('objname_text_de', Unicode)
    objname_text_fr = Column('objname_text_fr', Unicode)
    objname_text_it = Column('objname_text_it', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 80005
    __maxscale__ = 100000005
    the_geom = Column(Geometry2D)


class SgtPlanningTd(Base, Vector):
    __tablename__ = 'geologische_tiefenlager'
    __table_args__ = ({'schema': 'bfe', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    measurename_de = Column('measurename_de', Unicode)
    measurename_fr = Column('measurename_fr', Unicode)
    measurename_it = Column('measurename_it', Unicode)
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
    description = Column('description', Unicode)
    web = Column('web', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __minscale__ = 20005
    __maxscale__ = 500005
    the_geom = Column(Geometry2D)


class SgtPlanningRasterTd(Base, Vector):
    __tablename__ = 'geologische_tiefenlager_raster'
    __table_args__ = ({'schema': 'bfe', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/sgt_planning.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
    facname_de = Column('facname_de', Unicode)
    facname_fr = Column('facname_fr', Unicode)
    facname_it = Column('facname_it', Unicode)
    measurename_de = Column('measurename_de', Unicode)
    measurename_fr = Column('measurename_fr', Unicode)
    measurename_it = Column('measurename_it', Unicode)
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
    description = Column('description', Unicode)
    web = Column('web', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung', SgtFacilitiesTd)
register('ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung', SgtPlanningTd)
register('ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung', SgtPlanningRasterTd)


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
    chmobil_url_etappe = Column('bgdi_url_etappe', Unicode)
    chmobil_url_route = Column('bgdi_url_route', Unicode)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.veloland', ChmobilVeloland)


class ChmobilWanderland (Base, Vector):
    __tablename__ = 'chmobil_wanderland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.wanderland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_url_etappe = Column('bgdi_url_etappe', Unicode)
    chmobil_url_route = Column('bgdi_url_route', Unicode)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.wanderland', ChmobilWanderland)


class ChmobilSkatingland (Base, Vector):
    __tablename__ = 'chmobil_skatingland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.skatingland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_url_etappe = Column('bgdi_url_etappe', Unicode)
    chmobil_url_route = Column('bgdi_url_route', Unicode)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.skatingland', ChmobilSkatingland)


class ChmobilMountainbikeland (Base, Vector):
    __tablename__ = 'chmobil_mountainbikeland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.mountainbikeland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_url_etappe = Column('bgdi_url_etappe', Unicode)
    chmobil_url_route = Column('bgdi_url_route', Unicode)
    chmobil_title = Column('title', Unicode)
    chmobil_route_number = Column('route_number', Unicode)
    the_geom = Column(Geometry2D)

register('ch.astra.mountainbikeland', ChmobilMountainbikeland)


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
    arp_east = Column('arp_east', Float)
    arp_north = Column('arp_north', Float)
    elevation = Column('elevation', Float)
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
