from sqlalchemy import Column, Integer
from sqlalchemy.types import Float, Unicode

from chsdi.models import register, bases
from chsdi.models.vector import Vector, Geometry2D, Geometry3D


Base = bases['are']


class Landschaftstypen(Base, Vector):
    __tablename__ = 'landschaftstypen'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/landschaftstypen.mako'
    __bodId__ = 'ch.are.landschaftstypen'
    __label__ = 'typ_nr'
    id = Column('object', Unicode, primary_key=True)
    typ_nr = Column('typ_nr', Integer)
    typname_de = Column('typname_de', Unicode)
    typname_fr = Column('typname_fr', Unicode)
    regname_de = Column('regname_de', Unicode)
    regname_fr = Column('regname_fr', Unicode)
    object_are = Column('object_are', Float)
    typ_area = Column('typ_area', Float)
    stand = Column('stand', Unicode)
    the_geom = Column(Geometry2D)

register(Landschaftstypen.__bodId__, Landschaftstypen)


class Alpenkonvention(Base, Vector):
    __tablename__ = 'alpenkonvention'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/alpenkonvention.mako'
    __bodId__ = 'ch.are.alpenkonvention'
    __label__ = 'stand'
    id = Column('row_id', Integer, primary_key=True)
    flaeche_ha = Column('flaeche_ha', Float)
    stand = Column('stand', Float)
    the_geom = Column(Geometry3D)

register(Alpenkonvention.__bodId__, Alpenkonvention)


class Agglomerationsverkehr(Base, Vector):
    __tablename__ = 'agglomerationsverkehr'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/agglomerationsverkehr.mako'
    __bodId__ = 'ch.are.agglomerationsverkehr'
    __label__ = 'name'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode)
    gem_no = Column('gem_no', Integer)
    agglo_no = Column('agglo_no', Integer)
    agglo_name = Column('agglo_name', Unicode)
    land = Column('land', Unicode)
    the_geom = Column(Geometry2D)

register(Agglomerationsverkehr.__bodId__, Agglomerationsverkehr)


class GueteklasseOev(Base, Vector):
    __tablename__ = 'gueteklassen'
    __table_args__ = ({'schema': 'oeffentlicher_verkehr', 'autoload': False})
    __template__ = 'templates/htmlpopup/gueteklasseoev.mako'
    __bodId__ = 'ch.are.gueteklassen_oev'
    __label__ = 'klasse_fr'
    id = Column('id', Integer, primary_key=True)
    klasse_de = Column('klasse_de', Unicode)
    klasse_fr = Column('klasse_fr', Unicode)
    the_geom = Column(Geometry2D)

register(GueteklasseOev.__bodId__, GueteklasseOev)


class Bauzonen(Base, Vector):
    __tablename__ = 'bauzonen'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/bauzonen.mako'
    __bodId__ = 'ch.are.bauzonen'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    ch_code_hn = Column('ch_code_hn', Unicode)
    kt_kz = Column('kt_kz', Unicode)
    bfs_no = Column('bfs_no', Unicode)
    kt_no = Column('kt_no', Unicode)
    flaeche = Column('flaeche', Float)
    ch_bez_f = Column('ch_bez_f', Unicode)
    ch_bez_d = Column('ch_bez_d', Unicode)
    the_geom = Column(Geometry2D)

register(Bauzonen.__bodId__, Bauzonen)


class Gemeindetyp(Base, Vector):
    __tablename__ = 'gemeindetyp_1990_9klassen'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/gemeindetyp.mako'
    __bodId__ = 'ch.are.gemeindetyp-1990-9klassen'
    __label__ = 'name'
    id = Column('gde_no', Integer, primary_key=True)
    name = Column('name', Unicode)
    nom = Column('nom', Unicode)
    the_geom = Column(Geometry2D)

register(Gemeindetyp.__bodId__, Gemeindetyp)


