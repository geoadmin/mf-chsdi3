<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <tr><td class="cell-left">${h.translate('ch.bafu.vec25-seen.name', lang)}</td>                  <td>${c['attributes']['name']}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.vec25-seen.seetyp', lang)}</td>                <td>${c['attributes']['seetyp'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.vec25-seen.seeflaeche_km2', lang)}</td>        <td>${c['attributes']['seeflaeche_km2'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.vec25-seen.inhalt_see_mio_m3', lang)}</td>     <td>${c['attributes']['inhalt_see_mio_m3'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.vec25-seen.tiefe_see_m', lang)}</td>           <td>${c['attributes']['tiefe_see_m'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.vec25-seen.hoehenlage_muem', lang)}</td>       <td>${c['attributes']['hoehenlage_muem'] or '-'}</td></tr>
    <tr><td class="cell-left">${h.translate('ch.bafu.vec25-seen.gwlnr', lang)}</td>                 <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<table class="table-with-border kernkraftwerke-extended">
<tr>
<th width="25%"class="cell-left">${h.translate('ch.bafu.vec25-seen.gewaesserkennzahl', lang)}</th>
<td width="25%">${c['attributes']['gewaesserkennzahl'] or '-'}</td>
<th width="25%"class="cell-left">${h.translate('ch.bafu.vec25-seen.name', lang)}</th>
<td width="25%">${c['attributes']['name'] or '-'}</td>
</tr>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.seetyp', lang)}</th>
<td>${c['attributes']['seetyp'] or '-'}</td>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.natur_mit', lang)}</th>
<td>${c['attributes']['natur_mit'] or '-'}</td>
</tr>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.ausgleichsbecken', lang)}</th>
<td>${c['attributes']['ausgleichsbecken'] or '-'}</td>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.reguliert', lang)}</th>
<td>${c['attributes']['reguliert'] or '-'}</td>
</tr>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.seeflaeche_km2', lang)}</th>
<td>${round(c['attributes']['seeflaeche_km2'],2) or '-'}</td>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.inhalt_see_mio_m3', lang)}</th>
<td>${round(c['attributes']['inhalt_see_mio_m3'],2) or '-'}</td>
</tr>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.nutzinhalt_mio_m3', lang)}</th>
<td>${round(c['attributes']['nutzinhalt_mio_m3'],2) or '-'}</td>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.tiefe_see_m', lang)}</th>
<td>${c['attributes']['tiefe_see_m'] or '-'}</td>
</tr>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.hoehenlage_muem', lang)}</th>
<td>${c['attributes']['hoehenlage_muem'] or '-'}</td>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.uferlaenge_m', lang)}</th>
<td>${c['attributes']['uferlaenge_m'] or '-'}</td>
</tr>
<th class="cell-left">${h.translate('ch.bafu.vec25-seen.gwlnr', lang)}</th>
<td>${c['attributes']['gwlnr'] or '-'}</td>
<th class="cell-left">&nbsp;</th>
<td>&nbsp;</td>
</tr>

</table>
</%def>
