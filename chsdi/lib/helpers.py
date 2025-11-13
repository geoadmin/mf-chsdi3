import threading
import re
import math
import requests
import datetime
import gzip
import unidecode
from decimal import Decimal

from itertools import chain
from itertools import zip_longest

import cachetools
from pyramid.threadlocal import get_current_registry
from pyramid.i18n import get_locale_name
from pyramid.url import route_url
from pyramid.httpexceptions import HTTPBadRequest, HTTPRequestTimeout
import unicodedata

from urllib.parse import urlparse, urljoin, quote
from functools import reduce
import xml.etree.ElementTree as etree
from pyproj import CRS, Transformer
from requests.exceptions import ConnectionError, Timeout, RequestException
from urllib3.exceptions import InsecureRequestWarning
from shapely.ops import transform as shape_transform
from shapely.wkt import dumps as shape_dumps, loads as shape_loads
from shapely.geometry.base import BaseGeometry
from chsdi.lib.parser import WhereParser
from chsdi.lib.exceptions import QueryParseException, CoordinatesTransformationException
import logging

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # pylint: disable=no-member

log = logging.getLogger(__name__)

REQUESTS_DEFAULT_TIMEOUT = 5


# Rounding to abount 0.1 meters
COORDINATES_DECIMALS_FOR_METRIC_PROJ = 1
COORDINATES_DECIMALS_FOR_DEGREE_PROJ = 6


def to_utf8(data):
    try:
        data = data.decode('utf8')
    except (UnicodeDecodeError, AttributeError):
        pass
    return data

# Number of element in an iterator


def ilen(iterable):
    return reduce(lambda sum, element: sum + 1, iterable, 0)


def make_agnostic(path):
    handle_path = lambda x: x.split('://')[1] if len(x.split('://')) == 2 else path
    if path.startswith('http') and path.find('localhost') == -1:
        path = handle_path(path)
        return '//' + path
    else:
        return path


def make_geoadmin_url(request, agnostic=False):
    protocol = request.scheme
    base_url = ''.join((protocol, '://', request.registry.settings['geoadminhost']))
    if agnostic:
        return make_agnostic(base_url)
    return base_url


def resource_exists(path, headers=None, verify=False):
    if headers is None:
        headers = {'User-Agent': 'mf-geoadmin/python'}
    try:
        r = requests.head(path, headers=headers, verify=verify, timeout=REQUESTS_DEFAULT_TIMEOUT)
    except Timeout as e:
        log.error('Timeout while requesting HEAD on "%s"\n%s' % (path, e))
        return False
    except ConnectionError as e:
        log.error('ConnectionError while requesting HEAD on "%s\n%s"' % (path, e))
        return False
    except RequestException as e:
        log.error('Unknown exception while requesting "%s"\n%s' % (path, e))
        return False
    return r.status_code == requests.codes.ok  # pylint: disable=no-member


def sanitize_url(url):
    sanitized = url
    try:
        sanitized = urljoin(url, urlparse(url).path.replace('//', '/'))
    except Exception:
        pass
    return sanitized


def locale_negotiator(request):
    try:
        lang = request.params.get('lang')
    except UnicodeDecodeError:  # pragma: no cover
        raise HTTPBadRequest('Could not parse URL and parameters. Request send must be encoded in utf-8.')
    # This might happen if a POST request is aborted before all the data could be transmitted
    except IOError:  # pragma: no cover
        raise HTTPRequestTimeout('Request was aborted. Didn\'t receive full request')

    settings = get_current_registry().settings
    languages = settings['available_languages'].split()
    if lang == 'rm':
        return 'fi'
    elif lang is None or lang not in languages:
        if request.accept_language:
            return request.accept_language.best_match(languages, 'de')
        # the default_locale_name configuration variable
        return get_locale_name(request)
    return lang


def check_even(number):
    if number % 2 == 0:
        return True
    return False


def remove_accents(input_str):
    if input_str is None:
        return input_str
    input_str = input_str.replace('ü', 'ue')
    input_str = input_str.replace('Ü', 'ue')
    input_str = input_str.replace('ä', 'ae')
    input_str = input_str.replace('Ä', 'ae')
    input_str = input_str.replace('ö', 'oe')
    input_str = input_str.replace('Ö', 'oe')
    return ''.join(c for c in unicodedata.normalize('NFD', input_str) if unicodedata.category(c) != 'Mn')


