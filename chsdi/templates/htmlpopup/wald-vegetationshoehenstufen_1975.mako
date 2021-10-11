<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
  layer = c['layerBodId']
  lang = lang if lang in ('fr', 'it', 'rm', 'en') else 'de'
  hoehenstufen  = '.hoehenstufen_%s' % lang
%>
    <% c['stable_id'] = True %>
  <tr><td class="cell-left">${_(layer + hoehenstufen}</td> <td>${c['attributes'][hoehenstuffen] or '-'}</td></tr>
