<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    % if c['attributes']['masttyp']:
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Eigentuemer')}</td>
        <td>${c['attributes']['eigentuemer'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.StromnetzTyp')}</td>
        <td>${c['attributes']['stromnetztyp'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.MastTyp')}</td>
        <td>${c['attributes']['masttyp'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Hoehe')}</td>
        <td>${c['attributes']['hoehe'] or '-'}</td>
    </tr>
    % endif
    % if c['attributes']['stationtyp']:
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Bezeichnung')}</td>
        <td>${c['attributes']['bezeichnung'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Eigentuemer')}</td>
        <td>${c['attributes']['eigentuemer'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.StromnetzTyp')}</td>
        <td>${c['attributes']['stromnetztyp'] or '-'}</td>
    </tr>
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.StationTyp')}</td>
        <td>${c['attributes']['stationtyp'] or '-'}</td>
    </tr>
    % endif
</%def>
