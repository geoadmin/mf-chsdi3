<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
linkeddatahost = request.registry.settings['linkeddatahost']
ldlink = linkeddatahost + '/boundaries/municipality/' + str(c['id'])
%>
<% c['stable_id'] = True %>
<tr>
    <td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.id')}</td>
    % if c['featureId']:
        <td>${c['featureId']}</td>
    % else:
        <td>-</td>
    % endif
</tr>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.gemname')}</td><td>${c['attributes']['gemname']}</td></tr>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.typ')}</td><td>${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.%s' % c['attributes']['objektart'])}</td></tr>
<tr>
    <td class="cell-left">${_('flaeche_ha')}</td>
    % if c['attributes']['gemflaeche']:
        <td>${int(round(c['attributes']['gemflaeche']))}</td>
    % else:
        <td>-</td>
    % endif
</tr>
<tr>
    <td class="cell-left">${_('perimeter_m')}</td>
    % if c['attributes']['perimeter']:
        <td>${int(round(c['attributes']['perimeter']))}</td>
    % else:
        <td>-</td>
    % endif
</tr>
    % if c['attributes']['is_current_jahr']:
        <tr><td class="cell-left">${_('link')}</td><td><a href="${ldlink}" target="_blank">Linked Data URI</a></td></tr>
    % endif

</%def>
