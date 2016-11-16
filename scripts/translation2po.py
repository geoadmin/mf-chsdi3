# -*- coding: utf-8 -*-

import os
import sys
import codecs
import yaml
import psycopg2
from collections import OrderedDict
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import register_type, UNICODE


def validate_params(argv):
    if len(argv) > 2:
        print('Too many arguments, aborting...')
        sys.exit(1)
    if len(argv) == 1:
        print('Please provide a translation target folder...')
        sys.exit(1)
    yaml_file_path = argv[1]
    if not os.path.exists(yaml_file_path):
        print('%s file doesn\'t exists' % yaml_file_path)
        print('Aborting...')
        sys.exit(1)

    return yaml_file_path


def get_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as f:
        yml = f.read()

    return yaml.load(yml)


def get_db_connection():
    return psycopg2.connect(host=os.environ.get('DBHOST'), dbname='bod_master', user='www-data')


def select_all(cur):
    cur.execute('SELECT msg_id, de, fr, it, rm, en FROM translations ORDER BY msg_id;')
    return cur


def get_translations(cur, langs):
    translations = {}
    for row in cur:
        for lang in langs:
            translations.setdefault(lang, OrderedDict())
            translations[lang][row['msg_id']] = row[lang]
    return translations


def create_yaml_header(lang):
    # writing header
    myString = "# " + lang + " translations for chsdi.\n"
    myString += "# Copyright (C) 2010 ORGANIZATION\n"
    myString += "# This file is distributed under the same license as the chsdi project.\n"
    myString += "# FIRST AUTHOR <EMAIL@ADDRESS>, 2010.\n"
    myString += "#\n"
    myString += "msgid \"\"\n"
    myString += "msgstr \"\"\n"
    myString += "\"Project-Id-Version: chsdi 0.1\\n\"\n"
    myString += "\"Report-Msgid-Bugs-To: EMAIL@ADDRESS\\n\"\n"
    myString += "\"POT-Creation-Date: 2010-08-03 12:20+0200\\n\"\n"
    myString += "\"PO-Revision-Date: 2010-09-02 10:50+0200\\n\"\n"
    myString += "\"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n\"\n"
    myString += "\"Language-Team: "+ lang +" <LL@li.org>\\n\"\n"
    myString += "\"Plural-Forms: nplurals=2; plural=(n != 1)\\n\"\n"
    myString += "\"MIME-Version: 1.0\\n\"\n"
    myString += "\"Content-Type: text/plain; charset=utf-8\\n\"\n"
    myString += "\"Content-Transfer-Encoding: 8bit\\n\"\n"
    myString += "\"Generated-By: Babel 0.9.5\\n\"\n\n"
    return myString


def rm_lang(lang):
    if lang == 'rm':
        return 'fi'
    return lang


def sanatize(txt):
    txt = txt.replace('\\', '').replace('"', '\\"')
    return txt.strip()


def write_po_file(lang, translations, f):
    f.write(create_yaml_header(lang))
    for msg_id, val in translations[lang].iteritems():
        f.write("msgid \"" + sanatize(msg_id) + "\"\n")
        if val:
            f.write("msgstr \"" + sanatize(val) + "\"\n\n")
        else:
            f.write("msgstr \"" + sanatize(msg_id) + "\"\n\n")


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    langs = ['de', 'fr', 'it', 'rm', 'en']
    yaml_file_path = validate_params(sys.argv)
    conn = get_db_connection()
    register_type(UNICODE)
    conn.set_client_encoding('UTF8')
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur = select_all(cur)
    translations = get_translations(cur, langs)

    for lang in langs:
        with codecs.open(os.path.join(yaml_file_path, rm_lang(lang), 'LC_MESSAGES/chsdi.po'), 'w', 'utf-8') as f:
            write_po_file(lang, translations, f)
    print('Translations done')


if __name__ == '__main__':
    main()
