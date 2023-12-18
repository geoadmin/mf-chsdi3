<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        % if c['attributes']['geom_type'] == 'line':
            <td class="cell-left">${_('ch.bav.lage-stoerfallverordnung_eisenbahnanlagen.line_name')}</td>
        % else:
            <td class="cell-left">${_('ch.bav.lage-stoerfallverordnung_eisenbahnanlagen.poly_name')}</td>
        % endif
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
</%def>
