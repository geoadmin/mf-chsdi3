<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${_('ch.swisstopo.swissimage-product.metadata.kbnum')}</td>       <td>${c['attributes']['kbnum'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swissimage-product.metadata.flightyear')}</td>           <td>${c['attributes']['flightyear']}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swissimage-product.metadata.gsd')}</td>            <td>${c['attributes']['gsd'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('ch.swisstopo.swissimage-product.metadata.colormode')}</td>            <td>${_(c['attributes']['colormode'] or '-')}</td></tr>
</%def>

