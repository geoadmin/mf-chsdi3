<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
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
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.LeitungTyp')}</td>
        <td>${c['attributes']['leitungtyp'] or '-'}</td>
    </tr>
    % if c['attributes']['spannungandere']:
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Spannung')}</td>
        <td>${c['attributes']['spannungandere'] or '-'}</td>
    </tr>
    % else:
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Spannung')}</td>
        <td>${c['attributes']['spannung'] or '-'}</td>
    </tr>
    % endif
    <tr>
        <td class="cell-left">${_('ch.bfe.elektrische-anlagen_ueber_36.Frequenz')}</td>
        <td>${c['attributes']['frequenz'] or '-'}</td>
    </tr>
</%def>
