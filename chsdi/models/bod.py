# -*- coding: utf-8 -*-

import json

from sqlalchemy import Column, Text, Integer, Boolean
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects import sqlite
from sqlalchemy.orm import scoped_session, sessionmaker

from chsdi.lib.helpers import make_agnostic
from chsdi.models import bases

import os

# To switch between file-based/sqlite backed data and
# postgres/bod backed data, just adapt the variable below

__bodbackend__ = 'sqlite'  # file-based backend
# __bodbackend__ = 'bod'   # postgres backend

Base = bases[__bodbackend__]


def is_sqlite():
    return __bodbackend__ == 'sqlite'


class Bod(object):
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
    __tablename__ = 'view_layers_js'
    if is_sqlite():
        opacity = Column('opacity', sqlite.FLOAT)
        minResolution = Column('minresolution', sqlite.FLOAT)
        maxResolution = Column('maxresolution', sqlite.FLOAT)
        subLayersIds = Column('sublayersids', Text)
        timestamps = Column('timestamps', Text)
    else:
        __table_args__ = ({'schema': 're3'})
        opacity = Column('opacity', postgresql.DOUBLE_PRECISION)
        minResolution = Column('minresolution', postgresql.DOUBLE_PRECISION)
        maxResolution = Column('maxresolution', postgresql.DOUBLE_PRECISION)
        subLayersIds = Column('sublayersids', postgresql.ARRAY(Text))
        timestamps = Column('timestamps', postgresql.ARRAY(Text))
    layerBodId = Column('layer_id', Text, primary_key=True)
    attribution = Column('attribution', Text)
    background = Column('backgroundlayer', Boolean)
    hasLegend = Column('haslegend', Boolean)
    format = Column('image_format', Text)
    gutter = Column('wms_gutter', Integer)
    type = Column('layertype', Text)
    highlightable = Column('highlightable', Boolean)
    parentLayerId = Column('parentlayerid', Text)
    queryable = Column('queryable', Boolean)
    searchable = Column('searchable', Boolean)
    selectbyrectangle = Column('selectbyrectangle', Boolean)
    serverLayerName = Column('server_layername', Text)
    singleTile = Column('singletile', Boolean)
    matrixSet = Column('tilematrixsetid', Text)
    timeEnabled = Column('timeenabled', Boolean)
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

    def layerConfig(self, params):
        config = {}
        translate = params.translate
        excludedAttrs = ('geojsonUrlde', 'geojsonUrlfr', 'geojsonUrlit', 'geojsonUrlrm', 'geojsonUrlen')
        wmsHost = params.request.registry.settings['wmshost']
        for k in self.__dict__.keys():
            if not k.startswith("_") and k not in excludedAttrs and \
                self.__dict__[k] is not None and \
                    k not in ('staging'):
                if k == 'maps':
                    config['topics'] = self.__dict__[k]
                elif k == 'layerBodId':
                    config['label'] = translate(self.__dict__[k])
                elif k == 'attribution':
                    config[k] = translate(self.__dict__[k])
                elif k == 'matrixSet':
                    if self.__dict__[k] != '21781_26':
                        config['resolutions'] = self._getResolutionsFromMatrixSet(
                            self.__dict__[k]
                        )
                elif (k == 'subLayersIds' or k == 'timestamps') and \
                        not isinstance(self.__dict__[k], list):
                    config[k] = self.__dict__[k].split(',')
                else:
                    config[k] = self.__dict__[k]

        layerStaging = self.__dict__['staging']
        if config['type'] == 'wmts':
            del config['singleTile']
        elif config['type'] == 'wms':
            if layerStaging != 'prod':
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

        return {self.layerBodId: config}

    # All fields point to en for now
    def _getGeoJsonUrl(self, lang):
        return self.__dict__['geojsonUrl%s' % lang]

    def _getResolutionsFromMatrixSet(self, matrixSet):
        resolutions = [4000, 3750, 3500, 3250, 3000, 2750, 2500, 2250, 2000, 1750, 1500, 1250,
                       1000, 750, 650, 500, 250, 100, 50, 20, 10, 5, 2.5, 2, 1.5, 1, 0.5, 0.25, 0.1]
        matrixSet = int(matrixSet.split('_')[1])
        return resolutions[0:matrixSet + 1]


