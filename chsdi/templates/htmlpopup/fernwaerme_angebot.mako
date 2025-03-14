<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <%
    if not c['attributes']['heatpotential'] == None:
      heatpotential = "{:,}".format(int(c['attributes']['heatpotential'])).replace(',','\'')
    else:
      heatpotential = '-'
  %>
  <tr>
    <td class="cell-left">${_('ch.bfe.fernwaerme-angebot.name')}</td>
    <td>${c['attributes']['name'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.bfe.fernwaerme-angebot.heatpotential')}</td>
    <td>${heatpotential}</td>
  </tr>
</%def>
