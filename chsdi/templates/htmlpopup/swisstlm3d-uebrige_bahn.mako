<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    objektart_label = 'ch.swisstopo.swisstlm3d-uebrigerverkehr_objektart_%s' % c['attributes']['objektart']
    ausser_betrieb_label = 'ch.swisstopo.swisstlm3d-uebrigerverkehr_ausser_betrieb_%s' % c['attributes']['ausser_betrieb']
%>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-uebrigerverkehr.objektart')}</td>
      <td>${_(objektart_label) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-uebrigerverkehr.name')}</td>
      <td>${_(c['attributes']['name']) or '-'}</td>
    </tr>
    <tr>
      <td class="cell-left">${_('ch.swisstopo.swisstlm3d-uebrigerverkehr.ausser_betrieb')}</td>
      <td>${_(ausser_betrieb_label) or '-'}</td>
    </tr>
</%def>