def format_query(model, value, lang):
    '''
        Supported operators on numerical or date values are "=, !=, >=, <=, > and <"
        Supported operators for text are "ilike and not ilike"
    '''
    where = None

    def escapeSQL(value):
        if 'ilike' in value:
            match = re.search(r'([\w]+\s)(ilike|not ilike)(\s\'%)([\s\S]*)(%\')', value)
            where = ''.join((
                match.group(1).replace('\'', 'E\''),
                match.group(2),
                match.group(3),
                match.group(4).replace('\\', '\\\\')
                              .replace('\'', "\''")
                              .replace('_', '\\_'),
                match.group(5)
            ))
            return where
        return value

    def get_queryable_attributes(model, lang):
        attributes = []
        if hasattr(model, '__queryable_attributes__'):
            attributes = model.get_queryable_attributes_keys(lang)
        return attributes

    # Check if attributes are queryable and replace by the DB column name
    def replacePropByColumnName(model, values, lang):
        res = []
        queryable_attributes = get_queryable_attributes(model, lang)
        for val in values:
            prop = val.split(' ')[0].strip()
            column = model.get_column_by_property_name(prop)
            if prop not in queryable_attributes:
                error_msg = "Query attribute '{}' is not queryable. Queryable attributes are '{}'" \
                    .format(prop, ",".join(queryable_attributes))
                log.error(error_msg)
                raise QueryParseException(error_msg)
            if column is None:
                error_msg = "Query attribute '{} doesn't exist in the model".format(prop)
                log.error(error_msg)
                raise QueryParseException(error_msg)

            val = val.replace(prop, str(column.name))
            res.append(val)
        return res

    def merge_statements(statements, operators):
        ''' Given values=["toto >1', "'tutu' like 'tata%'"] and operators=["AND" ]
            return "toto >1' AND 'tutu' like 'tata%'"
        '''
        if len(statements) - 1 != ilen(operators):
            raise Exception

        # iters = [iter(statements), iter(operators)]
        # full = list(it.next() for it in cycle(iters))

        full = [x for x in chain.from_iterable(zip_longest(statements, operators))
            if x is not None]

        return " ".join(full)

    try:
        w = WhereParser(value)
        tokens = list(w.tokens)
        if ilen(tokens) == 0:
            return None
        # TODO: what does really do?
        # values = map(escapeSQL, values)
        values = replacePropByColumnName(model, tokens, lang)
        operators = list(w.operators)

        where = merge_statements(values, operators)

    except QueryParseException as qpe:
        raise HTTPBadRequest("Failed to parse where/layersDef: {}".format(qpe))
    except HTTPBadRequest:
        raise Exception
    except Exception as e:
        log.error("Unkown error while parsing where/layerDefs: {}".format(e))
        return None
    return where


def quoting(text):
    return quote(text.encode('utf-8'))


def parseHydroXML(id, root):
    html_attr = {'date_time': '-', 'abfluss': '-', 'wasserstand': '-', 'wassertemperatur': '-'}
    for child in root:
        fid = child.attrib['StrNr']
        if fid == id:
            if child.attrib['Typ'] == '10':
                for attr in child:
                    if attr.tag == 'Datum':
                        html_attr['date_time'] = attr.text
                    # Zeit is always parsed after Datum
                    elif attr.tag == 'Zeit':
                        html_attr['date_time'] = html_attr['date_time'] + ' ' + attr.text
                    elif attr.tag == 'Wert':
                        html_attr['abfluss'] = attr.text
                        break
            elif child.attrib['Typ'] == '02':
                for attr in child:
                    if attr.tag == 'Datum':
                        html_attr['date_time'] = attr.text
                    # Zeit is always parsed after Datum
                    elif attr.tag == 'Zeit':
                        html_attr['date_time'] = html_attr['date_time'] + ' ' + attr.text
                    elif attr.tag == 'Wert':
                        html_attr['wasserstand'] = attr.text
                        break
            elif child.attrib['Typ'] == '03':
                for attr in child:
                    if attr.tag == 'Datum':
                        html_attr['date_time'] = attr.text
                    # Zeit is always parsed after Datum
                    elif attr.tag == 'Zeit':
                        html_attr['date_time'] = html_attr['date_time'] + ' ' + attr.text
                    elif attr.tag == 'Wert':
                        html_attr['wassertemperatur'] = attr.text
                        break
    return html_attr


def imagesize_from_metafile(tileUrlBasePath, bvnummer):
    width = None
    height = None
    headers = {'Referer': 'http://admin.ch', 'User-Agent': 'mf-geoadmin/python'}
    metaurl = tileUrlBasePath + '/' + bvnummer + '/tilemapresource.xml'
    s = requests.Session()
    response = s.get(metaurl, headers=headers)
    if response.status_code == requests.codes.ok:  # pylint: disable=no-member
        xml = etree.fromstring(response.content)
        bb = xml.find('BoundingBox')
        if bb is not None:
            width = abs(int(float(bb.get('maxy'))) - int(float(bb.get('miny'))))
            height = abs(int(float(bb.get('maxx'))) - int(float(bb.get('minx'))))
    return (width, height)


