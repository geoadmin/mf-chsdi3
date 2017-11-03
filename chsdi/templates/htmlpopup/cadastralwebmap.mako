# -*- coding: utf-8 -*-


<%inherit file="base.mako"/>
<%namespace name="partials" file="cadastralwebmap.include.mako"/>

<%def name="table_body(c, lang)">
<%
  from gatilegrid import getTileGrid
  from chsdi.models.vector import get_scale
  from chsdi.lib.validation.identify import IdentifyServiceValidation
  request = context.get('request')
  grid = getTileGrid(2056)()
  defaultExtent = ','.join(map(str, grid.extent))
  defaultImageDisplay = '400,600,96'
  fallbackLang = 'fr' if request.lang in ('fr', 'it') else 'de'

  class CadastralWebMapParams(IdentifyServiceValidation):
      def __init__(self, request):
          self.mapExtent = request.params.get('mapExtent', defaultExtent)
          self.imageDisplay = request.params.get('imageDisplay', defaultImageDisplay)
  params = CadastralWebMapParams(request)

  c['bbox'] = params.mapExtent.bounds
  c['bboxlv03'] = [c['bbox'][0] - 2000000, c['bbox'][1] - 1000000,
                   c['bbox'][2] - 2000000, c['bbox'][3] - 1000000]
  c['scale']  = get_scale(params.imageDisplay, params.mapExtent)
  defaultCoord = [(c['bbox'][0] + c['bbox'][2]) / 2,
                  (c['bbox'][1] + c['bbox'][3]) / 2]
  clickCoord = request.params.get('coord').split(',') if request.params.get('coord') else defaultCoord
  c['clickCoordLv03'] = [clickCoord[0][1:],
                         clickCoord[1][1:]]
%>
${partials.table_body_cadastral(c, lang, fallbackLang, clickCoord)}
</%def>
