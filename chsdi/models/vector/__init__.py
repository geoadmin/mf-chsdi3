# -*- coding: utf-8 -*-

import re
import geojson
import esrijson
import datetime
import decimal
from pyramid.threadlocal import get_current_registry
from chsdi.models.types import GeometryChsdi
from chsdi.lib.helpers import transform_round_geometry
from shapely.geometry import box
from sqlalchemy.sql import func
from sqlalchemy.orm.util import class_mapper
from sqlalchemy.orm.properties import ColumnProperty
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape


Geometry2D = GeometryChsdi(geometry_type='GEOMETRY', dimension=2, srid=2056)
Geometry3D = GeometryChsdi(geometry_type='GEOMETRYZ', dimension=3, srid=2056)


MAX_FEATURE_GEOMETRY_SIZE = 1e6

DEFAULT_OUPUT_SRID = 21781


def get_resolution(imageDisplay, mapExtent):
    bounds = mapExtent.bounds
    map_meter_width = abs(bounds[0] - bounds[2])
    map_meter_height = abs(bounds[1] - bounds[3])
    x_res = map_meter_width / imageDisplay[0]
    y_res = map_meter_height / imageDisplay[1]
    return max(x_res, y_res)


def get_scale(imageDisplay, mapExtent):
    resolution = get_resolution(imageDisplay, mapExtent)
    return resolution * 39.37 * imageDisplay[2]


def has_buffer(imageDisplay, mapExtent, tolerance):
    return bool(imageDisplay and mapExtent and tolerance is not None
        and all(val != 0 for val in imageDisplay) and mapExtent.area != 0)


def get_tolerance_meters(imageDisplay, mapExtent, tolerance):
    if has_buffer(imageDisplay, mapExtent, tolerance):
        bounds = mapExtent.bounds
        map_meter_width = abs(bounds[0] - bounds[2])
        map_meter_height = abs(bounds[1] - bounds[3])
        img_px_width = imageDisplay[0]
        img_px_height = imageDisplay[1]
        tolerance_meters = max(map_meter_width / img_px_width,
                               map_meter_height / img_px_height) * tolerance
        return tolerance_meters
    return 0.0


def _wrap_wkb_geometry(geometry, srid):
    if not isinstance(geometry, WKBElement):
        return WKBElement(buffer(geometry.wkb), srid)
    return geometry


