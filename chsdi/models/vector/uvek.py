# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Unicode, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship, remote
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
    name = Column('name', Text)
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


class OevDepartures(Base):
    __tablename__ = 'oev_departures'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.departures-oev'
    __label__ = 'id'
    id = Column('oid', Text, primary_key=True)
    stop = Column('stop', Integer)
    time = Column('time', DateTime)
    label = Column('label', Text)
    type = Column('type', Integer)
    via = Column('via', Text)
    destination = Column('destination', Text,
                         ForeignKey(OevHaltestellenZoom1.name))
    haltestelle = relationship(OevHaltestellenZoom1,
                               primaryjoin=destination == remote(OevHaltestellenZoom1.name),
                               viewonly=True)


# IVS NAT and REG use the same template
class SicherheitsZonenPlan (Base, Vector):
    __tablename__ = 'sichereitszonen'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sicherheitszoneneplan.mako'
    __bodId__ = 'ch.bazl.sicherheitszonenplan'
    __extended_info__ = True
    __label__ = 'id'
    id = Column('stabil_id', Unicode, primary_key=True)
    zone = Column('zone', Text)
    zonetype_tid = Column('zonetype_tid', Text)
    type_id = Column('type_id', Text)
    zonetype_de = Column('zonetype_de', Text)
    zonetype_fr = Column('zonetype_fr', Text)
    zonetype_it = Column('zonetype_it', Text)
    zone_name = Column('zone_name', Text)
    originator = Column('originator', Text)
    canton = Column('canton', Text)
    municipality = Column('municipality', Text)
    approval_date = Column('approval_date', Text)
    status_id = Column('status_id', Text)
    legalstatus_tid = Column('legalstatus_tid', Text)
    legalstatus_de = Column('legalstatus_de', Text)
    legalstatus_fr = Column('legalstatus_fr', Text)
    legalstatus_it = Column('legalstatus_it', Text)
    title = Column('title', Text)
    weblink = Column('weblink', Text)
    valid_from = Column('valid_from', Text)
    valid_until = Column('valid_until', Text)
    latest_modification = Column('latest_modification', Text)
    doc_description = Column('doc_description', Text)
    doc_id = Column('doc_id', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.sicherheitszonenplan', SicherheitsZonenPlan)


class IVS_NAT(Base, Vector):
    __tablename__ = 'ivs_nat'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-nat'
    __queryable_attributes__ = ['ivs_slaname', 'ivs_nummer', 'ivs_signatur']
    __label__ = 'id'
    id = Column('nat_id', Integer, primary_key=True)
    ivs_slaname = Column('ivs_slaname', Text)
    ivs_nummer = Column('ivs_nummer', Text)
    ivs_signatur = Column('ivs_signatur', Text)
    ivs_signatur_fr = Column('ivs_signatur_fr', Text)
    ivs_signatur_it = Column('ivs_signatur_it', Text)
    ivs_signatur_de = Column('ivs_signatur_de', Text)
    ivs_kanton = Column('ivs_kanton', Text)
    ivs_sladatehist = Column('ivs_sladatehist', Integer)
    ivs_sladatemorph = Column('ivs_sladatemorph', Integer)
    ivs_slabedeutung = Column('ivs_slabedeutung', Integer)
    ivs_sortsla = Column('ivs_sortsla', Text)
    the_geom = Column(Geometry2D)

register('ch.astra.ivs-nat', IVS_NAT)
register('ch.astra.ivs-nat-verlaeufe', IVS_NAT)


class IVS_REG_LOC(Base, Vector):
    __tablename__ = 'ivs_reg_loc'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ivs_nat.mako'
    __bodId__ = 'ch.astra.ivs-reg_loc'
    __queryable_attributes__ = ['ivs_slaname', 'ivs_nummer', 'ivs_signatur']
    __label__ = 'ivs_nummer'
    id = Column('reg_loc_id', Integer, primary_key=True)
    ivs_slaname = Column('ivs_slaname', Text)
    ivs_nummer = Column('ivs_nummer', Text)
    ivs_signatur = Column('ivs_signatur', Text)
    ivs_signatur_fr = Column('ivs_signatur_fr', Text)
    ivs_signatur_it = Column('ivs_signatur_it', Text)
    ivs_signatur_de = Column('ivs_signatur_de', Text)
    ivs_kanton = Column('ivs_kanton', Text)
    ivs_sladatehist = Column('ivs_sladatehist', Integer)
    ivs_sladatemorph = Column('ivs_sladatemorph', Integer)
    ivs_slabedeutung = Column('ivs_slabedeutung', Integer)
    ivs_sortsla = Column('ivs_sortsla', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.astra.ivs-reg_loc', IVS_REG_LOC)


class AUSNAHMETRANSPORTROUTEN(Base, Vector):
    __tablename__ = 'ausnahmetransportrouten'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/ausnahmetransportrouten.mako'
    __bodId__ = 'ch.astra.ausnahmetransportrouten'
    __label__ = 'id'
    id = Column('id', Integer, primary_key=True)
    bgdi_id = Column('bgdi_id', Integer)
    ri_getrenn = Column('ri_getrenn', Text)
    anz_spuren = Column('anz_spuren', Integer)
    strassen_typ = Column('strassen_typ', Text)
    routentyp_id = Column('routentyp_id', Integer)
    the_geom = Column(Geometry2D)

register('ch.astra.ausnahmetransportrouten', AUSNAHMETRANSPORTROUTEN)


class ZAEHLSTELLENREGLOC(Base, Vector):
    __tablename__ = 'verkehr_reg_loc'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/verkehrszaehlstellen.mako'
    __bodId__ = 'ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal'
    __queryable_attributes__ = ['id', 'zaehlstellen_bezeichnung']
    __extended_info__ = True
    __label__ = 'zaehlstellen_bezeichnung'
    id = Column('nr', Integer, primary_key=True)
    zaehlstellen_bezeichnung = Column('zaehlstellen_bezeichnung', Text)
    uno_zaehlstelle = Column('uno_zaehlstelle', Text)
    zst_physisch_virtuell = Column('zst_physisch_virtuell', Text)
    messstellentyp = Column('messstellentyp', Text)
    koordinate_ost = Column('koordinate_ost', Integer)
    koordinate_nord = Column('koordinate_nord', Integer)
    kanton = Column('kanton', Text)
    swiss_10 = Column('swiss_10', Integer)
    netz = Column('netz', Text)
    status = Column('status', Text)
    strasse = Column('strasse', Text)
    richtung_1 = Column('richtung_1', Text)
    richtung_2 = Column('richtung_2', Text)
    inbetriebnahme = Column('inbetriebnahme', Text)
    anzahl_fahrstreifen_tot = Column('anzahl_fahrstreifen_tot', Integer)
    bulletins_sasvz = Column('bulletins_sasvz', Text)
    ssvz_2005 = Column('ssvz_2005', Text)
    jahresauswertung = Column('jahresauswertung', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.astra.strassenverkehrszaehlung_messstellen-regional_lokal', ZAEHLSTELLENREGLOC)


class ZAEHLSTELLENUEBER(Base, Vector):
    __tablename__ = 'verkehr_ueber'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/verkehrszaehlstellen.mako'
    __bodId__ = 'ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet'
    __queryable_attributes__ = ['id', 'zaehlstellen_bezeichnung']
    __extended_info__ = True
    __label__ = 'zaehlstellen_bezeichnung'
    id = Column('nr', Integer, primary_key=True)
    zaehlstellen_bezeichnung = Column('zaehlstellen_bezeichnung', Text)
    uno_zaehlstelle = Column('uno_zaehlstelle', Text)
    zst_physisch_virtuell = Column('zst_physisch_virtuell', Text)
    messstellentyp = Column('messstellentyp', Text)
    koordinate_ost = Column('koordinate_ost', Integer)
    koordinate_nord = Column('koordinate_nord', Integer)
    kanton = Column('kanton', Text)
    swiss_10 = Column('swiss_10', Integer)
    netz = Column('netz', Text)
    status = Column('status', Text)
    strasse = Column('strasse', Text)
    richtung_1 = Column('richtung_1', Text)
    richtung_2 = Column('richtung_2', Text)
    inbetriebnahme = Column('inbetriebnahme', Text)
    anzahl_fahrstreifen_tot = Column('anzahl_fahrstreifen_tot', Integer)
    bulletins_sasvz = Column('bulletins_sasvz', Text)
    ssvz_2005 = Column('ssvz_2005', Text)
    jahresauswertung = Column('jahresauswertung', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.astra.strassenverkehrszaehlung_messstellen-uebergeordnet', ZAEHLSTELLENUEBER)


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
    accidenttype_de = Column('accidenttype_de', Text)
    accidenttype_fr = Column('accidenttype_fr', Text)
    accidenttype_it = Column('accidenttype_it', Text)
    accidenttypecode = Column('accidenttypecode', Integer)
    accidentday_de = Column('accidentday_de', Text)
    accidentday_fr = Column('accidentday_fr', Text)
    accidentday_it = Column('accidentday_it', Text)
    accidentyear = Column('accidentyear', Integer)
    severitycategory_de = Column('severitycategory_de', Text)
    severitycategory_fr = Column('severitycategory_fr', Text)
    severitycategory_it = Column('severitycategory_it', Text)
    severitycategorycode = Column('severitycategorycode', Text)
    roadtype_de = Column('roadtype_de', Text)
    roadtype_fr = Column('roadtype_fr', Text)
    roadtype_it = Column('roadtype_it', Text)
    roadtypecode = Column('roadtypecode', Integer)
    canton = Column('canton', Text)
    fsocommunecode = Column('fsocommunecode', Text)
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
    canton = Column('canton', Text)
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


class KATASTERBELASTETERSTANDORTE(Base, Vector):
    __tablename__ = 'kataster_belasteter_standorte_oev'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/kataster_belasteter_standorte_oev.mako'
    __bodId__ = 'ch.bav.kataster-belasteter-standorte-oev'
    __queryable_attributes__ = ['katasternummer']
    __label__ = 'id'
    id = Column('vflz_id', Integer, primary_key=True)
    katasternummer = Column('katasternummer', Text)
    standorttyp_de = Column('standorttyp_de', Text)
    standorttyp_fr = Column('standorttyp_fr', Text)
    standorttyp_it = Column('standorttyp_it', Text)
    statusaltlv_de = Column('statusaltlv_de', Text)
    statusaltlv_fr = Column('statusaltlv_fr', Text)
    statusaltlv_it = Column('statusaltlv_it', Text)
    untersuchungsstand_de = Column('untersuchungsstand_de', Text)
    untersuchungsstand_fr = Column('untersuchungsstand_fr', Text)
    untersuchungsstand_it = Column('untersuchungsstand_it', Text)
    url = Column('url', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.bav.kataster-belasteter-standorte-oev', KATASTERBELASTETERSTANDORTE)


class ABGELTUNGWASSERKRAFTNUTZUNG(Base, Vector):
    __tablename__ = 'abgeltung_wasserkraftnutzung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/abgeltungwasserkraftnutzung.mako'
    __bodId__ = 'ch.bfe.abgeltung-wasserkraftnutzung'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('objectnumber', Integer, primary_key=True)
    area = Column('area', Numeric)
    name = Column('name', Text)
    perimeter = Column('perimeter', Numeric)
    startprotectioncommitment = Column('startprotectioncommitment', Text)
    endprotectioncommitment = Column('endprotectioncommitment', Text)
    the_geom = Column(Geometry2D)

register('ch.bfe.abgeltung-wasserkraftnutzung', ABGELTUNGWASSERKRAFTNUTZUNG)


class ENERGIESTAEDTE(Base, Vector):
    __tablename__ = 'energiestaedte'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte.mako'
    __bodId__ = 'ch.bfe.energiestaedte'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    bfsnr = Column('bfsnr', Integer)
    punktezahl = Column('punktezahl', Numeric)
    einwohner = Column('einwohner', Numeric)
    energiestadtseit = Column('energiestadtseit', Text)
    beteiligtegemeinde = Column('beteiligtegemeinde', Text)
    anzahlaudits = Column('anzahlaudits', Numeric)
    berater = Column('berater', Text)
    linkberater = Column('linkberater', Text)
    linkfaktenblatt = Column('linkfaktenblatt', Text)
    linkenergiestadtweb = Column('linkenergiestadtweb', Text)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte', ENERGIESTAEDTE)


class ENERGIESTAEDTEREGIONEN(Base, Vector):
    __tablename__ = 'energiestaedte_energieregionen'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte_energieregionen.mako'
    __bodId__ = 'ch.bfe.energiestaedte-energieregionen'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    kategorie = Column('kategorie', Text)
    bet_energiestaedte = Column('bet_energiestaedte', Text)
    bet_traegerverein = Column('bet_traegerverein', Text)
    berater = Column('berater', Text)
    linkberater = Column('linkberater', Text)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte-energieregionen', ENERGIESTAEDTEREGIONEN)


class ENERGIESTAEDTE2000WATTAREALE(Base, Vector):
    __tablename__ = 'energiestaedte_2000watt_areale'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte_2000watt_areale.mako'
    __bodId__ = 'ch.bfe.energiestaedte-2000watt-areale'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    kategorie = Column('kategorie', Text)
    gemeinde = Column('gemeinde', Text)
    berater = Column('berater', Text)
    linkberater = Column('linkberater', Text)
    linkfaktenblatt_de = Column('linkfaktenblatt_de', Text)
    linkfaktenblatt_fr = Column('linkfaktenblatt_fr', Text)
    linkfaktenblatt_it = Column('linkfaktenblatt_it', Text)
    linkfaktenblatt_en = Column('linkfaktenblatt_en', Text)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte-2000watt-areale', ENERGIESTAEDTE2000WATTAREALE)


class ENERGIESTAEDTE2000AUFDEMWEG(Base, Vector):
    __tablename__ = 'energiestaedte_aufdemweg_2000watt'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energiestaedte_2000watt_auf_dem_weg.mako'
    __bodId__ = 'ch.bfe.energiestaedte-2000watt-aufdemweg'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    kategorie = Column('kategorie', Text)
    berater = Column('berater', Text)
    linkberater = Column('linkberater', Text)
    linkfaktenblatt = Column('linkfaktenblatt', Text)
    the_geom = Column(Geometry2D)

register('ch.bfe.energiestaedte-2000watt-aufdemweg', ENERGIESTAEDTE2000AUFDEMWEG)


class ENERGIEFORSCHUNG(Base, Vector):
    __tablename__ = 'energieforschung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/energieforschung.mako'
    __bodId__ = 'ch.bfe.energieforschung'
    __extended_info__ = True
    __queryable_attributes__ = ['projektnummer', 'titel']
    __label__ = 'titel'
    id = Column('bgdi_id', Integer, primary_key=True)
    titel = Column('titel', Text)
    leuchtturm = Column('leuchtturm', Integer)
    beschreibung = Column('beschreibung', Text)
    projektstatus_fr = Column('projektstatus_fr', Text)
    projektstatus_de = Column('projektstatus_de', Text)
    projektstatus_it = Column('projektstatus_it', Text)
    projektstatus_en = Column('projektstatus_en', Text)
    projektnummer = Column('projektnummer', Text)
    projektbeginn = Column('projektbeginn', Text)
    projektende = Column('projektende', Text)
    oberthema_fr = Column('oberthema_fr', Text)
    oberthema_de = Column('oberthema_de', Text)
    oberthema_it = Column('oberthema_it', Text)
    oberthema_en = Column('oberthema_en', Text)
    unterthema_fr = Column('unterthema_fr', Text)
    unterthema_de = Column('unterthema_de', Text)
    unterthema_it = Column('unterthema_it', Text)
    unterthema_en = Column('unterthema_en', Text)
    bericht = Column('bericht', Text)
    fachartikel = Column('fachartikel', Text)
    infoclip = Column('infoclip', Text)
    projektpartner = Column('projektpartner', Text)
    kontakt = Column('kontakt', Text)
    plz = Column('plz', Text)
    ort = Column('ort', Text)
    kanton = Column('kanton', Text)
    bild0 = Column('bild0', Text)
    bild1 = Column('bild1', Text)
    bild2 = Column('bild2', Text)
    the_geom = Column(Geometry2D)

register('ch.bfe.energieforschung', ENERGIEFORSCHUNG)


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


class STATISTIKWASSERKRAFTANLAGEN(Base, Vector):
    __tablename__ = 'statistik_wasserkraftanlagen_powerplant'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/statistikwasserkraftanlagen.mako'
    __bodId__ = 'ch.bfe.statistik-wasserkraftanlagen'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('wastanumber', Integer, primary_key=True)
    name = Column('name', Text)
    location = Column('location', Text)
    canton = Column('canton', Text)
    hydropowerplantoperationalstatus_it = Column('hydropowerplantoperationalstatus_it', Text)
    hydropowerplanttype_it = Column('hydropowerplanttype_it', Text)
    hydropowerplantoperationalstatus_fr = Column('hydropowerplantoperationalstatus_fr', Text)
    hydropowerplanttype_fr = Column('hydropowerplanttype_fr', Text)
    hydropowerplantoperationalstatus_de = Column('hydropowerplantoperationalstatus_de', Text)
    hydropowerplanttype_de = Column('hydropowerplanttype_de', Text)
    beginningofoperation = Column('beginningofoperation', Integer)
    endofoperation = Column('endofoperation', Integer)
    leistung = Column('leistung', Numeric)
    produktionserwartung = Column('produktionserwartung', Numeric)
    leistungsaufnahme_pumpen = Column('leistungsaufnahme_pumpen', Numeric)
    energiebedarf_motore = Column('energiebedarf_motore', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bfe.statistik-wasserkraftanlagen', STATISTIKWASSERKRAFTANLAGEN)


class STAUANLAGENBUNDESAUFSICHT(Base, Vector):
    __tablename__ = 'stauanlagen_bundesaufsicht'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/stauanlagenbundesaufsicht.mako'
    __bodId__ = 'ch.bfe.stauanlagen-bundesaufsicht'
    __extended_info__ = True
    __queryable_attributes__ = ['damname', 'damtype_de', 'damtype_fr', 'damtype_en']
    __label__ = 'damname'
    id = Column('dam_stabil_id', Integer, primary_key=True)
    damname = Column('damname', Text)
    damtype_fr = Column('damtype_fr', Text)
    damtype_en = Column('damtype_en', Text)
    damtype_de = Column('damtype_de', Text)
    damheight = Column('damheight', Integer)
    crestlevel = Column('crestlevel', Integer)
    crestlength = Column('crestlength', Integer)
    facilityname = Column('facilityname', Text)
    beginningofoperation = Column('beginningofoperation', Text)
    startsupervision = Column('startsupervision', Text)
    reservoirname = Column('reservoirname', Text)
    impoundmentvolume = Column('impoundmentvolume', Text)
    impoundmentlevel = Column('impoundmentlevel', Integer)
    storagelevel = Column('storagelevel', Integer)
    facaim_fr = Column('facaim_fr', Text)
    facaim_en = Column('facaim_en', Text)
    facaim_de = Column('facaim_de', Text)
    has_picture = Column('has_picture', Integer)
    baujahr = Column('baujahr', Integer)
    facility_stabil_id = Column('facility_stabil_id', Integer)
    the_geom = Column(Geometry2D)

register('ch.bfe.stauanlagen-bundesaufsicht', STAUANLAGENBUNDESAUFSICHT)


class Kleinwasserkraftpotentiale(Base, Vector):
    __tablename__ = 'kleinwasserkraftpotentiale'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/kleinwasserkraftpotentiale.mako'
    __bodId__ = 'ch.bfe.kleinwasserkraftpotentiale'
    __label__ = 'gwlnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    kwprometer = Column('kwprometer', Numeric)
    laenge = Column('laenge', Numeric)
    gwlnr = Column('gwlnr', Text)
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
    fac_name = Column('fac_name', Text)
    fac_type_de = Column('fac_type_de', Text)
    fac_type_fr = Column('fac_type_fr', Text)
    fac_type_it = Column('fac_type_it', Text)
    fac_operator = Column('fac_operator', Text)
    fac_website = Column('fac_website', Text)
    fac_power = Column('fac_power', Text)
    fac_xml_prod = Column('fac_xml_prod', Text)
    fac_initial = Column('fac_initial', Text)
    fac_y = Column('fac_y', Integer)
    fac_x = Column('fac_x', Integer)
    turbines = Column('turbines', Text)
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
    fac_name = Column('fac_name', Text)
    fac_type_de = Column('fac_type_de', Text)
    fac_type_fr = Column('fac_type_fr', Text)
    fac_type_it = Column('fac_type_it', Text)
    fac_operator = Column('fac_operator', Text)
    fac_website = Column('fac_website', Text)
    fac_power = Column('fac_power', Text)
    fac_xml_prod = Column('fac_xml_prod', Text)
    fac_initial = Column('fac_initial', Text)
    tur_y = Column('tur_y', Integer)
    tur_x = Column('tur_x', Integer)
    turbines = Column('turbines', Text)
    tur_manufacturer = Column('tur_manufacturer', Text)
    tur_model = Column('tur_model', Text)
    tur_diameter = Column('tur_diameter', Text)
    tur_hubheight = Column('tur_hubheight', Text)
    tur_power = Column('tur_power', Text)
    tur_altitude = Column('tur_altitude', Text)
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
    name = Column('name', Text)
    code = Column('code', Text)
    power = Column('power', Text)
    service = Column('service', Text)
    program = Column('program', Text)
    freqchan = Column('freqchan', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.bakom.radio-fernsehsender', Bakomfernsehsender)


class Bakomgsm(Base, Vector):
    __tablename__ = 'nisdb_gsm'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomgsm.mako'
    __bodId__ = 'ch.bakom.mobil-antennenstandorte-gsm'
    __label__ = 'powercode'
    id = Column('id', Integer, primary_key=True)
    powercode = Column('powercode', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.bakom.mobil-antennenstandorte-gsm', Bakomgsm)


class Bakomumts(Base, Vector):
    __tablename__ = 'nisdb_umts'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomumts.mako'
    __bodId__ = 'ch.bakom.mobil-antennenstandorte-umts'
    __label__ = 'powercode'
    id = Column('id', Integer, primary_key=True)
    powercode = Column('powercode', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.bakom.mobil-antennenstandorte-umts', Bakomumts)


class Bakomlte(Base, Vector):
    __tablename__ = 'nisdb_lte'
    __table_args__ = ({'schema': 'bakom', 'autoload': False})
    __template__ = 'templates/htmlpopup/bakomlte.mako'
    __bodId__ = 'ch.bakom.mobil-antennenstandorte-lte'
    __label__ = 'powercode'
    id = Column('id', Integer, primary_key=True)
    powercode = Column('powercode', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    prog = Column('prog', Text)
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
    prog = Column('prog', Text)
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
    zonekind_text_de = Column('zonekind_text_de', Text)
    zonekind_text_fr = Column('zonekind_text_fr', Text)
    zonekind_text_it = Column('zonekind_text_it', Text)
    canton = Column('canton', Text)
    municipality = Column('municipality', Text)
    legalstatus_text_de = Column('legalstatus_text_de', Text)
    legalstatus_text_fr = Column('legalstatus_text_fr', Text)
    legalstatus_text_it = Column('legalstatus_text_it', Text)
    applicant = Column('applicant', Text)
    validfrom = Column('validfrom', Text)
    durationofeffect = Column('durationofeffect', Text)
    description = Column('description', Text)
    weblink_origin = Column('weblink_origin', Text)
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
    sanctiontext = Column('sanctiontext', Text)
    registrationnumber = Column('registrationnumber', Text)
    lk100 = Column('lk100', Text)
    obstacletype = Column('obstacletype', Text)
    state = Column('state', Text)
    maxheightagl = Column('maxheightagl', Integer)
    topelevationamsl = Column('topelevationamsl', Integer)
    totallength = Column('totallength', Integer)
    startofconstruction = Column('startofconstruction', Date)
    duration = Column('duration', Text)
    geomtype = Column('geomtype', Text)
    abortionaccomplished = Column('abortionaccomplished', Date)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.luftfahrthindernis', Luftfahrthindernis)


class SgtFacilities(Base, Vector):
    __tablename__ = 'geologische_tiefenlager_fac'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __template__ = 'templates/htmlpopup/sgt_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description = Column('description', Text)
    web = Column('web', Text)
    objname_text_de = Column('objname_text_de', Text)
    objname_text_fr = Column('objname_text_fr', Text)
    objname_text_it = Column('objname_text_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    facname_de = Column('facname_de', Text)
    measurename_de = Column('measurename_de', Text)
    measurename_fr = Column('measurename_fr', Text)
    measurename_it = Column('measurename_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description = Column('description', Text)
    web = Column('web', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    measurename_de = Column('measurename_de', Text)
    measurename_fr = Column('measurename_fr', Text)
    measurename_it = Column('measurename_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description = Column('description', Text)
    web = Column('web', Text)
    bgdi_created = Column('bgdi_created', Text)
    __maxscale__ = 20005
    __minscale__ = 1
    the_geom = Column(Geometry2D)

register('ch.bfe.sachplan-geologie-tiefenlager', SgtFacilities)
register('ch.bfe.sachplan-geologie-tiefenlager', SgtPlanning)
register('ch.bfe.sachplan-geologie-tiefenlager', SgtPlanningRaster)


class SgtFacilitiesTd(Base, Vector):
    __tablename__ = 'geologische_tiefenlager_fac'
    __table_args__ = ({'schema': 'bfe', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/sgt_facilities.mako'
    __bodId__ = 'ch.bfe.sachplan-geologie-tiefenlager-thematische-darstellung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Integer, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description = Column('description', Text)
    web = Column('web', Text)
    objname_text_de = Column('objname_text_de', Text)
    objname_text_fr = Column('objname_text_fr', Text)
    objname_text_it = Column('objname_text_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    measurename_de = Column('measurename_de', Text)
    measurename_fr = Column('measurename_fr', Text)
    measurename_it = Column('measurename_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description = Column('description', Text)
    web = Column('web', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    measurename_de = Column('measurename_de', Text)
    measurename_fr = Column('measurename_fr', Text)
    measurename_it = Column('measurename_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description = Column('description', Text)
    web = Column('web', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_text_de = Column('description_text_de', Text)
    description_text_fr = Column('description_text_fr', Text)
    description_text_it = Column('description_text_it', Text)
    document_web = Column('document_web', Text)
    objectname_de = Column('objectname_de', Text)
    objectname_fr = Column('objectname_fr', Text)
    objectname_it = Column('objectname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)


class SilPlanningA(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_plmeasures_anhorung'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_planning.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_anhorung'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_text_de = Column('description_text_de', Text)
    description_text_fr = Column('description_text_fr', Text)
    description_text_it = Column('description_text_it', Text)
    document_web = Column('document_web', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_text_de = Column('description_text_de', Text)
    description_text_fr = Column('description_text_fr', Text)
    description_text_it = Column('description_text_it', Text)
    document_web = Column('document_web', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_text_de = Column('description_text_de', Text)
    description_text_fr = Column('description_text_fr', Text)
    description_text_it = Column('description_text_it', Text)
    document_web = Column('document_web', Text)
    objectname_de = Column('objectname_de', Text)
    objectname_fr = Column('objectname_fr', Text)
    objectname_it = Column('objectname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)


class SilPlanningK(Base, Vector):
    __tablename__ = 'sachplan_inf_luft_plmeasures_kraft'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/sil_planning.mako'
    __bodId__ = 'ch.bazl.sachplan-infrastruktur-luftfahrt_kraft'
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Unicode, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_text_de = Column('description_text_de', Text)
    description_text_fr = Column('description_text_fr', Text)
    description_text_it = Column('description_text_it', Text)
    document_web = Column('document_web', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    measuretype_text_de = Column('measuretype_text_de', Text)
    measuretype_text_fr = Column('measuretype_text_fr', Text)
    measuretype_text_it = Column('measuretype_text_it', Text)
    coordinationlevel_text_de = Column('coordinationlevel_text_de', Text)
    coordinationlevel_text_fr = Column('coordinationlevel_text_fr', Text)
    coordinationlevel_text_it = Column('coordinationlevel_text_it', Text)
    planningstatus_text_de = Column('planningstatus_text_de', Text)
    planningstatus_text_fr = Column('planningstatus_text_fr', Text)
    planningstatus_text_it = Column('planningstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_text_de = Column('description_text_de', Text)
    description_text_fr = Column('description_text_fr', Text)
    description_text_it = Column('description_text_it', Text)
    document_web = Column('document_web', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    alias = Column('alias', Text)
    fdaurl = Column('fdaurl', Text)
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
    name = Column('name', Text)
    operator = Column('operator', Text)
    owner = Column('owner', Text)
    enforcement_1 = Column('enforcement_1', Text)
    enforcement_2 = Column('enforcement_2', Text)
    enforcement_3 = Column('enforcement_3', Text)
    regulatory = Column('regulatory', Text)
    license_de = Column('license_de', Text)
    license_fr = Column('license_fr', Text)
    license_it = Column('license_it', Text)
    license_en = Column('license_en', Text)
    municipality = Column('municipality', Text)
    canton = Column('canton', Text)
    reactor_name = Column('reactor_name', Text)
    reactors = Column('reactors', Integer)
    life_phase_de = Column('life_phase_de', Text)
    life_phase_fr = Column('life_phase_fr', Text)
    life_phase_it = Column('life_phase_it', Text)
    life_phase_en = Column('life_phase_en', Text)
    reactor_type_de = Column('reactor_type_de', Text)
    reactor_type_fr = Column('reactor_type_fr', Text)
    reactor_type_it = Column('reactor_type_it', Text)
    reactor_type_en = Column('reactor_type_en', Text)
    cooling_type_de = Column('cooling_type_de', Text)
    cooling_type_fr = Column('cooling_type_fr', Text)
    cooling_type_it = Column('cooling_type_it', Text)
    cooling_type_en = Column('cooling_type_en', Text)
    nominal_thermal_output = Column('nominal_thermal_output', Text)
    gross_el_output = Column('gross_el_output', Text)
    net_el_output = Column('net_el_output', Text)
    construction_phase = Column('construction_phase', Text)
    commissioning_phase = Column('commissioning_phase', Text)
    operation_phase = Column('operation_phase', Text)
    decontamination_phase = Column('decontamination_phase', Text)
    dismantling_phase = Column('dismantling_phase', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    name = Column('name', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    valid_from = Column('valid_from', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    katasternummer = Column('katasternummer', Text)
    standorttyp_de = Column('standorttyp_de', Text)
    standorttyp_fr = Column('standorttyp_fr', Text)
    standorttyp_it = Column('standorttyp_it', Text)
    statusaltlv_de = Column('statusaltlv_de', Text)
    statusaltlv_fr = Column('statusaltlv_fr', Text)
    statusaltlv_it = Column('statusaltlv_it', Text)
    untersuchungsstand_de = Column('untersuchungsstand_de', Text)
    untersuchungsstand_fr = Column('untersuchungsstand_fr', Text)
    untersuchungsstand_it = Column('untersuchungsstand_it', Text)
    url = Column('url', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.kataster-belasteter-standorte-zivilflugplaetze', KbsZivilflugpl)


class LaermEmissionsplanEisenbahnTag(Base, Vector):
    __tablename__ = 'laerm_emissionsplan_eisenbahn_tag'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/laerm_emissionsplan_eisenbahn_tag.mako'
    __bodId__ = 'ch.bav.laerm-emissionsplan_eisenbahn_tag'
    # Composite labels (bgdi_id::text ||' '||linienbez)
    __label__ = 'linienbeze'
    id = Column('bgdi_id', Integer, primary_key=True)
    lin_nr_dfa = Column('lin_nr_dfa', Numeric)
    linienbeze = Column('linienbeze', Text)
    von_abkz = Column('von_abkz', Text)
    von_bpk_bp = Column('von_bpk_bp', Text)
    bis_abkz = Column('bis_abkz', Text)
    bis_bpk_bp = Column('bis_bpk_bp', Text)
    von_m = Column('von_m', Numeric)
    bis_m = Column('bis_m', Numeric)
    lre_t = Column('lre_t', Numeric)
    k1_t = Column('k1_t', Numeric)
    fb1 = Column('fb1', Numeric)
    grund1 = Column('grund1', Text)
    fb2 = Column('fb2', Numeric)
    grund2 = Column('grund2', Text)
    typ_aender = Column('typ_aender', Text)
    datum = Column('datum', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bav.laerm-emissionsplan_eisenbahn_tag', LaermEmissionsplanEisenbahnTag)


class LaermEmissionsplanEisenbahnNacht(Base, Vector):
    __tablename__ = 'laerm_emissionsplan_eisenbahn_nacht'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __template__ = 'templates/htmlpopup/laerm_emissionsplan_eisenbahn_nacht.mako'
    __bodId__ = 'ch.bav.laerm-emissionsplan_eisenbahn_nacht'
    # Composite labels (bgdi_id::text ||' '||linienbez)
    __label__ = 'linienbeze'
    id = Column('bgdi_id', Integer, primary_key=True)
    lin_nr_dfa = Column('lin_nr_dfa', Numeric)
    linienbeze = Column('linienbeze', Text)
    von_abkz = Column('von_abkz', Text)
    von_bpk_bp = Column('von_bpk_bp', Text)
    bis_abkz = Column('bis_abkz', Text)
    bis_bpk_bp = Column('bis_bpk_bp', Text)
    von_m = Column('von_m', Numeric)
    bis_m = Column('bis_m', Numeric)
    lre_n = Column('lre_n', Numeric)
    k1_n = Column('k1_n', Numeric)
    fb1 = Column('fb1', Numeric)
    grund1 = Column('grund1', Text)
    fb2 = Column('fb2', Numeric)
    grund2 = Column('grund2', Text)
    typ_aender = Column('typ_aender', Text)
    datum = Column('datum', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bav.laerm-emissionsplan_eisenbahn_nacht', LaermEmissionsplanEisenbahnNacht)


class SifFacilitiesA(Base, Vector):
    __tablename__ = 'sif_fac_anhorung'
    __table_args__ = ({'schema': 'bav', 'autoload': False})
    __bodId__ = 'ch.bav.sachplan-infrastruktur-schifffahrt_anhoerung'
    __template__ = 'templates/htmlpopup/sif_facilities.mako'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it', 'doc_title']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    name = Column('name', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    facstatus = Column('facstatus', Text)
    fackind = Column('fackind', Text)
    valid_from = Column('valid_from', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.bav.sachplan-infrastruktur-schifffahrt_ausgangslage', SifAusgangslage)


class BazlLaermErsteNachtstunde(Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_erste_nachtstunde'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_erste-nachtstunde', BazlLaermErsteNachtstunde)


class bazl_laerm_helikopter_maximalpegel (Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_helikopter_maxpegel'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter-maximalpegel', bazl_laerm_helikopter_maximalpegel)


class bazl_laerm_helikopter (Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_helikopter'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_helikopter', bazl_laerm_helikopter)


class bazl_laerm_klein_grossflugzeuge (Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_klein_grossflugzeuge'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_klein-grossflugzeuge', bazl_laerm_klein_grossflugzeuge)


class bazl_laerm_kleinluftfahrzeuge (Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_kleinluftfahrzeuge'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_kleinluftfahrzeuge', bazl_laerm_kleinluftfahrzeuge)


class bazl_laerm_letzte_nachtstunde (Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_letzte_nachtstunde'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_letzte-nachtstunde', bazl_laerm_letzte_nachtstunde)


class bazl_laerm_militaer_gesamt (Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_militaer_gesamt'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_militaer-gesamt', bazl_laerm_militaer_gesamt)


class bazl_laerm_zweite_nachtstunde (Base, Vector):
    __tablename__ = 'laermbelastungskataster_zivilflugplaetze_zweite_nachtstunde'
    __table_args__ = ({'schema': 'bazl', 'autoload': False})
    __template__ = 'templates/htmlpopup/bazl_laerm.mako'
    __bodId__ = 'ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde'
    __label__ = 'exposurecurve_level_db'
    id = Column('bgdi_id', Integer, primary_key=True)
    noisepollutionregister_registername = Column('noisepollutionregister_registername', Text)
    noisepollutionregister_editor = Column('noisepollutionregister_editor', Text)
    noisepollutionregister_validity_validfrom = Column('bgdi_validfrom', Text)
    exposuregroup_exposuretype = Column('exposuregroup_exposuretype', Text)
    exposurecurve_level_db = Column('exposurecurve_level_db', Text)
    noisepollutionregister_documentlink = Column('noisepollutionregister_documentlink', Text)
    the_geom = Column(Geometry2D)

register('ch.bazl.laermbelastungskataster-zivilflugplaetze_zweite-nachtstunde', bazl_laerm_zweite_nachtstunde)


class SuelFacAnhorung(Base, Vector):
    __tablename__ = 'suel_fac_anhorung'
    __table_args__ = ({'schema': 'bfe', 'autoload': False})
    __bodId__ = 'ch.bfe.sachplan-uebertragungsleitungen_anhoerung'
    __template__ = 'templates/htmlpopup/suel_facilities.mako'
    __queryable_attributes__ = ['facname_de', 'facname_fr', 'facname_it']
    # Translatable labels in fr, it
    __label__ = 'facname_de'
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    id = Column('stabil_id', Text, primary_key=True)
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    fackind_text_de = Column('fackind_text_de', Text)
    fackind_text_fr = Column('fackind_text_fr', Text)
    fackind_text_it = Column('fackind_text_it', Text)
    facstatus_text_de = Column('facstatus_text_de', Text)
    facstatus_text_fr = Column('facstatus_text_fr', Text)
    facstatus_text_it = Column('facstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    objname_de = Column('objname_de', Text)
    objname_fr = Column('objname_fr', Text)
    objname_it = Column('objname_it', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    facname_de = Column('facname_de', Text)
    facname_fr = Column('facname_fr', Text)
    facname_it = Column('facname_it', Text)
    plname_de = Column('plname_de', Text)
    plname_fr = Column('plname_fr', Text)
    plname_it = Column('plname_it', Text)
    meastype_text_de = Column('meastype_text_de', Text)
    meastype_text_fr = Column('meastype_text_fr', Text)
    meastype_text_it = Column('meastype_text_it', Text)
    coordlevel_text_de = Column('coordlevel_text_de', Text)
    coordlevel_text_fr = Column('coordlevel_text_fr', Text)
    coordlevel_text_it = Column('coordlevel_text_it', Text)
    plstatus_text_de = Column('plstatus_text_de', Text)
    plstatus_text_fr = Column('plstatus_text_fr', Text)
    plstatus_text_it = Column('plstatus_text_it', Text)
    validfrom = Column('validfrom', Text)
    validuntil = Column('validuntil', Text)
    description_de = Column('description_de', Text)
    description_fr = Column('description_fr', Text)
    description_it = Column('description_it', Text)
    doc_web = Column('doc_web', Text)
    doc_title = Column('doc_title', Text)
    bgdi_created = Column('bgdi_created', Text)
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
    chmobil_url_etappe = Column('bgdi_url_etappe', Text)
    chmobil_url_route = Column('bgdi_url_route', Text)
    chmobil_title = Column('title', Text)
    chmobil_route_number = Column('route_number', Text)
    the_geom = Column(Geometry2D)

register('ch.astra.veloland', ChmobilVeloland)


class ChmobilWanderland (Base, Vector):
    __tablename__ = 'chmobil_wanderland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.wanderland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_url_etappe = Column('bgdi_url_etappe', Text)
    chmobil_url_route = Column('bgdi_url_route', Text)
    chmobil_title = Column('title', Text)
    chmobil_route_number = Column('route_number', Text)
    the_geom = Column(Geometry2D)

register('ch.astra.wanderland', ChmobilWanderland)


class ChmobilSkatingland (Base, Vector):
    __tablename__ = 'chmobil_skatingland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.skatingland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_url_etappe = Column('bgdi_url_etappe', Text)
    chmobil_url_route = Column('bgdi_url_route', Text)
    chmobil_title = Column('title', Text)
    chmobil_route_number = Column('route_number', Text)
    the_geom = Column(Geometry2D)

register('ch.astra.skatingland', ChmobilSkatingland)


class ChmobilMountainbikeland (Base, Vector):
    __tablename__ = 'chmobil_mountainbikeland'
    __table_args__ = ({'schema': 'astra', 'autoload': False})
    __template__ = 'templates/htmlpopup/chmobil.mako'
    __bodId__ = 'ch.astra.mountainbikeland'
    __label__ = 'chmobil_title'
    id = Column('full_number', Unicode, primary_key=True)
    chmobil_url_etappe = Column('bgdi_url_etappe', Text)
    chmobil_url_route = Column('bgdi_url_route', Text)
    chmobil_title = Column('title', Text)
    chmobil_route_number = Column('route_number', Text)
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

register('ch.bazl.spitallandeplaetze', Spitallandeplaetze)
