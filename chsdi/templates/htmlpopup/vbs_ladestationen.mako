<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
    %>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.ladestation')}</td>
        <td>${c['attributes']['ladestation'] or '-'}</td>
    </tr>
     <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.status')}</td>
        <td>${c['attributes']['status'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.strasse')}</td>
        <td>${c['attributes']['strasse'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.nummer')}</td>
        <td>${c['attributes']['nummer'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.plz')}</td>
        <td>${c['attributes']['plz'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.ort')}</td>
        <td>${c['attributes']['ort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.breitengrad')}</td>
        <td>${c['attributes']['breitengrad'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.laengengrad')}</td>
        <td>${c['attributes']['laengengrad'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.anzahl_ladepunkte')}</td>
        <td>${c['attributes']['anzahl_ladepunkte'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.bemerkungen')}</td>
        <td>${c['attributes']['bemerkungen'] or '-'}</td>
    </tr>
</%def>
