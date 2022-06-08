<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    % if c['attributes']['flaeche_ha']:
        <tr><td class="cell-left">${_('flaeche_ha')}</td><td>${int(round(c['attributes']['flaeche_ha']))}</td></tr>
    % else:
        <tr><td class="cell-left">${_('flaeche_ha')}</td><td>-</td></tr>
    % endif
    % if c['attributes']['stand']:
        <tr><td class="cell-left">${_('stand')}</td><td>${int(round(c['attributes']['stand']))}</td></tr>
    % else:
        <tr><td class="cell-left">${_('stand')}</td><td>-</td></tr>
    % endif
</%def>


