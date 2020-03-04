<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>

       <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-rohstoffe-industrieminerale.obname', lang)}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-rohstoffe-industrieminerale.obnamealt', lang)}</td><td>${c['attributes']['obnamealt'] or '-'}</td></tr>
       <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-rohstoffe-industrieminerale.imkinds', lang)}</td><td>${c['attributes']['imkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-rohstoffe-industrieminerale.edrskinds', lang)}</td><td>${c['attributes']['edrskinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-rohstoffe-industrieminerale.emkinds', lang)}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-rohstoffe-industrieminerale.stkind', lang)}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.geologie-rohstoffe-industrieminerale.purl', lang)}</td><td><a  target="_blank" href=${c['attributes']['purl'] or '-'}>${mod_translate.Translator.translate('layer_url_portal_text', lang)}</a></td></tr>
</%def>