class BodLayerDe(Base, Bod):
    __tablename__ = 'view_bod_layer_info_de'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class BodLayerFr(Base, Bod):
    __tablename__ = 'view_bod_layer_info_fr'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class BodLayerIt(Base, Bod):
    __tablename__ = 'view_bod_layer_info_it'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class BodLayerRm(Base, Bod):
    __tablename__ = 'view_bod_layer_info_rm'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class BodLayerEn(Base, Bod):
    __tablename__ = 'view_bod_layer_info_en'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class GetCap(object):
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
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class GetCapDe(Base, GetCap):
    __tablename__ = 'view_bod_wmts_getcapabilities_de'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class GetCapThemes(object):
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
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class GetCapThemesDe(Base, GetCapThemes):
    __tablename__ = 'view_bod_wmts_getcapabilities_themes_de'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


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
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


class ServiceMetadataFr(Base, ServiceMetadata):
    __tablename__ = 'view_wms_service_metadata_fr'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})


# TODO use GetCap model to fill that up instead
def computeHeader(mapName):
    return {
        'mapName': mapName,
        'description': 'Configuration for the map (topic) ' + mapName,
        'copyrightText': 'Data ' + mapName,
        'layers': [],
        'spatialReference': {"wkid": 21781},
        'tileInfo': {
            'rows': 256,  # tile width in pixel
            'cols': 256,
            'dpi': 96,
            'format': 'PNG,JPEG',
            'compressionQuality': '',
            'origin': {"x": 420000, "y": 350000, "spatialReference": {"wkid": 21781}},
            'spatialReference': {"wkid": 21781},
            'lods': [
                {'level': 0, 'resolution': 4000, 'scale': 14285750.5715, 'width': 1, 'height': 1},
                {'level': 1, 'resolution': 3750, 'scale': 13392891.1608, 'width': 1, 'height': 1},
                {'level': 2, 'resolution': 3500, 'scale': 12500031.7501, 'width': 1, 'height': 1},
                {'level': 3, 'resolution': 3250, 'scale': 11607172.3393, 'width': 1, 'height': 1},
                {'level': 4, 'resolution': 3000, 'scale': 10714312.9286, 'width': 1, 'height': 1},
                {'level': 5, 'resolution': 2750, 'scale': 9821453.51791, 'width': 1, 'height': 1},
                {'level': 6, 'resolution': 2500, 'scale': 8928594.10719, 'width': 1, 'height': 1},
                {'level': 7, 'resolution': 2250, 'scale': 8035734.69647, 'width': 1, 'height': 1},
                {'level': 8, 'resolution': 2000, 'scale': 7142875.28575, 'width': 1, 'height': 1},
                {'level': 9, 'resolution': 1750, 'scale': 6250015.87503, 'width': 2, 'height': 1},
                {'level': 10, 'resolution': 1500, 'scale': 5357156.46431, 'width': 2, 'height': 1},
                {'level': 11, 'resolution': 1250, 'scale': 4464297.05359, 'width': 2, 'height': 1},
                {'level': 12, 'resolution': 1000, 'scale': 3571437.64288, 'width': 2, 'height': 2},
                {'level': 13, 'resolution': 750, 'scale': 2678578.23216, 'width': 3, 'height': 2},
                {'level': 14, 'resolution': 650, 'scale': 2321434.46787, 'width': 3, 'height': 2},
                {'level': 15, 'resolution': 500, 'scale': 1785718.82144, 'width': 4, 'height': 3},
                {'level': 16, 'resolution': 250, 'scale': 892859.410719, 'width': 8, 'height': 5},
                {'level': 17, 'resolution': 100, 'scale': 357143.764288, 'width': 19, 'height': 13},
                {'level': 18, 'resolution': 50, 'scale': 178571.882144, 'width': 38, 'height': 25},
                {'level': 19, 'resolution': 20, 'scale': 71428.7528575, 'width': 94, 'height': 63},
                {'level': 20, 'resolution': 10, 'scale': 35714.3764288, 'width': 188, 'height': 125},
                {'level': 21, 'resolution': 5, 'scale': 17857.1882144, 'width': 375, 'height': 250},
                {'level': 22, 'resolution': 2.5, 'scale': 8928.59410719, 'width': 750, 'height': 500},
                {'level': 23, 'resolution': 2, 'scale': 7142.87528575, 'width': 938, 'height': 625},
                {'level': 24, 'resolution': 1.5, 'scale': 5357.15646431, 'width': 1250, 'height': 834},
                {'level': 25, 'resolution': 1, 'scale': 3571.43764288, 'width': 1875, 'height': 1250},
                {'level': 26, 'resolution': 0.5, 'scale': 1785.71882144, 'width': 3750, 'height': 2500},
                {'level': 27, 'resolution': 0.25, 'scale': 892.857, 'width': 7500, 'height': 5000},
                {'level': 28, 'resolution': 0.1, 'scale': 357.1425, 'width': 18750, 'height': 12500}
            ]
        },
        'initialExtent': {
            'xmin': 458000, 'ymin': 76375, 'xmax': 862500, 'ymax': 289125,
            'spatialReference': {'wkid': 21781}
        },
        'fullExtent': {
            'xmin': 42000, 'ymin': 30000, 'xmax': 900000, 'ymax': 350000,
            'spatialReference': {'wkid': 21781}
        },
        'units': 'esriMeters',
        'capabilities': 'Map'
    }


