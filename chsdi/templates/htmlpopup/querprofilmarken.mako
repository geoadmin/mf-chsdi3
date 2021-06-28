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
  % if c['attributes']['bww_km']:
  <td>${str(round(c['attributes']['bww_km'], 2))}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.lokale_km')}</td>
  % if c['attributes']['lokale_km']:
  <td>${str(round(c['attributes']['lokale_km'], 2))}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.datum')}</td>
  <td>${c['attributes']['datum'] or '-'}</td>
</tr>
</%def>



<%def name="extended_info(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
    markierung_li_text = 'markierung_li_desc_%s' % lang
    markierung_re_text = 'markierung_re_desc_%s' % lang
%>
<table class="table-with-border kernkraftwerke-extended">
<colgroup>
  <col width=50%><col width=50%>
</colgroup>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gwlnr')}</th>
  <td>${c['attributes']['gwlnr'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.flussname')}</th>
  <td>${c['attributes']['flussname'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.abschnitt')}</th>
  <td>${c['attributes']['abschnitt'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gewiss_adr')}</th>
  <td>${c['attributes']['gewiss_adr'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.bww_km')}</th>
  % if c['attributes']['bww_km']:
  <td>${str(round(c['attributes']['bww_km'], 2))}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.lokale_km')}</th>
  % if c['attributes']['lokale_km']:
  <td>${str(round(c['attributes']['lokale_km'], 2))}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.datum')}</th>
  <td>${c['attributes']['datum'] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.markierung_li')}</th>
  <td>${c['attributes'][markierung_li_text] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.e_li')}</th>
  % if c['attributes']['e_li']:
  <td>${round(c['attributes']['e_li'], 2)}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.n_li')}</th>
  % if c['attributes']['n_li']:
  <td>${round(c['attributes']['n_li'], 2)}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.hoehe_li')}</th>
  % if c['attributes']['hoehe_li']:
  <td>${round(c['attributes']['hoehe_li'], 2)}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.azimut_li')}</th>
  % if c['attributes']['azimut_li']:
  <td>${round(c['attributes']['azimut_li'], 2)}</td>
  % else:
  <td>-</td>
  % endif
  
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_1_li')}</th>
  % if c['attributes']['foto_1_li']:
    <td><a target="_blank" href="${c['attributes']['foto_1_li']}">${_('link')}</a></td>
  % else:
    <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_2_li')}</th>
  % if c['attributes']['foto_2_li']:
    <td><a target="_blank" href="${c['attributes']['foto_2_li']}">${_('link')}</a></td>
  % else:
    <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.markierung_re')}</th>
  <td>${c['attributes'][markierung_re_text] or '-'}</td>
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.e_re')}</th>
  % if c['attributes']['e_re']:
  <td>${round(c['attributes']['e_re'], 2)}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.n_re')}</th>
  % if c['attributes']['n_re']:
  <td>${round(c['attributes']['n_re'], 2)}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.hoehe_re')}</th>
  % if c['attributes']['hoehe_re']:
  <td>${round(c['attributes']['hoehe_re'], 2)}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.azimut_re')}</th>
  % if c['attributes']['azimut_re']:
  <td>${round(c['attributes']['azimut_re'], 2)}</td>
  % else:
  <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_1_re')}</th>
  % if c['attributes']['foto_1_re']:
    <td><a target="_blank" href="${c['attributes']['foto_1_re']}">${_('link')}</a></td>
  % else:
    <td>-</td>
  % endif
</tr>
<tr>
  <th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.foto_2_re')}</th>
  % if c['attributes']['foto_2_re']:
    <td><a target="_blank" href="${c['attributes']['foto_2_re']}">${_('link')}</a></td>
  % else:
    <td>-</td>
  % endif
</tr>
</table>
</%def>
