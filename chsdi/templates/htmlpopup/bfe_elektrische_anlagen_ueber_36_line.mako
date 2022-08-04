<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
    <%
        stromnetztyp = c['layerBodId'] + '.' + c['attributes']['stromnetztyp']
        leitungtyp = c['layerBodId'] + '.' + c['attributes']['leitungtyp']
        spannung = c['layerBodId'] + '.' + c['attributes']['spannung']
        frequenz = c['layerBodId'] + '.' + c['attributes']['frequenz']
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
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.LeitungTyp')}</td>
        <td>${_(leitungtyp)}</td>
    </tr>
    % if c['attributes']['spannungandere']:
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Spannung')}</td>
        <td>${c['attributes']['spannungandere']} kV</td>
    </tr>
    % else:
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Spannung')}</td>
        <td>${_(spannung)}</td>
    </tr>
    % endif
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Frequenz')}</td>
        <td>${_(frequenz)}</td>
    </tr>
</%def>
