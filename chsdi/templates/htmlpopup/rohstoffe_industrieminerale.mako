<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>

       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.obname')}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.obnamealt')}</td><td>${c['attributes']['obnamealt'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.imkinds')}</td><td>${c['attributes']['imkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.edrskinds')}</td><td>${c['attributes']['edrskinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.emkinds')}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.stkind')}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${_('ch.swisstopo.geologie-rohstoffe-industrieminerale.purl')}</td><td><a  target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text')}</a></td></tr>
</%def>
