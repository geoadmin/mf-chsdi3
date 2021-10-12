<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
  <%
    layer = c['layerBodId']
    lang = lang if lang in ('fr', 'it', 'rm', 'en') else 'de'
    hoehenstufen  = 'hoehenstufen_%s' % lang
    layer_1975 = 'ch.bafu.wald-vegetationshoehenstufen_1975'
    hs_title = '.hoehenstufen' if layer == layer_1975 else '.' + hoehenstufen
  %>

  <tr><td class="cell-left">${_(layer + hs_title)}</td> <td>${c['attributes'][hoehenstufen] or '-'}</td></tr>
</%def>
