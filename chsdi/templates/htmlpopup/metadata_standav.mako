<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr>
        <td class="cell-left">${_('ch.swisstopo-vd.geometa-standav.canton')}</td>
        <td>${c['attributes']['canton'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo-vd.geometa-standav.idn')}</td>
        <td>${c['attributes']['idn'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.swisstopo-vd.geometa-standav.quality')}</td>
        <td>${c['attributes']['quality'] or '-'}</td>
    </tr>
</%def>
