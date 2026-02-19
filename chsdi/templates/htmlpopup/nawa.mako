<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it','en') else 'de'
  klasse = 'klasse_%s' % lang
%>

<tr><td class="cell-left">${_('gewaesserschutz_klasse')}</td> <td>${c['attributes'][klasse]}</td></tr>
<tr><td class="cell-left">${_('gewaesserschutz_gewaesser')}</td> <td>${c['attributes']['gewaesser']}</td></tr>
<tr><td class="cell-left">${_('tt_ch_bav_kataster_belasteter_standorte_oev_standortname')}</td> <td>${c['attributes']['stelle_neu']}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.yearbw')}</td> <td>${c['attributes']['jahr']}</td></tr>
<tr><td class="cell-left">${_('kanton')}</td> <td>${c['attributes']['kanton']}</td></tr>

%if c['layerBodId'].startswith('ch.bafu.gewaesserschutz-chemischer_zustand_'):
    <tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_phosphat.station_nr')}</td> <td>${c['attributes']['station_nr']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-chemischer_zustand_phosphat.id_nawa')}</td> <td>${c['attributes']['id_nawa']}</td></tr>
%endif

</%def>
