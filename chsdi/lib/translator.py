# -*- coding: utf-8 -*-

import os
import psycopg2
from cachetools import TTLCache
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import register_type, UNICODE

CACHE_TTL = 3600  # Cache duration in seconds --> 1 hour cache for translations
CACHE_SIZE = 10000


class Translator:

    _translations = None
    _supported_languages = ['en', 'fr', 'de', 'rm', 'it']

    @staticmethod
    def get_db_connection():
        return psycopg2.connect(host=os.environ.get('DBHOST'), dbname='bod_master', user='www-data')

    @staticmethod
    def select_all(cur):
        cur.execute('SELECT msg_id, de, fr, it, rm, en FROM translations ORDER BY msg_id;')
        return cur

    @classmethod
    def get_translations(cls):
        if cls._translations is None:
            cls._translations = dict()
            for lang in cls._supported_languages:
                cls._translations.setdefault(lang, TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TTL))
        return cls._translations

    @classmethod
    def translate(cls, msg_id, lang):
        translations = cls.get_translations()
        if lang not in cls._supported_languages:
            lang = 'de'
        if translations[lang].currsize == 0:
            cls.fill_translations()
        translated_value = translations[lang].get(msg_id, msg_id)
        return translated_value

    @classmethod
    def fill_translations(cls):
        conn = cls.get_db_connection()
        register_type(UNICODE)
        conn.set_client_encoding('UTF8')
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur = cls.select_all(cur)
        for row in cur:
            for lang in cls._supported_languages:

                cls._translations[lang][row['msg_id']] = row[lang]
        conn.close()

    @classmethod
    def empty_cache(cls):
        for lang in cls._supported_languages:
            cls._translations[lang] = TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TTL)
