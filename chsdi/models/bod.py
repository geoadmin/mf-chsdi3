# -*- coding: utf-8 -*-

from gatilegrid import GeoadminTileGrid
from sqlalchemy import Column, Text, Integer, Boolean, DateTime
from sqlalchemy.dialects import postgresql

from chsdi.lib.helpers import make_agnostic
from chsdi.models import bases, models_from_bodid, get_models_attributes_keys

Base = bases['bod']


class Bod(object):
    __dbname__ = 'bod'
    layerBodId = Column('bod_layer_id', Text, primary_key=True)
    idGeoCat = Column('geocat_uuid', Text)
    name = Column('kurzbezeichnung', Text)
    fullName = Column('bezeichnung', Text)
    maps = Column('topics', Text)  # The topics
    chargeable = Column('chargeable', Boolean)
    dataOwner = Column('datenherr', Text)
    abstract = Column('abstract', Text)
    dataStatus = Column('datenstand', Text)
    downloadUrl = Column('url_download', Text)
    urlApplication = Column('url_portale', Text)
    fullTextSearch = Column('volltextsuche', Text)
    wmsContactAbbreviation = Column('wms_kontakt_abkuerzung', Text)
    wmsContactName = Column('wms_kontakt_name', Text)
    wmsUrlResource = Column('wms_resource', Text)
    staging = Column('staging', Text)
    urlDetails = Column('url', Text)
    inspireUpperAbstract = Column('inspire_oberthema_abstract', Text)
    inspireUpperName = Column('inspire_oberthema_name', Text)
    inspireAbstract = Column('inspire_abstract', Text)
    inspireName = Column('inspire_name', Text)
    bundCollectionNumber = Column('fk_geobasisdaten_sammlung_bundesrecht', Text)
    bundCollection = Column('geobasisdatensatz_name', Text)
    scaleLimit = Column('scale_limit', Text)

    def layerMetadata(self):
        primaryAttrs = ('layerBodId', 'idGeoCat', 'name', 'fullName')
        excludedAttrs = ('staging', 'searchText', 'chargeable')
        meta = {'attributes': {}}
        for k in self.__dict__.keys():
            if k != '_sa_instance_state':
                if k in primaryAttrs and self.__dict__[k] is not None:
                    meta[k] = self.__dict__[k]
                elif k not in excludedAttrs and self.__dict__[k] is not None:
                    meta['attributes'][k] = self.__dict__[k]
        return meta


class LayersConfig(Base):

    defaultMatrixSet21781 = '21781_26'

    __tablename__ = 'view_layers_js'
    __table_args__ = ({'schema': 're3', 'autoload': False})
    layerBodId = Column('layer_id', Text, primary_key=True)
    attribution = Column('attribution', Text)
    background = Column('backgroundlayer', Boolean)
    hasLegend = Column('haslegend', Boolean)
    format = Column('image_format', Text)
    gutter = Column('wms_gutter', Integer)
    type = Column('layertype', Text)
    highlightable = Column('highlightable', Boolean)
    opacity = Column('opacity', postgresql.DOUBLE_PRECISION)
    minResolution = Column('minresolution', postgresql.DOUBLE_PRECISION)
    maxResolution = Column('maxresolution', postgresql.DOUBLE_PRECISION)
    parentLayerId = Column('parentlayerid', Text)
    searchable = Column('searchable', Boolean)
    tooltip = Column('tooltip', Boolean)
    serverLayerName = Column('server_layername', Text)
    singleTile = Column('singletile', Boolean)
    subLayersIds = Column('sublayersids', postgresql.ARRAY(Text))
    matrixSet = Column('tilematrixsetid', Text)
    timeEnabled = Column('timeenabled', Boolean)
    timestamps = Column('timestamps', postgresql.ARRAY(Text))
    timeBehaviour = Column('time_behaviour', Text)
    maps = Column('topics', Text)
    chargeable = Column('chargeable', Boolean)
    staging = Column('staging', Text)
    wmsLayers = Column('wms_layers', Text)
    wmsUrl = Column('wms_url', Text)
    updateDelay = Column('geojson_update_delay', Integer)
    geojsonUrlde = Column('geojson_url_de', Text)
    geojsonUrlfr = Column('geojson_url_fr', Text)
    geojsonUrlit = Column('geojson_url_it', Text)
    geojsonUrlrm = Column('geojson_url_rm', Text)
    geojsonUrlen = Column('geojson_url_en', Text)
    config3d = Column('fk_config3d', Boolean)
    srid = Column('srid', Text)
    shop = Column('shop_option_arr', postgresql.ARRAY(Text))

    def layerConfig(self, params):
        config = {}
        translate = params.translate
        settings = params.request.registry.settings
        geodataStaging = settings['geodata_staging']
        wmsHost = settings['wmshost']
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
                elif k == 'matrixSet':
                    if val != self.defaultMatrixSet21781 and \
                            self.__dict__['srid'] != '4326':
                        config['resolutions'] = self._getResolutionsFromMatrixSet(
                            val)
                else:
                    config[k] = val

        if config['type'] in ('wmts', 'aggregate', 'geojson'):
            del config['singleTile']

        if config['type'] == 'wms':
            if geodataStaging != 'prod':
                config['wmsUrl'] = make_agnostic(
                    config['wmsUrl'].replace('wms.geo.admin.ch', wmsHost))
        elif config['type'] == 'geojson':
            api_url = params.request.registry.settings['api_url']
            config['styleUrl'] = make_agnostic(
                api_url + '/static/vectorStyles/' + self.layerBodId + '.json')
            config['geojsonUrl'] = self._getGeoJsonUrl(params.lang)
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

    def _getResolutionsFromMatrixSet(self, matrixSet):
        gagrid = GeoadminTileGrid()
        matrixSet = int(matrixSet.split('_')[1])
        return gagrid.RESOLUTIONS[0:matrixSet + 1]


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


