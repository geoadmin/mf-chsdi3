<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
<%
linkeddatahost = request.registry.settings['linkeddatahost']
ldlink = linkeddatahost + '/boundaries/district/' + str(c['id'])
%>
<% c['stable_id'] = True %>
<tr>
    <td class="cell-left">${_('bfsnr')}</td>
    % if c['featureId']:
        <td>${int(round(c['featureId']))}</td>
    % else:
        <td>-</td>
    % endif
</tr>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill.name')}</td><td>${c['attributes']['name']}</td></tr>
<tr>
    <td class="cell-left">${_('flaeche_ha')}</td>
    % if c['attributes']['flaeche']:
        <td>${int(round(c['attributes']['flaeche']))}</td>
    % else:
        <td>-</td>
    % endif
</tr>
<tr><td class="cell-left">${_('link')}</td><td><a href="${ldlink}" target="_blank">Linked Data URI</a></td></tr>
</%def>
