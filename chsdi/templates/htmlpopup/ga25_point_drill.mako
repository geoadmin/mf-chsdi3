<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr><td class="cell-left">${_('geocover_description')}</td><td>${c['attributes']['description'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_spec_description')}</td><td>${c['attributes']['spec_description'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_azimut')}</td><td>${c['attributes']['azimut'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_depth_1')}</td><td>${c['attributes']['depth_1'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_description_1')}</td><td>${c['attributes']['description_1'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_depth_2')}</td><td>${c['attributes']['depth_2'] or '-'}</td></tr>
    <tr><td class="cell-left">${_('geocover_description_2')}</td><td>${c['attributes']['description_2'] or '-'}</td></tr>
    <tr>
        <td class="cell-left">${_('geocover_erl_num')}</td>
        % if c['attributes']['erl_num'].startswith("http"):
            <td><a target ="_blank" href="${c['attributes']['erl_num']}">${_('link')}</a></td>
        % else:
            <td>${c['attributes']['erl_num']}</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('linkzurlegende')}</td>
        % if c['attributes']['leg_num']:
            <td><a target ="_blank" href="${c['attributes']['leg_num']}">${_('link')}</a></td>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>
