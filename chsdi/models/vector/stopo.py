# -*- coding: utf-8 -*-

from sqlalchemy import Column

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
    ads_name = Column('ads_name', Unicode)
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
    nr_lsn2004 = Column('nr_lsn2004', Unicode)
    name = Column('name', Unicode)
    label_tt = Column('label', Unicode)
    type = Column('type', Unicode)
    lat_etrs = Column('lat_etrs', Numeric)
    lon_etrs = Column('lon_etrs', Numeric)
    y_lv03 = Column('y_lv03', Numeric)
    x_lv03 = Column('x_lv03', Numeric)
    h_ln02 = Column('h_ln02', Numeric)
    gravity = Column('gravity', Numeric)
    rms = Column('rms', Numeric)
    vert_grad = Column('vert_grad', Numeric)
    link_hfp_title = Column('link_hfp_title', Unicode)
    link_hfp_url = Column('link_hfp_url', Unicode)
    link_lfp_title = Column('link_lfp_title', Unicode)
    link_lfp_url = Column('link_lfp_url', Unicode)
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
    nr_lsn2004 = Column('nr_lsn2004', Unicode)
    name = Column('name', Unicode)
    label_tt = Column('label', Unicode)
    type = Column('type', Unicode)
    lat_etrs = Column('lat_etrs', Numeric)
    lon_etrs = Column('lon_etrs', Numeric)
    y_lv03 = Column('y_lv03', Numeric)
    x_lv03 = Column('x_lv03', Numeric)
    h_ln02 = Column('h_ln02', Numeric)
    gravity = Column('gravity', Numeric)
    rms = Column('rms', Numeric)
    vert_grad = Column('vert_grad', Numeric)
    link_hfp_title = Column('link_hfp_title', Unicode)
    link_hfp_url = Column('link_hfp_url', Unicode)
    link_lfp_title = Column('link_lfp_title', Unicode)
    link_lfp_url = Column('link_lfp_url', Unicode)
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
    stationnam = Column('stationnam', Unicode)
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
    titel_1 = Column('titel_1', Unicode)
    titel_2 = Column('titel_2', Unicode)
    link = Column('link', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geowege', GeologieGeowege)


class ShopProductClass:
    __template__ = 'templates/htmlpopup/shop_product.mako'
    __label__ = 'id'
    __queryable_attributes__ = ['release']
    id = Column('pk_product', Unicode, primary_key=True)
    scale = Column('scale', Integer)
    release = Column('release', Integer)
    data = Column('data', Integer)
    isbn = Column('s_isbn', Unicode)
    author = Column('s_author', Unicode)
    available = Column('available', Boolean)
    the_geom = Column(Geometry2D)


class ShopStandardClass:
    __template__ = 'templates/htmlpopup/shop_product.mako'
    id = Column('pk_product', Unicode, primary_key=True)
    available = Column('available', Boolean)
    name_de = Column('s_title_de', Unicode)
    name_fr = Column('s_title_fr', Unicode)
    name_it = Column('s_title_it', Unicode)
    name_en = Column('s_title_en', Unicode)


class GravimetrischerAtlasPapierMetadata(Base, ShopProductClass, Vector):
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


class Icao500DigitalMeta(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __tablename__ = 'icao500_digital'
    __bodId__ = 'ch.swisstopo.luftfahrtkarten-icao.metadata'
    name_de = Column('s_title_de', Unicode)
    name_fr = Column('s_title_fr', Unicode)
    name_it = Column('s_title_it', Unicode)
    name_en = Column('s_title_en', Unicode)

register('ch.swisstopo.luftfahrtkarten-icao.metadata', Icao500DigitalMeta)


class SegelFlug300DigitalMeta(Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __tablename__ = 'segelflugkarte'
    __bodId__ = 'ch.swisstopo.segelflugkarte.metadata'
    name_de = Column('s_title_de', Unicode)
    name_fr = Column('s_title_fr', Unicode)
    name_it = Column('s_title_it', Unicode)
    name_en = Column('s_title_en', Unicode)

register('ch.swisstopo.segelflugkarte.metadata', SegelFlug300DigitalMeta)


class ShopProductGroupClass(ShopProductClass):
    __label__ = 'number'
    __queryable_attributes__ = ['number', 'name_de', 'name_fr', 'name_it', 'name_en', 'release']
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


class GeolAtlasVectorMetadata(Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gav25'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas_vector.metadata'

register('ch.swisstopo.geologie-geologischer_atlas_vector.metadata', GeolAtlasVectorMetadata)


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


class GeolGenKarteGGK200Meta(Base, ShopProductGroupClass, Vector):
    __tablename__ = 'view_gridstand_ggk_shop'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-generalkarte-ggk200.metadata'

register('ch.swisstopo.geologie-generalkarte-ggk200.metadata', GeolGenKarteGGK200Meta)


class Ga25Meta(Base, ShopProductGroupClass, Vector):
    __tablename__ = 'view_ga25_grid_shop'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas.metadata'

register('ch.swisstopo.geologie-geologischer_atlas.metadata', Ga25Meta)


class GeolSpezialKartenVectorMeta(Base, ShopProductGroupClass, Vector):
    __tablename__ = 'view_gsk_vector'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata'

register('ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata', GeolSpezialKartenVectorMeta)


class GeolSpezialKartenMetadata(Base, ShopProductGroupClass, Vector):
    __tablename__ = 'view_gsk_raster'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-spezialkarten_schweiz.metadata'

register('ch.swisstopo.geologie-spezialkarten_schweiz.metadata', GeolSpezialKartenMetadata)


class SwissboundariesBezirk(Base, Vector):
    __tablename__ = 'swissboundaries_bezirke'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_bezirk.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode)
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
    gemname = Column('gemname', Unicode)
    gemflaeche = Column('gemflaeche', Numeric)
    perimeter = Column('perimeter', Numeric)
    kanton = Column('kanton', Unicode)
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
    ak = Column('ak', Unicode)
    name = Column('name', Unicode)
    flaeche = Column('flaeche', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissboundaries3d-kanton-flaeche.fill', SwissboundariesKanton)


class SwissBoundariesLand(Base, Vector):
    __tablename__ = 'swissboundaries_land'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __bodId__ = 'ch.swisstopo.swissboundaries3d-land-flaeche.fill'
    id = Column('bgdi_id', Integer, primary_key=True)
    displayname = Column('displayname', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissboundaries3d-land-flaeche.fill', SwissBoundariesLand)


class Vec200Terminal(Base, Vector):
    __tablename__ = 'vec200_terminal'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_terminal.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    objval = Column('objval', Unicode)
    the_geom = Column(Geometry2D)


class Vec200ShipKursschiff(Base, Vector):
    __tablename__ = 'v200_ship_kursschiff_linie_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ship_kursschiff_linie.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    objval = Column('objval', Unicode)
    detn = Column('detn', Unicode)
    rsu = Column('rsu', Unicode)
    use = Column('use', Unicode)
    the_geom = Column(Geometry2D)


class Vec200Railway(Base, Vector):
    __tablename__ = 'vec200_railway'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_railway.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    objval = Column('objval', Unicode)
    construct = Column('construct', Unicode)
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
    objname = Column('objname', Unicode)
    objval = Column('objval', Unicode)
    the_geom = Column(Geometry2D)


class Vec200ShipAutofaehre(Base, Vector):
    __tablename__ = 'v200_ship_autofaehre_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ship_autofaehre.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'detn'
    id = Column('gtdboid', Unicode, primary_key=True)
    use = Column('use', Unicode)
    rsu = Column('rsu', Unicode)
    detn = Column('detn', Unicode)
    the_geom = Column(Geometry2D)


class Vec200Road(Base, Vector):
    __tablename__ = 'vec200_road'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_road.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    construct = Column('construct', Unicode)
    objval = Column('objval', Unicode)
    toll = Column('toll', Unicode)
    the_geom = Column(Geometry2D)


class Vec200Ramp(Base, Vector):
    __tablename__ = 'vec200_ramp'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ramp.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objval'
    id = Column('gtdboid', Unicode, primary_key=True)
    construct = Column('construct', Unicode)
    objval = Column('objval', Unicode)
    toll = Column('toll', Unicode)
    the_geom = Column(Geometry2D)


class Vec200Customsoffice(Base, Vector):
    __tablename__ = 'vec200_customsoffice'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_customsoffice.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'ojbname'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname = Column('objname', Unicode)
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
    name = Column('name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-adminboundaries-protectedarea', Vec200Protectedarea)


class Vec200Flowingwater(Base, Vector):
    __tablename__ = 'vec200_flowingwater'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_flowingwater.mako'
    __bodId__ = 'ch.swisstopo.vec200-hydrography'
    __label__ = 'name'
    id = Column('gtdboid', Unicode, primary_key=True)
    name = Column('name', Unicode)
    exs = Column('exs', Unicode)
    hoc = Column('hoc', Unicode)
    the_geom = Column(Geometry2D)


class Vec200Stagnantwater(Base, Vector):
    __tablename__ = 'vec200_stagnantwater'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_stagnantwater.mako'
    __bodId__ = 'ch.swisstopo.vec200-hydrography'
    __label__ = 'name'
    id = Column('gtdboid', Unicode, primary_key=True)
    name = Column('name', Unicode)
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
    objname1 = Column('objname1', Unicode)
    objval = Column('objval', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-landcover', Vec200Landcover)


class Vec200Builtupp(Base, Vector):
    __tablename__ = 'vec200_builtupp'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_builtupp.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'objname'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname = Column('objname', Unicode)
    ppi = Column('ppi', Unicode)
    the_geom = Column(Geometry2D)


class Vec200Poi(Base, Vector):
    __tablename__ = 'v200_poi_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_poi.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'objname'
    id = Column('gtdboid', Unicode, primary_key=True)
    objname = Column('objname', Unicode)
    objval = Column('objval', Unicode)
    ppc = Column('ppc', Unicode)
    pro = Column('pro', Unicode)
    the_geom = Column(Geometry2D)


class Vec200Supply(Base, Vector):
    __tablename__ = 'vec200_supply'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_supply.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'fco'
    id = Column('gtdboid', Unicode, primary_key=True)
    fco = Column('fco', Unicode)
    loc = Column('loc', Unicode)
    pro = Column('pro', Unicode)
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
    objname1 = Column('objname1', Unicode)
    objname2 = Column('objname2', Unicode)
    altitude = Column('altitude', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec200-names-namedlocation', Vec200Namedlocation)


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
    nom = Column('nom', Unicode)
    num = Column('num', Unicode)
    type = Column('type', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.dreiecksvermaschung', Dreiecksvermaschung)

# Gridstands PK layers noscale and metadata


class GridstandTemplate:
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __label__ = 'lk_name'
    id = Column('kbnum', Unicode, primary_key=True)
    lk_name = Column('lk_name', Unicode)
    datenstand = Column('release', Integer)
    the_geom = Column(Geometry2D)


class GridstandPermiterTemplate:
    __table_args__ = ({'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


# PK 25


class GridstandPK25Perimeter(Base, Vector):
    __tablename__ = 'shop_perimeter_pk25'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk25.noscale'
    __table_args__ = ({'autoload': False})
    the_geom = Column(Geometry2D)
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class GridstandPk25Meta(Base, GridstandTemplate, ShopStandardClass, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk25.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk25_tilecache'
    tileid = Column('tileid', Unicode)


register('ch.swisstopo.pixelkarte-pk25.metadata', GridstandPk25Meta)
register_perimeter('ch.swisstopo.pixelkarte-farbe-pk25.noscale', GridstandPK25Perimeter)

# PK 50


# Only PK50 has a fixed perimeter
class GridstandPK50Perimeter(Base, Vector):
    __tablename__ = 'shop_perimeter_pk50'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk50.noscale'
    __totalArea__ = 65520.0
    __table_args__ = ({'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class GridstandPk50Meta(Base, GridstandTemplate, ShopStandardClass, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk50.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk50_tilecache'
    tileid = Column('tileid', Unicode)


register('ch.swisstopo.pixelkarte-pk50.metadata', GridstandPk50Meta)
register_perimeter('ch.swisstopo.pixelkarte-farbe-pk50.noscale', GridstandPK50Perimeter)

# PK 100


class GridstandPK100Perimeter(Base, Vector):
    __tablename__ = 'shop_perimeter_pk100'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk100.noscale'
    __table_args__ = ({'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class GridstandPk100Meta(Base, GridstandTemplate, ShopStandardClass, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk100.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk100_tilecache'
    tileid = Column('tileid', Unicode)

register('ch.swisstopo.pixelkarte-pk100.metadata', GridstandPk100Meta)
register_perimeter('ch.swisstopo.pixelkarte-farbe-pk100.noscale', GridstandPK100Perimeter)

# PK 200


class GridstandPK200Perimeter(Base, Vector):
    __tablename__ = 'shop_perimeter_pk200'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk200.noscale'
    __table_args__ = ({'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class GridstandPk200Meta(Base, GridstandTemplate, ShopStandardClass, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk200.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk200_tilecache'
    tileid = Column('tileid', Unicode)

register('ch.swisstopo.pixelkarte-pk200.metadata', GridstandPk200Meta)
register_perimeter('ch.swisstopo.pixelkarte-farbe-pk200.noscale', GridstandPK200Perimeter)

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
    lk25_name  = Column('lk25_name', Unicode)
    datenstand = Column('datenstand', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.images-swissimage.metadata', GridstandSwissimage)


class SwissimageProduct(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_swissimage'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __bodId__ = 'ch.swisstopo.swissimage-product'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissimage-product', SwissimageProduct)
register_perimeter('ch.swisstopo.swissimage-product', SwissimageProductPerimeter)


class GeologischeKarteLine(Base, Vector):
    __tablename__ = 'geologische_karte_line'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologische_karte_line.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologische_karte'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('fid', Integer, primary_key=True)
    gid = Column('id', Integer)
    type_de = Column('type_de', Unicode)
    type_fr = Column('type_fr', Unicode)
    the_geom = Column(Geometry2D)


class GeologischeKartePlg(Base, Vector):
    __tablename__ = 'geologische_karte_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologische_karte_plg.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologische_karte'
    __label__ = 'leg_geol_d'
    id = Column('id', Integer, primary_key=True)
    leg_geol_d = Column('leg_geol_d', Unicode)
    leg_geol_f = Column('leg_geol_f', Unicode)
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
    legend = Column('legend', Unicode)
    area_name = Column('area_name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200', GeologieMineralischeRohstoffe200)


class GeologieBohrungenTiefer500(Base, Vector):
    __tablename__ = 'bohrungen_500'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/bohrungen_tiefer_500.mako'
    __bodId__ = 'ch.swisstopo.geologie-bohrungen_tiefer_500'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    auftraggeb_de = Column('auftraggeb_de', Unicode)
    auftraggeb_fr = Column('auftraggeb_fr', Unicode)
    auftraggeb_en = Column('auftraggeb_en', Unicode)
    auftraggeb_it = Column('auftraggeb_it', Unicode)
    auftraggeb_rm = Column('auftraggeb_rm', Unicode)
    rechtein_de = Column('rechtein_de', Unicode)
    rechtein_fr = Column('rechtein_fr', Unicode)
    rechtein_en = Column('rechtein_en', Unicode)
    rechtein_it = Column('rechtein_it', Unicode)
    rechtein_rm = Column('rechtein_rm', Unicode)
    inhalt_de = Column('inhalt_de', Unicode)
    inhalt_fr = Column('inhalt_fr', Unicode)
    inhalt_en = Column('inhalt_en', Unicode)
    inhalt_it = Column('inhalt_it', Unicode)
    inhalt_rm = Column('inhalt_rm', Unicode)
    download = Column('download', Unicode)
    auskunft_de = Column('auskunft_de', Unicode)
    auskunft_fr = Column('auskunft_fr', Unicode)
    auskunft_en = Column('auskunft_en', Unicode)
    auskunft_it = Column('auskunft_it', Unicode)
    auskunft_rm = Column('auskunft_rm', Unicode)
    tiefe_md = Column('tiefe_md', Float)
    bohrzweck_de = Column('bohrzweck_de', Unicode)
    bohrzweck_fr = Column('bohrzweck_fr', Unicode)
    bohrzweck_en = Column('bohrzweck_en', Unicode)
    bohrzweck_it = Column('bohrzweck_it', Unicode)
    bohrzweck_rm = Column('bohrzweck_rm', Unicode)
    status_de = Column('status_de', Unicode)
    status_fr = Column('status_fr', Unicode)
    status_en = Column('status_en', Unicode)
    status_it = Column('status_it', Unicode)
    status_rm = Column('status_rm', Unicode)
    startdate_de = Column('startdate_de', Unicode)
    startdate_fr = Column('startdate_fr', Unicode)
    startdate_en = Column('startdate_en', Unicode)
    startdate_it = Column('startdate_it', Unicode)
    startdate_rm = Column('startdate_rm', Unicode)
    enddate_de = Column('enddate_de', Unicode)
    enddate_fr = Column('enddate_fr', Unicode)
    enddate_en = Column('enddate_en', Unicode)
    enddate_it = Column('enddate_it', Unicode)
    enddate_rm = Column('enddate_rm', Unicode)
    height = Column('height', Float)
    land_de = Column('land_de', Unicode)
    land_fr = Column('land_fr', Unicode)
    land_en = Column('land_en', Unicode)
    land_it = Column('land_it', Unicode)
    land_rm = Column('land_rm', Unicode)
    kanton_de = Column('kanton_de', Unicode)
    kanton_fr = Column('kanton_fr', Unicode)
    kanton_en = Column('kanton_en', Unicode)
    kanton_it = Column('kanton_it', Unicode)
    kanton_rm = Column('kanton_rm', Unicode)
    koord_e = Column('koord_e', Float)
    koord_n = Column('koord_n', Float)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-bohrungen_tiefer_500', GeologieBohrungenTiefer500)


class GeologieGeotechnikGk200(Base, Vector):
    __tablename__ = 'geotechnik_gk200_lgd'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotechnik_gk200.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk200'
    __label__ = 'file_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    file_name = Column('file_name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk200', GeologieGeotechnikGk200)


class TiefenGeothermieProjekte(Base, Vector):
    __tablename__ = 'tiefengeothermie_projekte'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/tiefengeothermie_projekte.mako'
    __bodId__ = 'ch.swisstopo.geologie-tiefengeothermie_projekte'
    __label__ = 'name'
    __extended_info__ = True
    __queryable_attributes__ = ['name']
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    owner = Column('owner', Unicode)
    status = Column('status', Unicode)
    system = Column('system', Unicode)
    use = Column('use', Unicode)
    canton = Column('canton', Unicode)
    community = Column('community', Unicode)
    depth = Column('depth', Integer)
    temp = Column('temp', Unicode)
    power = Column('power', Unicode)
    produc = Column('produc', Unicode)
    weblink = Column('weblink', Unicode)
    id_project = Column('id_project', Unicode)

    the_geom = Column(Geometry2D)

register(TiefenGeothermieProjekte.__bodId__, TiefenGeothermieProjekte)


class Gk500Gensese (Base, Vector):
    __tablename__ = 'gk500_genese'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gk500-genese.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-genese'
    # Translatable labels in fr, it, rm, it
    __label__ = 'genese_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    genese_de = Column('genese_de', Unicode)
    genese_fr = Column('genese_fr', Unicode)
    genese_en = Column('genese_en', Unicode)
    genese_it = Column('genese_it', Unicode)
    genese_rm = Column('genese_rm', Unicode)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk500-genese', Gk500Gensese)


class Gk500Gesteinsklassierung (Base, Vector):
    __tablename__ = 'gk500_gesteinsklassierung'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gk500-gesteinsklassierung.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-gesteinsklassierung'
    __label__ = 'gestkl_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    # Translatable labels in fr, it, rm, it
    __label__ = 'gestkl_de'
    gestkl_de = Column('gestkl_de', Unicode)
    gestkl_fr = Column('gestkl_fr', Unicode)
    gestkl_en = Column('gestkl_en', Unicode)
    gestkl_it = Column('gestkl_it', Unicode)
    gestkl_rm = Column('gestkl_rm', Unicode)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk500-gesteinsklassierung', Gk500Gesteinsklassierung)


class Gk500LithologieHauptgruppen(Base, Vector):
    __tablename__ = 'gk500_lithologie_hauptgruppen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/lithologie_hauptgruppen.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-lithologie_hauptgruppen'
    # Translatable labels in fr, it, rm, it
    __label__ = 'bgdi_tooltip_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    bgdi_tooltip_de = Column('bgdi_tooltip_de', Unicode)
    bgdi_tooltip_fr = Column('bgdi_tooltip_fr', Unicode)
    bgdi_tooltip_en = Column('bgdi_tooltip_en', Unicode)
    bgdi_tooltip_it = Column('bgdi_tooltip_it', Unicode)
    bgdi_tooltip_rm = Column('bgdi_tooltip_rm', Unicode)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-gk500-lithologie_hauptgruppen', Gk500LithologieHauptgruppen)


class GeologieGeotechnikSteinbrueche1915(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1915'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1915.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1915'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Unicode)
    gestein = Column('gestein', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1915', GeologieGeotechnikSteinbrueche1915)


class GeologieGeotechnikSteinbrueche1965(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1965'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1965'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Unicode)
    gestein = Column('gestein', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1965', GeologieGeotechnikSteinbrueche1965)


class GeologieGeotechnikSteinbrueche1980(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1980'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1980.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1980'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Unicode)
    gestein = Column('gestein', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1980', GeologieGeotechnikSteinbrueche1980)


class GeologieGeotechnikSteinbrueche1995(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1995'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1995'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Unicode)
    gestein = Column('gestein', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1995', GeologieGeotechnikSteinbrueche1995)


class GeologieGeotechnikZementindustrie1965(Base, Vector):
    __tablename__ = 'geotechnik_zementindustrie'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/zementindustrie_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-zementindustrie_1965'
    __label__ = 'stoff'
    id = Column('id', Integer, primary_key=True)
    stoff = Column('stoff', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-zementindustrie_1965', GeologieGeotechnikZementindustrie1965)


class GeologieGeotechnikZementindustrie1995(Base, Vector):
    __tablename__ = 'geotechnik_zementindustrie'
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/zementindustrie_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-zementindustrie_1995'
    __label__ = 'stoff'
    id = Column('id', Integer, primary_key=True)
    stoff = Column('stoff', Unicode)
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
    ziegelei_2 = Column('ziegelei_2', Unicode)
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
    ziegelei = Column('ziegelei', Unicode)
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
    ziegeleien = Column('ziegeleien', Unicode)
    produkt = Column('produkt', Unicode)
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
    type_de = Column('type_de', Unicode)
    type_fr = Column('type_fr', Unicode)
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
    type_de = Column('type_de', Unicode)
    type_fr = Column('type_fr', Unicode)
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


class GeologischerAeromagnetikJura(Base, Vector):
    __tablename__ = 'gravimetrie_aeromagnetik_jura'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetik_jura.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-aeromagnetische_karte_jura'
    __label__ = 'et_fromatt'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-aeromagnetische_karte_jura', GeologischerAeromagnetikJura)


class GeologischerAeromagnetikCh(Base, Vector):
    __tablename__ = 'gravimetrie_aeromagnetik_ch'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetik_schweiz.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz'
    __label__ = 'fid'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz', GeologischerAeromagnetikCh)


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
    rohstoff = Column('rohstoff', Unicode)
    name_ads = Column('name_ads', Unicode)
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
    rohstoff = Column('rohstoff', Unicode)
    name_ads = Column('name_ads', Unicode)
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
    rohstoff = Column('rohstoff', Unicode)
    name_ads = Column('name_ads', Unicode)
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
    type_de = Column('type_de', Unicode)
    type_fr = Column('type_fr', Unicode)
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
    type_de = Column('type_de', Unicode)
    type_fr = Column('type_fr', Unicode)
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
    ads_name = Column('ads_name', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-eiszeit-lgm', GeologieEiszeitLgm)


class Swisstlm3dEisenbahn50000(Base, Vector):
    __tablename__ = 'eisenbahn_50000_tooltip'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-eisenbahn.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-eisenbahnnetz'
    __label__ = 'objektart'
    __minscale__ = 50000
    id = Column('bgdi_id', Integer, primary_key=True)
    objectid = Column('objectid', Integer)
    objektart = Column('objektart', Integer)
    verkehrsmittel = Column('verkehrsmittel', Integer)
    standseilbahn = Column('standseilbahn', Integer)
    zahnradbahn = Column('zahnradbahn', Integer)
    ausser_betrieb = Column('ausser_betrieb', Integer)
    the_geom = Column(Geometry2D)


class Swisstlm3dEisenbahn(Base, Vector):
    __tablename__ = 'eisenbahn'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-eisenbahn.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-eisenbahnnetz'
    __label__ = 'objektart'
    __maxscale__ = 50000
    id = Column('bgdi_id', Integer, primary_key=True)
    objectid = Column('objectid', Integer)
    objektart = Column('objektart', Integer)
    verkehrsmittel = Column('verkehrsmittel', Integer)
    standseilbahn = Column('standseilbahn', Integer)
    zahnradbahn = Column('zahnradbahn', Integer)
    ausser_betrieb = Column('ausser_betrieb', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisstlm3d-eisenbahnnetz', Swisstlm3dEisenbahn50000)
register('ch.swisstopo.swisstlm3d-eisenbahnnetz', Swisstlm3dEisenbahn)


class Swisstlm3dUebrigerverkehr25000(Base, Vector):
    __tablename__ = 'uebrige_bahn_25000_tooltip'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-uebrige_bahn.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-uebrigerverkehr'
    __label__ = 'objektart'
    __minscale__ = 25000
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Integer)
    name = Column('name', Unicode)
    ausser_betrieb = Column('ausser_betrieb', Integer)
    the_geom = Column(Geometry2D)


class Swisstlm3dUebrigerverkehr(Base, Vector):
    __tablename__ = 'uebrige_bahn'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-uebrige_bahn.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-uebrigerverkehr'
    __label__ = 'objektart'
    __maxscale__ = 25000
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Integer)
    name = Column('name', Unicode)
    ausser_betrieb = Column('ausser_betrieb', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisstlm3d-uebrigerverkehr', Swisstlm3dUebrigerverkehr25000)
register('ch.swisstopo.swisstlm3d-uebrigerverkehr', Swisstlm3dUebrigerverkehr)


class Swisstlm3dGewaessernetz(Base, Vector):
    __tablename__ = 'gewaessernetz_tooltip'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-fliessgewaesser.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-gewaessernetz'
    __label__ = 'objektart'
    id = Column('id', Integer, primary_key=True)
    objektart = Column('objektart', Integer)
    name = Column('name', Unicode)
    gwl_nr = Column('gwl_nr', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisstlm3d-gewaessernetz', Swisstlm3dGewaessernetz)


class Swisstlm3dStrassen500000(Base, Vector):
    __tablename__ = 'strasse_500000_tooltip'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-strassen.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-strassen'
    __label__ = 'objektart'
    __minscale__ = 500000
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Integer)
    belagsart = Column('belagsart', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbedeutung = Column('verkehrsbedeutung', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbeschraenkung = Column('verkehrsbeschraenkung', Unicode)
    the_geom = Column(Geometry2D)


class Swisstlm3dStrassen100000(Base, Vector):
    __tablename__ = 'strasse_100000_tooltip'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-strassen.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-strassen'
    __label__ = 'objektart'
    __maxscale__ = 500000
    __minscale__ = 100000
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Integer)
    belagsart = Column('belagsart', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbedeutung = Column('verkehrsbedeutung', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbeschraenkung = Column('verkehrsbeschraenkung', Unicode)
    the_geom = Column(Geometry2D)


class Swisstlm3dStrassen10000(Base, Vector):
    __tablename__ = 'strasse_10000_tooltip'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-strassen.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-strassen'
    __label__ = 'objektart'
    __maxscale__ = 100000
    __minscale__ = 10000
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Integer)
    belagsart = Column('belagsart', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbedeutung = Column('verkehrsbedeutung', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbeschraenkung = Column('verkehrsbeschraenkung', Unicode)
    the_geom = Column(Geometry2D)


class Swisstlm3dStrassen(Base, Vector):
    __tablename__ = 'strasse'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swisstlm3d-strassen.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-strassen'
    __label__ = 'objektart'
    __maxscale__ = 10000
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Integer)
    belagsart = Column('belagsart', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbedeutung = Column('verkehrsbedeutung', Unicode)
    eigentuemer = Column('eigentuemer', Unicode)
    verkehrsbeschraenkung = Column('verkehrsbeschraenkung', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisstlm3d-strassen', Swisstlm3dStrassen500000)
register('ch.swisstopo.swisstlm3d-strassen', Swisstlm3dStrassen100000)
register('ch.swisstopo.swisstlm3d-strassen', Swisstlm3dStrassen10000)
register('ch.swisstopo.swisstlm3d-strassen', Swisstlm3dStrassen)


class Swisstlm3dWanderwege(Base, Vector):
    __tablename__ = 'wanderwege_swissmap'
    __table_args__ = ({'schema': 'karto', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissmap_online_wanderwege.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-wanderwege'
    __label__ = 'id'
    id = Column('nr', Integer, primary_key=True)
    hikingtype = Column('hikingtype', Unicode)
    bridgetype = Column('bridgetype', Unicode)
    tunneltype = Column('tunneltype', Unicode)
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
    name = Column('name', Unicode)
    type = Column('type', Unicode)
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
    name = Column('name', Unicode)
    type = Column('type', Unicode)
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
    hikingtype = Column('hikingtype', Unicode)
    bridgetype = Column('bridgetype', Unicode)
    tunneltype = Column('tunneltype', Unicode)
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
    zusziff = Column('zusziff', Unicode)
    langtext = Column('langtext', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.ortschaftenverzeichnis_plz', PLZOrtschaften)


class GeometaStandAV(Base, Vector):
    __tablename__ = 'amogr_standav'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/standav.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-standav'
    __label__ = 'frame'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    quality = Column('quality', Unicode)
    frame = Column('frame', Unicode)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-standav', GeometaStandAV)


class GeometaPNF(Base, Vector):
    __tablename__ = 'amopnf_pnf'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/metadata_pnf.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-periodische_nachfuehrung'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    canton = Column('canton', Unicode)
    description = Column('description', Unicode)
    year = Column('year', Integer)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-periodische_nachfuehrung', GeometaPNF)


class GeometaLos(Base, Vector):
    __tablename__ = 'amogr_los'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/los.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-los'
    __label__ = 'operatsname'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    neu_id = Column('neu_id', Unicode)
    operatsname = Column('operatsname', Unicode)
    losnr = Column('losnr', Unicode)
    taetigkeit_d = Column('taetigkeit_d', Unicode)
    taetigkeit_f = Column('taetigkeit_f', Unicode)
    taetigkeit_i = Column('taetigkeit_i', Unicode)
    quality = Column('quality', Unicode)
    flaeche_vertrag = Column('flaeche_vertrag', Unicode)
    frame = Column('frame', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-los', GeometaLos)

# link sur le pdf ne fontionne pas...


class GeometaGemeinde(Base, Vector):
    __tablename__ = 'amogr_gemeinde'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/gemeinde.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-gemeinde'
    __label__ = 'gemeindename'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    gemeindename = Column('gemeindename', Unicode)
    kanton = Column('kanton', Unicode)
    flaeche_ha = Column('flaeche_ha', Unicode)
    bfs_nr = Column('bfs_nr', Integer)
    pdf_liste = Column('pdf_liste', Unicode)
    abgabestelle = Column('abgabestelle', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-gemeinde', GeometaGemeinde)


class GeometaGrundbuch(Base, Vector):
    __tablename__ = 'amogr_grundbuch'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/grundbuch.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-grundbuch'
    __label__ = 'ortsteil_grundbuch'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    ortsteil_grundbuch = Column('ortsteil_grundbuch', Unicode)
    grundbuchfuehrung_d = Column('grundbuchfuehrung_d', Unicode)
    grundbuchfuehrung_f = Column('grundbuchfuehrung_f', Unicode)
    grundbuchfuehrung_i = Column('grundbuchfuehrung_i', Unicode)
    grundbuchkreis = Column('grundbuchkreis', Unicode)
    adresse = Column('adresse', Unicode)
    telefon = Column('telefon', Unicode)
    email = Column('email', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-grundbuch', GeometaGrundbuch)


class GeometaNfGeom(Base, Vector):
    __tablename__ = 'amogr_nfgeom'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/nfgeom.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-nfgeom'
    __label__ = 'name'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    name = Column('name', Unicode)
    firmenname = Column('firmenname', Unicode)
    adresse = Column('adresse', Unicode)
    telefon = Column('telefon', Unicode)
    email = Column('email', Unicode)
    stellvertreter = Column('ist_stellvertreter', Boolean)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom_gen50 = Column('the_geom_gen50', Geometry2D)
    the_geom = Column('the_geom', Geometry2D)

register('ch.swisstopo-vd.geometa-nfgeom', GeometaNfGeom)


class Oerebkataster(Base, Vector):
    __tablename__ = 'view_oereb_nfgeom'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/oerebkataster.mako'
    __bodId__ = 'ch.swisstopo-vd.stand-oerebkataster'
    __label__ = 'gemeindename'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    gemeindename = Column('gemeindename', Unicode)
    kanton = Column('kanton', Unicode)
    oereb_status_de = Column('oereb_status_de', Unicode)
    oereb_status_fr = Column('oereb_status_fr', Unicode)
    oereb_status_it = Column('oereb_status_it', Unicode)
    oereb_status_rm = Column('oereb_status_rm', Unicode)
    oereb_status_en = Column('oereb_status_en', Unicode)
    bfs_nr = Column('bfs_nr', Integer)
    firmenname = Column('firmenname', Unicode)
    adresszeile = Column('adresszeile', Unicode)
    plz = Column('plz', Integer)
    ort = Column('ort', Unicode)
    telefon = Column('telefon', Unicode)
    email = Column('email', Unicode)
    url_oereb = Column('url_oereb', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.stand-oerebkataster', Oerebkataster)


class TransformationBezugsrahmenHoehePunkte(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_pkt'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'name'
    __queryable_attributes__ = ['name']
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    y = Column('y', Numeric)
    x = Column('x', Numeric)
    or_ln02_cm = Column('or_ln02_cm', Numeric)
    the_geom = Column(Geometry2D)


class TransformationBezugsrahmenHoeheLine5cm(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_line_5cm'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'contour'
    __maxscale__ = 500000
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    layer = Column('layer', Unicode)
    the_geom = Column(Geometry2D)


class TransformationBezugsrahmenHoeheLine10cm(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_line_10cm'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'contour'
    __minscale__ = 500000
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    layer = Column('layer', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.transformation-bezugsrahmen_hoehe', TransformationBezugsrahmenHoehePunkte)
register('ch.swisstopo.transformation-bezugsrahmen_hoehe', TransformationBezugsrahmenHoeheLine5cm)
register('ch.swisstopo.transformation-bezugsrahmen_hoehe', TransformationBezugsrahmenHoeheLine10cm)


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
    ord_nr = Column('ord_nr', Unicode)
    ort = Column('ort', Unicode)
    v = Column('v', Numeric)
    mfv = Column('mfv', Numeric)
    klasse = Column('klasse', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.hebungsraten', HebungsratenLine)
register('ch.swisstopo.hebungsraten', HebungsratenPunkt)


class SpannungsarmeGebiete(Base, Vector):
    __tablename__ = 'spannungsarme_gebiete'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/spannungsarme_gebiete.mako'
    __bodId__ = 'ch.swisstopo.transformationsgenauigkeit'
    __label__ = 'sg_name'
    id = Column('identifier', Unicode, primary_key=True)
    sg_name = Column('sg_name', Unicode)
    vali_date = Column('vali_date', DateTimeChsdi)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.transformationsgenauigkeit', SpannungsarmeGebiete)


class SpannungsarmeGebieteVD(SpannungsarmeGebiete):
    __bodId__ = 'ch.swisstopo-vd.spannungsarme-gebiete'

register('ch.swisstopo-vd.spannungsarme-gebiete', SpannungsarmeGebieteVD)


class GeologieGeotopePunkte(Base, Vector):
    __tablename__ = 'geotope_pkt'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotope.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotope'
    __label__ = 'nom'
    id = Column('objectid', Integer, primary_key=True)
    nom = Column('nom', Unicode)
    fix_id = Column('fix_id', Unicode)
    nummer = Column('nummer', Integer)
    the_geom = Column(Geometry2D)


class GeologieGeotopeFlaechen(Base, Vector):
    __tablename__ = 'geotope_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotope.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotope'
    __label__ = 'nom'
    id = Column('objectid', Integer, primary_key=True)
    nom = Column('nom', Unicode)
    fix_id = Column('fix_id', Unicode)
    nummer = Column('nummer', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotope', GeologieGeotopePunkte)
register('ch.swisstopo.geologie-geotope', GeologieGeotopeFlaechen)


class SteineHistBauwerke(Base, Vector):
    __tablename__ = 'geotechnik_steine_historische_bauwerke'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geol_steine_hist_bauwerke.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke'
    __extended_info__ = True
    __label__ = 'objekt'
    id = Column('bgdi_id', Integer, primary_key=True)
    objekt = Column('objekt', Unicode)
    obtyp = Column('obtyp', Unicode)
    ort = Column('ort', Unicode)
    objektteil = Column('objektteil', Unicode)
    age = Column('age', Unicode)
    gestart = Column('gestart', Unicode)
    referenz = Column('referenz', Unicode)
    hyperlink = Column('hyperlink', Unicode)
    abbauort = Column('abbauort', Unicode)
    bemerkung = Column('bemerkung', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke', SteineHistBauwerke)


class GisGeolBase:
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __queryable_attributes__ = ['sgd_nr', 'orig_id', 'title', 'author', 'aux_info', 'doccreation']
    __label__ = 'title'
    __timeInstant__ = 'year'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Unicode)
    orig_id = Column('original_document_id', Unicode)
    author = Column('author', Unicode)
    report_structure = Column('report_structure', Unicode)
    aux_info = Column('auxiliary_information', Unicode)
    doccreation = Column('doccreation_date', DateTimeChsdi)
    copy_avail = Column('copy_avail', Unicode)
    view_avail = Column('view_avail', Unicode)
    pdf_url = Column('pdf_url', Unicode)
    pdf_size = Column('pdf_size', Unicode)
    bgdi_data_status = Column('bgdi_data_status', Unicode)
    year = Column('year', Integer)
    the_geom = Column(Geometry2D)


class GisgeolPunkte(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_points'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-punkte'

register('ch.swisstopo.geologie-gisgeol-punkte', GisgeolPunkte)


class GisgeolLinien(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_lines'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-linien'

register('ch.swisstopo.geologie-gisgeol-linien', GisgeolLinien)


class GisgeolFlaechen1x1km(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1x1km'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1x1km'

register('ch.swisstopo.geologie-gisgeol-flaechen-1x1km', GisgeolFlaechen1x1km)


class GisgeolFlaechen10x10km(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10x10km'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10x10km'

register('ch.swisstopo.geologie-gisgeol-flaechen-10x10km', GisgeolFlaechen10x10km)


class GisgeolFlaechen10to100km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10to100km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10to100km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-10to100km2', GisgeolFlaechen10to100km2)


class GisgeolFlaechen100to1000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_100to1000km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2', GisgeolFlaechen100to1000km2)


class GisgeolFlaechen1000to21000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1000to21000km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2', GisgeolFlaechen1000to21000km2)


class GisgeolFlaechenGt21000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_gt21000km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2', GisgeolFlaechenGt21000km2)


class GisgeolFlaechenLt10km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_lt10km2'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-lt10km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2', GisgeolFlaechenLt10km2)


class Geocover:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    the_geom = Column(Geometry2D)


class GeocoverFeatures(Geocover):
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Unicode)
    description = Column('description', Unicode)
    __maxscale__ = 70000
    __queryable_attributes__ = []


class GeocoverLineAux(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_line_aux'
    __template__ = 'templates/htmlpopup/geocover_line_aux.mako'
    spec_description = Column('spec_description', Unicode)


class GeocoverPointHydro(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_hydro'
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)


class GeocoverPointGeol(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_geol'
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)


class GeocoverPointDrill(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_drill'
    __template__ = 'templates/htmlpopup/geocover_point_drill.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth_1 = Column('depth_1', Unicode)
    description_1 = Column('description_1', Unicode)
    depth_2 = Column('depth_2', Unicode)
    description_2 = Column('description_2', Unicode)


class GeocoverPointInfo(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_info'
    __template__ = 'templates/htmlpopup/geocover_point_info.mako'


class GeocoverPointStruct(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_point_struct'
    __template__ = 'templates/htmlpopup/geocover_point_struct.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    dip = Column('dip', Unicode)


class GeocoverPolygonAux1(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_polygon_aux_1'
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    tecto = Column('tecto', Unicode)
    litstrat_link = Column('litstrat_link', Unicode)
    litho_fr = Column('litho_fr', Unicode)
    litho_de = Column('litho_de', Unicode)
    chrono_fr = Column('chrono_fr', Unicode)
    chrono_de = Column('chrono_de', Unicode)
    harmos_rev_fr = Column('harmos_rev_fr', Unicode)
    harmos_rev_de = Column('harmos_rev_de', Unicode)


class GeocoverPolygonAux2(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_polygon_aux_2'
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    tecto = Column('tecto', Unicode)
    litstrat_link = Column('litstrat_link', Unicode)
    litho_fr = Column('litho_fr', Unicode)
    litho_de = Column('litho_de', Unicode)
    chrono_fr = Column('chrono_fr', Unicode)
    chrono_de = Column('chrono_de', Unicode)
    harmos_rev_fr = Column('harmos_rev_fr', Unicode)
    harmos_rev_de = Column('harmos_rev_de', Unicode)


class GeocoverPolygonMain(Base, GeocoverFeatures, Vector):
    __tablename__ = 'view_geocover_polygon_main'
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    tecto = Column('tecto', Unicode)
    litstrat_link = Column('litstrat_link', Unicode)
    litho_fr = Column('litho_fr', Unicode)
    litho_de = Column('litho_de', Unicode)
    chrono_fr = Column('chrono_fr', Unicode)
    chrono_de = Column('chrono_de', Unicode)
    harmos_rev_fr = Column('harmos_rev_fr', Unicode)
    harmos_rev_de = Column('harmos_rev_de', Unicode)


class GeocoverGridShop (Base, Geocover, ShopProductGroupClass, Vector):
    __tablename__ = 'view_geocover_grid_shop'
    __minscale__ = 70000
    base = Column('base', Unicode)
    version = Column('version', Unicode)

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
    version = Column('version', Unicode)
    base = Column('base', Unicode)

register('ch.swisstopo.geologie-geocover.metadata', GeolGeocoverMetadata)


class Ga25Atlas:
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    the_geom = Column(Geometry2D)


class Ga25AtlasGrid(Base, Ga25Atlas, ShopProductGroupClass, Vector):
    __tablename__ = 'view_ga25_grid'
    id = Column('bgdi_id', Integer, primary_key=True)
    __minscale__ = 70000


class Ga25Features(Ga25Atlas):
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Unicode)
    description = Column('description', Unicode)
    __maxscale__ = 70000
    __queryable_attributes__ = []


class Ga25LineAux(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_line_aux'
    __template__ = 'templates/htmlpopup/ga25_line_aux.mako'
    spec_description = Column('spec_description', Unicode)
    url_legend = Column('url_legende', Unicode)


class Ga25PointHydro(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_hydro'
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)
    url_legend = Column('url_legende', Unicode)


class Ga25PointGeol(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_geol'
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)
    url_legend = Column('url_legende', Unicode)


class Ga25PointDrill(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_drill'
    __template__ = 'templates/htmlpopup/ga25_point_drill.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth_1 = Column('depth_1', Unicode)
    description_1 = Column('description_1', Unicode)
    depth_2 = Column('depth_2', Unicode)
    description_2 = Column('description_2', Unicode)
    url_legend = Column('url_legende', Unicode)


class Ga25PointInfo(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_info'
    __template__ = 'templates/htmlpopup/ga25_point_info.mako'
    url_legend = Column('url_legende', Unicode)


class Ga25PointStruct(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_point_struct'
    __template__ = 'templates/htmlpopup/ga25_point_struct.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    dip = Column('dip', Unicode)
    url_legend = Column('url_legende', Unicode)


class Ga25PolygonAux1(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_polygon_aux_1'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Unicode)
    url_legend = Column('url_legende', Unicode)


class Ga25PolygonAux2(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_polygon_aux_2'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Unicode)
    url_legend = Column('url_legende', Unicode)


class Ga25PolygonMain(Base, Ga25Features, Vector):
    __tablename__ = 'view_ga25_polygon_main'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Unicode)
    url_legend = Column('url_legende', Unicode)

register('ch.swisstopo.geologie-geologischer_atlas', Ga25LineAux)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointHydro)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointGeol)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointDrill)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointInfo)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PointStruct)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PolygonAux1)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PolygonAux2)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25PolygonMain)
register('ch.swisstopo.geologie-geologischer_atlas', Ga25AtlasGrid)


class Swissnames3d:
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __label__ = 'name'
    __template__ = 'templates/htmlpopup/swissnames3d.mako'
    __bodId__ = 'ch.swisstopo.swissnames3d'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Unicode)
    objektklasse = Column('objektklasse', Unicode)
    name = Column('name', Unicode)
    sprachcode = Column('sprachcode', Unicode)
    namen_typ = Column('namen_typ', Unicode)
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


class SpotMosaicPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'view_gridstand_spot5_metadata'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.images-spot-5.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.images-spot-5.metadata', SpotMosaicPerimeter)


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


class SwissMapVector10MetadataPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_vector10'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.swiss-map-vector10.metadata'
    the_geom = Column(Geometry2D)

register(SwissMapVector10MetadataPerimeter.__bodId__, SwissMapVector10MetadataPerimeter)


class SwissMapRaster10MetadataPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_raster10'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.swiss-map-raster10.metadata'
    the_geom = Column(Geometry2D)

register(SwissMapRaster10MetadataPerimeter.__bodId__, SwissMapRaster10MetadataPerimeter)


class Dhm25MetadataPerimeter(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_dhm25'
    __table_args__ = ({'schema': 'public', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.digitales-hoehenmodell_25.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.digitales-hoehenmodell_25.metadata', Dhm25MetadataPerimeter)


class SwissBuildings3d2Meta(Base, ShopStandardClass, Vector):
    __tablename__ = 'shop_perimeter_build3d2'
    __table_args__ = ({'autoload': False})
    __bodId__ = 'ch.swisstopo.swissbuildings3d_2.metadata'
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissbuildings3d_2.metadata', SwissBuildings3d2Meta)


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


class Treasurehunt(Base, Vector):
    __tablename__ = 'treasurehunt'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/treasurehunt.mako'
    __bodId__ = 'ch.swisstopo.treasurehunt'
    id = Column('bgdi_id', Integer, primary_key=True)
    title_de = Column('title_de', Unicode)
    title_fr = Column('title_fr', Unicode)
    title_it = Column('title_it', Unicode)
    info_de = Column('info_de', Unicode)
    info_fr = Column('info_fr', Unicode)
    info_it = Column('info_it', Unicode)
    link_de = Column('link_de', Unicode)
    link_fr = Column('link_fr', Unicode)
    link_it = Column('link_it', Unicode)
    type_coord = Column('type_coord', Unicode)
    the_geom = Column(Geometry2D)
    __maxscale__ = 1500

register('ch.swisstopo.treasurehunt', Treasurehunt)
