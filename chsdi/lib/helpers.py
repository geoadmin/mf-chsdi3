# -*- coding: utf-8 -*-

from pyramid.threadlocal import get_current_registry
from pyramid.i18n import get_locale_name
import unicodedata
from urllib import quote


def versioned(path):
    version = get_current_registry().settings['app_version']
    if version is not None:
        if path.startswith('http'):
            return path.replace('wsgi', 'wsgi/' + version)
        else:
            return version + '/' + path
    else:
        return path


def locale_negotiator(request):
    lang = request.params.get('lang')
    settings = get_current_registry().settings
    languages = settings['available_languages'].split()
    if lang == 'rm':
        return 'fi'
    elif lang is None or lang not in languages:
        # the default_locale_name configuration variable
        return get_locale_name(request)
    return lang


def check_even(number):
    if number % 2 == 0:
        return True
    return False


def round(val):
    import math
    return math.floor(val + 0.5)


def remove_accents(input_str):
    # TODO find a better way to treat those characters
    input_str = input_str.replace(u'ü', u'ue')
    input_str = input_str.replace(u'Ü', u'ue')
    input_str = input_str.replace(u'ä', u'ae')
    input_str = input_str.replace(u'Ä', u'ae')
    input_str = input_str.replace(u'ö', u'oe')
    input_str = input_str.replace(u'Ö', u'oe')
    input_str = input_str.replace('/', '')
    input_str = input_str.replace('(', '')
    input_str = input_str.replace(')', '')
    input_str = input_str.replace('"', '')
    return ''.join(c for c in unicodedata.normalize('NFD', input_str) if unicodedata.category(c) != 'Mn')


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
