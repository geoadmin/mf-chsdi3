<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
status = _('ch.swisstopo.swissnames3d.status.%s' % c['attributes']['status'] or '-')
%>
    <tr><td class="cell-left">${t.translate('name', lang)}</td>    <td><b>${c['attributes']['name'] or '-'}</b></td></tr>
    <tr><td class="cell-left">${t.translate('objektart', lang)}</td>    <td>${c['attributes']['objektart'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('sprachcode', lang)}</td>    <td>${c['attributes']['sprachcode'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('namen_typ', lang)}</td>    <td>${c['attributes']['namen_typ'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.swissnames3d.status', lang)}</td>    <td>${status}</td></tr>
</%def>

