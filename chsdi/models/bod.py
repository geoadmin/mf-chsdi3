# -*- coding: utf-8 -*-


import cachetools.func

from gatilegrid import getTileGrid
from sqlalchemy import Column, Unicode, Integer, Boolean, DateTime, Float
from sqlalchemy.dialects import postgresql
from sqlalchemy.exc import SQLAlchemyError

from chsdi.lib.helpers import make_agnostic, shift_to
from chsdi.models import bases, models_from_bodid, get_models_attributes_keys

import logging

log = logging.getLogger(__name__)

# Interval (sec) between two request to translation table
DYNAMIC_TRANSLATION_TTL = 3600

Base = bases['bod']


class Bod(object):
    __dbname__ = 'bod'
    layerBodId = Column('bod_layer_id', Unicode, primary_key=True)
    idGeoCat = Column('geocat_uuid', Unicode)
    name = Column('kurzbezeichnung', Unicode)
    fullName = Column('bezeichnung', Unicode)
    maps = Column('topics', Unicode)  # The topics
    chargeable = Column('chargeable', Boolean)
    dataOwner = Column('datenherr', Unicode)
    abstract = Column('abstract', Unicode)
    dataStatus = Column('datenstand', Unicode)
    downloadUrl = Column('url_download', Unicode)
    urlApplication = Column('url_portale', Unicode)
    fullTextSearch = Column('volltextsuche', Unicode)
    wmsContactAbbreviation = Column('wms_kontakt_abkuerzung', Unicode)
    wmsContactName = Column('wms_kontakt_name', Unicode)
    wmsUrlResource = Column('wms_resource', Unicode)
    staging = Column('staging', Unicode)
    urlDetails = Column('url', Unicode)
    inspireUpperAbstract = Column('inspire_oberthema_abstract', Unicode)
    inspireUpperName = Column('inspire_oberthema_name', Unicode)
    inspireAbstract = Column('inspire_abstract', Unicode)
    inspireName = Column('inspire_name', Unicode)
    bundCollectionNumber = Column('fk_geobasisdaten_sammlung_bundesrecht', Unicode)
    bundCollection = Column('geobasisdatensatz_name', Unicode)
    scaleLimit = Column('scale_limit', Unicode)

    def layerMetadata(self):
        primaryAttrs = ('layerBodId', 'idGeoCat', 'name', 'fullName')
        excludedAttrs = ('staging', 'searchUnicode', 'chargeable')
        meta = {'attributes': {}}
        for k in self.__dict__.keys():
            if k != '_sa_instance_state':
                if k in primaryAttrs and self.__dict__[k] is not None:
                    meta[k] = self.__dict__[k]
                elif k not in excludedAttrs and self.__dict__[k] is not None:
                    meta['attributes'][k] = self.__dict__[k]
        return meta


