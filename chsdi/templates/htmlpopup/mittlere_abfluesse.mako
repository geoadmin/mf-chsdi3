<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<tr><td
class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_jahr', lang)}</td>
  % if c['attributes']['mqn_jahr'] != None:
       <td>${round(c['attributes']['mqn_jahr'],2)}</td></tr>
  % else:
       <td>-</td></tr>
  % endif 
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.regimetyp', lang)}</td><td>${c['attributes']['regimetyp'] or '-'}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.regimenummer', lang)}</td><td>${c['attributes']['regimenummer'] or '-'}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.abflussvar', lang)}</td><td>${c['attributes']['abflussvar'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<% c['stable_id'] = True %>
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
%>

<table class="table-with-border kernkraftwerke-extended">
<colgroup>
  <col width=60%>
  <col width=40%>
</colgroup>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_jahr', lang)}</th>
  % if c['attributes']['mqn_jahr'] != None:
<td>${round(c['attributes']['mqn_jahr'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_jan', lang)}</th>
  % if c['attributes']['mqn_jan'] != None:
<td>${round(c['attributes']['mqn_jan'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_feb', lang)}</th>
  % if c['attributes']['mqn_feb'] != None:
<td>${round(c['attributes']['mqn_feb'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_mar', lang)}</th>
  % if c['attributes']['mqn_mar'] != None:
<td>${round(c['attributes']['mqn_mar'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_apr', lang)}</th>
  % if c['attributes']['mqn_apr'] != None:
<td>${round(c['attributes']['mqn_apr'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_mai', lang)}</th>
  % if c['attributes']['mqn_mai'] != None:
<td>${round(c['attributes']['mqn_mai'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_jun', lang)}</th>
  % if c['attributes']['mqn_jun'] != None:
<td>${round(c['attributes']['mqn_jun'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_jul', lang)}</th>
  % if c['attributes']['mqn_jul'] != None:
<td>${round(c['attributes']['mqn_jul'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_aug', lang)}</th>
  % if c['attributes']['mqn_aug'] != None:
<td>${round(c['attributes']['mqn_aug'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_sep', lang)}</th>
  % if c['attributes']['mqn_sep'] != None:
<td>${round(c['attributes']['mqn_sep'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_okt', lang)}</th>
  % if c['attributes']['mqn_okt'] != None:
<td>${round(c['attributes']['mqn_okt'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_nov', lang)}</th>
  % if c['attributes']['mqn_nov'] != None:
<td>${round(c['attributes']['mqn_nov'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.mqn_dez', lang)}</th>
  % if c['attributes']['mqn_dez'] != None:
<td>${round(c['attributes']['mqn_dez'],2) or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.regimetyp', lang)}</th>
<td>${c['attributes']['regimetyp'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.regimenummer', lang)}</th>
  % if c['attributes']['regimenummer'] != None:
<td>${c['attributes']['regimenummer'] or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
<tr>
<th class="cell-left">${mod_translate.Translator.translate('ch.bafu.mittlere-abfluesse.abflussvar', lang)}</th>
  % if c['attributes']['abflussvar'] != None:
<td>${c['attributes']['abflussvar'] or '-'}</td>
  % else:
<td>-</td>
  % endif
</tr>
</table>
</%def>
