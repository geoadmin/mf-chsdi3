# -*- coding: utf-8 -*-

import re
import math
import requests
import datetime
import gzip
import six
import unidecode
from decimal import Decimal
from past.utils import old_div

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO, BytesIO

from six.moves import zip, reduce, zip_longest
from itertools import chain

from functools import partial
from pyramid.threadlocal import get_current_registry
from pyramid.i18n import get_locale_name
from pyramid.url import route_url
from pyramid.httpexceptions import HTTPBadRequest, HTTPRequestTimeout
import unicodedata
try:
    from urlparse import urlparse, urlunparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urlunparse, urljoin

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

import xml.etree.ElementTree as etree
from pyproj import Proj, transform as proj_transform
from requests.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from shapely.ops import transform as shape_transform
from shapely.wkt import dumps as shape_dumps, loads as shape_loads
from shapely.geometry.base import BaseGeometry
from chsdi.lib.parser import WhereParser
from chsdi.lib.exceptions import QueryParseException, CoordinatesTransformationException
import logging

if six.PY3:
    unicode = str
    long = int

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

log = logging.getLogger(__name__)


PROJECTIONS = {}

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


def versioned(path):
    version = get_current_registry().settings['app_version']
    entry_path = get_current_registry().settings['entry_path'] + '/'
    if version is not None:
        agnosticPath = make_agnostic(path)
        parsedURL = urlparse(agnosticPath)
        # we don't do version when behind pserve (at localhost)
        if 'localhost:' not in parsedURL.netloc:
            parts = parsedURL.path.split(entry_path, 1)
            if len(parts) > 1:
                parsedURL = parsedURL._replace(
                    path=parts[0] + entry_path + version + '/' + parts[1])
                agnosticPath = urlunparse(parsedURL)
        return agnosticPath
    else:
        return path


def make_agnostic(path):
    handle_path = lambda x: x.split('://')[1] if len(x.split('://')) == 2 else path
    if path.startswith('http'):
        path = handle_path(path)
        return '//' + path
    else:
        return path


def make_api_url(request, agnostic=False):
    base_path = request.registry.settings['apache_base_path']
    base_path = '' if base_path == 'main' else '/' + base_path
    host = request.host + base_path if 'localhost' not in request.host else request.host
    if agnostic:
        return ''.join(('//', host))
    return ''.join((request.scheme, '://', host))


def make_geoadmin_url(request, agnostic=False):
    protocol = request.scheme
    base_url = ''.join((protocol, '://', request.registry.settings['geoadminhost']))
    if agnostic:
        return make_agnostic(base_url)
    return base_url


def resource_exists(path, headers={'User-Agent': 'mf-geoadmin/python'}, verify=False):
    try:
        r = requests.head(path, headers=headers, verify=verify)
    except ConnectionError:
        return False
    return r.status_code == requests.codes.ok


def check_url(url, config):
    if url is None:
        raise HTTPBadRequest('The parameter url is missing from the request')
    parsedUrl = urlparse(url)
    hostname = parsedUrl.hostname
    if hostname is None:
        raise HTTPBadRequest('Could not determine the hostname')
    domain = ".".join(hostname.split(".")[-2:])
    allowed_hosts = config['shortener.allowed_hosts'] if 'shortener.allowed_hosts' in config else ''
    allowed_domains = config['shortener.allowed_domains'] if 'shortener.allowed_domains' in config else ''
    if domain not in allowed_domains and hostname not in allowed_hosts:
        raise HTTPBadRequest('Shortener can only be used for %s domains or %s hosts.' % (allowed_domains, allowed_hosts))
    return url


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


def format_search_text(input_str):
    return remove_accents(
        escape_sphinx_syntax(input_str)
    )


def format_locations_search_text(input_str):
    if input_str is None:
        return input_str
    # only remove trailing and leading dots
    input_str = ' '.join([w.strip('.') for w in input_str.split()])
    # remove double quotation marks
    input_str = input_str.replace('"', '')
    return format_search_text(input_str)


def remove_accents(input_str):
    if input_str is None:
        return input_str
    input_str = input_str.replace(u'ü', u'ue')
    input_str = input_str.replace(u'Ü', u'ue')
    input_str = input_str.replace(u'ä', u'ae')
    input_str = input_str.replace(u'Ä', u'ae')
    input_str = input_str.replace(u'ö', u'oe')
    input_str = input_str.replace(u'Ö', u'oe')
    return ''.join(c for c in unicodedata.normalize('NFD', input_str) if unicodedata.category(c) != 'Mn')


