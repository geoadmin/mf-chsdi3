<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
linkeddatahost = request.registry.settings['linkeddatahost']
ldlink = linkeddatahost + '/boundaries/country/' + str(c['id'])
%>
<% c['stable_id'] = True %> 
<tr><td class="cell-left">${h.translate('ch.swisstopo.swissboundaries3d-land-flaeche.fill.id', lang)}</td><td>${c['id'] or '-'}</td></tr>
<tr><td class="cell-left">${h.translate('ch.swisstopo.swissboundaries3d-land-flaeche.fill.name', lang)}</td><td>${c['attributes']['bez']}</td></tr>
<tr><td class="cell-left">${h.translate('flaeche_ha', lang)}</td><td>${int(round(c['attributes']['flaeche'])) or '-'} ha</td></tr>
<tr><td class="cell-left">${h.translate('link', lang)}</td><td><a href="${ldlink}" target="_blank">Linked Data URI</a></td></tr>
</%def>
