<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
%>
    <% c['stable_id'] = False %>

    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.typ')}</td>           <td>${c['attributes']['typ'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.kt_typbez')}</td>       <td>${c['attributes']['kt_typbez'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.istaltrechtlich')}</td>       <td>${c['attributes']['istaltrechtlich'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.rechtstatus')}</td>       <td>${c['attributes']['rechtsstatus'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.kt_status')}</td>       <td>${c['attributes']['kt_status'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.rechtskraftdatum')}</td>       <td>${c['attributes']['rechtskraftdatum'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.bemerkungen_de')}</td>       <td>${c['attributes']['bemerkungen_fr'] or c['attributes']['bemerkungen_fr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzzonen.kanton')}</td>       <td>${c['attributes']['kanton'] or '-'}</td></tr>
</%def>
