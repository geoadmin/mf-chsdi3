# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.types import Numeric, Unicode, Float, SmallInteger

from chsdi.models import register, bases
from chsdi.models.types import DateTimeChsdi
from chsdi.models.vector import Vector, Geometry2D


Base = bases['bafu']


class SchutzgebieteBiosphaerenreservate(Base, Vector):
    __tablename__ = 'biosphaeren'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-biosphaerenreservate'
    __template__ = 'templates/htmlpopup/biosphaerenreservate.mako'
    __returnedGeometry__ = 'the_geom_highlight'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Integer)
    version = Column('version', Unicode)
    shape_area_ha = Column('shape_area_ha', Float)
    the_geom = Column(Geometry2D)
    the_geom_highlight = Column('the_geom_gen50', Geometry2D)

register('ch.bafu.schutzgebiete-biosphaerenreservate', SchutzgebieteBiosphaerenreservate)


class AlpweidenHerdenschutzhunde(Base, Vector):
    __tablename__ = 'alpenweiden_herdenschutzhunde'
    __table_args__ = ({'schema': 'fauna', 'autoload': False})
    __bodId__ = 'ch.bafu.alpweiden-herdenschutzhunde'
    __template__ = 'templates/htmlpopup/alpweiden_herdenschutzhunde.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    kontname = Column('kontname', Unicode)
    konttel = Column('konttel', Unicode)
    kontemail = Column('kontemail', Unicode)
    code_refverhalten = Column('code_refverhalten', Integer)
    code_hundepraesenz = Column('code_hundepraesenz', Integer)
    code_hinweis = Column('code_hinweis', Integer)
    refmeldungbeweidungszone = Column('refmeldungbeweidungszone', Unicode)
    the_geom = Column(Geometry2D)

register(AlpweidenHerdenschutzhunde.__bodId__, AlpweidenHerdenschutzhunde)


class Hydrogeologischekarte100(Base, Vector):
    __tablename__ = 'hydrogeologische_karte_100'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrogeologische-karte_100'
    __template__ = 'templates/htmlpopup/hydrogeologische-karte_100.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('raster_name', Unicode)
    pdf_list = Column('pdf_list', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrogeologische-karte_100', Hydrogeologischekarte100)


class KarstFliesswege(Base, Vector):
    __tablename__ = 'karst_fliesswege'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __template__ = 'templates/htmlpopup/karst-unterirdische_fliesswege.mako'
    __bodId__ = 'ch.bafu.karst-unterirdische_fliesswege'
    __label__ = 'id'
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


class Vec25Gewaessernetz2000(Base, Vector):
    __tablename__ = 'gewaessernetz_2000'
    __table_args__ = ({'schema': 'vec25', 'autoload': False})
    __bodId__ = 'ch.bafu.vec25-gewaessernetz_2000'
    __template__ = 'templates/htmlpopup/vec25-gewaessernetz_2000.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objectval = Column('objectval', Unicode)
    gewissnr = Column('gewissnr', Integer)
    gwlnr = Column('gwlnr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.vec25-gewaessernetz_2000', Vec25Gewaessernetz2000)


class Untersuchungsgebiete(Base, Vector):
    __tablename__ = 'hydrologie_untersuchungsgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-untersuchungsgebiete'
    __template__ = 'templates/htmlpopup/hug.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    max_hoe = Column('max_hoe', Integer)
    min_hoe = Column('min_hoe', Integer)
    mit_hoe = Column('mit_hoe', Integer)
    regimtyp = Column('regimetyp', Unicode)
    antv_ab86 = Column('antv_ab86', Numeric)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Numeric)
    stationsseite_de = Column('stationsseite_de', Unicode)
    stationsseite_fr = Column('stationsseite_fr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-untersuchungsgebiete', Untersuchungsgebiete)


