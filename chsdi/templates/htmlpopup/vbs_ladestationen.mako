<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <%
        lang = lang if lang in ('fr','it','en') else 'de'
    %>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Standort')}</td>
        <td>${c['attributes']['standort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Strasse')}</td>
        <td>${c['attributes']['strasse'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.PLZ')}</td>
        <td>${int(c['attributes']['plz']) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Ort')}</td>
        <td>${c['attributes']['ort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Oeffnungszeiten')}</td>
        <td>${c['attributes']['oeffnungszeiten'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Anzahl_Ladepunkte')}</td>
        <td>${c['attributes']['anzahl_ladepunkte'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Leistung')}</td>
        <td>${c['attributes']['leistung'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Typ_Stecker')}</td>
        <td>${c['attributes']['typ_stecker'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Hinweis')}</td>
        <td>${c['attributes']['hinweis'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Kontakt')}</td>
        <td>${c['attributes']['kontakt'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.XKoordinate')}</td>
        <td>${int(c['attributes']['x_koordinate']) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.YKoordinate')}</td>
        <td>${int(c['attributes']['y_koordinate']) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.vbs.ladestationen.Bemerkungen')}</td>
        <td>${c['attributes']['bemerkungen'] or '-'}</td>
    </tr>
</%def>
