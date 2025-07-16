<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.prof_name')}</td>
        <td>${c['attributes']['profil_name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_(c['layerBodId'] + '.link_viewer')}</td>
        % if c['attributes']['link_viewer'] == '-' or c['attributes']['link_viewer'] is None:
            <td>-</td>
        % else:
            <td><a href="${c['attributes']['link_viewer']}" target="_blank">${c['attributes']['link_viewer']}</a></td>
        % endif
    </tr>
</%def>