class Hochwassergrenzwertpegel(Base, Vector):
    __tablename__ = 'hochwassergrenzwertpegel'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hochwassergrenzwertpegel'
    __template__ = 'templates/htmlpopup/hochwassergrenzwertpegel.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    nummer = Column('nummer', Unicode)
    datenherkunft = Column('datenherkunft', Unicode)
    rechtswert = Column('rechtswert', Numeric)
    hochwert = Column('hochwert', Numeric)
    hoehe = Column('hoehe', Numeric)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Numeric)
    fluss = Column('fluss', Unicode)
    m_beginn = Column('m_beginn', Unicode)
    m_ende = Column('m_ende', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-hochwassergrenzwertpegel', Hochwassergrenzwertpegel)


class AtlasKantonaleMessstationen(Base, Vector):
    __tablename__ = 'hydro_atlas_kant_messstationen'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_kantonale-messstationen'
    __template__ = 'templates/htmlpopup/atlas_kantonale_messstationen.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    nummer = Column('nummer', Unicode)
    datenherkunft = Column('datenherkunft', Unicode)
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
    __template__ = 'templates/htmlpopup/daueruntersuchung_fliessgewaesser.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    rechtswert = Column('rechtswert', Unicode)
    hochwert = Column('hochwert', Unicode)
    hoehe = Column('hoehe', Unicode)
    betriebsbeginn = Column('betriebsbeginn', Unicode)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Unicode)
    mittlerehoehe = Column('mittlerehoehe', Unicode)
    vergletscherung = Column('vergletscherung', Unicode)
    stationierung = Column('stationierung', Unicode)
    flussgebiet = Column('flussgebiet', Unicode)
    hyperlink_d = Column('hyperlink_d', Unicode)
    hyperlink_f = Column('hyperlink_f', Unicode)
    hyperlink_daten = Column('hyperlink_daten', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-daueruntersuchung_fliessgewaesser', Daueruntersuchung_fliessgewaesser)


class Vec25Seen(Base, Vector):
    __tablename__ = 'seen'
    __table_args__ = ({'schema': 'vec25', 'autoload': False})
    __bodId__ = 'ch.bafu.vec25-seen'
    __template__ = 'templates/htmlpopup/vec25_seen.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
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
    gwlnr = Column('gwlnr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.vec25-seen', Vec25Seen)


class HydroAtlasFlussgebiete(Base, Vector):
    __tablename__ = 'atlas_flussgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_flussgebiete'
    __template__ = 'templates/htmlpopup/atlas_flussgebiete.mako'
    __label__ = 'flussgb'
    __returnedGeometry__ = 'the_geom_simple'
    id = Column('bgdi_id', Integer, primary_key=True)
    flussgb = Column('flussgb', Unicode)
    flaeche = Column('flaeche', Numeric)
    the_geom = Column(Geometry2D)
    the_geom_simple = Column('the_geom_simple', Geometry2D)

register('ch.bafu.hydrologischer-atlas_flussgebiete', HydroAtlasFlussgebiete)


class HydroAtlasBilanzgebiete(Base, Vector):
    __tablename__ = 'atlas_bilanzgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_bilanzgebiete'
    __template__ = 'templates/htmlpopup/atlas_bilanzgebiete.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    nummer = Column('nummer', Integer)
    flussgebiet = Column('flussgebiet', Integer)
    shape_area = Column('shape_area', Numeric)
    umfang = Column('umfang', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologischer-atlas_bilanzgebiete', HydroAtlasBilanzgebiete)


class HydroAtlasBasisgebiete(Base, Vector):
    __tablename__ = 'atlas_basisgebiete'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologischer-atlas_basisgebiete'
    __template__ = 'templates/htmlpopup/atlas_basisgebiete.mako'
    __extended_info__ = True
    __label__ = 'nummer'
    id = Column('bgdi_id', Integer, primary_key=True)
    nummer = Column('nummer', Integer)
    gebietskennzahl = Column('gebietskennzahl', Integer)
    bemerkung = Column('bemerkung', Unicode)
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

register('ch.bafu.hydrologischer-atlas_basisgebiete', HydroAtlasBasisgebiete)


class Niedrigwasserstatistik(Base, Vector):
    __tablename__ = 'niedrigwasserstatistik'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-niedrigwasserstatistik'
    __template__ = 'templates/htmlpopup/niedrigwasserstatistik.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    url_nqpdf = Column('url_nqpdf', Unicode)
    hyperlink_de = Column('hyperlink_d', Unicode)
    hyperlink_fr = Column('hyperlink_f', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-niedrigwasserstatistik', Niedrigwasserstatistik)


class TypFliessgewaesser(Base, Vector):
    __tablename__ = 'typisierung_fliessgewaesser'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.typisierung-fliessgewaesser'
    __template__ = 'templates/htmlpopup/fliessgewaesser_typ.mako'
    __extended_info__ = True
    __label__ = 'objectid_gwn25'
    id = Column('bgdi_id', Integer, primary_key=True)
    gewaessertyp = Column('gewaessertyp', Integer)
    grosserfluss = Column('grosserfluss', Unicode)
    objectid_gwn25 = Column('objectid_gwn25', Integer)
    biogeo = Column('biogeo', Unicode)
    hoehe = Column('hoehe', Unicode)
    abfluss = Column('abfluss', Unicode)
    gefaelle = Column('gefaelle', Unicode)
    geo = Column('geo', Unicode)
    code = Column('code', Integer)
    objectid_gwn25 = Column('objectid_gwn25', Integer)
    aehnlichkeit = Column('aehnlichkeit', Integer)
    shape_length = Column('shape_length', Numeric)
    url_portraits = Column('url_portraits', Unicode)
    url_uebersicht_de = Column('url_uebersicht_de', Unicode)
    url_uebersicht_fr = Column('url_uebersicht_fr', Unicode)
    name = Column('name', Unicode)
    discharge = Column('discharge', Numeric)
    discharge_source = Column('discharge_source', Unicode)
    discharge_quality = Column('discharge_quality', Integer)
    slope = Column('slope', Numeric)
    slope_quality = Column('slope_quality', Integer)
    ibchqregim = Column('ibchqregim', Integer)
    ibch_corr = Column('ibch_corr', Integer)
    quali_d = Column('quali_d', Integer)
    quali_f = Column('quali_f', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.typisierung-fliessgewaesser', TypFliessgewaesser)


class WasserVermessungsstrecken(Base, Vector):
    __tablename__ = 'vermessungsabschnitte'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasserbau-vermessungsstrecken'
    __template__ = 'templates/htmlpopup/vermessungsstrecken.mako'
    __label__ = 'gwlnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    verantwortung = Column('verantwortung', Unicode)
    gwlnr = Column('gwlnr', Unicode)
    flussname = Column('flussname', Unicode)
    abschnitt = Column('abschnitt', Unicode)
    gerinnetyp = Column('gerinnetyp', Unicode)
    uebersicht_messkampagne_link = Column('uebersicht_messkampagne_link', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasserbau-vermessungsstrecken', WasserVermessungsstrecken)


class MittlereAbfluesse(Base, Vector):
    __tablename__ = 'mittlere_abfluesse'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.mittlere-abfluesse'
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
    regimetyp = Column('regimetyp', Unicode)
    regimenummer = Column('regimenummer', Integer)
    abflussvar = Column('abflussvar', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.mittlere-abfluesse', MittlereAbfluesse)


class MittlereAbfluesseZukunft(Base, Vector):
    __tablename__ = 'mittlere_abfluesse_zukunft'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.mittlere-abfluesse_zukunft'
    __template__ = 'templates/htmlpopup/mittlere_abfluesse_zukunft.mako'
    __label__ = 'place'
    id = Column('bgdi_id', Integer, primary_key=True)
    place = Column('place', Unicode)
    water_name = Column('water_name', Unicode)
    area = Column('area', Numeric)
    ezgheight = Column('ezgheight', Numeric)
    glacier = Column('glacier', Numeric)
    url = Column('url', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.mittlere-abfluesse_zukunft', MittlereAbfluesseZukunft)


class WasserbauQuerprofilmarken(Base, Vector):
    __tablename__ = 'querprofilmarken'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasserbau-querprofilmarken'
    __template__ = 'templates/htmlpopup/querprofilmarken.mako'
    __extended_info__ = True
    __label__ = 'gwlnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    gwlnr = Column('gwlnr', Unicode)
    flussname = Column('flussname', Unicode)
    abschnitt = Column('abschnitt', Unicode)
    gewiss_adr = Column('gewiss_adr', Integer)
    bww_km = Column('bww_km', Numeric)
    lokale_km = Column('lokale_km', Numeric)
    datum = Column('datum', Unicode)
    markierung_li = Column('markierung_li', Unicode)
    e_li = Column('e_li', Numeric)
    n_li = Column('n_li', Numeric)
    hoehe_li = Column('hoehe_li', Numeric)
    azimut_li = Column('azimut_li', Numeric)
    foto_1_li = Column('foto_1_li', Unicode)
    foto_2_li = Column('foto_2_li', Unicode)
    markierung_re = Column('markierung_re', Unicode)
    e_re = Column('e_re', Numeric)
    n_re = Column('n_re', Numeric)
    hoehe_re = Column('hoehe_re', Numeric)
    azimut_re = Column('azimut_re', Numeric)
    foto_1_re = Column('foto_1_re', Unicode)
    foto_2_re = Column('foto_2_re', Unicode)
    markierung_li_desc_de = Column('markierung_li_desc_de', Unicode)
    markierung_li_desc_fr = Column('markierung_li_desc_fr', Unicode)
    markierung_li_desc_it = Column('markierung_li_desc_it', Unicode)
    markierung_re_desc_de = Column('markierung_re_desc_de', Unicode)
    markierung_re_desc_fr = Column('markierung_re_desc_fr', Unicode)
    markierung_re_desc_it = Column('markierung_re_desc_it', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasserbau-querprofilmarken', WasserbauQuerprofilmarken)


class FeststoffeGeschiebemessnetz(Base, Vector):
    __tablename__ = 'geschiebemessnetz'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.feststoffe-geschiebemessnetz'
    __template__ = 'templates/htmlpopup/geschiebemessnetz.mako'
    __extended_info__ = True
    __label__ = 'fluss'
    id = Column('bgdi_id', Integer, primary_key=True)
    rechtswert = Column('rechtswert', Integer)
    hochwert = Column('hochwert', Unicode)
    gsch_n = Column('gsch_n', Numeric)
    lk = Column('lk', Numeric)
    lage = Column('lage', Integer)
    fn = Column('fn', Numeric)
    hmax = Column('hmax', Numeric)
    hmin = Column('hmin', Numeric)
    hmed = Column('hmed', Numeric)
    exp = Column('exp', Unicode)
    form = Column('form', Numeric)
    geologie = Column('geologie', Unicode)
    platz = Column('platz', Unicode)
    fluss = Column('fluss', Unicode)
    station = Column('station', Unicode)
    institut = Column('institut', Unicode)
    amt = Column('amt', Unicode)
    abteilung = Column('abteilung', Unicode)
    sektion = Column('sektion', Unicode)
    kontakt_name = Column('kontakt_name', Unicode)
    strasse = Column('strasse', Unicode)
    plz = Column('plz', Unicode)
    ort = Column('ort', Unicode)
    sachbearb = Column('sachbearb', Unicode)
    telephon = Column('telephon', Unicode)
    fax = Column('fax', Unicode)
    emailadresse1 = Column('emailadresse1', Unicode)
    emailadresse2 = Column('emailadresse2', Unicode)
    pdf_file = Column('pdf_file', Unicode)
    lage_de = Column('lage_de', Unicode)
    lage_fr = Column('lage_fr', Unicode)
    platz_de = Column('platz_de', Unicode)
    platz_fr = Column('platz_fr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.feststoffe-geschiebemessnetz', FeststoffeGeschiebemessnetz)


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


class HydroQ347(Base, Vector):
    __tablename__ = 'hydro_q347'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-q347'
    __template__ = 'templates/htmlpopup/hydro_q347.mako'
    __extended_info__ = True
    __label__ = 'gewaesser'
    id = Column('bgdi_id', Integer, primary_key=True)
    gewaesser = Column('gewaesser', Unicode)
    bilanzid = Column('bilanzid', Unicode)
    id_q347 = Column('id', Integer)
    basisid = Column('basisid', Unicode)
    lhg = Column('lhg', Unicode)
    gewaesser = Column('gewaesser', Unicode)
    flaeche = Column('flaeche', Numeric)
    q_84_93 = Column('q_84_93', Numeric)
    qp = Column('qp', Numeric)
    p = Column('p', Unicode)
    qmod = Column('qmod', Numeric)
    bemerkung = Column('bemerkung', Unicode)
    symbolisierung = Column('symbolisierung', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-q347', HydroQ347)


class HugStationen(Base, Vector):
    __tablename__ = 'hydrologie_untersuchungsgebiete_stationen'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-untersuchungsgebiete_stationen'
    __template__ = 'templates/htmlpopup/hug_stationen.mako'
    __label__ = 'name'
    id = Column('geodb_oid', Integer, primary_key=True)
    name = Column('name', Unicode)
    hochwert = Column('hochwert', Integer)
    rechtswert = Column('rechtswert', Integer)
    hoehe = Column('hoehe', Integer)
    betriebsbeginn = Column('betriebsbeginn', Integer)
    einzugsgebietsflaeche = Column('einzugsgebietsflaeche', Numeric)
    flussgebiet = Column('flussgebiet', Unicode)
    hyperlink_f = Column('hyperlink_f', Unicode)
    hyperlink_d = Column('hyperlink_d', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-untersuchungsgebiete_stationen', HugStationen)


class Hintergrundkarte(Base, Vector):
    __tablename__ = 'hydrologie_hintergrundkarte'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hintergrundkarte'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-hintergrundkarte', Hintergrundkarte)


class StrukturgueteHochrheinLinkesufer(Base, Vector):
    __tablename__ = 'strukturguete_hochrhein'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.strukturguete-hochrhein_linkesufer'
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Unicode)
    lumfeld = Column('l_umfeld', Integer)
    rumfeld = Column('r_umfeld', Integer)
    lufer = Column('l_ufer', Integer)
    rufer = Column('r_ufer', Integer)
    sohle = Column('sohle', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.strukturguete-hochrhein_linkesufer', StrukturgueteHochrheinLinkesufer)


class StrukturgueteHochrheinLinkesumfeld(Base, Vector):
    __tablename__ = 'strukturguete_hochrhein'
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.strukturguete-hochrhein_linkesumfeld'
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Unicode)
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
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Unicode)
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
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Unicode)
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
    __template__ = 'templates/htmlpopup/strukturguete_hochrhein.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenherkunft = Column('datenherkunft', Unicode)
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
    __template__ = 'templates/htmlpopup/gewaesserschutz_badewasserqualitaet.mako'
    __extended_info__ = True
    __label__ = 'bwname'
    id = Column('bwid', Unicode, primary_key=True, nullable=False)
    bwname = Column('bwname', Unicode, nullable=False)
    groupid = Column('groupid', Unicode, nullable=True)
    nwunitname = Column('nwunitname', Unicode, nullable=False)
    gemeinde = Column('gemeinde', Unicode, nullable=False)
    canton = Column('canton', Unicode, nullable=False)
    bwatercat = Column('bwatercat', Unicode, nullable=False)
    url = Column('url', Unicode, nullable=True)
    baquaimg = Column('baquaimg', Unicode, nullable=True)
    year_bw = Column('year_bw', Integer, nullable=False)
    qualitaet = Column('qualitaet', Unicode, nullable=False)
    the_geom = Column(Geometry2D)

register('ch.bafu.gewaesserschutz-badewasserqualitaet', GewaesserschutzBadewasserqualitaet)


class AmG(Base, Vector):
    __tablename__ = 'amphibien_wanderobjekte'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien_wanderobjekte'
    __template__ = 'templates/htmlpopup/bundinv_amphibien_w.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Unicode)
    name = Column('name', Unicode)
    refobjblat = Column('refobjblat', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien_wanderobjekte', AmG)


class AmL(Base, Vector):
    __tablename__ = 'amphibien'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien'
    __template__ = 'templates/htmlpopup/bundinv_amphibien.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Unicode)
    name = Column('name', Unicode)
    refobjblat = Column('refobjblat', Unicode)
    shape_area = Column('shape_area', Numeric)
    site = Column('site', Unicode)
    site_de = Column('site_de', Unicode)
    site_fr = Column('site_fr', Unicode)
    site_it = Column('site_it', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien', AmL)


class Lhg(Base, Vector):
    __tablename__ = 'lhg'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hydromessstationen'
    __template__ = 'templates/htmlpopup/hydromessstationen.mako'
    __label__ = 'lhg_name'
    __returnedGeometry__ = 'the_geom_highlight'
    id = Column('edv_nr4', Integer, primary_key=True)
    lhg_name = Column('lhg_name', Unicode)
    the_geom = Column(Geometry2D)
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bafu.hydrologie-hydromessstationen', Lhg)


class Temperaturmessnetz(Base, Vector):
    __tablename__ = 'temperaturmessnetz'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-wassertemperaturmessstationen'
    __template__ = 'templates/htmlpopup/temperaturmessnetz.mako'
    __label__ = 'name'
    id = Column('nr', Integer, primary_key=True)
    url = Column('url', Unicode)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-wassertemperaturmessstationen', Temperaturmessnetz)


class GewaesserschutzTemplate:
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/klaeranlagen.mako'
    __extended_info__ = True
    __label__ = 'name'
    id = Column('nummer', Integer, primary_key=True)
    name = Column('name', Unicode)
    rechtswert = Column('rechtswert', Integer)
    hochwert = Column('hochwert', Integer)
    hoehe = Column('hoehe', Integer)
    adresse = Column('adresse', Unicode)
    plz = Column('plz', Integer)
    ort = Column('ort', Unicode)
    tel_nr = Column('tel_nr', Unicode)
    vorfluterbez = Column('vorfluterbez', Unicode)
    name_vorfluter = Column('name_vorfluter', Unicode)
    gewiss_nr = Column('gewiss_nr', Integer)
    reinigungstyp = Column('reinigungstyp', Unicode)
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
    nh4_n_ganzjaehrig = Column('nh4_n_ganzjaehrig', Unicode)
    nanteil = Column('nanteil', Integer)
    nabsolut = Column('nabsolut', Integer)
    n_abwassertemperatur = Column('n_abwassertemperatur', Integer)
    gesamtpanteil = Column('gesamtpanteil', Integer)
    gesamtpabsolut = Column('gesamtpabsolut', Numeric)
    gesamt_ungel_stoffe_absolut = Column('gesamt_ungel_stoffe_absolut', Integer)
    andere_stoffe = Column('andere_stoffe', Unicode)
    kanton = Column('kanton', Unicode)
    vsa_kategorie = Column('vsa_kategorie', Unicode)
    ausbaugroesse_egw = Column('ausbaugroesse_egw', Integer)
    anzahl_nat_einwohner = Column('anzahl_nat_einwohner', Integer)
    jahr_nat_einwohner = Column('jahr_nat_einwohner', Integer)
    abwasseranteil_q347 = Column('abwasseranteil_q347', Numeric)
    gwlnr = Column('gwlnr', Unicode)
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


class GrundwasserkoerperBase:
    __table_args__ = ({'schema': 'wasser', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.grundwasserkoerper'
    __template__ = 'templates/htmlpopup/grundwasserkoerper.mako'
    __label__ = 'gwkname'
    id = Column('bgdi_id', Integer, primary_key=True)
    gwkid = Column('gwkid', Unicode)
    gwkname = Column('gwkname', Unicode)
    flussgebiet = Column('flussgebiet', Unicode)
    grundwasserleitertyp = Column('grundwasserleitertyp', Unicode)
    naturraum = Column('naturraum', Unicode)
    grundwasserregime = Column('grundwasserregime', Unicode)
    area = Column('area', Unicode)


class GrundwasserkoerperGen(Base, GrundwasserkoerperBase, Vector):
    __tablename__ = 'gwk'
    __minscale__ = 0
    __maxscale__ = 100000
    the_geom = Column('the_geom_gen', Geometry2D)


class Grundwasserkoerper(Base, GrundwasserkoerperBase, Vector):
    __tablename__ = 'gwk'
    __minscale__ = 100001
    the_geom = Column(Geometry2D)

register('ch.bafu.grundwasserkoerper', GrundwasserkoerperGen)
register('ch.bafu.grundwasserkoerper', Grundwasserkoerper)


class Vorfluter (Base, Vector):
    __tablename__ = 'effluent'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-vorfluter'
    __template__ = 'templates/htmlpopup/vorfluter.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    id_2 = Column('id', Integer)
    ezgnr = Column('ezgnr', Integer)
    gwlnr = Column('gwlnr', Unicode)
    unteresende = Column('unteresende', Integer)
    oberesende = Column('oberesende', Integer)
    gewaessername = Column('gewaessername', Unicode)
    de_nebenarm = Column('de_nebenarm', Unicode)
    fr_nebenarm = Column('fr_nebenarm', Unicode)
    it_nebenarm = Column('it_nebenarm', Unicode)
    en_nebenarm = Column('en_nebenarm', Unicode)
    rm_nebenarm = Column('rm_nebenarm', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-vorfluter', Vorfluter)


class Gewaesserzustandst (Base, Vector):
    __tablename__ = 'dbgz'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-gewaesserzustandsmessstationen'
    __template__ = 'templates/htmlpopup/gewaesserzustandsmessstationen.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    nr = Column('nr', Numeric)
    gewaesser = Column('gewaesser', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-gewaesserzustandsmessstationen', Gewaesserzustandst)


class Teileinzugsgebiete2 (Base, Vector):
    __tablename__ = 'teileinzugsgebiete_2_full'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-teileinzugsgebiete_2'
    __template__ = 'templates/htmlpopup/teileinzugsgebiete2.mako'
    __returnedGeometry__ = 'the_geom_ext'
    __label__ = 'id'
    __extended_info__ = True
    id = Column('ezgnr', Integer, primary_key=True)
    gewaessername = Column('gewaessername', Unicode)
    gesamtflaeche = Column('gesamtflaeche', Float)
    de_nebenarm = Column('de_nebenarm', Unicode)
    fr_nebenarm = Column('fr_nebenarm', Unicode)
    it_nebenarm = Column('it_nebenarm', Unicode)
    en_nebenarm = Column('en_nebenarm', Unicode)
    rm_nebenarm = Column('rm_nebenarm', Unicode)
    min_z = Column('min_z', Float)
    max_z = Column('max_z', Float)
    mean_z = Column('mean_z', Float)
    anteil_ch = Column('anteil_ch', Float)
    as_siedlungsflaechen = Column('as_siedlungsflaechen', Float)
    as_landwirtschaftsflaechen = Column('as_landwirtschaftsflaechen', Float)
    as_bestockteflaechen = Column('as_bestockteflaechen', Float)
    as_unproduktiveflaechen = Column('as_unproduktiveflaechen', Float)
    clc_bebauteflaechen = Column('clc_bebauteflaechen', Float)
    clc_landwirtschaft = Column('clc_landwirtschaft', Float)
    clc_waelder = Column('clc_waelder', Float)
    clc_feuchtflaechen = Column('clc_feuchtflaechen', Float)
    clc_wasserflaechen = Column('clc_wasserflaechen', Float)
    the_geom = Column(Geometry2D)
    the_geom_ext = Column('the_geom_ext', Geometry2D)

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
    __tablename__ = 'gebietsauslaesse'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-gebietsauslaesse'
    __template__ = 'templates/htmlpopup/gebietsauslaesse.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    id_2 = Column('id', Integer)
    ezgnr = Column('ezgnr', Integer)
    gwlnr = Column('gwlnr', Unicode)
    gewaessername = Column('gewaessername', Unicode)
    adresse = Column('adresse', Integer)
    de_nebenarm = Column('de_nebenarm', Unicode)
    fr_nebenarm = Column('fr_nebenarm', Unicode)
    it_nebenarm = Column('it_nebenarm', Unicode)
    rm_nebenarm = Column('rm_nebenarm', Unicode)
    en_nebenarm = Column('en_nebenarm', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-gebietsauslaesse', Gebietsauslaesse)


class AU(Base, Vector):
    __tablename__ = 'auen'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-auen'
    __template__ = 'templates/htmlpopup/auen.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Integer)
    refobjblat = Column('refobjblat', Unicode)
    auen_type = Column('auen_type', Integer)
    auen_type_de = Column('auen_type_de', Unicode)
    auen_type_fr = Column('auen_type_fr', Unicode)
    auen_type_it = Column('auen_type_it', Unicode)
    shape_area = Column('shape_area', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-auen', AU)


class AU_A2(Base, Vector):
    __tablename__ = 'auen_anhang2'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-auen_anhang2'
    __template__ = 'templates/htmlpopup/auen_anhang2.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Integer)
    refobjblat = Column('refobjblat', Unicode)
    auen_type = Column('typ', Integer)
    auen_type_de = Column('typ_de', Unicode)
    auen_type_fr = Column('typ_fr', Unicode)
    auen_type_it = Column('typ_it', Unicode)
    shape_area = Column('area', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-auen_anhang2', AU_A2)


class AuenVegetationAlpin(Base, Vector):
    __tablename__ = 'auen_vegetation_alpin'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-auen_vegetation_alpin'
    __template__ = 'templates/htmlpopup/auen_vegetation_alpin.mako'
    __label__ = 'objname'
    id = Column('bgdi_id', Integer, primary_key=True)
    objname = Column('objname', Unicode)
    objnummer = Column('objnummer', Integer)
    refobjblat = Column('refobjblat', Unicode)
    vegetation = Column('vegetation', Integer)
    vegetation_de = Column('devegetati', Unicode)
    vegetation_fr = Column('frvegetati', Unicode)
    vegetation_it = Column('itvegetati', Unicode)
    conflict = Column('konfliktpo', Integer)
    conflict_de = Column('dekonflikt', Unicode)
    conflict_fr = Column('frkonflikt', Unicode)
    conflict_it = Column('itkonflikt', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-auen_vegetation_alpin', AuenVegetationAlpin)


class AuenAusserhalbBundesinventar(Base, Vector):
    __tablename__ = 'auen_ausserhalb_bundinv'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.auen-ausserhalb_bundesinventar'
    __template__ = 'templates/htmlpopup/auen_ausserhalb_bundinv.mako'
    __label__ = 'name'
    id = Column('objnummer', Integer, primary_key=True)
    name = Column('name', Unicode)
    de_bedeutung = Column('de_bedeutung', Unicode)
    fr_bedeutung = Column('fr_bedeutung', Unicode)
    it_bedeutung = Column('it_bedeutung', Unicode)
    de_qualitaet = Column('de_qualitaet', Unicode)
    fr_qualitaet = Column('fr_qualitaet', Unicode)
    shape_area = Column('shape_area', Integer)
    the_geom = Column(Geometry2D)

register(AuenAusserhalbBundesinventar.__bodId__, AuenAusserhalbBundesinventar)


class AlpinAuenAusserhalbBundesinventar(Base, Vector):
    __tablename__ = 'alpinauen'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.auen-ausserhalb_bundesinventar_alpin'
    __template__ = 'templates/htmlpopup/auen_ausserhalb_bundinv_alpin.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Integer)
    name = Column('name', Unicode)
    de_biobedeutung = Column('de_biobedeutung', Unicode)
    fr_biobedeutung = Column('fr_biobedeutung', Unicode)
    it_biobedeutung = Column('it_biobedeutung', Unicode)
    de_geobedeutung = Column('de_geobedeutung', Unicode)
    fr_geobedeutung = Column('fr_geobedeutung', Unicode)
    it_geobedeutung = Column('it_geobedeutung', Unicode)
    de_qualitaet = Column('de_qualitaet', Unicode)
    fr_qualitaet = Column('fr_qualitaet', Unicode)
    it_qualitaet = Column('it_qualitaet', Unicode)
    auentyp = Column('auentyp', Unicode)
    shape_area = Column('shape_area', Integer)
    the_geom = Column(Geometry2D)

register(AlpinAuenAusserhalbBundesinventar.__bodId__, AlpinAuenAusserhalbBundesinventar)


class AuenVegetationsKarten(Base, Vector):
    __tablename__ = 'auen_vegetationskarte'
    __table_args__ = ({'schema': 'flora', 'autoload': False})
    __bodId__ = 'ch.bafu.auen-vegetationskarten'
    __template__ = 'templates/htmlpopup/auen_veg.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    obj_nummer = Column('obj_nummer', Integer)
    kartierjahr = Column('kartierjahr', Integer)
    primaervegetation_de = Column('primaervegetation_de', Unicode)
    primaervegetation_fr = Column('primaervegetation_fr', Unicode)
    primaervegetation_it = Column('primaervegetation_it', Unicode)
    code_primaervegetation = Column('code_primaervegetation', Unicode)
    ref_obj_blatt = Column('ref_obj_blatt', Unicode)
    area_ha = Column('area_ha', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.auen-vegetationskarten', AuenVegetationsKarten)


class BLN(Base, Vector):
    __tablename__ = 'bln_v2'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-bln'
    __template__ = 'templates/htmlpopup/bln.mako'
    __label__ = 'bln_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    bln_name = Column('bln_name', Unicode)
    bln_obj = Column('bln_obj', Integer)
    bln_fl = Column('bln_fl', Numeric)
    subareanumber = Column('subareanumber', Integer)
    subareaname = Column('subareaname', Unicode)
    linkurldescription = Column('linkurldescription', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-bln', BLN)


class HM(Base, Vector):
    __tablename__ = 'hochmoore'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-hochmoore'
    __template__ = 'templates/htmlpopup/hochmoore.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Integer)
    shape_area = Column('shape_area', Numeric)
    hm_ke = Column('hm_ke', Integer)
    unit_de = Column('unit_de', Unicode)
    unit_fr = Column('unit_fr', Unicode)
    unit_it = Column('unit_it', Unicode)
    hochmoore_type_de = Column('hochmoore_type_de', Unicode)
    hochmoore_type_fr = Column('hochmoore_type_fr', Unicode)
    hochmoore_type_it = Column('hochmoore_type_it', Unicode)
    refobjblat = Column('refobjblat', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-hochmoore', HM)


class JB(Base, Vector):
    __tablename__ = 'jb'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-jagdbanngebiete'
    __template__ = 'templates/htmlpopup/jb.mako'
    __label__ = 'jb_name'  # Composite labels
    id = Column('gid', Integer, primary_key=True)
    jb_name = Column('jb_name', Unicode)
    jb_obj = Column('jb_obj', Integer)
    jb_kat = Column('jb_kat', Unicode)
    jb_fl = Column('jb_fl', Numeric)
    jb_gf = Column('jb_gf', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-jagdbanngebiete', JB)


class ML(Base, Vector):
    __tablename__ = 'moorlandschaften'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-moorlandschaften'
    __template__ = 'templates/htmlpopup/moorlandschaften.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Unicode)
    shape_area = Column('shape_area', Unicode)
    refobjblat = Column('refobjblat', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-moorlandschaften', ML)


class WV(Base, Vector):
    __tablename__ = 'vogelreservate'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-vogelreservate'
    __template__ = 'templates/htmlpopup/vogelreservate.mako'
    __label__ = 'name'
    id = Column('objectid', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Integer)
    teilgebiet = Column('teilgebiet', Unicode)
    schutzkategorie_de = Column('schutzkategorie_de', Unicode)
    schutzkategorie_fr = Column('schutzkategorie_fr', Unicode)
    schutzkategorie_it = Column('schutzkategorie_it', Unicode)
    schutzebene_de = Column('schutzebene_de', Unicode)
    schutzebene_fr = Column('schutzebene_fr', Unicode)
    schutzebene_it = Column('schutzebene_it', Unicode)
    refobjblatt = Column('refobjblatt', Unicode)
    shape_area = Column('shape_area', Numeric)
    obj_gisflaeche = Column('obj_gisflaeche', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-vogelreservate', WV)


class WasserentnahmeAll(Base, Vector):
    __tablename__ = 'entnahme'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-entnahme'
    __template__ = 'templates/htmlpopup/wasserentnahme.mako'
    __label__ = 'rwknr'
    id = Column('gid', Integer, primary_key=True)
    rwknr = Column('rwknr', Unicode)
    kanton = Column('kanton', Unicode)
    kantoncode = Column('kantoncode', Unicode)
    ent_gew = Column('ent_gew', Unicode)
    link = Column('link', Unicode)
    link_de = Column('link_de', Unicode)
    link_fr = Column('link_fr', Unicode)
    link_it = Column('link_it', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-entnahme', WasserentnahmeAll)


class Wasserleitungen(Base, Vector):
    __tablename__ = 'leitungen'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-leitungen'
    __template__ = 'templates/htmlpopup/wasserleitungen.mako'
    __label__ = 'rwknr'
    id = Column('gid', Integer, primary_key=True)
    kanton = Column('kanton', Unicode)
    kantoncode = Column('kantoncode', Unicode)
    rwknr = Column('rwknr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-leitungen', Wasserleitungen)


class Wasserrueckgabe(Base, Vector):
    __tablename__ = 'rueckgabe'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.wasser-rueckgabe'
    __template__ = 'templates/htmlpopup/wasserrueckgabe.mako'
    __label__ = 'rwknr'
    id = Column('gid', Integer, primary_key=True)
    kanton = Column('kanton', Unicode)
    kantoncode = Column('kantoncode', Unicode)
    rwknr = Column('rwknr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wasser-rueckgabe', Wasserrueckgabe)


class Flachmoore(Base, Vector):
    __tablename__ = 'flachmoore'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-flachmoore'
    __template__ = 'templates/htmlpopup/flachmoore.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Unicode)
    refobjblat = Column('refobjblat', Unicode)
    shape_area = Column('shape_area', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-flachmoore', Flachmoore)


class SchutzgebieteAulav:
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_std.mako'
    __maxscale__ = 10000
    id = Column('bgdi_id', Integer, primary_key=True)
    key_obj = Column('objnummer', Integer)
    key_name = Column('name', Unicode)
    typ = Column('discriminator', Unicode)
    the_geom = Column(Geometry2D)


class SchutzgebieteAulavAuen(Base, SchutzgebieteAulav, Vector):
    __tablename__ = 'auen_gebiete'
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_auen'

register('ch.bafu.schutzgebiete-aulav_auen', SchutzgebieteAulavAuen)


class SchutzgebieteAulavJagdbanngebiete(Base, SchutzgebieteAulav, Vector):
    __tablename__ = 'jagdbann_gebiete'
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_jagdbanngebiete'

register('ch.bafu.schutzgebiete-aulav_jagdbanngebiete', SchutzgebieteAulavJagdbanngebiete)


class SchutzgebieteAulavMoorlandschaften(Base, SchutzgebieteAulav, Vector):
    __tablename__ = 'moor_landschaften'
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_moorlandschaften'

register('ch.bafu.schutzgebiete-aulav_moorlandschaften', SchutzgebieteAulavMoorlandschaften)


class SchutzgebieteAulavUebrige(Base, SchutzgebieteAulav, Vector):
    __tablename__ = 'uebrigegebiete'
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_uebrige'

register('ch.bafu.schutzgebiete-aulav_uebrige', SchutzgebieteAulavUebrige)


class SchutzgebieteAulavAuenGeneral(Base, Vector):
    __tablename__ = 'auengebiete_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_auen'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_auen_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_auen', SchutzgebieteAulavAuenGeneral)


class SchutzgebieteAulavJagdbanngebieteGeneral(Base, Vector):
    __tablename__ = 'jagdbanngebiete_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_jagdbanngebiete'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_jagdbanngebiete_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_jagdbanngebiete', SchutzgebieteAulavJagdbanngebieteGeneral)


class SchutzgebieteAulavMoorlandschaftenGeneral(Base, Vector):
    __tablename__ = 'moorlandschaften_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_moorlandschaften'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_moorlandschaften_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_moorlandschaften', SchutzgebieteAulavMoorlandschaftenGeneral)


class SchutzgebieteAulavUebrigeGeneral(Base, Vector):
    __tablename__ = 'uebrige_gebiete_general'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-aulav_uebrige'
    __template__ = 'templates/htmlpopup/bafu_schutzge_aulav_uebrige_general.mako'
    __minscale__ = 10001
    __maxscale__ = 5000000
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-aulav_uebrige', SchutzgebieteAulavUebrigeGeneral)


class Paerke:
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __label__ = 'name'
    name = Column('park_name', Unicode)
    kategorie = Column('kategorie', Unicode)
    rechtsgrundlage = Column('rechtsgrundlage', Integer)
    status = Column('status', Unicode)
    the_geom = Column(Geometry2D)


class PaerkeNationalerBedeutung (Base, Paerke, Vector):
    __tablename__ = 'paerke_nationaler_bedeutung_zonen'
    __bodId__ = 'ch.bafu.schutzgebiete-paerke_nationaler_bedeutung'
    __template__ = 'templates/htmlpopup/paerke_nationaler_bedeutung.mako'
    id = Column('bgdi_id', Integer, primary_key=True)
    teil_nummer = Column('teil_nummer', Integer)
    objektnummer = Column('objektnummer', Integer)
    zone = Column('zone', Unicode)
    shape_area = Column('shape_area', Numeric)

register('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung', PaerkeNationalerBedeutung)


class PaerkeNationalerBedeutungPerimeter(Base, Paerke, Vector):
    __tablename__ = 'paerke_nationaler_bedeutung_perimeter'
    __bodId__ = 'ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter'
    __template__ = 'templates/htmlpopup/paerke_nationaler_bedeutung_perimeter.mako'
    id = Column('objektnummer', Integer, primary_key=True)
    shape_area = Column('shape_area', Numeric)

register('ch.bafu.schutzgebiete-paerke_nationaler_bedeutung_perimeter', PaerkeNationalerBedeutungPerimeter)


class Ramsar(Base, Vector):
    __tablename__ = 'ramsar'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-ramsar'
    __template__ = 'templates/htmlpopup/ramsar.mako'
    __label__ = 'ra_name'
    id = Column('ra_id', Integer, primary_key=True)
    ra_name = Column('ra_name', Unicode)
    ra_obj = Column('ra_obj', Integer)
    ra_fl = Column('ra_fl', Unicode)
    ra_gf = Column('ra_gf', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-ramsar', Ramsar)


class OekomAbschnitte(Base, Vector):
    __tablename__ = 'oekom_abschnitte'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.oekomorphologie-f_abschnitte'
    __template__ = 'templates/htmlpopup/oekom_abschnitte.mako'
    __extended_info__ = True
    __label__ = 'anfangsmass'
    id = Column('bgdi_id', Integer, primary_key=True)
    abschnr = Column('abschnr', Unicode)
    gsbreite = Column('gsbreite', Numeric)
    breitenvar_de = Column('breitenvar_de', Unicode)
    breitenvar_fr = Column('breitenvar_fr', Unicode)
    sohlver_de = Column('sohlver_de', Unicode)
    sohlver_fr = Column('sohlver_fr', Unicode)
    lufbebre = Column('lufbebre', Numeric)
    rufbebre = Column('rufbebre', Numeric)
    oekomklasse_de = Column('oekomklasse_de', Unicode)
    oekomklasse_fr = Column('oekomklasse_fr', Unicode)
    bemerkung = Column('bemerkung', Unicode)
    anfangsmass = Column('anfangsmass', Numeric)
    endmass = Column('endmass', Numeric)
    anfangsrechtswert = Column('anfangsrechtswert', Numeric)
    anfangshochwert = Column('anfangshochwert', Numeric)
    endrechtswert = Column('endrechtswert', Numeric)
    endhochwert = Column('endhochwert', Numeric)
    eindol_de = Column('eindol_de', Unicode)
    eindol_fr = Column('eindol_fr', Unicode)
    vnatabst_de = Column('vnatabst_de', Unicode)
    vnatabst_fr = Column('vnatabst_fr', Unicode)
    tiefenvar_de = Column('tiefenvar_de', Unicode)
    tiefenvar_fr = Column('tiefenvar_fr', Unicode)
    sohlmat = Column('sohlmat', Numeric)
    lbukver_de = Column('lbukver_de', Unicode)
    lbukver_fr = Column('lbukver_fr', Unicode)
    rbukver_de = Column('rbukver_de', Unicode)
    rbukver_fr = Column('rbukver_fr', Unicode)
    lbukmat_de = Column('lbukmat_de', Unicode)
    lbukmat_fr = Column('lbukmat_fr', Unicode)
    rbukmat_de = Column('rbukmat_de', Unicode)
    rbukmat_fr = Column('rbukmat_fr', Unicode)
    luferber_de = Column('luferber_de', Unicode)
    luferber_fr = Column('luferber_fr', Unicode)
    ruferber_de = Column('ruferber_de', Unicode)
    ruferber_fr = Column('ruferber_fr', Unicode)
    lufbebew_de = Column('lufbebew_de', Unicode)
    lufbebew_fr = Column('lufbebew_fr', Unicode)
    rufbebew_de = Column('rufbebew_de', Unicode)
    rufbebew_fr = Column('rufbebew_fr', Unicode)
    bewalgen_de = Column('bewalgen_de', Unicode)
    bewalgen_fr = Column('bewalgen_fr', Unicode)
    bewmakro_de = Column('bewmakro_de', Unicode)
    bewmakro_fr = Column('bewmakro_fr', Unicode)
    totholz_de = Column('totholz_de', Unicode)
    totholz_fr = Column('totholz_fr', Unicode)
    notizen = Column('notizen', Unicode)
    translid = Column('translid', Numeric)
    datum = Column('datum', Unicode)
    oekomklasse = Column('oekomklasse', Numeric)
    sohlmat_de = Column('sohlmat_de', Unicode)
    sohlmat_fr = Column('sohlmat_fr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.oekomorphologie-f_abschnitte', OekomAbschnitte)


class OekomAbstuerze(Base, Vector):
    __tablename__ = 'oekom_abstuerze'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.oekomorphologie-f_abstuerze'
    __template__ = 'templates/htmlpopup/oekom_abstuerze.mako'
    __extended_info__ = True
    __label__ = 'abstnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    abstnr = Column('abstnr', Unicode)
    absttyp_de = Column('absttyp_de', Unicode)
    absttyp_fr = Column('absttyp_fr', Unicode)
    abstmat_de = Column('abstmat_de', Unicode)
    abstmat_fr = Column('abstmat_fr', Unicode)
    absthoehe = Column('absthoehe', Numeric,)
    bemerkung = Column('bemerkung', Unicode)
    mass = Column('mass', Numeric,)
    rechtswert = Column('rechtswert', Numeric)
    hochwert = Column('hochwert', Numeric)
    abschnr = Column('abschnr', Unicode)
    notizen = Column('notizen', Unicode)
    translid = Column('translid', Numeric)
    loc_angle_geo = Column('loc_angle_geo', Numeric)
    datum = Column('datum', Unicode)
    absttyp = Column('absttyp', Numeric)
    abstmat = Column('abstmat', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.oekomorphologie-f_abstuerze', OekomAbstuerze)


class OekomBauwerke(Base, Vector):
    __tablename__ = 'oekom_bauwerke'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.oekomorphologie-f_bauwerke'
    __template__ = 'templates/htmlpopup/oekom_bauwerke.mako'
    __extended_info__ = True
    __label__ = 'bauwnr'
    id = Column('bgdi_id', Integer, primary_key=True)
    bauwnr = Column('bauwnr', Unicode)
    bauwtyp_de = Column('bauwtyp_de', Unicode)
    bauwtyp_fr = Column('bauwtyp_fr', Unicode)
    bauwhoehe = Column('bauwhoehe', Numeric)
    mass = Column('mass', Numeric)
    rechtswert = Column('rechtswert', Numeric)
    hochwert = Column('hochwert', Numeric)
    abschnr = Column('abschnr', Unicode)
    bemerkung = Column('bemerkung', Unicode)
    notizen = Column('notizen', Unicode)
    translid = Column('translid', Numeric)
    loc_angle_geo = Column('loc_angle_geo', Numeric)
    datum = Column('datum', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.oekomorphologie-f_bauwerke', OekomBauwerke)


class Steinbockkolonien(Base, Vector):
    __tablename__ = 'steinbockkolonien'
    __table_args__ = ({'schema': 'fauna', 'autoload': False})
    __bodId__ = 'ch.bafu.fauna-steinbockkolonien'
    __template__ = 'templates/htmlpopup/steinbockkolonien.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Integer)
    kantone = Column('kantone', Unicode)
    shape_area = Column('shape_area', Numeric)
    gebietstyp_de = Column('gebietstyp_de', Unicode)
    gebietstyp_fr = Column('gebietstyp_fr', Unicode)
    gebietstyp_it = Column('gebietstyp_it', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.fauna-steinbockkolonien', Steinbockkolonien)


class Swissprtr(Base, Vector):
    __tablename__ = 'swissprtr'
    __table_args__ = ({'schema': 'prtr', 'autoload': False})
    __bodId__ = 'ch.bafu.swissprtr'
    __template__ = 'templates/htmlpopup/swissprtr.mako'
    __label__ = 'betrieb'
    id = Column('prtrnr', Integer, primary_key=True)
    betrieb = Column('betrieb', Unicode)
    ort = Column('ort', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.swissprtr', Swissprtr)


class Nabel(Base, Vector):
    __tablename__ = 'nabel'
    __table_args__ = ({'schema': 'luft', 'autoload': False})
    __bodId__ = 'ch.bafu.nabelstationen'
    __template__ = 'templates/htmlpopup/nabel.mako'
    __label__ = 'name'
    id = Column('id_stat', Unicode, primary_key=True)
    name = Column('name', Unicode)
    typ_de = Column('typ_de', Unicode)
    typ_fr = Column('typ_fr', Unicode)
    desc_de = Column('desc_de', Unicode)
    desc_fr = Column('desc_fr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.nabelstationen', Nabel)


class Krebspest(Base, Vector):
    __tablename__ = 'krebspest'
    __table_args__ = ({'schema': 'fischerei', 'autoload': False})
    __bodId__ = 'ch.bafu.fischerei-krebspest'
    __template__ = 'templates/htmlpopup/krebspest.mako'
    __label__ = 'kennummer'
    id = Column('_count', Integer, primary_key=True)
    kennummer = Column('kennummer', Unicode)
    gewaesser = Column('gewaesser', Unicode)
    art_lat = Column('art_lat', Unicode)
    jahr = Column('jahr', Unicode)
    ort = Column('ort', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.fischerei-krebspest', Krebspest)


class Biogeoreg(Base, Vector):
    __tablename__ = 'biogeoreg'
    __table_args__ = ({'schema': 'diverse', 'autoload': False})
    __bodId__ = 'ch.bafu.biogeographische_regionen'
    __template__ = 'templates/htmlpopup/biogeoreg.mako'
    __label__ = 'regionname_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Integer)
    regionname_de = Column('regionname_de', Unicode)
    regionname_fr = Column('regionname_fr', Unicode)
    regionname_it = Column('regionname_it', Unicode)
    unterregionname_de = Column('unterregionname_de', Unicode)
    unterregionname_fr = Column('unterregionname_fr', Unicode)
    unterregionname_it = Column('unterregionname_it', Unicode)
    area = Column('area', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.biogeographische_regionen', Biogeoreg)


class Smaragd(Base, Vector):
    __tablename__ = 'smaragd'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.schutzgebiete-smaragd'
    __template__ = 'templates/htmlpopup/smaragd.mako'
    __label__ = 'em_name'
    id = Column('id', Integer, primary_key=True)
    em_name = Column('em_name', Unicode)
    em_obj = Column('em_obj', Numeric)
    em_gf = Column('em_gf', Numeric)
    the_geom = Column(Geometry2D)

register('ch.bafu.schutzgebiete-smaragd', Smaragd)


class Moose(Base, Vector):
    __tablename__ = 'mooseflora'
    __table_args__ = ({'schema': 'flora', 'autoload': False})
    __bodId__ = 'ch.bafu.moose'
    __template__ = 'templates/htmlpopup/moose.mako'
    __label__ = 'genus'
    id = Column('bgdi_id', Integer, primary_key=True)
    genus = Column('genus', Unicode)
    populationsnr = Column('populationsnr', Numeric)
    jahr = Column('jahr', Integer)
    standort = Column('standort', Unicode)
    rl_text = Column('rl_text', Unicode)
    nhv_text = Column('nhv_text', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.moose', Moose)


class Weltensutter(Base, Vector):
    __tablename__ = 'ws'
    __table_args__ = ({'schema': 'flora', 'autoload': False})
    __bodId__ = 'ch.bafu.flora-weltensutter_atlas'
    __template__ = 'templates/htmlpopup/weltensutter.mako'
    __label__ = 'nom'
    id = Column('gid', Integer, primary_key=True)
    nom = Column('nom', Unicode)
    no_surface = Column('no_surface', Numeric)
    ty_surface = Column('ty_surface', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.flora-weltensutter_atlas', Weltensutter)


class Histerdbeben(Base, Vector):
    __tablename__ = 'historische_erdbeben'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-historische_erdbeben'
    __template__ = 'templates/htmlpopup/histerdbeben.mako'
    __label__ = 'date_time'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Integer)
    epicentral = Column('epicentral', Unicode)
    intensity = Column('intensity', Unicode)
    magnitude = Column('magnitude', Numeric)
    date_time = Column('date_time', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.gefahren-historische_erdbeben', Histerdbeben)


class Spektral(Base, Vector):
    __tablename__ = 'baugrundkl_spectral'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-spektral'
    __template__ = 'templates/htmlpopup/spektral.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    spectral_3 = Column('spectral_3', Unicode)
    spectral_4 = Column('spectral_4', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.gefahren-spektral', Spektral)


class Trockenwiesenundweiden(Base, Vector):
    __tablename__ = 'trockenwiesen'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-trockenwiesen_trockenweiden'
    __template__ = 'templates/htmlpopup/trockenwiesenundweiden.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    refobjblat = Column('refobjblat', Unicode)
    shape_area = Column('shape_area', Numeric)
    objnummer = Column('objnummer', Integer)
    teilobjnummer = Column('teilobjnummer', Unicode)
    singularitaet = Column('singularitaet', Unicode)
    bewertung = Column('bewertungs', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-trockenwiesen_trockenweiden', Trockenwiesenundweiden)


class TrockenwiesenundweidenAnhang2(Base, Vector):
    __tablename__ = 'trockenwiesen_anhang2'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2'
    __template__ = 'templates/htmlpopup/tww_anhang2.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    objnummer = Column('objnummer', Integer)
    refobjblat = Column('refobjblat', Unicode)
    shape_area = Column('shape_area', Numeric)
    teilobjnummer = Column('teilobjnummer', Unicode)
    singularit = Column('singularit', Unicode)
    bewertung = Column('bewertungs', Integer)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-trockenwiesen_trockenweiden_anhang2', TrockenwiesenundweidenAnhang2)


class AmphibienAnhang4(Base, Vector):
    __tablename__ = 'amphibien_anhang4'
    __table_args__ = ({'schema': 'bundinv', 'autoload': False})
    __bodId__ = 'ch.bafu.bundesinventare-amphibien_anhang4'
    __template__ = 'templates/htmlpopup/amphibien_anhang4.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    obnr = Column('objnummer', Unicode)
    refobjblat = Column('refobjblat', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.bundesinventare-amphibien_anhang4', AmphibienAnhang4)


class Baugrundklassen(Base, Vector):
    __tablename__ = 'baugrundklassen'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-baugrundklassen'
    __template__ = 'templates/htmlpopup/baugrundklassen.mako'
    __label__ = 'bgk'
    __returnedGeometry__ = 'the_geom_highlight'
    id = Column('bgdi_id', Integer, primary_key=True)
    bgk = Column('bgk', Unicode)
    referenz = Column('referenz', Unicode)
    the_geom = Column(Geometry2D)
    the_geom_highlight = Column('the_geom_highlight', Geometry2D)

register('ch.bafu.gefahren-baugrundklassen', Baugrundklassen)


class Wrzselect(Base, Vector):
    __tablename__ = 'jgd_select_flaechen'
    __table_args__ = ({'schema': 'wrzportal', 'autoload': False})
    __bodId__ = 'ch.bafu.wrz-jagdbanngebiete_select'
    __template__ = 'templates/htmlpopup/wrz_select.mako'
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
    url_kanton = Column('url_kanton', Unicode)
    the_geom = Column(Geometry2D)


class WrzselectWege(Base, Vector):
    __tablename__ = 'jgd_select_wege'
    __table_args__ = ({'schema': 'wrzportal', 'autoload': False})
    __bodId__ = 'ch.bafu.wrz-jagdbanngebiete_select'
    __template__ = 'templates/htmlpopup/wrz_wege.mako'
    __label__ = 'weg_id'
    id = Column('bgdi_id', Integer, primary_key=True)
    weg_id = Column('weg_id', Integer)
    wegtyp_de = Column('wegtyp_de', Unicode)
    wegtyp_it = Column('wegtyp_it', Unicode)
    wegtyp_fr = Column('wegtyp_fr', Unicode)
    einschraenkungen = Column('einschraenkungen', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.wrz-jagdbanngebiete_select', WrzselectWege)
register('ch.bafu.wrz-jagdbanngebiete_select', Wrzselect)


class Wrzportal(Base, Vector):
    __tablename__ = 'wrz_portal_flaechen'
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
    url_kanton = Column('url_kanton', Unicode)
    the_geom = Column(Geometry2D)


class WrzportalWege(Base, Vector):
    __tablename__ = 'wrz_portal_wege'
    __table_args__ = ({'schema': 'wrzportal', 'autoload': False})
    __bodId__ = 'ch.bafu.wrz-wildruhezonen_portal'
    __template__ = 'templates/htmlpopup/wrz_wege.mako'
    __label__ = 'weg_id'
    id = Column('bgdi_id', Integer, primary_key=True)
    weg_id = Column('weg_id', Integer)
    wegtyp_de = Column('wegtyp_de', Unicode)
    wegtyp_it = Column('wegtyp_it', Unicode)
    wegtyp_fr = Column('wegtyp_fr', Unicode)
    einschraenkungen = Column('einschraenkungen', Unicode)
    the_geom = Column(Geometry2D)


register('ch.bafu.wrz-wildruhezonen_portal', WrzportalWege)
register('ch.bafu.wrz-wildruhezonen_portal', Wrzportal)


class Wildtier(Base, Vector):
    __tablename__ = 'wildtierkorridore_national'
    __table_args__ = ({'schema': 'fauna', 'autoload': False})
    __bodId__ = 'ch.bafu.fauna-wildtierkorridor_national'
    __template__ = 'templates/htmlpopup/wildtierkorridor.mako'
    __label__ = 'objnummer'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Unicode)
    name = Column('name', Unicode)
    zustand_de = Column('zustand_de', Unicode)
    zustand_fr = Column('zustand_fr', Unicode)
    zustand_it = Column('zustand_it', Unicode)
    ref_obj_blat = Column('ref_obj_blat', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.fauna-wildtierkorridor_national', Wildtier)


class Waldreservate(Base, Vector):
    __tablename__ = 'waldreservate'
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __template__ = 'templates/htmlpopup/bafu_waldreservate.mako'
    __bodId__ = 'ch.bafu.waldreservate'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    objnummer = Column('objnummer', Unicode)
    gisteilobjekt = Column('obj_gisteilobjekt', Float)
    name = Column('name', Unicode)
    gisflaeche = Column('obj_gisflaeche', Float)
    gesflaeche = Column('obj_gesflaeche', Float)
    mcpfe_class_de = Column('mcpfe_class_de', Unicode)
    mcpfe_class_fr = Column('mcpfe_class_fr', Unicode)
    mcpfe_class_it = Column('mcpfe_class_it', Unicode)
    mcpfe_class_en = Column('mcpfe_class_en', Unicode)
    the_geom = Column(Geometry2D)

register(Waldreservate.__bodId__, Waldreservate)


class SturmStaudruck30(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False})
    __bodId__ = 'ch.bafu.sturm-staudruck_30'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Unicode)
    staudruck_50 = Column('staudruck_50', Unicode)
    staudruck_100 = Column('staudruck_100', Unicode)
    staudruck_300 = Column('staudruck_300', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_30', SturmStaudruck30)


class SturmStaudruck50(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-staudruck_50'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Unicode)
    staudruck_50 = Column('staudruck_50', Unicode)
    staudruck_100 = Column('staudruck_100', Unicode)
    staudruck_300 = Column('staudruck_300', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_50', SturmStaudruck50)


class SturmStaudruck100(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-staudruck_100'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Unicode)
    staudruck_50 = Column('staudruck_50', Unicode)
    staudruck_100 = Column('staudruck_100', Unicode)
    staudruck_300 = Column('staudruck_300', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_100', SturmStaudruck100)


class SturmStaudruck300(Base, Vector):
    __tablename__ = 'data_staudruck'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-staudruck_300'
    __template__ = 'templates/htmlpopup/sturm_staudruck.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    staudruck_30 = Column('staudruck_30', Unicode)
    staudruck_50 = Column('staudruck_50', Unicode)
    staudruck_100 = Column('staudruck_100', Unicode)
    staudruck_300 = Column('staudruck_300', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-staudruck_300', SturmStaudruck300)


class SturmBoeenspitzen30(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_30'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    boenspitzen_kmh_30 = Column('boenspitzen_kmh_30', Unicode)
    boenspitzen_ms_30 = Column('boenspitzen_ms_30', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_30', SturmBoeenspitzen30)


class SturmBoeenspitzen50(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_50'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    boenspitzen_kmh_50 = Column('boenspitzen_kmh_50', Unicode)
    boenspitzen_ms_50 = Column('boenspitzen_ms_50', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_50', SturmBoeenspitzen50)


class SturmBoeenspitzen100(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_100'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    boenspitzen_kmh_100 = Column('boenspitzen_kmh_100', Unicode)
    boenspitzen_ms_100 = Column('boenspitzen_ms_100', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_100', SturmBoeenspitzen100)


class SturmBoeenspitzen300(Base, Vector):
    __tablename__ = 'data_boeenspitzen'
    __table_args__ = ({'schema': 'diverse', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.bafu.sturm-boeenspitzen_300'
    __template__ = 'templates/htmlpopup/sturm_boeenspitzen.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    boenspitzen_kmh_300 = Column('boenspitzen_kmh_300', Unicode)
    boenspitzen_ms_300 = Column('boenspitzen_ms_300', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.sturm-boeenspitzen_300', SturmBoeenspitzen300)


class Hochwasserstatistik(Base, Vector):
    __tablename__ = 'hochwasserstatistik'
    __table_args__ = ({'schema': 'hydrologie', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrologie-hochwasserstatistik'
    __template__ = 'templates/htmlpopup/hochwasserstatistik.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    url_fr = Column('url_fr', Unicode)
    url_de = Column('url_de', Unicode)
    url_hqpdf = Column('url_hqpdf', Unicode)
    the_geom = Column(Geometry2D)

register('ch.bafu.hydrologie-hochwasserstatistik', Hochwasserstatistik)


class HydrogeologieMarkierversuche(Base, Vector):
    __tablename__ = 'hydrogeologie_markierversuche'
    __table_args__ = ({'schema': 'hydrogeolog', 'autoload': False})
    __bodId__ = 'ch.bafu.hydrogeologie-markierversuche'
    __template__ = 'templates/htmlpopup/hydrogeologie_markierversuche.mako'
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


class LandesForstInventarVegetation:
    __table_args__ = ({'schema': 'wald', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/landesforstinventar-vegetationshoehenmodell.mako'
    __label__ = 'datenstand'
    id = Column('bgdi_id', Integer, primary_key=True)
    datenstand = Column('datenstand', Integer)
    the_geom = Column(Geometry2D)


class LandesForstInventarVegetationsHoehenModell(Base, LandesForstInventarVegetation, Vector):
    __bodId__ = 'ch.bafu.landesforstinventar-vegetationshoehenmodell'
    __tablename__ = 'vegetationshoehenmodell'
    __queryable_attributes__ = ['datenstand']

register(LandesForstInventarVegetationsHoehenModell.__bodId__, LandesForstInventarVegetationsHoehenModell)


class LandesForstInventarVegetationsHoehenModellRelief(Base, LandesForstInventarVegetation, Vector):
    __bodId__ = 'ch.bafu.landesforstinventar-vegetationshoehenmodell_relief'
    __tablename__ = 'vegetationshoehenmodell_relief'

register(LandesForstInventarVegetationsHoehenModellRelief.__bodId__, LandesForstInventarVegetationsHoehenModellRelief)


class LandesforstinventarRegion:
    __table_args__ = ({'schema': 'wald', 'autoload': False})
    __template__ = 'templates/htmlpopup/landesforstinventar-region.mako'
    __label__ = 'id'
    id = Column('id', Integer, primary_key=True)
    name_de = Column('name_de', Unicode)
    name_fr = Column('name_fr', Unicode)
    name_it = Column('name_it', Unicode)
    name_en = Column('name_en', Unicode)
    the_geom = Column(Geometry2D)


class LandesforstinventarProduktionsregion(Base, LandesforstinventarRegion, Vector):
    __tablename__ = 'produktionsregionen'
    __bodId__ = 'ch.bafu.landesforstinventar-produktionsregionen'

register(LandesforstinventarProduktionsregion.__bodId__, LandesforstinventarProduktionsregion)


class LandesforstinventarWirtschaftsregion(Base, LandesforstinventarRegion, Vector):
    __tablename__ = 'wirtschaftsregionen'
    __bodId__ = 'ch.bafu.landesforstinventar-wirtschaftsregionen'

register(LandesforstinventarWirtschaftsregion.__bodId__, LandesforstinventarWirtschaftsregion)


class LandesforstinventarSchutzwaldregion(Base, LandesforstinventarRegion, Vector):
    __tablename__ = 'schutzwaldregionen'
    __bodId__ = 'ch.bafu.landesforstinventar-schutzwaldregionen'

register(LandesforstinventarSchutzwaldregion.__bodId__, LandesforstinventarSchutzwaldregion)


class AmphibienwanderungVerkehrskonflikte(Base, Vector):
    __tablename__ = 'amphibienwanderung_verkehrskonflikte'
    __table_args__ = ({'schema': 'fauna', 'autoload': False})
    __bodId__ = 'ch.bafu.amphibienwanderung-verkehrskonflikte'
    __template__ = 'templates/htmlpopup/amphibienwanderung-verkehrskonflikte.mako'
    __label__ = 'name'
    id = Column('nr_datenbank', Integer, primary_key=True)
    nr_kanton = Column('nr_kanton', Unicode)
    name = Column('name', Unicode)
    type_de = Column('type_de', Unicode)
    type_fr = Column('type_fr', Unicode)
    type_it = Column('type_it', Unicode)
    massnahme_de = Column('massnahme_de', Unicode)
    massnahme_fr = Column('massnahme_fr', Unicode)
    massnahme_it = Column('massnahme_it', Unicode)
    ref_datenblatt = Column('ref_datenblatt', Unicode)
    the_geom = Column(Geometry2D)

register(AmphibienwanderungVerkehrskonflikte.__bodId__, AmphibienwanderungVerkehrskonflikte)


class GewaesserUferbestockung(Base, Vector):
    __tablename__ = 'gewaesser_uferbestockung'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.gewaesser-uferbestockung'
    __template__ = 'templates/htmlpopup/bafu_gewaesser_uferbestockung.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    gwl_nr = Column('gwl_nr', Unicode)
    bestockung = Column('bestockung', Float)
    the_geom = Column('the_geom', Geometry2D)
    the_geom_simplified = Column('the_geom_simplified', Geometry2D)

register('ch.bafu.gewaesser-uferbestockung', GewaesserUferbestockung)


class LebensraumkarteSchweiz(Base, Vector):
    __tablename__ = 'lebensraumkarte_schweiz'
    __table_args__ = ({'schema': 'lebensraumkarte', 'autoload': False})
    __bodId__ = 'ch.bafu.lebensraumkarte-schweiz'
    __template__ = 'templates/htmlpopup/bafu_lebensraumkarte_schweiz.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    polyid = Column('polyid', Integer)
    typoch_de = Column('typoch_de', Unicode)
    typoch_fr = Column('typoch_fr', Unicode)
    typoch_it = Column('typoch_it', Unicode)
    prob_de = Column('prob_de', Unicode)
    prob_fr = Column('prob_fr', Unicode)
    prob_it = Column('prob_it', Unicode)
    cover = Column('cover', Float)
    the_geom = Column('the_geom', Geometry2D)

register('ch.bafu.lebensraumkarte-schweiz', LebensraumkarteSchweiz)


class TranquillityGebiete(Base, Vector):
    __tablename__ = 'tranquillity_gebiete'
    __table_args__ = ({'schema': 'schutzge', 'autoload': False})
    __bodId__ = 'ch.bafu.tranquillity-gebiete'
    __template__ = 'templates/htmlpopup/bafu_tranquillity_gebiete.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('fid', Integer)
    flaeche = Column('flaeche', Float)
    oev_erreichbarkeit = Column('oev_erreichbarkeit', Integer)
    bln_gebiet_de = Column('bln_gebiet_de', Unicode)
    bln_gebiet_fr = Column('bln_gebiet_fr', Unicode)
    name = Column('name', Unicode)
    kanton = Column('kanton', Unicode)
    gemeinde = Column('gemeinde', Unicode)
    naturpark_de = Column('naturpark_de', Unicode)
    naturpark_fr = Column('naturpark_fr', Unicode)
    moorlandschaft_de = Column('moorlandschaft_de', Unicode)
    moorlandschaft_fr = Column('moorlandschaft_fr', Unicode)
    the_geom = Column('the_geom', Geometry2D)

register('ch.bafu.tranquillity-gebiete', TranquillityGebiete)


class KlimaCO2AusstossGebaeude(Base, Vector):
    __tablename__ = 'co2_ausstoss_gebaeude'
    __table_args__ = ({'schema': 'klima', 'autoload': False})
    __bodId__ = 'ch.bafu.klima-co2_ausstoss_gebaeude'
    __template__ = 'templates/htmlpopup/bafu_klima_co2_ausstoss_gebaeude.mako'
    __label__ = 'id'
    id = Column('egid', Integer, primary_key=True)
    strname_deinr = Column('strname_deinr', Unicode)
    dplz4_dplzname = Column('dplz4_dplzname', Unicode)
    hinweis_de = Column('hinweis_de', Unicode)
    hinweis_fr = Column('hinweis_fr', Unicode)
    hinweis_it = Column('hinweis_it', Unicode)
    co2_range = Column('co2_range', Unicode)
    gwaerzh1_de = Column('gwaerzh1_de', Unicode)
    gwaerzh1_fr = Column('gwaerzh1_fr', Unicode)
    gwaerzh1_it = Column('gwaerzh1_it', Unicode)
    genh1_de = Column('genh1_de', Unicode)
    genh1_fr = Column('genh1_fr', Unicode)
    genh1_it = Column('genh1_it', Unicode)
    gwaersceh1_de = Column('gwaersceh1_de', Unicode)
    gwaersceh1_fr = Column('gwaersceh1_fr', Unicode)
    gwaersceh1_it = Column('gwaersceh1_it', Unicode)
    gexpdat = Column('gexpdat', Unicode)
    linkco2 = Column('linkco2', Unicode)
    linkpdf_de = Column('linkpdf_de', Unicode)
    linkpdf_fr = Column('linkpdf_fr', Unicode)
    linkpdf_it = Column('linkpdf_it', Unicode)
    linkbafu_de = Column('linkbafu_de', Unicode)
    linkbafu_fr = Column('linkbafu_fr', Unicode)
    linkbafu_it = Column('linkbafu_it', Unicode)
    the_geom = Column('the_geom', Geometry2D)

register('ch.bafu.klima-co2_ausstoss_gebaeude', KlimaCO2AusstossGebaeude)


class WaldbrandPraevention(Base, Vector):
    __tablename__ = 'waldbrandpraevention'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-waldbrand_praeventionsmassnahmen_kantone'
    __template__ = 'templates/htmlpopup/bafu_gefahren_waldbrandpraevention.mako'
    __label__ = 'id'
    id = Column('region_id', Integer, primary_key=True)
    name_de = Column('name_de', Unicode)
    name_fr = Column('name_fr', Unicode)
    name_it = Column('name_it', Unicode)
    name_en = Column('name_en', Unicode)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    title_en = Column('title_en', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_it = Column('description_it', Unicode)
    description_en = Column('description_en', Unicode)
    valid_from = Column('valid_from', DateTimeChsdi)
    canton = Column('canton', Unicode)
    the_geom = Column('the_geom', Geometry2D)

register(WaldbrandPraevention.__bodId__, WaldbrandPraevention)


class WaldbrandWarnung(Base, Vector):
    __tablename__ = 'waldbrandwarnung'
    __table_args__ = ({'schema': 'gefahren', 'autoload': False})
    __bodId__ = 'ch.bafu.gefahren-waldbrand_warnung'
    __template__ = 'templates/htmlpopup/bafu_gefahren_waldbrandwarnung.mako'
    __label__ = 'id'
    id = Column('region_id', Integer, primary_key=True)
    name_de = Column('name_de', Unicode)
    name_fr = Column('name_fr', Unicode)
    name_it = Column('name_it', Unicode)
    name_en = Column('name_en', Unicode)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    title_en = Column('title_en', Unicode)
    valid_from = Column('valid_from', DateTimeChsdi)
    canton = Column('canton', Unicode)
    the_geom = Column('the_geom', Geometry2D)

register(WaldbrandWarnung.__bodId__, WaldbrandWarnung)


class LandesforstinventarKantone(Base, Vector):
    __tablename__ = 'landesforstinventar_kantone'
    __table_args__ = ({'schema': 'diverse', 'autoload': False})
    __bodId__ = 'ch.bafu.landesforstinventar-kantone'
    __template__ = 'templates/htmlpopup/bafu_landesforstinventar_kantone.mako'
    __label__ = 'id'
    id = Column('kantonid', Integer, primary_key=True)
    kantonname_de = Column('kantonname_de', Unicode)
    kantonname_fr = Column('kantonname_fr', Unicode)
    kantonname_it = Column('kantonname_it', Unicode)
    kantonname_en = Column('kantonname_en', Unicode)
    alternatename = Column('alternatename', Unicode)
    the_geom = Column('the_geom', Geometry2D)

register(LandesforstinventarKantone.__bodId__, LandesforstinventarKantone)


class FaunaWildtierpassagen(Base, Vector):
    __tablename__ = 'wildtierpassagen'
    __table_args__ = ({'schema': 'fauna', 'autoload': False})
    __bodId__ = 'ch.bafu.fauna-wildtierpassagen'
    __template__ = 'templates/htmlpopup/bafu_fauna_wildtierpassagen.mako'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    name  = Column('name', Unicode)
    verkehrsinfrastrukturtyp  = Column('verkehrsinfrastrukturtyp', Unicode)
    realisierungsjahr  = Column('realisierungsjahr', Unicode)
    sanierungastra_de  = Column('sanierungastra_de', Unicode)
    sanierungastra_fr  = Column('sanierungastra_fr', Unicode)
    sanierungastra_it  = Column('sanierungastra_it', Unicode)
    the_geom = Column('the_geom', Geometry2D)

register(FaunaWildtierpassagen.__bodId__, FaunaWildtierpassagen)


class Trockenheitswarnkarte(Base, Vector):
    __tablename__ = 'trockenheitswarnkarte'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.trockenheitswarnkarte'
    __template__ = 'templates/htmlpopup/bafu_trockenheitswarnkarte.mako'
    __label__ = 'idn'
    id = Column('bgdi_id', Integer, primary_key=True)
    idn = Column('idn', Integer)
    warnlevel = Column('warnlevel', Integer)
    name_de = Column('name_de', Unicode)
    name_fr = Column('name_fr', Unicode)
    name_it = Column('name_it', Unicode)
    name_rm = Column('name_rm', Unicode)
    name_en = Column('name_en', Unicode)
    info_de = Column('info_de', Unicode)
    info_fr = Column('info_fr', Unicode)
    info_it = Column('info_it', Unicode)
    info_rm = Column('info_rm', Unicode)
    info_en = Column('info_en', Unicode)
    valid_from = Column('valid_from', Unicode)
    w_type = Column('w_type', Unicode)
    ws_class = Column('ws_class', Unicode)
    the_geom = Column('the_geom', Geometry2D)

register(Trockenheitswarnkarte.__bodId__, Trockenheitswarnkarte)


class Trockenheitsindex(Base, Vector):
    __tablename__ = 'trockenheitsindex_1'
    __table_args__ = ({'schema': 'wasser', 'autoload': False})
    __bodId__ = 'ch.bafu.trockenheitsindex'
    __template__ = 'templates/htmlpopup/bafu_trockenheitsindex.mako'
    id = Column('bgdi_id', Integer, primary_key=True)
    name_de = Column('name_de', Unicode)
    name_fr = Column('name_fr', Unicode)
    name_it = Column('name_it', Unicode)
    name_en = Column('name_en', Unicode)
    info_de = Column('info_de', Unicode)
    info_fr = Column('info_fr', Unicode)
    info_it = Column('info_it', Unicode)
    info_en = Column('info_en', Unicode)
    valid_from = Column('valid_from', DateTimeChsdi)
    valid_to = Column('valid_to', DateTimeChsdi)
    the_geom = Column('the_geom', Geometry2D)

register(Trockenheitsindex.__bodId__, Trockenheitsindex)
