<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    % if c['attributes']['length']:
        <tr><td class="cell-left">${_('laenge_m')}</td><td>${int(round(c['attributes']['length']))}</td></tr>
    % else:
        <tr><td class="cell-left">${_('laenge_m')}</td><td>-</td></tr>
    % endif
</%def>