class Topics(Base):
    __tablename__ = 'topics'
    if is_sqlite():
        selectedLayers = Column('selected_layers', Text)
        backgroundLayers = Column('background_layers', Text)
    else:
        selectedLayers = Column('selected_layers', postgresql.ARRAY(Text))
        backgroundLayers = Column('background_layers', postgresql.ARRAY(Text))
        __table_args__ = ({'schema': 're3'})
    id = Column('topic', Text, primary_key=True)
    orderKey = Column('order_key', Integer)
    availableLangs = Column('lang', Text)
    showCatalog = Column('show_catalog', Boolean)
    staging = Column('staging', Text)


class Catalog(Base):
    __tablename__ = 'view_catalog'
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})
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
    path = Column('path', Text)
    depth = Column('depth', Integer)
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
    if not is_sqlite():
        __table_args__ = ({'schema': 're3'})
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
    if lang in ('fr', 'it'):
        return {
            'GetCap': GetCapFr,
            'GetCapThemes': GetCapThemesFr,
            'ServiceMetadata': ServiceMetadataFr
        }
    else:
        return {
            'GetCap': GetCapDe,
            'GetCapThemes': GetCapThemesDe,
            'ServiceMetadata': ServiceMetadataDe
        }


def from_dict(model, values):
    item = model()
    for key in item.__mapper__.columns.keys():
        name = item.__mapper__.columns[key].name
        if name in values:
            setattr(item, key, values[name])
        else:
            raise Exception('Defined column with id ' + key + ' does not have value (' + name + ') in the given dictionary')
    return item


def parse_json(model, filename):
    jsonfile = open(os.path.join(os.path.dirname(__file__), '../../bod/' + filename))
    data = json.load(jsonfile)
    jsonfile.close()
    items = []
    for d in data:
        item = from_dict(model, d)
        items.append(item)
    return items


def initialize_sqlite():
    if not is_sqlite():
        return
    Base.metadata.create_all(Base.metadata.bind)
    items = parse_json(Catalog, 're3.view_catalog.json')
    items.extend(parse_json(Topics, 're3.topics.json'))
    items.extend(parse_json(LayersConfig, 're3.view_layers_js.json'))
    items.extend(parse_json(BodLayerDe, 're3.view_bod_layer_info_de.json'))
    items.extend(parse_json(BodLayerFr, 're3.view_bod_layer_info_fr.json'))
    items.extend(parse_json(BodLayerIt, 're3.view_bod_layer_info_it.json'))
    items.extend(parse_json(BodLayerRm, 're3.view_bod_layer_info_rm.json'))
    items.extend(parse_json(BodLayerEn, 're3.view_bod_layer_info_en.json'))
    items.extend(parse_json(GetCapDe, 're3.view_bod_wmts_getcapabilities_de.json'))
    items.extend(parse_json(GetCapFr, 're3.view_bod_wmts_getcapabilities_fr.json'))
    items.extend(parse_json(ServiceMetadataDe, 're3.view_wms_service_metadata_de.json'))
    items.extend(parse_json(ServiceMetadataFr, 're3.view_wms_service_metadata_fr.json'))
    items.extend(parse_json(GetCapThemesDe, 're3.view_bod_wmts_getcapabilities_themes_de.json'))
    items.extend(parse_json(GetCapThemesFr, 're3.view_bod_wmts_getcapabilities_themes_fr.json'))
    items.extend(parse_json(OerebMetadata, 're3.oereb_interlis_metadata.json'))
    session = scoped_session(sessionmaker())
    session.add_all(items)
    session.commit()
    session.close()
