<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.gebietskennzahl', lang)}</td>    <td>${c['attributes']['gebietskennzahl']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.bemerkung', lang)}</td>          <td>${c['attributes']['bemerkung']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.flussgebiet', lang)}</td>        <td>${c['attributes']['flussgebiet']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.mit_hoe', lang)}</td>            <td>${c['attributes']['mit_hoe']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.mit_ns', lang)}</td>             <td>${c['attributes']['mit_ns']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.s_w_ns', lang)}</td>             <td>${c['attributes']['s_w_ns']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    shape_area_in_km2 = c['attributes']['shape_area']
    if shape_area_in_km2 is not None:
        shape_area_in_km2 = round(shape_area_in_km2 / 1000000,1)
    else:
        shape_area_in_km2 = 0

%>
<table class="table-with-border kernkraftwerke-extended">
<tr>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.nummer', lang)}</th>
<td width="25%">${c['attributes']['nummer'] or '-'}</td>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.gebietskennzahl', lang)}</th>
<td width="25%">${c['attributes']['gebietskennzahl'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.bemerkung', lang)}</th>
<td width="25%">${c['attributes']['bemerkung'] or '-'}</td>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.flussgebiet', lang)}</th>
<td width="25%">${c['attributes']['flussgebiet'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.max_hoe', lang)}</th>
<td width="25%">${c['attributes']['max_hoe'] or '-'}</td>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.min_hoe', lang)}</th>
<td width="25%">${c['attributes']['min_hoe'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.mit_hoe', lang)}</th>
% if c['attributes']['mit_hoe'] != None:
<td width="25%">${round(c['attributes']['mit_hoe'],2) or '-'}</td>
% else:
<td width="25%">-</td>
% endif
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.mit_ns', lang)}</th>
% if c['attributes']['mit_ns'] != None:
<td width="25%">${round(c['attributes']['mit_ns'],2) or '-'}</td>
% else:
<td width="25%">-</td>
% endif
</tr>
<tr>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.s_w_ns', lang)}</th>
% if c['attributes']['s_w_ns'] != None:
<td width="25%">${round(c['attributes']['s_w_ns'],3) or '-'}</td>
% else:
<td width="25%">-</td>
% endif
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.jahrtemp_g', lang)}</th>
<td width="25%">${c['attributes']['jahrtemp_g'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${t.Translator.translate('ch.bafu.hydrologischer-atlas_basisgebiete.winttemp_g', lang)}</th>
<td width="25%">${c['attributes']['winttemp_g'] or '-'}</td>
<th width="25%"class="cell-left">${t.Translator.translate('flaeche_km2', lang)}</th>
<td width="25%">${shape_area_in_km2 or '-'}</td>
</tr>

</table>
</%def>
