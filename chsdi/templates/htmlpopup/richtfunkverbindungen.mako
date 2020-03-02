<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
  link_class = c['attributes']['link_class'].lower().strip()
  if link_class == 'kl1':
    hertz = '6 - 16 GHz'
  elif link_class == 'kl2':
    hertz = '17 - 29 GHz'
  elif link_class == 'kl3':
    hertz = '30 - 90 GHz'
  else:
    hertz = '-'
%>
    <tr><td class="cell-left">${Translator.translate('ch.bakom.richtfunkverbindungen.link_class', lang)}</td>           <td>${hertz}</td></tr>
</%def>

