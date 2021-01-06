<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gwlnr'}</td>
  <td>${c['attributes']['gwlnr'] or '-'}</td>
</tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.flussname')}</td>
  <td>${c['attributes']['flussname'] or '-'}</td></tr>
<tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.abschnitt')}</td>
  <td>${c['attributes']['abschnitt'] or '-'}</td></tr>
<tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.gewiss_adr')}</td>
  <td>${c['attributes']['gewiss_adr'] or '-'}</td></tr>
<tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.bww_km')}</td>
  <td>${c['attributes']['bww_km'] or '-'}</td></tr>
<tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.lokale_km')}</td>
  <td>${c['attributes']['lokale_km'] or '-'}</td></tr>
<tr>
<tr>
  <td class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.datum')}</td>
  <td>${c['attributes']['datum'] or '-'}</td></tr>
<tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    lang = lang if lang in ('fr','it') else 'de'
%>
<table class="table-with-border kernkraftwerke-extended">
<colgroup>
  <col width=50%>
  <col width=50%>
</colgroup>
<tr>
<th class="cell-left">${_('schluesselid')}</th>
<td>${c['attributes']['schluesselid'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.typ')}</th>
<td>${c['attributes']['typ'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('x')}</th>
  % if c['attributes']['x_koordinate']:
    <td>${round(c['attributes']['x_koordinate'],2) or '-'}</td>
  % else:
    <td>-</td>
  % endif  
</tr>
<tr>
<th class="cell-left">${_('y')}</th>
  % if c['attributes']['y_koordinate']:
    <td>${round(c['attributes']['y_koordinate'],2) or '-'}</td>
  % else:
    <td>-</td>
  % endif    
</tr>
<tr>
<th class="cell-left">${_('azimut')}</th>
<td>${c['attributes']['azimut'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('ch.bafu.wasserbau-querprofilmarken.herkunft')}</th>
<td>${c['attributes']['herkunft'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('ch.bafu.wasserbau-vermessungsstrecken.bemerkung')}</th>
<td>${c['attributes']['bemerkung'] or '-'}</td>
</tr>
</table>
</%def>
