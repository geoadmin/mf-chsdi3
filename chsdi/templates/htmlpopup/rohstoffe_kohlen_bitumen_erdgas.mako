<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.obname')}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.obnamealt')}</td><td>${c['attributes']['obnamealt'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.erkinds')}</td><td>${c['attributes']['erkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.ederkinds')}</td><td>${c['attributes']['ederkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.emkinds')}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.stkind')}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.purl')}</td><td>${c['attributes']['purl'] or '-'}</td></tr>
</%def>
