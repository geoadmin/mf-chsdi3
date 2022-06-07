<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    % if c['attributes']['area']:
        <tr><td class="cell-left">${_('flaeche_m2')}</td><td>${int(round(c['attributes']['area']))}</td></tr>
    % else:
        <tr><td class="cell-left">${_('flaeche_m2')}</td><td>-</td></tr>
    % endif
    % if c['attributes']['perimeter']:
        <tr><td class="cell-left">${_('perimeter_m')}</td><td>${int(round(c['attributes']['perimeter']))}</td></tr>
    % else:
        <tr><td class="cell-left">${_('perimeter_m')}</td><td>-</td></tr>
    % endif
</%def>
