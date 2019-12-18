# -*- coding: utf-8 -*-


<%inherit file="base.mako"/>
<%namespace name="partials" file="cadastralwebmap.include.mako"/>

<%def name="table_body(c, lang)">
<%
  from gatilegrid import getTileGrid
  from chsdi.models.vector import get_scale
  from chsdi.lib.validation.identify import IdentifyServiceValidation
  from chsdi.lib.helpers import shift_to
  request = context.get('request')
  fallbackLang = 'fr' if request.lang in ('fr', 'it') else 'de'

  class CadastralWebMapParams(IdentifyServiceValidation):
      def __init__(self, request):
          self.srid = request.params.get('sr', '21781')
          grid = getTileGrid(self.srid)()
          defaultImageDisplay = '400,600,96'
          defaultExtent = ','.join(map(str, grid.extent))
          defaultTolerance = 0

          self.tolerance = request.params.get('tolerance', defaultTolerance)
          self.mapExtent = request.params.get('mapExtent', defaultExtent)
          self.imageDisplay = request.params.get('imageDisplay', defaultImageDisplay)
          self.coord = request.params.get('coord')

  params = CadastralWebMapParams(request)

  c['scale']  = get_scale(params.imageDisplay, params.mapExtent)
  if params.srid == 2056:
      c['bboxlv95'] =  list(params.mapExtent.bounds)
      c['bboxlv03'] =  shift_to(c['bboxlv95'], 21781)
      defaultCoordLv95 = [(c['bboxlv95'][0] + c['bboxlv95'][2]) / 2,
                          (c['bboxlv95'][1] + c['bboxlv95'][3]) / 2]
      c['clickCoordLv95'] = [float(a) for a in params.coord.split(',')] if params.coord else defaultCoordLv95
      c['clickCoordLv03'] = shift_to(c['clickCoordLv95'], 21781)
  else:
    c['bboxlv03'] =  list(params.mapExtent.bounds)
    c['bboxlv95'] =  shift_to(c['bboxlv03'], 2056)

    defaultCoordLv03 = [(c['bboxlv03'][0] + c['bboxlv03'][2]) / 2,
                      (c['bboxlv03'][1] + c['bboxlv03'][3]) / 2]
    c['clickCoordLv03'] = [float(a) for a in params.coord.split(',')] if params.coord else defaultCoordLv03
    c['clickCoordLv95'] = shift_to(c['clickCoordLv03'], 2056)
%>
${partials.table_body_cadastral(c, lang, fallbackLang)}
</%def>