class WindenergieBundesinteressen(Base, Vector):
    __tablename__ = 'windenergie_bundesint'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False})
    __template__ = 'templates/htmlpopup/windenergie_bundesinteressen.mako'
    __bodId__ = 'ch.are.windenergie-bundesinteressen'
    __label__ = 'kbik'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    kbik = Column('kbik', Integer)
    weitere_einschraenk_de = Column('weitere_einschraenk_de', Unicode)
    weitere_einschraenk_fr = Column('weitere_einschraenk_fr', Unicode)
    weitere_einschraenk_it = Column('weitere_einschraenk_it', Unicode)
    schutzgeb_o_inter_de = Column('schutzgeb_o_inter_de', Unicode)
    schutzgeb_o_inter_fr = Column('schutzgeb_o_inter_fr', Unicode)
    schutzgeb_o_inter_it = Column('schutzgeb_o_inter_it', Unicode)
    grunds_ausschlussgeb_de = Column('grunds_ausschlussgeb_de', Unicode)
    grunds_ausschlussgeb_fr = Column('grunds_ausschlussgeb_fr', Unicode)
    grunds_ausschlussgeb_it = Column('grunds_ausschlussgeb_it', Unicode)
    inter_abwaeg_national_de = Column('inter_abwaeg_national_de', Unicode)
    inter_abwaeg_national_fr = Column('inter_abwaeg_national_fr', Unicode)
    inter_abwaeg_national_it = Column('inter_abwaeg_national_it', Unicode)
    vorbehaltsgeb_de = Column('vorbehaltsgeb_de', Unicode)
    vorbehaltsgeb_fr = Column('vorbehaltsgeb_fr', Unicode)
    vorbehaltsgeb_it = Column('vorbehaltsgeb_it', Unicode)
    the_geom = Column(Geometry2D)

register(WindenergieBundesinteressen.__bodId__, WindenergieBundesinteressen)


class ZweitwohnungsAnteil(Base, Vector):
    __tablename__ = 'zweitwohnungsanteil'
    __table_args__ = ({'schema': 'raumplanung', 'autoload': False})
    __template__ = 'templates/htmlpopup/zweitwohnungsanteil.mako'
    __bodId__ = 'ch.are.wohnungsinventar-zweitwohnungsanteil'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    gemeinde_name = Column('gemeinde_name', Unicode)
    gemeinde_nummer = Column('gemeinde_nummer', Integer)
    status = Column('status', Integer)
    verfahren = Column('verfahren', Integer)
    zwg_3150 = Column('zwg_3150', Integer)
    zwg_3010 = Column('zwg_3010', Integer)
    zwg_3100 = Column('zwg_3100', Integer)
    zwg_3110 = Column('zwg_3110', Float)
    zwg_3120 = Column('zwg_3120', Float)
    the_geom = Column(Geometry2D)

register(ZweitwohnungsAnteil.__bodId__, ZweitwohnungsAnteil)


