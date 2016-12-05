# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text

from sqlalchemy.types import Numeric, Boolean, Integer, Float, Unicode

from chsdi.models import register, register_perimeter, bases
from chsdi.models.types import DateTimeChsdi
from chsdi.models.vector import Vector, Geometry2D


Base = bases['stopo']


class GeologieGeomorphologie(Base, Vector):
    __tablename__ = 'geomorphologie'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie-geomorphologie.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomorphologie'
    __label__ = 'ads_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    ads_name = Column('ads_name', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geomorphologie', GeologieGeomorphologie)


class DosisleistungTerrestrisch(Base, Vector):
    __tablename__ = 'dosisleistung_terrestrisch'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/dosisleistung_terrestrisch.mako'
    __bodId__ = 'ch.swisstopo.geologie-dosisleistung-terrestrisch'
    __queryable_attributes__ = ['contour']
    __label__ = 'contour'
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-dosisleistung-terrestrisch', DosisleistungTerrestrisch)


class Smv1000(Base, Vector):
    __tablename__ = 'smv1000'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/smv.mako'
    __bodId__ = 'ch.swisstopo.swiss-map-vector1000.metadata'
    id = Column('perimeter', Unicode, primary_key=True)
    scale = Column('n_scale', Integer)
    price = Column('n_price', Integer)
    release = Column('dt_release', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swiss-map-vector1000.metadata', Smv1000)


class Smv500(Base, Vector):
    __tablename__ = 'smv500'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/smv.mako'
    __bodId__ = 'ch.swisstopo.swiss-map-vector500.metadata'
    id = Column('perimeter', Unicode, primary_key=True)
    scale = Column('n_scale', Integer)
    price = Column('n_price', Integer)
    release = Column('dt_release', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swiss-map-vector500.metadata', Smv500)


class Landesschwerenetz(Base, Vector):
    __tablename__ = 'landesschwerenetz'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/landesschwerenetz.mako'
    __bodId__ = 'ch.swisstopo.landesschwerenetz'
    __queryable_attributes__ = ['nr_lsn2004', 'name', 'type']
    __label__ = 'label_tt'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr_lsn2004 = Column('nr_lsn2004', Text)
    name = Column('name', Text)
    label_tt = Column('label', Text)
    type = Column('type', Text)
    lat_etrs = Column('lat_etrs', Numeric)
    lon_etrs = Column('lon_etrs', Numeric)
    y_lv03 = Column('y_lv03', Numeric)
    x_lv03 = Column('x_lv03', Numeric)
    h_ln02 = Column('h_ln02', Numeric)
    gravity = Column('gravity', Numeric)
    rms = Column('rms', Numeric)
    vert_grad = Column('vert_grad', Numeric)
    link_hfp_title = Column('link_hfp_title', Text)
    link_hfp_url = Column('link_hfp_url', Text)
    link_lfp_title = Column('link_lfp_title', Text)
    link_lfp_url = Column('link_lfp_url', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.landesschwerenetz', Landesschwerenetz)


class LandesschwerenetzExt(Base, Vector):
    __tablename__ = 'landesschwerenetz_exz'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/landesschwerenetz.mako'
    __bodId__ = 'ch.swisstopo.landesschwerenetz'
    __queryable_attributes__ = ['nr_lsn2004', 'name', 'type']
    __maxscale__ = 3000
    __label__ = 'label_tt'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr_lsn2004 = Column('nr_lsn2004', Text)
    name = Column('name', Text)
    label_tt = Column('label', Text)
    type = Column('type', Text)
    lat_etrs = Column('lat_etrs', Numeric)
    lon_etrs = Column('lon_etrs', Numeric)
    y_lv03 = Column('y_lv03', Numeric)
    x_lv03 = Column('x_lv03', Numeric)
    h_ln02 = Column('h_ln02', Numeric)
    gravity = Column('gravity', Numeric)
    rms = Column('rms', Numeric)
    vert_grad = Column('vert_grad', Numeric)
    link_hfp_title = Column('link_hfp_title', Text)
    link_hfp_url = Column('link_hfp_url', Text)
    link_lfp_title = Column('link_lfp_title', Text)
    link_lfp_url = Column('link_lfp_url', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.landesschwerenetz', LandesschwerenetzExt)


class GravimetrischerAtlasMesspunkte(Base, Vector):
    __tablename__ = 'gravimetrisch_messpunkte'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gravimetrischer_atlas_messpunkte.mako'
    __bodId__ = 'ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte'
    __queryable_attributes__ = ['stationnam']
    __label__ = 'stationnam'
    id = Column('bgdi_id', Integer, primary_key=True)
    stationnam = Column('stationnam', Text)
    coordhor = Column('coordhor', Numeric)
    coordver = Column('coordver', Numeric)
    altitude = Column('altitude', Numeric)
    bouguerano = Column('bouguerano', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte', GravimetrischerAtlasMesspunkte)


class GeologieGeowege(Base, Vector):
    __tablename__ = 'geowege'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie_geowege.mako'
    __bodId__ = 'ch.swisstopo.geologie-geowege'
    id = Column('bgdi_id', Integer, primary_key=True)
    titel_1 = Column('titel_1', Text)
    titel_2 = Column('titel_2', Text)
    link = Column('link', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geowege', GeologieGeowege)


class GeolSpezialKartenMetadata(Base, Vector):
    __tablename__ = 'kv_gsk_all'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gsk_metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-spezialkarten_schweiz.metadata'
    __label__ = 'id'
    id = Column('nr', Unicode, primary_key=True)
    titel = Column('titel', Text)
    jahr = Column('jahr', Numeric)
    author = Column('author', Text)
    format_kz = Column('format_kz', Text)
    massstab = Column('massstab', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-spezialkarten_schweiz.metadata', GeolSpezialKartenMetadata)


class ShopProductClass:
    __template__ = 'templates/htmlpopup/shop_product.mako'
    __label__ = 'id'
    __queryable_attributes__ = ['release']
    id = Column('pk_product', Unicode, primary_key=True)
    scale = Column('scale', Integer)
    release = Column('release', Integer)
    data = Column('data', Integer)
    isbn = Column('s_isbn', Text)
    author = Column('s_author', Text)
    available = Column('available', Boolean)
    the_geom = Column(Geometry2D)


class ShopStandardClass:
    __template__ = 'templates/htmlpopup/shop_product.mako'
    id = Column('pk_product', Unicode, primary_key=True)
    available = Column('available', Boolean)
    name_de = Column('s_title_de', Text)
    name_fr = Column('s_title_fr', Text)
    name_it = Column('s_title_it', Text)
    name_en = Column('s_title_en', Text)


class GravimetrischerAtlasPapierMetadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __tablename__ = 'view_gridstand_gravimetrie_atlas_metadata_shop'
    __bodId__ = 'ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata'

register('ch.swisstopo.geologie-gravimetrischer_atlas_papier.metadata', GravimetrischerAtlasPapierMetadata)


class Generalkarte300Metadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_gk300'
    __bodId__ = 'ch.swisstopo.generalkarte300_papier.metadata'

register('ch.swisstopo.generalkarte300_papier.metadata', Generalkarte300Metadata)


class Landeskarte500Metadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk500'
    __bodId__ = 'ch.swisstopo.landeskarte500_papier.metadata'

register('ch.swisstopo.landeskarte500_papier.metadata', Landeskarte500Metadata)


class Landeskarte1000PapierMetadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False, 'extend_existing': True})
    __tablename__ = 'view_gridstand_lk1000'
    __bodId__ = 'ch.swisstopo.landeskarte1000_papier.metadata'

register('ch.swisstopo.landeskarte1000_papier.metadata', Landeskarte1000PapierMetadata)


class SegelFlug300Metadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_sfk300'
    __bodId__ = 'ch.swisstopo.segelflugkarte_papier.metadata'

register('ch.swisstopo.segelflugkarte_papier.metadata', SegelFlug300Metadata)


class StrassenKarte200Metadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_stk200'
    __bodId__ = 'ch.swisstopo.strassenkarte200_papier.metadata'

register('ch.swisstopo.strassenkarte200_papier.metadata', StrassenKarte200Metadata)


class GeolKarte500Metadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkg500'
    __bodId__ = 'ch.swisstopo.geologie-geologische_karte_papier.metadata'

register('ch.swisstopo.geologie-geologische_karte_papier.metadata', GeolKarte500Metadata)


class TektonischeKarte500Metadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkt500'
    __bodId__ = 'ch.swisstopo.geologie-tektonische_karte_papier.metadata'

register('ch.swisstopo.geologie-tektonische_karte_papier.metadata', TektonischeKarte500Metadata)


class SchwereKarte500Metadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkba500'
    __bodId__ = 'ch.swisstopo.geologie-geodaesie-bouguer_anomalien_papier.metadata'

register('ch.swisstopo.geologie-geodaesie-bouguer_anomalien_papier.metadata', SchwereKarte500Metadata)


class GrundwasserVulnerabilitaetPapierMetadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __tablename__ = 'view_gridstand_gkwvul500'
    __bodId__ = 'ch.swisstopo.geologie-grundwasservulnerabilitaet_papier.metadata'

register('ch.swisstopo.geologie-grundwasservulnerabilitaet_papier.metadata', GrundwasserVulnerabilitaetPapierMetadata)


class IcaoPapierMetadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __tablename__ = 'icao_papier'
    __bodId__ = 'ch.swisstopo.luftfahrtkarten-icao_papier.metadata'

register('ch.swisstopo.luftfahrtkarten-icao_papier.metadata', IcaoPapierMetadata)


class GrundWasserVorkommenMetadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkwvor500'
    __bodId__ = 'ch.swisstopo.geologie-grundwasservorkommen_papier.metadata'

register('ch.swisstopo.geologie-grundwasservorkommen_papier.metadata', GrundWasserVorkommenMetadata)


class LetztEisMaxMetadata(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gklgm500'
    __bodId__ = 'ch.swisstopo.geologie-eiszeit-lgm-raster_papier.metadata'

register('ch.swisstopo.geologie-eiszeit-lgm-raster_papier.metadata', LetztEisMaxMetadata)


class Icao500Digital(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_icao500_dig'
    __bodId__ = 'ch.bazl.luftfahrtkarten-icao'

register('ch.bazl.luftfahrtkarten-icao', Icao500Digital)


class SegelFlug300Digital(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_sfk300_dig'
    __bodId__ = 'ch.bazl.segelflugkarte'

register('ch.bazl.segelflugkarte', SegelFlug300Digital)


class ShopProductGroupClass(ShopProductClass):
    __label__ = 'number'
    __queryable_attributes__ = ['number', 'name_de', 'release']
    number = Column('s_map_number', Unicode)
    name_de = Column('s_title_de', Unicode)
    name_fr = Column('s_title_fr', Unicode)
    name_it = Column('s_title_it', Unicode)
    name_en = Column('s_title_en', Unicode)


class SkitourenkarteMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lkski_shop'
    __bodId__ = 'ch.swisstopo.skitourenkarte-50.metadata'

register('ch.swisstopo.skitourenkarte-50.metadata', SkitourenkarteMetadata)


class Landeskarte25PapierMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __tablename__ = 'lk25_papier'
    __bodId__ = 'ch.swisstopo.landeskarte25_papier.metadata'

register('ch.swisstopo.landeskarte25_papier.metadata', Landeskarte25PapierMetadata)


class Landeskarte50PapierMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __tablename__ = 'lk50_papier'
    __bodId__ = 'ch.swisstopo.landeskarte50_papier.metadata'

register('ch.swisstopo.landeskarte50_papier.metadata', Landeskarte50PapierMetadata)


class Scale100Metadata(Base, ShopProductGroupClass, Vector):
    __tablename__ = 'view_gridstand_lk100_shop'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})


class Landeskarte100PapierMetadata(Base, ShopProductGroupClass, Vector):
    __tablename__ = 'lk100_papier'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __bodId__ = 'ch.swisstopo.landeskarte100_papier.metadata'

register('ch.swisstopo.landeskarte100_papier.metadata', Landeskarte100PapierMetadata)


class Luftfahrt100Metadata(Scale100Metadata):
    __bodId__ = 'ch.swisstopo.lhk100-papierkarte.metadata'

register('ch.swisstopo.lhk100-papierkarte.metadata', Luftfahrt100Metadata)


class Landeskarte200Metadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk200_shop'
    __bodId__ = 'ch.swisstopo.landeskarte200_papier.metadata'

register('ch.swisstopo.landeskarte200_papier.metadata', Landeskarte200Metadata)


class Wanderkarte50PapierMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __tablename__ = 'lkwander50_papier'
    __bodId__ = 'ch.swisstopo.wanderkarte50_papier.metadata'

register('ch.swisstopo.wanderkarte50_papier.metadata', Wanderkarte50PapierMetadata)


class WanderkarteT33Metadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_wkt33_shop'
    __bodId__ = 'ch.swisstopo.wanderkarte33_papier.metadata'

register('ch.swisstopo.wanderkarte33_papier.metadata', WanderkarteT33Metadata)


class Wanderkarte25zusMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lkwander25zus_shop'
    __bodId__ = 'ch.swisstopo.wanderkarte25-zus_papier.metadata'

register('ch.swisstopo.wanderkarte25-zus_papier.metadata', Wanderkarte25zusMetadata)


class BurgenKarte200Metadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_bk200'
    __bodId__ = 'ch.swisstopo.burgenkarte200_papier.metadata'

register('ch.swisstopo.burgenkarte200_papier.metadata', BurgenKarte200Metadata)


class GeolAtlasMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gas25'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas_papier.metadata'

register('ch.swisstopo.geologie-geologischer_atlas_papier.metadata', GeolAtlasMetadata)


class GeolSpezialKarteMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gsk'
    __bodId__ = 'ch.swisstopo.geologie-spezialkarten_schweiz_papier.metadata'

register('ch.swisstopo.geologie-spezialkarten_schweiz_papier.metadata', GeolSpezialKarteMetadata)


class GeolGeneralKarteMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_ggk'
    __bodId__ = 'ch.swisstopo.geologie-generalkarte-ggk200_papier.metadata'

register('ch.swisstopo.geologie-generalkarte-ggk200_papier.metadata', GeolGeneralKarteMetadata)


class GeolGenKarteGGK200(Base, ShopProductGroupClass, Vector):
    __tablename__ = 'view_gridstand_ggk_shop'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-generalkarte-ggk200'
    url_legend = Column('url_legend', Text)

register('ch.swisstopo.geologie-generalkarte-ggk200', GeolGenKarteGGK200)


class SwissboundariesBezirk(Base, Vector):
    __tablename__ = 'swissboundaries_bezirke'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_bezirk.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Text)
    flaeche = Column('flaeche', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill', SwissboundariesBezirk)


class SwissboundariesGemeinde(Base, Vector):
    __tablename__ = 'swissboundaries_gemeinden'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_gemeinde.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill'
    __queryable_attributes__ = ['gemname', 'id']
    __label__ = 'gemname'
    id = Column('id', Integer, primary_key=True)
    gemname = Column('gemname', Text)
    gemflaeche = Column('gemflaeche', Numeric)
    perimeter = Column('perimeter', Numeric)
    kanton = Column('kanton', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', SwissboundariesGemeinde)


class SwissboundariesKanton(Base, Vector):
    __tablename__ = 'swissboundaries_kantone'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_kanton.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-kanton-flaeche.fill'
    __queryable_attributes__ = ['id', 'ak', 'name']
    __label__ = 'name'
    id = Column('kantonsnr', Integer, primary_key=True)
    ak = Column('ak', Text)
    name = Column('name', Text)
    flaeche = Column('flaeche', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissboundaries3d-kanton-flaeche.fill', SwissboundariesKanton)


class SwissBoundariesLand(Base, Vector):
    __tablename__ = 'swissboundaries_land'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __bodId__ = 'ch.swisstopo.swissboundaries3d-land-flaeche.fill'
    id = Column('bgdi_id', Integer, primary_key=True)
    displayname = Column('displayname', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissboundaries3d-land-flaeche.fill', SwissBoundariesLand)


class CadastralWebMap(Base, Vector):
    __tablename__ = 'swissboundaries_kantone'
    __table_args__ = ({'schema': 'tlm', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/cadastralwebmap.mako'
    __bodId__ = 'ch.kantone.cadastralwebmap-farbe'
    __label__ = 'ak'
    id = Column('kantonsnr', Integer, primary_key=True)
    ak = Column('ak', Unicode)
    the_geom = Column(Geometry2D)

register('ch.kantone.cadastralwebmap-farbe', CadastralWebMap)


class CadastralWebMapOpenData(Base, Vector):
    __tablename__ = 'swissboundaries_gemeinden_vd_opendata'
    __table_args__ = ({'schema': 'tlm', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/cadastralwebmap_opendata.mako'
    __bodId__ = 'ch.swisstopo-vd.amtliche-vermessung'
    __label__ = 'name'
    __extended_info__ = True
    id = Column('bfsnr', Integer, primary_key=True)
    ak = Column('ak', Unicode)
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.amtliche-vermessung', CadastralWebMapOpenData)


class Vec200Terminal(Base, Vector):
    __tablename__ = 'vec200_terminal'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_terminal.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    objval = Column('objval', Text)
    the_geom = Column(Geometry2D)


class Vec200ShipKursschiff(Base, Vector):
    __tablename__ = 'v200_ship_kursschiff_linie_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ship_kursschiff_linie.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    objval = Column('objval', Text)
    detn = Column('detn', Text)
    rsu = Column('rsu', Text)
    use = Column('use', Text)
    the_geom = Column(Geometry2D)


class Vec200Railway(Base, Vector):
    __tablename__ = 'vec200_railway'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_railway.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    objval = Column('objval', Text)
    construct = Column('construct', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', Vec200Terminal)
register('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', Vec200ShipKursschiff)
register('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', Vec200Railway)


class Vec200Trafficinfo(Base, Vector):
    __tablename__ = 'vec200_trafficinfo'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_trafficinfo.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objname'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname = Column('objname', Text)
    objval = Column('objval', Text)
    the_geom = Column(Geometry2D)


class Vec200ShipAutofaehre(Base, Vector):
    __tablename__ = 'v200_ship_autofaehre_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ship_autofaehre.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'detn'
    id = Column('gtdboid', Unicode, primary_key=True)
    use = Column('use', Text)
    rsu = Column('rsu', Text)
    detn = Column('detn', Text)
    the_geom = Column(Geometry2D)


class Vec200Road(Base, Vector):
    __tablename__ = 'vec200_road'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_road.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    construct = Column('construct', Text)
    objval = Column('objval', Text)
    toll = Column('toll', Text)
    the_geom = Column(Geometry2D)


class Vec200Ramp(Base, Vector):
    __tablename__ = 'vec200_ramp'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ramp.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    construct = Column('construct', Text)
    objval = Column('objval', Text)
    toll = Column('toll', Text)
    the_geom = Column(Geometry2D)


class Vec200Customsoffice(Base, Vector):
    __tablename__ = 'vec200_customsoffice'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_customsoffice.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'ojbname'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname = Column('objname', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Trafficinfo)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200ShipAutofaehre)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Road)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Ramp)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Customsoffice)


class Vec200Protectedarea(Base, Vector):
    __tablename__ = 'vec200_protectedarea'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_protectedarea.mako'
    __bodId__ = 'ch.swisstopo.vec200-adminboundaries-protectedarea'
    __label__ = 'name'
    id = Column('gtdboid', Unicode, primary_key=True)
    name = Column('name', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-adminboundaries-protectedarea', Vec200Protectedarea)


class Vec200Flowingwater(Base, Vector):
    __tablename__ = 'vec200_flowingwater'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_flowingwater.mako'
    __bodId__ = 'ch.swisstopo.vec200-hydrography'
    __label__ = 'name'
    id = Column('gtdboid', Unicode, primary_key=True)
    name = Column('name', Text)
    exs = Column('exs', Text)
    hoc = Column('hoc', Text)
    the_geom = Column(Geometry2D)


class Vec200Stagnantwater(Base, Vector):
    __tablename__ = 'vec200_stagnantwater'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_stagnantwater.mako'
    __bodId__ = 'ch.swisstopo.vec200-hydrography'
    __label__ = 'name'
    id = Column('gtdboid', Unicode, primary_key=True)
    name = Column('name', Text)
    seesph = Column('seesph', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-hydrography', Vec200Flowingwater)
register('ch.swisstopo.vec200-hydrography', Vec200Stagnantwater)


class Vec200Landcover(Base, Vector):
    __tablename__ = 'vec200_landcover'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_landcover.mako'
    __bodId__ = 'ch.swisstopo.vec200-landcover'
    __label__ = 'objname1'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname1 = Column('objname1', Text)
    objval = Column('objval', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-landcover', Vec200Landcover)


class Vec200Builtupp(Base, Vector):
    __tablename__ = 'vec200_builtupp'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_builtupp.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'objname'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname = Column('objname', Text)
    ppi = Column('ppi', Text)
    the_geom = Column(Geometry2D)


class Vec200Poi(Base, Vector):
    __tablename__ = 'v200_poi_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_poi.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'objname'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname = Column('objname', Text)
    objval = Column('objval', Text)
    ppc = Column('ppc', Text)
    pro = Column('pro', Text)
    the_geom = Column(Geometry2D)


class Vec200Supply(Base, Vector):
    __tablename__ = 'vec200_supply'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_supply.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'fco'
    id = Column('gtdboid', Unicode, primary_key=True)
    fco = Column('fco', Text)
    loc = Column('loc', Text)
    pro = Column('pro', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-miscellaneous', Vec200Builtupp)
register('ch.swisstopo.vec200-miscellaneous', Vec200Poi)
register('ch.swisstopo.vec200-miscellaneous', Vec200Supply)


class Vec200Namedlocation(Base, Vector):
    __tablename__ = 'vec200_namedlocation'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_namedlocation.mako'
    __bodId__ = 'ch.swisstopo.vec200-names-namedlocation'
    __queryable_attributes__ = ['objname1', 'id']
    # Composite labels coalesce(objname1,'')||' '||coalesce(objname2,'')
    __label__ = 'objname1'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname1 = Column('objname1', Text)
    objname2 = Column('objname2', Text)
    altitude = Column('altitude', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-names-namedlocation', Vec200Namedlocation)


class Vec25Strassennetz(Base, Vector):
    __tablename__ = 'v25_str_25_l_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_strassennetz.mako'
    __bodId__ = 'ch.swisstopo.vec25-strassennetz'
    __label__ = 'id'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-strassennetz', Vec25Strassennetz)


class Vec25Uebrige(Base, Vector):
    __tablename__ = 'v25_uvk_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_uebrigeverk.mako'
    __bodId__ = 'ch.swisstopo.vec25-uebrigerverkehr'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-uebrigerverkehr', Vec25Uebrige)


class Vec25Anlagen(Base, Vector):
    __tablename__ = 'v25_anl_25_a'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_anlagen.mako'
    __bodId__ = 'ch.swisstopo.vec25-anlagen'
    __label__ = 'area'
    id = Column('objectid', Integer, primary_key=True)
    area = Column('area', Numeric)
    perimeter = Column('perimeter', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-anlagen', Vec25Anlagen)


class Vec25Eisenbahnnetz(Base, Vector):
    __tablename__ = 'v25_eis_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_eisenbahnnetz.mako'
    __bodId__ = 'ch.swisstopo.vec25-eisenbahnnetz'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-eisenbahnnetz', Vec25Eisenbahnnetz)


class Vec25Gebaeude(Base, Vector):
    __tablename__ = 'v25_geb_25_a'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_gebaeude.mako'
    __bodId__ = 'ch.swisstopo.vec25-gebaeude'
    __label__ = 'area'
    id = Column('objectid', Integer, primary_key=True)
    area = Column('area', Numeric)
    perimeter = Column('perimeter', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-gebaeude', Vec25Gebaeude)


class Vec25Gewaessernetz(Base, Vector):
    __tablename__ = 'v25_gwn_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_gewaessernetz.mako'
    __bodId__ = 'ch.swisstopo.vec25-gewaessernetz'
    __label__ = 'name'
    id = Column('objectid', Integer, primary_key=True)
    objectval = Column('objectval', Text)
    gewissnr = Column('gewissnr', Numeric)
    name = Column('name', Text)
    length = Column('length', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-gewaessernetz', Vec25Gewaessernetz)


class Vec25Primaerflaechen(Base, Vector):
    __tablename__ = 'v25_pri25_a'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_primaerflaechen.mako'
    __bodId__ = 'ch.swisstopo.vec25-primaerflaechen'
    __label__ = 'area'
    id = Column('objectid', Integer, primary_key=True)
    area = Column('area', Numeric)
    perimeter = Column('perimeter', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-primaerflaechen', Vec25Primaerflaechen)


class Vec25Einzelobjekte(Base, Vector):
    __tablename__ = 'v25_eob_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_einzelobjekte.mako'
    __bodId__ = 'ch.swisstopo.vec25-einzelobjekte'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-einzelobjekte', Vec25Einzelobjekte)


class Vec25Heckenbaeume(Base, Vector):
    __tablename__ = 'v25_heb_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_heckenbaeume.mako'
    __bodId__ = 'ch.swisstopo.vec25-heckenbaeume'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-heckenbaeume', Vec25Heckenbaeume)


class Dreiecksvermaschung(Base, Vector):
    __tablename__ = 'dreiecksvermaschung'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/dreiecksvermaschung.mako'
    __bodId__ = 'ch.swisstopo.dreiecksvermaschung'
    __label__ = 'nom'
    id = Column('bgdi_id', Integer, primary_key=True)
    nom = Column('nom', Text)
    num = Column('num', Text)
    type = Column('type', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.dreiecksvermaschung', Dreiecksvermaschung)

# Gridstands PK layers noscale and metadata


class GridstandTemplate:
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __label__ = 'lk_name'
    id = Column('kbnum', Unicode, primary_key=True)
    lk_name = Column('lk_name', Text)
    release = Column('release', Integer)
    the_geom = Column(Geometry2D)


class GridstandPermiterTemplate:
    __table_args__ = ({'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


# PK 25


class GridstandPK25Perimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_pk25'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk25.noscale'
    __table_args__ = ({'autoload': False})
    the_geom = Column(Geometry2D)


class GridstandPk25Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk25.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk25_tilecache'
    __template__ = 'templates/htmlpopup/pk25_metadata.mako'


register('ch.swisstopo.pixelkarte-farbe-pk25.noscale', GridstandPK25Perimeter)
register('ch.swisstopo.pixelkarte-pk25.metadata', GridstandPk25Meta)

# PK 50


# Only PK50 has a fixed perimeter
class GridstandPK50Perimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_pk50'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk50.noscale'
    __totalArea__ = 65520.0
    __table_args__ = ({'autoload': False})
    the_geom = Column(Geometry2D)


class GridstandPk50Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk50.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk50_tilecache'
    __template__ = 'templates/htmlpopup/pk50_metadata.mako'

register('ch.swisstopo.pixelkarte-farbe-pk50.noscale', GridstandPK50Perimeter)
register('ch.swisstopo.pixelkarte-pk50.metadata', GridstandPk50Meta)

# PK 100


class GridstandPK100Perimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_pk100'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk100.noscale'
    __table_args__ = ({'autoload': False})
    the_geom = Column(Geometry2D)


class GridstandPk100Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk100.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk100_tilecache'
    __template__ = 'templates/htmlpopup/pk100_metadata.mako'

register('ch.swisstopo.pixelkarte-farbe-pk100.noscale', GridstandPK100Perimeter)
register('ch.swisstopo.pixelkarte-pk100.metadata', GridstandPk100Meta)

# PK 200


class GridstandPK200Perimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_pk200'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk200.noscale'
    __table_args__ = ({'autoload': False})
    the_geom = Column(Geometry2D)


class GridstandPk200Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk200.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk200_tilecache'
    __template__ = 'templates/htmlpopup/pk200_metadata.mako'

register('ch.swisstopo.pixelkarte-farbe-pk200.noscale', GridstandPK200Perimeter)
register('ch.swisstopo.pixelkarte-pk200.metadata', GridstandPk200Meta)

# PK 500


class GridstandPk500(Base, ShopProductClass, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_pk500_tilecache_shop'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk500.noscale'


class GridstandPk500Perimeter(Base, GridstandPermiterTemplate, Vector):
    __tablename__ = 'shop_perimeter_pk500'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk500.noscale'


class GridstandPk500Meta(GridstandPk500):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk500.metadata'

register('ch.swisstopo.pixelkarte-farbe-pk500.noscale', GridstandPk500)
register_perimeter('ch.swisstopo.pixelkarte-farbe-pk500.noscale', GridstandPk500Perimeter)
register('ch.swisstopo.pixelkarte-pk500.metadata', GridstandPk500Meta)


class SwissimageProductPerimeter(Base, Vector):
    __tablename__ = 'shop_perimeter_swissimage'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __bodId__ = 'ch.swisstopo.images-swissimage.metadata'
    id = Column('min', Integer, primary_key=True)
    resolution = Column('resolution', Float)
    the_geom = Column(Geometry2D)


class GridstandSwissimage(Base, ShopStandardClass, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_swissimage_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.images-swissimage.metadata'
    __label__ = 'lk25_name'
    id = Column('tilenumber', Unicode, primary_key=True)
    tileid = Column('tileid', Unicode)
    lk25_name  = Column('lk25_name', Text)
    datenstand = Column('datenstand', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.images-swissimage.metadata', GridstandSwissimage)
register_perimeter('ch.swisstopo.images-swissimage.metadata', SwissimageProductPerimeter)


class SwissimageProduct(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_swissimage'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __bodId__ = 'ch.swisstopo.swissimage-product'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissimage-product', SwissimageProduct)
register_perimeter('ch.swisstopo.swissimage-product', SwissimageProductPerimeter)


class GeolGenKarteGGK200Meta(Base, Vector):
    __tablename__ = 'kv_ggk_pk'
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/generalkarte_ggk200.metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-generalkarte-ggk200.metadata'
    __queryable_attributes__ = ['titel', 'jahr', 'author', 'nr']
    __label__ = 'prod_id'
    id = Column('gid', Text, primary_key=True)
    nr = Column('nr', Integer)
    prod_id = Column('prod_id', Text)
    titel = Column('titel', Text)
    autor = Column('autor', Text)
    jahr = Column('jahr', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-generalkarte-ggk200.metadata', GeolGenKarteGGK200Meta)


class GeologischeKarteLine(Base, Vector):
    __tablename__ = 'geologische_karte_line'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologische_karte_line.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologische_karte'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('fid', Integer, primary_key=True)
    gid = Column('id', Integer)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry2D)


class GeologischeKartePlg(Base, Vector):
    __tablename__ = 'geologische_karte_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologische_karte_plg.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologische_karte'
    __label__ = 'leg_geol_d'
    id = Column('id', Integer, primary_key=True)
    leg_geol_d = Column('leg_geol_d', Text)
    leg_geol_f = Column('leg_geol_f', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geologische_karte', GeologischeKarteLine)
register('ch.swisstopo.geologie-geologische_karte', GeologischeKartePlg)


class GeologieMineralischeRohstoffe200(Base, Vector):
    __tablename__ = 'geotechnik_mineralische_rohstoffe200'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotechnik_mineralische_rohstoffe200.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200'
    __label__ = 'area_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    legend = Column('legend', Text)
    area_name = Column('area_name', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200', GeologieMineralischeRohstoffe200)


class GeologieGeotechnikGk200(Base, Vector):
    __tablename__ = 'geotechnik_gk200_lgd'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotechnik_gk200.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk200'
    __label__ = 'file_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    file_name = Column('file_name', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk200', GeologieGeotechnikGk200)


class Gk500_Gensese (Base, Vector):
    __tablename__ = 'gk500_genese'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gk500-genese.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-genese'
    # Translatable labels in fr, it, rm, it
    __label__ = 'genese_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    genese_de = Column('genese_de', Text)
    genese_fr = Column('genese_fr', Text)
    genese_en = Column('genese_en', Text)
    genese_it = Column('genese_it', Text)
    genese_rm = Column('genese_rm', Text)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk500-genese', Gk500_Gensese)


class Gk500_Gesteinsklassierung (Base, Vector):
    __tablename__ = 'gk500_gesteinsklassierung'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gk500-gesteinsklassierung.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-gesteinsklassierung'
    __label__ = 'gestkl_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    # Translatable labels in fr, it, rm, it
    __label__ = 'gestkl_de'
    gestkl_de = Column('gestkl_de', Text)
    gestkl_fr = Column('gestkl_fr', Text)
    gestkl_en = Column('gestkl_en', Text)
    gestkl_it = Column('gestkl_it', Text)
    gestkl_rm = Column('gestkl_rm', Text)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk500-gesteinsklassierung', Gk500_Gesteinsklassierung)


class Gk500_lithologie_hauptgruppen(Base, Vector):
    __tablename__ = 'gk500_lithologie_hauptgruppen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/lithologie_hauptgruppen.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-lithologie_hauptgruppen'
    # Translatable labels in fr, it, rm, it
    __label__ = 'bgdi_tooltip_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    bgdi_tooltip_de = Column('bgdi_tooltip_de', Text)
    bgdi_tooltip_fr = Column('bgdi_tooltip_fr', Text)
    bgdi_tooltip_en = Column('bgdi_tooltip_en', Text)
    bgdi_tooltip_it = Column('bgdi_tooltip_it', Text)
    bgdi_tooltip_rm = Column('bgdi_tooltip_rm', Text)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk500-lithologie_hauptgruppen', Gk500_lithologie_hauptgruppen)


class GeologieGeotechnikSteinbrueche1915(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1915'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1915.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1915'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1915', GeologieGeotechnikSteinbrueche1915)


class GeologieGeotechnikSteinbrueche1965(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1965'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1965'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1965', GeologieGeotechnikSteinbrueche1965)


class GeologieGeotechnikSteinbrueche1980(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1980'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1980.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1980'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1980', GeologieGeotechnikSteinbrueche1980)


class GeologieGeotechnikSteinbrueche1995(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1995'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1995'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1995', GeologieGeotechnikSteinbrueche1995)


class GeologieGeotechnikZementindustrie1965(Base, Vector):
    __tablename__ = 'geotechnik_zementindustrie'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/zementindustrie_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-zementindustrie_1965'
    __label__ = 'stoff'
    id = Column('id', Integer, primary_key=True)
    stoff = Column('stoff', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-zementindustrie_1965', GeologieGeotechnikZementindustrie1965)


class GeologieGeotechnikZementindustrie1995(Base, Vector):
    __tablename__ = 'geotechnik_zementindustrie'
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/zementindustrie_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-zementindustrie_1995'
    __label__ = 'stoff'
    id = Column('id', Integer, primary_key=True)
    stoff = Column('stoff', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-zementindustrie_1995', GeologieGeotechnikZementindustrie1995)


class GeologieGeotechnikZiegeleien1907(Base, Vector):
    __tablename__ = 'geotechnik_ziegeleien_1907'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ziegeleien_1907.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-ziegeleien_1907'
    __queryable_attributes__ = ['ziegelei_2']
    __label__ = 'ziegelei_2'
    id = Column('id', Integer, primary_key=True)
    ziegelei_2 = Column('ziegelei_2', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-ziegeleien_1907', GeologieGeotechnikZiegeleien1907)


class GeologieGeotechnikZiegeleien1965(Base, Vector):
    __tablename__ = 'geotechnik_ziegeleien_1965'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ziegeleien_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-ziegeleien_1965'
    __queryable_attributes__ = ['ziegelei']
    __label__ = 'ziegelei'
    id = Column('id', Integer, primary_key=True)
    ziegelei = Column('ziegelei', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-ziegeleien_1965', GeologieGeotechnikZiegeleien1965)


class GeologieGeotechnikZiegeleien1995(Base, Vector):
    __tablename__ = 'geotechnik_ziegeleien_1995'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ziegeleien_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-ziegeleien_1995'
    __queryable_attributes__ = ['ziegeleien']
    __label__ = 'ziegeleien'
    id = Column('id', Integer, primary_key=True)
    ziegeleien = Column('ziegeleien', Text)
    produkt = Column('produkt', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-ziegeleien_1995', GeologieGeotechnikZiegeleien1995)


class GeologieHydroKarteGrundwasservorkommen(Base, Vector):
    __tablename__ = 'grundwasservorkommen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/grundwasservorkommen.mako'
    __bodId__ = 'ch.swisstopo.geologie-hydrogeologische_karte-grundwasservorkommen'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-hydrogeologische_karte-grundwasservorkommen', GeologieHydroKarteGrundwasservorkommen)


class GeologieHydroKarteGrundwasservulneabilitaet(Base, Vector):
    __tablename__ = 'grundwasservorkommen_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/grundwasservulnerabilitaet.mako'
    __bodId__ = 'ch.swisstopo.geologie-hydrogeologische_karte-grundwasservulnerabilitaet'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-hydrogeologische_karte-grundwasservulnerabilitaet', GeologieHydroKarteGrundwasservulneabilitaet)


class GeologieGeothermie(Base, Vector):
    __tablename__ = 'geophysik_geothermie'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geothermie.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-geothermie'
    __label__ = 'contour'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-geothermie', GeologieGeothermie)


class Geologischer_Deklination(Base, Vector):
    __tablename__ = 'geophysik_deklination'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/deklination.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-deklination'
    __label__ = 'magne'
    id = Column('gid', Integer, primary_key=True)
    magne = Column('magne', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-deklination', Geologischer_Deklination)


class Geologischer_Inklination(Base, Vector):
    __tablename__ = 'geophysik_inklination'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/inklination.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-inklination'
    __label__ = 'contour'
    id = Column('gid', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-inklination', Geologischer_Inklination)


class Geologischer_Aeromagnetik_Jura(Base, Vector):
    __tablename__ = 'gravimetrie_aeromagnetik_jura'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetik_jura.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-aeromagnetische_karte_jura'
    __label__ = 'et_fromatt'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-aeromagnetische_karte_jura', Geologischer_Aeromagnetik_Jura)


class Geologischer_Aeromagnetik_CH(Base, Vector):
    __tablename__ = 'gravimetrie_aeromagnetik_ch'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetik_schweiz.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz'
    __label__ = 'fid'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz', Geologischer_Aeromagnetik_CH)


class GeologieIsostatischeAnomalien(Base, Vector):
    __tablename__ = 'schwerekarte_isostatische_anomalien'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/isostatische_anomalien.mako'
    __bodId__ = 'ch.swisstopo.geologie-geodaesie-isostatische_anomalien'
    __label__ = 'et_fromatt'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geodaesie-isostatische_anomalien', GeologieIsostatischeAnomalien)


class GeologieBouguerAnomalien(Base, Vector):
    __tablename__ = 'geodaesie_bouguer_anomalien'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/bouguer_anomalien.mako'
    __bodId__ = 'ch.swisstopo.geologie-geodaesie-bouguer_anomalien'
    __label__ = 'et_fromatt'
    id = Column('gid', Integer, primary_key=True)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geodaesie-bouguer_anomalien', GeologieBouguerAnomalien)


class GeologieGeophysikTotalintensitaet(Base, Vector):
    __tablename__ = 'geophysik_totalintensitaet'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/totalintensitaet.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-totalintensitaet'
    __label__ = 'contour'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-totalintensitaet', GeologieGeophysikTotalintensitaet)


class GeologieRohstoffeIndustrieminerale(Base, Vector):
    __tablename__ = 'rohstoffe_industrieminerale'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_industrieminerale.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-industrieminerale'
    __queryable_attributes__ = ['name_ads']
    __label__ = 'name_ads'
    id = Column('id', Integer, primary_key=True)
    rohstoff = Column('rohstoff', Text)
    name_ads = Column('name_ads', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-industrieminerale', GeologieRohstoffeIndustrieminerale)


class GeologieRohstoffeKohlenBitumenErdgas(Base, Vector):
    __tablename__ = 'rohstoffe_kohlen_bitumen_erdgas'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_kohlen_bitumen_erdgas.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas'
    __queryable_attributes__ = ['name_ads']
    __label__ = 'name_ads'
    id = Column('id', Integer, primary_key=True)
    rohstoff = Column('rohstoff', Text)
    name_ads = Column('name_ads', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas', GeologieRohstoffeKohlenBitumenErdgas)


class GeologieRohstoffeVererzungen(Base, Vector):
    __tablename__ = 'rohstoffe_vererzungen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_vererzungen.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-vererzungen'
    __queryable_attributes__ = ['name_ads']
    __label__ = 'name_ads'
    id = Column('id', Integer, primary_key=True)
    rohstoff = Column('rohstoff', Text)
    name_ads = Column('name_ads', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-vererzungen', GeologieRohstoffeVererzungen)


class GeologieTektonischeKarteLine(Base, Vector):
    __tablename__ = 'tektonische_karte_line'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/tektonische_karte_line.mako'
    __bodId__ = 'ch.swisstopo.geologie-tektonische_karte'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('fid', Integer, primary_key=True)
    line_id = Column('line_id', Integer)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry2D)


class GeologieTektonischeKartePoly(Base, Vector):
    __tablename__ = 'tektonische_karte_flaechen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/tektonische_karte_poly.mako'
    __bodId__ = 'ch.swisstopo.geologie-tektonische_karte'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('fid', Integer, primary_key=True)
    t2_id = Column('t2_id', Integer)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-tektonische_karte', GeologieTektonischeKarteLine)
register('ch.swisstopo.geologie-tektonische_karte', GeologieTektonischeKartePoly)


class GeologieEiszeitLgm(Base, Vector):
    __tablename__ = 'eiszeit_lgm500'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/eiszeit_lgm.mako'
    __bodId__ = 'ch.swisstopo.geologie-eiszeit-lgm'
    __label__ = 'ads_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    ads_name = Column('ads_name', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-eiszeit-lgm', GeologieEiszeitLgm)


class Swisstlm3dWanderwege(Base, Vector):
    __tablename__ = 'wanderwege_swissmap'
    __table_args__ = ({'schema': 'karto', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissmap_online_wanderwege.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-wanderwege'
    __label__ = 'id'
    id = Column('nr', Integer, primary_key=True)
    hikingtype = Column('hikingtype', Text)
    bridgetype = Column('bridgetype', Text)
    tunneltype = Column('tunneltype', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisstlm3d-wanderwege', Swisstlm3dWanderwege)


class VerschiebungsvektorenTsp1(Base, Vector):
    __tablename__ = 'verschiebungsvektoren_tsp1'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/verschiebungsvektoren_tps1.mako'
    __bodId__ = 'ch.swisstopo.verschiebungsvektoren-tsp1'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Integer)
    name = Column('name', Text)
    type = Column('type', Text)
    e_lv03 = Column('e_lv03', Numeric)
    e_lv95 = Column('e_lv95', Numeric)
    n_lv03 = Column('n_lv03', Numeric)
    n_lv95 = Column('n_lv95', Numeric)
    de = Column('de', Numeric)
    dn = Column('dn', Numeric)
    fs = Column('fs', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.verschiebungsvektoren-tsp1', VerschiebungsvektorenTsp1)


class VerschiebungsvektorenTsp2(Base, Vector):
    __tablename__ = 'verschiebungsvektoren_tsp2'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/verschiebungsvektoren_tps2.mako'
    __bodId__ = 'ch.swisstopo.verschiebungsvektoren-tsp2'
    __queryable_attributes__ = ['name', 'id']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Integer)
    name = Column('name', Text)
    type = Column('type', Text)
    e_lv03 = Column('e_lv03', Numeric)
    e_lv95 = Column('e_lv95', Numeric)
    n_lv03 = Column('n_lv03', Numeric)
    n_lv95 = Column('n_lv95', Numeric)
    de = Column('de', Numeric)
    dn = Column('dn', Numeric)
    fs = Column('fs', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.verschiebungsvektoren-tsp2', VerschiebungsvektorenTsp2)


class SwissmapOnlineWanderwege(Base, Vector):
    __tablename__ = 'wanderwege_swissmap'
    __table_args__ = ({'schema': 'karto', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/swissmap_online_wanderwege.mako'
    __bodId__ = 'ch.swisstopo-karto.wanderwege'
    __label__ = 'id'
    id = Column('nr', Integer, primary_key=True)
    hikingtype = Column('hikingtype', Text)
    bridgetype = Column('bridgetype', Text)
    tunneltype = Column('tunneltype', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-karto.wanderwege', SwissmapOnlineWanderwege)


class PLZOrtschaften(Base, Vector):
    __tablename__ = 'gabmo_plz'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/gabmo_plz.mako'
    __bodId__ = 'ch.swisstopo-vd.ortschaftenverzeichnis_plz'
    __queryable_attributes__ = ['plz', 'langtext']
    __label__ = 'plz'
    id = Column('os_uuid', Unicode, primary_key=True)
    plz = Column('plz', Integer)
    zusziff = Column('zusziff', Text)
    langtext = Column('langtext', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.ortschaftenverzeichnis_plz', PLZOrtschaften)


class geometaStandAV(Base, Vector):
    __tablename__ = 'amogr_standav'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/standav.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-standav'
    __label__ = 'frame'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    quality = Column('quality', Text)
    frame = Column('frame', Text)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-standav', geometaStandAV)


class geometaPNF(Base, Vector):
    __tablename__ = 'amopnf_pnf'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/metadata_pnf.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-periodische_nachfuehrung'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    canton = Column('canton', Text)
    description = Column('description', Text)
    year = Column('year', Integer)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-periodische_nachfuehrung', geometaPNF)


class geometaLos(Base, Vector):
    __tablename__ = 'amogr_los'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/los.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-los'
    __label__ = 'operatsname'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    neu_id = Column('neu_id', Text)
    operatsname = Column('operatsname', Text)
    losnr = Column('losnr', Text)
    taetigkeit_d = Column('taetigkeit_d', Text)
    taetigkeit_f = Column('taetigkeit_f', Text)
    taetigkeit_i = Column('taetigkeit_i', Text)
    quality = Column('quality', Text)
    flaeche_vertrag = Column('flaeche_vertrag', Text)
    frame = Column('frame', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-los', geometaLos)

# link sur le pdf ne fontionne pas...


class geometaGemeinde(Base, Vector):
    __tablename__ = 'amogr_gemeinde'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/gemeinde.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-gemeinde'
    __label__ = 'gemeindename'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    gemeindename = Column('gemeindename', Text)
    kanton = Column('kanton', Text)
    flaeche_ha = Column('flaeche_ha', Text)
    bfs_nr = Column('bfs_nr', Integer)
    pdf_liste = Column('pdf_liste', Text)
    abgabestelle = Column('abgabestelle', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-gemeinde', geometaGemeinde)


class geometaGrundbuch(Base, Vector):
    __tablename__ = 'amogr_grundbuch'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/grundbuch.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-grundbuch'
    __label__ = 'ortsteil_grundbuch'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    ortsteil_grundbuch = Column('ortsteil_grundbuch', Text)
    grundbuchfuehrung_d = Column('grundbuchfuehrung_d', Text)
    grundbuchfuehrung_f = Column('grundbuchfuehrung_f', Text)
    grundbuchfuehrung_i = Column('grundbuchfuehrung_i', Text)
    grundbuchkreis = Column('grundbuchkreis', Text)
    adresse = Column('adresse', Text)
    telefon = Column('telefon', Text)
    email = Column('email', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-grundbuch', geometaGrundbuch)


class geometaNfgeom(Base, Vector):
    __tablename__ = 'amogr_nfgeom'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/nfgeom.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-nfgeom'
    __label__ = 'name'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    name = Column('name', Text)
    firmenname = Column('firmenname', Text)
    adresse = Column('adresse', Text)
    telefon = Column('telefon', Text)
    email = Column('email', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-nfgeom', geometaNfgeom)


class oerebkataster(Base, Vector):
    __tablename__ = 'view_oereb_nfgeom'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/oerebkataster.mako'
    __bodId__ = 'ch.swisstopo-vd.stand-oerebkataster'
    __label__ = 'gemeindename'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    gemeindename = Column('gemeindename', Text)
    kanton = Column('kanton', Text)
    oereb_status_de = Column('oereb_status_de', Text)
    oereb_status_fr = Column('oereb_status_fr', Text)
    oereb_status_it = Column('oereb_status_it', Text)
    oereb_status_rm = Column('oereb_status_rm', Text)
    oereb_status_en = Column('oereb_status_en', Text)
    bfs_nr = Column('bfs_nr', Integer)
    firmenname = Column('firmenname', Text)
    adresszeile = Column('adresszeile', Text)
    plz = Column('plz', Integer)
    ort = Column('ort', Text)
    telefon = Column('telefon', Text)
    email = Column('email', Text)
    url_oereb = Column('url_oereb', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.stand-oerebkataster', oerebkataster)


class transformationBezugsrahmenHoehePunkte(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_pkt'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'name'
    __queryable_attributes__ = ['name']
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    y = Column('y', Numeric)
    x = Column('x', Numeric)
    or_ln02_cm = Column('or_ln02_cm', Numeric)
    the_geom = Column(Geometry2D)


class transformationBezugsrahmenHoeheLine5cm(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_line_5cm'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'contour'
    __maxscale__ = 500000
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    layer = Column('layer', Text)
    the_geom = Column(Geometry2D)


class transformationBezugsrahmenHoeheLine10cm(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_line_10cm'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'contour'
    __minscale__ = 500000
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    layer = Column('layer', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.transformation-bezugsrahmen_hoehe', transformationBezugsrahmenHoehePunkte)
register('ch.swisstopo.transformation-bezugsrahmen_hoehe', transformationBezugsrahmenHoeheLine5cm)
register('ch.swisstopo.transformation-bezugsrahmen_hoehe', transformationBezugsrahmenHoeheLine10cm)


class HebungsratenLine(Base, Vector):
    __tablename__ = 'hebungsraten_line'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/hebungsraten.mako'
    __bodId__ = 'ch.swisstopo.hebungsraten'
    __queryable_attributes__ = []
    __label__ = 'contour'
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry2D)


class HebungsratenPunkt(Base, Vector):
    __tablename__ = 'hebungsraten_pkt'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/hebungsraten.mako'
    __bodId__ = 'ch.swisstopo.hebungsraten'
    __queryable_attributes__ = ['ord_nr', 'ort']
    __label__ = 'ord_nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    ord_nr = Column('ord_nr', Text)
    ort = Column('ort', Text)
    v = Column('v', Numeric)
    mfv = Column('mfv', Numeric)
    klasse = Column('klasse', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.hebungsraten', HebungsratenLine)
register('ch.swisstopo.hebungsraten', HebungsratenPunkt)


class spannungsarmeGebiete(Base, Vector):
    __tablename__ = 'spannungsarme_gebiete'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/spannungsarme_gebiete.mako'
    __bodId__ = 'ch.swisstopo.transformationsgenauigkeit'
    __label__ = 'sg_name'
    id = Column('identifier', Unicode, primary_key=True)
    sg_name = Column('sg_name', Text)
    vali_date = Column('vali_date', DateTimeChsdi)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.transformationsgenauigkeit', spannungsarmeGebiete)


class spannungsarmeGebieteVD(spannungsarmeGebiete):
    __bodId__ = 'ch.swisstopo-vd.spannungsarme-gebiete'

register('ch.swisstopo-vd.spannungsarme-gebiete', spannungsarmeGebieteVD)


class geologieGeotopePunkte(Base, Vector):
    __tablename__ = 'geotope_pkt'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotope.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotope'
    __label__ = 'nom'
    id = Column('objectid', Integer, primary_key=True)
    nom = Column('nom', Text)
    fix_id = Column('fix_id', Text)
    nummer = Column('nummer', Integer)
    the_geom = Column(Geometry2D)


class geologieGeotopeFlaechen(Base, Vector):
    __tablename__ = 'geotope_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotope.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotope'
    __label__ = 'nom'
    id = Column('objectid', Integer, primary_key=True)
    nom = Column('nom', Text)
    fix_id = Column('fix_id', Text)
    nummer = Column('nummer', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotope', geologieGeotopePunkte)
register('ch.swisstopo.geologie-geotope', geologieGeotopeFlaechen)


class steine_hist_bauwerke(Base, Vector):
    __tablename__ = 'geotechnik_steine_historische_bauwerke'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geol_steine_hist_bauwerke.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke'
    __extended_info__ = True
    __label__ = 'objekt'
    id = Column('bgdi_id', Integer, primary_key=True)
    objekt = Column('objekt', Text)
    obtyp = Column('obtyp', Text)
    ort = Column('ort', Text)
    objektteil = Column('objektteil', Text)
    age = Column('age', Text)
    gestart = Column('gestart', Text)
    referenz = Column('referenz', Text)
    hyperlink = Column('hyperlink', Text)
    abbauort = Column('abbauort', Text)
    bemerkung = Column('bemerkung', Text)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke', steine_hist_bauwerke)


class GisGeolBase:
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __queryable_attributes__ = ['sgd_nr', 'orig_id', 'title', 'author', 'aux_info', 'doccreation']
    __label__ = 'title'
    __timeInstant__ = 'year'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', DateTimeChsdi)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    pdf_size = Column('pdf_size', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    year = Column('year', Integer)
    the_geom = Column(Geometry2D)


class gisgeol_punkte(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_points'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-punkte'

register('ch.swisstopo.geologie-gisgeol-punkte', gisgeol_punkte)


class gisgeol_linien(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_lines'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-linien'

register('ch.swisstopo.geologie-gisgeol-linien', gisgeol_linien)


class gisgeol_flaechen_1x1km(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1x1km'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1x1km'

register('ch.swisstopo.geologie-gisgeol-flaechen-1x1km', gisgeol_flaechen_1x1km)


class gisgeol_flaechen_10x10km(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10x10km'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10x10km'

register('ch.swisstopo.geologie-gisgeol-flaechen-10x10km', gisgeol_flaechen_10x10km)


class gisgeol_flaechen_10to100km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10to100km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10to100km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-10to100km2', gisgeol_flaechen_10to100km2)


class gisgeol_flaechen_100to1000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_100to1000km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2', gisgeol_flaechen_100to1000km2)


class gisgeol_flaechen_1000to21000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1000to21000km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2', gisgeol_flaechen_1000to21000km2)


class gisgeol_flaechen_gt21000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_gt21000km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2', gisgeol_flaechen_gt21000km2)


class gisgeol_flaechen_lt10km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_lt10km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-lt10km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2', gisgeol_flaechen_lt10km2)


class Geocover:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    the_geom = Column(Geometry2D)


class GeocoverFeatures(Geocover):
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    __maxscale__ = 70000
    __queryable_attributes__ = []


class GeocoverLineAux(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_line_aux'
    __template__ = 'templates/htmlpopup/geocover_line_aux.mako'
    spec_description = Column('spec_description', Text)


class GeocoverPointHydro(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_hydro'
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)


class GeocoverPointGeol(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_geol'
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)


class GeocoverPointDrill(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_drill'
    __template__ = 'templates/htmlpopup/geocover_point_drill.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth_1 = Column('depth_1', Text)
    description_1 = Column('description_1', Text)
    depth_2 = Column('depth_2', Text)
    description_2 = Column('description_2', Text)


class GeocoverPointInfo(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_info'
    __template__ = 'templates/htmlpopup/geocover_point_info.mako'


class GeocoverPointStruct(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_struct'
    __template__ = 'templates/htmlpopup/geocover_point_struct.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    dip = Column('dip', Text)


class GeocoverPolygonAux1(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_polygon_aux_1'
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    tecto = Column('tecto', Text)


class GeocoverPolygonAux2(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_polygon_aux_2'
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    tecto = Column('tecto', Text)


class GeocoverPolygonMain(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_polygon_main'
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    tecto = Column('tecto', Text)


class GeocoverGridShop (Base, Geocover, ShopProductGroupClass, Vector):
    __tablename__ = 'view_geocover_grid_shop'
    __minscale__ = 70000


register('ch.swisstopo.geologie-geocover', GeocoverLineAux)
register('ch.swisstopo.geologie-geocover', GeocoverPointHydro)
register('ch.swisstopo.geologie-geocover', GeocoverPointGeol)
register('ch.swisstopo.geologie-geocover', GeocoverPointDrill)
register('ch.swisstopo.geologie-geocover', GeocoverPointInfo)
register('ch.swisstopo.geologie-geocover', GeocoverPointStruct)
register('ch.swisstopo.geologie-geocover', GeocoverPolygonAux1)
register('ch.swisstopo.geologie-geocover', GeocoverPolygonAux2)
register('ch.swisstopo.geologie-geocover', GeocoverPolygonMain)
register('ch.swisstopo.geologie-geocover', GeocoverGridShop)
register_perimeter('ch.swisstopo.geologie-geocover', GeocoverGridShop)


class GeolGeocoverMetadata(Base, Geocover, ShopProductGroupClass, Vector):
    __tablename__ = 'view_geocover_grid_shop'
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.geologie-geocover.metadata'
    __label__ = 'name_de'


register('ch.swisstopo.geologie-geocover.metadata', GeolGeocoverMetadata)


class Ga25Atlas:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    the_geom = Column(Geometry2D)


class Ga25Features(Ga25Atlas):
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    __maxscale__ = 70000
    __queryable_attributes__ = []


class Ga25LineAux(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_line_aux'
    __template__ = 'templates/htmlpopup/ga25_line_aux.mako'
    spec_description = Column('spec_description', Text)
    url_legend = Column('url_legende', Text)


class Ga25PointHydro(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_hydro'
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)
    url_legend = Column('url_legende', Text)


class Ga25PointGeol(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_geol'
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)
    url_legend = Column('url_legende', Text)


class Ga25PointDrill(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_drill'
    __template__ = 'templates/htmlpopup/ga25_point_drill.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth_1 = Column('depth_1', Text)
    description_1 = Column('description_1', Text)
    depth_2 = Column('depth_2', Text)
    description_2 = Column('description_2', Text)
    url_legend = Column('url_legende', Text)


class Ga25PointInfo(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_info'
    __template__ = 'templates/htmlpopup/ga25_point_info.mako'
    url_legend = Column('url_legende', Text)


class Ga25PointStruct(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_struct'
    __template__ = 'templates/htmlpopup/ga25_point_struct.mako'
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    dip = Column('dip', Text)
    url_legend = Column('url_legende', Text)


class Ga25PolygonAux1(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_polygon_aux_1'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Text)
    url_legend = Column('url_legende', Text)


class Ga25PolygonAux2(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_polygon_aux_2'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Text)
    url_legend = Column('url_legende', Text)


class Ga25PolygonMain(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_polygon_main'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Text)
    url_legend = Column('url_legende', Text)


class Ga25GridShop(Base, Ga25Atlas, ShopProductGroupClass, Vector):
    __tablename__ = 'view_ga25_grid_shop'
    __minscale__ = 70000


register('ch.swisstopo.geologie-geologischer_atlas', Ga25LineAux)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointHydro)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointGeol)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointDrill)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointInfo)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointStruct)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PolygonAux1)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PolygonAux2)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PolygonMain)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25GridShop)
register_perimeter('ch.swisstopo.geologie-geologischer_atlas', Ga25GridShop)


class Swissnames3d:
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __label__ = 'name'
    __template__ = 'templates/htmlpopup/swissnames3d.mako'
    __bodId__ = 'ch.swisstopo.swissnames3d'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Text)
    objektklasse = Column('objektklasse', Text)
    name = Column('name', Text)
    sprachcode = Column('sprachcode', Text)
    namen_typ = Column('namen_typ', Text)
    the_geom = Column(Geometry2D)


class Swissnames3dRaster00(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_00'
    __maxscale__ = 25000000
    __minscale__ = 2100000


class Swissnames3dRaster01(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_01'
    __maxscale__ = 2100000
    __minscale__ = 1700000


class Swissnames3dRaster02(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_02'
    __maxscale__ = 1700000
    __minscale__ = 940000


class Swissnames3dRaster03(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_03'
    __maxscale__ = 940000
    __minscale__ = 370000


class Swissnames3dRaster04(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_04'
    __maxscale__ = 370000
    __minscale__ = 180000


class Swissnames3dRaster05(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_05'
    __maxscale__ = 180000
    __minscale__ = 75000


class Swissnames3dRaster06(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_06'
    __maxscale__ = 75000
    __minscale__ = 35000


class Swissnames3dRaster07(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_07'
    __maxscale__ = 35000
    __minscale__ = 18000


class Swissnames3dRaster08(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_08'
    __maxscale__ = 18000
    __minscale__ = 9000


class Swissnames3dRaster09(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_09'
    __maxscale__ = 9000
    __minscale__ = 7000


class Swissnames3dRaster10(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_10'
    __maxscale__ = 7000
    __minscale__ = 3500


class Swissnames3dRaster11(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_11'
    __maxscale__ = 3500
    __minscale__ = 1800


class Swissnames3dRaster12(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_12'
    __maxscale__ = 1800
    __minscale__ = 900


class Swissnames3dRaster13(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_13'
    __maxscale__ = 900
    __minscale__ = 1


register('ch.swisstopo.swissnames3d', Swissnames3dRaster00)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster01)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster02)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster03)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster04)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster05)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster06)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster07)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster08)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster09)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster10)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster11)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster12)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster13)


# Perimeter only layers


class SwissTLM3dPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_swisstlm3d'
    __table_args__ = ({'autoload': False})
    __bodId__ = 'ch.swisstopo.swisstlm3d-karte-farbe'
    __totalArea__ = 41455.0
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisstlm3d-karte-farbe', SwissTLM3dPerimeter)


class SwissAlti3dPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_swissalti3d'
    __table_args__ = ({'autoload': False})
    __bodId__ = 'ch.swisstopo.swissalti3d-reliefschattierung'
    __totalArea__ = 41455.0
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissalti3d-reliefschattierung', SwissAlti3dPerimeter)


class DHM25(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_dhm25'
    __table_args__ = ({'autoload': False})
    __bodId__ = 'ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'
    the_geom = Column(Geometry2D)


class DHM25Perimeter(Base, Vector):
    __tablename__ = 'shop_perimeter_dhm25'
    __table_args__ = ({'autoload': False})
    __bodId__ = 'ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung'
    __totalArea__ = 58500.0
    id = Column('min', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung', DHM25)
register_perimeter('ch.swisstopo.digitales-hoehenmodell_25_reliefschattierung', DHM25Perimeter)


class spotMosaicPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'view_gridstand_spot5_metadata'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.images-spot-5.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.images-spot-5.metadata', spotMosaicPerimeter)


class SwissAlti3dMetadataPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_swissalti3d'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.swissalti3d.metadata'
    __totalArea__ = 41455.0
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissalti3d.metadata', SwissAlti3dMetadataPerimeter)


class SwissTlm3dMetadataPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_swisstlm3d'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.swisstlm3d.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisstlm3d.metadata', SwissTlm3dMetadataPerimeter)


class SwissBuildings3d1MetadataPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_swissbuildings3d'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.swissbuildings3d_1.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissbuildings3d_1.metadata', SwissBuildings3d1MetadataPerimeter)


class Dhm25MetadataPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_dhm25'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.digitales-hoehenmodell_25.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.digitales-hoehenmodell_25.metadata', Dhm25MetadataPerimeter)


class SwissBuildings3d2Perimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_build3d2'
    __table_args__ = ({'autoload': False})
    __bodId__ = 'ch.swisstopo.swissbuildings3d_2.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissbuildings3d_2.metadata', SwissBuildings3d2Perimeter)


class SwissBuildings3dPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_swissbuildings3d'
    __table_args__ = ({'autoload': False})
    __bodId__ = 'ch.swisstopo.swissbuildings3d'
    __totalArea__ = 41455.0
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissbuildings3d', SwissBuildings3dPerimeter)


class Lotabweichungen(Base, Vector):
    __tablename__ = 'lotabweichungen_nur_punkte'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/lotabweichungen.mako'
    __bodId__ = 'ch.swisstopo.lotabweichungen'
    __label__ = 'name'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode)
    land = Column('land', Unicode)
    messjahr = Column('messjahr', Integer)
    instrument = Column('instrument', Unicode)
    xi_ch = Column('xi_ch', Float)
    eta_ch = Column('eta_ch', Float)
    xi_etrf = Column('xi_etrf', Float)
    eta_etrf = Column('eta_etrf', Float)
    symbol = Column('symbol', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.lotabweichungen', Lotabweichungen)


class HiksDufourMetadata(Base, ShopStandardClass, Vector):
    __tablename__ = 'view_gridstand_dufour_shop'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.hiks-dufour.metadata'
    number = Column('s_map_number', Unicode)
    scale = Column('scale', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.hiks-dufour.metadata', HiksDufourMetadata)


class HiksSiegfriedTa25Metadata(Base, ShopStandardClass, Vector):
    __tablename__ = 'view_gridstand_siegfried_ta25_shop'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.hiks-siegfried-ta25.metadata'
    number = Column('s_map_number', Unicode)
    scale = Column('scale', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.hiks-siegfried-ta25.metadata', HiksSiegfriedTa25Metadata)


class HiksSiegfriedTa50Metadata(Base, ShopStandardClass, Vector):
    __tablename__ = 'view_gridstand_siegfried_ta50_shop'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.hiks-siegfried-ta50.metadata'
    number = Column('s_map_number', Unicode)
    scale = Column('scale', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.hiks-siegfried-ta50.metadata', HiksSiegfriedTa50Metadata)
