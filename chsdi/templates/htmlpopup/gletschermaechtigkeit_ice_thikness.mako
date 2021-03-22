<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.mean_thik')}</td><td>${c['attributes']['mean_thick'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.max_thik')}</td><td>${c['attributes']['max_thick'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.volume_mio')}</td><td>${c['attributes']['volume'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.year_mode')}</td><td>${c['attributes']['year_mode'] or '-'}</td></tr>

</%def>

