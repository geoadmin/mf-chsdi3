<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<% c['stable_id'] = True %>
    <%
    official = 'yesText' if c['attributes']['adr_official'] else 'noText'
    %>

    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.adr_egaid')}</td>      <td>${c['featureId']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.bdg_egid')}</td>       <td>${c['attributes']['bdg_egid'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.adr_edid')}</td>       <td>${c['attributes']['adr_edid']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.str_esid')}</td>       <td>${c['attributes']['str_esid'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.stn_label')}</td>      <td>${c['attributes']['stn_label'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.adr_number')}</td>     <td>${c['attributes']['adr_number'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.zip_label')}</td>      <td>${_(c['attributes']['zip_label'] or '-')}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.com_fosnr')}</td>      <td>${_(c['attributes']['com_fosnr'] or '-')}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.com_name')}</td>       <td>${_(c['attributes']['com_name'] or '-')}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.bdg_category')}</td>   <td>${_(c['attributes']['bdg_category'] or '-')}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.adr_status')}</td>     <td>${_(c['attributes']['adr_status'] or '-')}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.adr_official')}</td>   <td>${_(official)}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.amtliches-gebaeudeadressverzeichnis.adr_modified')}</td>   <td>${h.parse_date_string(c['attributes']['adr_modified'],'%Y%m%d','%Y-%m-%d')}</td></tr>
</%def>
