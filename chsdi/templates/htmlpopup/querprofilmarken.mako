<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
%>
<tr><td
class="cell-left">${_('schluesselid')}</td><td>${c['attributes']['schluesselid']}</td></tr>
<tr><td class="cell-left">${_('typ_fr_de')}</td><td>${c['attributes']['typ']}</td></tr>
<tr><td class="cell-left">${_('x')}</td><td>${round(c['attributes']['x_koordinate'],2)}</td></tr>
<tr><td class="cell-left">${_('y')}</td><td>${round(c['attributes']['y_koordinate'],2)}</td></tr>
<tr><td class="cell-left">${_('azimut')}</td><td>${c['attributes']['azimut']}</td></tr>
<tr><td class="cell-left">${_('herkunft')}</td><td>${c['attributes']['herkunft']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
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
<th class="cell-left">${_('typ_fr_de')}</th>
<td>${c['attributes']['typ'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('x')}</th>
<td>${round(c['attributes']['x_koordinate'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('y')}</th>
<td>${round(c['attributes']['y_koordinate'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('azimut')}</th>
<td>${c['attributes']['azimut'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('herkunft')}</th>
<td>${c['attributes']['herkunft'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('ch_bafu_wasserbau_vermessungsstrecken.bemerkung')}</th>
<td>${c['attributes']['bemerkung'] or '-'}</td>
</tr>
</table>
</%def>
