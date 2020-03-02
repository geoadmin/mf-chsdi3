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
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-strassen.objektart', lang)}</td>
      <td>${_(objektart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-strassen.belagsart', lang)}</td>
      <td>${_(belagsart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-strassen.verkehrsbedeutung', lang)}</td>
      <td>${_(verkehrsbedeutung_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-strassen.eigentuemer', lang)}</td>
      <td>${_(eigentuemer_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${t.translate('ch.swisstopo.swisstlm3d-strassen.verkehrsbeschraenkung', lang)}</td>
      <td>${_(verkehrsbeschraenkung_label) or '-'}</td>
    </tr>
</%def>

