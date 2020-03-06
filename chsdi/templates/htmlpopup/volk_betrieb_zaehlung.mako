<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
layerBodId = c['layerBodId']
amount = c['attributes']['number'] or '-'

# handling bfs exceptions: "all good things must come to an end"
if amount <= 3:
  if layerBodId in ['ch.bfs.volkszaehlung-bevoelkerungsstatistik_einwohner',
                    'ch.bfs.betriebszaehlungen-arbeitsstaetten']:
    amount = '1-3'
  elif layerBodId == 'ch.bfs.betriebszaehlungen-beschaeftigte_vollzeitaequivalente':
    amount = '0.1-3'
%>
<% c['stable_id'] = False %>
  <tr><td class="cell-left">${h.translate('%s.year' % layerBodId, lang)}</td>           <td>${c['attributes']['i_year'] or '-'}</td></tr>
  <tr><td class="cell-left">${h.translate('%s.amount' % layerBodId, lang)}</td>         <td>${amount}</td></tr>
</%def>
