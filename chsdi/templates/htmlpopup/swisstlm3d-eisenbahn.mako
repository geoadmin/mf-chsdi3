<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    objektart_label = 'ch.swisstopo.swisstlm3d-eisenbahnnetz_objektart_%s' % c['attributes']['objektart']
    verkehrsmittel_label = 'ch.swisstopo.swisstlm3d-eisenbahnnetz_verkehrsmittel_%s' % c['attributes']['verkehrsmittel']
    standseilbahn_label = 'ch.swisstopo.swisstlm3d-eisenbahnnetz_standseilbahn_%s' % c['attributes']['standseilbahn']
    zahnradbahn_label = 'ch.swisstopo.swisstlm3d-eisenbahnnetz_zahnradbahn_%s' % c['attributes']['zahnradbahn']
    ausser_betrieb_label = 'ch.swisstopo.swisstlm3d-eisenbahnnetz_ausser_betrieb_%s' % c['attributes']['ausser_betrieb']
%>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-eisenbahnnetz.objektart')}</td>
      <td>${_(objektart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-eisenbahnnetz.verkehrsmittel')}</td>
      <td>${_(verkehrsmittel_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-eisenbahnnetz.standseilbahn')}</td>
      <td>${_(standseilbahn_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-eisenbahnnetz.zahnradbahn')}</td>
      <td>${_(zahnradbahn_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-eisenbahnnetz.ausser_betrieb')}</td>
      <td>${_(ausser_betrieb_label) or '-'}</td>
    </tr>
</%def>

