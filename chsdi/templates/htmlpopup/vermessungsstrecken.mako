<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<tr><td class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.gewaessernummer', lang)}</td>    <td>${c['attributes']['gewaessernummer'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.streckenid', lang)}</td>         <td>${c['attributes']['streckenid'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.bezeichnung', lang)}</td>        <td>${c['attributes']['bezeichnung'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.gwlnr', lang)}</td>              <td>${c['attributes']['gwlnr'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<%
    lang = 'fr' if lang in ('fr', 'it') else 'de'
    url_uebersicht = 'url_uebersicht_%s' % lang
%>
<table class="table-with-border kernkraftwerke-extended">
<tr>
<td width="20%">&nbsp;</td>
<td width="30%">&nbsp;</td>
<td width="20%">&nbsp;</td>
<td width="30%" >&nbsp;</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.routeid', lang)}</th>
<td>${c['attributes']['routeid'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.gewaessernummer', lang)}</th>
<td>${c['attributes']['gewaessernummer'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.bemerkung', lang)}</th>
<td>${c['attributes']['bemerkung'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.anfangsmass', lang)}</th>
% if c['attributes']['anfangsmass']:
    <td>${round(c['attributes']['anfangsmass'],3) or '-'}</td>
% else:
    <td>-</td>
% endif
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.endmass', lang)}</th>
% if c['attributes']['endmass']:
    <td>${round(c['attributes']['endmass'],3) or '-'}</td>
% else:
    <td>-</td>
% endif
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.streckenid', lang)}</th>
<td>${c['attributes']['streckenid'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.bezeichnung', lang)}</th>
<td>${c['attributes']['bezeichnung'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.laenge_km', lang)}</th>
% if c['attributes']['laenge_km']:
    <td>${round(c['attributes']['laenge_km'],3) or '-'}</td>
% else:
    <td>-</td>
% endif
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.anzahl_profile', lang)}</th>
<td>${c['attributes']['anzahl_profile'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.aufnahme_intervall', lang)}</th>
<td>${c['attributes']['aufnahme_intervall'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.aufnahme_letzte', lang)}</th>
<td>${c['attributes']['aufnahme_letzte'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.wasserbau-vermessungsstrecken.gwlnr', lang)}</th>
<td>${c['attributes']['gwlnr'] or '-'}</td>
</tr>
</table>
</%def>
