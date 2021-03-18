<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.name')}</td><td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.mean_thik')}</td><td>${round(c['attributes']['mean_thick'], 0) or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.max_thik')}</td><td>${round(c['attributes']['max_thick'], 0) or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.volume_mio')}</td><td>${round(c['attributes']['volume'], 2) or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.geologie-gletschermaechtigkeit.year_mode')}</td><td>${c['attributes']['year_mode'] or '-'}</td></tr>
${'{0:.2f}'.format(34.567645765)}").render()
</%def>

