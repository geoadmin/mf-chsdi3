<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr>
    <td class="cell-left-large">${_('ch.bfe.rohrleitungsanlagen.legalprovision')}</td>
    % if c['attributes']['legalprovision'].startswith('http'):
       <td><a target ="_blank" href="${c['attributes']['legalprovision']}">${_('link')}</a></td>
    % else:
      <td>-</td>
    % endif

  </tr>
</%def>
