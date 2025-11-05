<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.zone')}</td>
        <td>${c['attributes']['zone'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.date')}</td>
        <td>${c['attributes']['date'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.link')}</td>
        % if c['attributes']['link'] and c['attributes']['link'].startswith('http'):
            <td><a href="${c['attributes']['link']}" target="_blank">${_('link')}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.area')}</td>
        <td>${c['attributes']['area'] or '-'}</td>
    </tr>
</%def>
