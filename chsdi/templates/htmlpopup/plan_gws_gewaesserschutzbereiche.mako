<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
%>
    <% c['stable_id'] = False %>

    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_gewaesserschutzbereiche.typ')}</td>           <td>${c['attributes']['typ'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_gewaesserschutzbereiche.kt_typbez')}</td>       <td>${c['attributes']['kt_typbez'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_gewaesserschutzbereiche.bemerkungen_de')}</td>       <td>${c['attributes']['bemerkungen_fr'] or c['attributes']['bemerkungen_fr'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bafu.planerischer-gewaesserschutz_gewaesserschutzbereiche.kanton')}</td>       <td>${c['attributes']['kanton'] or '-'}</td></tr>
</%def>