class GetCap(object):
    __dbname__ = 'bod'
    id = Column('fk_dataset_id', Text, primary_key=True)
    arr_all_formats = Column('format', Text)
    tile_matrix_set_id = Column('tile_matrix_set_id', Text)
    timestamp = Column('timestamp', Text)
    sswmts = Column('sswmts', Integer)
    bod_layer_id = Column('bod_layer_id', Text)
    staging = Column('staging', Text)
    bezeichnung = Column('bezeichnung', Text)
    kurzbezeichnung = Column('kurzbezeichnung', Text)
    abstract = Column('abstract', Text)
    inspire_name = Column('inspire_name', Text)
    inspire_abstract = Column('inspire_abstract', Text)
    inspire_oberthema_name = Column('inspire_oberthema_name', Text)
    inspire_oberthema_abstract = Column('inspire_oberthema_abstract', Text)
    geobasisdatensatz_name = Column('geobasisdatensatz_name', Text)
    datenherr = Column('datenherr', Text)
    wms_kontakt_abkuerzung = Column('wms_kontakt_abkuerzung', Text)
    wms_kontakt_name = Column('wms_kontakt_name', Text)
    zoomlevel_min = Column('zoomlevel_min', Integer)
    zoomlevel_max = Column('zoomlevel_max', Integer)
    maps = Column('topics', Text)  # the topics
    chargeable = Column('chargeable', Boolean)
    idGeoCat = Column('idgeocat', Text)


class GetCapFr(Base, GetCap):
    __tablename__ = 'view_bod_wmts_getcapabilities_fr'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapDe(Base, GetCap):
    __tablename__ = 'view_bod_wmts_getcapabilities_de'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapEn(Base, GetCap):
    __tablename__ = 'view_bod_wmts_getcapabilities_en'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapIt(Base, GetCap):
    __tablename__ = 'view_bod_wmts_getcapabilities_it'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapRm(Base, GetCap):
    __tablename__ = 'view_bod_wmts_getcapabilities_rm'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapThemes(object):
    __dbname__ = 'bod'
    id = Column('inspire_id', Text, primary_key=True)
    inspire_name = Column('inspire_name', Text)
    inspire_abstract = Column('inspire_abstract', Text)
    inspire_oberthema_name = Column('inspire_oberthema_name', Text)
    oberthema_id = Column('oberthema_id', Text)
    inspire_oberthema_abstract = Column('inspire_oberthema_abstract', Text)
    fk_dataset_id = Column('fk_dataset_id', Text)
    sswmts = Column('sswmts', Text)


class GetCapThemesFr(Base, GetCapThemes):
    __tablename__ = 'view_bod_wmts_getcapabilities_themes_fr'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapThemesDe(Base, GetCapThemes):
    __tablename__ = 'view_bod_wmts_getcapabilities_themes_de'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapThemesEn(Base, GetCapThemes):
    __tablename__ = 'view_bod_wmts_getcapabilities_themes_en'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapThemesIt(Base, GetCapThemes):
    __tablename__ = 'view_bod_wmts_getcapabilities_themes_it'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class GetCapThemesRm(Base, GetCapThemes):
    __tablename__ = 'view_bod_wmts_getcapabilities_themes_rm'
    __table_args__ = ({'schema': 're3', 'autoload': False})