@cachetools.cached(cache={}, lock=threading.Lock())
def get_crs_from_srid(srid):
    return CRS.from_string('EPSG:{}'.format(srid))


@cachetools.cached(cache={}, lock=threading.Lock())
def get_transformer(srid_from, srid_to):
    return Transformer.from_crs(srid_from, srid_to, always_xy=True)


def get_precision_for_proj(srid):
    precision = COORDINATES_DECIMALS_FOR_METRIC_PROJ
    crs = get_crs_from_srid(srid)
    if crs.is_geographic:
        precision = COORDINATES_DECIMALS_FOR_DEGREE_PROJ
    return precision


def _round_bbox_coordinates(bbox, precision=None):
    tpl = '%.{}f'.format(precision)
    if precision is not None:
        return [float(Decimal(tpl % c)) for c in bbox]
    else:
        return bbox


def _round_shape_coordinates(shape, precision=None):
    if precision is None:
        return shape
    else:
        return shape_loads(
            shape_dumps(shape, rounding_precision=precision)
        )


def round_geometry_coordinates(geom, precision=None):
    if isinstance(geom, (list, tuple, )):
        return _round_bbox_coordinates(geom, precision=precision)
    elif isinstance(geom, BaseGeometry):
        return _round_shape_coordinates(geom, precision=precision)
    else:
        return geom


def _transform_point(coords, srid_from, srid_to):
    transformer = get_transformer(srid_from, srid_to)
    return transformer.transform(coords[0], coords[1])


def transform_round_geometry(geom, srid_from, srid_to, rounding=True):
    if (srid_from == srid_to):
        if rounding:
            precision = get_precision_for_proj(srid_to)
            return round_geometry_coordinates(geom, precision=precision)
        return geom
    if isinstance(geom, (list, tuple, )):
        return _transform_coordinates(geom, srid_from, srid_to, rounding=rounding)
    else:
        return _transform_shape(geom, srid_from, srid_to, rounding=rounding)


# Reprojecting pairs of coordinates and rounding them if necessary
# Only a point or a line are considered
def _transform_coordinates(coordinates, srid_from, srid_to, rounding=True):
    if len(coordinates) % 2 != 0:
        raise ValueError
    new_coords = []
    coords_iter = iter(coordinates)
    try:
        for pnt in zip(coords_iter, coords_iter):
            new_pnt = _transform_point(pnt, srid_from, srid_to)
            new_coords += new_pnt
        if rounding:
            precision = get_precision_for_proj(srid_to)
            new_coords = _round_bbox_coordinates(new_coords, precision=precision)
    except Exception:
        raise CoordinatesTransformationException("Cannot transform coordinates {} from {} to {}".format(coordinates, srid_from, srid_to))
    return new_coords


def _transform_shape(geom, srid_from, srid_to, rounding=True):
    transformer = get_transformer(srid_from, srid_to)

    new_geom = shape_transform(transformer.transform, geom)
    if rounding:
        precision = get_precision_for_proj(srid_to)
        return _round_shape_coordinates(new_geom, precision=precision)
    return new_geom

# float('NaN') does not raise an Exception. This function does.


def float_raise_nan(val):
    ret = float(val)
    if math.isinf(ret):
        raise ValueError('infinity is not considered to be a valid value')
    elif math.isnan(ret):
        raise ValueError('nan is not considered valid float')
    return ret


def parse_box2d(stringBox2D):
    extent = stringBox2D.replace('BOX(', '').replace(')', '').replace(',', ' ')
    box = list(map(float, extent.split(' ')))
    return box


def validate_box2d(box2D):
    # Bottom left to top right only
    if len(box2D) != 4 or box2D[0] > box2D[2] or box2D[1] > box2D[3]:
        raise ValueError('Invalid box2D.')
    return box2D


def center_from_box2d(box2D):
    box2D = validate_box2d(box2D)
    return [
        box2D[0] + ((box2D[2] - box2D[0]) / 2),
        box2D[1] + ((box2D[3] - box2D[1]) / 2)
    ]


def shift_to(coords, srid):
    cds = []
    x_offset = 2e6
    y_offset = 1e6
    coords_copy = coords[:]
    while len(coords_copy) > 0:
        c = coords_copy.pop(0)
        if not isinstance(c, (int, float)):
            raise TypeError('Coordinates should be of type int or float')
        if srid == 2056:
            cds.append(c + x_offset if len(coords_copy) % 2 else c + y_offset)
        elif srid == 21781:
            cds.append(c - x_offset if len(coords_copy) % 2 else c - y_offset)
    return cds


