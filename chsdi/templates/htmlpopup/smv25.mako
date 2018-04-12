<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.images-swissimage.metadata.name_de')}</td>   <td>${c['attributes']['name_de'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.tileid')}</td>    <td>${c['attributes']['tileid'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.lk25-papierkarte.metadata.datenstand')}</td>    <td>${c['attributes']['datenstand'] or '-'}</td></tr>
</%def>
