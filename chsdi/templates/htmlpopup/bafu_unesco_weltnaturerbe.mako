<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.bgdi_id')}</td>
        <td>${c['attributes']['bgdi_id'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.zone')}</td>
        <td>${c['attributes']['zone'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.datum')}</td>
        <td>${c['attributes']['datum'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.link')}</td>
        <td>${c['attributes'][link] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.unesco-weltnaturerbe.area')}</td>
        <td>${c['attributes']['area'] or '-'}</td>
    </tr>
</%def>
