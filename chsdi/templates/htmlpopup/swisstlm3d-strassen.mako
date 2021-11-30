<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    objektart_label = 'ch.swisstopo.swisstlm3d-strassen_objektart_%s' % c['attributes']['objektart']
    belagsart_label = 'ch.swisstopo.swisstlm3d-strassen_belagsart_%s' % c['attributes']['belagsart']
    verkehrsbedeutung_label = 'ch.swisstopo.swisstlm3d-strassen_verkehrsbedeutung_%s' % c['attributes']['verkehrsbedeutung']
    eigentuemer_label = 'ch.swisstopo.swisstlm3d-strassen_eigentuemer_%s' % c['attributes']['eigentuemer']
    verkehrsbeschraenkung_label = 'ch.swisstopo.swisstlm3d-strassen_verkehrsbeschraenkung_%s' % c['attributes']['verkehrsbeschraenkung']
%>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.strassenname')}</td>
      <td>c['attributes']['strassenname'] or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.objektart')}</td>
      <td>${_(objektart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.belagsart')}</td>
      <td>${_(belagsart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.verkehrsbedeutung')}</td>
      <td>${_(verkehrsbedeutung_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.eigentuemer')}</td>
      <td>${_(eigentuemer_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-strassen.verkehrsbeschraenkung')}</td>
      <td>${_(verkehrsbeschraenkung_label) or '-'}</td>
    </tr>
</%def>

