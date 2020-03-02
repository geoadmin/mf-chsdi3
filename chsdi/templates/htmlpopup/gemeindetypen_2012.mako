<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr><td class="cell-left">${t.Translator.translate('tt_gemeindetypen_TYP_CODE', lang)}</td>    <td>${c['attributes']['typ_code'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.Translator.translate('tt_gemeindetypen_TYP_BEZ_D', lang)}</td>
    % if lang in ('de', 'rm', 'en'):
      <td>${c['attributes']['typ_bez_d'] or '-'}</td>
    % else:
      <td>${c['attributes']['typ_bez_f'] or '-'}</td>
    % endif
  </tr>
	<tr><td class="cell-left">${t.Translator.translate('tt_bauzonen_gemeindetypen_BFS_NO', lang)}</td>    <td>${c['attributes']['bfs_no'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.Translator.translate('tt_bauzonen_gemeindetypen_NAME', lang)}</td>    <td>${c['attributes']['name_']}</td></tr>
  <tr><td class="cell-left">${t.Translator.translate('tt_bauzonen_gemeindetypen_KT_NO', lang)}</td>    <td>${c['attributes']['kt_no'] or '-'}</td></tr>
	<tr><td class="cell-left">${t.Translator.translate('tt_bauzonen_gemeindetypen_KT_KZ', lang)}</td>    <td>${c['attributes']['kt_kz'] or '-'}</td></tr>
  <tr><td class="cell-left">${t.Translator.translate('tt_gemeindetypen_FLAECHE_HA', lang)}</td>    <td>${int(round(c['attributes']['flaeche_ha'])) or '-'}</td></tr>
</%def>
