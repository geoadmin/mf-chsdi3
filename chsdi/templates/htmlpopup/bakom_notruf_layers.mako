<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_festnetz.routing_nr')}</td>
        <td>${c['attributes']['routing_nr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_festnetz.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bakom.notruf-112_festnetz.chg_date')}</td>
        <td>${c['attributes']['chg_date'] or '-'}</td>
    </tr>
</%def>
