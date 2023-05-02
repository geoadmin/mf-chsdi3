# -*- coding: utf-8 -*-

from sqlalchemy import Column

from sqlalchemy.types import Numeric, Boolean, Integer, Float, Unicode, BigInteger, SmallInteger

from chsdi.models import register, bases
from chsdi.models.types import DateTimeChsdi
from chsdi.models.vector import Vector, Geometry2D


Base = bases['stopo']


class GeologieGeologische3dmodelle(Base, Vector):
    __tablename__ = 'geologische_3dmodelle'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologische3dmodelle.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologische_3dmodelle'
    __returnedGeometry__ = 'the_geom_simplified'
    __extended_info__ = True
    __label_ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    purpose = Column('purpose', Unicode)
    content = Column('content', Unicode)
    remarks = Column('remarks', Unicode)
    year_publication = Column('year_publication', Unicode)
    de_contracting_entity = Column('de_contracting_entity', Unicode)
    fr_contracting_entity = Column('fr_contracting_entity', Unicode)
    it_contracting_entity = Column('it_contracting_entity', Unicode)
    en_contracting_entity = Column('en_contracting_entity', Unicode)
    rm_contracting_entity = Column('rm_contracting_entity', Unicode)
    de_author = Column('de_author', Unicode)
    fr_author = Column('fr_author', Unicode)
    it_author = Column('it_author', Unicode)
    en_author = Column('en_author', Unicode)
    rm_author = Column('rm_author', Unicode)
    de_link_portal = Column('de_link_portal', Unicode)
    fr_link_portal = Column('fr_link_portal', Unicode)
    it_link_portal = Column('it_link_portal', Unicode)
    en_link_portal = Column('en_link_portal', Unicode)
    rm_link_portal = Column('rm_link_portal', Unicode)
    de_link_description = Column('de_link_description', Unicode)
    fr_link_description = Column('fr_link_description', Unicode)
    it_link_description = Column('it_link_description', Unicode)
    en_link_description = Column('en_link_description', Unicode)
    rm_link_description = Column('rm_link_description', Unicode)
    de_link_documentation = Column('de_link_documentation', Unicode)
    fr_link_documentation = Column('fr_link_documentation', Unicode)
    it_link_documentation = Column('it_link_documentation', Unicode)
    en_link_documentation = Column('en_link_documentation', Unicode)
    rm_link_documentation = Column('rm_link_documentation', Unicode)
    the_geom_simplified = Column('the_geom_simplified', Geometry2D)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geologische_3dmodelle', GeologieGeologische3dmodelle)


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


class GeomolIsotherme:
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    id = Column('bgdi_id', Integer, primary_key=True)
    objectid = Column('objectid', Integer)
    name = Column('name', Unicode)
    elev = Column('elev', Integer)
    the_geom = Column(Geometry2D)


class GeomolIsotherme60(Base, GeomolIsotherme, Vector):
    __tablename__ = 'geomol_isotherme_60_elev'
    __template__ = 'templates/htmlpopup/geomol_isotherme60.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomol-isotherme_60'

register('ch.swisstopo.geologie-geomol-isotherme_60', GeomolIsotherme60)


class GeomolIsotherme100(Base, GeomolIsotherme, Vector):
    __tablename__ = 'geomol_isotherme_100_elev'
    __template__ = 'templates/htmlpopup/geomol_isotherme100.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomol-isotherme_100'

register('ch.swisstopo.geologie-geomol-isotherme_100', GeomolIsotherme100)


class GeomolIsotherme150(Base, GeomolIsotherme, Vector):
    __tablename__ = 'geomol_isotherme_150_elev'
    __template__ = 'templates/htmlpopup/geomol_isotherme150.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomol-isotherme_150'

register('ch.swisstopo.geologie-geomol-isotherme_150', GeomolIsotherme150)