class Vector(object):
    attributes = {}

    # Overrides GeoInterface
    def __read__(self):
        id = None
        geom = None
        bbox = None
        properties = {}
        for p in class_mapper(self.__class__).iterate_properties:
            if isinstance(p, ColumnProperty):
                if len(p.columns) != 1:  # pragma: no cover
                    raise NotImplementedError
                col = p.columns[0]
                val = getattr(self, p.key)
                if col.primary_key:
                    id = val
                elif (isinstance(col.type, GeometryChsdi)
                      and col.name == self.geometry_column_to_return().name):
                    if hasattr(self, '_shape') and \
                            len(self._shape) < MAX_FEATURE_GEOMETRY_SIZE:
                        geom = self._shape
                    elif val is not None and \
                            (len(val.data) < MAX_FEATURE_GEOMETRY_SIZE or
                            self.ignore_max_feature_geometry_size_column()):
                        geom = to_shape(val)
                    try:
                        bbox = geom.bounds
                    except Exception:
                        pass
                elif (not col.foreign_keys
                      and not isinstance(col.type, GeometryChsdi)):
                    properties[p.key] = val
        properties = self.insert_label(properties)
        return id, geom, properties, bbox

    def transform_shape(self, geom, srid_to, rounding=True):
        return transform_round_geometry(geom, self.srid, srid_to, rounding=rounding)

    @property
    def srid(self):
        return self.geometry_column().type.srid

    def to_esrijson(self, trans, returnGeometry, srid=DEFAULT_OUPUT_SRID):
        if returnGeometry:
            id, geom, properties, bbox = self.__read__()
            geom = self.transform_shape(geom, srid, rounding=True)
            bbox = self.transform_shape(bbox, srid, rounding=True)

            return esrijson.Feature(id=id,
                                   featureId=id,  # Duplicate id for backward compat...
                                   geometry=geom,
                                   wkid=srid,  # self.geometry_column().type.srid_out,
                                   attributes=properties,
                                   bbox=bbox,
                                   layerBodId=self.__bodId__,
                                   layerName=trans(self.__bodId__))
        return self._no_geom_template(trans)

    def to_geojson(self, trans, returnGeometry, srid=DEFAULT_OUPUT_SRID):
        if returnGeometry:
            id, geom, properties, bbox = self.__read__()
            geom = self.transform_shape(geom, srid, rounding=True)
            bbox = self.transform_shape(bbox, srid, rounding=True)

            # TODO: no need to reproject geometry?
            return geojson.Feature(id=id,
                                   featureId=id,  # Duplicate id for backward compat...
                                   type="Feature",
                                   geometry=geom,
                                   properties=properties,
                                   bbox=bbox,
                                   layerBodId=self.__bodId__,
                                   layerName=trans(self.__bodId__))
        return self._no_geom_template(trans, attrs_name='properties')

    def _no_geom_template(self, trans, attrs_name='attributes'):
        return {
            'layerBodId': self.__bodId__,
            'layerName': trans(self.__bodId__),
            'featureId': self.id,
            'id': self.id,
            attrs_name: self.get_attributes()
        }

    @classmethod
    def geometry_column(cls):
        return cls.__mapper__.columns['the_geom']

    def geometry_column_to_return(cls):
        geom_column_name = cls.__returnedGeometry__ if hasattr(cls, '__returnedGeometry__') else 'the_geom'
        return cls.__mapper__.columns[geom_column_name]

    def ignore_max_feature_geometry_size_column(cls):
        return cls.__mapper__columns[cls.__ignore_max_feature_geometry_size__] if hasattr(cls, '__ignore_max_feature_geometry_size__') else False

    @classmethod
    def primary_key_column(cls):
        return cls.__mapper__.primary_key[0]

    @classmethod
    def time_instant_column(cls):
        return getattr(cls, cls.__timeInstant__)

    @classmethod
    def label_column(cls):
        return cls.__mapper__.columns[cls.__label__] if hasattr(cls, '__label__') else cls.__mapper__.primary_key[0]

    @classmethod
    def geom_filter(cls, geometry, imageDisplay, mapExtent, tolerance, srid):
        tolerance_meters = get_tolerance_meters(imageDisplay, mapExtent, tolerance)
        geom_column = cls.geometry_column()
        wkb_geometry = WKBElement(buffer(geometry.wkb), srid)
        return func.ST_DWITHIN(geom_column,
                               transform_geometry(geom_column, wkb_geometry, srid),
                               tolerance_meters)

    @classmethod
    def geom_intersects(cls, geometry, srid):
        wkb_geometry = _wrap_wkb_geometry(geometry, srid)
        geom_column = cls.geometry_column()
        return func.ST_Intersects(geom_column,
                                  transform_geometry(geom_column, wkb_geometry, srid))

    @classmethod
    def geom_intersection(cls, geometry, srid):
        wkb_geometry = _wrap_wkb_geometry(geometry, srid)
        geom_column = cls.geometry_column()
        return func.ST_Intersection(geom_column,
                                    transform_geometry(geom_column, wkb_geometry, srid))

    '''
    The order_by_distance ordering is potentially very costly, depending
    of the number of results of whole query. To protect against such costly
    operations, a hard-coded tolerance of 250 meters is implemented. If the
    passed tolerance is bigger than 250 meters, we simply ignore the odering
    of the results.
    The limit parameter can't mitigate this, as sorting is done with all features
    inside the tolerance before limit is applied.
    Note that the order_by parameer is an undocumented feature and is used
    by selected clients only.
    '''
    @classmethod
    def order_by_distance(cls, geometry, geometryType, imageDisplay, mapExtent, tolerance, limit, srid):
        tolerance_meters = get_tolerance_meters(imageDisplay, mapExtent, tolerance)
        # If limit is equal to 1 we have to be accurate
        if tolerance_meters <= 250.0 or limit == 1:
            wkb_geometry = WKBElement(buffer(geometry.wkb), srid)
            geom_column = cls.geometry_column()
            return func.ST_DISTANCE(geom_column, transform_geometry(geom_column, wkb_geometry, srid))
        return None

    @classmethod
    def get_column_by_property_name(cls, mapped_column_name):
        if mapped_column_name in cls.__mapper__.columns:
            return cls.__mapper__.columns.get(mapped_column_name)
        return None

    # Based on a naming convention
    @classmethod
    def get_queryable_attributes_keys(cls, lang):
        queryable_attributes = []
        if hasattr(cls, '__queryable_attributes__'):
            settings = get_current_registry().settings
            available_langs = settings['available_languages'].replace(' ', '|')
            for attr in cls.__queryable_attributes__:
                fallback_match = get_fallback_lang_match(
                    cls.__queryable_attributes__,
                    lang,
                    attr,
                    available_langs
                )
                if fallback_match not in queryable_attributes:
                    queryable_attributes.append(fallback_match)

        return queryable_attributes

    def get_orm_columns_names(self, exclude_pkey=True):
        keys_to_exclude = []
        if exclude_pkey:
            primary_key_column = self.__mapper__.get_property_by_column(self.primary_key_column()).key
            keys_to_exclude.append(primary_key_column)

        for column in self.__mapper__.columns:
            mapped_column_name = self.__mapper__.get_property_by_column(column).key
            if mapped_column_name not in keys_to_exclude and not isinstance(column.type, GeometryChsdi):
                yield mapped_column_name

    def get_attributes_keys(self):
        return [col_name for col_name in self.get_orm_columns_names(exclude_pkey=False)]

    def get_attributes(self, exclude_pkey=True):
        attributes = {}
        for mapped_column_name in self.get_orm_columns_names(exclude_pkey=exclude_pkey):
            attribute = getattr(self, mapped_column_name)
            attributes[mapped_column_name] = format_attribute(attribute)
        return self.insert_label(attributes)

    def insert_label(self, attributes):
        label_mapped_column_name = self.__mapper__.get_property_by_column(self.label_column()).key
        attributes['label'] = format_attribute(getattr(self, label_mapped_column_name))
        return attributes


