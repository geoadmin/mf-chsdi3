<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.icao')}</td>
        <td>${c['attributes']['icao'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.location')}</td>
        <td>${c['attributes']['location'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.canton')}</td>
        <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.arp_east')}</td>
        <td>${int(round(c['attributes']['arp_east'])) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.arp_north')}</td>
        <td>${int(round(c['attributes']['arp_north'])) or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.elevation')}</td>
        % if c['attributes']['elevation']:
            <td>${int(round(c['attributes']['elevation']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>
