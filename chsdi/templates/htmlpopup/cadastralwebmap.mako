# -*- coding: utf-8 -*-


<%inherit file="base.mako"/>
<%namespace name="partials" file="cadastralwebmap.include.mako"/>

<%def name="table_body(c, lang)">
<%
  from chsdi.models.vector import getScale
  from chsdi.lib.validation.identify import IdentifyServiceValidation
  request = context.get('request')
  defaultExtent = '42000,30000,350000,900000'
  defaultImageDisplay = '400,600,96'
  fallbackLang = 'fr' if request.lang in ('fr', 'it') else 'de'
  class CadastralWebMapParams(IdentifyServiceValidation):
      def __init__(self, request):
          self.mapExtent = request.params.get('mapExtent', defaultExtent)
          self.imageDisplay = request.params.get('imageDisplay', defaultImageDisplay)
  params = CadastralWebMapParams(request)
  c['bbox'] = params.mapExtent.bounds
  c['bboxlv95'] = [2000000 + c['bbox'][0], 1000000 + c['bbox'][1], 2000000 + c['bbox'][2], 1000000 + c['bbox'][3]]
  c['scale']  = getScale(params.imageDisplay, params.mapExtent)
  defaultCoord = [(c['bbox'][0]+c['bbox'][2])/2, (c['bbox'][1]+c['bbox'][3])/2]
  clickCoord = request.params.get('coord').split(',') if request.params.get('coord') else defaultCoord
%>
${partials.table_body_cadastral(c, lang, fallbackLang, clickCoord)}
</%def>