def transform_geometry(geom_column, wkb_geometry, srid):
    if geom_column.type.srid != srid:
        wkb_geometry = func.ST_Transform(wkb_geometry, geom_column.type.srid)
    return wkb_geometry


def format_attribute(attribute):
    if isinstance(attribute, decimal.Decimal):
        return attribute.__float__()
    elif isinstance(attribute, datetime.datetime):
        return attribute.strftime("%d.%m.%Y")
    else:
        return attribute


def extent_area(i):
    geom = box(i[0], i[1], i[2], i[3])
    return geom.area


def get_fallback_lang_match(queryable_attrs, lang, attr, available_langs):
    # de and fr at least are defined
    def replace_last(source_string, replace_what, replace_with):
        head, sep, tail = source_string.rpartition(replace_what)
        return head + replace_with + tail

    match = re.search(r'(_(%s))$' % available_langs, attr)
    if match is not None:
        # Lang specific attr
        suffix = '_%s' % lang
        suffix_attr = match.groups()[0]

        attr_to_match = replace_last(attr, suffix_attr, suffix)
        if attr_to_match in queryable_attrs:
            return attr_to_match
        else:
            if suffix in ('_rm', '_en'):
                suffix = '_de'
                attr_to_match = replace_last(attr, suffix_attr, suffix)
                if attr_to_match in queryable_attrs:
                    return attr_to_match
            elif suffix == '_it':
                suffix = '_fr'
                attr_to_match = replace_last(attr, suffix_attr, suffix)
                if attr_to_match in queryable_attrs:
                    return attr_to_match
    # Not based on lang
    return attr
