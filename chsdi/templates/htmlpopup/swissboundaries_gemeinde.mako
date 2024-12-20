<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
<%
linkeddatahost = request.registry.settings['linkeddatahost']
ldlink = linkeddatahost + '/boundaries/municipality/' + str(c['id'])
lang = lang if lang in ('fr','it') else 'de'
link = 'link_%s' % lang
%>
<% c['stable_id'] = True %>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.gemname')}</td><td>${c['attributes']['gemname']}</td></tr>
<tr>
    <td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.gde_nr')}</td>
    % if c['attributes']['gde_nr']:
        <td>${c['attributes']['gde_nr']}</td>
    % else:
        <td>-</td>
    % endif
</tr>
<tr>
    <td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.gde_hist_id')}</td>
    % if c['attributes']['gde_hist_id']:
        <td>${c['attributes']['gde_hist_id']}</td>
    % else:
        <td>-</td>
    % endif
</tr>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.typ')}</td><td>${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.%s' % c['attributes']['objektart'])}</td></tr>
<tr>
    <td class="cell-left">${_('flaeche_ha')}</td>
    % if c['attributes']['gemflaeche']:
        <td>${int(round(c['attributes']['gemflaeche']))}</td>
    % else:
        <td>-</td>
    % endif
</tr>
<tr><td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.jahr')}</td><td>${c['attributes']['jahr']}</td></tr>
% if c['attributes'][link]:
<tr>
    <td class="cell-left">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.link')}</td>
        <td>${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.pre_link_label')} <a href="${c['attributes'][link]}" target="_blank">${_('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill.link_label')}</a></td>

</tr>
% endif
    % if c['attributes']['is_current_jahr']:
        <tr><td class="cell-left">${_('link')}</td><td><a href="${ldlink}" target="_blank">Linked Data URI</a></td></tr>
    % endif
</%def>