class ReisezeitAgglomerationen:
    __tablename__ = 'reisezeit_agglomerationen'
    id = Column('verkehrszone_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class Reisezeit:
    __tablename__ = 'reisezeit'
    id = Column('verkehrszone_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class Erreichbarkeit:
    __tablename__ = 'erreichbarkeit'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    __label__ = 'id'
    id = Column('verkehrszone_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class ReisezeitAgglomerationenOev(Base, ReisezeitAgglomerationen, Vector):
    __bodId__ = 'ch.are.reisezeit-agglomerationen-oev'
    __template__ = 'templates/htmlpopup/reisezeit_agglomerationen_oev.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    oev_reisezeit_agglo = Column('oev_reisezeit_agglo', Integer)
    oev_no_agglo = Column('oev_no_agglo', Integer)

register(ReisezeitAgglomerationenOev.__bodId__, ReisezeitAgglomerationenOev)


class ReisezeitAgglomerationenMiv(Base, ReisezeitAgglomerationen, Vector):
    __bodId__ = 'ch.are.reisezeit-agglomerationen-miv'
    __template__ = 'templates/htmlpopup/reisezeit_agglomerationen_miv.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    strasse_reisezeit_agglo = Column('strasse_reisezeit_agglo', Integer)
    strasse_no_agglo = Column('strasse_no_agglo', Integer)

register(ReisezeitAgglomerationenMiv.__bodId__, ReisezeitAgglomerationenMiv)


class ReisezeitOev(Base, Reisezeit, Vector):
    __bodId__ = 'ch.are.reisezeit-oev'
    __template__ = 'templates/htmlpopup/reisezeit_oev.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    oev_reisezeit_z = Column('oev_reisezeit_z', Integer)
    oev_no_z = Column('oev_no_z', Integer)

register(ReisezeitOev.__bodId__, ReisezeitOev)


class ReisezeitMiv(Base, Reisezeit, Vector):
    __bodId__ = 'ch.are.reisezeit-miv'
    __template__ = 'templates/htmlpopup/reisezeit_miv.mako'
    __table_args__ = ({'schema': 'siedlung_landschaft', 'autoload': False, 'extend_existing': True})
    strasse_reisezeit_z = Column('strasse_reisezeit_z', Integer)
    strasse_no_z = Column('strasse_no_z', Integer)

register(ReisezeitMiv.__bodId__, ReisezeitMiv)


class ErreichbarkeitOev(Base, Erreichbarkeit, Vector):
    __bodId__ = 'ch.are.erreichbarkeit-oev'
    __template__ = 'templates/htmlpopup/erreichbarkeit_oev.mako'
    oev_erreichb_ewap = Column('oev_erreichb_ewap', Integer)

register(ErreichbarkeitOev.__bodId__, ErreichbarkeitOev)


class ErreichbarkeitMiv(Base, Erreichbarkeit, Vector):
    __bodId__ = 'ch.are.erreichbarkeit-miv'
    __template__ = 'templates/htmlpopup/erreichbarkeit_miv.mako'
    strasse_erreichb_ewap = Column('strasse_erreichb_ewap', Integer)

register(ErreichbarkeitMiv.__bodId__, ErreichbarkeitMiv)


class GeneralPersonenverkehrStrasse:
    __table_args__ = ({'schema': 'strassen', 'autoload': False})
    __template__ = 'templates/htmlpopup/personenverkehr_strasse.mako'
    __label__ = 'nr'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    nr = Column('nr', Integer)
    dwv_fzg = Column('dwv_fzg', Integer)
    dwv_pw = Column('dwv_pw', Integer)
    dwv_li = Column('dwv_li', Integer)
    dwv_lw = Column('dwv_lw', Integer)
    dwv_lz = Column('dwv_lz', Integer)
    dtv_fzg = Column('dtv_fzg', Integer)
    dtv_pw = Column('dtv_pw', Integer)
    dtv_li = Column('dtv_li', Integer)
    dtv_lw = Column('dtv_lw', Integer)
    dtv_lz = Column('dtv_lz', Integer)
    msp_fzg = Column('msp_fzg', Integer)
    msp_pw = Column('msp_pw', Integer)
    msp_li = Column('msp_li', Integer)
    msp_lw = Column('msp_lw', Integer)
    msp_lz = Column('msp_lz', Integer)
    asp_fzg = Column('asp_fzg', Integer)
    asp_pw = Column('asp_pw', Integer)
    asp_li = Column('asp_li', Integer)
    asp_lw = Column('asp_lw', Integer)
    asp_lz = Column('asp_lz', Integer)
    the_geom = Column(Geometry2D)


class BelastungPersonenverkehrStrasse(Base, GeneralPersonenverkehrStrasse, Vector):
    __tablename__ = 'belastung_personenverkehr'
    __bodId__ = 'ch.are.belastung-personenverkehr-strasse'

register(BelastungPersonenverkehrStrasse.__bodId__, BelastungPersonenverkehrStrasse)


class BelastungPersonenverkehrStrasseZukunft(Base, GeneralPersonenverkehrStrasse, Vector):
    __tablename__ = 'belastung_personenverkehr_zukunft'
    __bodId__ = 'ch.are.belastung-personenverkehr-strasse_zukunft'

register(BelastungPersonenverkehrStrasseZukunft.__bodId__, BelastungPersonenverkehrStrasseZukunft)


class GeneralBelastungPersonenverkehrBahn:
    __table_args__ = ({'schema': 'oeffentlicher_verkehr', 'autoload': False})
    __template__ = 'templates/htmlpopup/personenverkehr_bahn.mako'
    __label__ = 'nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr = Column('nr', Integer)
    dwv_oev = Column('dwv_oev', Integer)
    dtv_oev = Column('dtv_oev', Integer)
    msp_oev = Column('msp_oev', Integer)
    asp_oev = Column('asp_oev', Integer)
    the_geom = Column(Geometry2D)


class BelastungPersonenverkehrBahn(Base, GeneralBelastungPersonenverkehrBahn, Vector):
    __tablename__ = 'belastung_personenverkehr'
    __bodId__ = 'ch.are.belastung-personenverkehr-bahn'

register(BelastungPersonenverkehrBahn.__bodId__, BelastungPersonenverkehrBahn)


class BelastungPersonenverkehrBahnZukunft(Base, GeneralBelastungPersonenverkehrBahn, Vector):
    __tablename__ = 'belastung_personenverkehr_zukunft'
    __bodId__ = 'ch.are.belastung-personenverkehr-bahn_zukunft'

register(BelastungPersonenverkehrBahnZukunft.__bodId__, BelastungPersonenverkehrBahnZukunft)


class SolaranlagenPruefenswerteGebieteVektor(Base, Vector):
    __tablename__ = 'pruefenswerte_gebiete'
    __table_args__ = ({'schema': 'solaranlagen', 'autoload': False})
    __template__ = 'templates/htmlpopup/are_solaranlagen_pruefenswerte_gebiete.mako'
    __bodId__ = 'ch.are.solaranlagen-pruefenswerte_gebiete_vektor'
    __label__ = 'id'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    ptid = Column('ptid', Unicode)
    pruefwert = Column('pruefwert', Integer)
    pruefwert_de = Column('pruefwert_de', Unicode)
    pruefwert_fr = Column('pruefwert_fr', Unicode)
    sn_01 = Column('sn_01', Integer)
    sn_01_de = Column('sn_01_de', Unicode)
    sn_01_fr = Column('sn_01_fr', Unicode)
    schutz_01 = Column('schutz_01', Integer)
    schutz_01_de = Column('schutz_01_de', Unicode)
    schutz_01_fr = Column('schutz_01_fr', Unicode)
    nutz_01 = Column('nutz_01', Integer)
    nutz_01_de = Column('nutz_01_de', Unicode)
    nutz_01_fr = Column('nutz_01_fr', Unicode)
    nutz_02 = Column('nutz_02', Float)
    nutz_03 = Column('nutz_03', Float)
    nutz_04 = Column('nutz_04', Float)
    nutz_05 = Column('nutz_05', Integer)
    nutz_05_de = Column('nutz_05_de', Unicode)
    nutz_05_fr = Column('nutz_05_fr', Unicode)
    nutz_06 = Column('nutz_06', Integer)
    nutz_07 = Column('nutz_07', Integer)
    nutz_08 = Column('nutz_08', Integer)
    nutz_08_de = Column('nutz_08_de', Unicode)
    nutz_08_fr = Column('nutz_08_fr', Unicode)
    nutz_09 = Column('nutz_09', Integer)
    nutz_09_de = Column('nutz_09_de', Unicode)
    nutz_09_fr = Column('nutz_09_fr', Unicode)
    nutz_10 = Column('nutz_10', Integer)
    prot_10 = Column('prot_10', Unicode)
    prot_10_de = Column('prot_10_de', Unicode)
    prot_10_fr = Column('prot_10_fr', Unicode)
    prot_20 = Column('prot_20', Unicode)
    prot_20_de = Column('prot_20_de', Unicode)
    prot_20_fr = Column('prot_20_fr', Unicode)
    prot_30 = Column('prot_30', Unicode)
    prot_30_de = Column('prot_30_de', Unicode)
    prot_30_fr = Column('prot_30_fr', Unicode)
    prot_40 = Column('prot_40', Unicode)
    prot_40_de = Column('prot_40_de', Unicode)
    prot_40_fr = Column('prot_40_fr', Unicode)
    prot_60 = Column('prot_60', Unicode)
    prot_60_de = Column('prot_60_de', Unicode)
    prot_60_fr = Column('prot_60_fr', Unicode)
    prot_70 = Column('prot_70', Unicode)
    prot_70_de = Column('prot_70_de', Unicode)
    prot_70_fr = Column('prot_70_fr', Unicode)
    the_geom = Column(Geometry2D)

register(SolaranlagenPruefenswerteGebieteVektor.__bodId__, SolaranlagenPruefenswerteGebieteVektor)