def escape_sphinx_syntax(input_str):
    if input_str is None:
        return input_str
    input_str = input_str.replace('|', '\\|')
    input_str = input_str.replace('!', '\\!')
    input_str = input_str.replace('@', '\\@')
    input_str = input_str.replace('&', '\\&')
    input_str = input_str.replace('~', '\\~')
    input_str = input_str.replace('^', '\\^')
    input_str = input_str.replace('=', '\\=')
    input_str = input_str.replace('/', '\\/')
    input_str = input_str.replace('(', '\\(')
    input_str = input_str.replace(')', '\\)')
    input_str = input_str.replace(']', '\\]')
    input_str = input_str.replace('[', '\\[')
    input_str = input_str.replace('*', '\\*')
    input_str = input_str.replace('<', '\\<')
    input_str = input_str.replace('$', '\\$')
    input_str = input_str.replace('"', '\"')
    return input_str


def format_query(model, value, lang):
    '''
        Supported operators on numerical or date values are "=, !=, >=, <=, > and <"
        Supported operators for text are "ilike and not ilike"
    '''
    where = None

    def escapeSQL(value):
        if u'ilike' in value:
            match = re.search(r'([\w]+\s)(ilike|not ilike)(\s\'%)([\s\S]*)(%\')', value)
            where = u''.join((
                match.group(1).replace(u'\'', u'E\''),
                match.group(2),
                match.group(3),
                match.group(4).replace(u'\\', u'\\\\')
                              .replace(u'\'', u"\''")
                              .replace(u'_', u'\\_'),
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

            val = val.replace(prop, unicode(column.name))
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

        return unicode(" ".join(full))

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
    if response.status_code == requests.codes.ok:
        xml = etree.fromstring(response.content)
        bb = xml.find('BoundingBox')
        if bb is not None:
            width = abs(int(float(bb.get('maxy'))) - int(float(bb.get('miny'))))
            height = abs(int(float(bb.get('maxx'))) - int(float(bb.get('minx'))))
    return (width, height)


def get_proj_from_srid(srid):
    if srid in PROJECTIONS:
        return PROJECTIONS[srid]
    else:
        proj = Proj(init='EPSG:{}'.format(srid))
        PROJECTIONS[srid] = proj
        return proj


def get_precision_for_proj(srid):
    precision = COORDINATES_DECIMALS_FOR_METRIC_PROJ
    proj = get_proj_from_srid(srid)
    if proj.is_latlong():
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
    proj_in = get_proj_from_srid(srid_from)
    proj_out = get_proj_from_srid(srid_to)
    return proj_transform(proj_in, proj_out, coords[0], coords[1])


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
    proj_in = get_proj_from_srid(srid_from)
    proj_out = get_proj_from_srid(srid_to)

    projection_func = partial(proj_transform, proj_in, proj_out)

    new_geom = shape_transform(projection_func, geom)
    if rounding:
        precision = get_precision_for_proj(srid_to)
        return _round_shape_coordinates(new_geom, precision=precision)
    return new_geom

# float('NaN') does not raise an Exception. This function does.


def float_raise_nan(val):
    ret = float(val)
    if math.isnan(ret):
        raise ValueError('nan is not considered valid float')
    return ret


def parse_box2d(stringBox2D):
    extent = stringBox2D.replace('BOX(', '').replace(')', '').replace(',', ' ')
    # Python2/3
    box = map(float, extent.split(' '))
    if not isinstance(box, list):
        box = list(box)
    return box


def is_box2d(box2D):
    # Python2/3
    if not isinstance(box2D, list):
        box2D = list(box2D)
    # Bottom left to top right only
    if len(box2D) != 4 or box2D[0] > box2D[2] or box2D[1] > box2D[3]:
        raise ValueError('Invalid box2D.')
    return box2D


def center_from_box2d(box2D):
    box2D = is_box2d(box2D)
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
        # Python2/3
        scale_prov = old_div(int(float(scale_str)), 1000)
        n = n + "'000"
        scale_str = str(scale_prov)
    scale = "1:" + scale_str + n
    return scale


def int_with_apostrophe(x):
    if type(x) not in [type(0), type(long(0))]:
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


def gzip_string(string):
    # Python2/3
    if six.PY2:
        infile = StringIO()
        data = string
    else:
        infile = BytesIO()
        try:
            data = string.encode('utf8')
        except (UnicodeDecodeError, AttributeError):
            data = string
    try:
        gzip_file = gzip.GzipFile(fileobj=infile, mode='w', compresslevel=5)
        gzip_file.write(data)
        gzip_file.close()
        infile.seek(0)
        out = infile.getvalue()
    except Exception as e:
        log.error("Cannot gzip string: {}".format(e))
        out = None
    finally:
        infile.close()
    return out


def decompress_gzipped_string(streaming_body):
    if six.PY2:
        string_file = StringIO(streaming_body.read())
        gzip_file = gzip.GzipFile(fileobj=string_file, mode='r', compresslevel=5)
        return gzip_file.read().decode('utf-8')
    else:
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
                    return "unaccent({}) {} {}".format(where_text_split[0], separator, sanitize_user_input_accents(separate_statements(where_text_split[1], model)))
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
