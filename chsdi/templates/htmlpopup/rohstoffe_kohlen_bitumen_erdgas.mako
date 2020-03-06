<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <% c['stable_id'] = True %>

       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.obname', lang)}</td><td>${c['attributes']['obname'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.obnamealt', lang)}</td><td>${c['attributes']['obnamealt'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.erkinds', lang)}</td><td>${c['attributes']['erkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.ederkinds', lang)}</td><td>${c['attributes']['ederkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.emkinds', lang)}</td><td>${c['attributes']['emkinds'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.stkind', lang)}</td><td>${c['attributes']['stkind'] or '-'}</td></tr>
       <tr><td class="cell-left">${h.translate('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas.purl', lang)}</td><td><a target="_blank" href=${c['attributes']['purl'] or '-'}>${h.translate('layer_url_portal_text', lang)}</a></td></tr>
</%def>
