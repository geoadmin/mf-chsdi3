<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    % if c['attributes']['geom_type'] == 'line':
    <tr>
        <td class="cell-left">${_('ch.bav.lage-stoerfallverordnung_eisenbahnanlagen.line_name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    % else:
    <tr>
        <td class="cell-left">${_('ch.bav.lage-stoerfallverordnung_eisenbahnanlagen.poly_name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    % endif
</%def>
