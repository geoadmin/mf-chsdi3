<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gwlnr')}</td>
  <td>${c['attributes']['gwlnr'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.flussname')}</td>
  <td>${c['attributes']['flussname'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.abschnitt')}</td>
  <td>${c['attributes']['abschnitt'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gewiss_adr')}</td>
  <td>${c['attributes']['gewiss_adr'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.bww_km')}</td>
  <td>${c['attributes']['bww_km'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.lokale_km')}</td>
  <td>${c['attributes']['lokale_km'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.datum')}</td>
  <td>${c['attributes']['datum'] or '-'}</td>
</tr>
</%def>


<%def name="extended_info(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>
<table class="table-with-border kernkraftwerke-extended">
<colgroup>
  <col width=50%><col width=50%>
</colgroup>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gwlnr')}</td>
  <td>${c['attributes']['gwlnr'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.flussname')}</td>
  <td>${c['attributes']['flussname'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.abschnitt')}</td>
  <td>${c['attributes']['abschnitt'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gewiss_adr')}</td>
  <td>${c['attributes']['gewiss_adr'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.bww_km')}</td>
  <td>${c['attributes']['bww_km'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.lokale_km')}</td>
  <td>${c['attributes']['lokale_km'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.datum')}</td>
  <td>${c['attributes']['datum'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.markierung_li')}</td>
  <td>${c['attributes']['markierung_li'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.e_li')}</td>
  <td>${c['attributes']['e_li'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.n_li')}</td>
  <td>${c['attributes']['n_li'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.hoehe_li')}</td>
  <td>${c['attributes']['hoehe_li'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.azimut_li')}</td>
  <td>${c['attributes']['azimut_li'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_1_li')}</td>
  <td>${c['attributes']['foto_1_li'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_2_li')}</td>
  <td>${c['attributes']['foto_2_li'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.markierung_re')}</td>
  <td>${c['attributes']['markierung_re'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.e_re')}</td>
  <td>${c['attributes']['e_re'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.n_re')}</td>
  <td>${c['attributes']['n_re'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.hoehe_re')}</td>
  <td>${c['attributes']['hoehe_re'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.azimut_re')}</td>
  <td>${c['attributes']['azimut_re'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_1_re')}</td>
  <td>${c['attributes']['foto_1_re'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_2_re')}</td>
  <td>${c['attributes']['foto_2_re'] or '-'}</td>
</tr>
</table>
</%def>
