<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.images-swissimage.metadata.name_de')}</td>      <td>${c['attributes']['lk_name']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swissimage-product.metadata.kbnum')}</td>       <td>${c['attributes']['tileid']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swissimage-product.metadata.flightyear')}</td>  <td>${c['attributes']['datenstand']}</td></tr>
</%def>
