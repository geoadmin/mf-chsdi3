<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">

<%
    lang = lang if lang in ('fr', 'it','en') else 'de'
    bezeichnung = 'bezeichnung_%s' % lang
    if not c['attributes']['heatpotential'] == None:
      heatpotential = "{:,.2f}".format(c['attributes']['heatpotential']).replace(',','\'')
    else:
      heatpotential = '-'

%>

    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-angebot.name')}</td>                         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-angebot.heatpotential')}</td>                <td>${heatpotential}</td></tr>
    <tr><td class="cell-left">${_('ch.bfe.fernwaerme-angebot.heat_supplier_category')}</td>       <td>${c['attributes'][bezeichnung] or '-'}</td></tr>
</%def>

