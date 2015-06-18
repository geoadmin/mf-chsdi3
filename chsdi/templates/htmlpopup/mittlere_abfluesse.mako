<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<tr><td
class="cell-left">${_('mqn_jahr')}</td><td>${round(c['attributes']['mqn_jahr'],2)}</td></tr>
<tr><td class="cell-left">${_('regimetyp')}</td><td>${c['attributes']['regimetyp']}</td></tr>
<tr><td class="cell-left">${_('regimenummer')}</td><td>${c['attributes']['regimenummer']}</td></tr>
<tr><td class="cell-left">${_('abflussvar')}</td><td>${c['attributes']['abflussvar']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
%>

<table class="table-with-border kernkraftwerke-extended">
<colgroup>
  <col width=60%>
  <col width=40%>
</colgroup>
<tr>
<th class="cell-left">${_('mqn_jahr')}</th>
<td>${round(c['attributes']['mqn_jahr'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_jan')}</th>
<td>${round(c['attributes']['mqn_jan'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_feb')}</th>
<td>${round(c['attributes']['mqn_feb'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_mar')}</th>
<td>${round(c['attributes']['mqn_mar'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_apr')}</th>
<td>${round(c['attributes']['mqn_apr'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_mai')}</th>
<td>${round(c['attributes']['mqn_mai'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_jun')}</th>
<td>${round(c['attributes']['mqn_jun'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_jul')}</th>
<td>${round(c['attributes']['mqn_jul'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_aug')}</th>
<td>${round(c['attributes']['mqn_aug'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_sep')}</th>
<td>${round(c['attributes']['mqn_sep'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_okt')}</th>
<td>${round(c['attributes']['mqn_okt'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_nov')}</th>
<td>${round(c['attributes']['mqn_nov'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('mqn_dez')}</th>
<td>${round(c['attributes']['mqn_dez'],2) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('regimetyp')}</th>
<td>${c['attributes']['regimetyp'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('regimenummer')}</th>
<td>${c['attributes']['regimenummer'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${_('abflussvar')}</th>
<td>${c['attributes']['abflussvar'] or '-'}</td>
</tr>
</table>
</%def>
