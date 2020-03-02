<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.translate('ch.swisstopo.swiss-map-vector25.metadata.kbbez', lang)}</td>   <td>${c['attributes']['name_de'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.swiss-map-vector25.metadata.kbnum', lang)}</td>    <td>${c['attributes']['tileid'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.translate('ch.swisstopo.swiss-map-vector25.metadata.flightyear', lang)}</td>    <td>${c['attributes']['datenstand'] or '-'}</td></tr>
</%def>
