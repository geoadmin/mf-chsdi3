<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-vererzungen.obname')}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-vererzungen.obnamealt')}</td><td>${c['attributes']['obnamealt'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-vererzungen.grkinds')}</td><td>${c['attributes']['grkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-vererzungen.edmikinds')}</td><td>${c['attributes']['edmikinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-vererzungen.emkinds')}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-vererzungen.stkind')}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-vererzungen.purl')}</td><td><a target="_blank" href=${c['attributes']['purl'] or '-'}>Link</a></td></tr>
</%def>
