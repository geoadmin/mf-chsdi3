<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.swiss-map-vector25.metadata.kbbez')}</td>   <td>${c['attributes']['name_de'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swiss-map-vector25.metadata.kbnum')}</td>    <td>${c['attributes']['tileid'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swiss-map-vector25.metadata.flightyear')}</td>    <td>${c['attributes']['datenstand'] or '-'}</td></tr>
</%def>
