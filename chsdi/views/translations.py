# -*- coding: utf-8 -*-


from collections import OrderedDict
from pyramid.view import view_config

from chsdi.models.bod import Translations


class TranslationService(object):

    def __init__(self, request):
        self.geodataStaging = request.registry.settings['geodata_staging']
        self.cbName = request.params.get('callback')
        self.request = request
        self.lang = request.lang

    @view_config(route_name='translations', renderer='jsonp')
    def translations(self):
        model = Translations
        lang = self.lang
        query = self.request.db.query(model).order_by(model.msgId)
        msgIds = OrderedDict([(q.msgId, getattr(q, lang)) for q in query])

        return msgIds
