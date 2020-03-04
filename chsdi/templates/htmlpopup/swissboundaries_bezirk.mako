<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
linkeddatahost = request.registry.settings['linkeddatahost']
ldlink = linkeddatahost + '/boundaries/district/' + str(c['id'])
%>
<% c['stable_id'] = True %>
<tr><td class="cell-left">${mod_translate.Translator.translate('bfsnr', lang)}</td><td>${int(round(c['featureId'])) or '-'}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill.name', lang)}</td><td>${c['attributes']['name']}</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('flaeche_ha', lang)}</td><td>${int(round(c['attributes']['flaeche'])) or '-'} ha</td></tr>
<tr><td class="cell-left">${mod_translate.Translator.translate('link', lang)}</td><td><a href="${ldlink}" target="_blank">Linked Data URI</a></td></tr>
</%def>
