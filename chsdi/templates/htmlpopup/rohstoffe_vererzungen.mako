<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>

       <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-rohstoffe-vererzungen.obname', lang)}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-rohstoffe-vererzungen.obnamealt', lang)}</td><td>${c['attributes']['obnamealt'] or '-'}</td></tr>
       <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-rohstoffe-vererzungen.grkinds', lang)}</td><td>${c['attributes']['grkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-rohstoffe-vererzungen.edmikinds', lang)}</td><td>${c['attributes']['edmikinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-rohstoffe-vererzungen.emkinds', lang)}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-rohstoffe-vererzungen.stkind', lang)}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${Translator.translate('ch.swisstopo.geologie-rohstoffe-vererzungen.purl')}</td><td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${_('layer_url_portal_text', lang)}</a></td></tr>
</%def>
