<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.well_name')}</td>
        <td>${c['attributes']['well_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.link_viewer')}</td>
        % if c['attributes']['link_viewer'] == '-' or c['attributes']['link_viewer'] is None:
            <td>-</td>
        % else:
            <td><a href="${c['attributes']['link_viewer']}" target="_blank">${c['attributes']['link_viewer']}</a></td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.link_assets')}</td>
        % if c['attributes']['link_assets'] == '-' or c['attributes']['link_assets'] is None:
            <td>-</td>
        % else:
            <td><a href="${c['attributes']['link_assets']}" target="_blank">${c['attributes']['link_assets']}</a></td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.link_boreholes')}</td>
        % if c['attributes']['link_boreholes'] == '-' or c['attributes']['link_boreholes'] is None:
            <td>-</td>
        % else:
            <td><a href="${c['attributes']['link_boreholes']}" target="_blank">${c['attributes']['link_boreholes']}</a></td>
        % endif
    </tr>
</%def>