def parse_date_string(dateStr, format_input='%Y-%m-%d', format_output='%d.%m.%Y'):
    try:
        return datetime.datetime.strptime(
            dateStr.strip(), format_input
        ).strftime(format_output)
    except Exception:
        return '-'


def parse_date_datenstand(dateDatenstand):
    result = ''
    for part in re.split('([-| ])', str(dateDatenstand).strip()):
        if part.isdigit():
            if len(part) == 4:
                result += parse_date_string(part, '%Y', '%Y')
            elif len(part) == 6:
                result += parse_date_string(part, '%Y%m', '%m.%Y')
            elif len(part) == 8:
                result += parse_date_string(part, '%Y%m%d', '%d.%m.%Y')
        elif part == '-' or part == ' ':
            result += part
        elif len(part) == 5 and ':' in part:
            result += part
        elif part == 'UTC':
            result += part
        else:
            return '-'
    return result


def format_scale(scale):
    """Format the scale denominator inserting the thousand separator (')

       Example:  50000  gives 1:50'000
    """
    scale_str = str(scale)
    n = ''
    while len(scale_str) > 3:
        scale_prov = int(float(scale_str)) // 1000
        n = n + "'000"
        scale_str = str(scale_prov)
    scale = "1:" + scale_str + n
    return scale


def int_with_apostrophe(x):
    if type(x) not in [type(0), type(int(0))]:
        return '-'
    if x < 0:
        return '-' + int_with_apostrophe(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = "'%03d%s" % (r, result)
    return "%d%s" % (x, result)


def get_loaderjs_url(request, version='3.6.0'):
    return make_agnostic(route_url('ga_api', request)) + '?version=' + version


def decompress_gzipped_string(streaming_body):
    return gzip.decompress(streaming_body.read()).decode()


def unnacent_where_text(where_string, model):

    # where_string is the arbitrary where text given by the query
    # model is the model corresponding to the layer for the query
    separator = None
    for possible_separator in ('+=', '=', 'ilike', 'like'):
        # Those are the only string separators that ask for custom inputs from the customer.
        if separator is None:
            # We are not looking for a valid separator if we already found one
            separator = possible_separator if where_string.find(possible_separator) > -1 else None
            if separator is not None:
                # splitting the string and trimming the substrings
                where_text_split = where_string.split(separator, 1)
                where_text_split[0] = where_text_split[0].strip()
                # TODO: we might have multiple statements here, with 'or' or 'and'
                where_text_split[1] = where_text_split[1].strip()
                if str(getattr(model, where_text_split[0]).type) == 'VARCHAR':
                    # if we get to this place, it means we have a string type of data with a custom input from the
                    # customer and we will need to unaccent them to make the search.
                    return "remove_accents({}) {} {}".format(where_text_split[0], separator, sanitize_user_input_accents(separate_statements(where_text_split[1], model)).lower())
                else:
                    # if we get here, it means we had a separator, but it's not a string (only possibility should be '='
                    # and a number. So we break out of the for loop for performances purpose
                    break

    return where_string


def separate_statements(substring, model):
    # in layerdefs, sometimes statements are separated by 'or' or 'and' clauses. this separates them. Only downside is that I'm calling sanitize input accents multiple times.
    splitted_substring = substring.split(" ", 2)
    if len(splitted_substring) == 3:
        separator = splitted_substring[1]
        if separator == 'or' or separator == 'and':
            splitted_substring[2] = unnacent_where_text(splitted_substring[2], model)
            return "{} {} {}".format(splitted_substring[0], separator, separate_statements(splitted_substring[2], model))
    return substring


def sanitize_user_input_accents(string):
    # this transforms the umlauts in latin compliant version, then remove the accents entirely
    return unidecode.unidecode(remove_accents(string))


def anonymize_string(text, length = None, replacement='*'):
    txt_length = len(text) if length is None else length
    return text.replace(text[0:], replacement * txt_length)


def get_payload(obj, trim=128):
    '''Get payload in text of a request or response object.'''
    if not obj.content_length:
        return ''
    if obj.content_type in [
        'application/json',
        'application/javascript',
        'text/javascript',
        'text/css',
        'text/plain',
        'text/html'
    ]:
        return obj.text[:trim]
    return '<not a text format>'


def strtobool(value):
    """Convert a string representation of truth to True or False.

    Replaces deprecated https://github.com/python/cpython/blob/3.10/Lib/distutils/util.py#L308
    """
    value = value.lower()
    if value in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    if value in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    raise ValueError(f"invalid truth value {value!r}")