class GeomolTempEingangdaten(Base, Vector):
    __tablename__ = 'geomol_temperaturmodell_eingangsdaten_pt'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geomol_temperaturmodell.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperaturmodell_eingangsdaten'
    __label__ = 'label'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    label = Column('label', Unicode)
    typ = Column('type', Unicode)
    country = Column('country', Unicode)
    canton = Column('canton', Unicode)
    x = Column('x', Integer)
    y = Column('y', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geomol-temperaturmodell_eingangsdaten', GeomolTempEingangdaten)


class GeomolTempTopRaster:
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/geomol_temperatur_top.mako'
    id = Column('bgdi_id', Integer, primary_key=True)
    pixel_value = Column('pixel_value', Float)
    the_geom = Column(Geometry2D)


class GeomolTempTopElev:
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    id = Column('bgdi_id', Integer, primary_key=True)
    elev = Column('elev', Integer)
    the_geom = Column(Geometry2D)


class GeomolTempTopOmmRaster(Base, GeomolTempTopRaster, Vector):
    __tablename__ = 'geomol_temperatur_omm_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperatur_top_omm'

register('ch.swisstopo.geologie-geomol-temperatur_top_omm', GeomolTempTopOmmRaster)


class GeomolTempTopOmmElev(Base, GeomolTempTopElev, Vector):
    __tablename__ = 'geomol_temperatur_omm_elev'
    __template__ = 'templates/htmlpopup/geomol_temperatur_omm_elev.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperatur_top_omm'

register('ch.swisstopo.geologie-geomol-temperatur_top_omm', GeomolTempTopOmmElev)


class GeomolTempTopOmalmRaster(Base, GeomolTempTopRaster, Vector):
    __tablename__ = 'geomol_temperatur_omalm_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperatur_top_omalm'

register('ch.swisstopo.geologie-geomol-temperatur_top_omalm', GeomolTempTopOmalmRaster)


class GeomolTempTopOmalmElev(Base, GeomolTempTopElev, Vector):
    __tablename__ = 'geomol_temperatur_omalm_elev'
    __template__ = 'templates/htmlpopup/geomol_temperatur_omalm_elev.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperatur_top_omalm'

register('ch.swisstopo.geologie-geomol-temperatur_top_omalm', GeomolTempTopOmalmElev)


class GeomolTempTopMuschelkalkRaster(Base, GeomolTempTopRaster, Vector):
    __tablename__ = 'geomol_temperatur_muschelkalk_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk'

register('ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk', GeomolTempTopMuschelkalkRaster)


class GeomolTempTopMuschelkalkElev(Base, GeomolTempTopElev, Vector):
    __tablename__ = 'geomol_temperatur_muschelkalk_elev'
    __template__ = 'templates/htmlpopup/geomol_temperatur_muschelkalk_elev.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk'

register('ch.swisstopo.geologie-geomol-temperatur_top_muschelkalk', GeomolTempTopMuschelkalkElev)


class GeomolTempverteilung:
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/geomol_temperaturverteilung.mako'
    id = Column('bgdi_id', Integer, primary_key=True)
    pixel_value = Column('pixel_value', Float)
    the_geom = Column(Geometry2D)


class GeomolTempverteilung500(Base, GeomolTempverteilung, Vector):
    __tablename__ = 'geomol_temperaturverteilung_500_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperaturverteilung_500'

register('ch.swisstopo.geologie-geomol-temperaturverteilung_500', GeomolTempverteilung500)


class GeomolTempverteilung1000(Base, GeomolTempverteilung, Vector):
    __tablename__ = 'geomol_temperaturverteilung_1000_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperaturverteilung_1000'

register('ch.swisstopo.geologie-geomol-temperaturverteilung_1000', GeomolTempverteilung1000)


class GeomolTempverteilung1500(Base, GeomolTempverteilung, Vector):
    __tablename__ = 'geomol_temperaturverteilung_1500_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperaturverteilung_1500'

register('ch.swisstopo.geologie-geomol-temperaturverteilung_1500', GeomolTempverteilung1500)


class GeomolTempverteilung2000(Base, GeomolTempverteilung, Vector):
    __tablename__ = 'geomol_temperaturverteilung_2000_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperaturverteilung_2000'

register('ch.swisstopo.geologie-geomol-temperaturverteilung_2000', GeomolTempverteilung2000)


class GeomolTempverteilung3000(Base, GeomolTempverteilung, Vector):
    __tablename__ = 'geomol_temperaturverteilung_3000_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperaturverteilung_3000'

register('ch.swisstopo.geologie-geomol-temperaturverteilung_3000', GeomolTempverteilung3000)


class GeomolTempverteilung4000(Base, GeomolTempverteilung, Vector):
    __tablename__ = 'geomol_temperaturverteilung_4000_raster'
    __bodId__ = 'ch.swisstopo.geologie-geomol-temperaturverteilung_4000'

register('ch.swisstopo.geologie-geomol-temperaturverteilung_4000', GeomolTempverteilung4000)


class DosisleistungTerrestrisch(Base, Vector):
    __tablename__ = 'dosisleistung_terrestrisch'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/dosisleistung_terrestrisch.mako'
    __bodId__ = 'ch.swisstopo.geologie-dosisleistung-terrestrisch'
    __label__ = 'contour'
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-dosisleistung-terrestrisch', DosisleistungTerrestrisch)


class Landesschwerenetz:
    __table_args__ = ({'schema': 'fida', 'autoload': False})
    __template__ = 'templates/htmlpopup/landesschwerenetz.mako'
    __bodId__ = 'ch.swisstopo.landesschwerenetz'
    __label__ = 'label_tt'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr_lsn2004 = Column('nr_lsn2004', Unicode)
    name = Column('name', Unicode)
    label_tt = Column('label', Unicode)
    type = Column('type', Unicode)
    lat_etrs = Column('lat_etrs', Numeric)
    lon_etrs = Column('lon_etrs', Numeric)
    y_lv95 = Column('y_lv95', Numeric)
    x_lv95 = Column('x_lv95', Numeric)
    h_ln02 = Column('h_ln02', Numeric)
    gravity = Column('gravity', Numeric)
    rms = Column('rms', Numeric)
    vert_grad = Column('vertgrad', Numeric)
    link_hfp_title = Column('linkhfptit', Unicode)
    link_hfp_url = Column('link_hfp', Unicode)
    link_lfp_title = Column('linklfptit', Unicode)
    link_lfp_url = Column('link_lfp', Unicode)
    the_geom = Column(Geometry2D)


class LandesschwerenetzZoom1(Base, Landesschwerenetz, Vector):
    __tablename__ = 'landesschwerenetz'
    __minscale__ = 1
    __maxscale__ = 3000


class LandesschwerenetzZoom2(Base, Landesschwerenetz, Vector):
    __tablename__ = 'landesschwerenetz_overview'
    __minscale__ = 3000


register(Landesschwerenetz.__bodId__, LandesschwerenetzZoom1)
register(Landesschwerenetz.__bodId__, LandesschwerenetzZoom2)


class GravimetrischerAtlasMesspunkte(Base, Vector):
    __tablename__ = 'gravimetrisch_messpunkte'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gravimetrischer_atlas_messpunkte.mako'
    __bodId__ = 'ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte'
    __label__ = 'stationnam'
    id = Column('bgdi_id', Integer, primary_key=True)
    stationnam = Column('stationnam', Unicode)
    coordhor = Column('coordhor', Numeric)
    coordver = Column('coordver', Numeric)
    altitude = Column('altitude', Numeric)
    bouguerano = Column('bouguerano', Numeric)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte', GravimetrischerAtlasMesspunkte)


class GeologieGeoevents:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie_geoevents.mako'
    __bodId__ = 'ch.swisstopo.geologie-geowege'
    id = Column('post_id', Integer, primary_key=True)
    post_title = Column('post_title', Unicode)
    allgemein_leadtext = Column('allgemein_leadtext', Unicode)
    treffpunkt_gemeinde = Column('treffpunkt_gemeinde', Unicode)
    treffpunkt_kanton = Column('treffpunkt_kanton', Unicode)
    kontakt_firma = Column('kontakt_firma', Unicode)
    post_permalink = Column('post_permalink', Unicode)
    the_geom = Column(Geometry2D)


class GeologieGeoeventsDemnaechst(Base, Vector, GeologieGeoevents):
    __tablename__ = 'v_erlebnis_naechste'
    __bodId__ = 'ch.swisstopo.geologie-geoevents_demnaechst'

register(GeologieGeoeventsDemnaechst.__bodId__, GeologieGeoeventsDemnaechst)


class GeologieGeoeventsAnfrage(Base, Vector, GeologieGeoevents):
    __tablename__ = 'v_erlebnis_anfrage'
    __bodId__ = 'ch.swisstopo.geologie-geoevents_anfrage'

register(GeologieGeoeventsAnfrage.__bodId__, GeologieGeoeventsAnfrage)


class GeologieGeoeventsSites(Base, Vector, GeologieGeoevents):
    __tablename__ = 'v_erlebnis_sites'
    __bodId__ = 'ch.swisstopo.geologie-geosites'

register(GeologieGeoeventsSites.__bodId__, GeologieGeoeventsSites)


class GeologieGeowege(Base, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie_geowege.mako'
    __bodId__ = 'ch.swisstopo.geologie-geowege'
    id = Column('post_id', Integer, primary_key=True)
    post_title = Column('agg_post_title', Unicode)
    allgemein_leadtext = Column('agg_allgemein_leadtext', Unicode)
    treffpunkt_gemeinde = Column('agg_treffpunkt_gemeinde', Unicode)
    treffpunkt_kanton = Column('agg_treffpunkt_kanton', Unicode)
    kontakt_firma = Column('agg_kontakt_firma', Unicode)
    post_permalink = Column('agg_post_permalink', Unicode)
    the_geom = Column(Geometry2D)
    __tablename__ = 'v_erlebnis_geowege_tracks'
    __bodId__ = 'ch.swisstopo.geologie-geowege'

register(GeologieGeowege.__bodId__, GeologieGeowege)


class GeolGeneralkarteGGK200Meta(Base, Vector):
    __tablename__ = 'generalkarte_ggk200_meta'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/generalkarte_ggk200.metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-generalkarte-ggk200.metadata'
    __label__ = 'titel'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr = Column('nr', Integer)
    titel = Column('titel', Unicode)
    jahr = Column('jahr', Integer)
    autor = Column('autor', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-generalkarte-ggk200.metadata', GeolGeneralkarteGGK200Meta)


class GeologischerAtlasMeta:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologischer_atlas_meta.mako'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    nummer = Column('nummer', Integer)
    name = Column('name', Unicode)
    massstab = Column('massstab', Unicode)
    ausgabejahr = Column('ausgabejahr', Integer)
    autoren = Column('autoren', Unicode)
    the_geom = Column(Geometry2D)


class GeologischerAtlasRasterMeta(Base, GeologischerAtlasMeta, Vector):
    __tablename__ = 'geologischer_atlas_raster_meta'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas.metadata'

register('ch.swisstopo.geologie-geologischer_atlas.metadata', GeologischerAtlasRasterMeta)


class GeologischerAtlasVectorMeta(Base, GeologischerAtlasMeta, Vector):
    __tablename__ = 'geologischer_atlas_vector_meta'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas_vector.metadata'

register('ch.swisstopo.geologie-geologischer_atlas_vector.metadata', GeologischerAtlasVectorMeta)


class GeolSpezialkartenMetadata:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/spezialkarten_meta.mako'
    __label__ = 'titel'
    id = Column('bgdi_id', Integer, primary_key=True)
    gsk_nr = Column('gsk_nr', Unicode)
    titel = Column('titel', Unicode)
    massstab = Column('massstab', Unicode)
    jahrgang = Column('jahrgang', Integer)
    autoren = Column('autoren', Unicode)
    the_geom = Column(Geometry2D)


class GeolSpezialkartenRasterMetadata(Base, GeolSpezialkartenMetadata, Vector):
    __tablename__ = 'spezialkarten_raster_meta'
    __bodId__ = 'ch.swisstopo.geologie-spezialkarten_schweiz.metadata'

register('ch.swisstopo.geologie-spezialkarten_schweiz.metadata', GeolSpezialkartenRasterMetadata)


class GeolSpezialKartenVectorMeta(Base, GeolSpezialkartenMetadata, Vector):
    __tablename__ = 'spezialkarten_vector_meta'
    __bodId__ = 'ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata'

register('ch.swisstopo.geologie-spezialkarten_schweiz_vector.metadata', GeolSpezialKartenVectorMeta)


class SwissboundariesBezirk(Base, Vector):
    __tablename__ = 'swissboundaries_bezirke'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_bezirk.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill'
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
    __label__ = 'gemname'
    id = Column('id', Integer, primary_key=True)
    gemname = Column('gemname', Unicode)
    gemflaeche = Column('gemflaeche', Float)
    perimeter = Column('perimeter', Float)
    kanton = Column('kanton', Unicode)
    objektart = Column('objektart', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', SwissboundariesGemeinde)


class SwissboundariesKanton(Base, Vector):
    __tablename__ = 'swissboundaries_kantone'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_kanton.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-kanton-flaeche.fill'
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
    __template__ = 'templates/htmlpopup/swissboundaries_country.mako'
    __label__ = 'displayname'
    id = Column('icc', Unicode, primary_key=True)
    flaeche = Column('flaeche', Numeric)
    displayname = Column('displayname', Unicode)
    bez = Column('bez', Unicode)
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
    __template__ = 'templates/htmlpopup/gridstand.mako'
    id = Column('gid', BigInteger, primary_key=True)
    tileid = Column('tileid', Unicode)
    lk_name = Column('lk_name', Unicode)
    datenstand = Column('release', Integer)
    releasekey = Column('releasekey', Unicode)
    the_geom = Column(Geometry2D)


class GridstandPermiterTemplate:
    __table_args__ = ({'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


# PK 25


class GridstandPk25Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk25.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk25_tilecache'


register('ch.swisstopo.pixelkarte-pk25.metadata', GridstandPk25Meta)

# PK 50


class GridstandPk50Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk50.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk50_tilecache'


register('ch.swisstopo.pixelkarte-pk50.metadata', GridstandPk50Meta)

# PK 100


class GridstandPk100Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk100.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk100_tilecache'

register('ch.swisstopo.pixelkarte-pk100.metadata', GridstandPk100Meta)

# PK 200


class GridstandPk200Meta(Base, GridstandTemplate, Vector):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk200.metadata'
    __tablename__ = 'view_gridstand_datenhaltung_pk200_tilecache'
    id = Column('kbnum', Unicode, primary_key=True)

register('ch.swisstopo.pixelkarte-pk200.metadata', GridstandPk200Meta)


class GridstandSwissimageDop10(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_swissimage_dop10_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.images-swissimage-dop10.metadata'
    __template__ = 'templates/htmlpopup/swissimage_dop10.mako'
    __label__ = 'id'
    id = Column('tile_id', Unicode, primary_key=True)
    datenstand = Column('flightyear', Unicode)
    resolution = Column('resolution', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.images-swissimage-dop10.metadata', GridstandSwissimageDop10)


class GridstandSwisssurface3d(Base, Vector):
    __tablename__ = 'view_gridstand_swisssurface3d'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.swisssurface3d.metadata'
    __template__ = 'templates/htmlpopup/swisssurface3d.mako'
    __label__ = 'id'
    id = Column('tilekey', Unicode, primary_key=True)
    temporalkey = Column('temporalkey', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swisssurface3d.metadata', GridstandSwisssurface3d)


class GridstandSwisssurface3dRaster(Base, Vector):
    __tablename__ = 'view_gridstand_swisssurface3d_raster_metadata'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.swisssurface3d-raster.metadata'
    __template__ = 'templates/htmlpopup/swisssurface3d_raster.mako'
    __label__ = 'id'
    id = Column('tilekey', Unicode, primary_key=True)
    fly_y_min = Column('fly_y_min', Integer)
    fly_y_max = Column('fly_y_max', Integer)
    the_geom = Column(Geometry2D)

register(GridstandSwisssurface3dRaster.__bodId__, GridstandSwisssurface3dRaster)


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


class GeologieFelsoberflaecheHoehenModell(Base, Vector):
    __tablename__ = 'felsoberflaeche_hoehenmodell'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie_felsoberflaeche_hoehenmodell.mako'
    __bodId__ = 'ch.swisstopo.geologie-felsoberflaeche_hoehenmodell'
    __label__ = 'height'
    id = Column('bgdi_id', Integer, primary_key=True)
    height = Column('height', Numeric)
    the_geom = Column(Geometry2D)

register(GeologieFelsoberflaecheHoehenModell.__bodId__, GeologieFelsoberflaecheHoehenModell)


class GeologieLockergesteinMaechtigkeitsModell(Base, Vector):
    __tablename__ = 'lockergestein_maechtigkeitsmodell'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie_lockergestein_maechtigkeitsmodell.mako'
    __bodId__ = 'ch.swisstopo.geologie-lockergestein_maechtigkeitsmodell'
    __label__ = 'height'
    id = Column('bgdi_id', Integer, primary_key=True)
    height = Column('height', Numeric)
    the_geom = Column(Geometry2D)

register(GeologieLockergesteinMaechtigkeitsModell.__bodId__, GeologieLockergesteinMaechtigkeitsModell)


class GeologieBohrungenTiefer500(Base, Vector):
    __tablename__ = 'bohrungen_tiefer_500'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/bohrungen_tiefer_500.mako'
    __bodId__ = 'ch.swisstopo.geologie-bohrungen_tiefer_500'
    __label__ = 'name'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    td_m_md = Column('td_m_md', Unicode)
    td_m_tvd = Column('td_m_tvd', Unicode)
    fm_at_td = Column('fm_at_td', Unicode)
    purpose_de = Column('purpose_d', Unicode)
    purpose_fr = Column('purpose_f', Unicode)
    purpose_en = Column('purpose_e', Unicode)
    discover_de = Column('discover_d', Unicode)
    discover_fr = Column('discover_f', Unicode)
    discover_en = Column('discover_e', Unicode)
    status_de = Column('status_d', Unicode)
    status_fr = Column('status_f', Unicode)
    status_en = Column('status_e', Unicode)
    spud = Column('spud', Unicode)
    end = Column('end_', Unicode)
    temp = Column('temp', Unicode)
    swissgeol = Column('swissgeol', Unicode)
    easting = Column('easting', Unicode)
    northing = Column('northing', Unicode)
    zgl = Column('zgl', Unicode)
    ref_type_de = Column('ref_type_d', Unicode)
    ref_type_fr = Column('ref_type_f', Unicode)
    ref_type_en = Column('ref_type_e', Unicode)
    zref = Column('zref', Unicode)
    client = Column('client', Unicode)
    owner = Column('owner', Unicode)
    download = Column('download', Unicode)
    content = Column('content', Unicode)
    web_link = Column('web_link', Unicode)
    info_de = Column('info_d', Unicode)
    info_fr = Column('info_f', Unicode)
    info_en = Column('info_e', Unicode)
    canton = Column('canton', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-bohrungen_tiefer_500', GeologieBohrungenTiefer500)


class GeologieGeothermischePotenzialstudien(Base, Vector):
    __tablename__ = 'geothermische_potenzialstudien'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geothermische_potenzialstudien.mako'
    __bodId__ = 'ch.swisstopo.geologie-geothermische_potenzialstudien_regional'
    __label__ = 'kanton'
    __extended_info__ = True
    id = Column('bgdi_id', Integer, primary_key=True)
    land = Column('land', Unicode)
    kanton = Column('kanton', Unicode)
    nb_studien = Column('nb_studien', Integer)
    titel_de = Column('titel_de', Unicode)
    titel_fr = Column('titel_fr', Unicode)
    titel_en = Column('titel_en', Unicode)
    titel_it = Column('titel_it', Unicode)
    titel_rm = Column('titel_rm', Unicode)
    autor = Column('autor', Unicode)
    jahr = Column('jahr', Unicode)
    auftraggeber = Column('auftraggeber', Unicode)
    weblink_de = Column('weblink_de', Unicode)
    weblink_fr = Column('weblink_fr', Unicode)
    weblink_en = Column('weblink_en', Unicode)
    weblink_it = Column('weblink_it', Unicode)
    download = Column('download', Unicode)
    legend = Column('legend', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geothermische_potenzialstudien_regional', GeologieGeothermischePotenzialstudien)


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


class TiefenGeothermieProjekte:
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    owner = Column('owner', Unicode)
    status_de = Column('status_de', Unicode)
    status_fr = Column('status_fr', Unicode)
    status_it = Column('status_it', Unicode)
    status_en = Column('status_en', Unicode)
    system_de = Column('system_de', Unicode)
    system_fr = Column('system_fr', Unicode)
    system_it = Column('system_it', Unicode)
    system_en = Column('system_en', Unicode)
    purpose_de = Column('purpose_de', Unicode)
    purpose_fr = Column('purpose_fr', Unicode)
    purpose_it = Column('purpose_it', Unicode)
    purpose_en = Column('purpose_en', Unicode)
    canton = Column('canton', Unicode)
    municipality_de = Column('municipality_de', Unicode)
    municipality_fr = Column('municipality_fr', Unicode)
    municipality_it = Column('municipality_it', Unicode)
    municipality_en = Column('municipality_en', Unicode)
    res_tvd = Column('res_tvd', Integer)
    reservoir = Column('reservoir', Unicode)
    temperature = Column('temperature', Unicode)
    year = Column('year', Unicode)
    subsidy_de = Column('subsidy_de', Unicode)
    subsidy_fr = Column('subsidy_fr', Unicode)
    subsidy_it = Column('subsidy_it', Unicode)
    subsidy_en = Column('subsidy_en', Unicode)
    download = Column('download', Unicode)
    more_de = Column('more_de', Unicode)
    more_fr = Column('more_fr', Unicode)
    more_it = Column('more_it', Unicode)
    more_en = Column('more_en', Unicode)
    the_geom = Column(Geometry2D)


class TiefenGeothermieProjektePoint(Base, TiefenGeothermieProjekte, Vector):
    __tablename__ = 'tiefengeothermie_projekte_pkt'
    __template__ = 'templates/htmlpopup/tiefengeothermie_projekte_pkt.mako'
    __bodId__ = 'ch.swisstopo.geologie-tiefengeothermie_projekte'
    __label__ = 'name'
    __extended_info__ = True

register('ch.swisstopo.geologie-tiefengeothermie_projekte', TiefenGeothermieProjektePoint)


class TiefenGeothermieProjektePoly(Base, TiefenGeothermieProjekte, Vector):
    __tablename__ = 'tiefengeothermie_projekte_plg'
    __template__ = 'templates/htmlpopup/tiefengeothermie_projekte_plg.mako'
    __bodId__ = 'ch.swisstopo.geologie-tiefengeothermie_projekte'
    __label__ = 'name'
    __extended_info__ = True
    permis_de = Column('permis_de', Unicode)
    permis_fr = Column('permis_fr', Unicode)
    permis_it = Column('permis_it', Unicode)
    permis_en = Column('permis_en', Unicode)
    date = Column('date', Unicode)

register('ch.swisstopo.geologie-tiefengeothermie_projekte', TiefenGeothermieProjektePoly)


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
    __label__ = 'ziegelei_2'
    id = Column('id', Integer, primary_key=True)
    ziegelei_2 = Column('ziegelei_2', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotechnik-ziegeleien_1907', GeologieGeotechnikZiegeleien1907)


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
    __tablename__ = 'rohstoffe_industriemin'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_industrieminerale.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-industrieminerale'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    obnamealt = Column('obnamealt', Unicode)
    imkinds = Column('imkinds', Unicode)
    edrskinds = Column('edrskinds', Unicode)
    emkinds = Column('emkinds', Unicode)
    stkind = Column('stkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-industrieminerale', GeologieRohstoffeIndustrieminerale)


class GeologieRohstoffeKohlenBitumenErdgas(Base, Vector):
    __tablename__ = 'rohstoffe_kohlenbitumenerdgas'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_kohlen_bitumen_erdgas.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    obnamealt = Column('obnamealt', Unicode)
    erkinds = Column('erkinds', Unicode)
    ederkinds = Column('ederkinds', Unicode)
    emkinds = Column('emkinds', Unicode)
    stkind = Column('stkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas', GeologieRohstoffeKohlenBitumenErdgas)


class GeologieRohstoffeVererzungen(Base, Vector):
    __tablename__ = 'rohstoffe_vererz'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_vererzungen.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-vererzungen'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    obnamealt = Column('obnamealt', Unicode)
    grkinds = Column('grkinds', Unicode)
    edmikinds = Column('edmikinds', Unicode)
    emkinds = Column('emkinds', Unicode)
    stkind = Column('stkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-vererzungen', GeologieRohstoffeVererzungen)


class GeologieRohstoffeNaturwerksteineAbbau(Base, Vector):
    __tablename__ = 'rohstoffe_naturwerksteineabbau'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_naturwerksteine_abbau.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    tckind = Column('tckind', Unicode)
    ltkinds = Column('ltkinds', Unicode)
    emkinds = Column('emkinds', Unicode)
    stkind = Column('stkind', Unicode)
    clkind = Column('clkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-naturwerksteine_abbau', GeologieRohstoffeNaturwerksteineAbbau)


class GeologieRohstoffeGebrocheneGesteine(Base, Vector):
    __tablename__ = 'rohstoffe_gebrochenegesteineabbau'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_gebrochene_gesteine.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    tckind = Column('tckind', Unicode)
    ltkinds = Column('ltkinds', Unicode)
    emkinds = Column('emkinds', Unicode)
    stkind = Column('stkind', Unicode)
    clkind = Column('clkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-gebrochene_gesteine_abbau', GeologieRohstoffeGebrocheneGesteine)


class GeologieRohstoffeSalzAbbauVerarbeitung(Base, Vector):
    __tablename__ = 'rohstoffe_salzabbauverarbeitung'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_salz_abbau_verarbeitung.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    obnamealt = Column('obnamealt', Unicode)
    ockind = Column('ockind', Unicode)
    ltkind = Column('ltkind', Unicode)
    emkinds = Column('emkinds', Unicode)
    pckind = Column('pckind', Unicode)
    cpkind = Column('cpkind', Unicode)
    stkind = Column('stkind', Unicode)
    clkind = Column('clkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-salz_abbau_verarbeitung', GeologieRohstoffeSalzAbbauVerarbeitung)


class GeologieRohstoffeGipsAbbauVerarbeitung(Base, Vector):
    __tablename__ = 'rohstoffe_gipsabbauverarbeitung'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_gips_abbau_verarbeitung.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    ockind = Column('ockind', Unicode)
    ltkinds = Column('ltkinds', Unicode)
    edltkinds = Column('edltkinds', Unicode)
    emkinds = Column('emkinds', Unicode)
    pckind = Column('pckind', Unicode)
    cpkind = Column('cpkind', Unicode)
    stkind = Column('stkind', Unicode)
    clkind = Column('clkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-gips_abbau_verarbeitung', GeologieRohstoffeGipsAbbauVerarbeitung)


class GeologieRohstoffeZementAbbauVerarbeitung(Base, Vector):
    __tablename__ = 'rohstoffe_zementabbauverarbeitung'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_zement_abbau_verarbeitung.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung'
    __label__ = 'obname'
    id = Column('obid', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    tckinds = Column('tckinds', Unicode)
    ltkinds = Column('ltkinds', Unicode)
    emkinds = Column('emkinds', Unicode)
    pckind = Column('pckind', Unicode)
    cpkind = Column('cpkind', Unicode)
    stkind = Column('stkind', Unicode)
    tlyearsformatted = Column('tlyearsformatted', Unicode)
    clkind = Column('clkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-rohstoffe-zement_abbau_verarbeitung', GeologieRohstoffeZementAbbauVerarbeitung)


class GeologieRohstoffeZiegelAbbau(Base, Vector):
    __tablename__ = 'rohstoffe_ziegel_abbau'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-ziegel_abbau'
    __template__ = 'templates/htmlpopup/rohstoffe_ziegel_abbau.mako'
    __label__ = 'obname'
    id = Column('bgdi_id', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    tckinds = Column('tckinds', Unicode)
    ltkinds = Column('ltkinds', Unicode)
    stkind = Column('stkind', Unicode)
    tlyearsformatted = Column('tlyearsformatted', Unicode)
    purl = Column('purl', Unicode)
    clkind = Column('clkind', Unicode)
    the_geom = Column(Geometry2D)

register(GeologieRohstoffeZiegelAbbau.__bodId__, GeologieRohstoffeZiegelAbbau)


class GeologieRohstoffeZiegelVerarbeitung(Base, Vector):
    __tablename__ = 'rohstoffe_ziegel_verarbeitung'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-ziegel_verarbeitung'
    __template__ = 'templates/htmlpopup/rohstoffe_ziegel_verarbeitung.mako'
    __label__ = 'obname'
    id = Column('bgdi_id', Integer, primary_key=True)
    obname = Column('obname', Unicode)
    pckind = Column('pckind', Unicode)
    cpkind = Column('cpkind', Unicode)
    stkind = Column('stkind', Unicode)
    tlyearsformatted = Column('tlyearsformatted', Unicode)
    clkind = Column('clkind', Unicode)
    purl = Column('purl', Unicode)
    the_geom = Column(Geometry2D)

register(GeologieRohstoffeZiegelVerarbeitung.__bodId__, GeologieRohstoffeZiegelVerarbeitung)


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


class GeologieGesteinsdichte(Base, Vector):
    __tablename__ = 'gesteinsdichte'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geol_gesteinsdichte.mako'
    __bodId__ = 'ch.swisstopo.geologie-gesteinsdichte'
    __label__ = 'saphyr_n'
    id = Column('bgdi_id', Integer, primary_key=True)
    saphyr_n = Column('saphyr_n', Unicode)
    rhob_m = Column('rhob_m', Integer)
    rhob_med = Column('rhob_med', Integer)
    rhob_sd = Column('rhob_sd', Integer)
    rhob_anz = Column('rhob_anz', Integer)
    rhob_p05 = Column('rhob_p05', Integer)
    rhob_p25 = Column('rhob_p25', Integer)
    rhob_p75 = Column('rhob_p75', Integer)
    rhob_p95 = Column('rhob_p95', Integer)
    saphyr_pdf = Column('saphyr_pdf', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-gesteinsdichte', GeologieGesteinsdichte)


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
    strassenname = Column('strassenname', Unicode)
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
    strassenname = Column('strassenname', Unicode)
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
    strassenname = Column('strassenname', Unicode)
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
    strassenname = Column('strassenname', Unicode)
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
    __label__ = 'plz'
    id = Column('os_uuid', Unicode, primary_key=True)
    plz = Column('plz', Integer)
    zusziff = Column('zusziff', Unicode)
    langtext = Column('langtext', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.ortschaftenverzeichnis_plz', PLZOrtschaften)


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


class Oerebkataster:
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


class OerebkatasterZoom1(Base, Oerebkataster, Vector):
    __tablename__ = 'view_stand_oereb_parcel'
    oereb_webservice = Column('oereb_webservice', Unicode)
    bgdi_status = Column('bgdi_status', Integer)
    egris_egrid = Column('egris_egrid', Integer)
    oereb_extract_pdf = Column('oereb_extract_pdf', Unicode)
    oereb_extract_url = Column('oereb_extract_url', Unicode)
    number = Column('number_', Integer)
    realestate_type = Column('realestate_type', Unicode)
    __minscale__ = 1
    __maxscale__ = 50000

register('ch.swisstopo-vd.stand-oerebkataster', OerebkatasterZoom1)


class OerebkatasterZoom2(Base, Oerebkataster, Vector):
    __tablename__ = 'view_oereb_nfgeom'
    __minscale__ = 50000

register('ch.swisstopo-vd.stand-oerebkataster', OerebkatasterZoom2)


class TransformationBezugsrahmenHoehePunkte(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_pkt'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'name'
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
    __label__ = 'contour'
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry2D)


class HebungsratenPunkt(Base, Vector):
    __tablename__ = 'hebungsraten_pkt'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/hebungsraten.mako'
    __bodId__ = 'ch.swisstopo.hebungsraten'
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


class GeologieGeotopeKantoneStand(Base, Vector):
    __tablename__ = 'view_stand_kantonale_geotope'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotope_kantone_stand.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotope_kantone_stand'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    sigel = Column('sigel', Unicode)
    inventar = Column('inventar', Unicode)
    link = Column('link', Unicode)
    kontakt = Column('kontakt', Unicode)
    publikation = Column('publikation', Unicode)
    quelle = Column('quelle', Unicode)
    bemerkung = Column('bemerkung', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geotope_kantone_stand', GeologieGeotopeKantoneStand)


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
    __label__ = 'title'
    __extended_info__ = True
    __timeInstant__ = 'year'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Unicode)
    title = Column('title', Unicode)
    orig_id = Column('original_document_id', Unicode)
    author = Column('author', Unicode)
    report_structure = Column('report_structure', Unicode)
    aux_info = Column('auxiliary_information', Unicode)
    doccreation = Column('doccreation_date', Unicode)
    copy_avail = Column('copy_avail', Unicode)
    view_avail = Column('view_avail', Unicode)
    pdf_url = Column('pdf_url', Unicode)
    pdf_size = Column('pdf_size', Unicode)
    bgdi_data_status = Column('bgdi_data_status', Unicode)
    year = Column('year', Unicode)
    count_pdf = Column('count_pdf', Integer)
    count_without_pdf = Column('count_without_pdf', Integer)
    count_total = Column('count_total', Integer)
    the_geom = Column(Geometry2D)


class GisgeolPunkte(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_points_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-punkte'

register('ch.swisstopo.geologie-gisgeol-punkte', GisgeolPunkte)


class GisgeolLinien(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_lines_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-linien'

register('ch.swisstopo.geologie-gisgeol-linien', GisgeolLinien)


class GisgeolFlaechen1x1km(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1x1km_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1x1km'

register('ch.swisstopo.geologie-gisgeol-flaechen-1x1km', GisgeolFlaechen1x1km)


class GisgeolFlaechen10x10km(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10x10km_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10x10km'

register('ch.swisstopo.geologie-gisgeol-flaechen-10x10km', GisgeolFlaechen10x10km)


class GisgeolFlaechen10to100km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10to100km2_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10to100km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-10to100km2', GisgeolFlaechen10to100km2)


class GisgeolFlaechen100to1000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_100to1000km2_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2', GisgeolFlaechen100to1000km2)


class GisgeolFlaechen1000to21000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1000to21000km2_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2', GisgeolFlaechen1000to21000km2)


class GisgeolFlaechenGt21000km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_gt21000km2_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2', GisgeolFlaechenGt21000km2)


class GisgeolFlaechenLt10km2(Base, GisGeolBase, Vector):
    __tablename__ = 'view_gisgeol_surfaces_lt10km2_aggregated'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-lt10km2'

register('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2', GisgeolFlaechenLt10km2)


class Geocover:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    erl_num = Column('erl_num', Unicode)
    ber_num = Column('ber_num', Unicode)
    the_geom = Column(Geometry2D)


class GeocoverExtended(Geocover):
    spec_description_de = Column('spec_description_de', Unicode)
    spec_description_fr = Column('spec_description_fr', Unicode)


class GeocoverLineAux(Base, GeocoverExtended, Vector):
    __tablename__ = 'geocover_line_aux'
    __template__ = 'templates/htmlpopup/geocover_aux.mako'


class GeocoverPointHydro(Base, GeocoverExtended, Vector):
    __tablename__ = 'geocover_point_hydro'
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)


class GeocoverPointGeol(Base, GeocoverExtended, Vector):
    __tablename__ = 'geocover_point_geol'
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)


class GeocoverPointDrill(Base, GeocoverExtended, Vector):
    __tablename__ = 'geocover_point_drill'
    __template__ = 'templates/htmlpopup/geocover_point_drill.mako'
    azimut = Column('azimut', Unicode)
    depth_1 = Column('depth_1', Unicode)
    description_1_de = Column('description_1_de', Unicode)
    description_1_fr = Column('description_1_fr', Unicode)
    depth_2 = Column('depth_2', Unicode)
    description_2_de = Column('description_2_de', Unicode)
    description_2_fr = Column('description_2_fr', Unicode)
    spec_val = Column('spec_val', Integer)
    rem_de = Column('rem_de', Unicode)
    rem_fr = Column('rem_fr', Unicode)


class GeocoverPointInfo(Base, Geocover, Vector):
    __tablename__ = 'geocover_point_info'
    __template__ = 'templates/htmlpopup/geocover_point_info.mako'


class GeocoverPointStruct(Base, GeocoverExtended, Vector):
    __tablename__ = 'geocover_point_struct'
    __template__ = 'templates/htmlpopup/geocover_point_struct.mako'
    azimut = Column('azimut', Unicode)
    dip = Column('dip', Unicode)


class GeocoverPolygonAux1(Base, GeocoverExtended, Vector):
    __tablename__ = 'geocover_polygon_aux_1'
    __template__ = 'templates/htmlpopup/geocover_aux.mako'


class GeocoverPolygonAux2(Base, GeocoverExtended, Vector):
    __tablename__ = 'geocover_polygon_aux_2'
    __template__ = 'templates/htmlpopup/geocover_aux.mako'


class GeocoverPolygonMain(Base, Geocover, Vector):
    __tablename__ = 'geocover_polygon_main'
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    litstrat_link_de = Column('litstrat_link_de', Unicode)
    litstrat_link_fr = Column('litstrat_link_fr', Unicode)
    litho_fr = Column('litho_fr', Unicode)
    litho_de = Column('litho_de', Unicode)
    tecto_de = Column('tecto_de', Unicode)
    tecto_fr = Column('tecto_fr', Unicode)
    chrono_fr = Column('chrono_fr', Unicode)
    chrono_de = Column('chrono_de', Unicode)
    orig_description_de = Column('orig_description_de', Unicode)
    orig_description_fr = Column('orig_description_fr', Unicode)


register('ch.swisstopo.geologie-geocover', GeocoverLineAux)
register('ch.swisstopo.geologie-geocover', GeocoverPointHydro)
register('ch.swisstopo.geologie-geocover', GeocoverPointGeol)
register('ch.swisstopo.geologie-geocover', GeocoverPointDrill)
register('ch.swisstopo.geologie-geocover', GeocoverPointInfo)
register('ch.swisstopo.geologie-geocover', GeocoverPointStruct)
register('ch.swisstopo.geologie-geocover', GeocoverPolygonAux1)
register('ch.swisstopo.geologie-geocover', GeocoverPolygonAux2)
register('ch.swisstopo.geologie-geocover', GeocoverPolygonMain)


class GeolGeocoverMetadata(Base, Vector):
    __tablename__ = 'geocover_meta'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover.metadata'
    __label__ = 'msh_map_ti'
    id = Column('bgdi_id', Integer, primary_key=True)
    msh_map_nb = Column('msh_map_nb', Integer)
    msh_map_ti = Column('msh_map_ti', Unicode)
    msh_scale = Column('msh_scale', Unicode)
    msh_edit = Column('msh_edit', Integer)
    msh_versio = Column('msh_versio', Unicode)
    msh_basis = Column('msh_basis', Unicode)
    msh_author = Column('msh_author', Unicode)
    msh_rev = Column('msh_rev', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-geocover.metadata', GeolGeocoverMetadata)


class GeologischerAtlas:
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    description = Column('description', Unicode)
    erl_num = Column('erl_num', Unicode)
    leg_num = Column('leg_num', Unicode)
    the_geom = Column(Geometry2D)


class GeologischerAtlasLineAux(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_line_aux'
    __template__ = 'templates/htmlpopup/ga25_line_aux.mako'
    spec_description = Column('spec_description', Unicode)


class GeologischerAtlasPointHydro(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_point_hydro'
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)


class GeologischerAtlasPointGeol(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_point_geol'
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth = Column('depth', Unicode)


class GeologischerAtlasPointDrill(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_point_drill'
    __template__ = 'templates/htmlpopup/ga25_point_drill.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    depth_1 = Column('depth_1', Unicode)
    description_1 = Column('description_1', Unicode)
    depth_2 = Column('depth_2', Unicode)
    description_2 = Column('description_2', Unicode)


class GeologischerAtlasPointInfo(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_point_info'
    __template__ = 'templates/htmlpopup/ga25_point_info.mako'


class GeologischerAtlasPointStruct(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_point_struct'
    __template__ = 'templates/htmlpopup/ga25_point_struct.mako'
    spec_description = Column('spec_description', Unicode)
    azimut = Column('azimut', Unicode)
    dip = Column('dip', Unicode)


class GeologischerAtlasPolygonAux1(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_polygon_aux_1'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Unicode)


class GeologischerAtlasPolygonAux2(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_polygon_aux_2'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Unicode)


class GeologischerAtlasPolygonMain(Base, GeologischerAtlas, Vector):
    __tablename__ = 'geologischer_atlas_polygon_main'
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    tecto = Column('tecto', Unicode)


register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasLineAux)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPointHydro)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPointGeol)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPointDrill)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPointInfo)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPointStruct)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPolygonAux1)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPolygonAux2)
register('ch.swisstopo.geologie-geologischer_atlas', GeologischerAtlasPolygonMain)


class GeologischerAtlasProfil(Base, Vector):
    __tablename__ = 'geologischer_atlas_profil'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologischer_atlas_profil.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas_profile'
    __label__ = 'id'
    __extended_info__ = True
    id = Column('ga25_id', Unicode, primary_key=True)
    ga25_name = Column('ga25_name', Unicode)
    ga25_no = Column('ga25_no', Integer)
    ga25_edition = Column('ga25_edition', Integer)
    plate_no = Column('plate_no', Unicode)
    section_no = Column('section_no', Unicode)
    section_type_de = Column('section_type_de', Unicode)
    section_type_fr = Column('section_type_fr', Unicode)
    section_type_it = Column('section_type_it', Unicode)
    section_type_en = Column('section_type_en', Unicode)
    scale = Column('scale', Unicode)
    vert_exag = Column('vert_exag', Float)
    author = Column('author', Unicode)
    link_original = Column('link_original', Unicode)
    link_onlineshop_de = Column('link_onlineshop_de', Unicode)
    link_onlineshop_fr = Column('link_onlineshop_fr', Unicode)
    link_onlineshop_it = Column('link_onlineshop_it', Unicode)
    link_onlineshop_en = Column('link_onlineshop_en', Unicode)
    swissgeol_link_de = Column('swissgeol_link_de', Unicode)
    swissgeol_link_fr = Column('swissgeol_link_fr', Unicode)
    swissgeol_link_it = Column('swissgeol_link_it', Unicode)
    swissgeol_link_en = Column('swissgeol_link_en', Unicode)
    the_geom = Column(Geometry2D)

register(GeologischerAtlasProfil.__bodId__, GeologischerAtlasProfil)


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
    status = Column('status', Unicode)
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


class HiksDufourMetadata(Base, Vector):
    __tablename__ = 'view_gridstand_dufour'
    __template__ = 'templates/htmlpopup/dufour_meta.mako'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.hiks-dufour.metadata'
    id = Column('kbnum', Unicode, primary_key=True)
    name = Column('kbbez', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.hiks-dufour.metadata', HiksDufourMetadata)


class HiksSiegfriedTa25Metadata(Base, Vector):
    __tablename__ = 'view_gridstand_siegfried_ta25'
    __template__ = 'templates/htmlpopup/dufour_meta.mako'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.hiks-siegfried-ta25.metadata'
    id = Column('kbnum', Unicode, primary_key=True)
    name = Column('kbbez', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.hiks-siegfried-ta25.metadata', HiksSiegfriedTa25Metadata)


class HiksSiegfriedTa50Metadata(Base, Vector):
    __tablename__ = 'view_gridstand_siegfried_ta50'
    __template__ = 'templates/htmlpopup/dufour_meta.mako'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __bodId__ = 'ch.swisstopo.hiks-siegfried-ta50.metadata'
    id = Column('kbnum', Unicode, primary_key=True)
    name = Column('kbbez', Unicode)
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


class SwissimageHistMetadata(Base, Vector):
    __tablename__ = 'swissimage_hist_chsdi'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissimagehist.mako'
    __bodId__ = 'ch.swisstopo.swissimage-product.metadata'
    __timeInstant__ = 'bgdi_flugjahr'
    id = Column('bgdi_id', Integer, primary_key=True)
    kbnum = Column('tilenumber', Unicode)
    flightyear = Column('gdwh_flightyear', Integer)
    gsd = Column('gsd', Unicode)
    colormode = Column('colormode', Unicode)
    bgdi_flugjahr = Column('bgdi_flugjahr', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.swissimage-product.metadata', SwissimageHistMetadata)


class AmtlichesStrassenverzeichnis(Base, Vector):
    __tablename__ = 'streetnames_tooltip'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/strassenverzeichnis.mako'
    __bodId__ = 'ch.swisstopo.amtliches-strassenverzeichnis'
    __label__ = 'stn_label'
    __queryable_attributes__ = ['stn_label', 'zip_label', 'com_name', 'com_fosnr', 'str_type']
    id = Column('id', Integer, primary_key=True)
    str_esid = Column('str_esid', Integer)
    stn_label = Column('stn_label', Unicode)
    zip_label = Column('zip_label', Unicode)
    com_name = Column('com_name', Unicode)
    com_fosnr = Column('com_fosnr', Integer)
    str_official = Column('str_official', Integer)
    str_modified = Column('str_modified', Unicode)
    str_type = Column('str_type', Unicode)
    str_status = Column('str_status', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.amtliches-strassenverzeichnis', AmtlichesStrassenverzeichnis)


class CadastralWebMap(Base, Vector):
    __tablename__ = 'view_os_realestate_cwm'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/cadastralwebmap.mako'
    __bodId__ = 'ch.kantone.cadastralwebmap-farbe'
    __label__ = 'ak'
    id = Column('id', Integer, primary_key=True)
    ak = Column('ak', Unicode)
    number = Column('number', Unicode)
    identnd = Column('identnd', Unicode)
    egris_egrid = Column('egris_egrid', Unicode)
    realestate_type = Column('realestate_type', Integer)
    geoportal_url = Column('geoportal_url', Unicode)
    the_geom = Column(Geometry2D)

register('ch.kantone.cadastralwebmap-farbe', CadastralWebMap)


class CadastralWebMapOpenData(Base, Vector):
    __tablename__ = 'view_os_realestate_vd_opendata'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/cadastralwebmap_opendata.mako'
    __bodId__ = 'ch.swisstopo-vd.amtliche-vermessung'
    __label__ = 'name'
    __extended_info__ = True
    id = Column('id', Integer, primary_key=True)
    bfsnr = Column('bfsnr', Integer)
    ak = Column('ak', Unicode)
    name = Column('name', Unicode)
    number = Column('number', Unicode)
    identnd = Column('identnd', Unicode)
    egris_egrid = Column('egris_egrid', Unicode)
    realestate_type = Column('realestate_type', Integer)
    geoportal_url = Column('geoportal_url', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo-vd.amtliche-vermessung', CadastralWebMapOpenData)


class Vec25GewaessernetzReferenz(Base, Vector):
    __tablename__ = 'v25_gewaessernetz_ref'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/gewaessernetzref.mako'
    __bodId__ = 'ch.swisstopo.vec25-gewaessernetz_referenz'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    gewissnr = Column('gewissnr', Integer)
    gwlnr = Column('gwlnr', Unicode)
    objectval = Column('objectval', Unicode)
    objectval_de = Column('objectval_de', Unicode)
    objectval_fr = Column('objectval_fr', Unicode)
    objectid = Column('objectid', Integer)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.vec25-gewaessernetz_referenz', Vec25GewaessernetzReferenz)


class AktuelleErdbeben(Base, Vector):
    __tablename__ = 'grid_pk1000'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/aktuelle_erdbeben.mako'
    __bodId__ = 'ch.bafu.gefahren-aktuelle_erdbeben'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)

register('ch.bafu.gefahren-aktuelle_erdbeben', AktuelleErdbeben)


class AmtlichesAdressVerzeichnis(Base, Vector):
    __tablename__ = 'addressverzeichnis'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/addressverzeichnis.mako'
    __bodId__ = 'ch.swisstopo.amtliches-gebaeudeadressverzeichnis'
    __label__ = 'adr_egaid'
    __queryable_attributes__ = ['adr_egaid', 'bdg_egid', 'adr_edid', 'str_esid', 'stn_label', 'adr_number']
    id = Column('id', BigInteger, primary_key=True)
    adr_egaid = Column('adr_egaid', BigInteger)
    bdg_egid = Column('bdg_egid', BigInteger)
    adr_edid = Column('adr_edid', Integer)
    str_esid = Column('str_esid', Integer)
    stn_label = Column('stn_label', Unicode)
    adr_number = Column('adr_number', Unicode)
    zip_label = Column('zip_label', Unicode)
    com_fosnr = Column('com_fosnr', SmallInteger)
    com_name = Column('com_name', Unicode)
    adr_status = Column('adr_status', Unicode)
    adr_official = Column('adr_official', Boolean)
    bdg_category = Column('bdg_category', Unicode)
    adr_modified = Column('adr_modified', Unicode)
    the_geom = Column(Geometry2D)

register(AmtlichesAdressVerzeichnis.__bodId__, AmtlichesAdressVerzeichnis)


class GeologieFelslabore(Base, Vector):
    __tablename__ = 'felslabore'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie_felslabore.mako'
    __bodId__ = 'ch.swisstopo.geologie-felslabore'
    __label__ = 'name'
    __extended_info__ = True
    __queryabl_attributes__ = ['name', 'operator']
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    description_de = Column('description_de', Unicode)
    description_fr = Column('description_fr', Unicode)
    description_en = Column('description_en', Unicode)
    operator = Column('operator', Unicode)
    time_frame = Column('time_frame', Unicode)
    website_de = Column('website_de', Unicode)
    website_fr = Column('website_fr', Unicode)
    website_en = Column('website_en', Unicode)
    contact_de = Column('contact_de', Unicode)
    contact_fr = Column('contact_fr', Unicode)
    contact_en = Column('contact_en', Unicode)
    visitor_de = Column('visitor_de', Unicode)
    visitor_fr = Column('visitor_fr', Unicode)
    visitor_en = Column('visitor_en', Unicode)
    partners_de = Column('partners_de', Unicode)
    partners_fr = Column('partners_fr', Unicode)
    partners_en = Column('partners_en', Unicode)
    publ_opr_de = Column('publ_opr_de', Unicode)
    publ_opr_fr = Column('publ_opr_fr', Unicode)
    publ_opr_en = Column('publ_opr_en', Unicode)
    publ_tech_de = Column('publ_tech_de', Unicode)
    publ_tech_fr = Column('publ_tech_fr', Unicode)
    publ_tech_en = Column('publ_tech_en', Unicode)
    research_data = Column('research_data', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-felslabore', GeologieFelslabore)


class Gletscherausdehnung(Base, Vector):
    __tablename__ = 'view_gletscherausdehnung_tooltip'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gletscherausdehnung.mako'
    __bodId__ = 'ch.swisstopo.geologie-gletscherausdehnung'
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Unicode)
    sgi_id = Column('sgi_id', Unicode)
    area_km2 = Column('area_km2', Float)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.geologie-gletscherausdehnung', Gletscherausdehnung)


class Gletschermaechtigkeit:
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __bodId__ = 'ch.swisstopo.geologie-gletschermaechtigkeit'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry2D)


class GletschermaechtigkeitGPRProfiles(Base, Gletschermaechtigkeit, Vector):
    __tablename__ = 'gletschermaechtigkeit_gpr_profiles'
    __template__ = 'templates/htmlpopup/gletschermaechtigkeit_gpr_profiles.mako'
    __label__ = 'gpr_prf_name'
    gpr_prf_name = Column('prf_name', Unicode)
    gpr_max_thik = Column('max_thik', Integer)


class GletschermaechtigkeitIceThikness(Base, Gletschermaechtigkeit, Vector):
    __tablename__ = 'gletschermaechtigkeit_ice_thinkness'
    __template__ = 'templates/htmlpopup/gletschermaechtigkeit_ice_thikness.mako'
    __label__ = 'pk_sgi'
    pk_sgi = Column('pk_sgi', Unicode)
    name = Column('name', Unicode)
    mean_thick = Column('mean_thick', Integer)
    max_thick = Column('max_thick', Integer)
    volume = Column('volume', Float)
    year_mode = Column('year_mode', Integer)

register('ch.swisstopo.geologie-gletschermaechtigkeit', GletschermaechtigkeitGPRProfiles)
register('ch.swisstopo.geologie-gletschermaechtigkeit', GletschermaechtigkeitIceThikness)


class FixpunkteLfp1(Base, Vector):
    __tablename__ = 'punkt_lage_lfp1'
    __table_args__ = ({'schema': 'fida', 'autoload': False})
    __template__ = 'templates/htmlpopup/fida_lfp1.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-lfp1'
    __label__ = 'id'
    id = Column('pointid', Unicode, primary_key=True)
    punktname = Column('punktname', Unicode)
    nbident = Column('nbident', Unicode)
    status = Column('status', Unicode)
    nummer = Column('nummer', Unicode)
    n95 = Column('n95', Numeric)
    e95 = Column('e95', Numeric)
    h02 = Column('h02', Numeric)
    proto_url = Column('proto_url', Unicode)
    zugang = Column('zugang', Unicode)
    ordnung = Column('ordnung', Unicode)
    l_gen_lv95 = Column('l_gen_lv95', Numeric)
    h_gen_lv95 = Column('h_gen_lv95', Numeric)
    l_zuv_lv95 = Column('l_zuv_lv95', Unicode)
    h_zuv_lv95 = Column('h_zuv_lv95', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-lfp1', FixpunkteLfp1)


class FixpunkteHfp1(Base, Vector):
    __tablename__ = 'punkt_hoehe_hfp1'
    __table_args__ = ({'schema': 'fida', 'autoload': False})
    __template__ = 'templates/htmlpopup/fida_hfp1.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-hfp1'
    __label__ = 'id'
    id = Column('pointid', Unicode, primary_key=True)
    punktname = Column('punktname', Unicode)
    e95 = Column('e95', Numeric)
    n95 = Column('n95', Numeric)
    h02 = Column('h02', Numeric)
    proto_url = Column('proto_url', Unicode)
    ordnung = Column('ordnung', Unicode)
    zugang = Column('zugang', Unicode)
    h95_ell = Column('h95_ell', Unicode)
    l_gen_lv95 = Column('l_gen_lv95', Numeric)
    h_gen_lv95 = Column('h_gen_lv95', Numeric)
    l_zuv_lv95 = Column('l_zuv_lv95', Unicode)
    h_zuv_lv95 = Column('h_zuv_lv95', Unicode)
    zust_haupt = Column('zust_haupt', Unicode)
    zustaendig = Column('zustaendig', Unicode)
    bgdi_created = Column('bgdi_created', Unicode)
    the_geom = Column(Geometry2D)

register('ch.swisstopo.fixpunkte-hfp1', FixpunkteHfp1)


class FixpunkteLfp2(Base, Vector):
    __tablename__ = 'fixpunkte_lfp2'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/fixpunkte.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-lfp2'
    __label__ = 'id'
    id = Column('nbident_nummer', Unicode, primary_key=True)
    status = Column('status', Unicode)
    koordinate = Column('koordinate', Unicode)
    hoehe_geom_m = Column('hoehe_geom_m', Unicode)
    url_punktprotokoll = Column('url_punktprotokoll', Unicode)
    punktzeichen = Column('punktzeichen', Unicode)
    kanton = Column('kanton', Unicode)
    zust_name = Column('zust_name', Unicode)
    the_geom = Column(Geometry2D)

register(FixpunkteLfp2.__bodId__, FixpunkteLfp2)


class FixpunkteHfp2(Base, Vector):
    __tablename__ = 'fixpunkte_hfp2'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/fixpunkte.mako'
    __bodId__ = 'ch.swisstopo.fixpunkte-hfp2'
    __label__ = 'id'
    id = Column('nbident_nummer', Unicode, primary_key=True)
    status = Column('status', Unicode)
    koordinate = Column('koordinate', Unicode)
    hoehe_geom_m = Column('hoehe_geom_m', Unicode)
    url_punktprotokoll = Column('url_punktprotokoll', Unicode)
    punktzeichen = Column('punktzeichen', Unicode)
    kanton = Column('kanton', Unicode)
    zust_name = Column('zust_name', Unicode)
    the_geom = Column(Geometry2D)

register(FixpunkteHfp2.__bodId__, FixpunkteHfp2)


class SwisstneBase:
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __bodId__ = 'ch.swisstopo.swisstne-base'
    __label__ = 'uuid'
    id = Column('bgdi_id', Unicode, primary_key=True)
    uuid = Column('uuid', Unicode)
    the_geom = Column(Geometry2D)


class SwisstneBasePoint(Base, SwisstneBase, Vector):
    __tablename__ = 'swisstne_base_point'
    __template__ = 'templates/htmlpopup/swisstne_base_point.mako'


class SwisstneBaseLine(Base, SwisstneBase, Vector):
    __tablename__ = 'swisstne_base_line'
    __template__ = 'templates/htmlpopup/swisstne_base_line.mako'
    from_node_uuid = Column('from_node_uuid', Unicode)
    to_node_uuid = Column('to_node_uuid', Unicode)
    rail = Column('rail', Integer)
    road = Column('road', Integer)
    cableway = Column('cableway', Integer)
    water = Column('water', Integer)


class SwisstneBasePoly(Base, SwisstneBase, Vector):
    __tablename__ = 'swisstne_base_poly'
    __template__ = 'templates/htmlpopup/swisstne_base_poly.mako'
    type_poly = Column('type', Unicode)
    type_de = Column('type_de', Unicode)
    type_fr = Column('type_fr', Unicode)
    type_it = Column('type_it', Unicode)
    type_en = Column('type_en', Unicode)

register(SwisstneBase.__bodId__, SwisstneBasePoint)
register(SwisstneBase.__bodId__, SwisstneBaseLine)
register(SwisstneBase.__bodId__, SwisstneBasePoly)
