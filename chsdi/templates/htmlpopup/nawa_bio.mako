<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it','en') else 'de'
  klasse = 'klasse_%s' % lang
%>

<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_diatomeen.klasse')}</td> <td>${c['attributes'][klasse]}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_diatomeen.gewaesser')}</td> <td>${c['attributes']['gewaesser']}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_diatomeen.stelle_neu')}</td> <td>${c['attributes']['stelle_neu']}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_diatomeen.jahr')}</td> <td>${c['attributes']['jahr']}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_diatomeen.kanton')}</td> <td>${c['attributes']['kanton']}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_diatomeen.station_nr')}</td> <td>${c['attributes']['station_nr']}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_diatomeen.id_nawa')}</td> <td>${c['attributes']['id_nawa']}</td></tr>

</%def>