class ServiceMetadata(object):
    id = Column('wms_id', Text, primary_key=True)
    pk_map_name = Column('pk_map_name', Text)
    title = Column('title', Text)
    onlineresource = Column('onlineresource', Text)
    abstract = Column('abstract', Text)
    keywords = Column('keywords', Text)
    fee = Column('fee', Text)
    accessconstraint = Column('accessconstraint', Text)
    encoding = Column('encoding', Text)
    feature_info_mime_type = Column('feature_info_mime_type', Text)
    map_projection = Column('map_projection', Text)
    fk_contact_id = Column('fk_contact_id', Integer)
    addresstype = Column('addresstype', Text)
    address = Column('address', Text)
    postcode = Column('postcode', Integer)
    city = Column('city', Text)
    country = Column('country', Text)
    contactelectronicmailaddress = Column('contactelectronicmailaddress', Text)
    contactperson = Column('contactperson', Text)
    contactvoicetelephon = Column('contactvoicetelephon', Text)
    stateorprovince = Column('stateorprovince', Text)
    fk_contactorganisation_id = Column('fk_contactorganisation_id', Integer)
    abkuerzung = Column('abkuerzung', Text)
    name = Column('name', Text)


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


def computeHeader(mapName):
    gagrid = GeoadminTileGrid()
    minZoom = 0
    maxZoom = 28
    dpi = 90.7
    lods = []
    for zoom in range(minZoom, maxZoom + 1):
        lods.append(
            {'level': zoom,
             'resolution': gagrid.getResolution(zoom),
             'scale': gagrid.getScale(zoom, dpi=dpi),
             'width': gagrid.numberOfXTilesAtZoom(zoom),
             'height': gagrid.numberOfYTilesAtZoom(zoom)}
        )

    return {
        'mapName': mapName,
        'description': 'Configuration for the map (topic) ' + mapName,
        'copyrightText': 'Data ' + mapName,
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
            'xmin': 458000, 'ymin': 76375, 'xmax': 862500, 'ymax': 289125,
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
    id = Column('topic', Text, primary_key=True)
    orderKey = Column('order_key', Integer)
    availableLangs = Column('lang', Text)
    selectedLayers = Column('selected_layers', postgresql.ARRAY(Text))
    defaultBackground = Column('default_background', Text)
    activatedLayers = Column('activated_layers', postgresql.ARRAY(Text))
    backgroundLayers = Column('background_layers', postgresql.ARRAY(Text))
    showCatalog = Column('show_catalog', Boolean)
    staging = Column('staging', Text)
    plconf = Column('permalink_configuration', Text)


class Catalog(Base):
    __dbname__ = 'bod'
    __tablename__ = 'view_catalog'
    __table_args__ = ({'schema': 're3', 'autoload': False})
    id = Column('bgdi_id', Integer, primary_key=True)
    parentId = Column('parent_id', Integer)
    topic = Column('topic', Text)
    category = Column('category', Text)
    layerBodId = Column('bod_layer_id', Text)
    nameDe = Column('name_de', Text)
    nameFr = Column('name_fr', Text)
    nameIt = Column('name_it', Text)
    nameRm = Column('name_rm', Text)
    nameEn = Column('name_en', Text)
    orderKey = Column('order_key', Integer)
    selectedOpen = Column('selected_open', Boolean)
    staging = Column('staging', Text)

    def to_dict(self, lang):

        self.label = self._get_label_from_lang(lang)

        return dict([
            (k, getattr(self, k)) for
            k in self.__dict__.keys()
            if not k.startswith("_") and
            self.__dict__[k] is not None and
            k not in ('nameDe', 'nameFr', 'nameIt', 'nameRm', 'nameEn')
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
    layerBodId = Column('layer_id', Text, primary_key=True)
    header = Column('header', Text)
    footer = Column('footer', Text)
    data_created = Column('data_created', Text)
    data_imported = Column('data_imported', Text)


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


def get_wmts_models(lang):
    if lang == 'fr':
        return {
            'GetCap': GetCapFr,
            'GetCapThemes': GetCapThemesFr,
            'ServiceMetadata': ServiceMetadataFr
        }
    elif lang == 'it':
        return {
            'GetCap': GetCapIt,
            'GetCapThemes': GetCapThemesFr,
            'ServiceMetadata': ServiceMetadataIt
        }
    elif lang == 'en':
        return {
            'GetCap': GetCapEn,
            'GetCapThemes': GetCapThemesEn,
            'ServiceMetadata': ServiceMetadataEn
        }
    elif lang == 'rm':
        return {
            'GetCap': GetCapRm,
            'GetCapThemes': GetCapThemesDe,
            'ServiceMetadata': ServiceMetadataRm
        }
    else:
        return {
            'GetCap': GetCapDe,
            'GetCapThemes': GetCapThemesDe,
            'ServiceMetadata': ServiceMetadataDe
        }


class CacheUpdate(Base):
    __dbname__ = 'bod'
    __tablename__ = 'dataset_cache'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    id = Column('layer_id', Text, primary_key=True)
    cache_type = Column('cache_type', Text)
    cache_modified = Column('cache_modified', DateTime)