class LayersConfig(Base):

    __tablename__ = 'view_layers_js'
    __table_args__ = ({'schema': 're3', 'autoload': False})
    layerBodId = Column('layer_id', Unicode, primary_key=True)
    attribution = Column('attribution', Unicode)
    background = Column('backgroundlayer', Boolean)
    hasLegend = Column('haslegend', Boolean)
    format = Column('image_format', Unicode)
    gutter = Column('wms_gutter', Integer)
    type = Column('layertype', Unicode)
    highlightable = Column('highlightable', Boolean)
    opacity = Column('opacity', postgresql.DOUBLE_PRECISION)
    minResolution = Column('minresolution', postgresql.DOUBLE_PRECISION)
    maxResolution = Column('maxresolution', postgresql.DOUBLE_PRECISION)
    parentLayerId = Column('parentlayerid', Unicode)
    searchable = Column('searchable', Boolean)
    tooltip = Column('tooltip', Boolean)
    serverLayerName = Column('server_layername', Unicode)
    singleTile = Column('singletile', Boolean)
    subLayersIds = Column('sublayersids', postgresql.ARRAY(Unicode))
    tilematrix_resolution_max = Column('tilematrix_resolution_max', postgresql.DOUBLE_PRECISION)
    timeEnabled = Column('timeenabled', Boolean)
    timestamps = Column('timestamps', postgresql.ARRAY(Unicode))
    timeBehaviour = Column('time_behaviour', Unicode)
    maps = Column('topics', Unicode)
    chargeable = Column('chargeable', Boolean)
    staging = Column('staging', Unicode)
    wmsLayers = Column('wms_layers', Unicode)
    updateDelay = Column('geojson_update_delay', Integer)
    geojsonUrlde = Column('geojson_url_de', Unicode)
    geojsonUrlfr = Column('geojson_url_fr', Unicode)
    geojsonUrlit = Column('geojson_url_it', Unicode)
    geojsonUrlrm = Column('geojson_url_rm', Unicode)
    geojsonUrlen = Column('geojson_url_en', Unicode)
    config3d = Column('fk_config3d', Boolean)
    srid = Column('srid', Unicode)
    extent = Column('extent', postgresql.ARRAY(Float))

    def layerConfig(self, params):
        config = {}
        translate = params.translate
        settings = params.request.registry.settings
        wmsHost = settings['wmshost']
        defaultResolution = 0.5
        for k in self.__dict__.keys():
            val = self.__dict__[k]
            if not k.startswith("_") and not k.startswith('geojsonUrl') and \
                    val is not None and k not in ('staging', 'srid'):
                if k == 'maps':
                    config['topics'] = val
                elif k == 'layerBodId':
                    config['label'] = translate(val)
                elif k == 'attribution':
                    config[k] = translate(val)
                elif k == 'tilematrix_resolution_max':
                    if val != defaultResolution and \
                            self.__dict__['srid'] != u'4326':
                        config['resolutions'] = self._getResolutionsFromMatrixSet(
                            val, params.srid)
                elif k == 'extent':  # Used for the shop, are still in lv03
                    if val and params.srid == 2056:
                        config['extent'] = shift_to(val, 2056)
                    else:
                        config['extent'] = val
                else:
                    config[k] = val

        if config['type'] in ('wmts', 'aggregate', 'geojson'):
            del config['singleTile']

        if not config['timeEnabled']:
            del config['timeBehaviour']

        if config['type'] == 'wms':
            # do not use https if wmsUrl starts with localhost
            protocol = "http" if wmsHost.lower().startswith('localhost') else "https"
            config['wmsUrl'] = f'{protocol}://{wmsHost}'
        elif config['type'] == 'geojson':
            api_url = params.request.registry.settings['api_url']
            config['styleUrl'] = make_agnostic(
                api_url + '/static/vectorStyles/' + self.layerBodId + '.json')
            config['geojsonUrl'] = self._getGeoJsonUrl(params.lang)
            if 'format' in config:
                del config['format']
        # sublayers don't have attributions
        if 'attribution' in config:
            config['attributionUrl'] = translate(self.__dict__['attribution'] + '.url')

        # adding __queryable_attributes__ if they have them
        models = models_from_bodid(self.layerBodId)
        if models is not None:
            queryable_attributes = get_models_attributes_keys(models, params.lang, True)
            if len(queryable_attributes) > 0:
                config['queryableAttributes'] = queryable_attributes

        return {self.layerBodId: config}

    # All fields point to en for now
    def _getGeoJsonUrl(self, lang):
        return self.__dict__['geojsonUrl%s' % lang]

    def _getResolutionsFromMatrixSet(self, Resolution, srid):
        gagrid = getTileGrid(srid)()
        zoomlevel = gagrid.getClosestZoom(Resolution)
        return gagrid.RESOLUTIONS[0:zoomlevel + 1]


class BodLayerDe(Base, Bod):
    __tablename__ = 'view_bod_layer_info_de'
    __table_args__ = ({'schema': 're3'})


class BodLayerFr(Base, Bod):
    __tablename__ = 'view_bod_layer_info_fr'
    __table_args__ = ({'schema': 're3'})


class BodLayerIt(Base, Bod):
    __tablename__ = 'view_bod_layer_info_it'
    __table_args__ = ({'schema': 're3'})


