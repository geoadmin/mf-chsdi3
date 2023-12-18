<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    
    <% c['stable_id'] = True %>

    <%
    lang = lang if lang in ('fr', 'it') else 'de'
    description = 'descrip_%s' % lang
    %>

    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.icao')}</td>         <td>${c['attributes']['icao'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.name')}</td>         <td>${c['attributes']['name'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.canton')}</td>           <td>${c['attributes']['canton'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.description')}</td>     <td>${c['attributes'][description] or '-'}</td></tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.arp_east')}</td>
        % if c['attributes']['arp_east']:
            <td>${int(round(c['attributes']['arp_east']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.arp_north')}</td>
        % if c['attributes']['arp_north']:
            <td>${int(round(c['attributes']['arp_north']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bazl.gebirgslandeplaetze.elevation')}</td>
        % if c['attributes']['elevation']:
            <td>${int(round(c['attributes']['elevation']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>
