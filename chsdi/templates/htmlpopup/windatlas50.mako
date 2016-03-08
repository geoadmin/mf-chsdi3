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
<tr><td class="cell-left">${_('altitude')}</td>    <td>${altitude}</td></tr>
<tr><td class="cell-left">${_('height')}</td>      <td>xxx</td></tr>
<tr><td class="cell-left">all attributes</td>      <td></td></tr>
% for key in c['properties']:
<tr><td class="cell-left">${key}</td>              <td>${c['properties'][key]}</td></tr>
% endfor
<tr><td class="cell-left">windrose</td>            <td><div id="rose"></div></td></tr>

</%def>
