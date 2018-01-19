<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
linkeddatahost = request.registry.settings['linkeddatahost']
ldlink = linkeddatahost + '/boundaries/municipality/' + str(c['id'])
arr_obj_art = ['gemeindegebiet', 'kantonsgebiet', 'kommunanz']
obj_art = arr_obj_art[c['attributes']['objektart']]
%>
<% c['stable_id'] = True %> 
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.id')}</td><td>${int(round(c['featureId'])) or '-'}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.gemname')}</td><td>${c['attributes']['gemname']}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.typ')}</td><td>${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.%s' % obj_art)}</td></tr>
<tr><td class="cell-left">${_('flaeche_ha')}</td><td>${int(round(c['attributes']['gemflaeche'])) or '-'} ha</td></tr>
<tr><td class="cell-left">${_('perimeter_m')}</td><td>${int(round(c['attributes']['perimeter'])) or '-'} m</td></tr>
<tr><td class="cell-left">${_('link')}</td><td><a href="${ldlink}" target="_blank">Linked Data URI</a></td></tr>
</%def>