class BodLayerRm(Base, Bod):
    __tablename__ = 'view_bod_layer_info_rm'
    __table_args__ = ({'schema': 're3'})


class BodLayerEn(Base, Bod):
    __tablename__ = 'view_bod_layer_info_en'
    __table_args__ = ({'schema': 're3'})


class ServiceMetadata(object):
    id = Column('wms_id', Unicode, primary_key=True)
    pk_map_name = Column('pk_map_name', Unicode)
    title = Column('title', Unicode)
    onlineresource = Column('onlineresource', Unicode)
    abstract = Column('abstract', Unicode)
    keywords = Column('keywords', Unicode)
    fee = Column('fee', Unicode)
    accessconstraint = Column('accessconstraint', Unicode)
    encoding = Column('encoding', Unicode)
    fk_contact_id = Column('fk_contact_id', Integer)
    addresstype = Column('addresstype', Unicode)
    address = Column('address', Unicode)
    postcode = Column('postcode', Integer)
    city = Column('city', Unicode)
    country = Column('country', Unicode)
    contactelectronicmailaddress = Column('contactelectronicmailaddress', Unicode)
    contactperson = Column('contactperson', Unicode)
    contactvoicetelephon = Column('contactvoicetelephon', Unicode)
    stateorprovince = Column('stateorprovince', Unicode)
    fk_contactorganisation_id = Column('fk_contactorganisation_id', Integer)
    abkuerzung = Column('abkuerzung', Unicode)
    name = Column('name', Unicode)


class ServiceMetadataDe(Base, ServiceMetadata):
    __tablename__ = 'view_wms_service_metadata_de'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class ServiceMetadataFr(Base, ServiceMetadata):
    __tablename__ = 'view_wms_service_metadata_fr'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class ServiceMetadataIt(Base, ServiceMetadata):
    __tablename__ = 'view_wms_service_metadata_it'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class ServiceMetadataRm(Base, ServiceMetadata):
    __tablename__ = 'view_wms_service_metadata_rm'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class ServiceMetadataEn(Base, ServiceMetadata):
    __tablename__ = 'view_wms_service_metadata_en'
    __table_args__ = ({'schema': 're3', 'autoload': False})


def computeHeader(mapName, srid):
    gagrid = getTileGrid(srid)()
    minZoom = 0
    maxZoom = len(gagrid.RESOLUTIONS)
    dpi = 90.7
    lods = []
    for zoom in range(minZoom, maxZoom):
        lods.append(
            {'level': zoom,
             'resolution': gagrid.getResolution(zoom),
             'scale': gagrid.getScale(zoom),
             'width': gagrid.numberOfXTilesAtZoom(zoom),
             'height': gagrid.numberOfYTilesAtZoom(zoom)}
        )

    return {
        'mapName': mapName,
        'description': 'Configuration for the map (topic) ' + mapName,
        'copyrightUnicode': 'Data ' + mapName,
        'layers': [],
        'spatialReference': {"wkid": gagrid.spatialReference},
        'tileInfo': {
            'rows': int(gagrid.tileSizePx),  # tile width in pixel
            'cols': int(gagrid.tileSizePx),
            'dpi': dpi,
            'format': 'PNG,JPEG',
            'compressionQuality': None,
            'origin': {'x': gagrid.origin[0],
                       'y': gagrid.origin[1]},
            'spatialReference': {'wkid': gagrid.spatialReference},
            'lods': lods
        },
        'initialExtent': {
            'xmin': gagrid.extent[0] + 38000.0, 'ymin': gagrid.extent[1] + 46375.0,
            'xmax': gagrid.extent[2] - 60875.0, 'ymax': gagrid.extent[3] - 37500.0,
            'spatialReference': {'wkid': gagrid.spatialReference}
        },
        'fullExtent': {
            'xmin': gagrid.extent[0], 'ymin': gagrid.extent[1],
            'xmax': gagrid.extent[2], 'ymax': gagrid.extent[3],
            'spatialReference': {'wkid': gagrid.spatialReference}
        },
        'units': 'esriMeters',
        'capabilities': 'Map'
    }


