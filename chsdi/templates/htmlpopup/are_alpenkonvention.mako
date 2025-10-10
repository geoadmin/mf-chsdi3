<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_('flaeche_ha')}</td>
        % if c['attributes']['flaeche_ha']:
            <td>${int(round(c['attributes']['flaeche_ha']))}</td></tr>
        % else:
            <td>-</td>
        % endif
    </tr>
    <tr>
        <td class="cell-left">${_('stand')}</td>
        % if c['attributes']['stand']:
            <td>${int(round(c['attributes']['stand']))}</td></tr>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>


