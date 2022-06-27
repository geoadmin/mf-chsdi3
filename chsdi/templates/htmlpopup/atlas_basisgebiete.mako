<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.gebietskennzahl')}</td>    <td>${c['attributes']['gebietskennzahl']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.bemerkung')}</td>          <td>${c['attributes']['bemerkung']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.flussgebiet')}</td>        <td>${c['attributes']['flussgebiet']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.mit_hoe')}</td>            <td>${c['attributes']['mit_hoe']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.mit_ns')}</td>             <td>${c['attributes']['mit_ns']}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.s_w_ns')}</td>             <td>${c['attributes']['s_w_ns']}</td></tr>
</%def>

<%def name="extended_info(c, lang)">

<table class="table-with-border kernkraftwerke-extended">
<tr>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.nummer')}</th>
<td width="25%">${c['attributes']['nummer'] or '-'}</td>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.gebietskennzahl')}</th>
<td width="25%">${c['attributes']['gebietskennzahl'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.bemerkung')}</th>
<td width="25%">${c['attributes']['bemerkung'] or '-'}</td>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.flussgebiet')}</th>
<td width="25%">${c['attributes']['flussgebiet'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.max_hoe')}</th>
<td width="25%">${c['attributes']['max_hoe'] or '-'}</td>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.min_hoe')}</th>
<td width="25%">${c['attributes']['min_hoe'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.mit_hoe')}</th>
% if c['attributes']['mit_hoe']:
    <td width="25%">${round(c['attributes']['mit_hoe'], 2)}</td>
% else:
    <td width="25%">-</td>
% endif
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.mit_ns')}</th>
% if c['attributes']['mit_ns']:
    <td width="25%">${round(c['attributes']['mit_ns'], 2)}</td>
% else:
    <td width="25%">-</td>
% endif
</tr>
<tr>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.s_w_ns')}</th>
% if c['attributes']['s_w_ns']:
    <td width="25%">${round(c['attributes']['s_w_ns'], 3)}</td>
% else:
    <td width="25%">-</td>
% endif
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.jahrtemp_g')}</th>
<td width="25%">${c['attributes']['jahrtemp_g'] or '-'}</td>
</tr>
<tr>
<th width="25%"class="cell-left">${_('ch.bafu.hydrologischer-atlas_basisgebiete.winttemp_g')}</th>
<td width="25%">${c['attributes']['winttemp_g'] or '-'}</td>
<th width="25%"class="cell-left">${_('flaeche_km2')}</th>
% if c['attributes']['shape_area']:
    <td width="25%">${_('flaeche_ha')}</td><td>${round(c['attributes']['shape_area'] / 1000000, 1)}</td>
% else:
    <td width="25%">${_('flaeche_ha')}</td><td>-</td>
% endif
</tr>

</table>
</%def>
