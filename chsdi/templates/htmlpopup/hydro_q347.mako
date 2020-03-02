<%inherit file="base.mako"/>

<%def name="preview()">${c.feature.titel or '-'}</%def>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
<tr><td class="cell-left">${t.translate('ch.bafu.hydrologie-q347.bilanzid', lang)}</td>     <td>${c['attributes']['bilanzid'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.hydrologie-q347.basisid', lang)}</td>      <td>${c['attributes']['basisid'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.hydrologie-q347.lhg', lang)}</td>          <td>${c['attributes']['lhg'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.hydrologie-q347.gewaesser', lang)}</td>    <td>${c['attributes']['gewaesser'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.hydrologie-q347.flaeche', lang)}</td>      <td>${c['attributes']['flaeche'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.hydrologie-q347.qp', lang)}</td>           <td>${c['attributes']['qp'] or '-'}</td></tr>
<tr><td class="cell-left">${t.translate('ch.bafu.hydrologie-q347.p', lang)}</td>            <td>${c['attributes']['p'] or '-'}</td></tr>
</%def>

<%def name="extended_info(c, lang)">
<table class="table-with-border kernkraftwerke-extended">
<tr>
<td width="25%">&nbsp;</td>
<td width="20%">&nbsp;</td>
<td width="25%">&nbsp;</td>
<td width="30%" >&nbsp;</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.bilanzid', lang)}</th>
<td>${c['attributes']['bilanzid'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.id', lang)}</th>
<td>${c['attributes']['id_q347'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.basisid', lang)}</th>
<td>${c['attributes']['basisid'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.lhg', lang)}</th>
<td>${c['attributes']['lhg'] or '-'}</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.gewaesser', lang)}</th>
<td>${c['attributes']['gewaesser'] or '-'}</td>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.flaeche', lang)}</th>
% if c['attributes']['flaeche']:
    <td>${round(c['attributes']['flaeche'],1) or '-'}</td>
% else:
    <td>-</td>
% endif
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.q_84_93', lang)}</th>
% if c['attributes']['q_84_93']:
    <td>${int(c['attributes']['q_84_93']) or '-'}</td>
% else:
    <td>-</td>
% endif
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.qp', lang)}</th>
<td>${int(c['attributes']['qp']) or '-'}</td>
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.p', lang)}</th>
% if c['attributes']['p'] != None:
    <td>${c['attributes']['p'] or '-'}&nbsp;</td>
% else:
    <td>-</td>
% endif
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.qmod', lang)}</th>
% if c['attributes']['qmod'] != None:
    <td>${int(c['attributes']['qmod']) or '-'}&nbsp;</td>
% else:
    <td>-</td>
% endif
</tr>
<tr>
<th class="cell-left">${t.translate('ch.bafu.hydrologie-q347.bemerkung', lang)}</th>
% if c['attributes']['bemerkung'] != None:
    <td>${c['attributes']['bemerkung'] or '-'}&nbsp;</td>
% else:
    <td>-</td>
% endif
<th class="cell-left">&nbsp;</th>
<td>&nbsp;</td>
</tr>
</table>
</%def>
