<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        stromnetztyp = c['layerBodId'] + '.' + c['attributes']['stromnetztyp']
    %>

    % if c['attributes']['masttyp']:
        <%
            masttyp = c['layerBodId'] + '.' + c['attributes']['masttyp']
        %>
        <tr>
            <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Eigentuemer')}</td>
            <td>${c['attributes']['eigentuemer'] or '-'}</td>
        </tr>
        <tr>
            <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.StromnetzTyp')}</td>
        <td>${_(stromnetztyp)}</td>
        </tr>
        <tr>
            <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.MastTyp')}</td>
        <td>${_(masttyp)}</td>
        </tr>
        <tr>
            <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Hoehe')}</td>
            <td>${c['attributes']['hoehe'] or '-'}</td>
        </tr>
    % endif

    % if c['attributes']['stationtyp']:
        <%
            stationtyp = c['layerBodId'] + '.' + c['attributes']['stationtyp']
        %>
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
        <td>${_(stromnetztyp)}</td>
        </tr>
        <tr>
            <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.StationTyp')}</td>
        <td>${_(stationtyp)}</td>
        </tr>
    % endif
    
</%def>
