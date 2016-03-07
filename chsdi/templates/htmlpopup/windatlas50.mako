<%inherit file="base.mako"/>


<%def name="table_body(c, lang)">
<%

test = None

if c['layerBodId'] == 'ch.bfe.windenergie-geschwindigkeit_h50':
    altitude = 50
elif c['layerBodId'] == 'ch.bfe.windenergie-geschwindigkeit_h75':
    altitude = 75
elif c['layerBodId'] == 'ch.bfe.windenergie-geschwindigkeit_h100':
    altitude = 100
elif c['layerBodId'] == 'ch.bfe.windenergie-geschwindigkeit_h125':
    altitude = 125
elif c['layerBodId'] == 'ch.bfe.windenergie-geschwindigkeit_h150':
    altitude = 150
else:
    altitude = None
endif

%>

<!-- html output -->
<tr><td class="cell-left">${_('v_mean')}</td>    <td>${c['properties']['v_mean'] or '-'}</td></tr
<tr><td class="cell-left">${_('altitude')}</td>    <td>${altitude}</td></tr>
<tr><td class="cell-left">${_('height')}</td>    <td>${test}</td></tr>
<tr><td class="cell-left">all attributes</td>    <td>${c['properties']}</td></tr>
<tr><td class="cell-left">windrose</td>    <td><div id="rose"></div></td></tr>

</%def>
