<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
       <tr><td class="cell-left">${t.translate('ch.swisstopo.verschiebungsvektoren-tsp1.name', lang)}</td><td>${c['attributes']['name'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.translate('typ', lang)}</td><td>${c['attributes']['type'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.translate('fp_Y03_X03', lang)}</td><td>${c['attributes']['e_lv03'] or '-'} / ${c['attributes']['n_lv03'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.translate('fp_E95_N95', lang)}</td><td>${c['attributes']['e_lv95'] or '-'} / ${c['attributes']['n_lv95'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.translate('DE', lang)}</td><td>${c['attributes']['de'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.translate('DN', lang)}</td><td>${c['attributes']['dn'] or '-'}</td></tr>
       <tr><td class="cell-left">${t.translate('FS', lang)}</td><td>${c['attributes']['fs'] or '-'}</td></tr>
</%def>
