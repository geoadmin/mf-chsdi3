<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
    lang = lang if lang in ('fr','it','en') else 'de'
    stationtyp_text = 'stationtyp_%s' % lang
    standorttyp_text = 'standorttyp_%s' % lang
    eigentuemer_text = 'eigentuemer_%s' % lang
    parameter_text = 'parameter_%s' % lang
%>

  <tr>
    <td class="cell-left">${_('ch.meteoschweiz.klimaszenarien-raumklima.station')}</td><td>${c['attributes']['station'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.meteoschweiz.klimaszenarien-raumklima.stationtyp')}</td><td>${c['attributes'][stationtyp_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.meteoschweiz.klimaszenarien-raumklima.standorttyp')}</td><td>${c['attributes'][standorttyp_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.meteoschweiz.klimaszenarien-raumklima.eigentuemer')}</td><td>${c['attributes'][eigentuemer_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.meteoschweiz.klimaszenarien-raumklima.stationshoehe')}</td><td>${c['attributes']['stationhoehe'] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.meteoschweiz.klimaszenarien-raumklima.parameter')}</td><td>${c['attributes'][parameter_text] or '-'}</td>
  </tr>
  <tr>
    <td class="cell-left">${_('ch.meteoschweiz.klimaszenarien-raumklima.link')}</td><td>${c['attributes']['link'] or '-'}</td>
  </tr>
</%def>

