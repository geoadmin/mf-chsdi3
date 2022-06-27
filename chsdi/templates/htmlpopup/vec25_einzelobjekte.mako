<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <td class="cell-left">${_('laenge_m')}</td>
    % if c['attributes']['length']:
        <td>${int(round(c['attributes']['length']))}</td>
    % else:
        <td>-</td>
    % endif
</%def>
