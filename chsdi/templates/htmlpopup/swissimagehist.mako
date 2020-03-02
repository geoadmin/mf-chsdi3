<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.swissimage-product.metadata.kbnum', lang)}</td>       <td>${c['attributes']['kbnum'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.swissimage-product.metadata.flightyear', lang)}</td>           <td>${c['attributes']['flightyear']}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.swissimage-product.metadata.gsd', lang)}</td>            <td>${c['attributes']['gsd'] or '-'}</td></tr>
    <tr><td class="cell-left">${t.Translator.translate('ch.swisstopo.swissimage-product.metadata.colormode')}</td>            <td>${_(c['attributes']['colormode'] or '-', lang)}</td></tr>
</%def>

