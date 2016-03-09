# -*- coding: utf-8 -*-

import re
import math
import requests
import datetime
from osgeo import osr, ogr
from pyramid.threadlocal import get_current_registry
from pyramid.i18n import get_locale_name
from pyramid.httpexceptions import HTTPBadRequest, HTTPRequestTimeout
import unicodedata
from urllib import quote
from urlparse import urlparse, urlunparse, urljoin
import xml.etree.ElementTree as etree


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
    else:
        return ''.join((request.scheme, '://', host))


def resource_exists(path, headers={}):
    r = requests.head(path, headers=headers)
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
    except:
        pass
    return sanitized


def locale_negotiator(request):
    try:
        lang = request.params.get('lang')
    except UnicodeDecodeError:
        raise HTTPBadRequest('Could not parse URL and parameters. Request send must be encoded in utf-8.')
    # This might happen if a POST request is aborted before all the data could be transmitted
    except IOError:
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


def format_query(model, value):
    '''
        Supported operators on numerical or date values are "=, !=, >=, <=, > and <"
        Supported operators for text are "ilike and not ilike"
    '''
    def escapeSQL(value):
        if u'ilike' in value:
            match = re.search(r'([\w]+\s)(ilike|not ilike)(\s\'%)(.*)(%\')', value)
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

    def replacePropByColumnName(model, values):
        res = []
        for val in values:
            prop = val.split(' ')[0]
            columnName = model.get_column_by_property_name(prop).name.__str__()
            val = val.replace(prop, columnName)
            res.append(val)
        return res

    def extractMatches(x):
        for v in x:
            if v != '':
                return v
        return v

    def getOperator(values):
        supportedOperators = [' and ', ' or ']
        if len(values) > 1:
            t = value.split(values[0])
            operator = extractMatches(t[1].split(values[1]))
            if operator not in supportedOperators:
                raise HTTPBadRequest()
            return operator
        return ''

    regEx = r'(\w+\s(?:ilike|not ilike)\s(?:\'%)[^\%]+(?:%\'))|(\w+\s(?:=|\!=|>=|<=|>|<)\s[^\s]+)|(\w+\s(?:is null|is not null))'

    try:
        values = map(extractMatches, re.findall(regEx, value))
        if len(values) == 0:
            return None
        operator = getOperator(values)
        values = map(escapeSQL, values)
        values = replacePropByColumnName(model, values)
        where = operator.join(values)
    except:
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
    headers = {'Referer': 'http://admin.ch'}
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


def transformCoordinate(wkt, srid_from, srid_to):
    srid_in = osr.SpatialReference()
    srid_in.ImportFromEPSG(srid_from)
    srid_out = osr.SpatialReference()
    srid_out.ImportFromEPSG(srid_to)
    geom = ogr.CreateGeometryFromWkt(wkt)
    geom.AssignSpatialReference(srid_in)
    geom.TransformTo(srid_out)
    return geom


# float('NaN') does not raise an Exception. This function does.
def float_raise_nan(val):
    ret = float(val)
    if math.isnan(ret):
        raise ValueError('nan is not considered valid float')
    return ret


def parse_box2d(stringBox2D):
    extent = stringBox2D.replace('BOX(', '').replace(')', '').replace(',', ' ')
    return map(float, extent.split(' '))


def is_box2d(box2D):
    # Bottom left to top right only
    if box2D[0] > box2D[2] or box2D[1] > box2D[3] or len(box2D) != 4:
        raise ValueError('Invalid box2D.')
    return True


def extend_box2d(box2D, distance):
    if is_box2d(box2D):
        return [
            box2D[0] - distance,
            box2D[1] - distance,
            box2D[2] + distance,
            box2D[3] + distance
        ]


def center_from_box2d(box2D):
    if is_box2d(box2D):
        return [
            box2D[0] + ((box2D[2] - box2D[0]) / 2),
            box2D[1] + ((box2D[3] - box2D[1]) / 2)
        ]


def parse_date_string(dateStr, format_input='%Y-%m-%d', format_output='%d.%m.%Y'):
    try:
        return datetime.datetime.strptime(
            dateStr.strip(), format_input
        ).strftime(format_output)
    except:
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
    scale_str = str(scale)
    n = ''
    while len(scale_str) > 3:
        scale_prov = int(scale_str) / 1000
        n = n + "'000"
        scale_str = str(scale_prov)
    scale = "1:" + scale_str + n
    return scale


def format_price(price):
    price_float = price / 100.0
    price_2dec = format(price_float, '.2f')
    price = "CHF " + str(price_2dec)
    return price


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


def filter_alt(alt):
    if alt is not None and alt > 0.0:
        # 10cm accuracy is enough for altitudes
        return round(alt, 1)
