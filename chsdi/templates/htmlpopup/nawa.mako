<%inherit file="base.mako"/>
<%def name="table_body(c, lang)">

<%
  lang = lang if lang in ('fr','it','en') else 'de'
  klasse = 'klasse_%s' % lang
%>

<tr><td class="cell-left">${t.Translator.translate('gewaesserschutz_klasse', lang)}</td> <td>${c['attributes'][klasse]}</td></tr>
<tr><td class="cell-left">${t.Translator.translate('gewaesserschutz_gewaesser', lang)}</td> <td>${c['attributes']['gewaesser']}</td></tr>
<tr><td class="cell-left">${t.Translator.translate('tt_ch_bav_kataster_belasteter_standorte_oev_standortname', lang)}</td> <td>${c['attributes']['stelle_neu']}</td></tr>
<tr><td class="cell-left">${t.Translator.translate('ch.bafu.gewaesserschutz-badewasserqualitaet.yearbw', lang)}</td> <td>${c['attributes']['jahr']}</td></tr>
<tr><td class="cell-left">${t.Translator.translate('kanton', lang)}</td> <td>${c['attributes']['kanton']}</td></tr>

</%def>
