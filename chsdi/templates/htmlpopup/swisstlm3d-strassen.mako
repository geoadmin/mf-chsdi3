<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    objektart_label = 'ch.swisstopo.swisstlm3d-strassen_objektart_%s' % c['attributes']['objektart']
%>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.objektart')}</td>
      <td>${_(objektart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.belagsart')}</td>
      <td>${c['attributes']['belagsart_resolved'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.verkehrsbedeutung')}</td>
      <td>${c['attributes']['verkehrsbedeutung_resolved'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.eigentuemer')}</td>
      <td>${c['attributes']['eigentuemer_resolved'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.verkehrsbeschraenkung')}</td>
      <td>${c['attributes']['verkehrsbeschraenkung_resolved'] or '-'}</td>
    </tr>
</%def>