class Topics(Base):
    __tablename__ = 'topics'
    __table_args__ = ({'schema': 're3', 'autoload': False})
    id = Column('topic', Unicode, primary_key=True)
    selectedLayers = Column('selected_layers', postgresql.ARRAY(Unicode))
    defaultBackground = Column('default_background', Unicode)
    activatedLayers = Column('activated_layers', postgresql.ARRAY(Unicode))
    backgroundLayers = Column('background_layers', postgresql.ARRAY(Unicode))
    showCatalog = Column('show_catalog', Boolean)
    staging = Column('staging', Unicode)
    plconf = Column('permalink_configuration', Unicode)
    groupId = Column('group_id', Integer)


class Catalog(Base):
    __dbname__ = 'bod'
    __tablename__ = 'view_catalog'
    __table_args__ = ({'schema': 're3', 'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    parentId = Column('parent_id', Integer)
    topic = Column('topic', Unicode)
    category = Column('category', Unicode)
    layerBodId = Column('bod_layer_id', Unicode)
    nameDe = Column('name_de', Unicode)
    nameFr = Column('name_fr', Unicode)
    nameIt = Column('name_it', Unicode)
    nameRm = Column('name_rm', Unicode)
    nameEn = Column('name_en', Unicode)
    orderKey = Column('order_key', Integer)
    selectedOpen = Column('selected_open', Boolean)
    staging = Column('staging', Unicode)

    def to_dict(self, lang):

        self.label = self._get_label_from_lang(lang)

        return dict([
            (k, getattr(self, k)) for
            k in self.__dict__.keys()
            if not k.startswith("_")
            and self.__dict__[k] is not None
            and k not in ('nameDe', 'nameFr', 'nameIt', 'nameRm', 'nameEn')
        ])

    def _get_label_from_lang(self, lang):
        return {
            'de': self.nameDe,
            'fr': self.nameFr,
            'it': self.nameIt,
            'rm': self.nameRm,
            'en': self.nameEn
        }[lang]

    @classmethod
    def get_name_from_lang(cls, lang):
        return {
            'de': cls.nameDe,
            'fr': cls.nameFr,
            'it': cls.nameIt,
            'rm': cls.nameRm,
            'en': cls.nameEn
        }[lang]


class OerebMetadata(Base):
    __tablename__ = 'oereb_interlis_metadata'
    __table_args__ = ({'schema': 're3', 'autoload': False})
    layerBodId = Column('layer_id', Unicode, primary_key=True)
    header = Column('header', Unicode)
    footer = Column('footer', Unicode)
    data_created = Column('data_created', Unicode)
    data_imported = Column('data_imported', Unicode)


def get_bod_model(lang):
    if lang == 'fr':
        return BodLayerFr
    elif lang == 'it':
        return BodLayerIt
    elif lang == 'rm':
        return BodLayerRm
    elif lang == 'en':
        return BodLayerEn
    else:
        return BodLayerDe


class CacheUpdate(Base):
    __dbname__ = 'bod'
    __tablename__ = 'dataset_cache'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    id = Column('layer_id', Unicode, primary_key=True)
    cache_type = Column('cache_type', Unicode)
    cache_modified = Column('cache_modified', DateTime)


class Translations(Base):
    __dbname__ = 'bod'
    __tablename__ = 'translations'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    msgId = Column('msg_id', Unicode, primary_key=True)
    id = Column('bgdi_id', Integer)
    de = Column('de', Unicode)
    fr = Column('fr', Unicode)
    it = Column('it', Unicode)
    rm = Column('rm', Unicode)
    en = Column('en', Unicode)


@cachetools.func.ttl_cache(ttl = DYNAMIC_TRANSLATION_TTL)
def get_translations(lang, session):
    # Returns the the translation dictionnary from BOD for all supported langs.
    log.debug('Get translations from DB for "{}"'.format(lang))

    d = {}
    try:
        query = session.query(Translations)
        results = query.all()
        for row in results:
            d[row.msgId] = getattr(row, lang)
    except SQLAlchemyError as e:
        log.error("Cannot get translations from BOD: {}".format(e))
        return None

    return d
