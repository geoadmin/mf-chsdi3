<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <tr>
        <td class="cell-left">${_('ch.bafu.gewaesser-uferbestockung.name')}</td>
        <td>${c['attributes']['name'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gewaesser-uferbestockung.gwl_nr')}</td>
        <td>${c['attributes']['gwl_nr'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bafu.gewaesser-uferbestockung.bestockung')}</td>
        % if c['attributes']['bestockung']:
            <td>${round(c['attributes']['bestockung'], 1)}</td>
        % else:
            <td>-</td>
        % endif
    </tr>
</%def>
