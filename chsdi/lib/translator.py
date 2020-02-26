# -*- coding: utf-8 -*-

import os
from threading import Lock
import psycopg2
import logging
from cachetools import TTLCache
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import register_type, UNICODE

CACHE_TTL = 3600  # Cache duration in seconds --> 1 hour cache for translations
CACHE_SIZE = 10000


# This is a class with a singleton approach. We do not need to have twenty caches around the code
class Translator:

    _translations = None
    _supported_languages = ['de', 'fr', 'en', 'rm', 'it']
    _lock = Lock()

    """
    Database transation methods
    """
    @staticmethod
    def get_db_connection():
        logging.debug(os.environ.get('DBHOST'))
        logging.debug(os.environ.get('DBSTAGING'))
        return psycopg2.connect(host=os.environ.get('DBHOST'),
                                dbname="bod_{}".format(os.environ.get('DBSTAGING')),
                                user='www-data')

    @staticmethod
    def select_all(cur):
        cur.execute('SELECT msg_id, de, fr, it, rm, en FROM translations ORDER BY msg_id;')
        return cur

    @classmethod
    def fill_translations(cls):
        # using the Lock from threadings to ensure non concurrent writings
        with cls._lock:
            # This little condition avoid multiple threads all trying to access the database.
            if cls._translations[cls._supported_languages[0]].currsize == 0:
                conn = cls.get_db_connection()
                register_type(UNICODE)
                conn.set_client_encoding('UTF8')
                cur = conn.cursor(cursor_factory=RealDictCursor)
                cur = cls.select_all(cur)
                for row in cur:
                    for lang in cls._supported_languages:
                        cls._translations[lang][row['msg_id']] = row[lang]
                conn.close()

    # this is a simili singleton approach.
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
            # default language is german
            lang = 'de'
        if translations[lang].currsize == 0:
            # we do not fill the cache unless it is empty
            cls.fill_translations()

        translated_value = translations[lang].get(msg_id, msg_id)
        return translated_value

    @classmethod
    def empty_cache(cls):
        with cls._lock:
            cls._translations = None
