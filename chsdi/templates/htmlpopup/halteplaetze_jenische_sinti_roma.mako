<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        lang = lang if lang in ('fr','it') else 'de'
        platzart_txt = 'platzart_%s' % lang
        platz_status_txt = 'platz_status_%s' % lang
        bemerkungen_txt = 'bemerkungen_%s' % lang
    %>
    <tr>
        <td class="cell-left">${_('ch.bak.halteplaetze-jenische_sinti_roma.standort')}</td>
        <td>${c['attributes']['standort'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bak.halteplaetze-jenische_sinti_roma.gemeinde')}</td>
        <td>${c['attributes']['gemeinde'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bak.halteplaetze-jenische_sinti_roma.kanton')}</td>
        <td>${c['attributes']['kanton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bak.halteplaetze-jenische_sinti_roma.platzart')}</td>
        <td>${c['attributes'][platzart_txt] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bak.halteplaetze-jenische_sinti_roma.platz_status')}</td>
        <td>${c['attributes'][platz_status_txt] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bak.halteplaetze-jenische_sinti_roma.anzahl')}</td>
        <td>${c['attributes']['anzahl_stellplaetze'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bak.halteplaetze-jenische_sinti_roma.bemerkung')}</td>
        <td>${c['attributes'][bemerkungen_txt] or '-'}</td>
    </tr>
</%def>
