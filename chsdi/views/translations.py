# -*- coding: utf-8 -*-


from collections import OrderedDict
from pyramid.view import view_config

from chsdi.lib.translator import Translator


class TranslationService(object):

    def __init__(self, request):
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.cbName = request.params.get('callback')
        self.request = request
        self.lang = request.lang

    @view_config(route_name='translations', renderer='jsonp')
    def translations(self):
        translations = Translator.get_translations()
        msg_ids = OrderedDict([(msg_id, translation) for msg_id, translation in translations[self.lang].items()])

        return msg_ids
