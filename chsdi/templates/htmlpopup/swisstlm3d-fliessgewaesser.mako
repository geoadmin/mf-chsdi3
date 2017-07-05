<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    objektart_label = 'ch.swisstopo.swisstlm3d-gewaessernetz_objektart_%s' % c['attributes']['objektart']
%>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-gewaessernetz.objektart')}</td>
      <td>${_(objektart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-gewaessernetz.name')}</td>
      <td>${_(c['attributes']['name']) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-gewaessernetz.gwl_nr')}</td>
      <td>${_(c['attributes']['gwl_nr']) or '-'}</td>
    </tr>
</%def>

