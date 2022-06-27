<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_('ch.swisstopo.geologie-geomol-temperaturverteilung_500.pixel_value')}</td>
        % if c['attributes']['pixel_value']:
            <td>${int(round(c['attributes']['pixel_value']))}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>

