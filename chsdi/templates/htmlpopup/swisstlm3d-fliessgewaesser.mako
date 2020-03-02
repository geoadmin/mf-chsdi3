<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    objektart_label = 'ch.swisstopo.swisstlm3d-gewaessernetz_objektart_%s' % c['attributes']['objektart']
%>
    <tr>
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-gewaessernetz.objektart', lang)}</td>
      <td>${_(objektart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-gewaessernetz.name', lang)}</td>
      <td>${_(c['attributes']['name']) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-gewaessernetz.gwl_nr', lang)}</td>
      <td>${_(c['attributes']['gwl_nr']) or '-'}</td>
    </tr>
</%def>

