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
        % if c['attributes']['arp_east']:
            <td>${int(round(c['attributes']['arp_east']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.flugplaetze-heliports.arp_north')}</td>
        % if c['attributes']['arp_north']:
            <td>${int(round(c['attributes']['arp_north']))}</td>
        % else:
            <td>-</td>
        % endif
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
