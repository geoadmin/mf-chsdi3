# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, Integer
from sqlalchemy.types import Numeric, Unicode, Float, SmallInteger
from geoalchemy2.types import Geometry

from chsdi.models import register, bases
from chsdi.models.types import DateTimeChsdi
from chsdi.models.vector import Vector, Geometry2D


Base = bases['bafu']


class Hydrogeologischekarte100(Base, Vector):
    __tablename__ = 'hydrogeologische_karte_100'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrogeologische-karte_100'
    __queryable_attributes__ = ['name', 'pdf_list']
    __template__ = 'templates/htmlpopup/hydrogeologische-karte_100.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('raster_name', Text)
    pdf_list = Column('pdf_list', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrogeologische-karte_100', Hydrogeologischekarte100)


class KarstFliesswege(Base, Vector):
    __tablename__ = 'karst_fliesswege'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __template__ = 'templates/htmlpopup/karst-unterirdische_fliesswege.mako'
    __bodId__ = 'ch.bafu.karst-unterirdische_fliesswege'
    __label__ = 'id'
    __queryable_attributes__ = ['ei_type', 'ei_hdyn']
    id = Column('objectid', Integer, primary_key=True)
    ei_id = Column('ei_id', Unicode)
    ei_hdyn = Column('ei_hdyn', SmallInteger)
    ei_type = Column('ei_type', SmallInteger)
    ei_type_fr = Column('ei_type_fr', Unicode)
    ei_type_de = Column('ei_type_de', Unicode)
    ei_type_it = Column('ei_type_it', Unicode)
    ei_type_en = Column('ei_type_en', Unicode)
    ei_hdyn_fr = Column('ei_hdyn_fr', Unicode)
    ei_hdyn_de = Column('ei_hdyn_de', Unicode)
    ei_hdyn_it = Column('ei_hdyn_it', Unicode)
    ei_hdyn_en = Column('ei_hdyn_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.karst-unterirdische_fliesswege', KarstFliesswege)


class KarstEinzugsgebieteinheiten(Base, Vector):
    __tablename__ = 'karst_einzugsgebieteinheiten'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __template__ = 'templates/htmlpopup/karst-einzugsgebietseinheiten.mako'
    __bodId__ = 'ch.bafu.karst-einzugsgebietseinheiten'
    __label__ = 'id'
    __queryable_attributes__ = ['ub_type', 'ub_flux']
    id = Column('objectid', Integer, primary_key=True)
    ub_name = Column('ub_name', Unicode)
    ub_type = Column('ub_type', SmallInteger)
    ub_flux = Column('ub_flux', SmallInteger)
    shape_area = Column('shape_area', Numeric)
    ub_alt_min = Column('ub_alt_min', SmallInteger)
    ub_alt_moy = Column('ub_alt_moy', SmallInteger)
    ub_alt_max = Column('ub_alt_max', SmallInteger)
    ub_type_fr = Column('ub_type_fr', Unicode)
    ub_type_de = Column('ub_type_de', Unicode)
    ub_type_it = Column('ub_type_it', Unicode)
    ub_type_en = Column('ub_type_en', Unicode)
    ub_flux_fr = Column('ub_flux_fr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.karst-einzugsgebietseinheiten', KarstEinzugsgebieteinheiten)


class KarstGrundwasservorkommen(Base, Vector):
    __tablename__ = 'karst_grundwasservorkommen'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __template__ = 'templates/htmlpopup/karst-ausdehnung_grundwasservorkommen.mako'
    __bodId__ = 'ch.bafu.karst-ausdehnung_grundwasservorkommen'
    __label__ = 'id'
    __queryable_attributes__ = ['nk_type', 'nk_level', 'nk_hdyn']
    id = Column('objectid', Integer, primary_key=True)
    nk_hdyn = Column('nk_hdyn', SmallInteger)
    nk_type = Column('nk_type', SmallInteger)
    nk_level = Column('nk_level', SmallInteger)
    nk_hdyn_fr = Column('nk_hdyn_fr', Unicode)
    nk_hdyn_de = Column('nk_hdyn_de', Unicode)
    nk_hdyn_it = Column('nk_hdyn_it', Unicode)
    nk_hdyn_en = Column('nk_hdyn_en', Unicode)
    nk_type_fr = Column('nk_type_fr', Unicode)
    nk_type_de = Column('nk_type_de', Unicode)
    nk_type_it = Column('nk_type_it', Unicode)
    nk_type_en = Column('nk_type_en', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.karst-ausdehnung_grundwasservorkommen', KarstGrundwasservorkommen)


class KarstEinzugsgebiete(Base, Vector):
    __tablename__ = 'karst_einzugsgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __template__ = 'templates/htmlpopup/karst-einzugsgebiete.mako'
    __bodId__ = 'ch.bafu.karst-einzugsgebiete'
    __label__ = 'ba_name'
    __queryable_attributes__ = ['ba_name']
    __returnedGeometry__ = 'the_geom_highlight'
    id = Column('objectid', Integer, primary_key=True)
    ba_id = Column('ba_id', Unicode)
    ba_name = Column('ba_name', Unicode)
    ba_alt_min = Column('ba_alt_min', SmallInteger)
    ba_alt_moy = Column('ba_alt_moy', SmallInteger)
    ba_alt_max = Column('ba_alt_max', SmallInteger)
    ba_surf = Column('ba_surf', Numeric)
    the_geom = Column(Geometry2D)
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bafu.karst-einzugsgebiete', KarstEinzugsgebiete)


class KarstQuellenschwinden(Base, Vector):
    __tablename__ = 'karst_quellen_schwinden'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __template__ = 'templates/htmlpopup/karst-quellen.mako'
    __bodId__ = 'ch.bafu.karst-quellen_schwinden'
    __label__ = 'ip_name'
    __returnedGeometry__ = 'the_geom_highlight'
    __queryable_attributes__ = ['ip_type', 'ip_name', 'ip_qclass', 'ip_reg', 'ip_exp']
    id = Column('objectid', Integer, primary_key=True)
    ip_id = Column('ip_id', Unicode)
    ip_name = Column('ip_name', Unicode)
    ip_type = Column('ip_type', SmallInteger)
    ip_qclass = Column('ip_qclass', SmallInteger)
    ip_reg = Column('ip_reg', SmallInteger)
    ip_exp = Column('ip_exp', SmallInteger)
    ip_type_fr = Column('ip_type_fr', Unicode)
    ip_type_de = Column('ip_type_de', Unicode)
    ip_type_it = Column('ip_type_it', Unicode)
    ip_type_en = Column('ip_type_en', Unicode)
    ip_qclass_fr = Column('ip_qclass_fr', Unicode)
    ip_qclass_de = Column('ip_qclass_de', Unicode)
    ip_qclass_it = Column('ip_qclass_it', Unicode)
    ip_qclass_en = Column('ip_qclass_en', Unicode)
    ip_reg_fr = Column('ip_reg_fr', Unicode)
    ip_reg_de = Column('ip_reg_de', Unicode)
    ip_reg_it = Column('ip_reg_it', Unicode)
    ip_reg_en = Column('ip_reg_en', Unicode)
    ip_exp_fr = Column('ip_exp_fr', Unicode)
    ip_exp_de = Column('ip_exp_de', Unicode)
    ip_exp_it = Column('ip_exp_it', Unicode)
    ip_exp_en = Column('ip_exp_en', Unicode)
    ip_x = Column('ip_x', Integer)
    ip_y = Column('ip_y', Integer)
    ip_z = Column('ip_z', Integer)
    the_geom = Column(Geometry2D)
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bafu.karst-quellen_schwinden', KarstQuellenschwinden)


class Vec25_gewaessernetz_2000(Base, Vector):
    __tablename__ = 'gewaessernetz_2000'
    __table_args__ = ({'schema': 'vec25', 'autoload': False})
    __bodId__ = 'ch.bafu.vec25-gewaessernetz_2000'
    __queryable_attributes__ = ['gwlnr', 'gewissnr', 'name', 'objectval']
    __template__ = 'templates/htmlpopup/vec25-gewaessernetz_2000.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    objectval = Column('objectval', Text)
    gewissnr = Column('gewissnr', Integer)
    gwlnr = Column('gwlnr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.vec25-gewaessernetz_2000', Vec25_gewaessernetz_2000)


class Untersuchungsgebiete(Base, Vector):
    __tablename__ = 'hydrologie_untersuchungsgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-untersuchungsgebiete'
    __queryable_attributes__ = ['name', 'max_hoe', 'min_hoe', 'mit_hoe', 'antv_ab86', 'einzugsgebietsflaeche', 'regimtyp']
    __template__ = 'templates/htmlpopup/hug.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    max_hoe = Column('max_hoe', Integer)
    min_hoe = Column('min_hoe', Integer)
    mit_hoe = Column('mit_hoe', Integer)
    regimtyp = Column('regimetyp', Text)
    antv_ab86 = Column('antv_ab86', Numeric)
    hyperlink = Column('hyperlink', Text)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Numeric)
    stationsseite_de = Column('stationsseite_de', Text)
    stationsseite_fr = Column('stationsseite_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-untersuchungsgebiete', Untersuchungsgebiete)


class Hochwassergrenzwertpegel(Base, Vector):
    __tablename__ = 'hochwassergrenzwertpegel'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hochwassergrenzwertpegel'
    __queryable_attributes__ = ['name', 'hoehe', 'einzugsgebietsflaeche', 'nummer', 'fluss', 'm_ende', 'm_beginn']
    __template__ = 'templates/htmlpopup/hochwassergrenzwertpegel.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    nummer = Column('nummer', Text)
    datenherkunft = Column('datenherkunft', Text)
    rechtswert = Column('rechtswert', Numeric)
    hochwert = Column('hochwert', Numeric)
    hoehe = Column('hoehe', Numeric)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Numeric)
    fluss = Column('fluss', Text)
    m_beginn = Column('m_beginn', Text)
    m_ende = Column('m_ende', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-hochwassergrenzwertpegel', Hochwassergrenzwertpegel)


class AtlasKantonaleMessstationen(Base, Vector):
    __tablename__ = 'hydro_atlas_kant_messstationen'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_kantonale-messstationen'
    __queryable_attributes__ = ['hoehe', 'betriebsbeginn', 'einzugsgebietsflaeche', 'nummer', 'vergletscherung', 'bilanzgebietsnummer']
    __template__ = 'templates/htmlpopup/atlas_kantonale_messstationen.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    nummer = Column('nummer', Text)
    datenherkunft = Column('datenherkunft', Text)
    rechtswert = Column('rechtswert', Numeric)
    hochwert = Column('hochwert', Numeric)
    hoehe = Column('hoehe', Numeric)
    betriebsbeginn = Column('betriebsbeginn', Numeric)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Numeric)
    bilanzgebietsnummer = Column('bilanzgebietsnummer', Integer)
    vergletscherung = Column('vergletscherung', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologischer-atlas_kantonale-messstationen', AtlasKantonaleMessstationen)


class Daueruntersuchung_fliessgewaesser(Base, Vector):
    __tablename__ = 'hydro_duntersuchung_fliessgewaesser'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser'
    __queryable_attributes__ = ['name', 'hoehe', 'betriebsbeginn', 'einzugsgebietsflaeche', 'mittlerehoehe', 'vergletscherung', 'stationierung', 'flussgebiet']
    __template__ = 'templates/htmlpopup/daueruntersuchung_fliessgewaesser.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    rechtswert = Column('rechtswert', Text)
    hochwert = Column('hochwert', Text)
    hoehe = Column('hoehe', Text)
    betriebsbeginn = Column('betriebsbeginn', Text)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Text)
    mittlerehoehe = Column('mittlerehoehe', Text)
    vergletscherung = Column('vergletscherung', Text)
    stationierung = Column('stationierung', Text)
    flussgebiet = Column('flussgebiet', Text)
    hyperlink_d = Column('hyperlink_d', Text)
    hyperlink_f = Column('hyperlink_f', Text)
    hyperlink_daten = Column('hyperlink_daten', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser', Daueruntersuchung_fliessgewaesser)


class Vec25_seen(Base, Vector):
    __tablename__ = 'seen'
    __table_args__ = ({'schema': 'vec25', 'autoload': False})
    __bodId__ = 'ch.bafu.vec25-seen'
    __queryable_attributes__ = ['gewaesserkennzahl', 'name', 'seetyp', 'ausgleichsbecken', 'reguliert', 'seeflaeche_km2', 'inhalt_see_mio_m3', 'nutzinhalt_mio_m3', 'tiefe_see_m', 'hoehenlage_muem', 'uferlaenge_m', 'gwlnr']
    __template__ = 'templates/htmlpopup/vec25_seen.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    gewaesserkennzahl = Column('gewaesserkennzahl', Integer)
    seetyp = Column('seetyp', Integer)
    natur_mit = Column('natur_mit', Integer)
    ausgleichsbecken = Column('ausgleichsbecken', Numeric)
    reguliert = Column('reguliert', Integer)
    seeflaeche_km2 = Column('seeflaeche_km2', Numeric)
    inhalt_see_mio_m3 = Column('inhalt_see_mio_m3', Numeric)
    nutzinhalt_mio_m3 = Column('nutzinhalt_mio_m3', Numeric)
    tiefe_see_m = Column('tiefe_see_m', Integer)
    hoehenlage_muem = Column('hoehenlage_muem', Integer)
    uferlaenge_m = Column('uferlaenge_m', Integer)
    gwlnr = Column('gwlnr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.vec25-seen', Vec25_seen)


class Hydro_Atlas_Flussgebiete(Base, Vector):
    __tablename__ = 'atlas_flussgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_flussgebiete'
    __queryable_attributes__ = ['nummer', 'name', 'shape_area', 'umfang']
    __template__ = 'templates/htmlpopup/atlas_flussgebiete.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    nummer = Column('nummer', Integer)
    flussgebiet = Column('flussgebiet', Integer)
    shape_area = Column('shape_area', Numeric)
    umfang = Column('umfang', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologischer-atlas_flussgebiete', Hydro_Atlas_Flussgebiete)


class Hydro_Atlas_Bilanzgebiete(Base, Vector):
    __tablename__ = 'atlas_bilanzgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_bilanzgebiete'
    __queryable_attributes__ = ['name', 'flussgebiet', 'shape_area']
    __template__ = 'templates/htmlpopup/atlas_bilanzgebiete.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    nummer = Column('nummer', Integer)
    flussgebiet = Column('flussgebiet', Integer)
    shape_area = Column('shape_area', Numeric)
    umfang = Column('umfang', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologischer-atlas_bilanzgebiete', Hydro_Atlas_Bilanzgebiete)


class Hydro_Atlas_Basisgebiete(Base, Vector):
    __tablename__ = 'atlas_basisgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_basisgebiete'
    __queryable_attributes__ = ['gebietskennzahl', 'bemerkung', 'flussgebiet', 'max_hoe', 'min_hoe', 'mit_hoe', 'mit_ns', 's_w_ns', 'jahrtemp_g', 'winttemp_g', 'shape_area']
    __template__ = 'templates/htmlpopup/atlas_basisgebiete.mako'
    __extended_info__ = True
    __label__ = 'nummer'
    id = Column('bgdi_id', Integer, primary_key=True)
    nummer = Column('nummer', Integer)
    gebietskennzahl = Column('gebietskennzahl', Integer)
    bemerkung = Column('bemerkung', Text)
    flussgebiet = Column('flussgebiet', Integer)
    max_hoe = Column('max_hoe', Integer)
    min_hoe = Column('min_hoe', Integer)
    mit_hoe = Column('mit_hoe', Numeric)
    mit_ns = Column('mit_ns', Numeric)
    s_w_ns = Column('s_w_ns', Numeric)
    jahrtemp_g = Column('jahrtemp_g', Numeric)
    winttemp_g = Column('winttemp_g', Numeric)
    shape_area = Column('shape_area', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologischer-atlas_basisgebiete', Hydro_Atlas_Basisgebiete)


class Niedrigwasserstatistik(Base, Vector):
    __tablename__ = 'niedrigwasserstatistik'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-niedrigwasserstatistik'
    __queryable_attributes__ = ['name']
    __template__ = 'templates/htmlpopup/niedrigwasserstatistik.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    url_nqpdf = Column('url_nqpdf', Text)
    hyperlink_de = Column('hyperlink_d', Text)
    hyperlink_fr = Column('hyperlink_f', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-niedrigwasserstatistik', Niedrigwasserstatistik)


class Typ_fliessgewaesser(Base, Vector):
    __tablename__ = 'typ_fliessgewaesser'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.typisierung-fliessgewaesser'
    __queryable_attributes__ = ['objectid_gwn25', 'grosserfluss', 'biogeo', 'hoehe', 'abfluss', 'gefaelle', 'geo', 'code', 'gewaessertyp', 'aehnlichkeit']
    __template__ = 'templates/htmlpopup/fliessgewaesser_typ.mako'
    __extended_info__ = True
    __label__ = 'objectid_gwn25'
    id = Column('bgdi_id', Integer, primary_key=True)
    gewaessertyp = Column('gewaessertyp', Integer)
    grosserfluss = Column('grosserfluss', Text)
    objectid_gwn25 = Column('objectid_gwn25', Integer)
    biogeo = Column('biogeo', Text)
    hoehe = Column('hoehe', Text)
    abfluss = Column('abfluss', Text)
    gefaelle = Column('gefaelle', Text)
    geo = Column('geo', Text)
    code = Column('code', Integer)
    objectid_gwn25 = Column('objectid_gwn25', Integer)
    aehnlichkeit = Column('aehnlichkeit', Integer)
    shape_length = Column('shape_length', Numeric)
    url_portraits = Column('url_portraits', Text)
    url_uebersicht_de = Column('url_uebersicht_de', Text)
    url_uebersicht_fr = Column('url_uebersicht_fr', Text)
    name = Column('name', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.typisierung-fliessgewaesser', Typ_fliessgewaesser)


class Wasser_Vermessungsstrecken(Base, Vector):
    __tablename__ = 'vermessungsstrecken'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasserbau-vermessungsstrecken'
    __queryable_attributes__ = ['gewaessernummer', 'streckenid', 'bezeichnung', 'gwlnr']
    __template__ = 'templates/htmlpopup/vermessungsstrecken.mako'
    __extended_info__ = True
    __label__ = 'bezeichnung'
    id = Column('bgdi_id', Integer, primary_key=True)
    bezeichnung = Column('bezeichnung', Text)
    routeid = Column('routeid', Integer)
    gewaessernummer = Column('gewaessernummer', Text)
    bemerkung = Column('bemerkung', Text)
    anfangsmass = Column('anfangsmass', Numeric)
    endmass = Column('endmass', Numeric)
    streckenid = Column('streckenid', Integer)
    bezeichnung = Column('bezeichnung', Text)
    laenge_km = Column('laenge_km', Numeric)
    anzahl_profile = Column('anzahl_profile', Integer)
    aufnahme_intervall = Column('aufnahme_intervall', Integer)
    aufnahme_letzte = Column('aufnahme_letzte', Integer)
    gwlnr = Column('gwlnr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasserbau-vermessungsstrecken', Wasser_Vermessungsstrecken)


class Mittlere_abfluesse(Base, Vector):
    __tablename__ = 'mittlere_abfluesse'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.mittlere-abfluesse'
    __queryable_attributes__ = ['mqn_jahr', 'mqn_jan', 'mqn_feb', 'mqn_mar', 'mqn_apr', 'mqn_mai', 'mqn_jun', 'mqn_jul',
                                'mqn_aug', 'mqn_sep', 'mqn_okt', 'mqn_nov', 'mqn_dez', 'regimetyp', 'regimenummer', 'abflussvar']
    __template__ = 'templates/htmlpopup/mittlere_abfluesse.mako'
    __extended_info__ = True
    __label__ = 'regimenummer'
    id = Column('bgdi_id', Integer, primary_key=True)
    mqn_jahr = Column('mqn_jahr', Numeric)
    mqn_jan = Column('mqn_jan', Numeric)
    mqn_feb = Column('mqn_feb', Numeric)
    mqn_mar = Column('mqn_mar', Numeric)
    mqn_apr = Column('mqn_apr', Numeric)
    mqn_mai = Column('mqn_mai', Numeric)
    mqn_jun = Column('mqn_jun', Numeric)
    mqn_jul = Column('mqn_jul', Numeric)
    mqn_aug = Column('mqn_aug', Numeric)
    mqn_sep = Column('mqn_sep', Numeric)
    mqn_okt = Column('mqn_okt', Numeric)
    mqn_nov = Column('mqn_nov', Numeric)
    mqn_dez = Column('mqn_dez', Numeric)
    regimetyp = Column('regimetyp', Text)
    regimenummer = Column('regimenummer', Integer)
    abflussvar = Column('abflussvar', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.mittlere-abfluesse', Mittlere_abfluesse)


class Wasserbau_querprofilmarken(Base, Vector):
    __tablename__ = 'querprofilmarken'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasserbau-querprofilmarken'
    __queryable_attributes__ = ['typ', 'herkunft']
    __template__ = 'templates/htmlpopup/querprofilmarken.mako'
    __extended_info__ = True
    __label__ = 'schluesselid'
    id = Column('bgdi_id', Integer, primary_key=True)
    schluesselid = Column('schluesselid', Integer)
    typ = Column('typ', Text)
    x_koordinate = Column('x_koordinate', Numeric)
    y_koordinate = Column('y_koordinate', Numeric)
    azimut = Column('azimut', Integer)
    herkunft = Column('herkunft', Text)
    bemerkung = Column('bemerkung', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasserbau-querprofilmarken', Wasserbau_querprofilmarken)


class Feststoffe_geschiebemessnetz(Base, Vector):
    __tablename__ = 'geschiebemessnetz'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.feststoffe-geschiebemessnetz'
    __queryable_attributes__ = ['gsch_n', 'lk', 'lage', 'fn', 'hmax', 'hmin', 'hmed', 'exp', 'form', 'geologie', 'platz', 'fluss', 'station', 'institut', 'amt']
    __template__ = 'templates/htmlpopup/geschiebemessnetz.mako'
    __extended_info__ = True
    __label__ = 'fluss'
    id = Column('bgdi_id', Integer, primary_key=True)
    rechtswert = Column('rechtswert', Integer)
    hochwert = Column('hochwert', Text)
    gsch_n = Column('gsch_n', Numeric)
    lk = Column('lk', Numeric)
    lage = Column('lage', Integer)
    fn = Column('fn', Numeric)
    hmax = Column('hmax', Numeric)
    hmin = Column('hmin', Numeric)
    hmed = Column('hmed', Numeric)
    exp = Column('exp', Text)
    form = Column('form', Numeric)
    geologie = Column('geologie', Text)
    platz = Column('platz', Text)
    fluss = Column('fluss', Text)
    station = Column('station', Text)
    institut = Column('institut', Text)
    amt = Column('amt', Text)
    abteilung = Column('abteilung', Text)
    sektion = Column('sektion', Text)
    kontakt_name = Column('kontakt_name', Text)
    strasse = Column('strasse', Text)
    plz = Column('plz', Text)
    ort = Column('ort', Text)
    sachbearb = Column('sachbearb', Text)
    telephon = Column('telephon', Text)
    fax = Column('fax', Text)
    emailadresse1 = Column('emailadresse1', Text)
    emailadresse2 = Column('emailadresse2', Text)
    pdf_file = Column('pdf_file', Text)
    lage_de = Column('lage_de', Text)
    lage_fr = Column('lage_fr', Text)
    platz_de = Column('platz_de', Text)
    platz_fr = Column('platz_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.feststoffe-geschiebemessnetz', Feststoffe_geschiebemessnetz)


class Nawa:
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __template__ = 'templates/htmlpopup/nawa.mako'
    __timeInstant__ = 'jahr'
    id = Column('bgdi_id', Integer, primary_key=True)
    klasse_de = Column('klasse_de', Unicode)
    klasse_fr = Column('klasse_fr', Unicode)
    klasse_it = Column('klasse_it', Unicode)
    klasse_en = Column('klasse_en', Unicode)
    gewaesser = Column('gewaesser_', Unicode)
    stelle_neu = Column('stelle_neu', Unicode)
    jahr = Column('jahr', Integer)
    kanton = Column('kanton', Unicode)
    the_geom = Column(Geometry2D)


class NawaNitrat(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_nitrat'
    __bodId__ = 'ch.bafu.gewaesserschutz-chemischer_zustand_nitrat'


class NawaNitrit(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_nitrit'
    __bodId__ = 'ch.bafu.gewaesserschutz-chemischer_zustand_nitrit'


class NawaAmmonium(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_ammonium'
    __bodId__ = 'ch.bafu.gewaesserschutz-chemischer_zustand_ammonium'


class NawaDoc(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_doc'
    __bodId__ = 'ch.bafu.gewaesserschutz-chemischer_zustand_doc'


class NawaPhosphorGesamt(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_phosphor_gesamt'
    __bodId__ = 'ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt'


class NawaFische(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_fische'
    __bodId__ = 'ch.bafu.gewaesserschutz-biologischer_zustand_fische'


class NawaMakrozoobenthos(Base, Nawa, Vector):
    __tablename__ = 'gewaessweschutz_makrozoobenthos'
    __bodId__ = 'ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos'


class NawaMakrophyten(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_makrophyten'
    __bodId__ = 'ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten'


class NawaDiatomeen(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_diatomeen'
    __bodId__ = 'ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen'


class NawaPhosphat(Base, Nawa, Vector):
    __tablename__ = 'gewaesserschutz_phosphat'
    __bodId__ = 'ch.bafu.gewaesserschutz-chemischer_zustand_phosphat'

register('ch.bafu.gewaesserschutz-chemischer_zustand_nitrat', NawaNitrat)
register('ch.bafu.gewaesserschutz-chemischer_zustand_nitrit', NawaNitrit)
register('ch.bafu.gewaesserschutz-chemischer_zustand_ammonium', NawaAmmonium)
register('ch.bafu.gewaesserschutz-chemischer_zustand_doc', NawaDoc)
register('ch.bafu.gewaesserschutz-chemischer_zustand_phosphor_gesamt', NawaPhosphorGesamt)
register('ch.bafu.gewaesserschutz-biologischer_zustand_fische', NawaFische)
register('ch.bafu.gewaesserschutz-biologischer_zustand_makrozoobenthos', NawaMakrozoobenthos)
register('ch.bafu.gewaesserschutz-biologischer_zustand_makrophyten', NawaMakrophyten)
register('ch.bafu.gewaesserschutz-biologischer_zustand_diatomeen', NawaDiatomeen)
register('ch.bafu.gewaesserschutz-chemischer_zustand_phosphat', NawaPhosphat)


class Hydro_q347(Base, Vector):
    __tablename__ = 'hydro_q347'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-q347'
    __queryable_attributes__ = ['basisid', 'lhg', 'gewaesser', 'flaeche', 'q_84_93', 'qp', 'p', 'qmod']
    __template__ = 'templates/htmlpopup/hydro_q347.mako'
    __extended_info__ = True
    __label__ = 'gewaesser'
    id = Column('bgdi_id', Integer, primary_key=True)
    gewaesser = Column('gewaesser', Text)
    bilanzid = Column('bilanzid', Text)
    id_q347 = Column('id', Integer)
    basisid = Column('basisid', Text)
    lhg = Column('lhg', Text)
    gewaesser = Column('gewaesser', Text)
    flaeche = Column('flaeche', Numeric)
    q_84_93 = Column('q_84_93', Numeric)
    qp = Column('qp', Numeric)
    p = Column('p', Text)
    qmod = Column('qmod', Numeric)
    bemerkung = Column('bemerkung', Text)
    symbolisierung = Column('symbolisierung', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-q347', Hydro_q347)


class HUG_stationen(Base, Vector):
    __tablename__ = 'hydrologie_untersuchungsgebiete_stationen'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-untersuchungsgebiete_stationen'
    __queryable_attributes__ = ['name', 'hoehe', 'betriebsbeginn', 'einzugsgebietsflaeche', 'flussgebiet']
    __template__ = 'templates/htmlpopup/hug_stationen.mako'
    __label__ = 'name'
    id = Column('geodb_oid', Integer, primary_key=True)
    name = Column('name', Text)
    hochwert = Column('hochwert', Integer)
    rechtswert = Column('rechtswert', Integer)
    hoehe = Column('hoehe', Integer)
    betriebsbeginn = Column('betriebsbeginn', Integer)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Numeric)
    flussgebiet = Column('flussgebiet', Text)
    hyperlink_f = Column('hyperlink_f', Text)
    hyperlink_d = Column('hyperlink_d', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-untersuchungsgebiete_stationen', HUG_stationen)


class Hintergrundkarte(Base, Vector):
    __tablename__ = 'hydrologie_hintergrundkarte'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hintergrundkarte'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-hintergrundkarte', Hintergrundkarte)


class Strukturguete_hochrhein_linkesufer(Base, Vector):
    __tablename__ = 'strukturguete_hochrhein'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.strukturguete-hochrhein_linkesufer'
    __queryable_attributes__ = ['lumfeld', 'rumfeld', 'lufer', 'rufer', 'sohle']
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Text)
    lumfeld = Column('l_umfeld', Integer)
    rumfeld = Column('r_umfeld', Integer)
    lufer = Column('l_ufer', Integer)
    rufer = Column('r_ufer', Integer)
    sohle = Column('sohle', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.strukturguete-hochrhein_linkesufer', Strukturguete_hochrhein_linkesufer)


class StrukturgueteHochrheinLinkesumfeld(Base, Vector):
    __tablename__ = 'strukturguete_hochrhein'
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.strukturguete-hochrhein_linkesumfeld'
    __queryable_attributes__ = ['lumfeld', 'rumfeld', 'lufer', 'rufer', 'sohle']
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Text)
    lumfeld = Column('l_umfeld', Integer)
    rumfeld = Column('r_umfeld', Integer)
    lufer = Column('l_ufer', Integer)
    rufer = Column('r_ufer', Integer)
    sohle = Column('sohle', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.strukturguete-hochrhein_linkesumfeld', StrukturgueteHochrheinLinkesumfeld)


class StrukturgueteHochrheinRechtesumfeld(Base, Vector):
    __tablename__ = 'strukturguete_hochrhein'
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.strukturguete-hochrhein_rechtesumfeld'
    __queryable_attributes__ = ['lumfeld', 'rumfeld', 'lufer', 'rufer', 'sohle']
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Text)
    lumfeld = Column('l_umfeld', Integer)
    rumfeld = Column('r_umfeld', Integer)
    lufer = Column('l_ufer', Integer)
    rufer = Column('r_ufer', Integer)
    sohle = Column('sohle', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.strukturguete-hochrhein_rechtesumfeld', StrukturgueteHochrheinRechtesumfeld)


class StrukturgueteHochrheinRechtesufer(Base, Vector):
    __tablename__ = 'strukturguete_hochrhein'
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.strukturguete-hochrhein_rechtesufer'
    __queryable_attributes__ = ['lumfeld', 'rumfeld', 'lufer', 'rufer', 'sohle']
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Text)
    lumfeld = Column('l_umfeld', Integer)
    rumfeld = Column('r_umfeld', Integer)
    lufer = Column('l_ufer', Integer)
    rufer = Column('r_ufer', Integer)
    sohle = Column('sohle', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.strukturguete-hochrhein_rechtesufer', StrukturgueteHochrheinRechtesufer)


class StrukturgueteHochrheinSohle(Base, Vector):
    __tablename__ = 'strukturguete_hochrhein'
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.strukturguete-hochrhein_sohle'
    __queryable_attributes__ = ['lumfeld', 'rumfeld', 'lufer', 'rufer', 'sohle']
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Text)
    lumfeld = Column('l_umfeld', Integer)
    rumfeld = Column('r_umfeld', Integer)
    lufer = Column('l_ufer', Integer)
    rufer = Column('r_ufer', Integer)
    sohle = Column('sohle', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.strukturguete-hochrhein_sohle', StrukturgueteHochrheinSohle)


class GewaesserschutzBadewasserqualitaet(Base, Vector):
    __tablename__ = 'baqua'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.gewaesserschutz-badewasserqualitaet'
    __queryable_attributes__ = ['id', 'bwname', 'groupid', 'nwunitname', 'rbdsuname',
                                'gemeinde', 'canton', 'bwatercat', 'qualitaet_ch']
    __template__ = 'templates/htmlpopup/gewaesserschutz_badewasserqualitaet.mako'
    __extended_info__ = True
    __label__ = 'bwname'
    id = Column('bwid', Unicode, primary_key=True, nullable=False)
    bwname = Column('bwname', Text, nullable=False)
    groupid = Column('groupid', Text, nullable=True)
    rbdsuname = Column('rbdsuname', Text, nullable=False)
    nwunitname = Column('nwunitname', Text, nullable=False)
    yearbw = Column('year_bw', Integer, nullable=False)
    bwatercat = Column('bwatercat', Text, nullable=False)
    url = Column('url', Text, nullable=True)
    canton = Column('canton', Text, nullable=False)
    eua_badeplatz = Column('eua_badeplatz', Integer, nullable=False)
    gemeinde = Column('gemeinde', Text, nullable=False)
    qualitaet_ch = Column('qualitaet_ch', Text, nullable=False)
    qualitaet_eua = Column('qualitaet_eua', Text, nullable=True)
    anzahlmessungen = Column('anzahlmessungen', Integer, nullable=False)
    verunreinigung_tage = Column('verunreinigung_tage', Integer, nullable=False)
    coord_ch = Column('coord_ch', Text, nullable=False)
    baquaimg = Column('baquaimg', Text, nullable=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.gewaesserschutz-badewasserqualitaet', GewaesserschutzBadewasserqualitaet)


class AM_G(Base, Vector):
    __tablename__ = 'am_g'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien_wanderobjekte'
    __template__ = 'templates/htmlpopup/bundinv_amphibien_w.mako'
    __label__ = 'am_g_name'
    id = Column('am_g_obj', Unicode, primary_key=True)
    am_g_name = Column('am_g_name', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien_wanderobjekte', AM_G)


class AM_L(Base, Vector):
    __tablename__ = 'am_l'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien'
    __template__ = 'templates/htmlpopup/bundinv_amphibien.mako'
    __label__ = 'am_l_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    am_l_obj = Column('am_l_obj', Text)
    am_l_name = Column('am_l_name', Text)
    am_l_fl = Column('am_l_fl', Text)
    am_l_berei = Column('am_l_berei', Text)
    am_l_gf = Column('am_l_gf', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien', AM_L)


class LHG(Base, Vector):
    __tablename__ = 'lhg'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hydromessstationen'
    __template__ = 'templates/htmlpopup/hydromessstationen.mako'
    __label__ = 'lhg_name'
    __returnedGeometry__ = 'the_geom_highlight'
    id = Column('edv_nr4', Integer, primary_key=True)
    lhg_name = Column('lhg_name', Text)
    the_geom = Column(Geometry2D)
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bafu.hydrologie-hydromessstationen', LHG)


class Temperaturmessnetz(Base, Vector):
    __tablename__ = 'temperaturmessnetz'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-wassertemperaturmessstationen'
    __queryable_attributes__ = ['id', 'name']
    __template__ = 'templates/htmlpopup/temperaturmessnetz.mako'
    __label__ = 'name'
    id = Column('nr', Integer, primary_key=True)
    url = Column('url', Text)
    name = Column('name', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-wassertemperaturmessstationen', Temperaturmessnetz)


class GewaesserschutzTemplate:
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klaeranlagen.mako'
    __extended_info__ = True
    __label__ = 'name'
    __queryable_attributes__ = ['nummer', 'name', 'ort', 'name_vorfluter', 'gewiss_nr', 'reinigungstyp', 'abw_tagesmittel', 'abw_tagesspitze',
                                'spitzenbelastung_regen', 'rohabwasser_tag', 'frischschlamm_tag', 'stabilisierter_schlamm_tag', 'bsb5anteil',
                                'bsb5absolut', 'csbanteil', 'csbabsolut', 'docanteil', 'docabsolut', 'nh4_nanteil', 'nh4_nabsolut', 'nh4_n_ganzjaehrig',
                                'nanteil', 'nabsolut', 'n_abwassertemperatur', 'gesamtpanteil', 'gesamtpabsolut', 'gesamt_ungel_stoffe_absolut',
                                'andere_stoffe', 'kanton', 'vsa_kategorie', 'ausbaugroesse_egw', 'anzahl_nat_einwohner', 'jahr_nat_einwohner', 'abwasseranteil_q347', 'gwlnr']
    id = Column('nummer', Integer, primary_key=True)
    name = Column('name', Text)
    rechtswert = Column('rechtswert', Integer)
    hochwert = Column('hochwert', Integer)
    hoehe = Column('hoehe', Integer)
    adresse = Column('adresse', Text)
    plz = Column('plz', Integer)
    ort = Column('ort', Text)
    tel_nr = Column('tel_nr', Text)
    vorfluterbez = Column('vorfluterbez', Text)
    name_vorfluter = Column('name_vorfluter', Text)
    gewiss_nr = Column('gewiss_nr', Integer)
    reinigungstyp = Column('reinigungstyp', Text)
    abw_tagesmittel = Column('abw_tagesmittel', Integer)
    abw_tagesspitze = Column('abw_tagesspitze', Integer)
    spitzenbelastung_regen = Column('spitzenbelastung_regen', Integer)
    rohabwasser_tag = Column('rohabwasser_tag', Integer)
    frischschlamm_tag = Column('frischschlamm_tag', Integer)
    stabilisierter_schlamm_tag = Column('stabilisierter_schlamm_tag', Integer)
    bsb5anteil = Column('bsb5anteil', Integer)
    bsb5absolut = Column('bsb5absolut', Integer)
    csbanteil = Column('csbanteil', Integer)
    csbabsolut = Column('csbabsolut', Integer)
    docanteil = Column('docanteil', Integer)
    docabsolut = Column('docabsolut', Integer)
    nh4_nanteil = Column('nh4_nanteil', Integer)
    nh4_nabsolut = Column('nh4_nabsolut', Integer)
    nh4_n_ganzjaehrig = Column('nh4_n_ganzjaehrig', Text)
    nanteil = Column('nanteil', Integer)
    nabsolut = Column('nabsolut', Integer)
    n_abwassertemperatur = Column('n_abwassertemperatur', Integer)
    gesamtpanteil = Column('gesamtpanteil', Integer)
    gesamtpabsolut = Column('gesamtpabsolut', Numeric)
    gesamt_ungel_stoffe_absolut = Column('gesamt_ungel_stoffe_absolut', Integer)
    andere_stoffe = Column('andere_stoffe', Text)
    kanton = Column('kanton', Text)
    vsa_kategorie = Column('vsa_kategorie', Text)
    ausbaugroesse_egw = Column('ausbaugroesse_egw', Integer)
    anzahl_nat_einwohner = Column('anzahl_nat_einwohner', Integer)
    jahr_nat_einwohner = Column('jahr_nat_einwohner', Integer)
    abwasseranteil_q347 = Column('abwasseranteil_q347', Numeric)
    gwlnr = Column('gwlnr', Text)
    the_geom = Column(Geometry2D)


class KlaeranlagenQ347(Base, GewaesserschutzTemplate, Vector):
    __tablename__ = 'klaeranlagen'
    __bodId__ = 'ch.bafu.gewaesserschutz-klaeranlagen_anteilq347'

register('ch.bafu.gewaesserschutz-klaeranlagen_anteilq347', KlaeranlagenQ347)


class Reinigungstyp(Base, GewaesserschutzTemplate, Vector):
    __tablename__ = 'klaeranlagen'
    __bodId__ = 'ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp'

register('ch.bafu.gewaesserschutz-klaeranlagen_reinigungstyp', Reinigungstyp)


class KlaeranlagenAusbaugroesse(Base, GewaesserschutzTemplate, Vector):
    __tablename__ = 'klaeranlagen'
    __bodId__ = 'ch.bafu.gewaesserschutz-klaeranlagen_ausbaugroesse'

register('ch.bafu.gewaesserschutz-klaeranlagen_ausbaugroesse', KlaeranlagenAusbaugroesse)


class FlussordnungszahlenStrahler(Base, Vector):
    __tablename__ = 'flussordnungszahlen'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.flussordnungszahlen-strahler'
    __template__ = 'templates/htmlpopup/flussordnungszahlen.mako'
    __label__ = 'arc_id'
    id = Column('bgdi_id', Integer, primary_key=True)
    arc_id = Column('arc_id', Integer)
    floz = Column('floz', Integer)
    main_len = Column('main_len', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.flussordnungszahlen-strahler', FlussordnungszahlenStrahler)


class Grundwasserschutzareale(Base, Vector):
    __tablename__ = 'grundwasserschutzareale'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.grundwasserschutzareale'
    __template__ = 'templates/htmlpopup/wasser_grundwasser.mako'
    __label__ = 'typ_de'  # Translatable labels in de fr it en
    id = Column('bgdi_id', Integer, primary_key=True)
    kanton = Column('kanton', Text)
    name = Column('name', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    typ_en = Column('typ_en', Text)
    source = Column('source', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    status_en = Column('status_en', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.grundwasserschutzareale', Grundwasserschutzareale)


class Grundwasserschutzzonen(Base, Vector):
    __tablename__ = 'grundwasserschutzzonen'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.grundwasserschutzzonen'
    __template__ = 'templates/htmlpopup/wasser_grundwasser.mako'
    __label__ = 'typ_de'  # Translatable labels in de fr it en
    id = Column('bgdi_id', Integer, primary_key=True)
    kanton = Column('kanton', Text)
    name = Column('name', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    typ_en = Column('typ_en', Text)
    source = Column('source', Text)
    status_de = Column('status_de', Text)
    status_fr = Column('status_fr', Text)
    status_it = Column('status_it', Text)
    status_en = Column('status_en', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.grundwasserschutzzonen', Grundwasserschutzzonen)


class Gewaesserschutzbereiche (Base, Vector):
    __tablename__ = 'gewaesserschutzbereiche'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.gewaesserschutzbereiche'
    __template__ = 'templates/htmlpopup/wasser_schutzbereiche.mako'
    __label__ = 'typ_de'  # Translatable labels in de fr it en
    id = Column('bgdi_id', Integer, primary_key=True)
    kanton = Column('kanton', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    typ_it = Column('typ_it', Text)
    typ_en = Column('typ_en', Text)
    source = Column('source', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.gewaesserschutzbereiche', Gewaesserschutzbereiche)


class Vorfluter (Base, Vector):
    __tablename__ = 'vorfluter'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-vorfluter'
    __template__ = 'templates/htmlpopup/vorfluter.mako'
    __label__ = 'teilezgnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    teilezgnr = Column('teilezgnr', Integer)
    gwlnr = Column('gwlnr', Text)
    measure = Column('measure', Integer)
    endmeasure = Column('endmeasure', Integer)
    name = Column('name', Text)
    regimenr = Column('regimenr', Integer)
    regimetyp = Column('regimetyp', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-vorfluter', Vorfluter)


class Gewaesserzustandst (Base, Vector):
    __tablename__ = 'dbgz'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-gewaesserzustandsmessstationen'
    __queryable_attributes__ = ['nr', 'name', 'gewaesser']
    __template__ = 'templates/htmlpopup/gewaesserzustandsmessstationen.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    nr = Column('nr', Numeric)
    gewaesser = Column('gewaesser', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-gewaesserzustandsmessstationen', Gewaesserzustandst)


class Teileinzugsgebiete2 (Base, Vector):
    __tablename__ = 'view_ebene_2km_full'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-teileinzugsgebiete_2'
    __template__ = 'templates/htmlpopup/teileinzugsgebiete2.mako'
    __returnedGeometry__ = 'ext_the_geom'
    __label__ = 'id'
    __extended_info__ = True
    __queryable_attributes__ = ['gwlnr', 'id', 'ext_ezg_flussgb']
    id = Column('teilezgnr', Integer, primary_key=True)
    gwlnr = Column('gwlnr', Text)
    measure = Column('measure', Integer)
    teilezgfla = Column('teilezgfla', Text)
    ezgflaeche = Column('ezgflaeche', Text)
    typ2_de = Column('typ2_de', Text)
    flussgb_de = Column('flussgb_de', Text)
    typ2_fr = Column('typ2_fr', Text)
    flussgb_fr = Column('flussgb_fr', Text)
    typ2_it = Column('typ2_it', Text)
    flussgb_it = Column('flussgb_it', Text)
    typ2_rm = Column('typ2_rm', Text)
    flussgb_rm = Column('flussgb_rm', Text)
    typ2_en = Column('typ2_en', Text)
    flussgb_en = Column('flussgb_en', Text)
    ext_gewiss_nr_namen_gewaesser = Column('ext_gewiss_nr_namen_gewaesser', Text)
    ext_ezg_xy_gebietsauslass = Column('ext_ezg_xy_gebietsauslass', Text)
    ext_gebietsauslaesse_gemeindename = Column('ext_gebietsauslaesse_gemeindename', Text)
    ext_ezg_gewissnr = Column('ext_ezg_gewissnr', Integer)
    ext_ezg_flussgb = Column('ext_ezg_flussgb', Integer)
    ext_physiogeographie_gesamtflaeche = Column('ext_physiogeographie_gesamtflaeche', Numeric)
    ext_physiogeographie_anteil_ch = Column('ext_physiogeographie_anteil_ch', Numeric)
    ext_landnutzung_ant_siedlung = Column('ext_landnutzung_ant_siedlung', Numeric)
    ext_landnutzung_ant_landwirtschaft = Column('ext_landnutzung_ant_landwirtschaft', Numeric)
    ext_landnutzung_ant_bestockt = Column('ext_landnutzung_ant_bestockt', Numeric)
    ext_landnutzung_ant_gewaesser = Column('ext_landnutzung_ant_gewaesser', Numeric)
    ext_landnutzung_ant_gletscher_firn = Column('ext_landnutzung_ant_gletscher_firn', Numeric)
    ext_landnutzung_ant_unprod_sonst = Column('ext_landnutzung_ant_unprod_sonst', Numeric)
    ext_physiogeographie_ch_min_z = Column('ext_physiogeographie_ch_min_z', Numeric)
    ext_physiogeographie_ch_mean_z = Column('ext_physiogeographie_ch_mean_z', Numeric)
    ext_physiogeographie_ch_max_z = Column('ext_physiogeographie_ch_max_z', Numeric)
    ext_abfluesse_regimetyp = Column('ext_abfluesse_regimetyp', Text)
    ext_abfluesse_mqn_jahr = Column('ext_abfluesse_mqn_jahr', Numeric)
    ext_abfluesse_mqn_jan = Column('ext_abfluesse_mqn_jan', Numeric)
    ext_abfluesse_mqn_feb = Column('ext_abfluesse_mqn_feb', Numeric)
    ext_abfluesse_mqn_mar = Column('ext_abfluesse_mqn_mar', Numeric)
    ext_abfluesse_mqn_apr = Column('ext_abfluesse_mqn_apr', Numeric)
    ext_abfluesse_mqn_mai = Column('ext_abfluesse_mqn_mai', Numeric)
    ext_abfluesse_mqn_jun = Column('ext_abfluesse_mqn_jun', Numeric)
    ext_abfluesse_mqn_jul = Column('ext_abfluesse_mqn_jul', Numeric)
    ext_abfluesse_mqn_aug = Column('ext_abfluesse_mqn_aug', Numeric)
    ext_abfluesse_mqn_sep = Column('ext_abfluesse_mqn_sep', Numeric)
    ext_abfluesse_mqn_okt = Column('ext_abfluesse_mqn_okt', Numeric)
    ext_abfluesse_mqn_nov = Column('ext_abfluesse_mqn_nov', Numeric)
    ext_abfluesse_mqn_dez = Column('ext_abfluesse_mqn_dez', Numeric)
    ext_ezg_datenausgabe = Column('ext_ezg_datenausgabe', Integer)
    ext_abfluesse_abflussvar = Column('ext_abfluesse_abflussvar', Numeric)
    the_geom = Column(Geometry2D)
    ext_the_geom = Column('ext_the_geom', Geometry(geometry_type='GEOMETRYCOLLECTION',
                                                   dimension=2, srid=21781))

register('ch.bafu.wasser-teileinzugsgebiete_2', Teileinzugsgebiete2)


class Teileinzugsgebiete40 (Base, Vector):
    __tablename__ = 'ebene_40km'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-teileinzugsgebiete_40'
    __template__ = 'templates/htmlpopup/teileinzugsgebiete40.mako'
    __label__ = 'tezgnr40'
    id = Column('bgdi_id', Integer, primary_key=True)
    tezgnr40 = Column('tezgnr40', Integer)
    teilezgfla = Column('teilezgfla', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-teileinzugsgebiete_40', Teileinzugsgebiete40)


class Gebietsauslaesse (Base, Vector):
    __tablename__ = 'outlets'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-gebietsauslaesse'
    __template__ = 'templates/htmlpopup/gebietsauslaesse.mako'
    __extended_info__ = True
    __label__ = 'ezgnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    ezgnr = Column('ezgnr', Integer)
    gwlnr = Column('gwlnr', Text)
    measure = Column('measure', Integer)
    gesamtflae = Column('gesamtflae', Text)
    gewaessern = Column('gewaessern', Text)
    anteil_ch = Column('anteil_ch', Text)
    kanal_de = Column('kanal_de', Text)
    kanal_fr = Column('kanal_fr', Text)
    kanal_it = Column('kanal_it', Text)
    kanal_rm = Column('kanal_rm', Text)
    kanal_en = Column('kanal_en', Text)
    meanalt = Column('meanalt', Text)
    maxalt = Column('maxalt', Text)
    mq_jahr = Column('mq_jahr', Text)
    feuchtflae = Column('feuchtflae', Text)
    wasserflae = Column('wasserflae', Text)
    bebautefl = Column('bebautefl', Text)
    landwirtsc = Column('landwirtsc', Text)
    wald_natur = Column('wald_natur', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-gebietsauslaesse', Gebietsauslaesse)


class AU(Base, Vector):
    __tablename__ = 'au'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-auen'
    __queryable_attributes__ = ['au_obj', 'au_name']
    __template__ = 'templates/htmlpopup/auen.mako'
    __label__ = 'au_name'
    id = Column('gid', Integer, primary_key=True)
    au_name = Column('au_name', Text)
    au_obj = Column('au_obj', Integer)
    au_objtyp = Column('au_objtyp', Text)
    au_fl = Column('au_fl', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-auen', AU)


class AuenVegetationsKarten(Base, Vector):
    __tablename__ = 'auen_vegetation'
    __table_args__ = ({'schema': 'flora', 'autoload': False})
    __bodId__ = 'ch.bafu.auen-vegetationskarten'
    __queryable_attributes__ = ['auveg_obj', 'auveg_name', 'auveg_jahr', 'auveg_k22']
    __template__ = 'templates/htmlpopup/auen_veg.mako'
    __label__ = 'auveg_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    auveg_name = Column('auveg_name', Text)
    auveg_obj = Column('auveg_obj', Integer)
    auveg_jahr = Column('auveg_jahr', Integer)
    auveg_k22 = Column('auveg_k22', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.auen-vegetationskarten', AuenVegetationsKarten)


class BLN(Base, Vector):
    __tablename__ = 'bln'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-bln'
    __queryable_attributes__ = ['bln_name']
    __template__ = 'templates/htmlpopup/bln.mako'
    __label__ = 'bln_name'
    id = Column('gid', Integer, primary_key=True)
    bln_name = Column('bln_name', Text)
    bln_obj = Column('bln_obj', Integer)
    bln_fl = Column('bln_fl', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-bln', BLN)


class HM(Base, Vector):
    __tablename__ = 'hm'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-hochmoore'
    __template__ = 'templates/htmlpopup/hochmoore.mako'
    __label__ = 'hm_name'
    id = Column('gid', Integer, primary_key=True)
    hm_name = Column('hm_name', Text)
    hm_obj = Column('hm_obj', Integer)
    hm_typ = Column('hm_typ', Integer)
    hm_fl = Column('hm_fl', Numeric)
    hm_ke = Column('hm_ke', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-hochmoore', HM)


class HMA(Base, Vector):
    __tablename__ = 'hochmoore_anhoerung'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-hochmoore_anhoerung'
    __template__ = 'templates/htmlpopup/hochmoore_anhoerung.mako'
    __label__ = 'obj_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    obj_nr = Column('obj_nr', Text)
    obj_name = Column('obj_name', Text)
    tobj_type = Column('tobj_type', Text)
    flaeche = Column('flaeche', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-hochmoore_anhoerung', HMA)


class TTA(Base, Vector):
    __tablename__ = 'trockenwiesen_trockenweiden_anhoerung'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung'
    __template__ = 'templates/htmlpopup/trockenwiesen_trockenweiden_anhoerung.mako'
    __label__ = 'obj_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    obj_nr = Column('obj_nr', Text)
    obj_name = Column('obj_name', Text)
    flaeche = Column('flaeche', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhoerung', TTA)


class MLA(Base, Vector):
    __tablename__ = 'moorlandschaften_anhoerung'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-moorlandschaften_anhoerung'
    __template__ = 'templates/htmlpopup/moorlandschaften_anhoerung.mako'
    __label__ = 'obj_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    obj_nr = Column('obj_nr', Text)
    obj_name = Column('obj_name', Text)
    flaeche = Column('flaeche', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-moorlandschaften_anhoerung', MLA)


class FMA(Base, Vector):
    __tablename__ = 'flachmoore_anhoerung'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-flachmoore_anhoerung'
    __template__ = 'templates/htmlpopup/flachmoore_anhoerung.mako'
    __label__ = 'obj_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    obj_nr = Column('obj_nr', Text)
    obj_name = Column('obj_name', Text)
    flaeche = Column('flaeche', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-flachmoore_anhoerung', FMA)


class AA(Base, Vector):
    __tablename__ = 'auen_anhoerung'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-auen_anhoerung'
    __template__ = 'templates/htmlpopup/auen_anhoerung.mako'
    __label__ = 'obj_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    obj_nr = Column('obj_nr', Text)
    obj_name = Column('obj_name', Text)
    flaeche = Column('flaeche', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-auen_anhoerung', AA)


class AWA(Base, Vector):
    __tablename__ = 'amphibien_wanderobjekte_anhoerung'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien_wanderobjekte_anhoerung'
    __template__ = 'templates/htmlpopup/amphibien_wanderobjekte_anhoerung.mako'
    __label__ = 'obj_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    obj_nr = Column('obj_nr', Text)
    obj_name = Column('obj_name', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien_wanderobjekte_anhoerung', AWA)


class AMA(Base, Vector):
    __tablename__ = 'amphibien_anhoerung'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien_anhoerung'
    __template__ = 'templates/htmlpopup/amphibien_anhoerung.mako'
    __label__ = 'obj_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    obj_nr = Column('obj_nr', Text)
    obj_name = Column('obj_name', Text)
    bereich = Column('bereich', Text)
    flaeche = Column('flaeche', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien_anhoerung', AMA)


class JB(Base, Vector):
    __tablename__ = 'jb'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-jagdbanngebiete'
    __queryable_attributes__ = ['jb_name']
    __template__ = 'templates/htmlpopup/jb.mako'
    __label__ = 'jb_name'  # Composite labels
    id = Column('gid', Integer, primary_key=True)
    jb_name = Column('jb_name', Text)
    jb_obj = Column('jb_obj', Integer)
    jb_kat = Column('jb_kat', Text)
    jb_fl = Column('jb_fl', Numeric)
    jb_gf = Column('jb_gf', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-jagdbanngebiete', JB)


class ML(Base, Vector):
    __tablename__ = 'ml'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-moorlandschaften'
    __template__ = 'templates/htmlpopup/moorlandschaften.mako'
    __label__ = 'ml_name'
    id = Column('gid', Integer, primary_key=True)
    ml_name = Column('ml_name', Text)
    ml_obj = Column('ml_obj', Integer)
    ml_fl = Column('ml_fl', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-moorlandschaften', ML)


class WV(Base, Vector):
    __tablename__ = 'wv'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-vogelreservate'
    __template__ = 'templates/htmlpopup/vogelreservate.mako'
    __label__ = 'wv_name'
    id = Column('gid', Integer, primary_key=True)
    wv_name = Column('wv_name', Text)
    wv_obj = Column('wv_obj', Integer)
    wv_kat = Column('wv_kat', Text)
    wv_fl = Column('wv_fl', Numeric)
    wv_gf = Column('wv_gf', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-vogelreservate', WV)


class wasserentnahmeAll(Base, Vector):
    __tablename__ = 'entnahme'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-entnahme'
    __template__ = 'templates/htmlpopup/wasserentnahme.mako'
    __label__ = 'rwknr'
    id = Column('gid', Integer, primary_key=True)
    rwknr = Column('rwknr', Text)
    kanton = Column('kanton', Text)
    kantoncode = Column('kantoncode', Text)
    ent_gew = Column('ent_gew', Text)
    link = Column('link', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-entnahme', wasserentnahmeAll)


class wasserleitungen(Base, Vector):
    __tablename__ = 'leitungen'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-leitungen'
    __template__ = 'templates/htmlpopup/wasserleitungen.mako'
    __label__ = 'rwknr'
    id = Column('gid', Integer, primary_key=True)
    kanton = Column('kanton', Text)
    kantoncode = Column('kantoncode', Text)
    rwknr = Column('rwknr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-leitungen', wasserleitungen)


class wasserrueckgabe(Base, Vector):
    __tablename__ = 'rueckgabe'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-rueckgabe'
    __template__ = 'templates/htmlpopup/wasserrueckgabe.mako'
    __label__ = 'rwknr'
    id = Column('gid', Integer, primary_key=True)
    kanton = Column('kanton', Text)
    kantoncode = Column('kantoncode', Text)
    rwknr = Column('rwknr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-rueckgabe', wasserrueckgabe)


class flachmoore(Base, Vector):
    __tablename__ = 'fm'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-flachmoore'
    __template__ = 'templates/htmlpopup/flachmoore.mako'
    __label__ = 'fm_name'
    id = Column('gid', Integer, primary_key=True)
    fm_name = Column('fm_name', Text)
    fm_obj = Column('fm_obj', Text)
    fm_gf = Column('fm_gf', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-flachmoore', flachmoore)


class flachmooreReg(Base, Vector):
    __tablename__ = 'flachmoore_regional'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-flachmoore_regional'
    __template__ = 'templates/htmlpopup/flachmoore_reg.mako'
    __label__ = 'fmreg_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    fmreg_name = Column('fmreg_name', Text)
    fmreg_obj = Column('fmreg_obj', Text)
    fmreg_gf = Column('fmreg_gf', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-flachmoore_regional', flachmooreReg)


class schutzgebiete_aulav_auen(Base, Vector):
    __tablename__ = 'auengebiete'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_auen'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_std.mako'
    __maxscale__ = 10000
    id = Column('bgdi_id', Integer, primary_key=True)
    key_obj = Column('au_obj', Numeric)
    key_name = Column('au_name', Text)
    key_version = Column('au_version', Text)
    typ = Column('typ', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_auen', schutzgebiete_aulav_auen)


class schutzgebiete_aulav_auen_general(Base, Vector):
    __tablename__ = 'auengebiete_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_auen'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_auen_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_auen', schutzgebiete_aulav_auen_general)


class schutzgebiete_aulav_jagdbanngebiete(Base, Vector):
    __tablename__ = 'jagdbanngebiete'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_jagdbanngebiete'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_std.mako'
    __maxscale__ = 10000
    id = Column('bgdi_id', Integer, primary_key=True)
    key_obj = Column('jb_obj', Numeric)
    key_name = Column('jb_name', Text)
    key_version = Column('jb_version', Text)
    typ = Column('typ', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_jagdbanngebiete', schutzgebiete_aulav_jagdbanngebiete)


class schutzgebiete_aulav_jagdbanngebiete_general(Base, Vector):
    __tablename__ = 'jagdbanngebiete_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_jagdbanngebiete'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_jagdbanngebiete_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_jagdbanngebiete', schutzgebiete_aulav_jagdbanngebiete_general)


class schutzgebiete_aulav_moorlandschaften(Base, Vector):
    __tablename__ = 'moorlandschaften'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_moorlandschaften'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_std.mako'
    __maxscale__ = 10000
    id = Column('bgdi_id', Integer, primary_key=True)
    key_obj = Column('ml_obj', Numeric)
    key_name = Column('ml_name', Text)
    key_version = Column('ml_version', Text)
    typ = Column('typ', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_moorlandschaften', schutzgebiete_aulav_moorlandschaften)


class schutzgebiete_aulav_moorlandschaften_general(Base, Vector):
    __tablename__ = 'moorlandschaften_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_moorlandschaften'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_moorlandschaften_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_moorlandschaften', schutzgebiete_aulav_moorlandschaften_general)


class schutzgebiete_aulav_uebrige(Base, Vector):
    __tablename__ = 'uebrige_gebiete'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_uebrige'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_uebrige.mako'
    __maxscale__ = 10000
    id = Column('bgdi_id', Integer, primary_key=True)
    wv_obj = Column('wv_obj', Numeric)
    wv_name = Column('wv_name', Text)
    nat_park = Column('nat_park', Numeric)
    fm_obj = Column('fm_obj', Numeric)
    fm_name = Column('fm_name', Text)
    hm_obj = Column('hm_obj', Numeric)
    hm_name = Column('hm_name', Text)
    np_name = Column('np_name', Text)
    typ = Column('typ', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_uebrige', schutzgebiete_aulav_uebrige)


class schutzgebiete_aulav_uebrige_general(Base, Vector):
    __tablename__ = 'uebrige_gebiete_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_uebrige'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_uebrige_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_uebrige', schutzgebiete_aulav_uebrige_general)


class paerke:
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __label__ = 'name'
    name = Column('park_name', Text)
    kategorie = Column('kategorie', Text)
    rechtsgrundlage = Column('rechtsgrundlage', Integer)
    status = Column('status', Text)
    the_geom = Column(Geometry2D)


class paerkeNationalerBedeutung (Base, paerke, Vector):
    __tablename__ = 'paerke_nationaler_bedeutung_zonen'
    __bodId__ = 'ch.bafu.schutzgebiete-paerke_nationaler_bedeutung'
    __template__ = 'templates/htmlpopup/paerke_nationaler_bedeutung.mako'
    id = Column('bgdi_id', Integer, primary_key=True)
    teil_nummer = Column('teil_nummer', Integer)
    objektnummer = Column('objektnummer', Integer)
    zone = Column('zone', Text)

register('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung', paerkeNationalerBedeutung)


class paerkeNationalerBedeutungPerimeter(Base, paerke, Vector):
    __tablename__ = 'paerke_nationaler_bedeutung_perimeter'
    __bodId__ = 'ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter'
    __template__ = 'templates/htmlpopup/paerke_nationaler_bedeutung_perimeter.mako'
    id = Column('objektnummer', Integer, primary_key=True)

register('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter', paerkeNationalerBedeutungPerimeter)


class ramsar(Base, Vector):
    __tablename__ = 'ramsar'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-ramsar'
    __template__ = 'templates/htmlpopup/ramsar.mako'
    __label__ = 'ra_name'
    id = Column('ra_id', Integer, primary_key=True)
    ra_name = Column('ra_name', Text)
    ra_obj = Column('ra_obj', Integer)
    ra_fl = Column('ra_fl', Text)
    ra_gf = Column('ra_gf', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-ramsar', ramsar)


class oekom_abschnitte(Base, Vector):
    __tablename__ = 'oekom_abschnitte'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.oekomorphologie-f_abschnitte'
    __template__ = 'templates/htmlpopup/oekom_abschnitte.mako'
    __extended_info__ = True
    __label__ = 'anfangsmass'
    id = Column('bgdi_id', Integer, primary_key=True)
    abschnr = Column('abschnr', Text)
    gsbreite = Column('gsbreite', Numeric)
    breitenvar_de = Column('breitenvar_de', Text)
    breitenvar_fr = Column('breitenvar_fr', Text)
    sohlver_de = Column('sohlver_de', Text)
    sohlver_fr = Column('sohlver_fr', Text)
    lufbebre = Column('lufbebre', Numeric)
    rufbebre = Column('rufbebre', Numeric)
    oekomklasse_de = Column('oekomklasse_de', Text)
    oekomklasse_fr = Column('oekomklasse_fr', Text)
    bemerkung = Column('bemerkung', Text)
    anfangsmass = Column('anfangsmass', Numeric)
    endmass = Column('endmass', Numeric)
    anfangsrechtswert = Column('anfangsrechtswert', Numeric)
    anfangshochwert = Column('anfangshochwert', Numeric)
    endrechtswert = Column('endrechtswert', Numeric)
    endhochwert = Column('endhochwert', Numeric)
    eindol_de = Column('eindol_de', Text)
    eindol_fr = Column('eindol_fr', Text)
    vnatabst_de = Column('vnatabst_de', Text)
    vnatabst_fr = Column('vnatabst_fr', Text)
    tiefenvar_de = Column('tiefenvar_de', Text)
    tiefenvar_fr = Column('tiefenvar_fr', Text)
    sohlmat = Column('sohlmat', Numeric)
    lbukver_de = Column('lbukver_de', Text)
    lbukver_fr = Column('lbukver_fr', Text)
    rbukver_de = Column('rbukver_de', Text)
    rbukver_fr = Column('rbukver_fr', Text)
    lbukmat_de = Column('lbukmat_de', Text)
    lbukmat_fr = Column('lbukmat_fr', Text)
    rbukmat_de = Column('rbukmat_de', Text)
    rbukmat_fr = Column('rbukmat_fr', Text)
    luferber_de = Column('luferber_de', Text)
    luferber_fr = Column('luferber_fr', Text)
    ruferber_de = Column('ruferber_de', Text)
    ruferber_fr = Column('ruferber_fr', Text)
    lufbebew_de = Column('lufbebew_de', Text)
    lufbebew_fr = Column('lufbebew_fr', Text)
    rufbebew_de = Column('rufbebew_de', Text)
    rufbebew_fr = Column('rufbebew_fr', Text)
    bewalgen_de = Column('bewalgen_de', Text)
    bewalgen_fr = Column('bewalgen_fr', Text)
    bewmakro_de = Column('bewmakro_de', Text)
    bewmakro_fr = Column('bewmakro_fr', Text)
    totholz_de = Column('totholz_de', Text)
    totholz_fr = Column('totholz_fr', Text)
    notizen = Column('notizen', Text)
    translid = Column('translid', Numeric)
    datum = Column('datum', Text)
    oekomklasse = Column('oekomklasse', Numeric)
    sohlmat_de = Column('sohlmat_de', Text)
    sohlmat_fr = Column('sohlmat_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.oekomorphologie-f_abschnitte', oekom_abschnitte)


class oekom_abstuerze(Base, Vector):
    __tablename__ = 'oekom_abstuerze'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.oekomorphologie-f_abstuerze'
    __template__ = 'templates/htmlpopup/oekom_abstuerze.mako'
    __extended_info__ = True
    __label__ = 'abstnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    abstnr = Column('abstnr', Text)
    absttyp_de = Column('absttyp_de', Text)
    absttyp_fr = Column('absttyp_fr', Text)
    abstmat_de = Column('abstmat_de', Text)
    abstmat_fr = Column('abstmat_fr', Text)
    absthoehe = Column('absthoehe', Numeric,)
    bemerkung = Column('bemerkung', Text)
    mass = Column('mass', Numeric,)
    rechtswert = Column('rechtswert', Numeric)
    hochwert = Column('hochwert', Numeric)
    abschnr = Column('abschnr', Text)
    notizen = Column('notizen', Text)
    translid = Column('translid', Numeric)
    loc_angle_geo = Column('loc_angle_geo', Numeric)
    datum = Column('datum', Text)
    absttyp = Column('absttyp', Numeric)
    abstmat = Column('abstmat', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.oekomorphologie-f_abstuerze', oekom_abstuerze)


class oekom_bauwerke(Base, Vector):
    __tablename__ = 'oekom_bauwerke'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.oekomorphologie-f_bauwerke'
    __template__ = 'templates/htmlpopup/oekom_bauwerke.mako'
    __extended_info__ = True
    __label__ = 'bauwnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    bauwnr = Column('bauwnr', Text)
    bauwtyp_de = Column('bauwtyp_de', Text)
    bauwtyp_fr = Column('bauwtyp_fr', Text)
    bauwhoehe = Column('bauwhoehe', Numeric)
    mass = Column('mass', Numeric)
    rechtswert = Column('rechtswert', Numeric)
    hochwert = Column('hochwert', Numeric)
    abschnr = Column('abschnr', Text)
    bemerkung = Column('bemerkung', Text)
    notizen = Column('notizen', Text)
    translid = Column('translid', Numeric)
    loc_angle_geo = Column('loc_angle_geo', Numeric)
    datum = Column('datum', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.oekomorphologie-f_bauwerke', oekom_bauwerke)


class steinbockkolonien(Base, Vector):
    __tablename__ = 'sb'
    __table_args__ = ({'schema': 'fauna', 'autoload': False})
    __bodId__ = 'ch.bafu.fauna-steinbockkolonien'
    __template__ = 'templates/htmlpopup/steinbockkolonien.mako'
    __label__ = 'sb_name'
    id = Column('gid', Integer, primary_key=True)
    sb_name = Column('sb_name', Text)
    sb_obj = Column('sb_obj', Integer)
    sb_kt = Column('sb_kt', Text)
    sb_fl = Column('sb_fl', Numeric)
    sb_gf = Column('sb_gf', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.fauna-steinbockkolonien', steinbockkolonien)


class SWISSPRTR(Base, Vector):
    __tablename__ = 'swissprtr'
    __table_args__ = ({'schema': 'prtr', 'autoload': False})
    __bodId__ = 'ch.bafu.swissprtr'
    __template__ = 'templates/htmlpopup/swissprtr.mako'
    __label__ = 'betrieb'
    id = Column('prtrnr', Integer, primary_key=True)
    betrieb = Column('betrieb', Text)
    ort = Column('ort', Text)
    jahr = Column('jahr', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.swissprtr', SWISSPRTR)


class HOLZVORRAT(Base, Vector):
    __tablename__ = 'holzvorrat'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __bodId__ = 'ch.bafu.holzvorrat'
    __template__ = 'templates/htmlpopup/holzvorrat.mako'
    __label__ = 'wireg_'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    vorrat = Column('vorrat', Numeric)
    wireg_ = Column('wireg_', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.holzvorrat', HOLZVORRAT)


class HOLZZUWACHS(Base, Vector):
    __tablename__ = 'holzzuwachs'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __bodId__ = 'ch.bafu.holzzuwachs'
    __template__ = 'templates/htmlpopup/holzzuwachs.mako'
    __label__ = 'wirtschaftsregion'
    id = Column('gid', Integer, primary_key=True)
    wirtschaftsregion = Column('wirtschaftsregion', Text)
    holzzuwachs = Column('holzzuwachs', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.holzzuwachs', HOLZZUWACHS)


class HOLZNUTZUNG(Base, Vector):
    __tablename__ = 'holznutzung'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __bodId__ = 'ch.bafu.holznutzung'
    __template__ = 'templates/htmlpopup/holznutzung.mako'
    __label__ = 'wireg_'
    id = Column('gid', Integer, primary_key=True)
    wireg_ = Column('wireg_', Text)
    nutzung = Column('nutzung', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.holznutzung', HOLZNUTZUNG)


class NABEL(Base, Vector):
    __tablename__ = 'nabel'
    __table_args__ = ({'schema': 'luft', 'autoload': False})
    __bodId__ = 'ch.bafu.nabelstationen'
    __template__ = 'templates/htmlpopup/nabel.mako'
    __label__ = 'name'
    id = Column('id_stat', Unicode, primary_key=True)
    name = Column('name', Text)
    typ_de = Column('typ_de', Text)
    typ_fr = Column('typ_fr', Text)
    desc_de = Column('desc_de', Text)
    desc_fr = Column('desc_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.nabelstationen', NABEL)


class krebspest(Base, Vector):
    __tablename__ = 'krebspest'
    __table_args__ = ({'schema': 'fischerei', 'autoload': False})
    __bodId__ = 'ch.bafu.fischerei-krebspest'
    __template__ = 'templates/htmlpopup/krebspest.mako'
    __label__ = 'kennummer'
    id = Column('_count', Integer, primary_key=True)
    kennummer = Column('kennummer', Text)
    gewaesser = Column('gewaesser', Text)
    art_lat = Column('art_lat', Text)
    jahr = Column('jahr', Text)
    ort = Column('ort', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.fischerei-krebspest', krebspest)


class biogeoreg(Base, Vector):
    __tablename__ = 'biogeoreg'
    __table_args__ = ({'schema': 'diverse', 'autoload': False})
    __bodId__ = 'ch.bafu.biogeographische_regionen'
    __template__ = 'templates/htmlpopup/biogeoreg.mako'
    __label__ = 'biogreg_r1'
    id = Column('bgdi_id', Integer, primary_key=True)
    biogreg_r6 = Column('biogreg_r6', Text)
    biogreg_ve = Column('biogreg_ve', Text)
    biogreg_r1 = Column('biogreg_r1', Text)
    biogreg_c6 = Column('biogreg_c6', Integer)
    biogreg_c1 = Column('biogreg_c1', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.biogeographische_regionen', biogeoreg)


class smaragd(Base, Vector):
    __tablename__ = 'smaragd'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-smaragd'
    __template__ = 'templates/htmlpopup/smaragd.mako'
    __label__ = 'em_name'
    id = Column('id', Integer, primary_key=True)
    em_name = Column('em_name', Text)
    em_obj = Column('em_obj', Numeric)
    em_gf = Column('em_gf', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-smaragd', smaragd)


class biosphaerenreservate(Base, Vector):
    __tablename__ = 'biores'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-biosphaerenreservate'
    __template__ = 'templates/htmlpopup/biosphaerenreservate.mako'
    __label__ = 'biores_nam'
    id = Column('bgdi_id', Integer, primary_key=True)
    biores_ver = Column('biores_ver', Text)
    biores_fl = Column('biores_fl', Text)
    biores_gf = Column('biores_gf', Text)
    biores_nam = Column('biores_nam', Text)
    biores_obj = Column('biores_obj', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-biosphaerenreservate', biosphaerenreservate)


class moose(Base, Vector):
    __tablename__ = 'mooseflora'
    __table_args__ = ({'schema': 'flora', 'autoload': False})
    __bodId__ = 'ch.bafu.moose'
    __template__ = 'templates/htmlpopup/moose.mako'
    __label__ = 'genus'
    id = Column('bgdi_id', Integer, primary_key=True)
    genus = Column('genus', Text)
    populationsnr = Column('populationsnr', Numeric)
    jahr = Column('jahr', Integer)
    standort = Column('standort', Text)
    rl_text = Column('rl_text', Text)
    nhv_text = Column('nhv_text', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.moose', moose)


class weltensutter(Base, Vector):
    __tablename__ = 'ws'
    __table_args__ = ({'schema': 'flora', 'autoload': False})
    __bodId__ = 'ch.bafu.flora-weltensutter_atlas'
    __template__ = 'templates/htmlpopup/weltensutter.mako'
    __label__ = 'nom'
    id = Column('gid', Integer, primary_key=True)
    nom = Column('nom', Text)
    no_surface = Column('no_surface', Numeric)
    ty_surface = Column('ty_surface', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.flora-weltensutter_atlas', weltensutter)


class baumarten(Base, Vector):
    __tablename__ = 'baumartenmischung'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __bodId__ = 'ch.bafu.landesforstinventar-baumarten'
    __template__ = 'templates/htmlpopup/baumarten.mako'
    __label__ = 'wirtschaft'
    id = Column('bgdi_id', Integer, primary_key=True)
    wirtschaft = Column('wirtschaft', Text)
    anteil_lau = Column('anteil_lau', Numeric)
    anteil_nad = Column('anteil_nad', Numeric)
    vorrat = Column('vorrat', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.landesforstinventar-baumarten', baumarten)


class waldanteil(Base, Vector):
    __tablename__ = 'waldanteil'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __bodId__ = 'ch.bafu.landesforstinventar-waldanteil'
    __template__ = 'templates/htmlpopup/waldanteil.mako'
    __label__ = 'wirtschaft'
    id = Column('bgdi_id', Integer, primary_key=True)
    wirtschaft = Column('wirtschaft', Text)
    waldflaech = Column('waldflaech', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.landesforstinventar-waldanteil', waldanteil)


class totholz(Base, Vector):
    __tablename__ = 'totholzvolumen'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __bodId__ = 'ch.bafu.landesforstinventar-totholz'
    __template__ = 'templates/htmlpopup/totholz.mako'
    __label__ = 'wirtschaft'
    id = Column('bgdi_id', Integer, primary_key=True)
    wirtschaft = Column('wirtschaft', Text)
    totholzvol = Column('totholzvol', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.landesforstinventar-totholz', totholz)


class histerdbeben(Base, Vector):
    __tablename__ = 'historische_erdbeben'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-historische_erdbeben'
    __template__ = 'templates/htmlpopup/histerdbeben.mako'
    __label__ = 'date_time'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Integer)
    epicentral = Column('epicentral', Text)
    intensity = Column('intensity', Text)
    magnitude = Column('magnitude', Numeric)
    date_time = Column('date_time', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.gefahren-historische_erdbeben', histerdbeben)


class spektral(Base, Vector):
    __tablename__ = 'baugrundkl_spectral'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-spektral'
    __template__ = 'templates/htmlpopup/spektral.mako'
    __label__ = 'id'
    id = Column('_count', Integer, primary_key=True)
    fid = Column('id', Integer)
    spectral_3 = Column('spectral_3', Text)
    spectral_4 = Column('spectral_4', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.gefahren-spektral', spektral)


class trockenwiesenundweiden(Base, Vector):
    __tablename__ = 'tww'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-trockenwiesen_trockenweiden'
    __template__ = 'templates/htmlpopup/trockenwiesenundweiden.mako'
    __label__ = 'tww_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    tww_name = Column('tww_name', Text)
    tww_fl = Column('tww_fl', Numeric)
    tww_gf = Column('tww_gf', Numeric)
    tww_obj = Column('tww_obj', Numeric)
    tww_tobj = Column('tww_tobj', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-trockenwiesen_trockenweiden', trockenwiesenundweiden)


class trockenwiesenundweiden_anhang2(Base, Vector):
    __tablename__ = 'trockenwiesen_weiden_anhang2'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2'
    __template__ = 'templates/htmlpopup/tww_anhang2.mako'
    __label__ = 'tww_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    tww_name = Column('tww_name', Text)
    tww_obj = Column('tww_obj', Numeric)
    tww_tobj = Column('tww_tobj', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2', trockenwiesenundweiden_anhang2)


class amphibien_anhang4(Base, Vector):
    __tablename__ = 'amphibien_anhang4'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien_anhang4'
    __template__ = 'templates/htmlpopup/amphibien_anhang4.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    obnr = Column('obnr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien_anhang4', amphibien_anhang4)


class baugrundklassen(Base, Vector):
    __tablename__ = 'baugrundklassen'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-baugrundklassen'
    __template__ = 'templates/htmlpopup/baugrundklassen.mako'
    __label__ = 'bgk'
    __returnedGeometry__ = 'the_geom_highlight'
    id = Column('_count', Integer, primary_key=True)
    bgk = Column('bgk', Text)
    the_geom = Column(Geometry2D)
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bafu.gefahren-baugrundklassen', baugrundklassen)


class wrzselect(Base, Vector):
    __tablename__ = 'jgd_select'
    __table_args__ = ({'schema': 'wrzportal', 'autoload': False})
    __bodId__ = 'ch.bafu.wrz-jagdbanngebiete_select'
    __template__ = 'templates/htmlpopup/wrz_select.mako'
    __queryable_attributes__ = ['kanton', 'jb_name', 'beschlussjahr', 'schutzs_de', 'schutzs_fr', 'schutzs_it']
    __label__ = 'jb_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    jb_name = Column('jb_name', Unicode)
    schutzs_de = Column('schutzs_de', Unicode)
    schutzs_it = Column('schutzs_it', Unicode)
    schutzs_fr = Column('schutzs_fr', Unicode)
    bestimmung = Column('bestimmung', Unicode)
    best_de = Column('best_de', Unicode)
    best_it = Column('best_it', Unicode)
    best_fr = Column('best_fr', Unicode)
    schutzzeit = Column('schutzzeit', Unicode)
    grundlage = Column('grundlage', Unicode)
    zusatzinformation = Column('zusatzinformation', Unicode)
    beschlussjahr = Column('beschlussjahr', Unicode)
    kanton = Column('kanton', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wrz-jagdbanngebiete_select', wrzselect)


class wrzportal(Base, Vector):
    __tablename__ = 'wrz_portal'
    __table_args__ = ({'schema': 'wrzportal', 'autoload': False})
    __bodId__ = 'ch.bafu.wrz-wildruhezonen_portal'
    __template__ = 'templates/htmlpopup/wrz_portal.mako'
    __queryable_attributes__ = ['kanton', 'wrz_name', 'beschlussjahr', 'schutzs_de', 'schutzs_fr', 'schutzs_it']
    __label__ = 'wrz_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    wrz_name = Column('wrz_name', Unicode)
    schutzs_de = Column('schutzs_de', Unicode)
    schutzs_it = Column('schutzs_it', Unicode)
    schutzs_fr = Column('schutzs_fr', Unicode)
    bestimmung = Column('bestimmung', Unicode)
    best_de = Column('best_de', Unicode)
    best_it = Column('best_it', Unicode)
    best_fr = Column('best_fr', Unicode)
    schutzzeit = Column('schutzzeit', Unicode)
    grundlage = Column('grundlage', Unicode)
    beschlussjahr = Column('beschlussjahr', Unicode)
    zusatzinformation = Column('zusatzinformation', Unicode)
    kanton = Column('kanton', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wrz-wildruhezonen_portal', wrzportal)


class wildtier(Base, Vector):
    __tablename__ = 'wildtierkorridore'
    __table_args__ = ({'schema': 'fauna', 'autoload': False})
    __bodId__ = 'ch.bafu.fauna-wildtierkorridor_national'
    __template__ = 'templates/htmlpopup/wildtierkorridor.mako'
    __label__ = 'nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr = Column('nr', Text)
    zusta_dt = Column('zusta_dt', Text)
    zusta_fr = Column('zusta_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.fauna-wildtierkorridor_national', wildtier)


class Waldreservate(Base, Vector):
    __tablename__ = 'waldreservate'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __template__ = 'templates/htmlpopup/bafu_waldreservate.mako'
    __bodId__ = 'ch.bafu.waldreservate'
    __queryable_attributes__ = ['objnummer', 'name', 'gisflaeche', 'gisteilobjekt', 'mcpfe']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Text)
    gisteilobjekt = Column('obj_gisteilobjekt', Numeric)
    name = Column('name', Text)
    gisflaeche = Column('obj_gisflaeche', Numeric)
    mcpfe = Column('mcpfe_class', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.waldreservate', Waldreservate)


class SturmStaudruck30(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False})
    __bodId__ = 'ch.bafu.sturm-staudruck_30'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Text)
    staudruck_50 = Column('staudruck_50', Text)
    staudruck_100 = Column('staudruck_100', Text)
    staudruck_300 = Column('staudruck_300', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_30', SturmStaudruck30)


class SturmStaudruck50(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-staudruck_50'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Text)
    staudruck_50 = Column('staudruck_50', Text)
    staudruck_100 = Column('staudruck_100', Text)
    staudruck_300 = Column('staudruck_300', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_50', SturmStaudruck50)


class SturmStaudruck100(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-staudruck_100'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Text)
    staudruck_50 = Column('staudruck_50', Text)
    staudruck_100 = Column('staudruck_100', Text)
    staudruck_300 = Column('staudruck_300', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_100', SturmStaudruck100)


class SturmStaudruck300(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-staudruck_300'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Text)
    staudruck_50 = Column('staudruck_50', Text)
    staudruck_100 = Column('staudruck_100', Text)
    staudruck_300 = Column('staudruck_300', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_300', SturmStaudruck300)


class SturmBoeenspitzen30(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_30'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    boenspitzen_kmh_30 = Column('boenspitzen_kmh_30', Text)
    boenspitzen_ms_30 = Column('boenspitzen_ms_30', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_30', SturmBoeenspitzen30)


class SturmBoeenspitzen50(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_50'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    boenspitzen_kmh_50 = Column('boenspitzen_kmh_50', Text)
    boenspitzen_ms_50 = Column('boenspitzen_ms_50', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_50', SturmBoeenspitzen50)


class SturmBoeenspitzen100(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_100'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    boenspitzen_kmh_100 = Column('boenspitzen_kmh_100', Text)
    boenspitzen_ms_100 = Column('boenspitzen_ms_100', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_100', SturmBoeenspitzen100)


class SturmBoeenspitzen300(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_300'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('oid', Integer, primary_key=True)
    boenspitzen_kmh_300 = Column('boenspitzen_kmh_300', Text)
    boenspitzen_ms_300 = Column('boenspitzen_ms_300', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_300', SturmBoeenspitzen300)


class Hochwasserstatistik(Base, Vector):
    __tablename__ = 'hochwasserstatistik'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hochwasserstatistik'
    __queryable_attributes__ = ['name']
    __template__ = 'templates/htmlpopup/hochwasserstatistik.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    url_fr = Column('url_fr', Text)
    url_de = Column('url_de', Text)
    url_hqpdf = Column('url_hqpdf', Text)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-hochwasserstatistik', Hochwasserstatistik)


class HydrogeologieMarkierversuche(Base, Vector):
    __tablename__ = 'hydrogeologie_markierversuche'
    __table_args__ = ({'schema': 'hydrogeolog', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrogeologie-markierversuche'
    __template__ = 'templates/htmlpopup/hydrogeologie_markierversuche.mako'
    __queryable_attributes__ = ['ort', 'milieu', 'markierstoff']
    __label__ = 'id'
    id = Column('id', Integer, primary_key=True)
    nummer_ein = Column('nummer_ein', Integer)
    y = Column('y', Float)
    x = Column('x', Float)
    ort = Column('ort', Unicode)
    datum = Column('datum', DateTimeChsdi)
    milieu = Column('milieu', Unicode)
    markierstoff = Column('markierstoff', Unicode)
    menge_einheit = Column('menge_einheit', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrogeologie-markierversuche', HydrogeologieMarkierversuche)
