<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">

<tr><td class="cell-left">${_(c['layerBodId'] + '.name')}</td> <td>${c['attributes']['name'] or '-'}</td></tr>
<tr><td class="cell-left">${_(c['layerBodId'] + '.sigel')}</td> <td>${c['attributes']['sigel'] or '-'}</td></tr>
<tr><td class="cell-left">${_(c['layerBodId'] + '.inventar')}</td> <td>${c['attributes']['inventar'] or '-'}</td></tr>

<tr><td class="cell-left">${_(c['layerBodId'] + '.link')}</td>
% if c['attributes']['link']:
<td><a href="${c['attributes']['link']}" target="_blank">${c['attributes']['link']}</a></td>
% else:
<td> ${'-'} </td>
% endif

<tr><td class="cell-left">${_(c['layerBodId'] + '.kontakt')}</td>
% if c['attributes']['kontakt']:
<td><a href="${c['attributes']['kontakt']}" target="_blank">${c['attributes']['kontakt']}</a></td></tr>
% else:
<td> ${'-'} </td></tr>
% endif

<tr><td class="cell-left">${_(c['layerBodId'] + '.publikation')}</td>
% if c['attributes']['publikation']:
<td><a href="${c['attributes']['publikation']}" target="_blank">${c['attributes']['publikation']}</a></td></tr>
% else:
<td> ${'-'} </td></tr>
% endif

<tr><td class="cell-left">${_(c['layerBodId'] + '.quelle')}</td> <td>${c['attributes']['quelle'] or '-'}</td></tr>
<tr><td class="cell-left">${_(c['layerBodId'] + '.bemerkung')}</td> <td>${c['attributes']['bemerkung'] or '-'}</td></tr>

</%def>
