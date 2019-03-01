<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
%>
    <% c['stable_id'] = False %>

    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.typ')}</td>           <td>${c['attributes']['typ'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.typ_txt')}</td>       <td>${c['attributes']['typ_txt'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.istaltrechtlich')}</td>       <td>${c['attributes']['istaltrechtlich'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.rechtstatus')}</td>       <td>${c['attributes']['rechtsstatus'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.kt_status')}</td>       <td>${c['attributes']['kt_status'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.rechtskraftdatum')}</td>       <td>${c['attributes']['rechtskraftdatum'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.bemerkungen_de')}</td>       <td>${c['attributes']['bemerkungen_fr'] or c['attributes']['bemerkungen_fr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_grundwasserschutzareale.kanton')}</td>       <td>${c['attributes']['kanton'] or '-'}</td></tr>
</%def>
