<%inherit file="base.mako"/>

<%def name="table_body(c,lang)">
    <tr>
      <td class="cell-left">${_('laenge_m')}</td>
      % if c['attributes']['length']:
         <td>${int(round(c['attributes']['length']))} m</td>
      % else:
         <td>-</td>
      % endif
    </tr>
</%def>
