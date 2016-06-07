<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<tr><td class="cell-left">${_('gewaesserschutz_klasse')}</td> <td>${c['attributes']['klasse']}</td></tr>
<tr><td class="cell-left">${_('gewaesserschutz_gewaesser')}</td> <td>${c['attributes']['gewaesser']}</td></tr>
<tr><td class="cell-left">${_('tt_ch_bav_kataster_belasteter_standorte_oev_standortname')}</td> <td>${c['attributes']['stelle_neu']}</td></tr>
<tr><td class="cell-left">${_('ch.bafu.gewaesserschutz-badewasserqualitaet.yearbw')}</td> <td>${c['attributes']['jahr']}</td></tr>
<tr><td class="cell-left">${_('kanton')}</td> <td>${c['attributes']['kanton']}</td></tr>

</%def>
